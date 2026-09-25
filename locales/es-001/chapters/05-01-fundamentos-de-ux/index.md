# 5.1 Cimientos de la experiencia de usuario

## Visión general y motivación

La [experiencia de usuario](https://en.wikipedia.org/wiki/User_experience) (UX) consiste en comprender a las personas (sus objetivos, sus contextos, sus limitaciones) y, a partir de esa comprensión, dar forma al software para que les ayude a lograr lo que buscan con la menor fricción posible. No es un adorno que se aplica al final; es una manera de trabajar que comienza antes de escribir la primera línea de código y se prolonga mucho después del lanzamiento. En este capítulo se abordan las prácticas de investigación, modelado y [pensamiento de diseño](https://en.wikipedia.org/wiki/Design_thinking) que permiten a una gran organización tomar decisiones de producto basadas en evidencia, no en conjeturas.

Para equipos numerosos, la UX es tanto un problema de coordinación como una disciplina artesanal. Cuando decenas de grupos de trabajo lanzan funciones sobre un mismo producto compartido, los modelos mentales incongruentes, los flujos duplicados y la terminología contradictoria se acumulan hasta formar un conjunto confuso que ningún equipo asume como propio. Un cimiento UX compartido, construido sobre personas comunes, mapas de viaje consensuados y una [arquitectura de la información](https://en.wikipedia.org/wiki/Information_architecture) documentada, da a cada equipo el mismo mapa del usuario, de modo que sus decisiones individuales, aunque tomadas en paralelo, suman en una experiencia coherente. Sin ese cimiento, cada equipo optimiza su propio rincón y el producto en su conjunto no tiene sentido.

Los entornos empresarial y gubernamental elevan la posta. El software empresarial suele tener usuarios cautivos que no pueden marcharse, de modo que una mala UX no se paga en pérdidas de clientes, sino en formación, tickets de soporte, errores y pérdida de productividad. Los servicios públicos, en cambio, alcanzan a toda la población, incluidas personas en crisis, con dispositivos obsoletos, con baja confianza digital o sin alternativa de proveedor. Ahí la calidad de la UX es una cuestión de equidad y de confianza cívica: un formulario de solicitud de subsidios mal diseñado puede negar a alguien la comida o la vivienda, no porque no tenga derecho, sino porque no fue capaz de completarlo.

## Principios fundamentales

- Diseñar para personas reales que realizan tareas reales en condiciones reales, no para un usuario idealizado conectado a una red rápida y con toda su atención.
- La investigación reduce riesgos. El momento más barato para descubrir una suposición errónea es antes de haber construido sobre ella.
- Los usuarios no pueden predecir con fiabilidad lo que harán; hay que observar el comportamiento, no solo la preferencia declarada.
- Centrar la atención en el trabajo que el usuario intenta completar, no en la funcionalidad que uno quiere lanzar.
- La coherencia es una característica: un modelo mental uniforme en todo el producto reduce la carga cognitiva.
- La [accesibilidad](https://en.wikipedia.org/wiki/Accessibility) y la inclusión forman parte de una buena UX desde el primer día, no de una verificación de cumplimiento a posteriori.
- Los métodos cualitativos y cuantitativos responden a preguntas distintas; hay que usar ambos.
- Pequeñas investigaciones frecuentes superan a los grandes estudios puntuales.

## Recomendaciones

### Establecer una investigación continua y mixta

Apuntar a una práctica de investigación ligera pero constante, no a grandes estudios ocasionales. Las entrevistas revelan motivaciones y modelos mentales. Las [pruebas de usabilidad](https://en.wikipedia.org/wiki/Usability_testing) muestran dónde se rompen los diseños; entre cinco y ocho participantes por ronda bastan para detectar la mayoría de los problemas graves. Las encuestas miden actitudes a gran escala pero no explican el porqué. La analítica y la instrumentación muestran lo que la gente realmente hace en la población completa. Acoplar un método cualitativo (el porqué) con un cuantitativo (el cuántos) permite que los hallazgos queden a la vez explicados y dimensionados. Y mantener un repositorio de investigación, para que los insights sigan siendo buscables y reutilizables entre equipos y no se pierdan en las diapositivas de un solo grupo.

### Modelar a los usuarios con personas, mapas de viaje y trabajos por los que se contrata

Construir un pequeño conjunto de personas basadas en evidencia que capturen objetivos, contextos y limitaciones, no caricaturas demográficas. Formular las necesidades como trabajos por los que se contrata: el resultado subyacente que el usuario busca lograr, no una funcionalidad («Cuando pierdo el empleo, quiero entender rápidamente qué apoyo me corresponde, para seguir pagando el alquiler»). Así se mantiene el foco en los resultados, no en las funcionalidades. Los mapas de viaje recorren la experiencia completa a través de canales y a lo largo del tiempo, exponiendo huecos y puntos de transición que ninguna pantalla aislada revela. Para servicios con un intenso trabajo de retaguardia (centros de llamadas, trabajadores sociales, operaciones de cumplimiento), usar [mapas de servicio](https://en.wikipedia.org/wiki/Service_blueprint) para vincular la experiencia del escenario visible con los sistemas y el personal que la sostienen.

### Diseñar la arquitectura de la información con deliberación

La arquitectura de la información (AI) es la forma en que se estructuran y nombran el contenido, las funcionalidades y la navegación. Emplear el [sorteo de tarjetas](https://en.wikipedia.org/wiki/Card_sorting) y la [prueba de árbol](https://en.wikipedia.org/wiki/Tree_testing) para derivar esa estructura de los modelos mentales de los usuarios, no de la organigrama. Un fallo habitual en grandes organizaciones es exponer las fronteras internas entre departamentos como navegación de primer nivel. Establecer un vocabulario controlado para que un mismo concepto tenga un mismo nombre en toda la interfaz. El [diseño de interacción](https://en.wikipedia.org/wiki/Interaction_design) define entonces el comportamiento momento a momento: estados, retroalimentación, recuperación de errores y la fluidez entre pasos.

### Aplicar el pensamiento de diseño con pragmatismo

El modelo del doble diamante (divergir y converger para definir el problema correcto; luego divergir y converger de nuevo para diseñar la solución correcta) es un marco útil. No obstante, conviene entenderlo como una mentalidad, no como un proceso rígido con fases cerradas. En la práctica, ejecutar ciclos ajustados: formular una hipótesis, bocetar, probar con un puñado de usuarios y aprender en cuestión de días. Reservar el descubrimiento más profundo para problemas genuinamente novedosos o de alto riesgo. Y tener cuidado con el «teatro de la innovación», donde los talleres producen post-its pero ningún cambio se materializa.

### Integrar la UX en la entrega

Insertar diseñadores e investigadores en los equipos de entrega, en lugar de mantener un «departamento de UX» aparte que entrega especificaciones a través de una pared. Convertir los hallazgos de investigación en una entrada permanente a la priorización. Incorporar controles de calidad UX, como benchmarks de usabilidad y verificaciones de accesibilidad, en los criterios de finalización de cada tarea. Y medir métricas de resultado (éxito en la tarea, tiempo en tarea, tasa de error, satisfacción) junto a las métricas de entrega.

## Costos-beneficios: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Investigación de descubrimiento continuo | Detecta problemas temprano, genera comprensión compartida | Coste sostenido, requiere un flujo constante de reclutamiento y personal calificado |
| Investigación pesada previa | Profundidad antes de invertir a gran escala | Lenta; puede postergar aprendizajes que solo la entrega a tiempo real revela |
| Decisiones basadas solo en analítica | Escala, es objetiva y económica una vez instrumentada | Explica el qué, no el porqué; es ciega ante los no usuarios y los casos límite |
| Personas y mapas de viaje | Alinean a muchos equipos en un mismo modelo del usuario | Se obsoletan; se convierten en ficción si no se renuevan con datos |
| Diseñadores embebidos | Retroalimentación rápida, sentido de propiedad compartido | Dificultad para mantener la coherencia artesanal entre muchos equipos |

Toda organización equilibra la inversión en investigación frente a la velocidad de entrega. El error es tratarlo como una elección excluyente. La postura productiva es proporcional: dedicar más descubrimiento a decisiones costosas de revertir (la arquitectura de la información central, los flujos principales, las decisiones de plataforma) y menos a detalles que se pueden cambiar con facilidad después. El coste de investigar es casi siempre insignificante frente al de construir bien la cosa equivocada.

## Preguntas para debatir con el equipo

1. **¿Quién es dueño de la arquitectura de la información y del vocabulario controlado, y qué ocurre cuando un equipo quiere desviarse?** A escala, el fallo más frecuente es que cada grupo exponga su propia estructura de organigrama y use sus propios nombres para el mismo concepto, de modo que el producto termina con tres términos para una sola cosa y una navegación que replica departamentos en lugar de tareas del usuario. Decidir desde ahora si la AI y el vocabulario se poseen de forma central, si se derivan del sorteo de tarjetas y la prueba de árbol en lugar de la política interna, y cómo un equipo solicita un cambio. Esto importa aún más en entornos empresarial y gubernamental porque los usuarios cautivos no pueden marcharse, y la incoherencia se paga en formación, tickets de soporte y errores, no en fuga de clientes. Llevar la lista actual de términos duplicados y flujos contradictorios como evidencia. Si no se puede nombrar un responsable, esa es la primera acción a tomar.

2. **¿Cuál es nuestro flujo de reclutamiento de participantes de investigación y alcanza a usuarios asistidos, de baja confianza y no digitales?** El descubrimiento continuo solo funciona si cada semana se puede estar frente a usuarios reales, y las personas más difíciles de reclutar suelen ser las que más necesitan el servicio: quienes atraviesan una crisis, usan dispositivos obsoletos o dependen habitualmente de ayuda. Probar solo con voluntarios conectados y confiados ofrece una lectura halagadora pero falsa, especialmente en servicios públicos donde la equidad de acceso es el punto central. Acordar quién gestiona el reclutamiento, qué incentivos se ofrecen y cómo se observan las sesiones de asistencia digital sin añadir carga a una persona vulnerable. Llevar la demografía de participantes de los últimos tres estudios y compararla con la base de usuarios real. Si se inclina hacia los más fáciles de alcanzar, corregir el flujo antes de fiarse de los resultados.

3. **¿Qué controles de calidad UX deben estar en los criterios de finalización y cómo impedimos que se conviertan en un teatro?** Insertar diseñadores e investigadores solo rinde si la investigación es una entrada permanente a la priorización y si las verificaciones de usabilidad y accesibilidad realmente bloquean el lanzamiento de una tarea, no son un documento que todos asienten y descarten. Elegir métricas de resultado concretas que se sigan junto a las de entrega: éxito en la tarea, tiempo en tarea, tasa de error y satisfacción. El riesgo es que la investigación se corra para justificar decisiones ya tomadas; conviene acordar quién puede vetar un lanzamiento por un control de UX y qué evidencia se impone a la opinión de un directivo. Tomar una funcionalidad reciente y preguntarse si su investigación cambió la decisión o solo la decoró. Si los hallazgos nunca mueven la hoja de ruta, los controles son cosméticos.

4. **¿Cómo evitamos que las personas, los mapas de viaje y la AI se conviertan en ficción un año después de la investigación que los originó?** Los modelos compartidos son lo que permite que decenas de equipos diseñen hacia una experiencia coherente, pero solo funcionan mientras describen usuarios reales; en el instante en que una persona se convierte en un artefacto que se cita para ganar argumentos en lugar de en un resumen de evidencia, causa un daño activo. Decidir quién se encarga de renovar cada modelo, con qué periodicidad y contra qué datos (entrevistas nuevas, analítica, temas recurrentes en soporte), y fijar una fecha visible de «última validación» para que los modelos obsoletos se noten de inmediato. La contrapartida es el coste: renovar todo de forma continua es desperdicio, por lo que la frecuencia de actualización debe vincularse a la velocidad con que cambia esa parte de la base de usuarios o ese recorrido. Llevar el origen de las personas principales actuales y preguntar cuándo se verificó cada una con un usuario real. En entornos empresarial y gubernamental, donde una base de usuarios cautiva o pública cambia lentamente pero con consecuencias (una población que envejece, un nuevo subsidio, una transición de dispositivos), un modelo que se desplaza en silencio puede encaminar años de inversión hacia usuarios que ya no existen.

5. **¿Dónde reside la accesibilidad en nuestro proceso y podemos demostrar que un lanzamiento la cumple antes de salir, no tras una queja?** Tratar la accesibilidad como una verificación de cumplimiento tardía es el fallo más común y el más caro, porque adaptar semántica, orden de foco y contraste a una interfaz ya construida cuesta mucho más que diseñarlos desde el inicio. Decidir qué norma se adopta (por ejemplo, WCAG, las Pautas de Accesibilidad para el Contenido Web), si el cumplimiento es un criterio de finalización que bloquea el lanzamiento y quién es responsable cuando una funcionalidad inaccesible llega a producción. La tensión es velocidad frente a inclusión, y los equipos bajo presión de plazo solerán saltarse los controles que no se aplican de forma estricta. Llevar la última auditoría, la cobertura automatizada y manual que la respalda, y el número de problemas de accesibilidad detectados tras el lanzamiento en lugar de antes. En el ámbito gubernamental, esto no es una cortesía opcional: suele ser una obligación legal y una cuestión de equidad, porque un servicio público que excluye a personas con discapacidad o que necesitan asistencia digital ha fracasado en su propósito central, no en uno secundario.

6. **¿Cuando la analítica y la investigación cualitativa se contradicen, a cuál creemos y quién arbitra?** Las grandes organizaciones acumulan tanto paneles que muestran lo que miles de usuarios hacen como entrevistas que explican por qué unos pocos se comportan de cierta manera, y ambas fuentes apuntarán con frecuencia en direcciones opuestas: un flujo con alta tasa de finalización que, en el fondo, avergüenza a la gente, o una funcionalidad que los usuarios elogian en sesiones pero que nadie usa a escala. Acordar de antemano cómo se triangula, qué pregunta responde con autoridad cada método (la analítica, la magnitud y el alcance; la investigación cualitativa, la causa y el sentido) y quién tiene la última palabra cuando chocan. El riesgo es seleccionar la fuente que aviva el plan ya elegido. Llevar un caso reciente de desacuerdo y recorrer cómo se resolvió de verdad. En entornos empresarial y público, la tensión se agudiza porque la analítica infrarecuenta sistemáticamente a las personas que más importan: los no usuarios, quienes abandonan y quienes usan tecnología asistiva rara vez aparecen en el embudo, de modo que fiarse solo de los números puede hacer invisibles a los excluidos.

## Perspectiva por sector

**Startup.** No hay investigador y no hay tiempo para un repositorio, así que convertir la investigación en un hábito de los fundadores: sentarse junto a cinco usuarios reales una tarde antes de construir lo que sigue. Omitir personas y mapas de viaje formales; una comprensión compartida del único problema que se resuelve, renovada cada semana al ver a la gente usar el producto, vale más que una documentación que nadie mantiene. La ventaja es que todo el equipo puede absorber un insight el mismo día en que aparece, así que proteger esa velocidad y resistirse al ceremonial.

**Pyme.** Sin especialista en UX y con un presupuesto ajustado, apoyarse en las convenciones que los usuarios ya conocen en lugar de inventar las propias, y adquirir herramientas con buenos valores predeterminados en vez de diseñar flujos desde cero. Hacer la investigación de bajo coste y alto impacto: un puñado de sesiones de usabilidad por videollamada y una lectura de los tickets de soporte revelarán la mayoría de los problemas graves. Considerar lo básico de accesibilidad (contraste, etiquetas, navegación por teclado) como un requisito que se obtiene de una buena biblioteca de componentes, no como un proyecto que hay que staffear.

**Gran empresa.** El problema central es la coherencia entre muchos equipos, por lo que conviene invertir en los cimientos compartidos: personas con dueño designado, mapas de viaje mantenidos, un vocabulario controlado y una arquitectura de la información documentada hacia la que los grupos diseñen, no alrededor de la cual se esquiven. Insertar diseñadores e investigadores en los equipos de entrega, pero gobernar la calidad artesanal de forma central para que el producto no se fraccione en dialectos inconsistentes. Financiar un repositorio de investigación y controles de calidad en los criterios de finalización, y seguir las métricas de resultado UX como un portafolio para que la optimización local de un solo equipo no degrade el conjunto.

**Sector público.** La accesibilidad y la equidad de acceso son deberes, no preferencias, por lo que someter cada lanzamiento a un estándar publicado e investigar con toda la diversidad de la población, incluidos usuarios asistidos, de baja confianza y no digitales. La contratación y la transparencia condicionan la entrega: publicar los principios de diseño y los métodos de investigación, estructurar los servicios en torno a los hitos de la vida ciudadana y no en torno a los departamentos internos, y conservar la evidencia de las pruebas para la auditoría. Como a menudo el usuario no tiene proveedor alternativo, un flujo que no puede completar es un servicio denegado; por eso, la medida real de éxito es que el usuario más difícil de alcanzar logre terminar.

## Ejemplos

**Startup.** Una startup de cuatro personas que construía una herramienta de agenda para clínicas pequeñas tenía fuertes convicciones sobre lo que necesitaban las recepcionistas, pero sin evidencia. Antes de escribir más funcionalidades, los fundadores se sentaron junto a cinco recepcionistas, una tarde cada uno, y las observaron trabajar. Descubrieron que el dolor real no era la velocidad de la agenda, sino los dobles reservas causados por una vista de calendario confusa, algo que nadie había mencionado en las llamadas de ventas previas. Reenfocar el producto en torno a ese único trabajo y, durante una semana, bocetar y probar soluciones con las mismas cinco personas, transformó un piloto estancado en sus primeros clientes pagantes.

**Gran empresa.** Un banco multinacional consolidó siete herramientas internas de originación de préstamos regionales en una sola plataforma. En lugar de fusionar conjuntos de funcionalidades, el equipo realizó mapeo de viaje y modelado de servicio con los subdirectores de las distintas regiones. Descubrió que las «diferencias regionales» que todos daban por ciertas eran en su mayoría terminología inconsistente y orden de pantallas dispar, no diferencias genuinas de proceso. Una AI unificada y un vocabulario compartido redujeron notablemente el tiempo de formación de los subdirectores y disminuyeron los errores de procesamiento, porque ahora todos compartían un mismo modelo mental.

**Sector público.** Una agencia de tributación nacional que rediseñaba su servicio de declaración online realizó pruebas de usabilidad moderadas con contribuyentes de distintas edades, dispositivos y niveles de confianza digital, además de observaciones de sesiones de asistencia digital con personas que normalmente dependen de ayuda. Las pruebas revelaron que los encabezados repletos de jerga hacían que la gente abandonara o declarara mal. Reformular el contenido en torno a los trabajos por los que los contribuyentes contrataban el servicio y reestructurar la AI en torno a hitos de la vida en lugar de códigos tributarios internos incrementó la finalización exitosa del autodespacho y redujo el volumen de llamadas al centro de atención, lo que bajó directamente el coste de servicio y mejoró la equidad de acceso.

## Argumento económico: motivaciones, retorno y coste total de propiedad

La rentabilidad de la UX opera por tres palancas: más éxito (más usuarios completan tareas valiosas), menor coste de servicio (menos contactos de soporte, menos formación, menos errores) y menos trabajo redobrado (correr en la dirección equivocada antes de construirla). En entornos empresariales donde los usuarios son cautivos, el retorno se manifiesta como productividad y menos errores, no como conversión; unos pocos segundos ahorrados por transacción, multiplicados por miles de empleados, se acumulan en un ahorro anual significativo.

El coste total de propiedad debe sopesar el coste de adoptar frente al de no adoptar. Los costes de adopción son fáciles de ver: investigadores y diseñadores, reclutamiento e incentivos para los participantes, herramientas y tiempo en el calendario. El coste de no adoptar es mayor, pero más difícil de detectar: transacciones abandonadas, sobrecarga de soporte y formación, rediseños tardíos y costosos, lanzamientos fallidos y exposición reputacional o legal cuando los servicios públicos excluyen a personas. Como esos costes se reparten entre presupuestos de soporte, formación y operaciones en lugar de la línea de producto, la dirección a menudo los subestima.

Para presentar el caso a la dirección, vincular la UX con las métricas que los directivos ya siguen: tasas de finalización y conversión, coste por transacción, volumen de tickets, días de formación y tasas de error y retrabajo. Ejecutar un piloto pequeño e instrumentado que muestre un antes-después medible y, a partir de ahí, extrapolar al portafolio. Enmarcar la investigación como reducción de riesgo en decisiones irreversibles suele resonar entre los interesados en finanzas y gobernanza.

## Antipatrones y trampas

- **Diseño por HiPPO**: decisiones tomadas por la opinión de la persona mejor pagada en lugar de por evidencia.
- **Teatro de investigación**: estudios realizados para justificar decisiones ya tomadas, cuyos hallazgos se ignoran.
- **Personas de ficción**: perfiles inventados, nunca validados con usuarios reales, que se usan para ganar argumentos.
- **Organigrama como AI**: navegación que replica los departamentos internos en lugar de las tareas del usuario.
- **Investigación de gran impacto puntual**: estudios raros y caros que llegan demasiado tarde para cambiar nada.
- **Probar solo el flujo ideal**: ignorar los estados de error, los casos límite y a los usuarios bajo presión.
- **Diseño como capa final de pintura**: traer la UX solo para que un build terminado «se vea bonito».
- **Ignorar a los usuarios asistidos y no digitales**: diseñar solo para usuarios confiados y bien conectados.

## Modelo de madurez

**Nivel 1: Iniciar.** No hay práctica de UX dedicada. Las decisiones se toman por la opinión y la intuición de la persona mejor pagada. La investigación, si existe, es ad hoc y reactiva, activada por un lanzamiento que salió mal. Los flujos y la terminología son inconsistentes entre equipos y nadie asume la experiencia global.

**Nivel 2: Desarrollar.** Algunos equipos tienen diseñadores y realizan pruebas de usabilidad ocasionales; existen unas cuantas personas o mapas de viaje, pero la práctica varía mucho entre grupos y no se mantiene. La UX se trata como una fase más y, bajo presión de plazo, a menudo se salta. Hay buenos momentos puntuales, pero no suman en el producto.

**Nivel 3: Estandarizar.** La investigación mixta y continua alimenta la priorización, y las personas, mapas de viaje y AI con vocabulario controlado están documentados y en uso entre equipos. Los controles de calidad UX, incluyendo benchmarks de usabilidad y verificaciones de accesibilidad, figuran en los criterios de finalización y se aplican en toda la organización. Un repositorio de investigación consultable mantiene los insights reutilizables en lugar de encerrados en las diapositivas de un solo equipo.

**Nivel 4: Gestionar.** La práctica se mide contra baselines en lugar de limitarse a ejecutarse. Se sigue el éxito en la tarea, el tiempo en tarea, la tasa de error, la satisfacción y la conformidad de accesibilidad como métricas acordadas, se fijan objetivos y se vigilan entre lanzamientos. Las muestras de participantes de investigación se contrastan con la base de usuarios real para que los hallazgos sean representativos, los controles de calidad reportan tasas de cumplimiento en lugar de opiniones, y el coste de la investigación se sopesa frente a las reducciones medidas en contactos de soporte, formación y retrabajo. Las decisiones de lanzar o retener se basan en la evidencia frente a esas baselines.

**Nivel 5: Orquestar.** La investigación es continua, vinculada a resultados e integrada con la planificación de producto, negocio y riesgo a nivel organizacional. Los equipos ejecutan experimentos controlados, cierran el ciclo de insight a cambio implementado a efecto medido y retiran o redefinen los modelos de usuarios a medida que la población y sus recorridos se transforman. El cimiento UX se adapta de forma permanente: personas, recorridos, AI y estándares se renuevan sobre evidencia, y la organización redistribuye dónde invierte su descubrimiento a medida que cambian la reversibilidad y el riesgo.

## Ideas para el debate

- ¿Cuánto descubrimiento es «suficiente» antes de comprometerse con una dirección, y quién lo decide?
- ¿Cómo se mantienen vivas las personas y los mapas de viaje en lugar de dejar que se conviertan en artefactos obsoletos?
- Cuando la analítica cuantitativa y la investigación cualitativa discrepan, ¿a cuál se confía y por qué?
- ¿Cómo debe una gran organización equilibrar un estándar central de UX con la autonomía de cada equipo?
- ¿Cuál es la forma adecuada de investigar servicios utilizados por personas en crisis sin añadirles carga?
- ¿Cómo se mide el retorno de una investigación que previene un error que, por eso, nunca se cometió?

## Ideas clave

- La UX es una manera de trabajar desde el inicio, no una capa de decoración al final.
- Combinar métodos cualitativos (el porqué) con cuantitativos (el cuántos).
- Modelar a los usuarios con personas basadas en evidencia, mapas de viaje, trabajos por los que se contrata y mapas de servicio.
- Estructurar la información según los modelos mentales de los usuarios, no según el organigrama.
- Entender el pensamiento de diseño como una mentalidad pragmática con ciclos de aprendizaje ajustados, no como un proceso rígido.
- El coste de investigar es insignificante frente al de construir bien la cosa equivocada.
- En entornos empresarial y gubernamental, la calidad de la UX se traduce directamente en productividad, coste de servicio y equidad de acceso.

## Referencias y lecturas complementarias

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville y Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen y cols., *Competing Against Luck* (trabajos por los que se contrata)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* y *Design Principles*
- U.S. General Services Administration, *18F Methods* y la guía de investigación del *U.S. Web Design System*
- Nielsen Norman Group, artículos y informes sobre métodos de investigación

