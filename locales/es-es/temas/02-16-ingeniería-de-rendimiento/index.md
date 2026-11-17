# 2.16 Ingeniería de rendimiento

## Visión general y motivación

La ingeniería de rendimiento es la disciplina de lograr que el código sea lo bastante rápido, de forma deliberada, a través de la medición y no de la intuición. Este capítulo opera a nivel de código y de componentes: funciones, bucles, estructuras de datos, consultas, asignaciones de memoria y la manera en que un servicio concreto destina su tiempo. Es el complemento del capítulo 3.5, que aborda el rendimiento a nivel de sistema (escalado horizontal, equilibrado de carga, capacidad y resiliencia). Cuando un sistema es lento, el capítulo 3.5 pregunta cuántas máquinas se necesitan; este capítulo pregunta por qué una sola máquina está haciendo tanto trabajo en primer lugar. En la mayoría de los casos se necesitarán ambos enfoques, y es a nivel de código donde se esconde, en realidad, una parte sorprendente del coste y la latencia.

Para equipos grandes, esta disciplina es esencial porque el rendimiento se degrada en silencio. Ningún *commit* individual hace que un servicio se ralentice, pero mil pequeñas contribuciones, cada una añadiendo una consulta a la base de datos o un bucle sin límite, sí lo lograrán. Sin un método compartido para medir, presupuestar y controlar el rendimiento, solo se descubre la putrefacción cuando un cliente se queja o un lanzamiento se derrite. Un método convierte el rendimiento de una heroica extinción de incendios en una propiedad rutinaria que se protege.

Para las empresas, el rendimiento es dinero: código más rápido significa menos máquinas, facturas de nube más bajas y la capacidad de cumplir un [acuerdo de nivel de servicio](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) en materia de latencia sin sobredimensionar la infraestructura. Para los gobiernos, el rendimiento es acceso: una página que carga en un teléfono antiguo sobre una conexión móvil débil marca la diferencia entre que un ciudadano complete la solicitud de una prestación o que desista. Los sistemas públicos también requieren evidencia de *benchmarks* reproducible, porque los organismos de contratación y supervisión exigirán que se demuestren los números, no que se asienten como simples afirmaciones.

## Principios clave

- **Mida antes de optimizar.** El cuello de botella casi nunca está donde se imagina. Perfile, luego actúe.
- **Evite la optimización prematura.** El aviso de Donald Knuth sigue vigente: optimizar código que no importa cuesta claridad y no aporta nada.
- **Defina «lo bastante rápido» como un número.** Un presupuesto de rendimiento con un objetivo y un percentil convierte la opinión en un veredicto claro: se cumple o no se cumple.
- **Las medias engañan; los percentiles dicen la verdad.** La cola (p99) es lo que los usuarios sienten, no la media.
- **Las mejoras algorítmicas superan al microajuste.** Una clase de complejidad mejor supera a cualquier cantidad de ingenio en el factor constante.
- **Latencia y caudal son objetivos distintos.** Mejorar uno puede empeorar el otro; sepa cuál está persiguiendo.
- **El *benchmarking* honesto o nada.** El calentamiento previo, la varianza y una carga de trabajo representativa separan los números reales de la ficción.
- **Frene el rendimiento en CI y obsérvelo en producción.** Las regresiones detectadas antes del *merge* son baratas; las detectadas por los usuarios, carísimas.

## Recomendaciones

### Mida primero y perfile antes de tocar una línea

La regla más antigua de este campo es la más ignorada: identifique el cuello de botella antes de optimizar. Busque un [perfilador](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), una herramienta que muestree o instrumente un programa en ejecución para mostrar dónde gasta tiempo y memoria. Perfile el CPU (qué funciones consumen ciclos), la memoria y las asignaciones (qué se asigna y con qué frecuencia, porque la rotación de asignaciones provoca las pausas de la [recogida de basura](https://en.wikipedia.org/wiki/Garbage_collection)), y la E/S (tiempo perdido esperando al disco, la red o la base de datos). Un [gráfico de llamas](https://en.wikipedia.org/wiki/Flame_graph), una visualización apilada en la que cada rectángulo representa una función y su ancho el tiempo dedicado, hace que el coste dominante sea evidente de un vistazo: busque los rectángulos más anchos, no las pilas de llamadas más profundas. Optimice primero el mayor coste, remida y deténgase al alcanzar el presupuesto. Esto se conecta con las prácticas de observabilidad del capítulo 9.2, porque un perfil de producción supera cualquier suposición hecha desde un portátil.

Guárdesese también del error opuesto. La frase completa de Knuth es que la optimización prematura es la raíz de mucho mal, y se refería a las pequeñas ineficiencias que tientan a sacrificar código legible por una velocidad imaginaria. Escriba primero la versión clara, mida y optimice solo el código que el perfilador señala con dedo acusador.

### Defina qué significa «lo bastante rápido» con presupuestos de rendimiento

La velocidad no es una virtud en el vacío; es un objetivo que se cumple o se incumple. Fije un **presupuesto de rendimiento**: un límite concreto como «la latencia p99 del proceso de compra por debajo de 300 ms» o «esta *endpoint* asigna menos de 1 MB por solicitud». Átelo a algo que los usuarios o el negocio sientan, y expreselo como **percentil**, no como media, porque la media oculta la cola lenta donde viven los usuarios reales. Si el 1 % de las solicitudes tardan 5 segundos, la media puede parecer aceptable mientras una fracción considerable de clientes sufre. Los presupuestos dotan al equipo de una definición compartida e inapelable de «terminado» y de una línea que una regresión cruza de forma visible.

### Priorice la eficiencia algorítmica antes que el microajuste

Las mayores y más baratas ganancias provienen de la [eficiencia algorítmica](https://en.wikipedia.org/wiki/Algorithmic_efficiency), cómo crece el trabajo a medida que crece la entrada, descrita con la [notación Big O](https://en.wikipedia.org/wiki/Big_O_notation) (un método para clasificar la tasa de crecimiento, de modo que un ordenamiento en O(n log n) escala mucho mejor que uno en O(n²)). Un bucle anidado que es invisible con diez elementos se convierte en una catástrofe con diez mil. Antes de retocar a mano una función crítica, pregúntese si está haciendo un trabajo fundamentalmente excesivo: una consulta N+1 accidental, una búsqueda lineal que debería ser una búsqueda por hash, o un trabajo repetido que podría memoizarse. Esto se vincula con los fundamentos algorítmicos del capítulo 2.13. Ninguna cantidad de ajuste en el factor constante rescatará una clase de complejidad equivocada.

### Distinga latencia de caudal y respete la cola

La **latencia** es cuánto tarda una operación individual; el **caudal** es cuántas operaciones se completan por unidad de tiempo. No son el mismo objetivo, y optimizar uno puede perjudicar al otro. El procesamiento por lotes mejora el caudal pero añade latencia al primer elemento del lote; añadir trabajadores en paralelo eleva el caudal pero puede empeorar la latencia de cola por la contención. Decida cuál de los dos necesitan realmente sus usuarios. Y vigile siempre la cola: la latencia p95 y p99, el 5 % y el 1 % de solicitudes más lentas, porque a escala un usuario realiza muchas solicitudes y cae en la cola con frecuencia. Informe percentiles, genere alertas sobre ellos y presupuéstelos.

### Conozca los límites del paralelismo

Cuando paralelice, recuerde la [Ley de Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): la aceleración que aporta añadir procesadores está limitada por la fracción del trabajo que debe ejecutarse en serie. Si el 10 % de una tarea es inherentemente secuencial, por muchas que sean las núcleos no se superará una aceleración de 10×. La concurrencia (estructurar el trabajo para que las tareas puedan avanzar de forma independiente) y el paralelismo (ejecutarlas realmente a la vez) introducen una complejidad real, desde condiciones de carrera hasta sobrecostes de coordinación. Mida la fracción secuencial antes de dar por hecho que más hilos le ahorrarán tiempo, y sea honesto: la versión correcta y más simple a menudo es lo bastante rápida.

### Utilice caché y localidad de datos, y respete sus costes

Una [caché](https://en.wikipedia.org/wiki/Cache_(computing)), un almacén rápido de resultados recientemente o costosamente calculados, es la herramienta de rendimiento más poderosa que tiene y también la más peligrosa. La réplica de Phil Karlton, de que los dos problemas más difíciles de la informática son la invalidación de caché y el nombrado de cosas, es un aviso: una caché obsoleta sirve respuestas erróneas, y la lógica de invalidación es donde se crían los errores más sutiles. Ponga caché de forma deliberada, fije expiraciones y conozca su historia de corrección antes de optimizar la tasa de aciertos. Al nivel más bajo, la [localidad de referencia](https://en.wikipedia.org/wiki/Locality_of_reference), mantener juntos en memoria los datos que se usan juntos, aprovecha la jerarquía de caché de la CPU y puede acelerar el código varias veces sin ningún cambio algorítmico, convirtiendo los fallos de caché en aciertos. Por esta razón, los arrays contiguos superan a las estructuras con persecución de punteros. Esto se cruza con las decisiones de disposición de datos del capítulo 3.4.

### Realice *benchmarks* honestos y desconfíe de los micro*benchmarks*

Un *benchmark* que miente es peor que ninguno, porque da una falsa seguridad. Caliente antes de medir, para cronometrar el comportamiento en estado estable y no la inicialización de una sola vez ni la compilación *just-in-time*. Ejecute muchas iteraciones e informe la varianza, no un único número afortunado. Use una carga de trabajo representativa con tamaños de datos y distribuciones realistas, porque un micro*benchmark* sobre una entrada trivial suele medir la capacidad del compilador para eliminar la prueba en lugar de la velocidad real del código. Tenga cuidado con las trampas clásicas: un valor que el optimizador demuestra que es inactivo y elimina, un bucle que el entorno de ejecución sube al nivel superior, o una caché que está caliente en el *benchmark* y fría en producción. En caso de duda, mida el camino completo, no la función aislada.

### Controle el rendimiento en CI y obsérvelo en producción

Haga del rendimiento una propiedad que la *pipeline* proteja. Añada pruebas de rendimiento a la estrategia del capítulo 2.4, con puertas de regresión que fallen la construcción cuando un *benchmark* clave o un presupuesto se deteriore más allá de un umbral. Esto captura el enlentecimiento progresivo antes de que se fusioné. Después, cierre el ciclo en producción con la telemetría del capítulo 9.2: rastre percentiles de latencia reales, tasas de asignación y consultas lentas en comparación con los presupuestos, porque el tráfico de producción encuentra los casos que los *benchmarks* nunca imaginaron.

## Compromisos: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Optimizar ahora, por intuición | Se productivo; alguna victoria afortunada | Generalmente ajusta el código equivocado; añade complejidad sin ganancia |
| Medir primero y luego optimizar | Apunta al cuello de botella real; basado en evidencia | Requiere herramientas y disciplina; arranque más lento |
| Uso de caché | Grandes ganancias en latencia y caudal | Errores de invalidación; datos obsoletos; coste de memoria |
| Más paralelismo | Mayor caudal en trabajo paralelo | Techo de Amdahl; contención; errores de concurrencia |
| Microoptimización | Exprime factores constantes | Techo bajo; daña la legibilidad; a menudo es ruido |
| Mejora algorítmica | Las ganancias escalan con el tamaño de la entrada | Requiere análisis; a veces implica una reescritura mayor |
| Puertas de rendimiento en CI | Frena las regresiones temprano y a bajo coste | Los *benchmarks* inestables erosionan la confianza; requiere un entorno estable |

La tensión central es entre el esfuerzo y el rendimiento, y su resolución es la medición. El trabajo de rendimiento tiene rendimientos fuertemente decrecientes: el primer ajuste guiado por el perfil puede reducir la latencia a la mitad, el décimo puede esquilmar un uno por ciento mientras duplica la complejidad del código. Se resuelve negándose a optimizar sin un número en la mano y un presupuesto que cumplir. Mida para encontrar la reparación que merece la pena, y deténgase en el momento en que se supere el presupuesto en lugar de perseguir la velocidad por sí misma.

## Preguntas para debatir con su equipo

1. **¿Tienen un presupuesto de rendimiento escrito para sus caminos críticos, y está expresado como percentil?** Muchos equipos tienen una vaga sensación de que las cosas deberían ser «rápidas», pero no existe un número contra el que alguien pueda fallar, lo que significa que el rendimiento no es responsabilidad de nadie hasta que algo se rompe. Un presupuesto como «p99 por debajo de 300 ms» hace que el objetivo sea concreto, da a los revisores algo que hacer cumplir y convierte una regresión en un evento visible en lugar de una deriva silenciosa. Es más importante en equipos grandes, donde la latencia se introduce a través de muchas manos y ningún autor individual percibe el coste acumulativo. Presenten los datos de latencia actuales y pregunten si informan con medias, que halagan, o con percentiles, que dicen la verdad. Si no pueden expresar «lo bastante rápido» como un número, ese es el primer punto a resolver.

2. **¿La última vez que optimizaron algo, un perfilador les indicó dónde mirar o se guiaron por corazonada?** El cuello de botella está, célebremente, en otro lugar del que los ingenieros con experiencia imaginan, y el tiempo dedicado a ajustar el código equivocado se pierde dos veces: una en el trabajo y otra en la complejidad añadida. Una cultura que perfile primero invierte su esfuerzo donde rinde y deja el código claro en paz. Pidan a su equipo que recuerde los tres últimos ajustes de rendimiento y si cada uno partió de una medición o de una intuición. Consideren si pueden perfilar en producción, o al menos en un entorno de preproducción realista, porque un perfil de portátil puede inducir al error con facilidad. La respuesta revela si su trabajo de rendimiento es ingeniería o folclore.

3. **¿Qué impide hoy que una regresión de rendimiento llegue a producción?** En un equipo en crecimiento, la respuesta honesta suele ser «la queja de un cliente», lo que significa que los usuarios son su prueba de regresión. Una puerta en CI que falla la construcción cuando un *benchmark* o un presupuesto se deteriora capta el problema mientras es barato corregirlo y el autor aún recuerda el cambio. Discutan si sus *benchmarks* son lo bastante estables para servir de puerta, porque una prueba de rendimiento inestable que alarma sin razón será ignorada o desactivada. Hablen también de lo que vigilan en producción, ya que algunas regresiones solo aparecen bajo tráfico y datos reales. El objetivo es que el rendimiento sea una propiedad que el sistema defiende de forma automática, no una que se redescubre en un incidente.

4. **¿Optimizan para latencia o para caudal en cada camino crítico, y lo ha escrito alguien?** Son objetivos distintos que tiran en direcciones opuestas: el procesamiento por lotes y los trabajadores en paralelo elevan el caudal pero pueden añadir latencia a las solicitudes individuales, de modo que un equipo que optimiza por instinto a menudo compra el eje equivocado y hace esperar a los usuarios para ahorrar tiempo de máquina del que no escaseaba. En un equipo grande el peligro se multiplica, porque un grupo ajusta un servicio compartido para el caudal por lotes mientras otro depende de él para la latencia interactiva, y ninguno conoce el objetivo del otro. Presenten el patrón de uso real de cada camino (solicitud interactiva frente a lote de fondo), la latencia percentil actual y el caudal sostenido que necesitan, y decidan el eje explícitamente en lugar de dejar que un valor predeterminado se imponga. En un sistema empresarial o gubernamental sujeto a un SLA, nombren la métrica contra la que está redactado el acuerdo, porque optimizar el eje no medido puede incumplir un contrato mientras los paneles de control parecen saludables.

5. **¿Cómo sepan que sus *benchmarks* miden trabajo real y no el optimizador eliminando su prueba?** Un *benchmark* que miente es peor que ninguno, porque entrega al equipo una falsa confianza y después una regresión se despliega igualmente. Los equipos suelen informar un único número afortunado de una ejecución en frío sobre una entrada trivial, lo que mide la inicialización, la compilación *just-in-time* y la capacidad del compilador de eliminar código inactivo en lugar del comportamiento que los usuarios realmente encuentran. Presenten un *benchmark* de ejemplo y sométanlo a interrogatorio: ¿incluye calentamiento previo, ejecuta muchas iteraciones, informa la varianza, usa tamaños de datos y distribuciones representativas y neutraliza la eliminación de código muerto en su resultado? La tensión contraria es que los *benchmarks* honestos son más lentos de escribir y ejecutar que los micro*benchmarks* rápidos, así que acuerden dónde las aproximaciones baratas son aceptables y dónde exigen rigor. En un entorno público o regulado donde los organismos de contratación y supervisión exigirán reproducir los números, capturen el dispositivo, la carga de trabajo y el entorno junto con el resultado, para que la afirmación pueda verificarse y no simplemente asentirse.

6. **¿Cuando el trabajo de rendimiento compite con las funcionalidades por los mismos ingenieros, cómo se decide y quién detenta la autoridad sobre el presupuesto?** El rendimiento tiene rendimientos fuertemente decrecientes, así que el primer ajuste guiado por el perfil puede reducir la latencia a la mitad mientras el décimo esquila un uno por ciento al doble de complejidad, y sin una regla la voz más ruidosa o el plazo más urgente gana. Las consideraciones contrarias son reales: la deuda de rendimiento sin resolver se compone en silencio y encarece el refit posterior, pero perseguir la velocidad más allá del presupuesto desangra la hoja de ruta y añade complejidad que frena el trabajo futuro. Presenten el estado actual del presupuesto de cada camino crítico, el coste estimado del statu quo en máquinas o en conversión perdida, y el beneficio marginal de la próxima optimización, para que la decisión se tome con evidencia y no con presión. En un programa empresarial o gubernamental a gran escala, nombren quién es el responsable del presupuesto de rendimiento y quién puede autorizar la inversión de tiempo de ingeniería contra él, porque un objetivo del que nadie es responsable de defender se erosiona en silencio.

## Lente por sector

**Startup.** La velocidad de entrega va por delante del proceso, así que resístanse a las reescrituras y a los marcos de rendimiento grandilocuentes. Dedicen una tarde a un perfilador en el camino por el que los usuarios realmente se quejan, resuelvan el mayor coste (a menudo una consulta N+1 o una búsqueda lineal accidental) y añadan un presupuesto percentil ligero a CI para que la ganancia no se deteriore en silencio. Reserven la optimización profunda para el momento en que un número real, no una corazonada, diga que el código es demasiado lento.

**Pequeña empresa.** Sin especialista en rendimiento y con un presupuesto ajustado, apóyense en las herramientas que ya pagan: el perfilador de su entorno de ejecución, los percentiles de latencia del panel de su proveedor de *hosting* y el analizador de consultas integrado en su base de datos. Fijen uno o dos presupuestos claros atados a algo que los clientes sientan, como el tiempo de carga de una página o el de una compra, y traten una infracción como una señal para contratar una capa de servicio más rápida o arreglar la peor consulta en lugar de iniciar un proyecto de ajuste que no pueden dotar de personal.

**Empresa.** A escala de flota, el rendimiento es coste directo, así que góbernése como una disciplina compartida: herramientas de perfilado estandarizadas, presupuestos percentil atados a métricas de negocio y puertas de regresión en CI aplicadas de forma consistente para que el enlentecimiento silencioso de un solo equipo no hinche la factura de nube de todos. Rastre latencia, asignación y caudal frente a líneas de base entre servicios, y conserven evidencia de *benchmarks* reproducible, porque una reducción del 30 % en el CPU de una flota grande es un ahorro recurrente que merece auditoría y defensa frente a penalizaciones de SLA.

**Gobierno.** El rendimiento es una garantía de acceso: una página que carga en un teléfono antiguo sobre una conexión rural lenta determina si un ciudadano completa una solicitud de prestación. Fijen presupuestos explícitos contra dispositivos de gama baja y redes limitadas, y publiquen resultados de *benchmarks* reproducibles que capturen el dispositivo, la red y la carga de trabajo, para que los organismos de supervisión y las auditorías de accesibilidad puedan verificar los números en lugar de tomarlos como fe. Prefieran la medición transparente y auditable frente a las afirmaciones de los proveedores, y exijan a los suministradores la misma evidencia reproducible.

## Ejemplos

**Startup.** Un pequeño equipo de SaaS nota que su panel se siente perezoso y se tienta a reescribirlo en un marco más rápido. En lugar de eso, dedican una tarde a un perfilador y un gráfico de llamas, que revela que el 70 % del tiempo de la solicitud lo consume una única *endpoint* que emite una consulta a la base de datos por cada fila, el clásico patrón N+1. Lo reemplazan por una consulta loteada: la latencia cae de 1,2 segundos a 90 milisegundos, y añaden un presupuesto p99 de 200 ms a un *benchmark* ligero en CI para que la reparación no se deteriore en silencio. Sin reescritura, una tarde, una decuplicación de la velocidad.

**Empresa.** Una plataforma de comercio electrónico ejecuta miles de instancias y su factura de nube la domina un servicio de recomendaciones. Una campaña de perfilado revela una intensa rotación de asignaciones que provoca frecuentes pausas de recogida de basura, sumada a una caché con un bajo índice de aciertos. Ajustar las estructuras de datos para la localidad y corregir las claves de caché reduce el CPU por solicitud un 40 %, lo que permite al equipo gestionar el mismo tráfico con un 40 % menos de máquinas. El ahorro se amortiza el esfuerzo de ingeniería en cuestión de semanas, y un SLA de latencia p99 que antes se incumplía de vez en cuando ahora se sostiene con comodidad, evitando penalizaciones contractuales.

**Gobierno.** Un organismo nacional de tributación debe atender a ciudadanos con dispositivos antiguos y conexiones rurales lentas. El equipo fija un presupuesto explícito: la página de declaración debe ser interactiva en menos de 3 segundos en un teléfono de gama baja sobre un perfil 3G limitado. Perfilan la página, reducen el trabajo que bloquea la interactividad y publican resultados de *benchmarks* reproducibles, capturando el dispositivo, la red y la carga de trabajo, para que los organismos de supervisión y los auditores de accesibilidad puedan verificar la afirmación en lugar de tomarla como fe. El rendimiento aquí no es una palanca de coste, sino una garantía de acceso que mantiene el servicio usable para todos.

## Caso de negocio: motivaciones, ROI y coste total de propiedad

El retorno de la ingeniería de rendimiento aparece en tres contabilidad. La primera es el coste de infraestructura: código más rápido realiza el mismo trabajo en menos máquinas, y para una flota grande una reducción del 30 % en el CPU es un ahorro recurrente y directo que eclipsa el esfuerzo de ingeniería de una sola vez. La segunda es la ingresos y la satisfacción: la latencia se correlaciona con la conversión, el abandono y la confianza del usuario, de modo que reducir la cola es una palanca de crecimiento, no solo una tarea de higiene. La tercera es el riesgo evitado: un incumplimiento de SLA conlleva penalizaciones, y un lanzamiento que colapsa bajo carga conlleva daño reputacional y coste de extinción.

El coste total de propiedad es modesto y concentrado al inicio. Se invierte en herramientas de perfilado, un entorno de *benchmarking* estable y puertas de CI, junto con la disciplina de redactar presupuestos y leer perfiles. El mayor coste, el oculto, es la alternativa: la deuda de rendimiento se compone en silencio, y refit la velocidad en un sistema ya lento tras el lanzamiento es muy más caro que protegerla de forma continua. Presenten el caso a la dirección en sus propias unidades. Traduzcan la latencia en conversión o en tasas de completitud del ciudadano, traduzcan el CPU en gasto mensual de nube y traduzcan una puerta de regresión en incidentes evitados. El argumento más sólido es que el rendimiento es barato de proteger *commit* a *commit* y ruinoso de recuperar una vez que se ha corroído.

## Antipatrónos y trampas

- **Optimizar sin perfi.** Ajustar código que no es el cuello de botella mientras el coste real sigue sin atender.
- **Optimización prematura.** Sacrificar la claridad por una velocidad imaginada que el perfilador nunca habría señalado.
- **Informar con medias.** Ocultar una cola dolorosa detrás de una media confortable; los usuarios sienten la p99, no la media.
- **Teatro de micro*benchmarks*.** Números de una carga trivial que el optimizador eliminó a medias, sin calentamiento ni varianza informados.
- **Caché sin historia de invalidación.** Perseguir la tasa de aciertos mientras se sirven datos obsoletos o incorrectos.
- **Suponer que más hilos ayudan.** Ignorar la Ley de Amdahl y la fracción secuencial, y acabar ahogados en contención.
- **Ausencia de puerta de regresión.** Dejar que los usuarios sean la prueba de rendimiento porque nada en CI vigila el presupuesto.
- **Optimizar el eje equivocado.** Comprar caudal con lotes cuando los usuarios necesitaban baja latencia, o viceversa.

## Modelo de madurez

- **Nivel 1, Iniciar:** El rendimiento solo se atiende cuando algo se rompe. No hay presupuestos, no hay hábito de perfilado, no hay *benchmarks*. La optimización es un acto de fe guiado por la intuición, y las medias son la única métrica que nadie informa.
- **Nivel 2, Desarrollar:** Algunos equipos perfilan durante los incidentes y conservan unos pocos *benchmarks*, pero la práctica es inconsistente y depende del entusiasmo individual. Los presupuestos existen de forma informal para uno o dos caminos críticos, y los percentiles aparecen en algunos paneles, pero nada frena una regresión antes de que se despliegue y cada equipo reinventa su propio enfoque.
- **Nivel 3, Estandarizar:** Los caminos críticos cuentan con presupuestos percentil escritos, y el perfilado es el primer paso documentado y esperado antes de que nadie optimice. La CI incluye pruebas de rendimiento con puertas de regresión, las reglas de *benchmarking* honesto (calentamiento previo, varianza, datos representativos) están redactadas y se aplican a nivel de organización, y cada equipo sigue el mismo método en lugar del propio.
- **Nivel 4, Gestionar:** La organización mide el rendimiento como una propiedad controlada. Los percentiles de latencia, el caudal, las tasas de asignación y el conteo de consultas lentas se rastrean frente a líneas de base explícitas en producción y en CI, las regresiones se cuantifican contra umbrales en lugar de discutirse, y los presupuestos están atados a métricas de negocio como la conversión o el gasto de nube, de modo que una infracción desencadena una decisión basada en datos. La evidencia de *benchmarks* es reproducible y se captura junto con el dispositivo, la carga de trabajo y el entorno para auditoría.
- **Nivel 5, Orquestar:** El rendimiento se mejora de forma continua y se integra en toda la organización. Los presupuestos, el perfilado, el *benchmarking* honesto y el análisis de gráficos de llamas son habilidades habituales, las puertas de regresión son estables y gozan de confianza, y los datos de producción y CI cierran el ciclo de forma automática. La organización adapta los presupuestos a medida que cambian el tráfico, el hardware y las prioridades de negocio, reequilibra el esfuerzo hacia los caminos donde el retorno es mayor y defiende el rendimiento como una propiedad permanente y no como una campaña periódica.

## Ideas para la reflexión

1. ¿Cuál de sus caminos críticos cuenta hoy con un presupuesto escrito y basado en percentiles, y cuáles solo están protegidos por la esperanza?
2. ¿Cuándo un perfilador los sorprendió por última vez, y qué les enseñó sobre dónde suponen que va el tiempo?
3. ¿Sus *benchmarks* incluyen calentamiento previo, informan varianza y usan datos representativos, o están midiendo al optimizador?
4. ¿Dónde están gastando máquinas para tapar un código que una campaña de perfilado podría abaratar?
5. Para su carga de trabajo más paralelizada, cuál es la fracción secuencial y limita la Ley de Amdahl la aceleración que persiguen?
6. Si un compañero fusionara un cambio que duplicara la latencia p99, cuánto tardaría alguien en notarlo y cómo lo descubriría?

## Ideas clave

- Mida antes de optimizar; el cuello de botella rara vez está donde se imagina, y la optimización prematura cuesta claridad sin ganancia.
- Defina «lo bastante rápido» como un presupuesto percentil, porque las medias ocultan la cola donde viven los usuarios reales.
- Prefiera las mejoras algorítmicas (una clase de complejidad Big O mejor) al microajuste, y sepa si necesita latencia o caudal.
- Respete los límites del paralelismo (Ley de Amdahl) y los riesgos de la caché (invalidación y obsolescencia).
- Realice *benchmarks* honestos con calentamiento previo, varianza y cargas de trabajo representativas, y desconfíe de los micro*benchmarks*.
- Controle el rendimiento en CI (capítulo 2.4) y obsérvelo en producción (capítulo 9.2); complemente la visión a nivel de sistema del capítulo 3.5.
- El rendimiento es coste para las empresas, acceso para los gobiernos, y es barato de proteger de forma continua pero caro de recuperar.

## Referencias y lectura adicional

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (perfilado, gráficos de llamas y método).
- Brendan Gregg, *BPF Performance Tools* (observabilidad y perfilado práctico en Linux).
- Donald E. Knuth, «Structured Programming with go to Statements» (*ACM Computing Surveys*, 1974): el origen de la máxima sobre la optimización prematura.
- Donald E. Knuth, *The Art of Computer Programming* (análisis algorítmico y complejidad).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest y Clifford Stein, *Introduction to Algorithms* (notación Big O y eficiencia algorítmica).
- Gene M. Amdahl, «Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities» (1967): el origen de la Ley de Amdahl.
- Ulrich Drepper, «What Every Programmer Should Know About Memory» (la jerarquía de memoria y la localidad de datos).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latencia, caudal y comportamiento de cola en sistemas).
- Aleksey Shipilev, «JMH y las trampas del micro*benchmarking*» (práctica honesta de *benchmarking* en entornos gestionados).
- Ilya Grigorik, *High Performance Browser Networking* (rendimiento de red y del lado del cliente para usuarios de baja banda).

