# 2.4 Estrategia de pruebas

## Visión general y motivación

Una [estrategia de pruebas](https://en.wikipedia.org/wiki/Software_testing) es el conjunto deliberado de decisiones sobre qué se prueba, a qué nivel, con qué grado de automatización y hasta qué nivel de confianza, de modo que el equipo pueda modificar el código con rapidez y sin provocar roturas. Son las pruebas lo que permite a una gran organización desplegar con frecuencia y en condiciones de seguridad. Codifican el comportamiento esperado, detectan regresiones y dan a los ingenieros la confianza necesaria para [refactorizar](https://en.wikipedia.org/wiki/Code_refactoring) el código. Sin una estrategia coherente, la práctica de pruebas tiende a caer en uno de dos extremos negativos: ausencia (un desarrollo paralizado por el miedo y la lentitud) o hinchazón (miles de pruebas lentas e inestables que nadie confía).

En un equipo grande, la estrategia importa más que cualquier prueba individual. Cientos de ingenieros trabajando en una base de código compartida necesitan una red de seguridad rápida y fiable. Sin ella, cada cambio es arriesgado y cada lanzamiento se convierte en una odisea manual. Las pruebas también funcionan como documentación ejecutable del comportamiento previsto, algo inestimable una vez que los autores originales ya no están. La estrategia decide si la suite de pruebas es un activo que acelera la entrega o una carga que la frena.

En el ámbito empresarial y gubernamental, las pruebas tienen un peso adicional. Las regulaciones pueden exigir cobertura documentada y evidencias de pruebas. Los sistemas críticos para la seguridad y los que atienden a la ciudadanía demandan un alto nivel de garantías. Las pruebas de accesibilidad y seguridad pueden ser un requisito legal. Por ello, la estrategia debe equilibrar velocidad, confianza, coste y cumplimiento, y debe tratar la cobertura como una señal, no como una meta susceptible de manipulación.

## Principios fundamentales

- Poner a prueba para ganar la confianza de cambiar, no para alcanzar un número.
- Priorizar pruebas rápidas, fiables e aisladas. Las pruebas lentas o inestables erosionan la confianza que hace útil a una suite.
- Situar las pruebas al nivel más bajo que ofrezca una confianza real y reservar las pruebas amplias y lentas para el riesgo genuino de integración.
- Una prueba inestable es una prueba rota. Tratar la inestabilidad como un defecto de primera clase.
- La cobertura es una señal, no una meta. Una cobertura alta de código trivial no demuestra gran cosa.
- Probar el comportamiento y los contratos, no los detalles de implementación, para que las pruebas sobrevivan a la refactorización.
- Incluir en la estrategia las pruebas de no funcionalidad (accesibilidad, rendimiento, seguridad), no dejarlas como un añadido posterior.

## Recomendaciones

### Usar la pirámide de pruebas como punto de partida y conocer sus críticas

Partir de un enfoque basado en muchas [pruebas unitarias](https://en.wikipedia.org/wiki/Unit_testing) rápidas, menos [pruebas de integración](https://en.wikipedia.org/wiki/Integration_testing) y un pequeño número de pruebas de extremo a extremo, porque el coste y la fragilidad crecen al aumentar el alcance. Pero conocer también las críticas: la forma debe seguir la arquitectura, no un dogma. Un sistema de servicios intensivos puede necesitar una capa de integración más amplia (el «trofeo de pruebas»), y el verdadero objetivo es obtener la máxima confianza por unidad de coste y velocidad, no una silueta concreta. Lo que sí conviene evitar siempre es la pirámide invertida, compuesta sobre todo por pruebas de extremo a extremo lentas.

### Adoptar TDD, BDD y desarrollo basado en especificaciones donde aporten valor

Usar el [desarrollo guiado por pruebas](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) para impulsar el diseño y garantizar la testabilidad, especialmente en lógica compleja. Es tanto una disciplina de diseño como de pruebas. Usar el [desarrollo guiado por el comportamiento](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) para expresar las pruebas en un lenguaje de dominio compartido con las partes interesadas, algo valioso en entornos regulados o con criterios de aceptación exigentes. El desarrollo basado en especificaciones va un paso más allá: trata la especificación ejecutable (el comportamiento acordado, expresado en ejemplos) como la única fuente de verdad que a la vez guía la implementación y la verifica. Brilla allí donde los requisitos deben ser trazables hasta la evidencia de aceptación, como en programas gubernamentales y regulados. Vinculado a las tres approaches está el **[desplazamiento a la izquierda (shift-left)](https://en.wikipedia.org/wiki/Shift-left_testing)**: llevar la verificación lo más al principio posible del ciclo de vida, escribiendo pruebas junto al código o incluso antes, y ejecutándolas de forma continua, de modo que los defectos se detecten cuando es más barato corregirlos, en lugar de en fases tardías de pruebas o en producción. Ninguna de estas técnicas es obligatoria en todo momento. Aplicarlas donde aporten claridad.

### Emplear técnicas avanzadas para el código de alto valor

Usar pruebas basadas en propiedades para verificar invariantes con múltiples entradas generadas, detectando casos límite que las pruebas por ejemplo no alcanzan. Aplicar [pruebas de borrosidad](https://en.wikipedia.org/wiki/Fuzzing) en analizadores y en los puntos de entrada de datos no fiables para encontrar bloqueos y vulnerabilidades de seguridad. Emplear [pruebas de mutación](https://en.wikipedia.org/wiki/Mutation_testing) para medir si las pruebas realmente detectan los fallos inyectados: una señal de calidad muy superior a la cobertura bruta. Usar pruebas de snapshot con prudencia para salidas serializadas y evitar la trampa de reaprobar snapshots a ciegas.

### Gestionar los datos de prueba y recurrir a datos sintéticos

Hacer que las pruebas sean deterministas con datos de prueba controlados e aislados, y evitar los fijos mutables compartidos que acoplan las pruebas entre sí. Generar [datos sintéticos](https://en.wikipedia.org/wiki/Synthetic_data) que repliquen las características de producción sin exponer información personal real, algo imprescindible donde las normas de privacidad prohíben usar datos de producción en entornos de prueba. Ofrecer fbricas o constructores para que cada prueba pueda construir exactamente los datos que necesita.

### Tratar las pruebas inestables como defectos

Detectar la inestabilidad de forma automática, mover las pruebas inestables fuera de la ruta de bloqueo y corregirlas o eliminarlas en un plazo concreto. Una suite que falla al azar adiestra a los ingenieros a ignorar los fallos, lo que destruye todo su valor. Rastrear la tasa de inestabilidad y hacer que la fiabilidad sea una métrica de calidad explícita de la propia suite.

### Usar la cobertura como señal y añadir pruebas de no funcionalidad

Medir la cobertura para identificar zonas sin pruebas, pero no convertirla en una meta rígida que invite a la manipulación con pruebas sin aserciones. Complementarla con pruebas de mutación para profundizar. Integrar en el pipeline pruebas de accesibilidad (comprobaciones automatizadas más auditorías manuales), pruebas de rendimiento (líneas base de carga y latencia con detección de regresiones) y pruebas de seguridad (barrido de dependencias, [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis) y pruebas dinámicas).

## Compromisos: ventajas e inconvenientes

| Tipo de prueba o práctica | Ventajas | Inconvenientes |
|---|---|---|
| Pruebas unitarias | Rápidas, precisas, económicas y estables | No captan errores a nivel de integración o de sistema |
| Pruebas de integración | Detectan defectos de interfaz y de conexión | Más lentas; mayor configuración; más frágiles |
| Pruebas de extremo a extremo | Máxima confianza en el comportamiento real | Lentas, inestables, costosas de mantener |
| TDD | Mejor diseño, testabilidad garantizada | Curva de aprendizaje; sensación de lentitud al inicio |
| Pruebas basadas en propiedades | Detectan casos límite, codifican invariantes | Exigen pensar en propiedades; más difíciles de redactar |
| Pruebas de mutación | Medida real de la eficacia de las pruebas | Costosas computacionalmente; lentas de ejecutar |
| Meta estricta de cobertura | Revela código sin probar | Susceptible de manipulación; puede incentivar pruebas de bajo valor |

El compromiso central es entre confianza y velocidad/coste. Las pruebas más amplias dan más confianza pero son más lentas y se rompen con más frecuencia. Las pruebas más estrechas son rápidas y estables, pero se escapan defectos a nivel de sistema. La mezcla correcta maximiza la confianza por segundo de retroalimentación y por hora de mantenimiento. Y la sobretesting es un modo de fallo real: una suite hinchada de pruebas redundantes, lentas y frágiles puede costar más que los errores que previene.

## Preguntas para debatir con el equipo

1. **¿Qué pruebas de no funcionalidad (accesibilidad, rendimiento y seguridad) deben bloquear un lanzamiento y cuáles deben limitarse a informar?** Este capítulo defiende que la no funcionalidad pertenezca a la estrategia y no se considere un añadido posterior, y señala que la accesibilidad puede ser un requisito legal y que las pruebas de seguridad pueden formar parte de la evidencia de autorización de operación. En un sistema grande o dirigido a la ciudadanía, una puerta de entrada bloqueante frena la entrega, pero el coste de un defecto de accesibilidad o de seguridad descubierto en producción (remediación, reputación y posible exposición legal) supera con creces el del test. Aportar a la discusión las señales que deciden: la exposición regulatoria, si el sistema atiende a la ciudadanía y con qué frecuencia estos defectos llegan actualmente a producción. Hacer que las comprobaciones legalmente exigentes sean bloqueantes y permitir que las de menor riesgo informen con tendencia, de modo que la puerta refleje el riesgo real y no un dogma. La respuesta determina directamente qué puede y qué no puede integrarse.

2. **¿Se establece un porcentaje de cobertura estricto como umbral y, de ser así, qué impide que los ingenieros lo manipulen con pruebas sin aserciones?** El capítulo es rotundo: la cobertura es una señal, no una meta; la alta cobertura de código trivial no demuestra gran cosa; y una meta numérica rígida invita a la manipulación. Un único número impuesto en toda una organización produce de forma fiable pruebas que ejecutan código sin aserciones, lo que eleva la métrica y reduce la confianza real. Aportar una señal mejor: un índice de mutación en los módulos de mayor valor, que mide si las pruebas realmente detectan los fallos inyectados. Usar la cobertura para identificar zonas sin probar y las pruebas de mutación para medir profundidad, y resistirse a convertir ninguna de las dos en una meta que la dirección siga de forma aislada. Decidir dónde el número ayuda de verdad y dónde solo genera teatro.

3. **¿Cuál es la política cuando la suite de pruebas se vuelve demasiado lenta para que los ingenieros la esperen?** El compromiso central de este capítulo es entre confianza y velocidad/coste, y señala la sobretesting como un modo de fallo real: una suite hinchada, redundante y lenta que cuesta más que los errores que previene. En un equipo grande, el tiempo de ejecución de la suite es un impuesto compartido que cada cambio impone a cada ingeniero, y una suite que la gente aprende a eludir pierde todo su valor. Aportar las pruebas: el tiempo total de CI, las pruebas más lentas y la cantidad de cobertura redundante de extremo a extremo que duplica pruebas unitarias más económicas. Situar las pruebas al nivel más bajo que ofrezca confianza real, paralelizar y eliminar pruebas lentas redundantes en un plazo concreto. El objetivo es optimizar la confianza por segundo de retroalimentación, no el número total de pruebas.

4. **¿Cuando una prueba se vuelve inestable, quién es su responsable, con qué rapidez debe corregirse o eliminarse y qué mecanismo hace cumplir ese plazo?** Este capítulo trata la prueba inestable como una prueba rota, un defecto de primera clase, porque una suite que falla al azar adiestra a un equipo grande a ignorar los builds en rojo y destruye en silencio la red de seguridad de la que todos dependen. La presión contraria es real: poner una prueba inestable en cuarentena desbloquea la entrega hoy, pero arriesga enmascarar un fallo intermitente genuino, mientras que bloquear por ella paraliza a cientos de ingenieros por una posible anomalía pura. Aportar la evidencia que lo resuelva: la tasa de inestabilidad actual, cuánto tiempo llevan las pruebas en cuarentena antes de que alguien las toque y cuántas de las puestas en cuarentena resultaron ocultar un defecto real. Asignar un responsable a cada prueba en cuarentena, fijar un plazo firme para corregirla o eliminarla y rastrear la fiabilidad como métrica explícita de la suite. En entornos empresariales y gubernamentales donde un build verde forma parte de la evidencia de lanzamiento, un montón de cuarentenas sin gestionar es también un pasivo de auditoría, porque se está publicando sobre una señal que se ha acordado, en privado, no confiar.

5. **¿Se permite usar datos de producción en los entornos de prueba y, si no, cómo se generarán datos sintéticos足够 fidedignos para captar defectos reales?** El capítulo es directo: las normas de privacidad suelen prohibir los datos personales reales en prueba, y los datos sintéticos deben replicar las características de producción o las pruebas darán una confianza falsa. En una gran organización, la tensión es entre fidelidad y cumplimiento: los datos de producción captan los casos límite caóticos que los sintéticos se escapan, pero cada copia multiplica la exposición y las obligaciones. Aportar los detalles concretos: qué conjuntos de datos contienen información personal o regulada, qué exigen realmente las normas de privacidad y de residencia de datos, y qué bien reproducen los fijos actuales las distribuciones y los casos límite observados en producción. Estandarizar fbricas o constructores para que cada prueba construya exactamente los datos que necesita, e invertir en generación sintética que coincida con las distribuciones demográficas y de volumen reales. En programas gubernamentales y regulados, usar datos de ciudadanos en un entorno de prueba no es un atajo: es una infracción reportable, por lo que la estrategia de datos debe estar resuelta antes de que se levante el primer entorno.

6. **¿Dónde deberían esperarse TDD, BDD o desarrollo basado en especificaciones y no ser opcionales, y quién lo decide?** Este capítulo presenta estas disciplinas como prácticas a aplicar donde aporten claridad, no como mandatos para cada línea de código; aun así, un equipo grande se beneficia de un punto de partida compartido para que la práctica no se fragmente equipo a equipo. El compromiso es entre los beneficios de diseño y trazabilidad (especificaciones ejecutables que los expertos en política pueden revisar, pruebas que sobreviven a la refactorización) y la curva de aprendizaje genuina y la lentitud inicial que hacen que un mandato generalizado se convierta en contraproducente. Aportar evidencia para delimitarlo: qué módulos tienen lógica compleja o tasas altas de fallo por cambio, dónde los criterios de aceptación deben ser trazables hasta los requisitos, y cómo reportan velocidad y tasas de defecto los equipos que ya practican estos enfoques. Reservar la expectativa para la lógica compleja y las áreas con requisitos densos, y dejar que el código más sencillo decida por sí mismo. En programas regulados y gubernamentales donde el software debe ser trazable hasta la norma que implementa, el desarrollo basado en especificaciones con evidencia de aceptación ejecutable es menos una preferencia que la vía hacia la autorización de operación, por lo que conviene nombrar explícitamente dónde es obligatorio.

## Perspectiva por sector

**Startup.** Un equipo diminuto no puede permitirse un equipo de QA, así que hay que hacer que la suite justifique su existencia: pruebas unitarias rápidas en cada commit y un par de pruebas de extremo a extremo sobre el único camino que da ingresos, y nada que no se pueda mantener. Saltarse las metas de cobertura y probar la lógica que más aterra romper, para poder desplegar varias veces al día sin una pasada manual de regresión. Corregir una prueba inestable el mismo día, porque en esta fase una suite que el equipo aprende a ignorar es peor que no tener suite.

**Pyme.** Sin un ingeniero de pruebas dedicado y con un presupuesto ajustado, conviene apoyarse en las pruebas integradas en los frameworks y herramientas que ya se usan, en lugar de un arnés a medida que no se puede sostener. Priorizar el puñado de comprobaciones que protegen los ingresos y la confianza del cliente, y usar CI alojado para no tener que mantener la infraestructura de build propia. Preferir comprar accesibilidad y escaneo de seguridad como servicio antes que construirlos, ya que un único defecto descubierto puede costar más que un año de la herramienta.

**Gran empresa.** En múltiples equipos, el problema es la coherencia: un punto de partida piramidal compartido, cuarentena automática de pruebas inestables y puertas de no funcionalidad que signifiquen lo mismo en todas partes, de modo que un build verde sea fiable con independencia de quién lo haya producido. Presupuestar el tiempo de ejecución de la suite como un impuesto compartido y paralelizar de forma agresiva, porque el tiempo total de CI se paga con cada cambio y por cada ingeniero. Gestionar la cobertura y los índices de mutación como señales de portafolio con propiedad clara, no como números que la dirección siga de forma aislada.

**Sector público y gubernamental.** La contratación y la supervisión convierten las pruebas en evidencia, no solo en higiene de ingeniería. Expresar las reglas de elegibilidad y de política como especificaciones ejecutables revisadas por expertos en dominio, para poder trazar el software hasta la norma que implementa. Hacer que las pruebas de accesibilidad y seguridad sean bloqueantes, pues son un requisito legal y forman parte de la evidencia de autorización de operación. Usar datos sintéticos generados para coincidir con las distribuciones reales, ya que los datos de ciudadanos en un entorno de prueba constituyen una infracción reportable. Y mantener los artefactos de pruebas auditables, de modo que un revisor externo pueda confirmar exactamente qué se verificó.

## Ejemplos

**Startup.** Una startup de cinco personas no puede permitirse un equipo de QA, así que se apoya en una suite de pruebas unitarias rápidas que se ejecuta en cada commit y en un par de pruebas de extremo a extremo que cubren el camino de registro a compra, el que da los ingresos. Los fundadores se saltan la cobertura exhaustiva y prueban en su lugar la lógica que más les aterra romper, lo que les permite desplegar varias veces al día sin una pasada manual de regresión. Cuando una prueba empieza a fallar al azar, la corrigen el mismo día, porque una suite que el equipo aprende a ignorar es peor que no tener suite en la fase en que la confianza lo es todo.

**Gran empresa.** Una gran plataforma de comercio electrónico mantiene miles de pruebas unitarias rápidas que se ejecutan en minutos en cada commit, un conjunto enfocado de pruebas de integración alrededor de los límites de pagos e inventario, y una suite pequeña de pruebas de extremo a extremo para los recorridos críticos de compra. Las pruebas de extremo a extremo inestables se ponen automáticamente en cuarentena y se asignan para reparación. Como los ingenieros confían en la suite, despliegan varias veces al día, seguros de que un build rojo significa un problema real.

**Sector público y gubernamental.** Un sistema nacional de prestaciones que opera bajo supervisión regulatoria usa BDD para expresar las reglas de elegibilidad como especificaciones ejecutables revisadas por expertos en política, lo que aporta evidencia trazable de que el software implementa la ley. Usa datos sintéticos generados para coincidir con las distribuciones demográficas reales, porque las normas de privacidad prohíben los datos de ciudadanos en entornos de prueba. Las pruebas de accesibilidad son obligatorias y bloquean el lanzamiento, ya que el servicio debe ser usable por todos los ciudadanos. Y las pruebas de seguridad forman parte de la evidencia de autorización de operación (ATO), la aprobación formal para ejecutar el sistema en producción.

## Justificación económica: motivación, retorno de inversión y coste total

El retorno de invertir en pruebas es la capacidad de cambiar software con rapidez y seguridad, que es la base de la velocidad de entrega sostenida. Una suite automatizada fiable reemplaza las lentas y costosas [pruebas de regresión](https://en.wikipedia.org/wiki/Regression_testing) manuales y captura los defectos cuando es más barato corregirlos, antes del lanzamiento y no en producción. En un sistema regulado o dirigido a la ciudadanía, el coste de un defecto en producción (remediación, reputación y posible exposición legal) supera con creces el coste de las pruebas que lo habrían detectado.

El coste de adopción es real: hay que escribir y mantener pruebas, y construir infraestructura de [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Pero el coste de no probar es mayor y se acumula: un desarrollo paralizado por el miedo que se hunde a un ritmo raquítico, regresiones frecuentes y procesos de lanzamiento manuales que no escalan. También existe un coste de la sobretesting, así que el argumento es a favor de una estrategia bien diseñada, no del máximo número de pruebas. Para presentar el caso a la dirección, hay que vincular la suite con la frecuencia de despliegue, la tasa de fallo por cambio y el tiempo medio de recuperación, y cuantificar el esfuerzo de pruebas manuales que reemplaza y los incidentes de producción que previene.

## Antipatrón y errores comunes

- **Prueba en forma de helado:** sobre todo pruebas de extremo a extremo lentas sobre una base unitaria delgada; lentas, inestables y costosas.
- **Cobertura como meta:** perseguir un porcentaje con pruebas sin aserciones o triviales que no prueban nada.
- **Probar detalles de implementación:** pruebas acopladas a los internos que se rompen en cada refactorización y desincentivan el cambio.
- **Tolerancia a la inestabilidad:** fallos aleatorios que adiestran al equipo a ignorar los builds en rojo.
- **Datos de prueba mutables compartidos:** pruebas que interfieren entre sí y fallan de forma impredecible.
- **Uso de datos de producción en test:** una brecha de privacidad y de cumplimiento esperando pasar factura.
- **No funcionalidad omitida:** accesibilidad, rendimiento y seguridad descubiertos solo en producción.
- **La suite desconfiada:** tan poco fiable que los ingenieros la reexecutan o la eluden de forma habitual, anulando su propósito.

## Modelo de madurez

- **Nivel 1, Iniciar:** Las pruebas son manuales y reactivas; la cobertura automatizada es mínima; las regresiones son frecuentes y se detectan tarde, a menudo por los usuarios y no por la suite.
- **Nivel 2, Desarrollar:** Existen pruebas unitarias automatizadas y algunas de integración, pero la suite es lenta o inestable, la confianza es baja y la práctica varía enormemente de un equipo a otro.
- **Nivel 3, Estandarizar:** Una suite equilibrada, rápida y fiable verifica cada cambio; un punto de partida piramidal documentado, una política de pruebas inestables y pruebas de no funcionalidad (accesibilidad, rendimiento, seguridad) se aplican de forma coherente en todos los equipos.
- **Nivel 4, Gestionar:** La salud de la suite se mide y controla contra líneas base; se rastrea y revisa la tasa de inestabilidad, el tiempo total de CI, el índice de mutación en los módulos de alto valor y la tasa de defectos escapados; la cobertura es una señal entre varias, y las puertas se activan con evidencia, no con opinión.
- **Nivel 5, Orquestar:** Las técnicas avanzadas (pruebas basadas en propiedades, de mutación y de borrosidad) se aplican al código de alto valor; la prueba se integra con las métricas de entrega como la frecuencia de despliegue, la tasa de fallo por cambio y el tiempo medio de recuperación; la organización reconfigura la suite de forma continua en función de su arquitectura y su perfil de riesgo, retirando pruebas redundantes e invirtiendo donde la evidencia muestra que los defectos aún escapan.

## Ideas para la reflexión

- ¿Qué forma tiene realmente la distribución de pruebas y responde a la arquitectura y al riesgo?
- ¿Cómo se decide si un fragmento de código merece pruebas basadas en propiedades o de mutación frente a pruebas por ejemplo?
- ¿Cuál es la política sobre pruebas inestables y se aplica de verdad?
- ¿Cómo se generan datos sintéticos realistas sin filtrar información sensible?
- ¿Dónde ayuda de verdad la cobertura y dónde ha sido manipulada?
- ¿Cómo deben revisarse las pruebas generadas por IA para que aporten confianza y no ruido?

## Ideas clave

- Probar para ganar la confianza de cambiar; optimizar la confianza por unidad de velocidad y de coste.
- Usar la pirámide como punto de partida, pero adaptar la prueba a la propia arquitectura.
- Tratar las pruebas inestables como defectos y la cobertura como señal, no como meta.
- Aplicar técnicas avanzadas donde el valor justifique el coste.
- Incluir en la estrategia las pruebas de accesibilidad, rendimiento y seguridad, y usar datos sintéticos para proteger la privacidad.

## Referencias y lecturas complementarias

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin y Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, artículos sobre la pirámide de pruebas y patrones relacionados con la prueba

