# 1.4 Formas de trabajar

## Visión general y motivación

Las «formas de trabajar» describen cómo se coordina, planifica, comunica y ejecuta el día a día en tu equipo. ¿Cómo se descompone el trabajo? ¿Quién habla con quién y en qué momento? ¿Cómo se rastrea el avance y cómo fluyen las decisiones y el conocimiento?

La mayoría de las organizaciones adopta alguna metodología con nombre propio: [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), algún marco de escalado, y da por hecho que los rituales que acompañan son la misma cosa que el valor que suponen. No lo son. Las metodologías que transformaron la entrega de software surgieron como reacción contra procesos pesados y fragmentados en cadenas de traspaso. Su objetivo era el feedback rápido, los lotes pequeños y los equipos con autonomía. Si se adoptan solo los ritos (las reuniones diarias, los sprints, los puntos de historia) sin los principios que los sustentan, se obtienen los costes del proceso sin la mitad de los beneficios: un [agilismo de ritual vacío](https://en.wikipedia.org/wiki/Cargo_cult) al más puro estilo cargo cult.

En equipos grandes, aquí es donde las buenas intenciones triunfan o fracasan. Mil ingenieros no pueden caber en la misma sala, asistir a la misma reunión ni compartir el mismo contexto tácito. A mayor tamaño, más se depende de la comunicación escrita, la colaboración asíncrona y una coordinación ligera en lugar de las reuniones y los conversatorios de pasillo. La escala cambia la física. Prácticas que funcionan a la perfección con ocho personas en el mismo lugar pueden colapsar con ochenta distribuidas por distintas ciudades. Y los marcos de escalado que prometen remediarlo a menudo reintroducen exactamente los traspasos y la centralización que [lo ágil](https://en.wikipedia.org/wiki/Agile_software_development) pretendía eliminar.

En las grandes empresas y en el sector público, cada una de estas presiones se siente con toda su intensidad. Abarcan múltiples zonas horarias, mezclan personal propio con contratados y proveedores externos, y suelen arrastrar puertas de control y reportes obligados. En ese contexto, una forma de trabajar centrada en la documentación, asíncrona y orientada a resultados no es un lujo. Es la única que escala. Las recomendaciones que siguen priorizan adaptar los principios al contexto antes que importar marcos completos, y prefieren prácticas escritas, asíncronas y transparentes que permitan a grandes equipos distribuidos y mixtos colaborar de verdad.

## Principios fundamentales

- Adóptense los principios, no los ritos; comprenda por qué existe una práctica antes de imitarla.
- Los lotes pequeños y el feedback rápido vencen a los planes grandes y los ciclos largos.
- Prefiera el flujo (limitar el trabajo en curso) al encajonamiento en intervalos fijos cuando la naturaleza del trabajo lo permita.
- Estímese para abrir conversaciones y planificar, no para fabricar una falsa precisión.
- Que lo asíncrono y lo escrito sean la norma; reserve el tiempo sincrónico para lo que verdaderamente lo exige.
- Que el trabajo y las decisiones sean visibles y documentados para que cualquiera pueda ponerse al día sin convocar una reunión.
- Se optimice por los resultados entregados, no por la actividad realizada ni por el aprovechamiento de capacidad.

## Recomendaciones

### Adapten Agile, Scrum, Kanban y Lean al contexto

Trátense como un kit de herramientas, no como una religión. Los sprints encajonados de Scrum convienen a equipos con trabajo de descubrimiento que se beneficia de un ritmo regular de planificación y revisión. El flujo continuo de Kanban, con sus límites explícitos de trabajo en curso, encaja en equipos con trabajo impredecible y guiado por interrupciones, como los de plataforma y operaciones. El enfoque de [Lean](https://en.wikipedia.org/wiki/Lean_software_development) en eliminar el desperdicio y acortar los tiempos de respuesta es el cimiento de ambos. Elija con intención. Mezcle lo que ayude; muchos equipos practican una variante [Scrumban](https://en.wikipedia.org/wiki/Scrumban). Conserve las prácticas que generan valor y suelte las ceremonias que se han vaciado de sentido. La prueba de fuego de cualquier práctica es sencilla: ¿acorta el feedback, reduce el tamaño del lote o aumenta la claridad? Si la respuesta es no, póngala en duda.

### Escalen con cautela, no por imitación

Los marcos de escalado ([SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), LeSS (Large-Scale Scrum), el popularizado «modelo de Spotify») prometen coordinar a muchos equipos. Acérquense con un ojo escéptico. SAFe aporta estructura y suele elegirse en grandes empresas y administraciones públicas por su exhaustividad y su ecosistema de formación, pero puede reintroducir la planificación pesada, la jerarquía y los traspasos que socavan la agilidad. LeSS se mantiene más cerca de los principios lean, pero exige un cambio organizativo profundo. El «modelo de Spotify» fue una instantánea de la cultura en evolución de una sola compañía, nunca una plantilla; ni siquiera Spotify lo ejecutaba como la mayoría imagina. Lo más sano es escalar reduciendo la necesidad de coordinación (a través de las topologías de equipos del capítulo anterior) en lugar de atornillar un marco de coordinación sobre una estructura fragmentada.

### Estimen con honestidad y ligereza

Los puntos de historia y la velocidad ayudan a un equipo a planificar su trabajo a corto plazo y a hablar de la complejidad relativa. No son una métrica de productividad, ni una moneda interequipo, ni una promesa. Nunca se convierta la velocidad en un objetivo: el inflado de puntos es la respuesta racional y la corruptela es inmediata. Para la previsión a más largo plazo, prefiera contar el throughput (volumen de entregas completadas) y apoyarse en datos históricos de tiempo de ciclo, que con frecuencia son más precisos que la suma de estimaciones. Muchos equipos maduros reducen la carga de estimación descomponiendo el trabajo en piezas pequeñas y homogéneas y limitándose a contarlas. Sea cual sea el método, recuerde: las estimaciones son pronósticos bajo incertidumbre, no compromisos. Comúniquense como rangos.

### Que lo asíncrono y lo documentado sea la norma

En organizaciones grandes y distribuidas, las reuniones sincrónicas no escalan y excluyen a quien está en otra zona horaria. Hágase la escritura la norma por defecto: documentos de diseño, [registros de decisiones](https://en.wikipedia.org/wiki/Architectural_decision), actualizaciones de estado por escrito y tickets lo bastante completos como para poder actuar sin una conversación en vivo. Graben y resuman las reuniones que no se pueden evitar. Una cultura documentada permite que alguien en otra zona horaria contribuya plenamente, que nuevos incorporados y contratados se integren leyendo, y deja una huella duradera. Reserve el tiempo sincrónico para la colaboración genuina, el mantenimiento de relaciones y la resolución ágil de la ambigüedad. Protejan bloques de concentración frente a la fragmentación que generan las reuniones.

### Trabajen bien con distintas zonas horarias, contratados y proveedores

La fuerza de trabajo distribuida y mixta es la norma a gran escala. Diseñen para el [seguir al sol](https://en.wikipedia.org/wiki/Follow-the-sun), donde los traspasos sean escritos y completos, no verbales. Fijen unas pocas horas de solape para el contacto sincrónico que sí se necesita, y distribuyan la carga de las horas incómodas con justicia en lugar de hacerla recaer siempre sobre la misma región. Con los contratados y proveedores, inviertan de más en contexto escrito, interfaces claras y herramientas compartidas, porque carecen del conocimiento tácito que el personal propio ha ido acumulando. Incorpórenlos a los mismos tableros visibles y a la misma documentación, en lugar de gestionarlos por un canal paralelo y opaco. En la medida de lo posible, estructuren los contratos en torno a resultados, no a horas.

## Compensaciones: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
| --- | --- | --- |
| Ágil (interacción con el cliente) | Alta colaboración y entrega de valor más rápida | Exige confianza y flexibilidad |
| Scrum (sprints en intervalos fijos) | Ritmo regular y previsible; reflexión incorporada | Sobrecarga de ceremonias; poco apropiado para trabajo guiado por interrupciones |
| Kanban (flujo continuo, límites de WIP) | Flexible; expone cuellos de botella; ideal para operaciones | Menos ritmo; requiere disciplina para limitar el trabajo en curso |
| SAFe / marco de escalado pesado | Estructura, formación, familiar para grandes organizaciones y sector público | Reintroduce jerarquía y traspasos; puede asfixiar la agilidad |
| LeSS / escalado ligero | Se mantiene cerca de los principios lean | Exige un cambio organizativo profundo |
| Asíncrono / centrado en documentación | Escala entre zonas horarias; es duradero e inclusivo | Más lento para temas ambigüos; exige disciplina de escritura |

La compensación de fondo es entre coordinación y autonomía, entre estructura y adaptabilidad. Más marco y más coordinación sincrónica compran previsibilidad y alineación, a costa de la velocidad, la sobrecarga y el empoderamiento del equipo. Menos marco compra velocidad y sentido de pertenencia, a costa de un posible desalineamiento entre muchos equipos. Para la mayoría de las grandes organizaciones, la mejor respuesta es un ritmo compartido mínimo sumado a una solidez en las prácticas escritas. Eso reduce la carga de coordinación en su origen, en lugar de gestionarla con un proceso más pesado.

## Cuestiones para debatir en el equipo

1. **Si la dirección pide la previsibilidad que un marco de escalado promete, ¿cómo se la dará sin reintroducir los traspasos que lo ágil pretendía eliminar?** Las grandes empresas y los programas del sector público suelen imponer planificación masiva a lo SAFe y reportes por puertas de control porque los organismos de supervisión exigen pronósticos y coordinación que puedan ver. Los factores en conflicto son genuinos: la dirección necesita previsibilidad y alineación entre muchos equipos, y los marcos pesados la compran a costa de la velocidad, la sobrecarga y precisamente esos traspasos que frenan la entrega. Traigan evidencia al debate: qué fracción de la semana laboral se pierde en eventos de planificación y coordinación de dependencias interequipo, y si esos eventos eliminan las dependencias o solo las ponen sobre la mesa. La jugada más firme es escalar reduciendo la necesidad de coordinación mediante la topología de equipos y luego satisfacer el reporting desde tableros en vivo e interfaces documentadas, en lugar de desde maratones de planificación. Decidan qué coordinación es real y cuál es mera ceremonia, y ofrézcanle a la dirección el pronóstico que necesita a partir de datos de throughput y tiempo de ciclo, no del sobrecoste de un marco.

2. **¿Qué van a hacer de concreto para impedir que la velocidad se convierta en una métrica de productividad entre equipos?** Los puntos de historia sirven para que un equipo planifique su propio trabajo a corto plazo, y pierden todo valor en el instante en que se comparan entre equipos o se fijan como meta, porque el inflado de puntos es la respuesta racional. En una organización grande, el impulso de agrupar la velocidad en un panel que los ejecutivos comparan entre sí es enorme y corrompe en silencio las estimaciones de las que los equipos dependen. Traigan la evidencia del desvío: ¿los puntos se inflan con el tiempo?, ¿los equipos hinchan las estimaciones?, ¿alguien se clasifica por velocidad? Prefieran contar el throughput y usar datos históricos de tiempo de ciclo para cualquier pronóstico que salga del equipo, y comuniquen las estimaciones como rangos bajo incertidumbre, no como promesas. El resultado debe ser un acuerdo explícito de que la velocidad nunca sale del equipo y que la previsión interequipo se basa en métricas de flujo.

3. **¿Cuál es el umbral concreto de «está escrito», y qué decisiones de verdad aún requieren una conversación en vivo?** Un default de documentación primero es lo que escala entre zonas horarias, contratados y proveedores, y supone una disciplina de escritura real que no todos han consolidado aún. Sea específico sobre el umbral: ¿un ticket trae suficiente contexto para actuar sin una llamada en vivo?, ¿las decisiones caen en un registro duradero?, ¿las reuniones que no se pueden evitar se graban y resumen? Para empresas y programas del sector público que mezclan personal propio con contratados que carecen de conocimiento tácito, el contexto escrito es lo que permite a una fuerza de trabajo mixta y distribuida contribuir plenamente. El contrapunto es que los temas ambigüos o controvertidos a menudo se resuelven más rápido en vivo, así que nómbralos explícitamente y reserven el escaso tiempo sincrónico para ellos. Decidan quién asume el coste de construir el hábito de escribir y de las horas incómodas de reunión, y distribuyan esa carga con justicia en lugar de cargarla siempre sobre la misma región.

4. **¿Qué ceremonias nuestras sobrevivirían si juzgáramos cada una únicamente por si acorta el feedback, reduce el lote o aumenta la claridad?** Las ceremonias se acumulan sin que nadie lo note: una diaria aquí, una de refinamiento allá, una revisión, una retrospectiva y una planificación, hasta que un equipo grande dedica más de su semana a reuniones recurrentes que al trabajo que esas reuniones pretenden servir. Los factores en conflicto son reales, porque un ritual que a una persona le parece puro sobrecoste puede ser el único lugar donde un equipo distribuido construye contexto compartido o revela un bloqueo. Traigan evidencia: el total de horas de reuniones recurrentes por persona y por semana, la asistencia y el compromiso en cada ceremonia, y qué decisión o señal produce cada una que no habría podido llegar por una actualización escrita. Para una empresa o programa del sector público donde cada equipo corre la misma cadencia impuesta, el coste acumulado es enorme; así que fijen una prueba explícita que cada ceremonia debe superar para mantener su franja, y estén dispuestos a recortar o fusionar las que solo persisten por inercia.

5. **Cuando el trabajo se estanca, ¿sabemos dónde está esperando realmente y estamos gestionando el flujo o solo el personal?** En la mayoría del trabajo de conocimiento, una tarea pasa muchísimo más de su vida en colas, traspasos y revisiones que en ejecución activa, y aun así los equipos reaccionan al retraso añadiendo personas o empujando por mayor aprovechamiento, lo que alarga las colas en lugar de acortarlas. La tensión es que limitar el trabajo en curso parece dejar capacidad ociosa, y las personas que parecen ociosas inquietan a los managers y a los organismos de supervisión. Traigan la evidencia que revela la realidad: distribuciones de tiempo de ciclo, la proporción de tiempo activo sobre el tiempo total de entrega, dónde se atascan los ítems en el tablero y cómo cambian el throughput los límites de trabajo en curso (un tope de cuántos ítems están en vuelo a la vez) cuando se cumplen. Para una gran organización o programa del sector público medido por el aprovechamiento del personal, esto reorienta la meta de mantener a todos ocupados a mantener fluyendo el trabajo terminado, y ese cambio suele ser la palanca de mayor impacto en la velocidad de entrega.

6. **¿Cómo va a absorber nuestra forma de trabajar a quienes no son personal fijo en la zona horaria del núcleo: los contratados, los proveedores y las regiones muchas horas desplazadas respecto a la sede central?** A escala, una fuerza de trabajo mixta y distribuida es lo normal, y las prácticas ajustadas a un equipo local excluyen silenciosamente a todos los demás: el proveedor gestionado por un canal privado, el contratado sin el contexto tácito, la región cuya jornada laboral nunca se solapa con la reunión donde se decide. Los factores tiran en sentidos opuestos, porque interfaces escritas más estrictas y traspasos completos exigen disciplina real y frenan la coordinación informal y veloz que un grupo colocalizado disfruta. Traigan evidencia: ¿quién suele estar ausente de las reuniones donde se toman decisiones?, ¿con qué frecuencia las regiones desfasadas quedan bloqueadas esperando un traspaso?, ¿los proveedores trabajan en los mismos tableros visibles que el personal o en un canal opaco y aparte? Para empresas y programas del sector público que mezclan personal fijo, contratados y proveedores en varias zonas horarias bajo reporting obligatorio, traten la práctica escrita, transparente y de seguir al sol como la línea base que permite a toda la fuerza de trabajo contribuir, y compartan la carga de las horas incómodas en lugar de imponerla siempre a la misma región.

## Perspectiva por sector

**Startup.** Con un puñado de personas y poca caja, saltense el catálogo de ceremonias y funcionen con el flujo más ligero posible: un tablero compartido, una actualización breve y escrita cada mañana y las decisiones registradas en un documento para que nadie quede bloqueado esperando a que un compañero despierte. Hagan de la escritura la norma desde el día uno, porque el hábito asíncrono es infinitamente más barato de construir con cinco personas que de implantar a posteriori con cincuenta. No adopten un marco de escalado que no necesitarán durante años; su ventaja es que apenas tienen nada que coordinar, así que protégan esa ventaja.

**Pyme.** Sin coach ágil ni manager de delivery en plantilla y con un presupuesto apretado, prefiera la práctica de estante a los marcos precertificados que arrastran costes de formación y acreditación que no puede justificar. Elija una metodología que encaje con su trabajo (Kanban para servicios guiados por interrupciones o un Scrum ligero para proyectos) y resista el impulso de comprar una herramienta pesada cuando un tablero sencillo y tickets claros bastan. Invierta el escaso esfuerzo de coordinación en poner todo por escrito para que un equipo pequeño no quede rehén de la memoria de una sola persona.

**Gran empresa.** Con muchos equipos, el problema es el coste de coordinación y la consistencia: un ritmo compartido mínimo, una definición común de qué significa «está escrito» y métricas de flujo que se agrupen sin convertir la velocidad en una meta interequipo. Escale reduciendo la necesidad de coordinar mediante la topología de equipos, no pegando un marco que reintroduce traspasos, y gobierne la forma de trabajar como algo que se ajusta con evidencia, no como un despliegue de una sola vez. Estandaricen las interfaces y el reporting para que la supervisión se satisfaga desde tableros en vivo, no desde maratones de planificación.

**Sector público.** Las reglas de contratación, las puertas de control obligadas y la rendición de cuentas ante la ciudadanía modelan cada decisión, y las fuerzas de trabajo mixtas (personal fijo, contratados y proveedores) se extienden por varias zonas horarias bajo un reporting de progreso exigido por la normativa. Prefieran una forma de trabajar centrada en la documentación y transparente, donde cada tarea lleve contexto completo escrito en un tablero visible para el personal y para los proveedores por igual, de modo que los informes de estado broten directamente del registro y no de reuniones aparte. Estructuren los contratos con proveedores en torno a resultados y visibilidad compartida en lugar de la facturación horaria opaca, y traten la huella escrita y auditable como un activo de cumplimiento, no como una carga.

## Ejemplos

**Startup.** Una startup distribuida de ocho personas salta el catálogo completo de ceremonias de Scrum y funciona con un tablero Kanban compartido más una actualización breve y escrita cada día en Slack. Como los dos fundadores están en zonas horarias distintas, hacen de la escritura la norma desde el primer día: cada decisión queda registrada en un documento, de modo que nadie se bloquea esperando a que el otro despierte. Cuando luego contratan en una tercera zona horaria, la incorporación se reduce a leer, y el hábito asíncrono escala sin cambio alguno. La práctica que nunca adoptaron, la reunión de estado sincrónica, es la que nunca extrañaron.

**Gran empresa.** Un banco multinacional implantó un marco de escalado en cientos de equipos, con planificación masiva trimestral incluida. El alineamiento mejoró en el papel, pero la entrega se frenó. Los equipos pasaban días en eventos de planificación y coordinando dependencias interequipo que el marco revelaba pero no eliminaba. El banco corrigió el rumbo: conservó solo el alineamiento interequipo ligero que realmente necesitaba, reestructuró los equipos para que cada uno fuera dueño de su corriente de valor de extremo a extremo, y desplazó la mayor parte de la coordinación a interfaces escritas y actualizaciones asíncronas. El tiempo de entrega se acortó y los agotadores maratones de planificación se redujeron a sincronizaciones focalizadas y ocasionales.

**Sector público.** Una agencia gubernamental que presta servicios al ciudadano operaba con personal fijo en una región y equipos de contratados en otras dos, abarcando varias zonas horarias, bajo un reporting de progreso mandado por la normativa. Adoptó una forma de trabajar basada en Kanban y centrada en la documentación. Cada tarea llevaba contexto completo escrito en un tablero compartido visible para el personal y para los proveedores por igual. Los traspasos entre regiones eran escritos y completos. Los informes de estado obligados emergían directamente del tablero, no de reuniones separadas. Esto permitió a una fuerza de trabajo distribuida y mixta colaborar de forma continua, satisfizo el reporting de supervisión como efecto colateral y redujo la dependencia de la agencia de las difíciles de programar reuniones interzonas.

## Caso de negocio: motivaciones, retorno de inversión y coste total

El argumento económico se apoya en la eficiencia del flujo. En la mayor parte del trabajo de conocimiento, el tiempo que una unidad de trabajo pasa en ejecución activa es una fracción pequeña de su tiempo total de entrega. El resto es espera: en colas, en reuniones, en traspasos, en lagunas de zona horaria. Las formas de trabajar que reducen el tamaño de los lotes, limitan el trabajo en curso y sustituyen los cuellos de botella sincrónicos por flujo asíncrono y escrito atacan esa espera de frente. El retorno es tiempos de entrega más cortos y mayor throughput sin añadir personal, además de menos defectos, porque el feedback llega antes y el contexto aún está fresco.

Pese el coste de adoptar frente al coste del statu quo. Lo centrado en documentación, lo asíncrono y el flujo lean cuestan principalmente un cambio de hábitos y una inversión inicial en escritura y herramientas. No requieren licencias caras. Los marcos de escalado pesados, por el contrario, arrastran un coste real: formación, certificaciones, roles dedicados y el sobrecoste continuo de grandes eventos de planificación. Solo una necesidad genuina de coordinación lo justifica. El coste de no hacer nada se manifiesta en calendares saturados de reuniones, colaboradores remotos excluidos, ceremonias vacías que consumen tiempo sin mejorar los resultados y una entrega lenta. Para el caso ante la dirección, midan el tiempo de entrega, la frecuencia de despliegue y la fracción de la semana laboral perdida en reuniones de bajo valor. Las pequeñas mejoras de flujo en una gran fuerza de trabajo se acumulan en grandes ganancias de capacidad.

## Antipatrones y trampas

- Agilismo de ritual: ejecutar ceremonias sin los principios que las sostienen.
- La velocidad como meta: invita al inflado de puntos y destruye la utilidad de la métrica.
- Adoración al marco: imponer SAFe o un «modelo de Spotify» por plantilla, sin mirar el ajuste.
- Estimaciones como compromisos: tratar pronósticos bajo incertidumbre como promesas vinculantes.
- Cultura de reunión: default a llamadas sincrónicas que excluyen a otras zonas horarias.
- Decisiones sin registro: conocimiento encerrado en las cabezas y en conversaciones pasadas.
- Cajas negras de proveedores: gestionar contratados por canales paralelos y opacos en vez de con visibilidad compartida.
- Obsesión por el aprovechamiento: maximizar el ajetreo de todos en lugar del flujo del trabajo terminado.

## Modelo de madurez

- **Nivel 1, Iniciar.** El proceso es ad hoc o ritualista; los equipos ejecutan ceremonias prestadas sin los principios que las sustentan, o improvisan sin un método compartido. La comunicación es de reunión a reunión y sin registro; las decisiones viven en las cabejas; las estimaciones se tratan como promesas. Los colaboradores distribuidos, los contratados y las zonas horarias desfasadas se coordinan por palabra y quedan bloqueados cada vez que la persona clave está dormida.

- **Nivel 2, Desarrollar.** Equipos individuales adoptan una metodología nombrada (Scrum o Kanban) y la siguen con cierta constancia, pero la práctica varía de un equipo a otro y las ceremonias suelen ser mecánicas. Algunos equipos escriben documentos de diseño y registros de decisiones; otros siguen dependiendo de las reuniones. La estimación y la coordinación ocurren, pero sin un umbral compartido de lo que significa «está escrito», de modo que el contexto aún se filtra y los traspasos interequipo siguen siendo pesados.

- **Nivel 3, Estandarizar.** Las prácticas se eligen con intención, encajan con el trabajo y se documentan como expectativa organizativa: un ritmo compartido mínimo, un umbral definido para el contexto escrito en tickets y registros de decisiones, la comunicación asíncrona y documentada como norma por defecto, y la estimación usada para la conversación y no para el control. El estándar se aplica de forma consistente, de modo que un contratado o un nuevo incorporado en cualquier equipo puede integrarse leyendo, y los proveedores trabajan en los mismos tableros visibles que el personal propio.

- **Nivel 4, Gestionar.** La forma de trabajar se mide frente a líneas base y no se da por sentada. Los equipos rastrean el tiempo de entrega, las distribuciones de tiempo de ciclo, la frecuencia de despliegue, el throughput y la fracción de la semana laboral perdida en reuniones de bajo valor, y vigilan que la velocidad no se falsee por inflado de puntos. Los límites de trabajo en curso se cumplen sobre la base de la evidencia; se gestiona el flujo, no el aprovechamiento, y los datos, no la opinión, deciden qué ceremonias conservan su franja y dónde se alargan las colas. El reporting a la dirección y a los organismos de supervisión brota directamente de esas métricas en vivo.

- **Nivel 5, Orquestar.** La organización ajusta continuamente su forma de trabajar a partir de métricas de flujo y de la evidencia de las retrospectivas, y minimiza la necesidad de coordinación en su origen mediante la topología de equipos en lugar de gestionarla con procesos más pesados. La forma de trabajar, las métricas de entrega y el diseño organizativo se integran y se adaptan a medida que cambian la fuerza de trabajo, el mercado y el panorama regulatorio; equipos distribuidos y mixtos de personal propio, contratados y proveedores en varias zonas horarias colaboran sin fricción, y las prácticas que dejan de justificar su coste se retiran sin ceremonia.

## Ideas para la reflexión

- ¿Qué ceremonias conservaríamos si las juzgáramos solo por el valor que generan?
- ¿Estamos escalando añadiendo un marco o reduciendo la necesidad de coordinar?
- ¿Nuestra velocidad es una ayuda para planificar o una meta que estamos falseando en silencio?
- ¿Qué decisiones y qué estados viven solo en reuniones y en la memoria de alguien, y deberían estar escritos?
- ¿Cuya zona horaria asume el coste de nuestras reuniones sincrónicas y es eso justo?
- ¿Nuestros contratados y proveedores trabajan en el mismo flujo visible que el personal propio?

## Ideas clave

- Adóptense los principios que hay detrás de las metodologías, no solo sus ritos.
- Elija Agile, Kanban o una mezcla en función del trabajo; priorice lotes pequeños y feedback rápido.
- Acérquese a los marcos de escalado con escepticismo; escale reduciendo la coordinación, no sumando proceso.
- Use las estimaciones para la conversación y la previsión, nunca como meta de productividad ni como promesa.
- Que lo asíncrono y lo documentado sea la norma para que grandes equipos distribuidos y mixtos puedan colaborar.
- Optímicese por los resultados y el flujo, no por la actividad ni el aprovechamiento.

## Referencias y lecturas adicionales

- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*
- Donald A. Reinertsen, *The Principles of Product Development Flow*
- Mary y Tom Poppendieck, *Lean Software Development: An Agile Toolkit*
- Craig Larman y Bas Vodde, *Large-Scale Scrum (LeSS)*
- Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate* (métricas de entrega)
- El Manifiesto Ágil y sus doce principios
- Henrik Kniberg, *Scaling Agile @ Spotify* (con la advertencia de que es una instantánea, no un modelo)
- El Handbook público de GitLab sobre trabajo asíncrono y remoto-first

