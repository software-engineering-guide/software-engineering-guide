# 11.3 Teoría de colas

## Presentación y motivación

La [teoría de colas](https://en.wikipedia.org/wiki/Queueing_theory) es el estudio matemático de las líneas de espera. En la ingeniería de software, es la teoría silenciosa detrás de una enorme cantidad de práctica. La capacidad de respuesta del servicio al cliente, la planificación [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (un método basado en extracción que limita el [trabajo en progreso](https://en.wikipedia.org/wiki/Work_in_process) para mejorar el flujo), las colas de mensajes entre procesos, los pipelines de despliegue continuo: todos estos son colas, y todos obedecen las mismas leyes. Entender esas leyes permite a un equipo razonar sobre los [tiempos de entrega](https://en.wikipedia.org/wiki/Lead_time), el [rendimiento](https://en.wikipedia.org/wiki/Throughput), la capacidad, y el costo real de ejecutar sistemas cerca de sus límites, en lugar de ser sorprendido por ellos en producción. Este capítulo se ubica en la parte de Flujo porque la teoría de colas es el fundamento formal del flujo: explica *por qué* el trabajo espera, y qué realmente reduce la espera.

Esta es la motivación: la intuición sobre las colas es confiablemente incorrecta, e incorrecta de maneras costosas. La gente asume que un servidor funcionando al 90% de utilización está "a 10% del problema", cuando de hecho los tiempos de espera explotan de manera no lineal conforme la utilización se acerca al 100%. Asumen que agregar trabajo en progreso (WIP) acelera la entrega, cuando en realidad alarga los tiempos de entrega. Planifican la capacidad alrededor de promedios, y luego son destruidos por la variabilidad. Un poco de teoría de colas reemplaza estas intuiciones costosas con un pequeño número de relaciones robustas, la más importante siendo la **[ley de Little](https://en.wikipedia.org/wiki/Little%27s_law)**, que se sostienen tanto en colas de clientes, tableros de tareas, como en pipelines de CI/CD.

Para equipos grandes, empresas, y gobiernos, la teoría de colas es un lenguaje compartido para la capacidad y el flujo, uno que conecta roles que de otro modo hablan sin entenderse. Los gestores de producto se preocupan por el tiempo de entrega desde la idea hasta el cliente. Los SRE se preocupan por la utilización del servidor y la latencia. Los equipos de DevOps se preocupan por la frecuencia de despliegue. Los líderes de soporte se preocupan por los tiempos de respuesta. Todas estas son métricas de cola, y expresarlas en un solo marco (tasa de llegada, tasa de servicio, utilización, tiempo de espera) permite a una organización planificar la capacidad, establecer SLO realistas (objetivos de nivel de servicio), y justificar la inversión con matemáticas en lugar de anécdotas.

## Principios fundamentales

- **Todo lo que tiene una espera es una cola:** tickets, tareas, mensajes, y despliegues incluidos.
- **La ley de Little es el ancla:** elementos en el sistema = tasa de llegada × tiempo en el sistema (κ = λτ).
- **La utilización y el tiempo de espera son no lineales:** el último 15% de la capacidad es el más costoso.
- **La variabilidad es el enemigo del flujo:** los promedios esconden el dolor; la varianza crea colas.
- **Reducir el trabajo en progreso reduce el tiempo de entrega:** el flujo, no la ocupación, es el objetivo.
- **Mide todo el flujo:** llegadas, servicio, éxitos, fallos, omisiones, y esperas.
- **Un proceso es una cola de colas:** modela las etapas, luego optimiza la que restringe.

## Recomendaciones

### Aprende la notación central y úsala consistentemente

Un puñado de cantidades describe cualquier cola. Estandarizarlas (las letras griegas son convencionales) elimina la ambigüedad entre equipos:

- **λ (lambda), tasa de llegada:** qué tan rápido entran nuevos elementos.
- **μ (mu), tasa de servicio:** qué tan rápido se manejan los elementos. Como "tasa de servicio" se usa de manera ambigua, a menudo vale la pena dividir explícitamente el rendimiento en **tasa total (χ)**, **tasa de éxito (α)**, **tasa de fallo (β)**, y **tasa de omisión (σ)**, donde χ = α + β + σ.
- **ρ (rho), utilización / intensidad de tráfico = λ / μ:** el resumen individual más importante. ρ < 1 significa que la cola se drena; ρ ≥ 1 significa que crece sin límite.
- **Tiempos:** tiempo de entrega (τ, de inicio a fin), tiempo de trabajo (φ, procesamiento real), tiempo de espera (ω, pendiente), y tiempo de paso (θ, entre finalizaciones).
- **ε (épsilon), proporción de error:** fallos ÷ total.

Nombrar explícitamente los fallos y las *omisiones* importa en el software: un elemento que se abandona (un cliente que se rinde, un carrito abandonado, un ticket de trabajo rechazado) deja la cola sin ser atendido, y fingir que fue "atendido" corrompe tus métricas. Rastrea el **rechazo** (decidir no unirse), la **deserción** (rendirse después de esperar), y el **cambio de cola** (cambiar de cola) como resultados de primera clase.

### Ancla la planificación en la ley de Little

La ley de Little establece que el número promedio a largo plazo de elementos en un sistema estable es igual a la tasa de llegada promedio multiplicada por el tiempo promedio que cada elemento pasa en el sistema: **κ = λτ** (clásicamente L = λW). Es asombrosamente general (no necesita ningún supuesto sobre la distribución de llegadas o el orden de servicio), lo que la convierte en el caballo de batalla de la planificación de flujo. Reordenada, te dice que el **tiempo de entrega = trabajo en progreso ÷ rendimiento**. Esa es la base matemática de kanban y lean: si quieres tiempos de entrega más cortos y no puedes elevar el rendimiento, debes bajar el WIP. También da verificaciones rápidas de sanidad. Si hay 40 tickets abiertos y cierras 8 por día, el ticket promedio toma aproximadamente 5 días, sin importar qué tan ocupado se sienta cualquiera. Su único requisito es la *estabilidad*: las llegadas no deben exceder persistentemente las salidas (ρ < 1), o la cola, y los supuestos de la ley, se rompen.

### Respeta la no linealidad de la utilización

La lección operativa más importante de la teoría de colas es que el tiempo de respuesta sube abruptamente, no gradualmente, conforme la utilización se acerca al 100%. Las *Siete perspectivas sobre la teoría de colas* de Bob Wescott capturan las consecuencias prácticas vívidamente:

1. Cuanto más lento el centro de servicio, más bajo debería ser el pico de utilización que planifiques.
2. Es muy difícil usar el último 15% de cualquier cosa.
3. Cuanto más cerca del borde operas, más alto el precio de equivocarse.
4. El crecimiento del tiempo de respuesta está limitado por cuántos elementos pueden esperar.
5. Estos son promedios, no máximos: planifica para la cola de la distribución.
6. Cuidado con el efecto de negación humana a través de múltiples centros de servicio.
7. Muestra las pequeñas mejoras en su mejor luz.

La implicación de diseño: **provisiona margen deliberadamente.** Apuntar al 70-80% de utilización para sistemas sensibles a la latencia no es desperdicio; es comprar tiempo de respuesta predecible. Esto informa directamente la planificación de capacidad y los SLO (capítulos 3.5 y 9.1).

### Modela los procesos como una cola de colas

El trabajo real fluye a través de etapas, y un proceso de múltiples etapas es simplemente una cola cuyos elementos a su vez están en cola en cada paso. Modélalo de esa manera: la tasa de llegada del proceso es la tasa de llegada de la etapa 1; la tasa de éxito del proceso es la tasa de éxito de la etapa final; los conteos de errores y omisiones del proceso son las sumas a través de las etapas. Recurren dos formas comunes:

- **Embudos**, donde los conteos de elementos se reducen en cada etapa (contratación: alcance → entrevista → oferta; compra: navegar → carrito → pagar; entrega: integrar → UAT → producción). Optimiza la etapa que más importa: maximiza las llegadas en la parte superior del embudo, minimiza las omisiones a mitad del embudo (abandono de carrito), o minimiza los errores de la etapa final (malos despliegues de producción).
- Flujos de descubrimiento y entrega de **doble diamante** (descubrir → definir → desarrollar → entregar), que la parte de Flujo de este libro trata directamente (capítulo 11.1).

Encontrar y aliviar la **etapa restrictiva** (el cuello de botella) es donde la mejora del flujo rinde frutos; optimizar las no restricciones solo mueve la cola.

### Conecta las métricas de cola con los KPI que los equipos ya usan

Las cantidades de cola se mapean limpiamente a las métricas de entrega y fiabilidad de otras partes de este libro, que es lo que hace que la teoría sea práctica en lugar de académica:

- El **tiempo de entrega de entrega (Dτ)**, "de concepto a cliente", es una medida de tiempo de entrega (τ) y una métrica DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (capítulo 11.2).
- La **frecuencia de despliegue (Dμ)** es una medida de tasa de servicio.
- La **tasa de fallo de cambio (Dε)** es una proporción de error.
- El **tiempo de restauración (Rτ)** es un tiempo de entrega de restauración, es decir, MTTR (capítulo 9.3).

Distingue los varios **MTTR** (tiempo medio para *responder*, *reparar*, *recuperar*, y *resolver*) porque miden diferentes segmentos de la cola de incidentes y rutinariamente se confunden. Fundamentar los SLI/SLO/SLA (capítulo 9.1) en términos de cola mantiene los objetivos honestos y comparables.

## Ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| **Ejecutar sistemas con alta utilización** | Menor hardware/costo por unidad | Explosiones de latencia no lineales; frágil ante picos |
| **Provisionar margen generoso** | Latencia predecible; resiliente a la varianza | Mayor costo en estado estable; parece "subutilizado" |
| **Limitar el WIP (kanban)** | Tiempos de entrega más cortos; menos cambio de contexto | Se siente más lento; requiere disciplina para mantener el límite |
| **Modelado formal de colas** | Decisiones de capacidad cuantificadas; menos sorpresas | Curva de aprendizaje; los modelos simplifican una realidad desordenada |
| **Solo reglas de dedo** | Rápido, sin matemáticas | Incorrecto precisamente donde es más costoso (cerca de la capacidad) |

El intercambio recurrente es **eficiencia frente a previsibilidad**: empujar la utilización hacia arriba ahorra dinero hasta que de repente no lo hace, momento en el cual la latencia, el fallo, y los costos de apagar incendios empequeñecen los ahorros. La contribución de la teoría de colas es decirte *dónde* está ese precipicio para que el intercambio sea una elección, no un accidente.

## Preguntas para discutir con tu equipo

1. **¿Cuál es tu objetivo explícito de utilización para cada sistema sensible a la latencia, y quién lo aprobó?** El margen es una compra deliberada de latencia predecible, así que debería ser una política declarada, no un accidente de la carga que resultó llegar. Como el tiempo de respuesta sube no linealmente, funcionar al 85% ya puede significar latencia de cola elevada, sin embargo finanzas ve el margen como desperdicio y empuja la utilización hacia arriba. Trae los números: la utilización actual, la curva de latencia medida, y el costo de tu último incidente de latencia, luego muestra dónde está el precipicio para cada servicio. Para sistemas empresariales y gubernamentales con picos estacionales (temporada de declaración, ventanas de inscripción), establece el objetivo lejos del precipicio para el período pico, no el promedio. Si nadie posee el objetivo de utilización, los incidentes de latencia seguirán apareciendo "de la nada".

2. **¿Dónde en tus sistemas hay una cola sin límite, sin contrapresión para descargar trabajo cuando se abruma?** Una cola sin límite no falla con gracia; se degrada en colapso, porque las llegadas que exceden persistentemente las salidas (rho >= 1) significan que la cola crece sin límite. Inventaría tus colas de mensajes, grupos de hilos, y búferes de solicitud, y pregunta qué sucede en cada uno cuando la tasa de llegada excede la tasa de servicio: ¿descarga trabajo, aplica contrapresión, o colapsa? Esto importa agudamente a escala empresarial, donde un flujo descendente saturado puede propagarse en cascada a través de los servicios. Trae un resultado de prueba de carga o un incidente pasado donde una cola se atascó, y verifica si el sistema rechazó el exceso de trabajo o intentó retener todo. La solución son colas limitadas con contrapresión explícita y tiempos de espera derivados de la ley de Little, para que una sobrecarga descargue en lugar de derrumbarse.

3. **¿Estás modelando tu flujo de idea a producción como una cola de colas, y tus mejoras están dirigidas a la restricción real?** Un proceso de múltiples etapas es una cola cuyos elementos están en cola en cada etapa, y optimizar cualquier cosa que no sea la etapa restrictiva solo mueve la cola. Mapea tu embudo de entrega (integrar a UAT a producción, o descubrir a definir a desarrollar a entregar) y mide las tasas de llegada, servicio, espera, y omisión en cada etapa para encontrar dónde realmente se acumula el trabajo. Los equipos rutinariamente optimizan la etapa que mejor entienden en lugar del cuello de botella, lo que gasta esfuerzo y no mueve nada. Trae datos de tiempo de espera por etapa, no sensación visceral, porque el cuello de botella a menudo es un estado de espera (revisión, aprobación, disponibilidad de entorno) en lugar de un estado de trabajo. Una vez que conoces la restricción, apunta ahí y deja en paz las no restricciones.

4. **¿Estás usando la ley de Little para establecer límites de WIP, o estás agregando capacidad para curar tiempos de entrega que solo más disciplina arreglaría?** La ley de Little dice que el tiempo de entrega es igual al trabajo en progreso dividido entre el rendimiento, así que si no puedes elevar el rendimiento, la única palanca que queda para tiempos de entrega más cortos es bajar el WIP, lo cual no cuesta nada excepto contención. La atracción en competencia es real: limitar el trabajo en progreso se siente más lento y ocioso, y los gerentes bajo presión preferirían contratar o comprar hardware antes que decirle a los equipos que empiecen menos y terminen más. Trae los números duros, los elementos abiertos actuales y la tasa de finalización por etapa, y calcula el tiempo de entrega promedio implícito, luego compáralo con lo que la gente cree que es; la brecha suele ser grande y vergonzosa. En una gran empresa o agencia, una solicitud de contratación o adquisición justificada como una corrección de tiempo de entrega debería probarse contra esta aritmética primero, porque un aumento de personal que eleva el WIP puede alargar los mismos tiempos de entrega que se suponía debía acortar.

5. **¿Planificas la capacidad alrededor de promedios, o has cuantificado la variabilidad que realmente crea tus colas?** Las colas se forman por la varianza, no por la media, así que dos sistemas con carga promedio idéntica pueden comportarse completamente diferente si uno tiene llegadas a ráfagas o tiempos de servicio de cola larga. La tensión es que los promedios son fáciles de reunir y reconfortantes de reportar, mientras que la varianza y la cola son más difíciles de medir y no bienvenidos en una actualización de estado. Trae la distribución, no la media: la ráfaga de llegadas, los tiempos de servicio y espera de los percentiles 95 y 99, y los tamaños de lote que concentran el trabajo en picos. Para sistemas empresariales y gubernamentales con aumentos predecibles (temporada de declaración, corridas de nómina, ventanas de inscripción, cargas de fin de trimestre), planifica el búfer y el objetivo de utilización a partir de la varianza del período pico, porque un diseño dimensionado para el promedio anual fallará precisamente cuando el público esté observando.

6. **¿Cuáles de tus colas cuentan silenciosamente los abandonos y rechazos como si el trabajo hubiera sido atendido, y qué demanda insatisfecha esconde eso?** Un elemento que rechaza, deserta, o es rechazado deja la cola sin ser manejado, y registrarlo como "atendido" corrompe tu rendimiento, tu proporción de error, y tu plan de capacidad a la vez. La consideración en competencia es que "llamadas respondidas" o "tickets cerrados" se ve mejor en un tablero que "llamantes que se rindieron", así que el número honesto es el que nadie se ofrece a sacar a la superficie. Trae la tasa de omisión (σ), los conteos de rechazo y deserción, y la diferencia entre la carga ofrecida y la carga servida, para que la demanda verdadera se vuelva visible. Esto importa agudamente en la entrega de servicios gubernamentales, donde los ciudadanos que abandonan una cola telefónica o una solicitud de beneficios son obligaciones insatisfechas en lugar de casos resueltos, y reportarlos como manejados tanto tergiversa el desempeño como subestima la capacidad que se le debe al público.

## Perspectiva sectorial

**Startup.** No tienes tiempo para el modelado formal de colas ni lo necesitas. Recurre primero a las dos victorias más baratas: aplica la ley de Little a tu backlog para ver el tiempo de entrega real que implica tu WIP, y vigila tu tablero kanban por la etapa donde se acumula el trabajo antes de contratar contra un cuello de botella que puede no existir. Mantén la utilización lejos del precipicio en cualquier camino sensible a la latencia dejando margen en lugar de ajustarlo, porque una interrupción durante un pico de crecimiento cuesta mucho más que un poco de capacidad ociosa.

**Pequeña empresa.** Sin un especialista en colas en plantilla, compra las métricas en lugar de construir los modelos. Elige una mesa de ayuda, un intermediario de mensajes, o una plataforma de alojamiento que ya reporte la tasa de llegada, el tiempo de espera, y el abandono, y lee esos números en lugar de derivarlos. Enmarca la decisión como vigilar dos síntomas: esperas que suben no linealmente conforme te ocupas más, y clientes que se rinden antes de ser atendidos, ya que un cliente perdido es el costo de cola que más duele a una pequeña empresa.

**Empresa.** El trabajo es hacer del pensamiento de colas una disciplina compartida a través de muchos equipos: una notación acordada (λ, μ, ρ, tiempo de entrega), políticas consistentes de WIP y margen de utilización, y estándares de contrapresión para que un flujo descendente saturado no pueda propagarse en cascada a través de los servicios. Establece los SLO y la capacidad a partir del análisis de colas en lugar de conjeturas, y gestiona tus colas como un portafolio con líneas base y revisiones para que ningún equipo individual funcione caliente en aislamiento. Incorpora el análisis en la gobernanza y auditoría de capacidad, para que un objetivo de margen sea una decisión documentada que alguien posee.

**Gobierno.** La adquisición, la transparencia, y la responsabilidad pública dan forma a cada elección de capacidad. Dimensiona los centros de contacto y los sistemas orientados al ciudadano a partir de la varianza del período pico (temporada de declaración, ventanas de inscripción), no el promedio anual, y dota de personal para mantener la utilización lejos del precipicio cuando aumenta la demanda. Rastrea el rechazo y la deserción como demanda pública insatisfecha en lugar de esconderla dentro de "llamadas respondidas", y justifica el gasto de capacidad con estimaciones de tiempo de espera de la ley de Little, que dan a los auditores y funcionarios electos un caso defendible y respaldado por matemáticas en lugar de una anécdota.

## Ejemplos

**Startup.** Un equipo SaaS de cinco personas ahogándose en un backlog de soporte asume que necesita contratar otro agente. Antes de gastar el dinero, aplican la ley de Little: 60 tickets abiertos y 12 cerrados por día significa que un ticket promedio espera aproximadamente 5 días, lo cual coincide con los correos enojados. Observando su tablero kanban, notan que los tickets se acumulan esperando en ingeniería, no en soporte, así que limitan el trabajo en progreso y enrutan los reportes de errores directo al sprint en lugar de dejarlos en cola. El tiempo de entrega cae a menos de dos días sin ninguna contratación nueva, y usan el presupuesto liberado en el cuello de botella real en su lugar.

**Empresa.** Una plataforma de pagos que dimensiona su servicio de autorización mide λ ≈ 850 solicitudes/segundo y μ por nodo ≈ 200/segundo. Ingenuamente eso son aproximadamente 5 nodos (ρ = 0.85), pero sabiendo que ρ = 0.85 ya significa latencia de cola marcadamente elevada, el equipo provisiona hacia ρ ≈ 0.65 y usa la ley de Little para predecir los conteos de solicitudes en vuelo y establecer profundidades de cola y tiempos de espera. Los incidentes de temporada pico que solían aparecer "de la nada" desaparecen, porque el equipo ya no estaba operando en la parte empinada de la curva.

**Gobierno.** El centro de contacto de una agencia tributaria modela el soporte de temporada de declaración como una cola: picos de llegada (λ), capacidad de agentes (μ), y, críticamente, la **tasa de omisión (σ)** de ciudadanos que abandonan después de largas esperas. Al rastrear el rechazo y la deserción en lugar de solo "llamadas respondidas", el liderazgo ve la verdadera demanda insatisfecha, dota de personal para mantener la utilización lejos del precipicio durante los picos, y justifica la capacidad extra con estimaciones de tiempo de espera de la ley de Little, un caso defendible y respaldado por matemáticas para el gasto público en lugar de uno anecdótico.

## Caso de negocio: motivaciones, ROI y TCO

La teoría de colas rinde frutos previniendo dos errores costosos: el **sobreaprovisionamiento** (pagar por capacidad ociosa que no necesitabas) y, mucho más dañino, el **subaprovisionamiento cerca del precipicio** (donde pequeños aumentos de carga causan gran latencia, SLA violados, clientes abandonados, y gasto de emergencia). Como el costo de funcionar cerca del 100% de utilización es no lineal, los ahorros de "solo agregar un poco más de carga" son pequeños y la desventaja es catastrófica, exactamente la asimetría que un poco de matemáticas convierte en una decisión deliberada. El retorno se mide en interrupciones evitadas, SLA cumplidos, clientes retenidos que de otro modo se rechazarían, y rotaciones de guardia más tranquilas.

En el **costo total de propiedad**, el marco es barato de adoptar (es conocimiento, no herramientas) y mejora casi cada decisión de capacidad, latencia, y flujo que una gran organización toma a lo largo de la vida de un sistema. La ley de Little y los límites de WIP reducen los tiempos de entrega sin comprar nada (una victoria de proceso pura), mientras que la disciplina de utilización cambia un costo modesto y predecible en estado estable por la eliminación de fallos costosos e impredecibles. Para hacer el caso al liderazgo, traduce un incidente de latencia reciente a la curva de utilización y muestra cómo un objetivo de margen lo habría prevenido, y usa la ley de Little para conectar la reducción de WIP directamente con una entrega más rápida.

## Antipatrones y trampas

- **Planificar la capacidad alrededor de promedios:** ignorar la varianza, que es lo que realmente crea las colas.
- **Funcionar caliente:** apuntar a más del 90% de utilización en sistemas sensibles a la latencia y sorprenderse por la latencia de cola.
- **Contar omisiones como servicio:** tratar clientes abandonados o tickets rechazados como manejados, corrompiendo las métricas.
- **Acumular WIP:** confundir la ocupación con el rendimiento y alargar los tiempos de entrega.
- **Optimizar un no cuello de botella:** mejorar etapas que no son la restricción y mover la cola a otro lugar.
- **Confundir los MTTR:** reportar "recuperación" mientras se mide "reparación", o viceversa.
- **Colas sin límite:** sin contrapresión, así que un sistema sobrecargado se degrada en colapso en lugar de descargar trabajo.
- **Promedios como máximos:** diseñar para la media y ser alertado por la cola de la distribución.

## Modelo de madurez

- **Nivel 1 (Iniciar):** Las colas (tickets, tareas, mensajes, despliegues) no se gestionan y son reactivas; la capacidad se adivina; la utilización funciona donde sea que aterrice la carga; los problemas de latencia sorprenden al equipo y se combaten después del hecho.
- **Nivel 2 (Desarrollar):** Algunos equipos reúnen métricas básicas (rendimiento, espera promedio) pero las leen como promedios y las aplican inconsistentemente; algunos grupos limitan el WIP o dejan margen mientras otros funcionan calientes; no hay notación compartida, así que las prácticas no viajan entre equipos.
- **Nivel 3 (Estandarizar):** Una notación común (λ, μ, ρ, tiempo de entrega) está documentada y se aplica en toda la organización; los límites de WIP y los objetivos de margen de utilización se establecen deliberadamente para cada sistema sensible a la latencia; se distinguen los varios MTTR; las colas limitadas con contrapresión son el predeterminado en todos los servicios.
- **Nivel 4 (Gestionar):** Las colas se miden y controlan contra líneas base: la tasa de llegada, la tasa de servicio, la utilización, la latencia de cola (p95/p99), y el tiempo de entrega se rastrean contra objetivos y SLO definidos; las profundidades de cola, los tiempos de espera, y el margen se derivan de la ley de Little en lugar de adivinarse; el rechazo, la deserción, y la tasa de omisión se cuentan para que la carga ofrecida se distinga de la carga servida; las decisiones de capacidad se revisan con esta evidencia, no por sensación.
- **Nivel 5 (Orquestar):** El flujo se modela continuamente como una cola de colas; los cuellos de botella se identifican y alivian como una práctica continua; la capacidad, los SLO, y la contrapresión se adaptan a la demanda y la varianza cambiantes; las métricas de cola se atan directamente a los KPI de DORA y de negocio, y la organización reequilibra la capacidad a través de todo el flujo conforme cambian el panorama de carga y riesgo.

## Ideas para el debate

1. ¿A qué utilización están realmente funcionando tus sistemas sensibles a la latencia, y dónde está su precipicio?
2. Aplica la ley de Little a tu backlog actual: ¿qué tiempo de entrega implica tu WIP ÷ rendimiento, y coincide con la realidad?
3. ¿Cuáles de tus colas cuentan silenciosamente las "omisiones" (abandonos, rechazos) como si hubieran sido atendidas?
4. ¿Dónde bajar el WIP acortaría el tiempo de entrega más económicamente que agregar capacidad?
5. ¿Qué etapa en tu flujo de idea a producción es el verdadero cuello de botella, y tus mejoras están dirigidas ahí?
6. ¿Tus tableros muestran promedios donde la cola de la distribución es lo que realmente te lastima?

## Puntos clave

- Las colas de clientes, los tableros kanban, las colas de mensajes, y los pipelines de despliegue son todos colas gobernadas por las mismas leyes.
- La **ley de Little (κ = λτ)** ancla la planificación de flujo: tiempo de entrega = WIP ÷ rendimiento.
- La utilización y el tiempo de espera son **no lineales**: provisiona margen; el último 15% es el más costoso.
- Rastrea la imagen completa: llegadas, servicio, éxitos, **fallos y omisiones**, y esperas; no dejes que el abandono se esconda.
- Modela los procesos como una **cola de colas** y arregla el **cuello de botella**, no el trabajo ocupado.
- Las métricas de cola se mapean directamente a las medidas de **DORA/flujo** y **SLI/SLO** (capítulos 11.1, 11.2, 9.1), dando a toda la organización un lenguaje para la capacidad y el flujo.

## Referencias y lecturas adicionales

- Bob Wescott, *Seven Insights into Queueing Theory* (y *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): la ley de Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: métricas DORA basadas en flujo que se alinean con los KPI de cola.
- Donald Reinertsen, *The Principles of Product Development Flow*: colas, tamaño de lote, y economía de WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: la ley de Little aplicada a kanban.
- Joel Parker Henderson, *Queueing Theory*: notación, KPI, y cola de colas (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory", "M/M/1 queue", "Little's law", "Markov chain".
