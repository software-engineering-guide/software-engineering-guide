# 6.6 Infraestructura y operaciones de IA

## Visión general y motivación

La infraestructura y las operaciones de IA son la disciplina que abarca la provisión, planificación y ejecución de los sistemas especializados de cómputo, almacenamiento y servicio que exigen las cargas de trabajo de inteligencia artificial, de manera eficaz en costes, fiable y observable. En la actualidad, la IA resulta costosa de operar. Entrenar y servir modelos de gran escala exige aceleradores escasos (las [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) y las [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), redes de alta banda, almacenamiento vectorial a gran escala para recuperación (índices que representan los datos como vectores numéricos para localizar elementos similares con rapidez) y capas de servicio optimizadas para latencia y caudal. Acertar en esta infraestructura marca la diferencia entre una IA que escala de forma sostenible y una que, en silencio, consume el presupuesto sin rendir resultados a la altura.

En equipos grandes, los problemas centrales son la escala, la escasez y el coste. Los aceleradores son limitados y caros, por lo que la planificación y la utilización cuentan enormemente. Una GPU inactiva es dinero que se malgasta, y una inferencia sin agrupación por lotes multiplica el coste por solicitud. Las aplicaciones con intensa recuperación de información necesitan [bases de datos vectoriales](https://en.wikipedia.org/wiki/Vector_database) que sigan siendo ágiles a medida que crecen. Las aplicaciones de IA generativa requieren control de versiones de indicaciones, pipelines de evaluación y observabilidad (lo que a veces se denomina LLMOps) para operar con seguridad y mejorar en el tiempo. Sin infraestructura compartida y disciplina operativa, cada equipo lucha las mismas batallas y los costes se disparan.

Las instituciones públicas y los entornos regulados añaden exigencias de soberanía de datos, seguridad y previsibilidad en el gasto. Pueden requerir despliegue en premisas o en nube soberana para que los datos y los modelos sensibles no salgan nunca de entornos controlados. Deben prever y justificar el gasto en infraestructura, y cumplir normas de seguridad y disponibilidad. Las decisiones sobre infraestructura de IA en estos contextos tienen consecuencias a largo plazo, por lo que deben tomarse teniendo en cuenta la contratación, la seguridad y las salidas.

## Principios fundamentales

- Tratar el cómputo con aceleradores como un recurso escaso y caro que debe planificarse y explotarse al máximo, no acapararse.
- Optimizar el coste por unidad útil de trabajo, no la capacidad bruta.
- Ajustar el tamaño de los modelos y el hardware a la tarea; la opción más grande rara vez es la más rentable.
- Diseñar el servicio de inferencia pensando en la latencia y el caudal, con el agrupamiento por lotes y la caché como técnicas de primera clase.
- Hacer que los sistemas de IA sean observables: registrar costes, latencias, calidad y errores de forma continua.
- Gestionar las versiones de las indicaciones y los modelos con el mismo rigor que el código.
- Planificar la portabilidad y evitar la dependencia de un proveedor en las decisiones de infraestructura y servicio.

## Recomendaciones

### Planificar y controlar el cómputo con aceleradores

Prever la demanda de entrenamiento y de inferencia por separado, pues tienen perfiles distintos. El entrenamiento es intermitente y se puede planificar; la inferencia es continua y sensible a la latencia. Utilizar planificadores y cuotas para compartir las GPU y las TPU escasas entre equipos, priorizar cargas de trabajo y elevar la utilización. Medir la utilización y considerar la inactividad crónica un problema a resolver. Combinar capacidad reservada para la carga base con capacidad bajo demanda o *spot* para los picos y así controlar el coste. Valorar si aceleradores más económicos o de menor potencia, o incluso la inferencia en CPU para modelos ligeros, serían suficientes. Elegir entre nube, premisas o entornos híbridos en función del coste a escala, las necesidades de soberanía de datos y los patrones de picos, y mantener siempre una vía de salida.

### Construir la infraestructura de recuperación: representaciones vectoriales y bases de datos vectoriales

Para las aplicaciones con recuperación aumentada, poner en marcha la infraestructura que genere [representaciones vectoriales](https://en.wikipedia.org/wiki/Word_embedding) (vectores numéricos que colocan los elementos similares cerca unos de otros) y las almacene en una base de datos vectorial que permita una [búsqueda aproximada del vecino más próximo](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (localizar los vectores más parecidos sin comparar exhaustivamente cada uno) a la escala requerida. Planificar tres aspectos: el coste y la latencia de la generación de representaciones vectoriales, la actualización de los índices a medida que cambian los documentos y la carga operativa de mantenerlos consistentes. Evaluar si conviene una base de datos vectorial dedicada, una extensión con capacidad vectorial de una base de datos ya existente, o un servicio gestionado, según la escala y la tolerancia a la dependencia de un proveedor. Monitorizar la latencia y la recuperación de la búsqueda, porque la calidad de la recuperación determina directamente la calidad de la aplicación.

### Optimizar el servicio de modelos: agrupación por lotes, caché y latencia

El servicio de inferencia es donde se decide el coste y la experiencia del usuario. Utilizar el **agrupamiento por lotes** para procesar varias solicitudes a la vez y elevar el rendimiento del acelerador, equilibrando el tamaño del lote frente a la latencia. Emplear la **caché** de forma agresiva: almacenar respuestas a solicitudes idénticas o semánticamente similares, cachear representaciones vectoriales y aprovechar el caché de prefijos o de indicaciones cuando la plataforma lo permita, para no recalcular contexto compartido. Fijar objetivos de latencia claros y medir la latencia en la cola, no solo la media. Enrutador las solicitudes hacia modelos bien dimensionados: un modelo pequeño para los casos sencillos y uno más grande solo cuando sea necesario. Escalar el servicio de forma automática según la demanda y realizar pruebas de carga antes de cada lanzamiento para conocer la capacidad y la curva de costes.

### Practicar LLMOps: control de versiones de indicaciones, pipelines de evaluación y observabilidad

Tratar las indicaciones como artefactos con control de versiones en repositorios de código, con revisión y capacidad de reversión. Crear pipelines de evaluación que ejecuten suites de prueba de forma automática cada vez que cambien las indicaciones o los modelos, para detectar regresiones antes del lanzamiento. Instrumentar la producción de manera integral: registrar entradas, salidas, latencias, consumo de tokens, costes y errores, con muestreo y salvaguardas de privacidad. Seguir señales de calidad y retroalimentación de usuarios en tiempo real. Esta observabilidad permite detectar degradaciones, controlar costes, depurar fallos y mejorar los sistemas con seguridad: es la columna vertebral operativa de la IA generativa en producción.

### Gestionar el coste de forma rigurosa y observable

Atribuir el gasto en IA a equipos y casos de uso para que sea visible y tenga un responsable. Establecer presupuestos y alertas, monitorizar el coste por solicitud y por resultado, y revisar periódicamente los mayores impulsores de coste. Mover las palancas disponibles: ajuste de tamaño de modelos, caché, agrupación por lotes, recorte de indicaciones y contexto, y elegir el despliegue más económico que cumpla los requisitos. Los costes de IA pueden crecer con el uso de formas inesperadas, por lo que la observabilidad continua del gasto es esencial para evitar sorpresas desagradables.

## Compensaciones: ventajas e inconvenientes

| Decisión | Opción A | Opción B | Compensación |
|---|---|---|---|
| Ubicación del cómputo | Nube | En premisas | Elasticidad y bajo coste inicial frente a control, soberanía y economía en régimen estable |
| Capacidad | Reservada | Bajo demanda / *spot* | Coste previsible frente a flexibilidad y riesgo de interrupción |
| Tamaño del lote | Lotes grandes | Lotes pequeños | Caudal y economía frente a latencia |
| Tamaño del modelo | Modelo grande | Modelo pequeño | Calidad frente a coste y velocidad |
| Almacenamiento vectorial | Base de datos dedicada | Extensión de base de datos existente | Rendimiento a gran escala frente a simplicidad y menor número de sistemas |
| Caché | Agresiva | Mínima | Menor coste y latencia frente a actualidad y complejidad |

La compensación dominante es entre coste y latencia/calidad. El agrupamiento por lotes, la caché y los modelos más pequeños reducen el coste pero pueden aumentar la latencia o reducir la calidad. El equilibrio adecuado depende de la tolerancia de la aplicación. La elección entre premisas y nube intercambia control y economía en régimen estable por elasticidad y bajo compromiso, una decisión condicionada en gran medida por las necesidades de soberanía de datos y la escala.

## Preguntas para debatir con el equipo

1. **¿Cuál es hoy nuestro coste por resultado útil y qué palanca lo movería con mayor efecto?** La capacidad bruta y las medias por solicitud ocultan el dato que de verdad importa: cuánto cuesta entregar una unidad real de valor y cómo escala con el uso. En un equipo grande, la brecha entre un despliegue optimizado y uno sin optimizar suele ser de varios órdenes de magnitud en gasto, de modo que esta pregunta convierte una preocupación difusa por la factura en una lista ordenada de mejoras. Traer el desglose de costes por equipo y caso de uso, las tendencias por solicitud y por resultado, y los mayores impulsores de gasto. Discutir las palancas por orden de impacto: ajuste de tamaño de modelos, caché (incluida caché de prefijos y semántica), agrupación por lotes y recorte de indicaciones o contexto. En el ámbito público, añadir la presión de prever y justificar el gasto plurianual. La respuesta debe asignar a cada mayor impulsor de coste un responsable y una palanca concreta, no una encogida de hombros.

2. **Si nuestro proveedor de inferencia actual duplicara su precio o dejara de operar mañana, ¿con qué rapidez podríamos cambiar?** La dependencia de un proveedor se construye en silencio y duele al escapar, y las capas de servicio son donde se esconde con más fuerza. Para grandes empresas y, sobre todo, para instituciones públicas, la portabilidad es un requisito de contratación y continuidad, no un capricho. Traer la arquitectura: si los modelos están tras una interfaz interna, si las indicaciones y las suites de evaluación son portables, y cuánto se depende del comportamiento de servicio específico de un proveedor. La señal a vigilar es si alguien ha ejecutado nunca la suite de evaluación contra un segundo proveedor o un segundo objetivo de despliegue. Si cambiar llevara meses y requiriera reescribir caminos críticos, tratarlo como un defecto de diseño a resolver ya, pues las opciones de nube soberana o en premisas pueden volverse obligatorias sin apenas aviso.

3. **¿Cuál es ahora mismo nuestra utilización de aceleradores y cuánto nos cuesta la inactividad de las GPU y la inferencia sin agrupar?** Los aceleradores son escasos y caros, por lo que la inactividad crónica y el servicio por solicitud individual drenan en silencio presupuestos que podrían financiar más capacidad. En una organización que comparte GPU entre equipos, esta pregunta revela si la planificación, las cuotas y las prioridades mantienen realmente la utilización alta, o si lo habitual es un hardware acaparado y subutilizado. Traer cifras reales de utilización, la postura en agrupación por lotes y caché, y mediciones de latencia en la cola (no solo medias), porque son las colas lentas las que el usuario percibe. Discutir si la demanda de entrenamiento y de inferencia se prevén por separado, dado su perfil distinto, y si un modelo más pequeño o la inferencia en CPU bastaría para los casos ligeros. La respuesta debe señalar capacidad inactiva concreta para recuperar y solicitudes concretas para agrupar o enrutar a un modelo de tamaño adecuado.

4. **Cuando se publica un cambio de indicación o de modelo, ¿qué impide que una regresión de calidad o de coste llegue a los usuarios en silencio?** Una capa de servicio puede parecer saludable en latencia y disponibilidad mientras las respuestas que devuelve se degradan sin que nadie lo note, o una indicación nueva duplica el consumo de tokens por solicitud. En un equipo grande donde muchos grupos editan indicaciones y cambian modelos de forma independiente, un cambio sin control es un incidente en producción a la espera de ocurrir, y su radio de impacto crece con cada equipo en la plataforma compartida. Traer la cobertura de evaluación: qué indicaciones y modelos tienen suites de prueba offline, si esas suites se ejecutan automáticamente con cada cambio, qué umbrales de calidad y coste actúan como puerta de lanzamiento y con qué rapidez se puede revertir. Discutir si las indicaciones viven en el control de versiones con revisión o si aún alguien puede editar una indicación de sistema en vivo a mano. En entornos corporativos y públicos, vincular cada cambio a una trazabilidad registrada y a un aprobador con nombre, porque un regulador que pregunte «¿quién cambió esto y qué se probó» necesita una respuesta documentada, no recordada.

5. **¿Cómo decidimos entre nube, premisas y despliegue soberano, y hemos calculado la economía real en régimen estable o solo la del piloto?** La elección de ubicación del cómputo define la curva de costes, la postura de soberanía de datos y las opciones de salida durante años, y con frecuencia se toma sobre la factura de un piloto en la nube que nada tiene que ver con la producción a escala. En una organización grande, la capacidad elástica en la nube resulta barata al principio y puede convertirse en la línea de gasto más importante cuando la inferencia se ejecuta de forma continua, mientras que el despliegue en premisas intercambiando bajo compromiso por control y economía en régimen estable. Traer las previsiones de volumen de entrenamiento e inferencia, el punto de equilibrio donde el hardware reservado o propio supera al de demanda, las restricciones de residencia de datos y de seguridad, y los patrones de picos que justifican un enfoque híbrido. En entornos públicos y regulados, sopesar los requisitos de nube soberana o premisas que pueden volverse obligatorios sin apenas aviso, y comprobar que la arquitectura mantiene los modelos tras una interfaz interna para que un cambio forzado de proveedor o plataforma soberana no deje desamparado a nadie.

6. **¿Llegamos a asumir la responsabilidad de nuestro gasto en IA y cada equipo puede ver y responder del coste que genera?** El gasto en IA crece con el uso de formas sorprendentes, y sin atribución la factura llega como un número opaco del que nadie se siente responsable de reducirlo. En una organización grande, un coste que nadie posee es un coste que nadie optimiza, de modo que la pregunta es si el gasto se etiqueta por equipo y caso de uso con presupuestos, alertas y tendencias por resultado, o si solo se descubre cuando finanzas escalará. Traer el modelo de atribución de costes, los mayores impulsores por equipo y las palancas que cada responsable controla: ajuste de tamaño, caché, agrupación por lotes y recorte de contexto. Para presupuestos empresariales y públicos, añadir la disciplina de prever y justificar el gasto plurianual en infraestructura, pues una institución que no pueda explicar su factura de cómputo línea por línea tendrá dificultades para defenderla ante una auditoría.

## Perspectiva por sector

**Startup.** No poseer ninguna infraestructura que pueda evitarse. Usar una API de inferencia alojada, enrutar las solicitudes sencillas a un modelo pequeño y barato y reservar el mayor para los casos difíciles, y cachear agresivamente para que las indicaciones repetidas no cuesten nada. Emplear una base de datos vectorial gestionada en lugar de operarla en propia casa, mantener las indicaciones en un repositorio de código con un breve script de evaluación antes de cada cambio, y registrar el coste por solicitud para que el aumento del gasto aparezca antes de que duela. El recurso más escaso es la atención del equipo de ingeniería, por lo que conviene comprar operatividad y mantener el cambio de proveedor barato.

**Pyme.** Sin equipo de plataforma, tratar el servicio, la recuperación y la observabilidad como cosas que se adquieren dentro de herramientas ya existentes, no como sistemas que precisan personal dedicado. Preferir la inferencia gestionada y la búsqueda vectorial gestionada con precios transparentes y predecibles, y establecer un tope de gasto y una alerta de facturación desde el primer día. Plantear la decisión de comprar o construir con honestidad: operar GPU o un índice vectorial rara vez compensa al volumen que se maneja, y un modelo pequeño tras una API alojada suele cubrir la necesidad con una fracción del esfuerzo.

**Gran empresa.** El reto es una plataforma de referencia compartida para muchos equipos: aceleradores en pool con planificadores, cuotas y prioridades para elevar la utilización, agrupación por lotes y caché estandarizadas, enrutadores de ajuste de tamaño y costes atribuidos a cada equipo y caso de uso. Controlar los cambios de indicaciones y modelos con suites de evaluación automatizadas, estandarizar la capa de interfaz para que proveedores y objetivos de despliegue sean intercambiables, y gestionar el coste por resultado como una métrica de primera clase, en lugar de que cada grupo reinvente infraestructura costosa y subutilizada.

**Sector público.** La soberanía de datos, la seguridad y la previsibilidad del gasto condicionan cada decisión. Preferir el despliegue en premisas o en nube soberana para que los datos y modelos sensibles permanezcan dentro de entornos controlados, planificar el uso de las GPU escasas entre departamentos con cuotas justificables en la contratación, y prever la capacidad para defender el gasto plurianual línea por línea. Gestionar versiones y evaluar indicaciones y modelos antes de cada lanzamiento, mantener una observabilidad integral de costes y calidad, y conservar los modelos tras una interfaz interna para que un cambio forzado a un nuevo proveedor o a una plataforma soberana no suponga un callejón sin salida.

## Ejemplos

**Startup.** Una pequeña startup que operaba una función de escritura con IA mantuvo su factura bajo control sin poseer una sola GPU. Utilizaba una API de inferencia alojada, enrutaba las solicitudes sencillas a un modelo pequeño y barato y reservaba el mayor para los casos difíciles, y cachear las respuestas a las indicaciones repetidas. Guardaba sus indicaciones en un repositorio de código con un breve script de evaluación que se ejecutaba antes de cada cambio, usaba una base de datos vectorial gestionada para la recuperación sin tener que operar la suya propia, y registraba el coste por solicitud para que los fundadores pudieran ver cómo el gasto aumentaba antes de que se convirtiera en una sorpresa.

**Gran empresa.** Una compañía mediática que operaba una función de IA de gran tráfico recortó sustancialmente los costes de inferencia. Enrutaba las solicitudes sencillas a un modelo pequeño y reservaba un modelo mayor para los casos complejos. Cachear las respuestas a las consultas repetidas y activó la caché de prefijos para su indicación de sistema compartida. Hizo circular las GPU por un planificador compartido para mantener la utilización alta, gestionó todas las indicaciones en un repositorio de código con una suite de evaluación automatizada que controlaba cada cambio, e instrumentó el coste por solicitud para que cada equipo de producto asumiera la responsabilidad de su gasto.

**Sector público.** Un organismo nacional con estrictas normas de soberanía de datos desplegó sus sistemas de IA en sus propias instalaciones para que los datos y modelos sensibles no salieran nunca de su entorno controlado. Planificó el uso de las GPU escasas entre departamentos con cuotas y prioridades, previó la capacidad para justificar la contratación plurianual y construyó una plataforma de búsqueda vectorial para la recuperación en documentos oficiales. Las indicaciones y los modelos se versionaban y evaluaban antes de cada publicación. Una observabilidad integral seguía los costes y la calidad, y la arquitectura mantenía los modelos tras una interfaz interna para preservar una vía de salida y evitar la dependencia de un proveedor.

## Caso de negocio: motivaciones, retorno de la inversión y coste total de propiedad

La motivación de una infraestructura de IA disciplinada es sencilla. La IA a gran escala es costosa, y la brecha entre un despliegue optimizado y uno sin optimizar suele ser de varios órdenes de magnitud en gasto. El retorno de la inversión proviene de una mayor utilización de los aceleradores, un menor coste por solicitud mediante el agrupamiento por lotes y la caché, modelos bien dimensionados y la evitación de la sobredimensionación. La observabilidad y los pipelines de evaluación se recuperan impidiendo incidentes costosos y permitiendo iteraciones seguras.

El coste total de propiedad abarca el cómputo con aceleradores (la línea más gruesa para muchas cargas de trabajo), el almacenamiento vectorial, la infraestructura de servicio, la red y el personal de plataforma y operaciones que la sostiene. Contraponer esto al coste de no invertir: facturas de inferencia descontroladas, latencias deficientes que frenan la adopción y la incapacidad de escalar. En el sector público, añadir el coste de incumplir requisitos de soberanía o seguridad. Presentar el caso a la dirección mostrando las tendencias de coste por resultado y una plataforma de referencia que permita a muchos equipos desplegar IA de forma eficiente, en lugar de que cada uno construya infraestructura costosa y subutilizada.

## Antipatrones y errores frecuentes

- **Aceleradores inactivos.** Asignar GPU escasas a equipos que las dejan subutilizadas.
- **Sin agrupación por lotes ni caché.** Servir cada solicitud de forma individual y recalculando el contexto compartido.
- **El modelo más grande por defecto.** Usar un modelo caro donde un pequeño bastaría.
- **Ceguera ante los costes.** Sin atribución, presupuestos ni visibilidad del coste por solicitud hasta que llega la factura.
- **Indicaciones sin control de versiones.** Modificar indicaciones en producción sin versión ni puerta de evaluación.
- **Descuido de la latencia en la cola.** Optimizar la latencia media mientras los usuarios sufren las colas lentas.
- **Dependencia silenciosa de un proveedor.** Construir en profundidad sobre la capa de servicio de un único proveedor sin portabilidad.

## Modelo de madurez

1. **Iniciar.** Asignación de GPU ad hoc a quien pide con más insistencia, sin agrupación por lotes ni caché, sin visibilidad de costes hasta que llega la factura, indicaciones editadas en vivo y sin versión, con monitorización mínima.
2. **Desarrollar.** Algunos equipos adoptan planificación compartida, caché e indicaciones con control de versiones, pero la práctica es desigual en la organización: un grupo agrupa y evalúa mientras otro sigue sirviendo cada solicitud de forma individual y cambia las indicaciones a mano.
3. **Estandarizar.** Una plataforma de referencia documentada se impone en toda la organización: planificación compartida con cuotas y prioridades, agrupación por lotes, caché y ajuste de tamaño estándar, infraestructura vectorial para la recuperación, pipelines de evaluación automatizados que controlan cada cambio de indicación o modelo, y atribución de costes a equipos y casos de uso.
4. **Gestionar.** La plataforma se mide y controla respecto a líneas base: la utilización de los aceleradores, el coste por resultado útil, la latencia en la cola, la recuperación de la búsqueda y las regresiones de calidad por cambio se rastrean con alertas y umbrales, cada equipo asume la responsabilidad de su coste y la decisión de avanzar o no con un cambio se toma con evidencia, no con intuición.
5. **Orquestar.** La infraestructura mejora y se adapta de forma continua: el enrutamiento, la agrupación por lotes y el escalado se ajustan solos a las señales vivas de coste y calidad, la capacidad se reequilibra entre equipos y entre objetivos en la nube, en premisas y soberanos a medida que cambian la demanda y las restricciones, la portabilidad se ensaya de forma periódica y la planificación de infraestructura se integra con producto, seguridad y contratación.

## Ideas para la reflexión

- ¿Cómo elevar la utilización de los aceleradores sin asfixiar las cargas de trabajo prioritarias?
- ¿Dónde está el punto óptimo entre agrupación por lotes y caché para los requisitos de latencia?
- ¿Cuándo justifica el despliegue en premisas o soberano su coste frente a la nube?
- ¿Cómo atribuir y controlar el gasto en IA entre muchos equipos?
- ¿Qué debe controlar el paso de un cambio de indicación o modelo a producción?
- ¿Cómo mantener la infraestructura de servicio lo suficientemente portable para cambiar de proveedor?

## Puntos clave

- Los aceleradores son escasos y caros; hay que planificarlos, compartirlos y explotarlos a propósito.
- La agrupación por lotes, la caché y el ajuste de tamaño de los modelos son las palancas principales de coste y latencia.
- Las aplicaciones de recuperación necesitan una infraestructura bien operada de representaciones vectoriales y búsqueda vectorial.
- El LLMOps (control de versiones de indicaciones, pipelines de evaluación y observabilidad) es la columna vertebral operativa de la IA generativa.
- Gestionar el gasto de forma observable y preservar la portabilidad para evitar la dependencia de un proveedor.

## Referencias y lecturas complementarias

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, eds.).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.

