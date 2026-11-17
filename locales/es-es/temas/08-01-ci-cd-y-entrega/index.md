# 8.1 CI/CD y entrega

## Presentación y motivación

La [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) y la [entrega continua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) son el tejido conectivo entre escribir código y ponerlo frente a los usuarios con seguridad. La integración continua significa que cada cambio se fusiona frecuentemente en una línea principal compartida, luego se construye y prueba automáticamente, para que los problemas de integración aparezcan en minutos en lugar de al final de un ciclo de lanzamiento largo. La entrega continua significa que cada cambio que pasa el canal se mantiene en un estado desplegable, para que lanzar a producción se convierta en una decisión de negocio en lugar de una carrera de ingeniería. El [despliegue continuo](https://en.wikipedia.org/wiki/Continuous_deployment) va un paso más allá y libera automáticamente cada cambio que pasa, sin una puerta humana.

Para los equipos grandes, estas distinciones importan enormemente. Cuando cientos de ingenieros hacen commits a sistemas superpuestos, el costo de la integración manual y las pruebas manuales crece de forma no lineal. Un canal compartido y automatizado es la única manera práctica de dar a muchos colaboradores retroalimentación rápida y confiable y de evitar que el cambio de un equipo rompa silenciosamente el de otro. El canal se convierte en la fuente única de verdad sobre si el software está saludable, y aplica una consistencia que ninguna cantidad de documentación o buenas intenciones puede garantizar a escala.

Los contextos empresariales y gubernamentales añaden una dimensión más: la auditabilidad y el control de cambios. Los reguladores, los oficiales de seguridad, y los auditores necesitan evidencia de que los cambios fueron revisados, probados, y aprobados, y de que el artefacto que se ejecuta en producción es exactamente el que se construyó y verificó. Un canal de CI/CD bien diseñado convierte estas obligaciones de cumplimiento de una carga de papeleo en un subproducto automático del flujo de trabajo de ingeniería normal. Bien hecho, la entrega se vuelve más rápida y más segura al mismo tiempo, que es el resultado que más importa al liderazgo.

*Véase también:* el capítulo 8.4 (ingeniería de plataforma y experiencia del desarrollador), el capítulo 8.5 (automatización de pruebas y procesos), y el capítulo 7.4 (analítica de producto y experimentación) para las [banderas de función](https://en.wikipedia.org/wiki/Feature_toggle) (interruptores en tiempo de ejecución que exponen funcionalidad a los usuarios sin redesplegar) y las prácticas de experimentación que habilita la entrega progresiva (liberar un cambio gradualmente mientras se monitorean automáticamente sus métricas de salud).

## Principios fundamentales

- Integra cambios pequeños frecuentemente; las ramas de larga vida son el enemigo de la integración continua.
- Construye el artefacto una vez y promueve el artefacto idéntico a través de cada entorno.
- Haz del canal la puerta autoritativa: si está verde, el cambio es enviable; si está rojo, el trabajo se detiene hasta arreglarlo.
- Optimiza sin descanso para la retroalimentación rápida para que los desarrolladores se mantengan en flujo y los defectos se atrapen mientras el contexto está fresco.
- Automatiza todo lo que se repite, incluyendo pruebas, escaneos de seguridad, aprovisionamiento, y despliegue.
- Trata las definiciones de canal como código bajo control de versiones sujeto a revisión, no como configuración de consola clicable.
- Diseña para lanzamientos seguros y reversibles para que cualquier despliegue pueda deshacerse rápidamente.
- Separa el despliegue (instalar el código) del lanzamiento (exponerlo a los usuarios) usando banderas de función.

## Recomendaciones

### Diseña el canal como una serie de puertas de calidad

Estructura el canal en etapas que progresan de baratas y rápidas a costosas y exhaustivas: primero la compilación y las pruebas unitarias, luego las pruebas de integración, el escaneo de seguridad y licencias, y finalmente el despliegue a staging y producción. Cada etapa es una puerta que un cambio debe pasar. Ordena las puertas para que las comprobaciones más rápidas y con mayor probabilidad de fallar corran primero, lo cual da a los desarrolladores retroalimentación en el menor tiempo posible. Mantén el bucle de retroalimentación de la etapa de commit por debajo de diez minutos donde puedas. Más allá de eso, los desarrolladores cambian de contexto y la productividad cae.

### Construye una vez, promueve en todas partes

Produce un único artefacto inmutable en la etapa de construcción y promueve ese artefacto exacto a través de prueba, staging, y producción. Nunca reconstruyas por entorno, porque una reconstrucción puede introducir silenciosamente diferencias. La configuración que varía por entorno debería inyectarse en el momento del despliegue, no incrustarse en construcciones separadas. Esta práctica también es lo que te permite decirle a un auditor, con certeza, que el binario en producción es el que pasó cada puerta.

### Haz del canal el punto de aplicación de la política

Codifica las comprobaciones requeridas (aprobación de revisión de código, umbrales de cobertura de pruebas, resultados de escaneo de seguridad, commits firmados) directamente en el canal y las reglas de protección de ramas. La política manual que vive en una wiki se salta rutinariamente bajo presión de plazo. La política codificada en el canal se aplica uniforme y automáticamente a cada cambio.

### Mantén la línea principal siempre lanzable

Usa el desarrollo basado en tronco, que integra todo el trabajo en una única rama compartida con pocas o ninguna rama de larga vida, o usa ramas de función de vida corta, y confía en las banderas de función para ocultar el trabajo incompleto en lugar de ramas de larga vida. Esto mantiene los conflictos de fusión pequeños y mantiene la línea principal siempre en un estado desplegable, que es la precondición para la entrega continua genuina.

### Elige las estrategias de despliegue deliberadamente

Ajusta la estrategia de despliegue al riesgo y radio de impacto del servicio:

- Los despliegues **rodantes** reemplazan las instancias gradualmente y son un valor predeterminado sensato para los servicios sin estado.
- **[Azul-verde](https://en.wikipedia.org/wiki/Blue-green_deployment)** mantiene dos entornos idénticos y cambia el tráfico todo de una vez, dando una ruta de reversión instantánea.
- Los lanzamientos **canario** enrutan un pequeño porcentaje del tráfico a la nueva versión, vigilan las métricas de salud, y se expanden solo si las señales son buenas.
- Las **banderas de función** desacoplan el lanzamiento del despliegue, permitiéndote habilitar funcionalidad para usuarios o cohortes específicos sin redesplegar.

### Adopta la entrega progresiva con reversión automatizada

La entrega progresiva combina los lanzamientos canario con el análisis automatizado de métricas como la tasa de error, la latencia, y la saturación. Define criterios de salud objetivos por adelantado, luego deja que el sistema promueva o revierta automáticamente según esas señales. La reversión automatizada elimina la vacilación humana que convierte un pequeño incidente en uno mayor.

### Provee gestión de lanzamientos y control de cambios para entornos regulados

En entornos regulados, mantén un registro de gestión de cambios ligero pero real. Captura automáticamente quién aprobó cada cambio, qué pruebas se ejecutaron, y qué artefacto se desplegó. Usa procesos de consejo asesor de cambios para los cambios genuinamente de alto riesgo, pero resérvalos para esos casos. Enrutar cada cambio rutinario a través de una junta semanal destruye el valor de la automatización. Apunta en cambio a tipos de cambio estándar preaprobados que fluyan a través del canal sin ceremonia.

## Ventajas y desventajas

| Enfoque | Ventajas | Desventajas | Mejor ajuste |
|---|---|---|---|
| Entrega continua (puerta de lanzamiento manual) | El negocio controla el momento; fuerte para ventanas de lanzamiento reguladas | Requiere disciplina para mantener lanzable la línea principal | Empresas con ventanas de cambio |
| Despliegue continuo (totalmente automático) | Retroalimentación más rápida; lotes más pequeños | Exige pruebas y observabilidad maduras | Equipos de alta confianza y alta frecuencia |
| Azul-verde | Reversión instantánea; modelo mental simple | Duplica el costo de entorno durante el cambio | Servicios críticos que necesitan revertir rápido |
| Canario + entrega progresiva | Limita el radio de impacto; basado en datos | Complejo de construir; necesita buenas métricas | Sistemas de cara al usuario a gran escala |
| Banderas de función | Desacopla el despliegue del lanzamiento | Deuda de banderas si no se limpian | Equipos que envían trabajo incompleto con seguridad |

La contrapartida central es velocidad frente a control, pero eso a menudo es una elección falsa. La automatización madura entrega ambas: los lanzamientos son más rápidos porque son más pequeños, y más seguros porque cada uno se verifica y es reversible. El costo real es la inversión por adelantado en cobertura de pruebas, observabilidad, e ingeniería de canal, más la disciplina continua para mantenerlas saludables. Las organizaciones que escatiman en esa inversión obtienen la velocidad sin la seguridad, lo cual es peor que un proceso manual lento.

## Preguntas para discutir con tu equipo

1. **¿Cuál es tu objetivo para el tiempo de retroalimentación de la etapa de commit, y qué se recorta cuando la suite supera los diez minutos?** Una etapa de commit lenta mata silenciosamente la integración continua, porque los desarrolladores dejan de esperar el verde y empiezan a agrupar cambios. Decide el número ahora (este capítulo argumenta por menos de diez minutos) y decide el mecanismo para mantenerlo: trabajadores paralelos, una pirámide de pruebas estricta, y mover las comprobaciones de integración lentas a una etapa posterior. A escala empresarial esto es una decisión de plataforma, ya que cientos de ingenieros comparten el mismo canal y cada minuto añadido se multiplica a través de cada commit. Trae datos reales a la reunión: la duración p50 y p95 actual del canal, las diez pruebas más lentas, y con qué frecuencia la gente vuelve a ejecutar en lugar de esperar. Si no puedes declarar el objetivo y defenderlo con números, tu canal está derivando hacia un proceso por lotes disfrazado de CI.

2. **¿Qué estrategia de despliegue usa cada servicio, y quién es responsable de esa elección?** Rodante, azul-verde, y canario no son intercambiables: intercambian costo, velocidad de reversión, y complejidad de forma distinta, y la elección correcta depende del radio de impacto del servicio. Azul-verde compra reversión instantánea al precio de un entorno duplicado durante el cambio, lo cual vale la pena para un sistema de pagos y es un desperdicio para un tablero interno. Canario limita la exposición pero exige buenas métricas de salud y más ingeniería de canal. Para un patrimonio grande o regulado, dejar esto al hábito de cada equipo produce inconsistencia que aparece durante un incidente, así que acuerda valores predeterminados por nivel de servicio y registra la decisión. Trae tu catálogo de servicios y etiqueta cada servicio con su estrategia, su ruta de reversión, y la persona dueña de esa decisión.

3. **¿Cómo pruebas que el artefacto en producción es exactamente el que pasó cada puerta?** Construir una vez y promover el artefacto idéntico es todo el juego para la auditabilidad, y se rompe en el momento en que alguien reconstruye por entorno o parchea una máquina en ejecución. En entornos empresariales y gubernamentales un auditor te pedirá rastrear un binario en ejecución hasta su commit, su revisión, y sus aprobaciones, y quieres que esa respuesta tome segundos, no una semana. Decide cómo lo haces cumplir: artefactos inmutables, imágenes firmadas, verificación de firma en el momento del despliegue, y configuración inyectada en el despliegue en lugar de incrustada en construcciones separadas. Trae las brechas actuales a la mesa, como cualquier etapa que reconstruya, cualquier ruta de parche manual, y cualquier lugar donde la configuración bifurque el artefacto. La respuesta determina si tu evidencia de cumplimiento es un subproducto del canal o una carrera manual antes de cada auditoría.

4. **Cuando la línea principal se pone roja, ¿qué realmente se detiene, y cómo manejas las pruebas inestables?** Un canal solo es una puerta autoritativa si una construcción roja genuinamente detiene el trabajo, sin embargo muchas organizaciones toleran silenciosamente una línea principal rota y un atraso de fallos intermitentes, lo cual entrena a los desarrolladores a volver a ejecutar hasta el verde y a enviar sobre los fallos. Para un equipo grande esta podredumbre se compone, porque el fallo intermitente ignorado de un equipo se convierte en la excusa de todos para saltarse la puerta, y la confianza en el canal es mucho más barata de mantener que de reconstruir. Pesa los impulsos en competencia: una regla estricta de detener la línea protege la calidad pero puede bloquear a cientos de ingenieros por un único mal commit, mientras una política laxa preserva el rendimiento y erosiona la puerta. Trae evidencia a la discusión: tu tiempo actual de línea principal roja, el número de pruebas en cuarentena o inestables, la tasa de reejecución, y con qué frecuencia los cambios se fusionan sobre una comprobación fallida. En entornos empresariales y gubernamentales, nombra quién es dueño del triaje de fallos intermitentes y quién tiene autoridad para congelar las fusiones, porque una puerta que nadie es responsable de hacer cumplir es una que los auditores encontrarán que se ha anulado rutinariamente.

5. **¿Cuál es tu ciclo de vida para las banderas de función, y quién es responsable de retirarlas?** Las banderas son lo que te permite separar el despliegue del lanzamiento y ocultar el trabajo incompleto, pero cada bandera es una rama en tu código que nunca se limpia sola, y las banderas sin gestionar se acumulan en complejidad condicional que nadie se atreve a tocar. En un patrimonio grande esta deuda es peligrosa, porque una bandera obsoleta puede silenciosamente bloquear una corrección de seguridad o voltear rutas de código no probadas a producción, y la persona que la creó a menudo ya se ha ido. Equilibra la tensión: las banderas te compraron entrega segura e incremental, así que la meta no son menos banderas sino un ciclo de vida disciplinado con un dueño, una expectativa de expiración, y herramientas que expongan las obsoletas. Trae el inventario actual a la reunión: cuántas banderas están vivas, cuán vieja es la más antigua, cuáles no tienen dueño, y si alguna bandera de larga vida ahora funciona como configuración permanente que pertenece a otro lugar. Para entornos regulados, añade quién puede cambiar una bandera en producción y si ese cambio se registra con el mismo rigor que un despliegue, ya que voltear una bandera es un lanzamiento incluso cuando el canal nunca se ejecuta.

6. **¿Dónde está la frontera entre la entrega continua con una puerta humana y el despliegue continuo completo, y quién fija los umbrales de reversión?** La entrega continua mantiene a una persona en control del momento del lanzamiento, lo cual conviene a ventanas de cambio estatutarias y sistemas de alto radio de impacto, mientras el despliegue continuo envía cada cambio que pasa automáticamente y exige pruebas maduras, observabilidad, y reversión automatizada para ser seguro. Para una organización grande o regulada la respuesta rara vez es uniforme: tu sitio de marketing puede desplegarse continuamente mientras tu núcleo de pagos mantiene una puerta humana documentada, y trazar esa línea por nivel de servicio previene tanto la fricción innecesaria como la automatización imprudente. Las consideraciones en competencia son la velocidad y el tamaño de lote frente al control y la auditabilidad, más el costo de ingeniería de las métricas de salud que requiere la reversión automatizada. Trae la evidencia: la tasa de fallo de cambio por servicio, el tiempo medio de recuperación, la cadencia de lanzamiento actual, y las señales objetivas (tasa de error, latencia, saturación) en las que confiarías para promover o revertir sin un humano. En entornos gubernamentales y empresariales, vincula cada nivel a quién es dueño de los umbrales de reversión y quién aprueba cualquier movimiento de un lanzamiento con puerta a la automatización completa, para que la decisión sea deliberada en lugar de a la deriva.

## Perspectiva sectorial

**Startup.** Apóyate en CI/CD gestionado desde el primer día: un ejecutor alojado, un canal, una imagen inmutable, y despliegue automático a staging al fusionar. No construyas infraestructura de canal que luego tengas que mantener. Las banderas de función permiten que dos o tres ingenieros fusionen trabajo a medio terminar con seguridad y lancen varias veces al día, y un despliegue a producción de un clic más un apagado rápido de bandera es todo el control de cambios que necesitas hasta que la escala exija más.

**Pequeña empresa.** Sin un ingeniero de plataforma o lanzamiento dedicado, favorece el canal que te da tu host de código fuente (Actions incorporado o equivalente) y su estrategia de despliegue predeterminada sobre cualquier cosa personalizada. Enmarca honestamente la elección de comprar frente a construir: un canal gestionado y una plataforma de alojamiento con reversión incorporada cuestan menos que las horas de ingeniero que consume una configuración a medida. Mantén lo esencial, que es construir una vez, promover el mismo artefacto, y una reversión fácil, y salta la maquinaria de entrega progresiva hasta que el volumen la justifique.

**Empresa.** El problema central es la consistencia entre muchos equipos: estandariza una plantilla de canal compartida que aplique revisión, escaneo, artefactos inmutables firmados, y estrategias de despliegue por nivel, para que la calidad no varíe equipo por equipo. Trata las definiciones de canal como código revisado, captura la evidencia de control de cambios automáticamente, y gestiona las banderas de función y los umbrales de reversión como activos gobernados en lugar del hábito privado de cada equipo. El beneficio es una entrega más rápida y evidencia de auditoría producida como subproducto en lugar de una carrera trimestral.

**Gobierno.** Las reglas de contratación pública, las ventanas de cambio estatutarias, y la rendición de cuentas pública moldean el canal. Prefiere la entrega continua con una puerta de lanzamiento humana documentada sobre la automatización completa para los sistemas consecuentes, clasifica el trabajo rutinario como cambios estándar preaprobados, y mantén una ruta de reversión instantánea (azul-verde o canario automatizado) para los servicios de los que dependen los ciudadanos durante ventanas anuales estrechas. Asegura que el canal registre quién aprobó cada cambio, qué pruebas se ejecutaron, y qué artefacto se desplegó, para que las obligaciones de transparencia y auditoría se cumplan por el flujo de trabajo normal en lugar de por papeleo manual.

## Ejemplos

**Startup.** Una startup SaaS de cuatro personas conecta un único canal de GitHub Actions que ejecuta pruebas unitarias, construye una imagen Docker, y despliega esa misma imagen a staging automáticamente en cada fusión a main. Un despliegue a producción es un clic, y los fundadores se apoyan en banderas de función para poder fusionar trabajo a medio terminar detrás de una bandera en lugar de mantener viva una rama durante semanas. Cuando se cuela un mal lanzamiento, apagan la bandera en segundos y lo arreglan con calma, lo cual mantiene a su equipo diminuto lanzando varias veces al día sin una persona de operaciones dedicada.

**Empresa.** Un banco global consolida docenas de trabajos de Jenkins específicos de equipo en una plantilla de canal estandarizada que hereda cada equipo de producto. La plantilla aplica análisis estático, escaneo de dependencias, y un artefacto inmutable firmado, y despliega vía canario con reversión automatizada con clave en umbrales de tasa de error y latencia. Como el mismo artefacto se promueve de prueba a producción y cada puerta se registra, los auditores del banco pueden rastrear cualquier binario de producción hasta su commit, revisión, y aprobación en segundos, reemplazando un ejercicio trimestral manual de recolección de evidencia.

**Gobierno.** Una agencia tributaria nacional que moderniza un sistema de declaración adopta la entrega continua con una puerta de lanzamiento humana explícita, así puede respetar las ventanas de cambio estatutarias durante la temporada de declaraciones. Los cambios rutinarios se clasifican como cambios estándar preaprobados que fluyen automáticamente a staging. El lanzamiento a producción requiere una única aprobación documentada que el canal registra. El despliegue azul-verde da a la agencia una ruta de reversión instantánea si un defecto llega a producción, lo cual es crítico cuando millones de ciudadanos dependen del servicio durante una ventana anual estrecha.

## Caso de negocio: motivaciones, ROI y TCO

El retorno de la inversión en CI/CD se manifiesta como un tiempo de espera reducido para los cambios, una tasa de fallo de cambio más baja, y una recuperación más rápida cuando ocurren incidentes: las métricas que la investigación vincula consistentemente tanto al rendimiento de entrega como a los resultados organizacionales. Los lanzamientos más rápidos y pequeños recortan la sobrecarga de coordinación que consume capacidad de ingeniería a escala, y la verificación automatizada recorta el trabajo costoso y desmoralizante de apagar incendios de defectos de producción.

El costo total de propiedad pesa el costo de adopción contra el costo de no adoptar. Los costos de adopción incluyen construir y mantener canales, hacer crecer la cobertura de pruebas, e invertir en observabilidad y personal de plataforma. El costo de no adoptar es mayor pero menos visible: lanzamientos manuales lentos, dolor de integración, incidentes de producción que dañan la reputación, y, en entornos regulados, auditorías fallidas y remediación. Para el liderazgo, el argumento se enmarca mejor en términos de reducción de riesgo y capacidad. La automatización convierte el escaso tiempo de ingenieros superiores de esfuerzo repetitivo de lanzamiento en trabajo de producto, mientras hace que las interrupciones sean más raras y cortas.

## Antipatrones y trampas

- **Canales copo de nieve.** Cada equipo construye a mano un canal único, así las mejoras y correcciones no pueden compartirse y la calidad varía enormemente.
- **Reconstruir por entorno.** Reconstruir para cada etapa rompe la garantía de «construir una vez» y deja que diferencias sutiles lleguen a producción.
- **Construcciones rojas ignoradas.** Tolerar una línea principal persistentemente rota destruye la confianza en el canal y normaliza enviar sobre los fallos.
- **Pruebas inestables sin atender.** Los fallos intermitentes entrenan a los desarrolladores a volver a ejecutar hasta el verde, derrotando el propósito de la puerta.
- **Teatro de aprobación manual.** Un consejo asesor de cambios que sella todo con goma añade demora sin añadir seguridad.
- **Deuda de banderas.** Las banderas de función que nunca se eliminan se acumulan en complejidad condicional inmantenible.
- **Despliegue igual a lanzamiento.** Acoplar los dos significa que cada cambio de cara al usuario requiere un redespliegue riesgoso.

## Modelo de madurez

**Nivel 1: Iniciar.** Las construcciones y los despliegues son en gran medida manuales, ad hoc, y reactivos. La integración ocurre tarde, los lanzamientos son poco frecuentes y estresantes, la reversión significa redesplegar una versión antigua a mano, y no hay una noción compartida de una puerta de canal.

**Nivel 2: Desarrollar.** Las construcciones automatizadas y las pruebas unitarias corren en cada commit, pero las prácticas varían equipo por equipo. Los despliegues están escritos como script pero todavía se disparan y supervisan manualmente, algunos entornos son consistentes, y los artefactos todavía pueden reconstruirse por etapa. Donde existe un canal, a menudo es un copo de nieve que no puede compartirse.

**Nivel 3: Estandarizar.** Una plantilla de canal documentada y estandarizada se aplica entre equipos. Promueve un único artefacto inmutable a través de todos los entornos, aplica puertas de calidad y seguridad automatizadas, codifica las comprobaciones requeridas como la aprobación de revisión y los resultados de escaneo, y captura los registros de cambio automáticamente. Las estrategias de despliegue como canario o azul-verde se eligen deliberadamente por nivel de servicio.

**Nivel 4: Gestionar.** La entrega se mide y controla contra líneas base. La organización rastrea el tiempo de espera para los cambios, la frecuencia de despliegue, la tasa de fallo de cambio, y el tiempo medio de recuperación, junto con la duración p50 y p95 del canal, las tasas de pruebas inestables y reejecución, y la antigüedad de las banderas de función. Los umbrales de reversión se fijan a partir de datos observados de tasa de error, latencia, y saturación, las puertas se aplican con base en evidencia en lugar de hábito, y cada métrica tiene un dueño que actúa cuando se desvía del objetivo.

**Nivel 5: Orquestar.** La entrega se mejora continuamente y se integra en toda la organización. La entrega progresiva con reversión automatizada impulsada por métricas es la norma, el lanzamiento se desacopla del despliegue vía banderas bien gobernadas, y la evidencia de cumplimiento se produce automáticamente como subproducto. El canal se adapta a medida que cambia el patrimonio, y las métricas de entrega alimentan la planificación de negocio y riesgo para que la inversión fluya hacia las mejoras de mayor apalancamiento.

## Ideas para el debate

- ¿Dónde está la frontera correcta entre la entrega continua con una puerta humana y el despliegue continuo completo para tus sistemas más críticos?
- ¿Cómo mantienes significativo un proceso obligatorio de gestión de cambios sin convertirlo en un teatro de sellado de goma?
- ¿Qué métricas de salud objetivas deberían gobernar la reversión automatizada, y quién es dueño de sus umbrales?
- ¿Cómo deberían los equipos de plataforma equilibrar las plantillas de canal estandarizadas contra las necesidades legítimas de equipos con requisitos inusuales?
- ¿Cuál es tu política y herramientas para retirar las banderas de función antes de que se conviertan en deuda?
- ¿Cómo mides si una entrega más rápida realmente está mejorando los resultados de negocio en lugar de solo enviar más?

## Puntos clave

- CI, CD, y el despliegue continuo son distintos; elige el nivel de automatización que coincida con tu tolerancia al riesgo y madurez.
- Construye el artefacto una vez y promueve el artefacto idéntico a través de cada entorno.
- Diseña el canal como puertas de calidad ordenadas optimizadas para retroalimentación rápida, y trátalo como la decisión de envío autoritativa.
- Elige las estrategias de despliegue deliberadamente, y adopta la entrega progresiva con reversión automatizada para limitar el radio de impacto.
- Desacopla el lanzamiento del despliegue con banderas de función, y gestiona la deuda de banderas.
- En entornos regulados, captura la evidencia de control de cambios automáticamente en lugar de a través de papeleo manual.

## Referencias y lecturas adicionales

- Jez Humble y David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, y Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, y John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, y George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, y Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, «Feature Toggles (Feature Flags)» (ensayo).
- ITIL (Information Technology Infrastructure Library), guía de gestión de cambios.
