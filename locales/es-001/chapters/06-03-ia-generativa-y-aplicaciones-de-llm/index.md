# 6.3 Aplicaciones de IA generativa y LLM

## Panorama y motivación

La [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), y en particular los [modelos de lenguaje de gran escala](https://en.wikipedia.org/wiki/Large_language_model) (LLM), son capaces de producir texto fluido, código, resúmenes y datos estructurados a partir de instrucciones en lenguaje natural. Eso los convierte en componentes de gran potencia para asistentes, buscadores, procesamiento de documentos y automatización. Pero esas fortalezas vienen acompañadas de un perfil de riesgo propio. Los LLM son probabilistas: pueden producir afirmaciones erróneas con total confianza (las llamadas [alucinaciones](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Son sensibles a la forma en que se les formula la petición. Y abren nuevas superficies de ataque, como la [inyección de prompts](https://en.wikipedia.org/wiki/Prompt_injection) (instrucciones maliciosas que se cuelan en la entrada para tomar el control del comportamiento del modelo). Por eso, construir aplicaciones de LLM fiables depende menos del propio modelo y más de la ingeniería que lo rodea: cómo se le aporta contexto, cómo se anclan las respuestas en conocimiento confiable, cómo se limitan las salidas y cómo se evalúa la calidad.

En equipos grandes, las aplicaciones de LLM exigen patrones nuevos, distintos tanto del software tradicional como del aprendizaje automático clásico. Con frecuencia no existe una fase de entrenamiento. En su lugar, el comportamiento se moldea mediante prompts, contexto recuperado, definiciones de herramientas y medidas de salvaguardia (comprobaciones en tiempo de ejecución que restringen las entradas y salidas del modelo). Eso desplaza el esfuerzo de ingeniería hacia la gestión del contexto, la calidad de la recuperación, la orquestación y la evaluación. Las empresas que adoptan LLM a gran escala necesitan patrones compartidos para que cada equipo no tenga que redescubrir los mismos modos de fallo de la forma más dura.

En el sector público y en organizaciones reguladas, las exigencias son aún mayores. Un LLM que inventa una cita normativa o que filtra datos sensibles no comete un simple fallo: puede ser un incidente legal o de seguridad. En esos entornos se necesita un anclaje en fuentes autorizadas, una validación estricta de las salidas, supervisión humana en todo lo que tenga consecuencias, y un registro claro de lo que se le pidió al sistema y de lo que este produjo. Las técnicas de este capítulo (la generación aumentada por recuperación, las medidas de salvaguardia y una evaluación rigurosa) son lo que hace viable el despliegue de LLM en contextos de alto riesgo. Los modelos Claude de Anthropic son una de las opciones líderes entre varios proveedores capaces; las prácticas aquí descritas aplican independientemente del modelo que se elija.

## Principios clave

- Anclar al modelo en conocimiento confiable en lugar de fiarse de lo que haya memorizado.
- Tratar los prompts y el contexto como artefactos diseñados y versionados, no como cadenas descartables.
- Partir de la premisa de que el modelo puede equivocarse o manipularse; validar las salidas y limitar las acciones.
- Proporcionar al modelo solo el contexto y las herramientas que necesita, ni una más, para reducir el error y la superficie de ataque.
- Evaluar de forma continua con conjuntos de prueba fuera de línea, métricas en producción y juicio humano.
- Mantener a las personas en el bucle cuando las salidas tengan consecuencias.
- Concebir el modelo como un componente no confiable dentro de un sistema confiable.

## Recomendaciones

### Diseñar prompts y gestionar el contexto de forma deliberada

Trate los prompts como código: guárdelos en control de versiones, revise los cambios y póngalos a prueba contra un conjunto de ejemplos. Estructure cada prompt con claridad: rol y tarea, restricciones, requisitos de formato y, cuando aporten, ejemplos. Considere la ventana de contexto (el tramo fijo de texto que el modelo puede considerar a la vez) como un recurso escaso. Incluya solo la información más pertinente, ordénela con criterio y elimine el ruido, porque el contexto irrelevante o excesivo degrada la calidad y aumenta el coste. En aplicaciones de varios turnos, gestione el estado de la conversación de forma explícita, resumiendo o acortando el historial para mantenerse dentro de los límites sin perder lo esencial. Prefiera instrucciones claras y algunos ejemplos demostrativos (un puñado de casos trabajados incluidos en el prompt) antes que trucos elaborados que se rompen en el instante en que cambia el modelo.

### Anclar las respuestas con la generación aumentada por recuperación (RAG)

En tareas intensivas en conocimiento, recupere documentos relevantes de un corpus confiable y proporcionesélos al modelo como contexto, indicándole que responda únicamente a partir de ese material y que cite sus fuentes. RAG mantiene el conocimiento actualizado sin volver a entrenar, confina las respuestas a contenido aprobado y permite la cita y la verificación. Invierta en la calidad de la recuperación: divida los documentos en fragmentos con criterio, elija [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (representaciones vectoriales numéricas que colocan los significados afines próximos entre sí) adecuados a su dominio, y compruebe que los pasajes recuperados contengan en efecto la respuesta, porque un texto fluido construido sobre el fragmento equivocado es peor que no dar respuesta alguna. Y cuando no aparezca nada relevante, el sistema debe decirlo en lugar de inventar contenido.

### Construir agentes y uso de herramientas con mesura

Los LLM pueden invocar herramientas (búsqueda, bases de datos, calculadoras, APIs internas) y pueden componerse en agentes que planifican y actúan en varios pasos. Eso añade capacidad real, pero multiplica el riesgo: cada herramienta es otra vía por la que un modelo erróneo o manipulado puede causar daño. Defina las herramientas con esquemas precisos, valide cada argumento, aplique el principio de menor privilegio y exija confirmación o aprobación humana para acciones con consecuencias, como enviar comunicaciones o mover dinero. Mantenga los bucles del agente acotados, observables e interrumpibles. Comience con herramientas de alcance estrecho y un solo propósito antes de llegar a la autonomía sin límites.

### Añadir medidas de salvaguardia y validar las salidas

Envuelva el modelo en capas de defensa. En la entrada, filtre y detecte inyecciones de prompts, sobre todo cuando contenido no confiable (páginas web, documentos del usuario) ingresa al contexto. En la salida, valide la estructura contra un esquema, compruebe las afirmaciones contra las fuentes, filtre contenido inseguro o no conforme y rechace o reintentante cuando la validación falle. En salidas estructuradas, parsee y verifique; no confíe en el formato que el modelo produzca. Nunca permita que una salida cruda del modelo dispare acciones irreversibles sin validación. Trate la mitigación de alucinaciones como una propiedad del sistema que se logra mediante el anclaje, la cita, la validación y la revisión humana, no como algo que el modelo resuelve por sí solo.

### Evaluar fuera de línea, en línea y con personas

Construya un conjunto de evaluación con entradas representativas y salidas de referencia conocidas o puntuadas por rúbrica, y ejecútelo ante cada cambio de prompt o modelo (evaluación fuera de línea). Mida el comportamiento real en producción con métricas como tasa de éxito de la tarea, tasa de escalación y retroalimentación del usuario (evaluación en línea). Para la calidad subjetiva, recurra a revisores humanos y, con cautela, a calificación por modelos. La evaluación es la red de seguridad que permite cambiar prompts y modelos con confianza. Sin ella, se opera a ciegas.

## Compromisos: ventajas e inconvenientes

| Elección | Ventajas | Inconvenientes | Cuando conviene |
|---|---|---|---|
| Solo prompts | Sencillo, rápido y barato de modificar | Anclaje limitado; puede alucinar | Tareas amplias de bajo riesgo |
| RAG | Actualizado, anclado y citable | La recuperación es difícil de ajustar bien | Tareas de conocimiento y de carácter factual |
| Agentes con herramientas | Potente, puede actuar | Mayor superficie de ataque, más difícil de controlar | Automatización bien delimitada con salvaguardias |
| Modelo mayor y más potente | Mejor calidad y razonamiento | Mayor coste y latencia | Tareas complejas o de alto riesgo |
| Modelo menor y más económico | Rápido e inexpensivo | Menos capaz en tareas difíciles | Gran volumen y tareas sencillas |

La tensión central es entre capacidad y control (o coste). Mayor autonomía y modelos más grandes entregan más valor, pero exigen más salvaguardias, más evaluación y más presupuesto. El anclaje mediante RAG mejora la fiabilidad a costa de un esfuerzo de ingeniería en la recuperación. El equilibrio adecuado depende de lo que se arriesga: en aplicaciones de alto riesgo conviene inclinarse hacia el anclaje, la validación y la supervisión humana, aunque eso cueste más.

## Preguntas para debatir con el equipo

1. **¿Qué umbral de exactitud y de anclaje debe superar una función de LLM antes de quedar a disposición del público, y quién la aprueba?** Una respuesta fluida que cita la fuente equivocada o inventa una política es peor que no dar respuesta, y en el sector público una cita fabricada es un incidente legal, no un fallo. En un equipo grande, un umbral explícito impide que cada grupo fije su propia barra por instinto. Traiga su definición de «suficientemente anclado»: si cada afirmación debe trazarse a una fuente recuperada y verificada, si el sistema debe rehusarse cuando la recuperación no devuelve nada y qué cubre realmente su conjunto de evaluación adversarial. La señal a vigilar es si alguien puede llevar hoy mismo un cambio de prompt a los usuarios sin ejecutar una prueba de regresión. Si el riesgo es legal o de seguridad, la respuesta debe canalizar las salidas de mayor riesgo a través de un revisor humano con autoridad real antes de su publicación.

2. **¿Cuáles de nuestras funciones de LLM son, en realidad, agentes, y cada herramienta ha recibido el menor privilegio y una puerta humana para las acciones irreversibles?** Cualquier función que permita al modelo invocar herramientas o actuar en varios pasos ha cruzado el umbral de lo que llamamos agente, y cada herramienta es otra vía por la que un modelo erróneo o manipulado puede causar daño. En empresas que conectan LLM a APIs internas, esta pregunta revela riesgos que la etiqueta de «asistente sencillo» oculta. Presente un inventario de cada herramienta que el modelo puede invocar, su validación de argumentos, su ámbito de privilegio y qué acciones (enviar comunicaciones, mover dinero, modificar registros) requieren confirmación. Debata si los bucles del agente son acotados, observables e interrumpibles. La respuesta debe estrechar ámbitos y añadir puertas de aprobación humana donde una acción de peso o irreversible sea hoy alcanzable sin ella.

3. **¿Cómo sabríamos en un día que la calidad de la recuperación ha bajado, cuando una respuesta segura construida sobre el fragmento equivocado se ve bien?** RAG hace confiables las respuestas solo cuando la recuperación efectivamente hace surgir el pasaje que contiene la respuesta, y la recuperación se deteriora en silencio a medida que los documentos cambian, los fragmentos se vuelven obsoletos o los embeddings se alejan del dominio. Como el modelo sigue escribiendo con fluidez sobre un contexto defectuoso, los usuarios quizá no se quejen hasta que la confianza ya se ha perdido. Aporte sus medidas actuales de latencia y recuperación, cómo se comprueba que los pasajes recuperados contienen en efecto la respuesta y cómo la frescura del índice acompaña los cambios documentales. En despliegues de alto riesgo o públicos, debata el registro de las fuentes recuperadas para auditoría, de modo que se pueda rastrear una mala respuesta hasta su fragmento defectuoso. Si no hay ninguna evaluación de la recuperación, se está anclando a la fe.

4. **¿Tratamos los prompts, el contexto y los conjuntos de evaluación como artefactos versionados y revisados, o como cadenas dispersas por cuadernos y registros de chat?** Cuando los prompts se esparcen por equipos sin versión y con duplicados, una corrección en un lugar nunca llega a los demás, y nadie puede reproducir lo que se le pidió al sistema el trimestre pasado. En un equipo grande, un registro compartido de prompts y un conjunto de regresión que se ejecuta ante cada cambio son lo que permite cambiar de modelo o editar una instrucción sin romper silenciosamente una función de otro equipo. La tentación contraria es la velocidad: los ingenieros iteran más rápido cuando pegan un prompt y publican, así que fijen dónde está el límite entre un experimento rápido y lo que toca al usuario. Aporte dónde viven realmente sus prompts hoy, si un conjunto de evaluación hace de puerta de paso ante cada cambio y cómo se versiona el corpus de recuperación junto con el prompt. En entornos empresariales y del sector público, añada la exigencia de auditoría: puede que haya que mostrar, meses después, exactamente qué prompt y qué fuentes produjeron una salida dada, y un prompt que no se pueda reconstruir es un registro que no se puede defender.

5. **A medida que crece el volumen, ¿cómo controlaremos el coste de inferencia sin degradar la calidad en silencio, y quién es el responsable de la decisión de modelo?** El coste total de propiedad de una función de LLM lo domina la inferencia por llamada, y gastos que parecen triviales en un piloto se acumulan con rapidez a escala de producción, lo que tienta a los equipos a bajar de forma discreta a un modelo más débil y esperar que nadie note la caída de calidad. En una organización grande, que cada equipo elija modelos y límites de coste a su antojo produce tanto facturas inesperadas como calidad irregular. El compromiso genuino es entre capacidad y coste (y latencia): un modelo mayor razona mejor en tareas difíciles, uno menor es más barato y rápido en las sencillas, y la caché, el enrutamiento y el alcance de la recuperación mueven la cifra. Aporte el coste por tarea resuelta, la calidad por nivel de modelo en su conjunto de evaluación y dónde el hinchazón del prompt o del contexto está inflando el gasto en tokens. En la presupuestación empresarial y pública, designe quién aprueba la elección del modelo y el techo de gasto, porque una línea de coste sin dueño es una que nadie controla cuando el tráfico se multiplica por tres.

6. **¿Qué datos sensibles pueden llegar al modelo, a dónde van esos datos y podemos demostrar que se mantuvieron dentro de los límites?** Cada prompt, cada documento recuperado y cada resultado de herramienta puede携带 datos personales o confidenciales al modelo y, con un proveedor alojado, fuera del perímetro de la organización; una fuga aquí es un incidente legal o de seguridad, no un ticket de defecto. En un equipo grande que conecta LLM a sistemas internos, el riesgo se esconde en la tubería: un corpus de recuperación que incluye registros que un usuario dado nunca debería ver, o registros que capturan entradas en bruto. La tensión es entre capacidad y exposición, porque la redacción y el acotamiento estricto pueden mermar la función que se intenta construir. Aporte un mapa de flujos de datos de lo que ingresa al contexto, los términos de retención y entrenamiento del proveedor, y cómo se redactan, se acotan y se registran los campos sensibles. En entornos regulados y públicos, vincúlelo a las normas de residencia de datos, los deberes de conservación de registros y los límites contractuales sobre cómo un proveedor puede usar sus datos, porque una supervisión que no se puede acreditar es una supervisión que no existe.

## Perspectiva por sector

**Startup.** Lance una única función de LLM estrecha que toque su valor central, construida sobre un modelo alojado con recuperación sobre su propio contenido, y mantenga los prompts en git tras una capa delgada de interfaz para poder cambiar de proveedor. Antes de cada cambio, ejecute los prompts contra un pequeño archivo de preguntas reales de usuarios para detectar regresiones, filtre el texto que los usuarios pegan para atenuar la inyección de prompts y fije un límite mensual de gasto inflexible. Resista el impulso de los agentes y de la autoalojación: un bucle de invocación de herramientas sin límites que no puede supervisar es una responsabilidad, no una demostración.

**Pequeña empresa.** Probablemente no tiene un especialista en aprendizaje automático, así que adquiera funciones de LLM integradas en las herramientas que ya utiliza en lugar de montar un equipo de desarrollo. Enmarque el riesgo con una pregunta sencilla: ¿dónde una respuesta errónea pero segura le costaría un cliente y quién revisa la salida antes de que salga? Prefiera proveedores que muestren sus fuentes, que permitan mantener a una persona en el bucle y que hagan fácil desactivar la IA cuando se comporta mal.

**Empresa.** El problema es la escala en muchos equipos: publiquen patrones compartidos para RAG, salvaguardias y esquemas de herramientas, junto con un arnés de evaluación común y un registro de prompts, para que cada grupo deje de redescubrir los mismos modos de fallo. Presupueste el coste de inferencia y la revisión humana de forma explícita, estandarice la capa de interfaz para que los modelos sean intercambiables, y gobierne los agentes de forma centralizada con menor privilegio, bucles acotados y registros de auditoría. Gestione las funciones de LLM como un portafolio con métricas y criterios de clausura, no como un puñado de pilotos dispersos.

**Sector público.** La transparencia, las reglas de contratación pública y la rendición de cuentas moldean cada decisión. Ancle estrictamente en fuentes aprobadas con citas, rechace cuando la recuperación no devuelva nada y prohíba al modelo declarar leyes que no pueda citar. Mantenga un responsable designado que revise cada borrador antes de su emisión, registre las entradas y las fuentes recuperadas para auditoría, ejecute un conjunto de evaluación adversarial antes de cada publicación y exija en el contrato la divulgación de las limitaciones del modelo y de las condiciones de manejo de datos.

## Ejemplos

**Startup.** Una startup de tres personas en el sector de herramientas para desarrolladores añadió un asistente de chat sobre su propia documentación para que los usuarios dejaran de escribir correos con preguntas básicas. Usó RAG para que cada respuesta citara una página de documentación concreta, instruyó al modelo a decir «No estoy seguro, aquí les digo a quién preguntar» cuando la recuperación no devolvía nada, y guardó los prompts en git. Antes de cada cambio, ejecutaba los prompts contra un pequeño archivo de preguntas reales de usuarios para detectar regresiones y filtraba el texto pegado por los usuarios para atenuar la inyección de prompts. El asistente resolvía las preguntas habituales y derivaba el resto, sin ruido, a la bandeja compartida de los fundadores.

**Empresa.** Una empresa de software construyó un asistente interno de soporte sobre su documentación de producto. Empleó [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) para que las respuestas citaran páginas concretas de la documentación, indicó al modelo que dijera «No lo sé» cuando la recuperación fallaba, y verificaba que cada fuente citada existiera de verdad. Los prompts estaban bajo control de versiones y se ponían a prueba contra un conjunto de preguntas reales de soporte en cada cambio. El asistente desviaba los tickets rutinarios y escalaba a agentes humanos todo lo que tuviera baja confianza, mientras métricas en línea seguían las tasas de resolución y corrección.

**Sector público.** Un organismo público desplegó un asistente de LLM para ayudar al personal a redactar respuestas a consultas ciudadanas. El anclaje era estricto: el modelo solo podía componer respuestas a partir de pautas aprobadas con citas, y se le prohibía declarar políticas que no estuvieran presentes en las fuentes recuperadas. Un responsable designado revisaba cada borrador antes de su emisión. El filtrado de entradas protegía contra la inyección de prompts proveniente de documentos remitidos por ciudadanos, las salidas se registraban para auditoría y un conjunto de evaluación con casos adversarios y de borde se ejecutaba antes de cada publicación para confirmar que el sistema se negaba a especular en materia de derecho.

## Justificación económica: motivaciones, retorno y coste total de propiedad

Las aplicaciones de LLM generan retorno al automatizar el trabajo intensivo en lenguaje: responder preguntas, resumir documentos, redactar contenido y extraer estructura de texto no estructurado. El valor se manifiesta en tickets desviados, redacción más rápida, menor revisión manual y nuevas capacidades de autoservicio. Como con frecuencia no hay fase de entrenamiento, el tiempo hasta el primer valor es breve, un gran atractivo.

El coste total de propiedad, sin embargo, lo dominan la inferencia continua, la infraestructura de recuperación, los pipelines de evaluación, los sistemas de salvaguardia y la revisión humana. Los costes por llamada se acumulan con rapidez a escala, y una aplicación sin supervisión puede derivar hacia un comportamiento inseguro o caro. El coste de no adoptar es quedarse atrás en calidad de servicio y productividad del personal. El coste de adoptar con descuido es un incidente público de alucinación o una fuga de datos. Presente el caso a la dirección asociando una meta de productividad concreta con un plan de seguridad y evaluación concreto, y presupuestando las salvaguardias y la supervisión humana que mantienen el valor en el tiempo.

## Antipatrones y trampas

- **Confiar en la fluidez.** Tomar por correcto un texto bien escrito y seguro.
- **RAG sin evaluación de recuperación.** Dar por hecho que la recuperación funciona y nunca comprobar si hace surgir los pasajes correctos.
- **Ceguera ante la inyección de prompts.** Alimentar el prompt con contenido no confiable sin defensas.
- **Agentes sin límites.** Dejar que los agentes ejecuten acciones de peso sin restricciones ni aprobación humana.
- **Sin arnés de evaluación.** Cambiar prompts y modelos a ojo, sin pruebas de regresión.
- **Dispersión de prompts.** Prompts esparcidos, sin versión y duplicados entre equipos.
- **Sobreautomatización.** Quitar a las personas de decisiones que cargan con peso legal o de seguridad.

## Modelo de madurez

1. **Iniciación.** Prompts ad hoc en proyectos aislados; sin anclaje, sin salvaguardias ni evaluación; los prompts viven donde cada quien los pegó, y las alucinaciones se descubren en producción.
2. **Desarrollo.** Algunos equipos añaden RAG, control de versiones de prompts, validación básica de salidas y un pequeño conjunto de evaluación manual, pero las prácticas varían de un equipo a otro y dependen de personas individuales en lugar de de una expectativa compartida.
3. **Estandarización.** Se documentan y aplican orgánicamente patrones para RAG, salvaguardias, esquemas de herramientas y control de versiones de prompts; la evaluación automatizada fuera de línea se ejecuta ante cada cambio de prompt o modelo; los flujos de alto riesgo incluyen métricas en línea y revisión humana.
4. **Gestión.** El portafolio se mide frente a líneas de base: la recuperación, las tasas de alucinación y rechazo, la cobertura de defensa ante inyección, el coste y la latencia por llamada, y las tasas de escalación y corrección se siguen en paneles; las puertas de publicación y los criterios de clausura se activan con evidencia, no con opinión, y una prueba de regresión bloquea cualquier cambio que desplace una métrica en la dirección equivocada.
5. **Orquestación.** La evaluación continua, fuera de línea y en línea, se vincula a resultados de negocio; las defensas ante inyección, los agentes y el anclaje se gobernan y se observan; la organización retira, reajusta y reenfoca sus funciones de LLM con regularidad, e intercambia modelos conforme cambian la calidad, el coste y el riesgo.

## Ideas para el debate

- ¿Cómo se decide qué salidas requieren revisión humana antes de su uso?
- ¿Cuál es su estándar de «suficientemente anclado» antes de que una respuesta pueda mostrarse a los usuarios?
- ¿Cómo se defiende contra la inyección de prompts cuando contenido no confiable debe entrar en el contexto?
- ¿Cuándo un agente justifica su riesgo añadido frente a un diseño más simple de una sola llamada?
- ¿Cómo se evalúa la calidad subjetiva a gran escala sin depender en exceso de la calificación por modelos?
- ¿Cómo se mantienen los prompts mantenibles y consistentes entre muchos equipos?

## Ideas clave

- La fiabilidad nace de la ingeniería que rodea al modelo: contexto, anclaje, salvaguardias y evaluación.
- RAG ancla las respuestas en fuentes confiables y habilita la cita y la verificación.
- Trate el modelo como un componente no confiable; valide las salidas y limite el uso de herramientas.
- Otorgue a los agentes el menor privilegio, bucles acotados y aprobación humana para las acciones de peso.
- Evalúe de forma continua, fuera de línea, en línea y con personas; es lo que hace seguro el cambio.

## Referencias y lecturas adicionales

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (guía de ingeniería).
- Louis-François Bouchard y Louie Peters, *Building LLMs for Production*.

---

**Nota sobre la traducción:** He optado por mantener los acrónimos y términos técnicos ampliamente consensuados en la comunidad hispanohablante de IA (LLM, RAG, embeddings, prompt, tokens, APIs, git), ya que su uso en español técnico es natural y su traducción forzaría lecturas artificiales. Los enlaces se han conservado tal cual. En pasajes donde el original es deliberadamente directo y desafiante (como en las preguntas de debate), he buscado un registro que mantenga esa firmeza sin perder naturalidad en español.

