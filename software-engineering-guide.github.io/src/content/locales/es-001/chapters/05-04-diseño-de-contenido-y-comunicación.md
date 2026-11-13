# 5.4 Diseño de contenido y comunicación

## Resumen y motivación

El diseño de contenido y comunicación consiste en dar forma a las palabras, los mensajes y la información que un producto emplea para orientar a las personas en la acción. Abarca la [estrategia de contenido](https://en.wikipedia.org/wiki/Content_strategy) (qué contenido debe existir, para quién y con qué propósito), la redacción de experiencia de usuario y el microtexto (las etiquetas, los botones, las sugerencias y los mensajes de error dentro de una interfaz), y las comunicaciones que alcanzan al usuario a través del correo electrónico, las notificaciones y otros canales. Las palabras son interfaz. En la mayoría de los productos de software, el contenido constituye la experiencia del usuario mucho más que lo visual.

En equipos grandes, el contenido es un problema de coordinación y de confianza. Cuando muchos equipos redactan de forma independiente, la terminología se desvía, el tono oscila de cercano a burocrático de una pantalla a otra y un mismo concepto recibe tres nombres distintos. El usuario pierde el hilo y, con él, la confianza. Una estrategia de contenido compartida lo resuelve. Una guía de voz y tono, un [vocabulario controlado](https://en.wikipedia.org/wiki/Controlled_vocabulary) y patrones reutilizables para errores y estados vacíos hacen con las palabras lo que un sistema de diseño hace con los píxeles: permiten que equipos independientes produzcan un conjunto coherente y digno de confianza.

En entornos empresariales y del sector público, un contenido claro es con frecuencia un requisito legal y ético, no una cuestión de estilo. Las leyes de [lenguaje claro](https://en.wikipedia.org/wiki/Plain_language) exigen que las comunicaciones públicas sean comprensibles para las personas que deben actuar sobre ellas. Un lenguaje deficiente en un formulario de prestaciones, unas instrucciones médicas o una advertencia de seguridad puede causar un daño real: un plazo incumplido, una dosis errónea, una víctima de estafa. Y en una era de manipulativos ["patrones oscuros"](https://en.wikipedia.org/wiki/Dark_pattern) (diseños de interfaz que engañan o presionan a las personas para que tomen decisiones contrarias a su propio interés), la forma en que un producto presenta sus opciones es cuestión de confianza, seguridad y, cada vez más, de regulación.

## Principios clave

- Las palabras son interfaz; el contenido es parte esencial de la experiencia, no un relleno que se añade después.
- Escribir para el objetivo y el contexto del lector, en lenguaje claro, en el momento exacto en que lo necesita.
- La claridad por encima de la ingeniosidad: un usuario confundido no se siente complacido por un mensaje de error ingenioso.
- La consistencia en la terminología y el tono reduce la carga cognitiva y fortalece la confianza.
- Buenos valores predeterminados y estados vacíos útiles guían a las personas hacia el éxito.
- Honestidad por diseño: nunca engañar, presionar ni avergonzar a los usuarios para que elijan.
- El contenido debe ser estructurado y reutilizable, no incrustado en el código ni duplicado.
- Diseñar las comunicaciones para todo el recorrido multicanal, respetando la atención del usuario.

## Recomendaciones

### Establecer una estrategia de contenido y una voz

Comience definiendo para quién se escribe, qué tareas ayuda a realizar y cómo debe sonar. Redacte una guía de voz y tono con ejemplos concretos y un glosario de terminología, un [vocabulario controlado](https://en.wikipedia.org/wiki/Controlled_vocabulary), para que lo mismo se llame siempre igual. Que el tono se adapte al contexto: reconfortante ante un error, sereno ante una advertencia de seguridad, festivo ante un logro. La voz se mantiene constante; el tono flexiona. Trate el contenido como un activo gestionado, con responsables, revisiones y un ciclo de vida, no como texto que se escribe a última hora en un campo de un formulario.

### Redactar microtextos que impulsen a la acción

Etiquete los botones con la acción que ejecutan («Enviar solicitud», no «Aceptar»). Redacte sugerencias y textos de ayuda que anticipen los errores antes de que ocurran. Coloque las palabras clave al inicio para que quien barre la pantalla con la mirada capte el mensaje. Use la segunda persona y la voz activa. Mantenga las frases breves y concretas. Cada microtexto debe reducir la incertidumbre sobre lo que va a ocurrir y sobre qué hacer a continuación.

### Hacer del lenguaje claro un estándar y cumplir los requisitos legales

Escriba a un [nivel de lectura](https://en.wikipedia.org/wiki/Readability) adecuado a toda la audiencia, no a los autores. Prefiera palabras corrientes, frases breves e instrucciones concretas; desarrolle la jerga y las siglas al primer uso o evítelas. En el sector público, el lenguaje claro suele ser un requisito legal y normativo: acate los estándares de lenguaje claro aplicables y verifique la comprensión con usuarios reales, incluyendo personas con menor nivel de lectoescritura y hablantes no nativos. El lenguaje claro no es «bajar el nivel»: los lectores expertos también valoran un texto claro y eficiente.

### Diseñar deliberadamente los mensajes de error, los estados vacíos y los valores predeterminados

Un mensaje de error debe indicar qué falló, por qué y cómo solucionarlo, en lenguaje claro, sin culpar y sin códigos que el usuario no pueda interpretar. Conserve la entrada del usuario y sitúe el mensaje justo donde está el problema. Los estados vacíos son una oportunidad de incorporación: expliquen qué debe aparecer allí y cómo añadirlo, en lugar de mostrar un vacío en blanco. Elija valores predeterminados útiles y seguros para que la mayoría de los usuarios logre el objetivo sin cambios, y que el predeterminado sea la opción que sirve al interés del usuario, no solo al del negocio.

### Diseñar para la confianza y la seguridad; evitar patrones oscuros

Presente las opciones con honestidad y simetría: darse de baja debe ser tan sencillo como darse de alta, y rechazar tan visible como aceptar. No use la técnica de la «vergüenza al rechazar» («No, gracias, prefiero no ahorrar»), casillas de consentimiento premarcadas, costes ocultos, falsa urgencia ni flujos de tipo «hotel de la cucaracha» (fáciles de entrar, imposibles de salir) . Más allá de la ética, muchos de estos patrones son ya ilegales en virtud de la legislación de protección al consumidor y de privacidad. Preste atención especial a las comunicaciones sobre seguridad, privacidad y dinero, porque ahí es donde la manipulación causa mayor daño y donde los estafadores imitan el mensaje legítimo.

### Diseñar comunicaciones multicanal de forma coherente

El correo electrónico, las notificaciones push, los mensajes SMS y los mensajes dentro de la app forman parte de un mismo recorrido. Coordínelos para que el usuario no reciba spam ni mensajes contradictorios entre canales. Respeta la atención: notifique solo cuando sea oportuno y útil, permita al usuario controlar la frecuencia y el canal, y asegure que cada mensaje sea accesible y claro. Garantice que las comunicaciones transaccionales (comprobantes, alertas, plazos) sean fiables, inequívocas y difíciles de confundir con [phishing](https://en.wikipedia.org/wiki/Phishing): una identidad de remitente y un formato consistentes ayudan a que el usuario distinga los mensajes genuinos.

## Compromisos: ventajas e inconvenientes

| Decisión | Ventajas | Inconvenientes |
|---|---|---|
| Estrategia de contenido centralizada | Consistencia, confianza, reutilización | Sobrecarga; puede frenar a los equipos si se convierte en un cuello de botella |
| Lenguaje claro en todo el producto | Comprensión, inclusión, cumplimiento legal | Esfuerzo de reescritura; los especialistas pueden resistirse a renunciar a su jerga |
| Voz de marca lúdica y personal | Personalidad, memorable | Puede fallar ante errores, situaciones de alto riesgo o audiencias diversas |
| Valores predeterminados sólidos | La mayoría de los usuarios logra el objetivo sin esfuerzo | Riesgo de sesgo conductual; deben ajustarse al interés del usuario |
| Mensajería multicanal enriquecida | Inmediatez, implicación | Puede convertirse en ruido; exige gestión de privacidad y consentimiento |

La tensión fundamental es entre la personalidad de marca y la claridad, y entre la implicación y el respeto a la atención del usuario. El contexto la resuelve. Que la voz añada calidez donde el riesgo es bajo y priorice una claridad serena donde el riesgo es alto (errores, dinero, seguridad, asuntos legales). En cuanto a valores predeterminados y mensajería, la línea ética es sencilla: ¿el diseño sirve al interés genuino del usuario o explota su descuido?

## Preguntas para debatir con el equipo

1. **¿Los mensajes de error, los estados vacíos y los valores predeterminados son patrones compartidos del sistema de diseño, o cada pantalla los inventa desde cero?** Son los momentos de mayor palancada de toda la experiencia: un buen mensaje de error indica qué falló, por qué y cómo solucionarlo, sin culpar ni mostrar un código ininterpretable, y un buen estado vacío enseña qué debe ir allí en lugar de mostrar un vacío. Cuando cada equipo los redacta desde cero, aparece un «Error 500» en un lugar y un mensaje útil en otro, y el usuario pierde confianza. Decida si estos patrones viven en el sistema de diseño junto a los componentes, con estructuras y ejemplos acordados. Traiga tres mensajes de error y tres estados vacíos reales de su producto y léalos en voz alta. Si alguno culpa al usuario o no ofrece camino de recuperación, ya ha encontrado su primera tarea pendiente.

2. **¿El contenido está estructurado y es reutilizable, o está incrustado en el código y duplicado entre pantallas?** El texto escrito directamente en un componente no se puede actualizar con consistencia, no se puede revisar ni localizar sin un cambio de código, lo que bloquea silenciosamente cada nuevo mercado y cada corrección de redacción. El problema se agudiza a gran escala, cuando el mismo concepto recibe tres nombres porque no hay glosario ni una sola fuente de verdad. Decida cómo se almacena el contenido, quién es dueño del vocabulario controlado y cómo se propaga un cambio de redacción sin desplegar código para cada pantalla. Traiga un ejemplo de un término que su producto escribe o nombra de forma inconsistente y trace cuántos lugares habría que corregir. Si la respuesta es «buscar y reemplazar a mano», el contenido está atrapado en el código.

3. **¿Cuándo se incorporan los diseñadores de contenido al flujo de trabajo y quién tiene autoridad para vetar un flujo manipulativo?** Si el contenido es un añadido de última hora (texto de relleno hasta el lanzamiento, y lo que quepa en la caja), las palabras que cargan con la mayor parte de la experiencia reciben menos atención y los patrones oscuros se cuelan bajo la presión del crecimiento porque nadie es responsable de la honestidad. Acuerde que el contenido es una entrada de diseño desde el principio, con una guía de voz y tono y una revisión en el flujo, y nombre a quien puede frenar un flujo con vergüenza al rechazar o una casilla de consentimiento premarcada antes de que se publique. Es ya una cuestión legal además de ética, porque la legislación de protección al consumidor y de privacidad prohíbe cada vez más estos patrones. Traiga un flujo reciente y pregunte si rechazar es tan fácil y tan visible como aceptar. Si no lo es, decida hoy quién es responsable de corregirlo.

4. **¿A qué nivel de lectura estamos escribiendo de verdad y cómo sabemos que los usuarios reales comprenden nuestro contenido más sensible?** El lenguaje claro es fácil de proclamar y difícil de demostrar: los autores escriben a su propio nivel de comprensión, y quienes más necesitan claridad (personas con menor nivel de lectoescritura y hablantes no nativos) son los menos representados en la sala. Para una organización grande, el riesgo se multiplica, porque un comunicado de prestaciones confuso o una advertencia de seguridad se envía a millones de destinatarios antes de que nadie mida si ha llegado. Fije un nivel de lectura objetivo para toda la audiencia, desarrolle o prohíba la jerga en el primer uso y comprométase a probar la comprensión con personas reales en lugar de fiarse de una puntuación de legibilidad. Traiga sus tres comunicaciones de mayor tráfico y la evidencia de que alguien fuera del equipo de redacción puede actuar correctamente sobre ellas. En contextos empresariales y del sector público, añada la ley o norma de lenguaje claro aplicable y sea sincero sobre qué documentos no pasarían una auditoría hoy.

5. **¿Quién regula cómo, cuándo y con qué frecuencia comunicamos con los usuarios a través de correo, notificaciones, SMS y mensajes dentro de la app, para que el recorrido global siga siendo coherente?** Cuando cada equipo gestiona su propio canal, el usuario recibe spam, mensajes contradictorios y, al final, aprende a ignorar o darse de baja de todo, incluidas las transaccionales que de verdad importan. Coordinar el recorrido significa acordar límites de frecuencia, dar al usuario un control real sobre el canal y el consentimiento, y mantener una identidad de remitente consistente para que los mensajes genuinos no se confundan con el phishing que los imita. Traiga un registro de todos los mensajes que un usuario podría recibir en una semana intensa y cuente las duplicaciones, las contradicciones y los que podrían tomarse por estafa. La presión contraria es la del crecimiento, porque los equipos comerciales siempre quieren un punto de contacto más y el respeto a la atención no tiene métrica inmediata. En contextos empresariales y del sector público, añada las obligaciones de consentimiento y privacidad que convierten la mensajería no solicitada en un riesgo legal, y nombre a quien pueda vetar una campaña que abuse del canal.

6. **¿Cómo medimos si nuestro contenido funciona y dónde cede por completo la voz de marca ante la claridad?** El contenido que nunca se mide deriva según los gustos y el stakeholder más ruidoso decide la redacción en lugar del usuario. Vince el contenido a señales reales: categorías de tickets de soporte, funnels de finalización y conversión, tasas de error y recurso, y tasas de baja y de reclamación, para que una reescritura se juzgue por su resultado y no por preferencia. Al mismo tiempo, acuerde dónde la voz debe ceder: un error ingenioso, un mensaje juguetón sobre dinero o una advertencia de seguridad con gracia erosionan la confianza justo cuando el riesgo es mayor. Traiga un flujo de alto tráfico, la métrica que mueve y una propuesta de línea entre dónde la personalidad ayuda y dónde la claridad serena es obligatoria. En una organización grande o pública, nombre a quien es dueño de esa línea y cómo se propaga una mejora demostrada entre equipos, en lugar de ganar una pantalla y perder el resto.

## Perspectiva sectorial

**Startup.** Sin redactor y con dos desarrolladores, trate el contenido como una tarea del fundador, no como una contratación. Dedique un día a las palabras de mayor palancada: nombre los botones por su acción, convierta el panel vacío en un tutorial de primera ejecución y haga que los errores digan qué se debe corregir. Redacte una guía de voz de una página para que el tono siga siendo claro mientras crece, y posponga el glosario y la plataforma de contenido hasta que la inconsistencia duela de verdad.

**Pequeña empresa.** Sin diseñador de contenido y con presupuesto ajustado, apoye en las convenciones de lenguaje claro y microtexto integradas en las herramientas que ya usa, y adquiera plantillas para el correo transaccional en lugar de crearlas desde cero. Priorice las pocas pantallas que hacen perder clientes: un estado vacío, un error en el pago, un flujo de cancelación, y mantenga que rechazar sea tan fácil como aceptar para no tropezar con la legislación contra los patrones oscuros. Pase un verificador de legibilidad gratuito sobre todo lo que el cliente vea antes de publicar.

**Empresa grande.** El problema es la coherencia entre muchos equipos: una guía de voz y tono compartida, un vocabulario controlado para que un concepto conserve un solo nombre y patrones de error, estado vacío y valores predeterminados que vivan en el sistema de diseño junto a los componentes. Almacene el contenido en control de versiones, estructurado y localizable, no incrustado en el código; asigne responsables y revisiones, y coordine la mensajería multicanal para que el usuario no reciba spam ni contradicciones. Gobiernes la honestidad de forma central para que ningún equipo publique vergüenza al rechazar o casillas de consentimiento premarcadas bajo presión de crecimiento.

**Sector público.** El lenguaje claro suele ser un deber legal, no una preferencia: acate los estándares aplicables y pruebe la comprensión con destinatarios reales, incluyendo personas con menor nivel de lectoescritura y hablantes no nativos. Comience cada aviso con la acción requerida y el plazo, elimine la jerga legal y asegure que cada comunicación identifique con claridad a su emisor para que no se confunda con una estafa. Mantenga las opciones honestas y simétricas, publique los estándares de contenido a los que se somete y ofrezca a las personas una vía sencilla para cuestionar una decisión que no comprenden.

## Ejemplos

**Startup.** Una pequeña startup sin redactores notó que la mayoría de los usuarios de prueba se registraban, veían un panel vacío y no regresaban. Un fundador dedicó un día a reescribir el microtexto: el estado vacío ahora explicaba qué añadir y ofrecía un proyecto de muestra con un clic, los botones nombraban su acción en lugar de decir «Aceptar», y los mensajes de error decían qué fallaba y cómo arreglarlo. La activación subió notablemente la semana siguiente, y el mismo fundador redactó una guía de voz de una página para que todo el equipo mantuviera un tono claro y coherente a medida que crecía.

**Empresa.** Una compañía SaaS reescribió su incorporación, sus mensajes de error y sus estados vacíos en torno a un microtexto claro y orientado a la acción y a una guía de voz documentada. Los tickets de soporte por preguntas de «¿cómo se hace…?» cayeron, la activación mejoró porque los estados vacíos ahora enseñaban al usuario qué hacer, y la conversión de prueba a pago aumentó. La empresa también eliminó un flujo de cancelación con vergüenza al rechazar que había dañado la confianza y atraído críticas, reemplazándolo por una ruta de cancelación directa y simétrica; y, contrariamente a lo que cabría esperar, eso mejoró la reputación y la recuperación de clientes.

**Sector público.** Un organismo reescribió una carta de elegibilidad para prestaciones que los destinatarios solían malinterpretar, lo que provocaba citas perdidas y la pérdida injusta de derechos. Aplicando estándares de lenguaje claro, el equipo situó al frente la acción requerida y el plazo, eliminó la jerga legal y probó la comprensión con destinatarios reales, incluidos hablantes no nativos. La comprensión mejoró notablemente y la tasa de plazos incumplidos descendió, reduciendo los recursos y la carga administrativa. Como la carta ahora identificaba claramente a su emisor, los destinatarios también la confundían menos con una estafa.

## Caso de negocio: motivaciones, retorno de la inversión y coste total

La calidad del contenido genera resultados medibles: mayor finalización de tareas y conversión, menor volumen de soporte, menos errores y recursos, y mayor confianza y fidelización. El microtexto claro y los valores predeterminados útiles reducen el número de personas que se atoran y contactan con soporte o abandonan. Las comunicaciones en lenguaje claro reducen costes a aval: menos llamadas por confusión, menos errores que corregir, menos recursos en el contexto público. Un diseño confiable y no manipulador protege la reputación y reduce el riesgo legal a medida que se endurece la regulación sobre patrones oscuros.

En cuanto al coste total, el coste de adopción es modesto: diseñadores de contenido o redactores formados, una guía de voz y un glosario, y una revisión en el flujo. El coste de no adoptar es difuso y grande: la carga de soporte y de centro de llamadas, las transacciones abandonadas, la corrección de errores, los recursos, las sanciones regulatorias por patrones manipuladores o comunicaciones no conformes, y la erosión de la confianza. Estos costes caen en soporte y operaciones, no en el presupuesto del producto, de modo que la dirección tiende a infravalorarlos.

Para construir el caso, vincule el trabajo de contenido con las categorías de tickets de soporte, los funnels de finalización y conversión, las tasas de error y recurso, y las tasas de baja y de reclamación. Una pequeña reescritura de un flujo de alto tráfico o de una comunicación de alto volumen suele producir una mejora clara y atribuible, y eso es lo que justifica escalar la práctica.

## Antipatrones y errores frecuentes

- **Contenido como añadido de última hora**: texto de relleno hasta el lanzamiento y, después, lo que quepa en la caja.
- **Jerga y lenguaje interno**: escribir desde la perspectiva de la organización, no del usuario.
- **Errores que culpan y no ayudan**: «Error 500» o «Entrada no válida» sin camino de recuperación.
- **Estados vacíos en blanco**: un vacío donde debía ir una guía.
- **Patrones oscuros**: vergüenza al rechazar, casillas de consentimiento premarcadas, costes ocultos, flujos tipo hotel de la cucaracha, falsa urgencia.
- **Terminología inconsistente**: tres nombres para un mismo concepto en el producto.
- **Spam de notificaciones**: sobrecomunicar hasta que el usuario aprende a ignorar o a darse de baja.
- **Legibilidad no probada**: dar por supuesto que el contenido es claro sin probarlo con usuarios reales.
- **Texto incrustado y duplicado**: imposible de actualizar o localizar con consistencia.

## Modelo de madurez

**Nivel 1: Inicio.** No hay práctica de contenido. Las palabras las escribe quien construye la pantalla, reaccionando a lo que la caja necesita en el momento. La terminología y el tono son inconsistentes, los errores culpan al usuario o muestran códigos ininterpretables, y los estados vacíos son un vacío en blanco.

**Nivel 2: Desarrollo.** Puede existir una guía de estilo o algunas notas de voz, y algunos equipos han adoptado hábitos de lenguaje claro. El contenido sigue siendo una actividad tardía y por equipo, con poca reutilización y poca prueba, de modo que la calidad y la consistencia varían enormemente de un squad a otro.

**Nivel 3: Estandarización.** Una estrategia de contenido, una guía de voz y tono y un vocabulario controlado están documentados y en uso entre equipos. El lenguaje claro es el estándar y, donde procede, el cumplimiento; los errores, los estados vacíos y los valores predeterminados siguen patrones compartidos; el contenido está estructurado, revisado y es reutilizable, no incrustado pantalla a pantalla.

**Nivel 4: Gestión.** El contenido se mide contra resultados con datos. Las puntuaciones de legibilidad y de comprensión, las categorías de tickets de soporte, los funnels de finalización y conversión, las tasas de error y recurso, y las tasas de baja y de reclamación se siguen contra baselines, y cada cambio de contenido se juzga por si mueve esas cifras. Los patrones oscuros se auditan contra una política documentada y la frecuencia de los mensajes multicanal se monitoriza contra límites acordados.

**Nivel 5: Orquestación.** El contenido se mejora de forma continua e integrada en toda la organización. Los patrones viven en el sistema de diseño, localizados y accesibles por defecto; el vocabulario controlado mantiene un solo nombre por concepto en todas partes; las comunicaciones multicanal están coordinadas y controladas por el usuario; y la práctica se adapta a medida que cambian la regulación, la audiencia y los canales, retirando y reescribiendo contenido con base en evidencias y no en opiniones.

## Propuestas de debate

- ¿Dónde debe ceder por completo la voz de marca ante la claridad y quién traza esa línea?
- ¿Cómo se hace cumplir una política de «cero patrones oscuros» cuando los equipos de crecimiento están bajo presión de métricas?
- ¿Cómo se mantiene la terminología consistente entre muchos equipos sin convertirse en un cuello de botella?
- ¿Qué nivel de lectura es adecuado para un servicio usado por toda la ciudadanía?
- ¿Cómo debe gobernarse la frecuencia de las notificaciones y el control de canales a nivel de organización?
- ¿Cómo se distinguen las comunicaciones genuinas del phishing que las imita?

## Ideas esenciales

- El contenido es interfaz de primera; diseñe las palabras con el mismo rigor que lo visual.
- El lenguaje claro mejora la comprensión para todos y, a menudo, es un requisito legal.
- Los errores, los estados vacíos y los valores predeterminados son momentos de alta palancada: diseñe para ayudar.
- Evite los patrones oscuros: presente las opciones con honestidad y simetría; cada vez son más ilegales.
- La terminología y el tono consistentes construyen confianza y reducen la carga cognitiva.
- Coordine las comunicaciones multicanal y respete la atención y el control del usuario.
- La calidad del contenido se refleja directamente en el volumen de soporte, la finalización, los errores y la confianza.

## Referencias y lectura adicional

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson y Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton y Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (investigación sobre patrones oscuros)
- Directrices federales de lenguaje claro de EE. UU. y PlainLanguage.gov
- Servicio Digital del Gobierno del Reino Unido, guía de diseño y estilo de contenido
- Nielsen Norman Group, artículos sobre mensajes de error, microtexto y legibilidad

