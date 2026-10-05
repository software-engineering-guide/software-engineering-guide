# 7.2 Ingeniería de datos

## Presentación y motivación

La [ingeniería de datos](https://en.wikipedia.org/wiki/Data_engineering) es la disciplina de construir y operar los canales y plataformas que mueven los datos desde donde se producen hasta donde crean valor. Cubre la ingesta desde sistemas fuente, la transformación en formas limpias y modeladas, el almacenamiento en formatos rentables, la orquestación de todo el flujo, y las prácticas de fiabilidad que mantienen todo confiable. Si la estrategia de datos decide qué datos deberían existir y quién es su dueño, la ingeniería de datos es la plomería y la maquinaria que los hace fluir.

Para los equipos grandes, esta disciplina es fundacional. La analítica, la [inteligencia de negocio](https://en.wikipedia.org/wiki/Business_intelligence), la experimentación de producto, el [aprendizaje automático](https://en.wikipedia.org/wiki/Machine_learning), y el reporte regulatorio se sitúan todos aguas abajo de los canales de datos. Cuando esos canales son frágiles, lentos u opacos, cada función dependiente sufre. Los tableros muestran números obsoletos. Los modelos entrenan con características corruptas. Los auditores no pueden reconstruir cómo se produjo una cifra. A escala empresarial y gubernamental, los canales procesan miles de millones de registros a través de muchos sistemas fuente, y un único fallo silencioso puede introducir datos incorrectos en decisiones, pagos o estadísticas públicas.

El campo ha crecido desde scripts artesanales y herramientas monolíticas de [ETL (extracción, transformación, carga)](https://en.wikipedia.org/wiki/Extract,_transform,_load) hasta la pila de datos moderna: componentes modulares, en gran medida impulsados por SQL, para la ingesta, transformación, orquestación y almacenamiento, conectados por formatos abiertos. Esta modularidad es tanto un regalo como una trampa. Te permite ensamblar las mejores herramientas de su clase, pero sin disciplina de ingeniería produce una maraña de trabajos no documentados y no probados. Este capítulo cubre las prácticas que mantienen los canales idempotentes, comprobables, observables y asequibles a escala.

## Principios fundamentales

- Los canales son software y merecen control de versiones, pruebas, revisión y CI/CD.
- Prefiere transformaciones idempotentes y reproducibles que puedan volver a ejecutarse con seguridad.
- Haz observables los flujos de datos: la frescura, el volumen, el esquema y la calidad se monitorean.
- Modela los datos deliberadamente para sus consumidores en lugar de volcar tablas crudas.
- Elige por lotes o en flujo según las necesidades reales de latencia, no por novedad.
- Optimiza el formato de almacenamiento, la partición y el costo de cómputo como preocupaciones de primera clase.
- Separa la ingesta, la transformación y el servicio para que cada una pueda evolucionar independientemente.
- Falla ruidosa y tempranamente; un canal roto es más seguro que un dato silenciosamente incorrecto.

## Recomendaciones

### Elige ETL o ELT deliberadamente

ETL transforma los datos antes de cargarlos en el destino. [ELT (extracción, carga, transformación)](https://en.wikipedia.org/wiki/Extract,_load,_transform) carga primero los datos crudos y los transforma dentro de un almacén o lakehouse potente. Las plataformas en la nube modernas han hecho de ELT el valor predeterminado, porque el almacenamiento es barato y el cómputo es elástico, y mantener los datos crudos te permite reprocesar cuando la lógica cambia o aparecen errores. Prefiere ELT para cargas de trabajo de analítica: aterriza datos crudos inmutables, luego construye transformaciones por capas encima. Reserva la transformación previa a la carga para casos donde la privacidad, el costo o las restricciones contractuales requieran limpiar o filtrar antes de que el dato aterrice.

### Diseña canales por lotes y en flujo según sus necesidades de latencia

La mayoría de las necesidades de analítica están bien servidas por canales programados por lotes, que son más simples de razonar, probar y rellenar retroactivamente. Recurre al flujo solo cuando el negocio genuinamente necesite datos de baja latencia: detección de fraude, alertas operacionales, personalización en tiempo real. El flujo añade complejidad real en torno al orden, la semántica de exactamente una vez, los datos que llegan tarde, y la gestión de estado. Donde necesites ambos, considera arquitecturas que unifiquen la lógica de lotes y flujo en lugar de mantener dos bases de código divergentes. Sé honesto sobre tus requisitos de latencia. «Tiempo real» a menudo es un deseo no examinado que duplica tu costo.

### Orquesta con dependencias explícitas

Usa un orquestador para expresar los canales como [grafos acíclicos dirigidos (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) de tareas con dependencias explícitas, reintentos y programación. Esto te da visibilidad sobre qué se ejecutó, qué falló, y qué está bloqueado, más la capacidad de rellenar retroactivamente y volver a ejecutar de forma determinista. Basa las dependencias en la disponibilidad de datos, no solo en el tiempo del reloj, para que los trabajos posteriores esperen los datos anteriores en lugar de dispararse por una suposición. Mantén la lógica de orquestación en control de versiones, y trata los cambios de DAG como cambios de código.

### Modela los datos para el consumo

Las tablas crudas rara vez son aptas para los analistas. Aplica el [modelado dimensional](https://en.wikipedia.org/wiki/Dimensional_modeling), que organiza hechos y dimensiones conformes en [esquemas de estrella](https://en.wikipedia.org/wiki/Star_schema), donde necesites analítica gobernada, reutilizable y de autoservicio. Las tablas anchas desnormalizadas («una gran tabla») pueden rendir mejor para patrones de consulta específicos y son más simples para algunos consumidores, al costo de duplicación y flexibilidad. Estratifica tus transformaciones: una capa de preparación cruda, una capa central limpia y conforme, y data marts orientados al consumidor. Esta separación te permite arreglar la lógica en un solo lugar, y permite a los consumidores depender de interfaces estables.

### Haz que los canales sean idempotentes y comprobables

Diseña las transformaciones para que volver a ejecutarlas produzca el mismo resultado, en lugar de duplicar o corromper datos, por ejemplo usando upserts deterministas con clave en identificadores de negocio y patrones de sobrescritura por partición. Escribe pruebas en varios niveles: pruebas unitarias para la lógica de transformación, pruebas de esquema, y pruebas de datos que afirmen expectativas como unicidad, claves no nulas, integridad referencial, y rangos de valores aceptados. Ejecuta estas en CI, para que un mal cambio se detecte antes de que llegue a los datos de producción.

### Instrumenta la observabilidad y la fiabilidad

Monitorea las cuatro señales centrales de la salud de los datos: frescura (está actualizado), volumen (el conteo de filas está en el rango esperado), esquema (la estructura ha cambiado inesperadamente), y distribución (los valores han derivado de forma anómala). Alerta ante incumplimientos, y enrútalos al equipo dueño. Mantén runbooks, rotaciones de guardia, y postmortems sin culpa para los incidentes de datos, tal como lo harías para los servicios. Rastrea el linaje, para que cuando algo se rompa, puedas ver el impacto posterior de inmediato.

### Optimiza el almacenamiento y el costo

Usa formatos columnares abiertos como Parquet, o formatos de tabla abiertos que soporten la evolución de esquema, viaje en el tiempo, y actualizaciones eficientes. Particiona los datos por las columnas por las que más filtras, típicamente la fecha, y evita una proliferación de archivos diminutos compactando. Separa los datos calientes y fríos con almacenamiento por niveles y políticas de ciclo de vida. Monitorea el gasto de cómputo por canal y por consulta. Los costos desbocados usualmente vienen de escaneos completos, particiones faltantes, y reprocesamiento sin límites. Trata el costo como una métrica con dueños, no como una sorpresa en la factura mensual.

## Ventajas y desventajas

| Elección | Ventajas | Desventajas | Mejor ajuste |
|---|---|---|---|
| ELT (transformar en el destino) | Conserva los datos crudos, almacenamiento barato, reprocesable | Huella de almacenamiento grande, necesita gobernanza | Analítica en la nube |
| ETL (transformar antes de cargar) | Controla el costo, filtra datos sensibles temprano | Pierde lo crudo, más difícil de reprocesar | Cargas reguladas o restringidas |
| Por lotes | Simple, comprobable, fácil de rellenar retroactivamente | Mayor latencia | La mayoría de la analítica |
| En flujo | Baja latencia, reacción en tiempo real | Complejo, costoso, difícil de probar | Fraude, alertas operacionales |
| Esquema de estrella | Gobernado, reutilizable, amigable al autoservicio | Esfuerzo de modelado por adelantado | BI compartida |
| Tabla ancha | Rápida para consultas conocidas, simple | Duplicación, menos flexible | Uso de alto rendimiento estrecho |

La contrapartida dominante es simplicidad frente a latencia y flexibilidad. Los lotes y ELT con esquemas de estrella por capas te dan un sistema comprobable, rellenable retroactivamente y bien comprendido que sirve a la mayoría de las necesidades de forma asequible. El flujo, el tiempo real, y los diseños altamente desnormalizados compran velocidad y rendimiento específico, pero a un costo elevado en complejidad operacional y dificultad de prueba. Adopta la complejidad solo donde un requisito de negocio concreto la paga, y mantén el camino simple como tu valor predeterminado.

## Preguntas para discutir con tu equipo

1. **¿Has elegido deliberadamente ELT sobre ETL, y mantienes datos crudos inmutables para poder reprocesar cuando la lógica cambia o surgen errores?** El valor predeterminado del capítulo es ELT: aterrizar datos crudos de forma barata, luego construir transformaciones por capas, porque mantener lo crudo te permite volver a ejecutar todo cuando una regla cambia o aparece un error semanas después. Borrar los datos crudos cierra esa opción y es una trampa común y dolorosa. El caso opuesto a favor de ETL es real en cargas reguladas o restringidas, donde la privacidad, el costo o los términos contractuales requieren filtrar o enmascarar antes de que el dato aterrice. Trae evidencia: ¿con qué frecuencia has necesitado reprocesar el historial, y qué costó cuando no pudiste? Para un canal gubernamental o empresarial que debe rastrear cualquier cifra hasta la fuente, los registros crudos inmutables son también un requisito de auditabilidad, así que la respuesta moldea tanto tu política de almacenamiento como tu defendibilidad legal.

2. **¿Cuáles de las cuatro señales de salud de datos realmente monitoreas, y a quién se le avisa cuando una falla?** El capítulo nombra cuatro señales que vale la pena vigilar: frescura, volumen, esquema y distribución. Muchos equipos no monitorean ninguna y se enteran de los fallos por un ejecutivo mirando un tablero obsoleto, que es el peor detector posible. A escala empresarial y gubernamental, un único fallo silencioso puede introducir datos incorrectos en pagos, informes o estadísticas públicas, así que el costo de la detección tardía se mide en confianza y dinero, no solo en retrabajo. Trae tu tiempo medio real de detección y el nombre de quien actualmente encuentra los incidentes primero. Si la respuesta es «un consumidor», necesitas alertas enrutadas al equipo dueño más runbooks y postmortems sin culpa, tratando los incidentes de datos exactamente como interrupciones de servicio.

3. **¿Tus analistas consumen data marts modelados y probados, o les estás volcando tablas crudas y llamándolo autoservicio?** El capítulo es directo: las tablas crudas rara vez son aptas para los analistas, y estratificar las transformaciones en una capa de preparación cruda, un núcleo conforme, y data marts orientados al consumidor te permite arreglar la lógica una vez y dar a los consumidores interfaces estables. La tensión en competencia es la velocidad, ya que modelar con esquemas de estrella o tablas anchas deliberadas cuesta esfuerzo por adelantado y es tentador saltárselo. Pero volcar datos crudos empuja el costo del modelado a cada analista repetidamente, produciendo números divergentes y horas desperdiciadas. Trae una señal: qué porcentaje del tiempo del analista va a remodelar datos crudos, y cuántos equipos han reconstruido las mismas uniones. Si el número es alto, invierte en una capa central conforme para que los consumidores dependan de interfaces probadas y reutilizables en lugar de reinventarlas.

4. **¿Dónde se gana genuinamente su costo el «tiempo real», y dónde es un deseo no examinado que silenciosamente duplica tu carga operacional?** El valor predeterminado del capítulo es el lote programado, que es más simple de razonar, probar y rellenar retroactivamente, reservando el flujo para casos donde el negocio realmente necesita baja latencia, como la detección de fraude o las alertas operacionales. La tensión en competencia es el prestigio y las peticiones vagas de las partes interesadas de datos «en vivo», que suenan baratas en una reunión de planificación y se vuelven costosas en producción, porque el flujo arrastra consigo el orden, la semántica de exactamente una vez, los datos que llegan tarde, y la gestión de estado, más una segunda base de código que mantener sincronizada con la lógica por lotes. Trae evidencia a la discusión: para cada canal de flujo que operas o propones, nombra la decisión que alimenta y la latencia que esa decisión realmente tolera, medida en minutos u horas en lugar de adjetivos. Para una gran empresa o plataforma gubernamental, añade el costo de guardia y prueba de cada camino en tiempo real, porque un canal de flujo que nadie puede probar ni cubrir las 24 horas es un pasivo de fiabilidad disfrazado de función, y la respuesta honesta a menudo colapsa un requisito de «tiempo real» de vuelta a un lote por hora que sirve la misma decisión.

5. **¿Cuáles de tus canales no podrían volver a ejecutarse con seguridad hoy, y qué se necesitaría para hacer idempotente cada transformación?** El capítulo insiste en transformaciones idempotentes y reproducibles, usando upserts deterministas con clave en identificadores de negocio y patrones de sobrescritura por partición, para que una nueva ejecución produzca el mismo resultado en lugar de duplicar o corromper datos. La presión en competencia es la velocidad de entrega, ya que un trabajo ingenuo de solo anexar se envía más rápido que uno diseñado para volver a ejecutarse, y el costo de ese atajo permanece oculto hasta que un fallo fuerza una reejecución parcial a las 2 de la madrugada y alguien cuenta doble los ingresos. Trae un inventario concreto: enumera los trabajos que corromperían datos si se volvieran a ejecutar desde un punto de fallo, y estima el radio de impacto del peor. A escala empresarial y gubernamental, donde un único fallo silencioso puede introducir datos incorrectos en pagos, informes o estadísticas públicas, el procesamiento no idempotente no es meramente inconveniente, socava la auditabilidad que te permite reprocesar un período después de un cambio de regla y aun así rastrear cada cifra hasta la fuente, así que financiar el retrabajo para hacer seguras las reejecuciones es una cuestión de control, no solo de prolijidad.

6. **¿Sabes lo que cuesta ejecutar cada canal, quién es dueño de ese número, y cuánto de tu factura de la nube viene de escaneos completos y particiones faltantes?** El capítulo trata el formato de almacenamiento, la partición y el gasto de cómputo como preocupaciones de primera clase con dueños, advirtiendo que los costos desbocados usualmente se rastrean a escaneos completos, particiones faltantes, y reprocesamiento sin límites. La consideración en competencia es que el trabajo de costo se siente menos urgente que enviar funciones, así que se pospone hasta que la factura mensual se vuelve una sorpresa y finanzas empieza a hacer preguntas que ingeniería no puede responder. Trae evidencia: el gasto por canal y por consulta, el porcentaje de costo que viene de escaneos sin partición, y el conteo de archivos diminutos que deberían compactarse. Para una gran organización que ejecuta miles de millones de registros a través de muchos sistemas fuente, una factura de la nube sin dueño crece sin que ningún equipo se sienta responsable, y en entornos gubernamentales el gasto público debe justificarse línea por línea, así que atribuir el costo de cómputo a un dueño nombrado con una métrica rastreada convierte un gasto opaco en uno gestionado y a menudo revela ahorros lo bastante grandes para financiar la siguiente inversión en plataforma.

## Perspectiva sectorial

**Startup.** La velocidad supera a la arquitectura. Conecta la ingesta a un conector gestionado, construye un puñado de transformaciones bajo control de versiones, y ejecútalas en un orquestador ligero que reintenta y rellena retroactivamente por sí solo, en lugar de fabricar a mano trabajos cron que se rompen silenciosamente durante la noche. Mantén cada modelo idempotente desde el primer commit y añade unas cuantas pruebas baratas para claves nulas y conteos de filas, para que un mal cambio de fuente falle en CI en lugar de aparecer en el tablero del lunes del fundador. No levantes flujo ni una plataforma a medida: tu recurso más escaso es la atención de ingeniería.

**Pequeña empresa.** Sin un ingeniero de datos dedicado, favorece comprar una pila integrada en lugar de ensamblar una. Un servicio ELT gestionado más un almacén en la nube te da conectores, programación y almacenamiento sin un equipo de plataforma que los mantenga. Enmarca la elección como higiene de datos en lugar de un proyecto de canal: sabe qué sistemas fuente alimentan tus informes, mantén datos crudos para que un número erróneo pueda rastrearse y reprocesarse, y elige herramientas cuyos costos sean predecibles para que un escaneo de tabla completa no reviente el presupuesto mensual.

**Empresa.** El problema es la consistencia entre muchos equipos y miles de millones de registros de muchos sistemas fuente. Estandariza el patrón ELT, el modelo por capas de preparación-núcleo-mart, y las cuatro señales de salud de datos para que los grupos dejen de reinventar canales frágiles. Aplica pruebas de datos y CI en cada modelo, atribuye el costo de cómputo a los equipos dueños, y haz correr los incidentes de datos por la misma disciplina de guardia, runbook y postmortem sin culpa que usas para los servicios, para que un fallo silencioso nunca llegue a un tablero sin notarse.

**Gobierno.** Las reglas de contratación pública, la transparencia y la rendición de cuentas pública moldean el canal. Aterriza registros crudos inmutables para la auditabilidad, transfórmalos en etapas estratificadas y probadas, y mantén linaje completo para que un auditor pueda rastrear cualquier cifra publicada hasta sus documentos fuente, a menudo un requisito legal. El procesamiento idempotente te permite reprocesar de forma segura un período de declaración o reporte cuando cambia una regla, y favorecer formatos abiertos y código de transformación portable te evita quedar atrapado con un único proveedor a lo largo de un contrato de varios años.

## Ejemplos

**Startup.** Una startup de analítica de diez personas había hecho crecer una maraña de trabajos cron que se rompían silenciosamente durante la noche y a veces contaban filas dos veces cuando un ingeniero volvía a ejecutar uno a mano. El equipo se cambió a un conector gestionado para la ingesta, un marco de transformación para modelos versionados, y un orquestador ligero que reintenta y rellena retroactivamente por sí solo. Hicieron idempotente cada modelo y añadieron un puñado de pruebas para claves nulas y conteos de filas, así que un mal cambio de fuente ahora falla en CI en lugar de aparecer en el tablero del lunes del fundador.

**Empresa.** Un minorista global reemplazó cientos de scripts de extracción escritos a mano con una pila ELT. Los conectores gestionados aterrizan los datos fuente crudos, un marco de transformación construye modelos probados y versionados en un lakehouse, y un orquestador gestiona las dependencias con reintentos y rellenos retroactivos. Las pruebas de datos atrapan la deriva de esquema de los sistemas fuente antes de que llegue a los tableros. El almacenamiento columnar particionado redujo sustancialmente los costos de consulta, mientras mejoraba la frescura de diaria a horaria.

**Gobierno.** Una autoridad tributaria ingiere declaraciones y datos de terceros a través de un canal gobernado que aterriza registros crudos inmutables para la auditabilidad, luego los transforma en etapas estratificadas y probadas. El procesamiento idempotente les permite reprocesar de forma segura un período de declaración cuando cambia una regla. El linaje completo permite a los auditores rastrear cualquier cifra calculada hasta los documentos fuente, un requisito legal para la rendición de cuentas pública.

## Caso de negocio: motivaciones, ROI y TCO

El ROI de una ingeniería de datos disciplinada viene de la fiabilidad, la velocidad y el control de costos. Los canales confiables significan que las decisiones y los informes descansan en datos confiables, así que evitas el retrabajo costoso y el daño reputacional de los números erróneos. Los canales modulares y probados permiten a los equipos enviar nuevos productos de datos más rápido, componiendo el valor de cada inversión posterior en analítica y aprendizaje automático. Optimizar el almacenamiento y el cómputo reduce directamente la factura de la nube, a menudo por márgenes grandes una vez que se arreglan la partición y los patrones de consulta.

El costo de adopción incluye herramientas de plataforma, tiempo de ingeniería para construir canales modulares probados, y la disciplina de tratar los datos como software. Pesa esto contra el costo de no adoptar: trabajos artesanales frágiles que solo su autor comprende, corrupción de datos silenciosa descubierta por ejecutivos, gasto en la nube inflado por escaneos de tabla completa, y analistas bloqueados esperando datos. Al liderazgo, enmarca la ingeniería de datos como el fundamento que hace confiable y asequible la analítica, la BI y la IA. Subinvierte aquí, y limitas el retorno de cada iniciativa de datos por encima de ella.

## Antipatrones y trampas

- Canales construidos como scripts únicos sin control de versiones, pruebas ni revisión.
- Trabajos no idempotentes que duplican o corrompen datos al volver a ejecutarse tras un fallo.
- Adoptar el flujo por prestigio cuando el lote cumpliría el requisito de latencia.
- Volcar tablas crudas sobre los analistas y llamarlo autoservicio.
- Sin observabilidad, así que los fallos los descubren los consumidores posteriores.
- Ignorar la partición y el tamaño de archivo hasta que la factura de la nube explota.
- Acoplar la ingesta, la transformación y el servicio de modo que nada pueda cambiar con seguridad.
- Borrar los datos crudos, haciendo imposible reprocesar cuando cambia la lógica.

## Modelo de madurez

1. Iniciar: Scripts ad hoc y ejecuciones manuales, sin pruebas ni monitoreo. Los fallos los descubren los consumidores posteriores, los trabajos no pueden volver a ejecutarse con seguridad, y los costos de la nube no se gestionan ni se atribuyen.
2. Desarrollar: Algunos equipos han adoptado un orquestador y puesto transformaciones básicas en control de versiones, pero la práctica es inconsistente en toda la organización. Existen pruebas ocasionales, la idempotencia es irregular, y los canales rotos todavía significan apagar incendios de forma reactiva.
3. Estandarizar: ELT con un modelo por capas de preparación-núcleo-mart, probado y versionado, es el estándar documentado aplicado entre equipos. Las dependencias orquestadas con reintentos y rellenos retroactivos, las pruebas de datos ejecutándose en CI, y las convenciones compartidas para el modelado de esquema de estrella y la partición se aplican en toda la organización en lugar de dejarse a cada grupo.
4. Gestionar: La plataforma se mide y controla. La frescura, el volumen, el esquema y la distribución se monitorean con alertas enrutadas a los equipos dueños, y los acuerdos de nivel de servicio de los canales, el tiempo medio de detección, las tasas de aprobación de calidad de datos, y el costo de cómputo por canal y por consulta se rastrean contra líneas base. Los umbrales de reversión y cancelación se aplican con base en evidencia, y el costo y la fiabilidad tienen dueños nombrados sujetos a objetivos.
5. Orquestar: Los canales se tratan completamente como software con CI/CD, contratos de datos, y detección automatizada de anomalías que atrapa la deriva antes que los consumidores. La lógica de lotes y flujo se unifica donde la latencia genuinamente lo paga, la plataforma se mejora continuamente y es de autoservicio, y la capacidad, los niveles de almacenamiento y el costo se reequilibran adaptativamente a medida que cambian las cargas de trabajo para que los nuevos productos de datos se envíen rápidamente sobre una base estable.

## Ideas para el debate

- ¿Dónde en tu pila el «tiempo real» realmente se gana su costo, y dónde es un deseo?
- ¿Qué canales no podrían volver a ejecutarse con seguridad hoy, y qué se necesitaría para arreglarlo?
- ¿Cuánto de tu factura de datos en la nube viene de escaneos completos y particiones faltantes?
- ¿Tus analistas consumen data marts modelados o tablas crudas, y qué les cuesta eso?
- ¿Cuál es tu tiempo medio para detectar un incidente de datos, y quién lo encuentra primero?
- ¿Unificar la lógica de lotes y flujo reduciría tu carga de mantenimiento o añadiría riesgo?

## Puntos clave

- Trata los canales como software: control de versiones, pruebas, revisión, CI/CD, y observabilidad.
- Prefiere ELT con modelos estratificados y probados; conserva los datos crudos para reprocesar.
- Elige el lote por defecto y el flujo solo donde la latencia genuinamente lo paga.
- Haz idempotentes las transformaciones para que las reejecuciones sean seguras.
- Modela los datos para los consumidores con esquemas de estrella o tablas anchas deliberadas.
- Monitorea la frescura, el volumen, el esquema y la distribución, y trata los incidentes de datos como interrupciones.
- Optimiza los formatos de almacenamiento, la partición y el costo de cómputo como preocupaciones de primera clase.

## Referencias y lecturas adicionales

- Joe Reis y Matt Housley, «Fundamentals of Data Engineering».
- Ralph Kimball y Margy Ross, «The Data Warehouse Toolkit».
- Martin Kleppmann, «Designing Data-Intensive Applications».
- Bill Inmon, «Building the Data Warehouse».
- James Densmore, «Data Pipelines Pocket Reference».
- Nathan Marz y James Warren, «Big Data» (arquitectura Lambda).
- Barr Moses y colegas, «Data Quality Fundamentals» (observabilidad de datos).
