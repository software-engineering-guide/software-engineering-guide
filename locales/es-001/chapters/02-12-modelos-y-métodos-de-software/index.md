# 2.12 Modelos y métodos de software

## Visión general y motivación

Un modelo es una simplificación deliberada de un sistema, concebida para responder a una pregunta concreta. Un método es una forma disciplinada de producir software, que incluye los modelos que utiliza a lo largo del proceso. En conjunto, constituyen un área de conocimiento del SWEBOK (Cuerpo de Conocimiento de la Ingeniería del Software), porque son las herramientas mentales con las que razonas sobre un sistema antes, durante y después de construirlo. Un diagrama de clases UML (Lenguaje Unificado de Modelado), un diagrama de entidad-relación, un autómata de estados, una especificación formal y un prototipo desechable son todos ellos modelos. Waterfall, el prototipado, el desarrollo formal y ágil son todos ellos métodos.

¿Para qué sirve un modelo? Porque la memoria de trabajo humana es pequeña y los sistemas de software son grandes. Nadie puede retener en la cabeza un sistema de cien mil líneas de código, así que dibujamos esquemas y escribimos abstracciones que muestran una faceta a la vez: los datos, el flujo de control, los estados, las interacciones. Ningún modelo pretende ser fiel al código; pretende ser adecuado para una decisión. Un buen modelo muestra exactamente lo necesario para decidir algo y oculta todo lo demás.

En equipos grandes, lo que realmente está en juego es la coordinación y la comunicación. Cuando cientos de ingenieros, arquitectos, analistas y auditores trabajan en un mismo sistema, los modelos compartidos son el terreno común donde negocian el diseño, los requisitos y el riesgo. Piensa, pues, en la modelización como una herramienta con una tarea concreta: compensa cuando un modelo cuesta menos que el error que previene. Se convierte en desperdicio cuando lo dibujas por el mero hecho de dibujarlo, lo conservas mucho después de que se ha vuelto obsoleto o lo elaboras más allá de la decisión que debía servir. La modelización se conecta estrechamente con los requisitos de software (capítulo 2.8), los principios de diseño (capítulo 2.2), la arquitectura y sus notaciones, como C4 y arc42 (capítulo 3.1), y los enfoques ágiles (capítulo 10.7).

## Principios clave

- Todo modelo tiene un propósito; si no puedes nombrar la decisión que informa, no lo dibujes.
- La abstracción es el acto central de modelar: incluye lo relevante para el propósito y omite el resto.
- La coherencia importa dentro de cada modelo y entre los distintos modelos; unos modelos contradictorios son peores que la ausencia de modelos.
- Los modelos son, ante todo, artefactos de comunicación; su público determina la notación y el nivel de detalle.
- Prefiere el modelo más ligero que responda a la pregunta; la elaboración conlleva un coste de mantenimiento.
- Un modelo es tan bueno como su análisis; un modelo sin verificar es un supuesto no probado.
- Elige el método según la incertidumbre, el riesgo y la consecuencia de la falla del problema.

## Recomendaciones

### Modela con abstracción, propósito y coherencia

Empieza todo modelo nombrando su propósito y su público. Después, abstracte con rigor hacia ese propósito: un diagrama de secuencias destinado a resolver una condición de carrera debe mostrar tiempos y mensajes, no cada campo. Mantén tus modelos coherentes entre sí, de modo que las entidades de un diagrama de entidad-relación, las clases de un diagrama de clases y los sustantivos de los requisitos coincidan, y coherentes con la realidad, lo que significa que actualizas o eliminas un modelo cuando el sistema ha avanzado. Un modelo obsoleto que la gente confía en él es un peligro. Un modelo obsoleto que todos ignoran es un gasto que, aun así, consume atención.

### Elige modelos estructurales o conductuales según la pregunta

Usa modelos estructurales para mostrar de qué está hecho un sistema y cómo se relacionan sus partes: diagramas de clases, diagramas de componentes y diagramas de entidad-relación para la estructura de datos. Usa modelos conductuales para mostrar lo que un sistema hace a lo largo del tiempo: autómatas de estados para objetos con ciclos de vida significativos, diagramas de secuencias para interacciones entre componentes y diagramas de actividades para flujos de trabajo y procesos de negocio. Elige la notación que ponga en evidencia la decisión que tienes delante. La mayoría de los sistemas necesitan solo un puñado de tipos de diagrama, seleccionados con criterio, no el catálogo completo de UML aplicado a todo.

### Analiza los modelos, no solo los dibujes

Un modelo justifica su existencia mediante el análisis, no solo al dibujarse. Revisa un autómata de estados en busca de estados inalcanzables, transiciones omitidas y bloqueos mutuos. Examina un diagrama de entidad-relación en busca de problemas de normalización y relaciones huérfanas. Recorre un diagrama de secuencias frente a los requisitos para hallar caminos de error ausentes. Revisa tus modelos con los expertos de dominio, quienes pueden detectar lo que está mal. Y cuando el coste de la falla es elevado, recurra a análisis asistido por herramientas (verificadores de modelos, verificadores de coherencia, simulación) en lugar de confiar en la inspección visual.

### Aplica métodos heurísticos como norma

La mayor parte del software se construye con métodos heurísticos: enfoques basados en la experiencia, iterativos, que usan modelos de forma informal y evalúan los resultados frente a expectativas en lugar de frente a demostraciones. Para la mayoría de los sistemas empresariales y gubernamentales, eso es exactamente lo correcto: los requisitos evolucionan y un defecto suele ser recuperable. Los métodos heurísticos encajan de forma natural con el enfoque ágil (capítulo 10.7): modeliza lo suficiente para alinear al equipo y luego construye y aprende.

### Reserva los métodos formales para los núcleos de alta consecuencia

Los métodos formales expresan especificaciones en lenguaje matemático y emplean verificación, ya sea por demostración o por verificación exhaustiva de modelos, para establecer propiedades. Exigen una formación y un tiempo reales, y compensan precisamente cuando la falla es catastrófica o irreversible: control de sistemas críticos para la seguridad, protocolos criptográficos, núcleos de liquidación financiera y similares. Aplícalos al pequeño núcleo crítico, no al sistema en su conjunto. Y ten en cuenta que, incluso sin una demostración completa, una sola especificación formal suele aportar valor solo por el hecho de obligarte a ser preciso.

### Usa el prototipado para disipar la incertidumbre

Cuando los requisitos o la viabilidad son inciertos, construye un prototipo para aprender y decide, deliberadamente, si evolucionarlo o descartarlo. Los prototipos desechables exploran una cuestión de forma económica y luego se eliminan. Los prototipos evolutivos se convierten en el producto y deben construirse con estándares de producción desde el principio. El fracaso clásico es que un prototipo desechable se infiltre en producción por accidente. Así que define el tipo de prototipo antes de construirlo.

### Ajusta el método al riesgo, no a la moda

Elige los métodos según la incertidumbre del problema y la consecuencia de la falla. La alta incertidumbre favorece el prototipado y la iteración ágil. La alta consecuencia favorece el análisis formal y la verificación rigurosa. Un sistema con ambas necesidades exige un núcleo formal crítico dentro de un marco ágil. Lo que sea que hagas, no adoptes un método solo porque resulte prestigioso o porque un proveedor lo esté vendiendo.

## Contrapartidas: ventajas y desventajas

| Modelo o método | Aplicado con acierto | Modo de fallo |
|---|---|---|
| Modelos estructurales (UML, diagramas de entidad-relación) | Imagen compartida de las partes y los datos | Proliferación de diagramas; desfasaje respecto al código |
| Modelos conductuales (estados, secuencias, actividades) | Revelan tiempos, estados y casos límite | Diagramas sobredetalados que nadie lee |
| Métodos heurísticos | Rápidos, flexibles, adecuados para la mayoría de los sistemas | Falta de disciplina; supuestos ocultos |
| Métodos formales | Propiedades demostrables para núcleos críticos | Coste elevado; aplicación indevida al sistema entero |
| Prototipado | Aprendizaje barato; retira el riesgo a tiempo | Código desechable promovido a producción |
| Métodos ágiles | Se adaptan a requisitos cambiantes | Omiten la modelización necesaria para problemas difíciles |

La tensión recurrente es entre rigor y velocidad. Demasiada poca modelización envía supuestos ocultos a producción. Demasiada modelización quema esfuerzo en diagramas que nunca informan una decisión y se desfasan en el instante en que el código cambia. No existe una dosis fija que resuelva esto; solo una regla de proporción: invierte en un modelo o en un método en proporción a la incertidumbre que resuelve y al coste de tomar la decisión equivocada. Un motor de pagos y un micrositio de marketing merecen tratamientos muy distintos.

## Preguntas para debatir con tu equipo

1. **¿Analizamos nuestros modelos o simplemente los dibujamos y pasamos página?** Un modelo justifica su existencia mediante el análisis, no por el mero hecho de existir: un autómata de estados que nadie revisa en busca de estados inalcanzables o transiciones omitidas es un supuesto no probado disfrazado de diagrama. En un equipo grande, ahí es donde se esconden los defectos reales, porque una imagen verosímil genera confianza justo cuando nadie ha recorrido su diagrama frente a los requisitos para hallar el camino de error que falta o la relación huérfana que nadie conectó. Lleva al encuentro vuestro modelo conductual más importante e intentad romperlo: ¿qué transición está indefinida, qué estado no tiene salida, qué secuencia no tiene un tiempo de espera? Cuando el coste de la falla es alto, la respuesta debería empujaros hacia el análisis asistido por herramientas (verificadores de modelos, verificadores de coherencia, simulación) en lugar de la inspección visual, porque toda la razón de modelar un núcleo crítico es hallar la fallada en una pizarra y no en producción.

2. **¿Cuando dos de nuestros modelos se contradicen, cuál prevalece y quién nota la contradicción?** La coherencia importa dentro y entre modelos, y los modelos contradictorios son peores que la ausencia de modelos, porque la gente actúa en función de ambos. En un sistema grande, las entidades del modelo de datos, las clases del diseño y los sustantivos de los requisitos se desfasan en silencio mientras equipos distintos actualizan artefactos distintos, y la primera señal suele ser un defecto en producción donde dos componentes discreparon sobre qué es una cosa. Trae un ejemplo: elige un concepto central y comprueba si el diagrama de entidad-relación, el código y los requisitos coinciden realmente en su forma y en su ciclo de vida. Si no coinciden, decide qué artefacto es la fuente autorizada y quién es responsable de mantener a los demás en sintonía, y ten el valor de eliminar un modelo antes que dejar que uno obsoleto siga engañando al equipo.

3. **¿Qué núcleo de nuestro sistema, si se equivoca, pierde dinero real o perjudica a alguien, y recibe el rigor que merece?** El movimiento central de este capítulo es ajustar el método al riesgo: métodos heurísticos y ágiles para la mayoría recuperable, especificación formal y verificación para el pequeño núcleo de alta consecuencia, y prototipado económico para lo genuinamente incierto. Los modos de fallo son simétricos y ambos caros: aplicar métodos formales a un micrositio de marketing quema presupuesto, y tratar un motor de liquidación o un conjunto de reglas de elegibilidad como trabajo ágil ordinario invites el defecto catastrófico e irreversible. Lleva un mapa de vuestro sistema y marca dónde un error es catastrófico frente a recuperable y dónde los requisitos son ciertos frente a desconocidos. La respuesta debería concentrar vuestra inversión en modelización donde están el dinero y la ambigüedad, y retirarla explícitamente en todo lo demás, para que un núcleo formal crítico pueda coexistir dentro de un marco ágil sin que ninguno de los dos métodos se filtre al terreno del otro.

4. **¿Cuánta modelización hacemos antes de escribir código, y cambia esa dosis con la incertidumbre que tenemos delante?** Un diseño exhaustivo desde el inicio y la ausencia total de diseño son ambos modos de fallo, y la dosis adecuada se sitúa entre ambos, gobernada por cuánto incertidumbre un modelo retira realmente. En un equipo grande, la presión actúa en ambos sentidos: un proceso de gobernanza puede exigir un conjunto completo de diagramas antes de cualquier línea de código, cerrando decisiones tomadas con la menor información posible, mientras que la presión de entrega puede llevar a un equipo a saltarse el único autómata de estados que habría capturado un caso límite costoso. Trae vuestros dos proyectos más recientes y separa los modelos que produjisteis en los que informaron una decisión real y los que se dibujaron solo porque una plantilla los pedía. En programas empresariales y gubernamentales, donde una fase de control o un comité de aprobación suele exigir documentos de antemano, presenta argumentos a favor de una modelización que siga el riesgo en lugar de una lista fija de entregables, para que el núcleo de pagos reciba su rigor y la herramienta interna de informes no se ahogue en diagramas que nadie lee.

5. **¿Hemos acordado una notación compartida y un lugar único para nuestros modelos, o cada equipo inventa la suya?** Los modelos son, ante todo, artefactos de comunicación, y su valor se derrumba cuando un autómata de estados dibujado en la herramienta de un equipo no puede leerse, encontrarse o confiarse por el equipo que lo hereda. Para cientos de ingenieros, las tensiones son reales: una notación y un repositorio obligatorios compran coherencia y descubribilidad, pero también imponen un coste de aprendizaje y pueden empujar a la gente hacia herramientas pesadas cuando una pizarra fotografiada bastaría. Trae ejemplos de dónde vivió realmente un modelo (una wiki, una herramienta de diagramas, una presentación de diapositivas, el portátil de alguien) y pregúntate quién pudo encontrarlo y comprenderlo seis meses después. En entornos empresariales y regulados, el ángulo de la auditoría agudiza esto: un auditor que no puede localizar el modelo de datos actual ni trazar una decisión hasta un autómata de estados documentado tratará el sistema como si no estuviera documentado, así que acordad una notación pequeña y compartida y un lugar duradero, y aceptad la captura ligera antes que la ceremonia siempre que la consecuencia sea baja.

6. **¿Antes de construir un prototipo decidimos de forma deliberada si es desechable o evolutivo, y nos hacemos responsables de esa decisión?** El fallo clásico y caro es que un prototipo desechable se infiltre en producción por accidente porque demostró bien y nadie definió su tipo de antemano. La tensión es genuina: los prototipos desechables compran el aprendizaje más barato posible y deben eliminarse, mientras que los prototipos evolutivos se convierten en el producto y deben construirse con estándares de producción desde la primera línea, y confundir ambos o bien desperdicia trabajo de rehacer o bien envía código frágil a un papel para el que nunca se lo ingenierizó. Trae un prototipo reciente y pregúntate qué se decidió antes de construirlo, quién tuvo autoridad para promoverlo o descartarlo y si esa decisión resistió la presión de la entrega. En entornos gubernamentales y de otro tipo donde rige la rendición de cuentas, donde un sistema orientado al ciudadano conlleva obligaciones de transparencia y fiabilidad, tratad la promoción accidental como un fallo de control: fijad el destino del prototipo de antemano y considerad el descarte de un prototipo desechable exitoso un logro digno de celebrarse, no un gasto a evitar.

## Enfoque por sector

**Startups.** Modeliza en una pizarra, fotografía el resultado y sigue adelante. Tu recurso más escaso es la atención de los ingenieros, así que acude a un modelo solo cuando es más barato que el error que previene: un autómata de estados del ciclo de suscripción antes de codificar los casos límite de facturación, no un catálogo completo de UML para un producto que puede pivotar el mes que viene. Mantente en el terreno heurístico y ágil, deja los métodos formales completamente fuera de la mesa y trata todo prototipo como desechable a menos que decidas conscientemente lo contrario.

**PyMEs.** Es probable que nadie tenga como misión la modelización formal, así que apóyate en los modelos que ya vienen integrados en las herramientas y marcos que compras en lugar de poner en pie una práctica de modelización propia. Enmarca los pocos modelos que dibujes en decisiones concretas: un boceto de modelo de datos para acordar qué datos del cliente guardáis, un diagrama de estados para el único flujo que os hace perder un cliente cuando se rompe. Prefiere un producto adquirido con un modelo de datos probado antes que construir y documentar el vuestro, y mantén lo que dibujes lo bastante ligero para que una sola persona pueda mantenerlo al día.

**Empresas.** El problema central es la coordinación entre muchos equipos, así que los modelos compartidos se convierten en el terreno común: un modelo de datos acordado, una notación consistente y un lugar donde el diagrama de entidad-relación, los diagramas C4 y los autómatas de estados pueden encontrarse y confiarse. Estandariza una notación pequeña y exige la coherencia para que las entidades de los requisitos, del diseño y de la base de datos no se desfasen entre equipos. Reserva la especificación formal y la verificación de modelos para los núcleos de alta consecuencia (liquidación, conciliación, control de accesos), financia el talento especializado que eso exige y mantén una trazauditoría que ligue cada modelo documentado a la decisión que justificó.

**Sector público.** Las normas establecidas en la ley deben ser trazables al texto legal, y ahí es donde la especificación formal justifica su coste: especificad con precisión la lógica de elegibilidad o de evaluación, verificad las propiedades clave y permitid que los auditores rastreen cada resultado hasta la regla que lo produjo. Los procesos de contratación añaden su propio peso, ya que los documentos y modelos suelen ser entregables contractuales, así que acordad qué modelos son genuinamente decisivos frente a los que solo se producen para cumplir una lista de verificación. Publicad descripciones en lenguaje cotidiano de cómo funcionan los sistemas de mayor trascendencia y usad prototipos desechables para probar la recogida de datos ante usuarios reales antes de comprometeros con una construcción de producción.

## Ejemplos

**Startup.** Una pequeña empresa emergente que desarrolla un producto de facturación por suscripción dibuja en una pizarra, antes de escribir código, el ciclo de vida de la suscripción (prueba, activa, en morosidad, cancelada, reactivada) como un autómata de estados. Al recorrer el diagrama, descubren que nunca definieron qué ocurre cuando el pago de una cuenta en morosidad finalmente se liquida, un caso límite que habría dejado a clientes reales en el limbo. Ese modelo de cinco minutos evita un dolor de cabeza en producción, y lo fotografían en lugar de mantener una herramienta de diagramas pesada. En todo lo demás se mantienen ágiles y modelizan lo justo para alinear al equipo, porque a su escala un defecto es recuperable y los métodos formales serían un gasto puro.

**Empresa.** Un banco global construye una nueva plataforma de pagos. El equipo usa un diagrama de entidad-relación para acordar el modelo de datos compartido entre los equipos de cuentas, contabilidad y mensajería, y diagramas C4 (capítulo 3.1) para mostrar cómo encajan los servicios entre sí. Modelizan el ciclo de vida de la transacción (pendiente, liquidada, conciliada, revertida, en disputa) como un autómata de estados explícito, y el análisis revela que falta una transición para los reversales parciales. La brecha se corrige en la pizarra en lugar de en producción. Los diagramas de secuencias recorren el flujo de liquidación frente a los requisitos (capítulo 2.8) para hacer aflorar caminos de tiempo de espera y reintento que faltaban. La entrega diaria es ágil, pero el algoritmo de conciliación, donde un error significa dinero real perdido, recibe una especificación formal y se verifica mediante model checking antes de implementarse. La modelización se concentra donde están el dinero y la ambigüedad y se mantiene ligera en todo lo demás.

**Sector público.** Una agencia tributaria nacional moderniza la evaluación de prestaciones. Dado que las reglas de elegibilidad están fijadas en la ley y son objeto de auditoría, el equipo redacta una especificación formal de las reglas como transformaciones puras y verifica propiedades clave, como que ningún solicitante sea simultáneamente elegible y no elegible y que cada caso llegue a una decisión, para que los auditores puedan rastrear los resultados hasta la norma que los originó. Junto al núcleo formal, el equipo construye un prototipo desechable del formulario de solicitud para el ciudadano y lo pone a prueba con usuarios reales. Descubren que un asistente multipasos reduce los errores, y luego descartan el prototipo y reconstruyen el formulario con estándares de producción. Los diagramas de actividades documentan el proceso de fin a fin del trabajador social para la formación y la auditoría. Las reglas de alta consecuencia reciben rigor formal; la experiencia de usuario incierta recibe prototipado económico; ningún método se aplica donde corresponde el otro.

## Justificación empresarial: motivación, retorno y coste total de propiedad

El retorno de la modelización proviene de hallar defectos antes, donde son mucho más baratos de corregir. Una contradicción detectada en una pizarra cuesta minutos. La misma contradicción detectada en producción puede costar una interrupción del servicio, un programa de reconstrucción o, en dominios regulados, una responsabilidad legal. Los modelos también reducen el coste total de propiedad al servir como comunicación duradera. Un sistema que sobrevive a sus autores (lo normal en entornos empresariales y públicos) es mucho más barato de mantener cuando su modelo de datos, sus autómatas de estados y sus flujos clave están documentados con precisión.

Los costes son reales y hay que ponderarlos. Los modelos requieren tiempo para construirse, habilidad para construirse bien y esfuerzo continuo para mantenerlos al día; los métodos formales añaden personal especializado. El punto de equilibrio lo gobiernan la incertidumbre y la consecuencia. Cuando ambas son bajas, la modelización pesada destruye valor y los heurísticos ágiles ganan. Cuando alguna de las dos es alta, la modelización dirigida (y, para el núcleo crítico, la verificación formal) se recupera con creces previniendo la clase de fallo más costosa. Para hacer el caso ante la dirección, vinculad la inversión en modelización a riesgos concretos retirados y a la mantenibilidad de sistemas de vida prolongada. Y seguid el rastro de si los modelos se consultan realmente, porque un modelo sin uso es un gasto puro.

## Antipatrones y trampas

- **Modelar por modelar:** producir diagramas porque un proceso lo exige, no porque informen una decisión.
- **Modelos obsoletos de los que se confía:** diagramas que ya no coinciden con el código pero a los que sigue confiando la gente.
- **Diseño exhaustivo desde el inicio:** modelos agotantes producidos antes de cualquier código, que cierran decisiones tomadas con la menor información.
- **Proliferación de diagramas:** cada tipo de UML aplicado de forma uniforme, ahogando en ruido los pocos puntos de vista útiles.
- **Métodos formales por todas partes:** aplicar una verificación costosa a código donde la consecuencia de la falla no la justifica.
- **Promoción accidental de prototipos:** un prototipo desechable que se publica en producción sin que nadie se haya dado cuenta.
- **Notación por encima de la sustancia:** discutir sobre la corrección de la notación UML en lugar de si el modelo responde a la pregunta.

## Modelo de madurez

- **Nivel 1 (Iniciación):** La modelización es puntual o inexistente y puramente reactiva; no se nombra ningún método; los modelos, cuando se dibujan, son incoherentes, sin análisis y se abandonan en cuanto termina la reunión.
- **Nivel 2 (Desarrollo):** Algunos equipos dibujan diagramas habituales y siguen un método nombrado, pero la práctica es desigual en toda la organización: los modelos se producen de forma ceremonial, se desfasan respecto al código y rara vez se analizan en busca de defectos.
- **Nivel 3 (Estandarización):** Se definen y aplican a nivel de organización una notación compartida, una guía de selección de métodos documentada y reglas de coherencia; los modelos se eligen por su propósito, se mantienen en sintonía con el sistema, se revisan en busca de defectos y el método se ajusta al riesgo de cada problema.
- **Nivel 4 (Gestión):** La modelización se mide y controla frente a líneas base; los equipos rastrean cuántos defectos captura el análisis antes de la implementación, cuánto se desfasan los modelos del código, si cada modelo se consultó realmente para una decisión concreta y cuánto trabajo de rehacer y tiempo de ciclo se ahorró frente a una línea base definida; la elección del método se calibra a la incertidumbre y la consecuencia medidas, y los núcleos críticos se verifican formalmente frente a objetivos de cobertura acordados.
- **Nivel 5 (Orquestación):** La modelización y la selección de métodos se mejoran de forma continua y se integran con la entrega y la planificación de riesgos en toda la organización; la inversión se adapta a medida que la incertidumbre y la consecuencia cambian, los modelos se mantienen al día, se retiran o se profundizan según la evidencia, y los métodos formal, heurístico y de prototipado se componen de modo que cada uno ocupa exactamente donde rinde.

## Propuestas de debate

- ¿En vuestro último proyecto, qué modelos informaron una decisión real y cuáles se dibujaron solo porque un proceso lo exigía?
- ¿Dónde en vuestros sistemas una especificación formal se pagaría sola y dónde sería un gasto?
- ¿Cómo decidís si un prototipo es desechable o evolutivo, y os hacéis responsables de esa decisión?
- ¿Cómo evitáis que los modelos se desfasen del código, o aceptáis que algunos deben eliminarse?
- ¿Cuál es la cantidad adecuada de modelización antes del código en vuestro contexto, y cómo cambia con la incertidumbre?
- ¿Qué modelo conductual (de estados, de secuencias o de actividades) habría captado vuestro incidente de producción más reciente?

## Ideas clave

- Un modelo es una abstracción con propósito; si no puedes nombrar la decisión que informa, no lo dibujes.
- Ajusta los modelos estructurales y conductuales a la pregunta concreta y mantenlos coherentes y actualizados.
- Analiza los modelos; un modelo sin verificar es un supuesto no probado.
- Los métodos heurísticos y ágiles encajan con la mayoría de los sistemas; reserva los métodos formales para los núcleos de alta consecuencia.
- Usa los prototipos para disipar la incertidumbre y decide de antemano si son desechables o evolutivos.
- Invierte en modelización en proporción a la incertidumbre que resuelve y al coste de tomar la decisión equivocada.

## Referencias y lectura adicional

- IEEE Computer Society, *SWEBOK Guide (Guía del Cuerpo de Conocimiento de la Ingeniería del Software), Versión 4.0*, área de conocimiento de Modelos y Métodos de Ingeniería del Software
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* y *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (el lenguaje de modelado Alloy)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (el modelo C4)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*

