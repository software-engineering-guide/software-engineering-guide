# 2.2 Principios de diseño de software

## Visión general y motivación

Los principios de diseño de software son heurísticas para organizar el código de modo que pueda entenderse, modificarse y extenderse con el paso del tiempo. Incluyen acrónimos de uso extendido ([SOLID](https://en.wikipedia.org/wiki/SOLID), que agrupa cinco principios de diseño [orientado a objetos](https://en.wikipedia.org/wiki/Object-oriented_programming); [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), por *don't repeat yourself* o «no te repitas»; [KISS](https://en.wikipedia.org/wiki/KISS_principle), por *keep it simple* o «mántenlo simple»; [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), por *you aren't gonna need it* o «no vas a necesitarlo»), conceptos estructurales ([acoplamiento](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [cohesión](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [separación de responsabilidades](https://en.wikipedia.org/wiki/Separation_of_concerns)), catálogos de [patrones de diseño](https://en.wikipedia.org/wiki/Software_design_pattern), enfoques de modelado a mayor escala como el [diseño orientado al dominio](https://en.wikipedia.org/wiki/Domain-driven_design) (modelar el software en el lenguaje del propio dominio de negocio) y la elección entre estilos [orientado a objetos](https://en.wikipedia.org/wiki/Object-oriented_programming), [funcional](https://en.wikipedia.org/wiki/Functional_programming) y [orientado a datos](https://en.wikipedia.org/wiki/Data-oriented_design). Ninguno de estos es una ley. Son experiencia condensada, y hay que aplicarlos con criterio.

En equipos grandes, el valor de unos principios compartidos es la coordinación. Cuando cientos de ingenieros trabajan sobre un mismo sistema, necesitan un vocabulario común para los debates de diseño y un conjunto compartido de decisiones por defecto para que los módulos escritos por separado encajen entre sí. Un buen diseño es lo que permite que muchas personas modifiquen un sistema en paralelo sin colisiones constantes. También es lo que lo mantiene modificable una década después, la vida útil habitual de los sistemas empresariales y de la administración pública, mucho más allá del periodo en que trabajaron sus autores originales.

La habilidad crítica no es memorizar principios. Es saber cuándo cada uno te lleva a error. Todo principio tiene un modo de fallo: DRY puede generar la abstracción equivocada, SOLID puede producir indirectiones innecesarias, YAGNI puede asfixiar una extensibilidad que sí se necesita de verdad. Este capítulo trata los principios como herramientas con un ámbito de aplicación determinado, y pone énfasis en el acoplamiento y la cohesión como las propiedades más profundas que los acrónimos intentan servir.

## Principios clave

- Priorizar el acoplamiento y la cohesión; la mayoría de los principios con nombre son caminos indirectos para mejorar estas dos propiedades.
- Optimizar para el cambio: un buen diseño minimiza el coste de los cambios que de verdad se van a tener que hacer.
- Preferir el diseño más simple que funcione ahora, pero mantener los límites donde el cambio es probable.
- La duplicación cuesta menos que la abstracción equivocada; esperar a que el patrón se muestre con claridad.
- Hacer las dependencias explícitas y orientarlas hacia lo estable.
- Modelar el dominio en el lenguaje del propio dominio; alinear los límites del software con los del negocio.
- Elegir paradigmas en función del problema, no de la ideología; la mayoría de los sistemas grandes son pragmáticamente mixtos.

## Recomendaciones

### Usar SOLID como lente, no como lista de verificación

Aplicar la responsabilidad única para mantener los módulos cohesivos, la inversión de dependencias para dirigir las dependencias hacia abstracciones donde existe un límite real, y abierto-cerrado donde los puntos de extensión son genuinos. No fabricar interfaces, factorías ni capas solo para cumplir con el acrónimo cuando solo hay una implementación y no se avista una segunda. La indirección tiene un coste, y se paga en cada lectura.

### Aplicar DRY al conocimiento, no al texto

DRY se refiere a no duplicar una pieza de *conocimiento* con una única fuente de verdad. No se trata de eliminar líneas que solo parecen iguales. Dos fragmentos de código que se parecen pero cambian por motivos distintos deben permanecer separados. Es preferible una duplicación menor a una abstracción compartida prematura que acopla cosas sin relación. Extraer la abstracción una vez que el patrón real se ha manifestado dos o tres veces.

### Dejar que KISS y YAGNI frenen la especulación

Construir para los requisitos que se tienen, no para los que se imaginan. Evitar la generalización especulativa, como marcos configurables, sistemas de complementos y puntos de extensión que nadie ha pedido. El contrapeso es que cierta flexibilidad de verdad resulta más barata de incorporar desde el inicio, como una interfaz estable o una costura limpia. YAGNI argumenta contra la *implementación* especulativa, no contra los límites pensados con cuidado.

### Diseñar para un acoplamiento bajo y una cohesión alta de forma explícita

Que cada módulo haga una sola cosa bien definida (cohesión) y que dependa de lo menos posible de otros módulos, a través de interfaces estrechas (bajo acoplamiento). Al revisar un diseño, preguntarse qué cambios se propagan a través de los límites de los módulos. Esas propagaciones son la verdadera medida del acoplamiento. La separación de responsabilidades es la misma idea aplicada a las capas y a las preocupaciones transversales.

### Usar los patrones de diseño como vocabulario y los antipatrónicos como señales de alerta

Los patrones son nombres compartidos útiles para soluciones recurrentes. Acudir a uno cuando el problema realmente le corresponde. No imponer patrones para parecer sofisticado, porque un código cargado de patrones suele ser signo de sobrediseño. Conocer los [antipatrónicos](https://en.wikipedia.org/wiki/Anti-pattern) comunes (objetos dios, modelos anémicos cuando no proceden, la bola de lodo, el monolito distribuido) como etiquetas diagnósticas.

### Adoptar el diseño orientado al dominio cuando el dominio sea complejo

En sistemas con reglas de negocio ricas, emplear las herramientas tácticas y estratégicas del DDD: un lenguaje unificado compartido con los expertos del dominio, contextos delimitados que dividen el sistema en piezas modeladas de forma independiente y mapas de contextos que describen cómo se relacionan esas piezas. Los contextos delimitados son especialmente valiosos a escala empresarial, porque alinean la responsabilidad de cada equipo con los límites del modelo. El DDD es excesivo para sistemas simples de [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (crear, leer, actualizar, eliminar).

### Elegir paradigmas según su ajuste

Usar la orientación a objetos para encapsular comportamiento con estado y modelar dominios. Usar el estilo funcional para transformaciones, concurrencia y predictibilidad a través de la [inmutabilidad](https://en.wikipedia.org/wiki/Immutable_object). Usar el diseño orientado a datos cuando el rendimiento y el comportamiento de la caché son lo que dominan. Los sistemas grandes combinan los tres. Hacer la elección por componente y mantener limpios los límites entre estilos.

## Compensaciones: ventajas e inconvenientes

| Principio / enfoque | Bien aplicado | Modo de fallo |
|---|---|---|
| SOLID | Costuras claras donde ocurre el cambio; unidades testables | Proliferación de interfaces y capas; indirecto sin beneficio |
| DRY | Una única fuente de verdad para el conocimiento real | Abstracción equivocada que acopla código sin relación |
| KISS / YAGNI | Sistemas esbeltos y comprensibles | Costuras infradiseñadas; costosos retrabajos de flexibilidad necesaria |
| Patrones de diseño | Vocabulario compartido; estructuras probadas | Aplicación ciega de patrones; complejidad accidental |
| Diseño orientado al dominio | Modelos alineados y equipos coordinados; complejidad domada | Ceremonia excesiva sobre dominios simples; límites de contexto mal ubicados |
| Funcional / inmutable | Predictibilidad; concurrencia más segura | Ajuste forzoso para problemas con estado inherente; sorpresas de rendimiento |

La tensión recurrente es entre el infradiseño y el sobrediseño. Los sistemas infradiseñados acumulan acoplamiento y se vuelven rígidos. Los sobrediseñados se ahogan en abstracciones que alguien tiene que entender y mantener. La respuesta no es un punto fijo. Es una disciplina: diferir las decisiones hasta tener información suficiente, al mismo tiempo que se mantienen las costuras que permitan cambiar de opinión.

## Preguntas para debatir con el equipo

1. **¿Cuál es vuestro umbral concreto para extraer una abstracción compartida y cómo evitáis que DRY genere la abstracción equivocada?** Este capítulo es franco: la duplicación cuesta menos que la abstracción equivocada y conviene esperar a que el patrón aparezca dos o tres veces antes de extraerlo. En un equipo grande, el peligro es que alguien factoriza dos fragmentos parecidos en un módulo compartido entre límites de equipo, y entonces cualquier cambio futuro en un llamador se propaga al otro. La señal a aportar es si las duplicaciones cambian por el mismo motivo o si solo se parecen ahora mismo. Acordar una regla de tres y exigir que una abstracción candidata haya cambiado de verdad junto con sus llamadores antes de acoplarlos. Un solo acuerdo de ese tipo evita una clase de acoplamiento muy caro de deshacer cuando ya dependen de ella muchos equipos.

2. **¿Cómo hacéis que el acoplamiento y la cohesión sean visibles en la revisión de diseño en lugar de dejarlos al instinto?** Los principios clave sitúan el acoplamiento y la cohesión por encima de cualquier acrónimo y definen el acoplamiento como los cambios que se propagan a través de los límites de los módulos. La intuición no escala a cientos de ingenieros que solo ven su rincón del sistema. Traer evidencia que una máquina puede producir: gráficos de dependencias y datos de co-cambio que muestren qué módulos se siguen editando juntos en los mismos commits. Añadir una pregunta explícita en la revisión que pregunte qué límites de módulo obliga a cruzar un cambio. Cuando dos módulos siempre cambian juntos, esa es la señal para fusionarlos o corregir el límite entre ellos.

3. **¿Dónde está la línea en vuestros sistemas entre un dominio lo bastante rico para justificar el diseño orientado al dominio y una aplicación CRUD sencilla donde resulta excesivo?** El capítulo recomienda los contextos delimitados del DDD precisamente porque alinean la responsabilidad de los equipos con los límites del modelo, y advierte que el DDD es excesivo para sistemas simples de creación, lectura, actualización y eliminación, y que degenera en pura ceremonia sin modelado real. Equivocarse en uno u otro sentido tiene un coste alto: aplicar DDD pesado sobre un dominio delgado entierra una aplicación sencilla en ceremonias, mientras que un modelo compartido expansivo entre muchos equipos obliga a una coordinación constante entre equipos. Traer las señales que de verdad lo deciden: la densidad de reglas de negocio y cuántos equipos necesitan poseer piezas de forma independiente. Reservar la maquinaria estratégica para el núcleo complejo y dejar que los extremos simples permanezcan simples. Así se evita tanto el teatro DDD como la bola de lodo.

4. **¿Cuándo merece una abstracción, una interfaz o un patrón de diseño la indirección que añade, y quién tiene la autoridad para calificar un diseño de sobrediseñado?** Este capítulo es explícito: la indirección tiene un coste que se paga en cada lectura, y fabricar interfaces, factorías y capas para cumplir con SOLID o para parecer sofisticado es un modo de fallo. En un equipo grande la presión va en sentido contrario: los revisores dejan pasar abstracciones de más porque parecen disciplinadas y nadie quiere ser el que argumente a favor de menos estructura. La consideración contraria es real, porque algunas costuras de verdad justifican su existencia y retirarla después es caro. Traer evidencia concreta al debate: cuántas implementaciones tiene hoy una interfaz, cuántas veces se ha flexionado un punto de extensión y cuántos archivos hay que abrir para seguir un camino de código. Acordar que una implementación única, sin una segunda a la vista, es motivo suficiente por defecto para inlinar, y designar quién puede etiquetar un diseño de sobrediseñado sin que suene a insulto. En sistemas empresariales y de la administración pública que sobreviven a sus autores durante una década, la indirección gratuita es un impuesto que paga cada futuro mantenedor, así que «¿qué nos aporta esta abstracción?» debe ser una pregunta fija en la revisión, no un desafío personal.

5. **¿Cómo decidís qué paradigma usa cada componente, orientado a objetos, funcional u orientado a datos, y cómo mantenéis limpios los límites entre ellos?** El capítulo sostiene que los sistemas grandes son pragmáticamente mixtos y que conviene elegir por componente según su ajuste: orientación a objetos para dominios con estado, estilo funcional para transformaciones y concurrencia, y diseño orientado a datos donde el rendimiento y la caché dominan. Si se deja sin gestionar, la elección de paradigma se convierte en cuestión de quién escribió el módulo primero, el estado mutable se filtra a lo que debería ser una transformación pura, o un purismo funcional choca con un problema de naturaleza estatal. La evidencia que vale la pena aportar es dónde está el dolor real: qué componentes son difíciles de probar por el estado oculto, qué rutas críticas están limitadas por la caché y dónde el estilo actual obliga a contorsiones. Decidir el paradigma por defecto de cada capa de forma deliberada y documentar dónde caen las costuras entre estilos, para que un núcleo funcional y un extremo imperativo no se contaminen mutuamente. En un sistema regulado o de la administración pública donde un cálculo debe ser auditable y reproducible para un periodo dado, un núcleo inmutable y funcional suele ser un requisito de cumplimiento y no una cuestión de gusto, y esa restricción debe conducir el límite, no al revés.

6. **¿Cómo evitáis que estos principios se endurezcan en dogma, y dónde registráis el razonamiento de una decisión de diseño para que un equipo futuro pueda revisarlo?** Todo principio de este capítulo tiene un ámbito de aplicación y un modo de fallo, y el marco general los trata como herramientas que se aplican con criterio, no como leyes que se ejecutan. En un equipo grande, un principio se convierte silenciosamente en una norma: DRY prohíbe toda duplicación, SOLID exige una interfaz por clase, y las excepciones pragmáticas quedan bloqueadas en la revisión por personas que citan el acrónimo en vez del resultado. La tensión es que cierta coherencia de verdad ayuda a cientos de ingenieros a coordinarse, de modo que no se puede declarar cada principio opcional. Traer ejemplos en que seguir un principio al pie de la letra produjo un diseño peor y, si existen, las actas de decisión que explican por qué existe un límite o una abstracción determinada. Acordar que los principios son valores por defecto de los que un ingeniero puede desviarse con un motivo registrado, y capturar las decisiones de diseño de consecuencias en una breve acta de decisión de arquitectura, para que el siguiente equipo herede el razonamiento y no solo el código. En sistemas empresariales y del sector público, donde los autores originales llevan mucho tiempo fuera y las auditorías preguntan por qué el sistema tiene la forma que tiene, ese rastro escrito es la diferencia entre un diseño que los equipos futuros pueden modificar con seguridad y uno del que tienen miedo.

## Perspectiva por sector

**Startups.** Priorizar el diseño más simple que permita publicar y mantener un único módulo bien estructurado hasta que un segundo caso de uso real exija una costura. El recurso más escaso es la atención del ingeniero, así que las interfaces prematuras, las capas adicionales y los marcos especulativos son puro coste. Seguir la regla de tres antes de extraer cualquier abstracción compartida y dejar que YAGNI elimine los puntos de extensión que nadie ha pedido todavía.

**Pequeña empresa.** Sin un arquitecto dedicado y con un presupuesto ajustado, apoyarse en el diseño que ya viene integrado en los marcos y las librerías que se adquieren, en vez de inventar patrones propios. Reservar el esfuerzo de diseño personalizado para el puñado de reglas que de verdad son el negocio, y mantener todo lo demás convencional para que un contratista o un nuevo incorporado pueda leerlo. Una pequeña duplicación que se comprende vale más que una abstracción ingeniosa que solo su autor puede mantener.

**Empresa grande.** El beneficio de los principios compartidos es la coordinación entre muchos equipos: un vocabulario común para la revisión de diseño y contextos delimitados que alinean los límites del modelo con la responsabilidad de cada equipo, de modo que los grupos evolucionen de forma independiente. Gestionar el acoplamiento y la cohesión de forma explícita con datos de dependencias y co-cambio, y registrar las decisiones de diseño relevantes para que los sistemas se mantengan modificables mucho después de que se vayan sus autores. Vigilar por igual la abstracción equivocada que acopla equipos y el sobrediseño que grava a cada lector.

**Administración pública.** La auditabilidad y la reproducibilidad a menudo dictan el diseño. Un núcleo funcional inmutable permite reproducir exactamente un cálculo histórico para un periodo dado, algo que un grafo de objetos enredado con estado mutable oculto no puede garantizar. Preferir contratos publicados explícitos a tablas compartidas en los límites entre contextos, y mantener el diseño y sus registros de decisión legibles para los auditores y para el equipo que herede el sistema una década después.

## Ejemplos

**Startup.** Una startup con tres ingenieros que construye su primer producto resiste la tentación de dividir cada funcionalidad en capas de interfaces y factorías, y mantiene un único módulo bien estructurado hasta que un segundo caso de uso real se manifiesta. Cuando la misma lógica aparece por tercera vez en los flujos de registro y de facturación, extraen una pequeña función compartida en lugar de un marco especulativo. Esto mantiene la base de código lo bastante pequeña como para que cualquiera de ellos la pueda retener en su cabeza, y las pocas costuras que trazan caen justo donde el producto es más probable que cambie.

**Empresa grande.** Una plataforma aseguradora de gran envergadura modela pólizas, siniestros y facturación como contextos delimitados separados, cada uno con su equipo dedicado, su propio modelo de datos y su límite de servicio. Donde los contextos se encuentran, como cuando un siniestro referencia una póliza, se comunican a través de contratos publicados explícitos en lugar de tablas de base de datos compartidas. Esto permite a los tres equipos evolucionar de forma independiente, y el lenguaje unificado mantiene las conversaciones con los corredores y los actuarios precisas. Una versión anterior compartía un único modelo expansivo, y cualquier cambio requería coordinación entre equipos.

**Administración pública.** Un sistema nacional de procesamiento de impuestos prefiere deliberadamente un núcleo orientado a datos y funcional para su motor de cálculo. Las reglas tributarias se expresan como transformaciones puras sobre registros de entrada inmutables, lo que las hace auditables, probables y reproducibles para un ejercicio fiscal dado. Las partes imperativas y con estado (flujo de trabajo, notificaciones) se mantienen en los extremos. Los auditores pueden señalar una versión concreta de una regla y reproducir cualquier cálculo histórico exactamente, lo cual es un requisito legal que un grafo de objetos enredado con estado mutable oculto no podría garantizar.

## Justificación económica: motivaciones, retorno de la inversión y coste total de propiedad

La calidad del diseño es una inversión en la *modificabilidad* de un sistema, y la modificabilidad domina el coste total de propiedad. La mayor parte del coste de un sistema se produce después de su primera publicación, en la modificación y la extensión. Los sistemas bien diseñados mantienen el coste de cada cambio más o menos estable en el tiempo. Los mal diseñados ven cómo el coste de cada cambio se dispara hasta que el sistema se vuelve efectivamente inmodificable y hay que reescribirlo, el resultado más caro de todos.

El coste de adopción es sobre todo de habilidad y disciplina en la revisión: enseñar los principios y dedicar tiempo de diseño desde el principio. El coste de no adoptarlos es la acumulación lenta de [deuda técnica](https://en.wikipedia.org/wiki/Technical_debt), el descenso de la velocidad de entrega, el aumento de la tasa de defectos y, finalmente, los costosos programas de reescritura. Para hacer el caso ante la dirección, vincular la disciplina de diseño con la predictibilidad de la entrega y con la evitación de programas de reescritura, y seguir indicadores anticipados como la tasa de fallo de cambios y el tiempo de implementación de funciones comparables a lo largo del tiempo. Vigilar también el fallo opuesto: sobreinvertir en diseño para futuros inciertos también destruye valor. Así que el argumento es a favor del diseño *apropiado*, calibrado a la probabilidad y al coste del cambio futuro.

## Antipatrónicos y errores frecuentes

- **Generalización especulativa:** construir extensibilidad para requisitos imaginados que nunca llegan.
- **La abstracción equivocada:** forzar la unión de código sin relación para cumplir con DRY, creando un acoplamiento peor que la duplicación.
- **Aplicación ciega de patrones:** aplicar patrones de diseño por el hecho mismo, añadiendo indirección sin beneficio.
- **Objetos dios o modelos anémicos:** modelos sin comportamiento u objetos que lo hacen todo; ambos señalan responsabilidades mal ubicadas.
- **Monolito distribuido:** servicios separados físicamente pero aún fuertemente acoplados, que combinan los costes de ambos enfoques.
- **Bola de lodo:** ninguna estructura discernible; cada cambio pone en riesgo todo.
- **Teatro DDD:** adoptar el vocabulario y la estructura de carpetas sin el modelado de dominio que les da valor.

## Modelo de madurez

- **Nivel 1, Iniciar:** El diseño es ad hoc y reactivo; el acoplamiento se acumula sin control; los principios son desconocidos o se invocan como lemas, y las abstracciones aparecen o desaparecen al antojo de cada cual.
- **Nivel 2, Desarrollar:** Los equipos conocen los principios y los aplican, pero de forma inconsistente y a menudo dogmática; algunos grupos gestionan el acoplamiento y la cohesión de forma deliberada y otros no, y no hay un vocabulario compartido en toda la organización.
- **Nivel 3, Estandarizar:** Un vocabulario de diseño compartido, una regla de tres para extraer abstracciones, un análisis de acoplamiento y cohesión, y contextos delimitados alineados con los equipos están documentados y son esperables en toda la organización, aplicados de forma consistente en la revisión de diseño en lugar de dejarse al gusto individual.
- **Nivel 4, Gestionar:** La salud del diseño se mide frente a líneas de base: los datos de acoplamiento y co-cambio, la tasa de fallo de cambios y el tiempo de implementación de funciones comparables se siguen en el tiempo, de modo que las abstracciones y los límites se añaden, se mantienen o se retiran con base en datos, y el sobrediseño y la abstracción equivocada se detectan por evidencia y no por opinión.
- **Nivel 5, Orquestar:** La disciplina de diseño se integra con la planificación de entrega y de riesgo en toda la organización; los principios se aplican con matices y se conocen sus modos de fallo; las elecciones de paradigma y límite son deliberadas y se revisan de forma continua, y la organización refactoriza, reaborda y retira abstracciones de forma rutinaria a medida que el dominio y la evidencia evolucionan.

## Propuestas de debate

- ¿Cómo distinguir una costura necesaria de una generalización especulativa antes de tener el requisito futuro?
- ¿Cuándo ha llevado DRY a vuestro equipo a la abstracción equivocada y cómo lo reconocieron?
- ¿Dónde deberían caer los límites de los contextos delimitados y hasta qué punto deberían reflejar la estructura organizativa?
- ¿Cuánto diseño debe preceder al código en vuestro contexto y cómo se registran las decisiones?
- ¿Qué partes de vuestro sistema se beneficiarían de un estilo más funcional u orientado a datos?
- ¿Cómo evitáis que los principios de diseño se endurezcan en un dogma que resiste las excepciones pragmáticas?

## Ideas clave

- El acoplamiento y la cohesión son las propiedades que importan; los acrónimos son medios para alcanzarlos.
- Cada principio tiene un modo de fallo; saber cuándo cada uno engaña.
- Preferir una pequeña duplicación a una abstracción prematura o equivocada.
- Usar el DDD y los contextos delimitados para alinear los dominios complejos con la responsabilidad de los equipos.
- Elegir paradigmas según su ajuste; los sistemas grandes son pragmáticamente mixtos.
- Diseñar para los cambios que de verdad se van a necesitar, evitando tanto el infradiseño como el sobrediseño.

## Referencias y lecturas complementarias

- Robert C. Martin, *Clean Architecture* y *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* y *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*

