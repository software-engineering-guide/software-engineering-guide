# 6.1. Estrategia y preparación en inteligencia artificial

## Contexto y justificación

La [inteligencia artificial](https://en.wikipedia.org/wiki/Inteligencia_artificial) ha dejado de ser una curiosidad de laboratorio para convertirse en una capacidad esencial que las grandes organizaciones se esperan ya que desplieguen con responsabilidad y a gran escala. Para empresas y organismos públicos, la pregunta que ya no importa no es si la IA puede lograr algo impresionante en una demostración. Lo que de verdad está en juego es si una inversión concreta resuelve mejor un problema real que las alternativas, si puede operarse con seguridad durante años y si resistirá la auditoría, las normas de contratación y el escrutinio público. La estrategia de IA es la disciplina de decidir dónde aplicarla, dónde abstenerse y qué cimientos se necesitan antes de que el primer modelo llegue a producción.

En equipos grandes, la escala y la inercia elevan la apuesta. Una iniciativa mal planteada puede consumir presupuestos, desviar el esfuerzo de ingenieros brillantes y erosionar la confianza de reguladores y ciudadanos cuando fracasa ante los ojos de todos. Una iniciativa bien elegida, en cambio, puede suprimir el trabajo mecánico, extraer conocimientos de datos a los que antes era imposible acceder y liberar a personas cualificadas para tareas de mayor valor. La diferencia rara vez reside en el propio modelo: depende de cómo se enmarque el problema, del grado de preparación de los datos y los equipos y de lo honesta que sea la justificación económica.

En contextos públicos y regulados se añaden más restricciones. Las administraciones tienen que justificar el gasto, garantizar la transparencia, evitar la discriminación arbitraria y rendir cuentas ante los cargos elegidos y ante la ciudadanía. Las normas de contratación pueden prohibir la dependencia exclusiva de un solo proveedor, exigir explicabilidad y requerir que los proveedores expongan el comportamiento de sus modelos. En estos entornos, la conformidad normativa, la auditabilidad y las opciones de salida deben tratarse como requisitos de primer orden, no como añadidos de última hora.

## Principios fundamentales

- Partir de un problema que merezca la pena resolver, no de una tecnología que busca aplicación.
- Optar por el enfoque más simple que cumpla el objetivo: la IA es una opción entre muchas, y a menudo no la mejor.
- Considerar la preparación de datos, los talentos disponibles y la madurez de la plataforma como prerrequisitos, no como frentes de trabajo paralelos para resolver después.
- Tomar decisiones explícitas entre construir, adquirir, afinar o emplear prompting, y revisarlas a medida que cambian el mercado y las capacidades internas.
- Cuantificar el coste total de propiedad, incluyendo operación, supervisión y sustitución eventual, no solo la licencia o el piloto.
- Diseñar para la salida desde el primer día: evitar arquitecturas que encarezcan prohibitivamente el cambio de proveedor o de modelo.
- En entornos regulados y públicos, tratar la transparencia, la conformidad de contratación y la rendición de cuentas como restricciones de diseño.
- Medir el coste de *no* actuar junto al coste de actuar.

## Recomendaciones

### Enmarcar el problema antes de elegir tecnología

Redactar una declaración de un página sobre el problema. Nombrar la decisión o la tarea que se pretende mejorar, el punto de partida actual, el resultado medible buscado y lo que ocurre cuando el sistema se equivoca. Luego plantearse si el problema encaja siquiera con la IA. ¿Hay datos suficientes y relevantes? ¿La tarea es de tipo patrón y no de reglas fijas? ¿Se toleran respuestas probabilísticas? ¿Puede una persona comprobar el resultado? Muchos problemas se resuelven mejor con software determinista, con un mejor diseño de procesos o simplemente con una higiene de datos más rigurosa. Anotar con claridad dónde la IA *no* encaja: por ejemplo, en decisiones que la ley exige que sean perfectamente explicables, o donde el coste de un error infrecuente es catastrófico e imposible de detectar.

### Aplicar un árbol de decisiones: prompting, recuperación, afinado, adquisición o construcción

Progresar de lo más económico y rápido a lo más costoso y controlado:

1. **Emplear prompting con un modelo alojado.** Si un modelo generalista (como Claude de Anthropic u ofertas comparables de otros proveedores) resuelve el problema con prompting cuidadoso y recuperación de documentos, empezar por ahí. Es la opción de menor coste, la que permite iterar más rápido y no requiere infraestructura de entrenamiento.
2. **Complementar con recuperación o herramientas.** Si la brecha es de conocimiento o de acción, añadir [generación aumentada por recuperación](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), que obtiene documentos relevantes en el momento de la consulta y los aporta como contexto al modelo, o integrar herramientas antes de tocar los pesos del modelo.
3. **Afinar o adaptar el modelo.** Si el prompting no alcanza de forma consistente la precisión, el tono o el formato requeridos, [afinar](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) un modelo más pequeño con los propios datos: es decir, completar su entrenamiento con ejemplos propios para especializarlo. Esto se paga en control a cambio de una pipeline de [operaciones de aprendizaje automático](https://en.wikipedia.org/wiki/MLOps) (MLOps).
4. **Adquirir un producto especializado.** Para dominios bien definidos (procesamiento de documentos, puntuación de fraude), un producto maduro de un proveedor puede superar cualquier solución interna.
5. **Construir desde cero.** Reservar el entrenamiento de [modelos de base](https://en.wikipedia.org/wiki/Foundation_model) (modelos grandes preentrenados en datos diversos y adaptables a múltiples tareas) para organizaciones con datos singulares, talento profundo y razones estratégicas. Para casi todas las empresas y organismos, esta no es la opción adecuada.

### Establecer prerrequisitos de datos, talento y plataforma

Auditar los datos en cuanto a disponibilidad, calidad, etiquetado, trazabilidad y base legal de uso. Confirmar que se tiene efectivamente derecho a emplearlos con fines de IA, incluyendo datos personales o de terceros. Evaluar con honestidad el talento disponible: se necesitan científicos de datos, pero también ingenieros de aprendizaje automático, ingenieros de datos, gestores de producto que entiendan los sistemas probabilísticos y revisores capaces de evaluar los resultados. Antes de escalar, poner en marcha una base de plataforma: seguimiento de experimentos, un registro de modelos (el sistema de referencia para las versiones entrenadas y su estado de aprobación), supervisión y servicio seguro, para que cada nuevo caso de uso no tenga que reinventar la operación.

### Abordar los contextos regulados y públicos con deliberación

Incorporar desde el principio a los equipos de contratación, jurídica y gestión de riesgos. Exigir a los proveedores que divulguen el origen del modelo, las prácticas de entrenamiento, los resultados de evaluación y las limitaciones conocidas. Preferir contratos que garanticen la portabilidad de datos y prompts y evitar formatos propietarios que generen dependencia. Donde proceda, publicar el propósito y las salvaguardas de los sistemas de IA orientados al público y ofrecer a las personas un canal para impugnar decisiones automatizadas. Alinearse con marcos de referencia reconocidos (véase el capítulo 6.5) para que las auditorías encuentren un proceso documentado y defendible.

### Calcular el coste total de propiedad y prevenir la dependencia del proveedor

Modelar el coste de todo el ciclo de vida: inferencia o licencias, pipelines de datos, revisión humana, supervisión, reentrenamiento, respuesta a incidentes y desmantelamiento final. Compararlo con el coste del statu quo y con el de las alternativas. Reducir la dependencia del proveedor situando el modelo tras una interfaz interna, conservando los prompts y los conjuntos de evaluación portables y probando periódicamente un segundo proveedor.

## Compromisos: ventajas e inconvenientes

| Enfoque | Ventajas | Inconvenientes | Cuándo conviene |
|---|---|---|---|
| Prompting con modelo alojado | Rápido, económico, sin infraestructura, fácil de cambiar | Menor control, coste por llamada, dudas sobre el intercambio de datos | Prototipos, tareas amplias, requisitos aún inciertos |
| Aumento por recuperación | Ancla las respuestas en los propios datos, fácilmente actualizable | La calidad de la recuperación es difícil de garantizar; añade infraestructura | Tareas intensivas en conocimiento |
| Afinado de modelo pequeño | Mayor control, menor coste por llamada a gran escala, opción local | Requiere MLOps, datos y mantenimiento | Tareas estables, de alto volumen y especializadas |
| Adquisición de producto | Probado, con soporte, rápido para generar valor | Coste de licencia, dependencia del proveedor, ajuste limitado | Problemas commodity bien definidos |
| Construcción de modelo de base | Control máximo y diferenciación | Coste enorme, talento escaso, riesgo elevado | Casi nunca, fuera de los laboratorios de vanguardia |

El compromiso dominante es entre control y coste/velocidad. El prompting ofrece mayor velocidad y flexibilidad, pero menor control; construir ofrece el máximo control, pero exige recursos que pocas organizaciones deberían destinar. La mayoría de los equipos grandes deberían situarse en el medio: primero prompting y recuperación, luego afinado selectivo y, para necesidades commodity, adquisición. La dependencia del proveedor trueca la comodidad a corto plazo por el riesgo a largo plazo, y esto importa especialmente en el sector público, donde las obligaciones de salida a varios años son habituales.

## Preguntas para debatir con el equipo

1. **¿En qué peldaño de la escala *prompting*, recuperación, afinado, adquisición o construcción se sitúa cada uno de nuestros tres casos de uso prioritarios, y qué evidencia lo elevaría o bajaría un peldaño?** Esto importa porque la mayoría del gasto desperdiciado en IA procede de empezar un peldaño demasiado alto: entrenar un modelo cuando un prompting riguroso habría bastado. En un equipo grande, acordar la escala como norma compartida evita que cada grupo reinvente una pipeline costosa. Traer la declaración de problema de una página de cada candidato, el punto de partida actual y una lectura honesta de si la brecha es de conocimiento (recuperación), de consistencia (afinado) o de un problema ya resuelto (adquisición). En entornos empresariales y públicos, añadir el coste de contratación y auditoría de cada peldaño, porque un modelo afinado arrastra una carga de MLOps que una llamada alojada no tiene. La respuesta debería permitir descartar o reducir al menos un proyecto sobredimensionado.

2. **¿Cuál es nuestro plan de salida concreto para el proveedor o el modelo del que más dependemos, y lo hemos ensayado de verdad?** La dependencia del proveedor se acepta barata y se deshace cara, y en el sector público pueden existir obligaciones de salida a varios años que no se podrán cumplir si nunca se han ensayado. Traer la lista de funciones propietarias de las que se depende, si los prompts y los conjuntos de evaluación son portables y cómo se sitúa el modelo tras una interfaz interna (o si no). La señal a vigilar es si alguien ha ejecutado jamás la suite de evaluación contra un segundo proveedor; si no, el plan de salida es una esperanza, no un plan. Si la respuesta honesta es que cambiar implicaría meses y reescribir código central, tratarlo como un defecto de diseño que conviene reparar ahora, no como un puente que cruzar más adelante.

3. **¿Qué dice un cuadro de preparación honesto sobre los derechos sobre nuestros datos, y qué casos de uso descarta hoy?** Omitir la preparación de datos es el fallo que hunde los pilotos en silencio: el modelo funciona, pero nunca se tuvo base legal para usar los datos, o están sin etiquetar y sin trazabilidad. En una organización grande, los datos personales y de terceros plantean límites de consentimiento y contractuales que varían según la jurisdicción y el conjunto de datos. Traer una auditoría de disponibilidad, calidad, etiquetado, trazabilidad y base legal de cada candidato, y estar dispuestos a marcar algunos casos de uso como bloqueados hasta que existan los cimientos de datos. En entornos regulados y públicos, una base legal inexistente no es un retraso: es un punto de parada absoluto, y financiar el trabajo de preparación debe ser una línea explícita en el plan, no un añadido posterior.

4. **¿Cómo sabremos que un caso de uso de IA en producción funciona realmente, y qué evidencia nos llevaría a cancelarlo?** La mayoría de las carteras de IA acumulan proyectos zombi: pilotos que se implementaron, impresionaron a alguien y ahora siguen en marcha sin que nadie compruebe si siguen justificando su coste. Acordar el punto de partida y la métrica de éxito antes del lanzamiento y fijar un umbral de cancelación explícito, de modo que la decisión de detener se tome por adelantado en vez de defenderse en el momento. Traer la métrica actual, el coste de la supervisión humana por resultado y el desplazamiento observado desde el lanzamiento. En carteras empresariales y públicas, nombrar quién revisa cada sistema en un plazo fijo y quién ostenta la autoridad para retirarlo; un caso de uso al que nadie es responsable de revisar es uno que nadie apagará nunca.

5. **¿Dónde permanece el ser humano en el bucle, cuánto cuesta esa supervisión y de verdad la hemos presupuestado?** Los casos de uso de IA que parecen más económicos son los que, en silencio, asumen automatización total y luego filtran costes a través de la revisión, la corrección y la escalación que la realidad impone. Decidir deliberadamente qué decisiones debe confirmar una persona, cuáles puede tomar el modelo por sí solo y cuáles nunca debe tomar, y presupuestar el tiempo humano que eso implica. Traer el volumen de casos de baja confianza, el coste de una respuesta errónea y la vía de escalación actual. En entornos regulados y públicos, vincular cada decisión automatizada a un responsable nombrado y a una vía de apelación, porque una supervisión que no puede describirse es una supervisión que no existe.

6. **¿Contamos con el talento y la plataforma necesarios para ejecutar lo que proponemos, o estamos asumiendo en silencio capacidad que no tenemos?** Los planes de IA más ambiciosos fracasan menos en el modelo que en los cimientos menos glamorosos: nadie que mantenga la pipeline, nadie que evalúe los resultados, ninguna plataforma sobre la que desplegar. Asignar cada caso de uso a las competencias y la infraestructura que realmente requiere, y ser honesto donde la brecha sea una contratación, un socio o una razón para no construir. Traer un inventario de quién puede hacerse cargo de cada sistema en producción, sobre qué plataforma se ejecutará y qué capacidades habría que adquirir. En una organización grande o pública, añadir los plazos de contratación y reclutamiento, porque un plan que depende de talento que no se puede incorporar en la ventana relevante es un plan destinado a incumplir.

## Perspectiva por sector

**Startup.** La velocidad y la supervivencia lo dominan todo. Elegir un caso de uso estrecho que toque el valor central del negocio, desplegarlo sobre un modelo alojado tras una interfaz delgada y fijar un techo duro de gasto. Evitar construir infraestructura o entrenar modelos: el recurso más escaso es la atención de los ingenieros, y una pipeline afinada que no se puede mantener es una carga, no una fortaleza. Mantener el cambio barato para poder seguir un mercado que se mueve rápido.

**Pequeña empresa.** Probablemente no hay científicos de datos y el presupuesto es ajustado, así que conviene tratar la IA como algo que se adquiere integrado en las herramientas que ya se usan, no como un programa que hay que dotar de personal. Enmarcar la preparación como una cuestión de higiene de datos y privacidad, no como un proyecto de aprendizaje automático: saber qué datos de clientes se poseen, qué se permite hacer con ellos y dónde una respuesta automatizada errónea costaría un cliente. Preferir proveedores que ofrezcan una IA opcional, transparente y fácil de desactivar.

**Gran empresa.** El reto es la gobernanza de cartera entre muchos equipos: una escala compartida entre construir, adquirir o afinar, evaluaciones de preparación consistentes y análisis de dependencia y coste total de propiedad para que los grupos dejen de reinventar pipelines costosas. Presupuestar de forma explícita la carga de MLOps y la supervisión humana, estandarizar la capa de interfaz para que los proveedores sigan siendo intercambiables y gestionar los casos de uso de IA como una cartera con métricas claras y criterios de cancelación, no como un conjunto disperso de pilotos.

**Sector público.** La transparencia, las normas de contratación y la rendición de cuentas condicionan cada decisión. Favorecer sistemas que citen fuentes oficiales en lugar de generar política, mantener a un humano responsable de las decisiones de consecuencias relevantes, y exigir portabilidad de datos y divulgación de limitaciones del modelo en los contratos. Publicar una descripción en lenguaje claro del sistema y una vía de apelación, cumplir las obligaciones de salida a varios años que se suscriban, y mantener la IA fuera de las decisiones de evaluación final que deben recaer en un funcionario responsable.

## Ejemplos

**Startup.** Una empresa de agendamiento de cinco personas quería añadir una función de "resérvanos una reunión" en lenguaje natural sin apartar a sus dos ingenieros del producto central. Elegió el problema más pequeño que importaba (analizar una solicitud y proponer un horario) y lo desplegó con un modelo alojado tras una API interna delgada para poder cambiar de proveedor. El equipo fijó un techo mensual de gasto, vigiló si los usuarios aceptaban los horarios propuestos y acordó revisar un modelo afinado solo si el volumen lo justificara.

**Gran empresa.** Una aseguradora multinacional quería agilizar el triage de siniestros. En vez de entrenar un modelo a medida, enmarcó el problema de forma estrecha (clasificar y resumir los siniestros entrantes), hizo un prototipo con un modelo alojado más recuperación sobre sus documentos de póliza y midió el resultado contra el tiempo y la precisión del manejo humano. Solo tras demostrar el valor afinó un modelo más pequeño para el tipo de siniestro de mayor volumen, reduciendo el coste por llamada. Mantuvo el modelo tras una API interna para poder cambiar de proveedor y modeló un coste total de propiedad a tres años que incluía la revisión humana de los casos de baja confianza.

**Sector público.** Un organismo tributario nacional barajó un asistente de IA para ayudar a su personal a responder consultas de la ciudadanía. Como esas respuestas tocaban obligaciones legales, el organismo exigió transparencia: el sistema podía solo hacer emerger pautas oficiales con citas, nunca inventar política, y un humano revisaba cada sugerencia automatizada antes de su difusión. La contratación exigió al proveedor que divulgue las limitaciones del modelo y garantice la portabilidad de datos, y el organismo publicó una descripción en lenguaje claro del sistema junto a una vía de apelación. Mantuvo la IA completamente fuera de las decisiones de evaluación final, reservándolas para los funcionarios responsables.

## Justificación económica: motivaciones, retorno y coste total de propiedad

La estrategia de IA existe para evitar dos fallos simétricos: sobreinvertir en una IA que nunca da frutos e invertir de menos mientras competidores u organismos pares se adelantan. El retorno proviene del trabajo ahorrado, del tiempo de ciclo reducido, de la caída de los índices de error y de las nuevas capacidades habilitadas. Medir estas magnitudes frente a un punto de partida genuino y descontar el coste real de la supervisión humana, que rara vez desaparece.

El coste total de propiedad debe incluir las partidas menos glamorosas: pipelines de datos, supervisión, reentrenamiento a medida que el mundo cambia, revisión de seguridad y desmantelamiento eventual. Un piloto que parece barato puede resultar caro una vez que opera a escala durante años. Presentar también el coste de *no* adoptar: servicio más lento, mayor coste manual y deriva estratégica. Plantear el caso ante la dirección con una visión de cartera: algunas apuestas de alta confianza, métricas de éxito claras, criterios de cancelación para los fracasos y una evaluación de preparación que demuestre que los cimientos de datos y talento existen. Pedir a los responsables que financien la preparación de forma explícita; si se omite, se garantiza un rework costoso.

## Antipatrones y trampas

- **Solución en busca de problema.** Adquirir IA porque otros lo hicieron, para luego buscarle una aplicación.
- **Omitir la preparación de datos.** Lanzar modelos sobre datos que no están disponibles, que no tienen etiquetas o que no se pueden usar legalmente.
- **Decisiones guiadas por la demo.** Comprometerse tras una demostración pulida, sin una evaluación de calidad de producción.
- **Ignorar el bucle humano.** Asumir la automatización total y presupuestar la revisión por debajo de lo necesario, que es donde se esconde la mayor parte del coste.
- **Dependencia silenciosa del proveedor.** Construir en profundidad sobre funciones propietarias de un solo proveedor sin plan de salida.
- **Subestimar la operación.** Tratar el despliegue como la línea de meta en vez del comienzo de una obligación de mantenimiento.
- **La conformidad como añadido de última hora.** Integrar la transparencia y la auditabilidad después del diseño, a un múltiplo del coste.

## Modelo de madurez

1. **Iniciar.** Experimentos esporádicos, sin estrategia compartida; las decisiones las impulsan la euforia y el entusiasmo individual.
2. **Desarrollar.** Existe un enmarcado del problema en algunos proyectos; aparece una primera base de plataforma; se debate construir o adquirir, pero de forma inconsistente.
3. **Estandarizar.** Se gestiona una cartera de casos de uso de IA con métricas claras, un árbol de decisiones documentado, evaluaciones de preparación y análisis de dependencia y coste total de propiedad, aplicados de forma coherente entre equipos.
4. **Gestionar.** La cartera se mide: la preparación, el retorno, el coste total de propiedad y el coste de la supervisión humana se siguen frente a puntos de partida; los criterios de cancelación se aplican con base en la evidencia; la entrega y el impacto en la calidad dirigen cada decisión de continuar o detener.
5. **Orquestar.** La estrategia de IA está integrada en la planificación de negocio y de riesgo; la preparación se mantiene de forma continua; la organización retira, sustituye y reelabora sistemas de IA con base en la evidencia, reequilibrando la cartera a medida que cambian el mercado y el panorama de riesgo.

## Pautas para la reflexión

- ¿Cómo se decide que un problema no encaja con la IA de verdad, y quién tiene autoridad para decir que no?
- ¿Qué umbral de preparación debe impedir el paso de piloto a producción?
- ¿Cuánta dependencia del proveedor es aceptable a cambio de una velocidad superior para generar valor?
- En el sector público, ¿cómo deben condicionar las obligaciones de transparencia la decisión entre construir y adquirir?
- ¿Cómo mantener honestos los estimados de coste total de propiedad cuando proveedores y entusiastas tienen incentivos para subestimarlos?
- ¿Quién es el responsable de la cartera de IA y cómo se toman las decisiones de cancelación?

## Ideas clave

- La estrategia parte de un problema real y de un punto de partida honesto, no de una tecnología.
- Preferir la opción más simple: primero prompting, luego recuperación, después afinado, a continuación adquisición y, raramente, construcción desde cero.
- La preparación de datos, el talento y la plataforma son prerrequisitos; financiarlos forma parte del plan.
- Los contextos regulados y públicos exigen transparencia, conformidad de contratación y opciones de salida desde el diseño.
- Modelar el coste total de propiedad y el coste de la inacción, y protegerse de la dependencia del proveedor desde la primera decisión arquitectónica.

## Referencias y lectura adicional

- Ajay Agrawal, Joshua Gans y Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- Instituto Nacional de Estándares y Tecnología de Estados Unidos, *Marco de Gestión de Riesgos de IA (AI RMF 1.0)*.
- Organización para la Cooperación y el Desarrollo Económicos, *Principios de la OCDE sobre IA*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.

