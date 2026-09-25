# 1.1 Valores de la ingeniería de software

## Visión general y motivación

Los [valores de la ingeniería de software](https://en.wikipedia.org/wiki/Software_engineering) son las creencias compartidas, las normas y las conductas cotidianas que configuran la forma en que las personas construyen software en conjunto. No son los carteles de la pared ni los versos del manual del empleado. Son lo que realmente ocurre cuando un incidente despierta a alguien a las tres de la madrugada, o cuando un ingeniero junior discrepa con un ingeniero principal, o cuando un plazo se choca con la calidad. Los valores son el sistema invisible que subyace a cada decisión técnica.

En un equipo pequeño, los valores se transmiten por ósmosis: la gente se sienta junta, absorbe las normas y se autocorrige. En un equipo grande, la ósmosis fracasa. Ya hay que hacer los valores explícitos, ponerlos por escrito, que los líderes los encarnen y reforzarlos a través de los sistemas. Si se omite ese paso, la cultura se fractura en decenas de microculturas incompatibles que gravan silenciosamente toda colaboración.

En un equipo grande, las consecuencias son estructurales. Los valores débiles se manifiestan en rotación, decisiones lentas, conocimiento acaparado e incidentes repetidos cuyas causas de raíz nunca se corrigen por completo. Los valores sólidos se manifiestan en cambios rápidos, seguros y fiables: los ingenieros detectan los problemas a tiempo, aprenden del fracaso y asumen la responsabilidad. La distancia entre ambos estados suele ser más amplia que cualquier decisión tecnológica.

Las organizaciones empresariales y gubernamentales lo sienten con particular crudeza, porque operan a gran escala, bajo escrutinio y en plazos prolongados. Los sistemas que se construyen hoy pueden funcionar durante una década o más, atendidos por personas que nunca se cruzaron con los autores originales. En ese contexto, la cultura es lo que transporta la intención a través del tiempo y la rotación de personal.

Las organizaciones reguladas enfrentan una presión adicional: la tentación de sustituir la confianza por el proceso. Cuando la responsabilidad es alta y los errores son visibles, el reflejo es acumular controles, firmas y reproches. Es comprensible, pero contraproducente. Las organizaciones más fiables, seguras y en cumplimiento son, por lo general, las que cultivan las culturas de aprendizaje más sólidas, no las más punitivas. Los valores y el cumplimiento normativo son aliados, no opuestos.

## Principios clave

- La [seguridad psicológica](https://en.wikipedia.org/wiki/Psychological_safety) es el cimiento; sin ella, todas las demás prácticas se degradan.
- El fracaso es un dato. El aprendizaje sin culpa convierte los incidentes en mejoras duraderas.
- La responsabilidad significa rendición de cuentas por los resultados, no solo por las entregas: «Quien lo construye, lo opera».
- Escribir es pensar. Una cultura que documenta sus decisiones escala su criterio.
- El ritmo sostenible supera al heroísmo; el [agotamiento profesional](https://en.wikipedia.org/wiki/Occupational_burnout) es un fallo del sistema, no un asunto personal.
- La [diversidad, equidad e inclusión](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) son fortalezas de ingeniería que mejoran la calidad de las decisiones.
- Los valores se encarnan desde la cima y se refuerzan desde la base; las acciones de los líderes pesan más que sus palabras.

## Recomendaciones

### Construir la seguridad psicológica con intención

La seguridad psicológica es la creencia compartida de que se puede hablar, hacer preguntas, admitir errores y cuestionar decisiones sin temor a la humillación ni al castigo. Es el predictor más fuerte de la eficacia de un equipo en los grandes estudios del sector. Hay que construirla con intención. Que los líderes asuman en voz alta sus propios errores («aquí está el error que cometí y lo que aprendí»). Recibir las malas noticias con curiosidad en lugar de con castigo. Invitar abiertamente la disensión en las reuniones. Rotar quién habla primero para que las voces senior no anclen la discusión. Y normalizar decir «no lo sé» y «necesito ayuda».

### Practicar el aprendizaje sin culpa

Cuando algo se rompe, examinen las condiciones que permitieron el fallo, no la persona que lo detonó. Adopten el [posmortem sin culpa](https://en.wikipedia.org/wiki/Postmortem_documentation): un registro escrito de lo que ocurrió, la cronología, los factores contribuyentes y acciones concretas con responsables y fechas. Partan del supuesto de que todos actuaron razonablemente dado lo que sabían en ese momento. Pregunten «¿qué hizo que fuera tan fácil equivocarse?» en lugar de «¿quién metió la pata?». Y sigan las acciones hasta su cierre. Una cultura de posmortem que nunca cierra sus seguimiento es puro teatro.

### Establecer modelos de responsabilidad claros

«Quien lo construye, lo opera» implica que el equipo que escribe un servicio es responsable de su operación, incluida la guardia técnica. Esto acorta el bucle de retroalimentación entre las decisiones de diseño y el dolor operativo, y eso mejora la calidad. Acompáñenlo con un catálogo de servicios que registre, para cada sistema, quién es el responsable, cómo contactarlo, sus dependencias y sus manuales de operación. Mantengan la responsabilidad explícita y sin solapamientos. La responsabilidad ambigua es cómo se pudren los sistemas y como los incidentes se prolongan. Cuando un equipo genuinamente no puede operar un sistema por sí solo, bríndele apoyo de plataforma en lugar de diluir la responsabilidad.

### Cultivar una cultura de escritura

Escribir afila el pensamiento y crea artefactos que atraviesan husos horarios y años. Hagan de los documentos de diseño y los registros de decisión una rutina para los cambios significativos: un texto breve que exponga el problema, las opciones consideradas, el enfoque propuesto y las compensaciones, circulado para comentarios antes de construir. Esto hace visible el desacuerdo mientras aún es barato resolverlo, y deja constancia duradera de por qué se decidió lo que se decidió. Mantengan las plantillas ligeras y las expectativas en proporción al peso de la decisión. Y reconozcan buena escritura en público.

### Proteger un ritmo sostenible

La cultura del héroe, en la que unas pocas personas rescatan una y otra vez a la organización con un esfuerzo insostenible, es síntoma de debilidad, no de virtud. Quema a la gente, concentra peligrosamente el conocimiento y oculta los problemas subyacentes que deberían corregirse. Así que midan y gestionen la carga de guardia. Si a una persona la llaman constantemente, traten eso como un defecto que hay que ingenierar y eliminar. Normalicen el tiempo libre, protejan el tiempo de enfoque y midan la producción por trimestre, no por semana.

### Tratar la diversidad, equidad e inclusión como una fortaleza de ingeniería

Los equipos diversos toman mejores decisiones. Ponen en la balanza más perspectivas y caen con menor frecuencia en el [pensamiento de grupo](https://en.wikipedia.org/wiki/Groupthink) y los puntos ciegos, y eso importa enormemente para la accesibilidad, la seguridad y el servicio a poblaciones amplias. Integren la inclusión en la ingeniería cotidiana: documentación accesible, lenguaje inclusivo en el código y las interfaces, prácticas de reunión que permitan a las voces más silenciosas participar, y una distribución equitativa entre el trabajo glamoroso y el trabajo de pegamento.

## Compromisos: ventajas e inconvenientes

| Enfoque | Ventajas | Inconvenientes |
| --- | --- | --- |
| Posmortem sin culpa | Reveal las causas de raíz reales; genera confianza; impulsa soluciones sistémicas | Puede parecer «falta de responsabilidad» a los de fuera; exige disciplina para cerrar las acciones |
| «Quien lo construye, lo opera» | Bucle de retroalimentación de calidad acortado; responsabilidad clara | Carga de guardia; requiere una plataforma sólida para evitar el agotamiento |
| Cultura de documentación previa / RFC | Decisiones duraderas; escala ante la rotación; compatible con el trabajo asíncrono | Más lento para cambios triviales; riesgo de burocracia si se aplica en exceso |
| Ritmo sostenible | Retención, fiabilidad, velocidad a largo plazo | Se percibe más lento durante los periodos de carga extrema; exige que la dirección sostenga la línea |

La tensión central es entre la rapidez a corto plazo y la salud a largo plazo. El heroísmo y la culpa compran un estallido de control aparente, pero luego provocan un colapso lento de la moral y la fiabilidad. El aprendizaje sin culpa, la responsabilidad clara y el ritmo sostenible se sienten más lentos en cualquier semana individual, pero se acumulan en una velocidad muy superior a lo largo de los trimestres y los años. Los líderes deben estar dispuestos a absorber la incomodidad a corto plazo para proteger la capacidad a largo plazo.

## Preguntas para debatir con el equipo

1. **¿Cómo mantienen que «sin culpa» no se lea como «sin responsabilidad» ante auditores, directivos y el público?** En una empresa regulada o un organismo público bajo supervisión, un posmortem que no nombra culpable puede parecer un encubrimiento a ojos de quienes están fuera de la ingeniería. Las tensiones son reales: se necesita la honestidad que solo la ausencia de culpa produce, y se necesita también que los decisores confíen en que los fracasos se abordan. Llevad evidencia concreta al debate, como la tasa de recurrencia de incidentes y el porcentaje de acciones cerradas tras un posmortem, porque un sistema que cierra sus seguimientos con fiabilidad es visiblemente responsable aunque no designe chivo expiatorio. Separen las dos preguntas que la cultura de la culpa funde en una: ¿qué hizo que fuera tan fácil equivocarse, y actúo alguien con negligencia genuina o de mala fe? Si la respuesta es que la responsabilidad reside en corregir las condiciones y cerrar las acciones, publiquen ese mecanismo para que los de fuera puedan ver la rendición de cuentas que buscan.

2. **¿Qué equipos sostienen sistemas de guardia que no pueden operar de forma realista, y quién asume esa brecha?** «Quien lo construye, lo opera» acorta el bucle de retroalimentación, y presupone que el equipo dispone del soporte de plataforma para operar lo que construyó. A escala empresarial y gubernamental, algunos equipos heredan sistemas legacy, cajas negras de proveedores o infraestructura transversal que ningún equipo pequeño puede asumir genuinamente en solitario. La tensión radica entre diluir la responsabilidad (malo) y dejar a un equipo a su merced con una alarma que no puede atender (también malo). Traed los datos de las llamadas: si una persona o un equipo es llamado constantemente, traten eso como un defecto que hay que ingenierar y eliminar, no como un distintivo de honor. La respuesta debería señalar dónde invertir en equipos de plataforma, despliegues escalonados y manuales de operación vigentes, para que la responsabilidad permanezca clara y la carga operativa sea humana.

3. **¿Las conductas que realmente premiáis coinciden con los valores que publicáis?** Los valores se convierten en cinismo en el instante en que los líderes premian lo que los carteles condenan, y a gran escala esa brecha permanece invisible hasta que la rotación y el acaparamiento silencioso de conocimiento la delatan. Miren con atención el último ciclo de promociones: ¿premió el rescate en crisis y el heroísmo, o la prevención y el trabajo de pegamento que mantiene sano a un gran equipo? Las empresas y organismos públicos multiplican el riesgo, porque los sistemas rígidos de categorías y los largos periodos de permanencia dejan que un incentivo desalineado se prolongue durante años antes de que nadie lo corrija. Traed evidencia real: quién fue promocionado, a quién se alabó en público y qué hizo realmente esa persona. Si el heroísmo obtiene las recompensas, están entrenando a la organización para fabricar las crisis que luego celebra resolver, y la solución es cambiar los incentivos, no el adorno de la pared.

4. **¿Cómo sabrían realmente si la seguridad psicológica es alta o baja en un equipo concreto, en lugar de suponerlo por el organigrama?** La seguridad es el cimiento sobre el que descansa toda práctica y, a la vez, lo más fácil de engañarse, porque los equipos con menos seguridad son los menos propensos a decirlo. A escala, la media de mil personas oculta la variación que sí importa: un solo manager puede dirigir en silencio un equipo basado en el miedo dentro de una organización de lo contrario sana. La tensión es entre la franqueza y la comodidad, porque las preguntas que revelan problemas reales son las que la gente está más reluctante a responder con honestidad, y recopilar la señal puede resultar en sí mismo inseguro. Traed evidencia concreta en lugar de impresiones: resultados a nivel de equipo de un instrumento validado de seguridad psicológica, la frecuencia con la que la gente admite errores por escrito, los incidentes evitados que se reportaron antes de convertirse en incidentes, y los temas que surgen en las entrevistas de salida. En una empresa u organismo público, exijan que los datos se mantengan a nivel de equipo y que nunca se usen para castigar a un equipo con puntuación baja, porque en el momento en que una puntuación de seguridad se convierte en un instrumento punitivo, deja de medir seguridad y empieza a medir el miedo a la propia medición.

5. **¿Cuál es la carga real de guardia y heroísmo, y están premiando a quienes previenen los incendios o a quienes los apagan?** El ritmo sostenible es donde las buenas intenciones se derrumban en silencio bajo la presión de entrega, y una organización grande puede sostenerse durante años con la hora extra invisible de unas pocas personas agotadas antes de notarlo. La tensión es honesta: el heroísmo realmente rescata en el momento, y depender de él concentra el conocimiento, oculta defectos sistémicos y agota a los ingenieros más comprometidos. Traed los datos operativos al debate: número de llamadas por persona y por semana, despliegues fuera de horario, la distribución de la carga de guardia en el equipo y cuánto de ella recae en los mismos nombres mes tras mes. Miren también a quién premió el último ciclo de promociones. En empresas y organismos públicos con escalas de categoría rígidas y largas permanencias, una cultura que paga por apagar incendios puede persistir sin cuestionamiento durante una década, así que la respuesta debería señalar dónde ingenierar la reducción de llamadas y cómo hacer que la prevención sea un acto visiblemente promocionable.

6. **¿Qué decisiones significativas de los últimos dos años no tienen un registro escrito de su razonamiento, y qué costará eso cuando los autores se marchen?** Una cultura de escritura es lo que transporta la intención a través de la rotación, y su ausencia es invisible hasta el momento exacto en que alguien necesita modificar un sistema que nadie comprende ya. La tensión contraria es la velocidad: escribir un documento de diseño o un registro de decisión se siente como fricción en el momento, y aplicada en exceso se convierte en burocracia que ralentiza los cambios triviales. Traed evidencia para calibrarlo: el porcentaje de cambios importantes que tienen un documento de diseño o registro de decisión, con qué frecuencia la gente puede encontrar y citar el razonamiento detrás de una arquitectura existente, y cuánto tarda un ingeniero nuevo en ser productivo en un servicio sin documentación. Para empresas y organismos públicos cuyos sistemas superan la permanencia de quienes los construyeron y que pueden enfrentarse a auditorías o solicitudes de acceso a la información, el registro escrito es al mismo tiempo memoria institucional y evidencia de diligencia debida, así que la respuesta debería trazar la línea donde el peso de la decisión justifica la escritura y no más abajo.

## Perspectiva por sector

**Startup.** Los valores aún se transmiten por ósmosis, así que no importen procesos pesados, pero nombren el o dos comportamientos que más importan, normalmente la honestidad sin culpa sobre los errores y la tendencia a traer malas noticias a tiempo. Los fundadores marcan el tono asumiendo en voz alta sus propios errores, porque en un equipo diminuto una sola reacción seca en el chat puede enseñar a todos a ocultar problemas durante meses. La escasez de recursos es motivo para proteger la seguridad, no para saltársela: un equipo que esconde bugs es mucho más caro que cinco minutos de retrospectiva.

**Pyme.** Sin un especialista dedicado a cultura de ingeniería y con un presupuesto ajustado, apóyense en ritos ligeros en lugar de herramientas que haya que comprar o mantener. Un canal compartido de incidentes, un registro de decisiones de una página y el hábito de preguntar «¿qué hizo que fuera tan fácil equivocarse?» no cuestan nada y transportan la mayor parte del valor. Sean deliberados también con la frontera entre comprar y construir prácticas: adopten una plantilla de posmortem ya existente y una sencilla rotación de guardia en lugar de crear un sistema a medida que no podrán mantener.

**Empresa.** A gran escala, el reto es la consistencia sin uniformidad: el aprendizaje sin culpa, la responsabilidad clara y sin solapamientos, y la cultura de escritura se convierten en normas organizativas respaldadas por herramientas, expectativas y un catálogo de servicios. La gobernanza y la auditoría empujan hacia los controles, así que hagan el caso de que una cultura de aprendizaje sólida es la opción más fiable y en cumplimiento, y demuéstrerlo con métricas de recurrencia de incidentes y tasa de cierre de acciones. Vigilen la variación entre equipos, porque las medias ocultan los focos de miedo que filtran talento y conocimiento en silencio.

**Sector público.** Las reglas de contratación, las obligaciones de transparencia y la rendición de cuentas ante la ciudadanía condicionan cómo se expresan los valores, especialmente en torno a la culpa. Un posmortem que no nombra culpable puede leerse como un encubrimiento ante la supervisión externa, así que publiquen el mecanismo, mostrando que la responsabilidad reside en corregir las condiciones y cerrar las acciones, y permitan que ciudadanías y auditores lo vean. Como los sistemas superan las legislaciones y la rotación de personal se mide en años, traten los registros de decisión como memoria institucional y evidencia de diligencia debida ante las solicitudes de acceso a la información.

## Ejemplos

**Startup.** Una startup de seis personas funciona con confianza y conversación de pasillo, así que nadie pone los valores del equipo por escrito. Un ingeniero fundador empuja una migración defectuosa y la CTO estalla con él en el chat, la sala se calla, y los dos bugs siguientes se ocultan en vez de reportarse. El equipo se recupera adoptando un solo hábito ligero: un chat de cinco minutos sin culpa con la pregunta «¿qué hizo que fuera tan fácil equivocarse?» tras cada incidente, sin plantilla. Ese pequeño rito mantiene sana la cultura osmótica sin la sobrecarga de proceso que una organización mayor necesitaría.

**Empresa.** Una gran entidad financiera sufrió una importante caída cuando un cambio rutinario de configuración se propagó en cascada por los servicios. En una cultura de la culpa, al ingeniero que empujó el cambio le habrían reprendido y habría sido el final del asunto. En cambio, un posmortem sin culpa reveló que la herramienta de despliegue hacía que el cambio peligroso se viera idéntico a uno seguro, que no existía un despliegue escalonado y que el manual de operación estaba desactualizado. La entidad invirtió en despliegues progresivos y validación de configuración, y ahora los cambios similares fallan de forma segura. Elegir mirar al sistema en vez de a la persona produjo una mejora de ingeniería duradera.

**Sector público.** Una agencia de servicios digitales del gobierno adoptó «Quien lo construye, lo opera» junto con un estricto proceso [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (propuesta de comentario) que prioriza la documentación. Como sus sistemas deben sobrevivir a los cambios de administración y a una rotación de personal medida en años, cada decisión significativa se registra en un documento de diseño que explica el contexto y las compensaciones. Los ingenieros nuevos y los contratistas entrantes pueden leer el razonamiento detrás de una arquitectura de una década de antigüedad en lugar de tener que reconstruirlo. Esa [memoria institucional](https://en.wikipedia.org/wiki/Institutional_memory) escrita es lo que permite a la agencia mantener los servicios públicos fiables a pesar de la alta rotación y las estrictas exigencias de rendición de cuentas.

## Caso de negocio: motivación, retorno y coste total

El retorno de la cultura es real pero indirecto, y por eso recibe crónicamente financiación insuficiente. A lo largo de la vida de un sistema, el coste dominante no es la construcción. Es el mantenimiento, la respuesta a incidentes, la retrabajación y el coste de perder y recontratar personas calificadas. Una cultura de aprendizaje sólida mejora todos esos frentes. El posmortem sin culpa reduce los incidentes repetidos. La responsabilidad clara reduce el tiempo medio de recuperación. Una cultura de escritura abarata el [onboarding](https://en.wikipedia.org/wiki/Onboarding) y el coste de las decisiones tomadas sin conocer el razonamiento que las precedió.

Solo con la rotación. Reemplazar a un ingeniero de nivel intermedio suele costar entre la mitad y el doble de su salario anual una vez que se cuentan la contratación, el periodo de rampa y el conocimiento institucional que se va con la persona. Si una cultura más sana reduce la rotación lamentable apenas un par de puntos porcentuales en una organización de mil personas, los ahorros eclipsan el modesto coste de ejecutar posmortem y escribir documentos. El coste de adoptar es, sobre todo, atención de liderazgo y algo de sobrecarga de proceso. El coste de no adoptar se paga de forma continua e invisible: entregas más lentas, incidentes recurrentes y fuga silenciosa de talento.

Para hacer el caso ante la dirección, vinculen la cultura con las métricas que los directivos ya siguen: tiempo de entrega, tasa de fallo del cambio, tiempo medio de recuperación, recurrencia de incidentes y rotación lamentable. Enmarquen la seguridad psicológica no como un beneficio intangible, sino como el mecanismo que hace que toda inversión de ingeniería dé fruto, porque los equipos inseguros ocultan precisamente los problemas que esas inversiones buscan resolver.

## Antipatrón y errores frecuentes

- Revisiones de incidentes basadas en la culpa: hunden los problemas bajo tierra y la gente deja de reportarlos.
- Culto al héroe: premiar la lucha contra el fuego en lugar de su prevención perpetúa los incendios.
- «Valores» que los líderes incumplen: los valores declarados contradichos por el comportamiento generan cinismo.
- Responsabilidad sin soporte: asignar guardia técnica para sistemas que los equipos no pueden operar de forma realista.
- El proceso como sustituto de la confianza: acumular firmas en vez de construir seguridad genuina.
- Teatro de documentación: escribir documentos que nadie lee o que nunca influyen en decisiones.
- Inclusión como casilla: contratar diversidad pero excluir esas mismas voces de las decisiones.

## Modelo de madurez

- **Nivel 1, Iniciación.** Los valores son accidentales y dependientes de la personalidad. Los incidentes significan culpa, el conocimiento vive en unas pocas cabezas y el heroísmo es la forma de resolver las cosas. Nadie ha escrito lo que el equipo cree ni cómo se comporta bajo presión.
- **Nivel 2, Desarrollo.** Algunos equipos inician posmortem sin culpa, redactan algún documento de diseño ocasional y hablan de responsabilidad, pero las prácticas son inconsistentes, se aplican de forma desigual y la dirección aún no las refuerza. Caer en un equipo sano depende en gran medida de la suerte.
- **Nivel 3, Estandarización.** El aprendizaje sin culpa, la responsabilidad clara y sin solapamientos, y la cultura de escritura son normas organizativas documentadas con plantillas, un catálogo de servicios y expectativas de guardia definidas. Los líderes encarnan los valores y se esperan los mismos comportamientos en todas partes, no solo donde cae un buen manager.
- **Nivel 4, Gestión.** La cultura se mide frente a líneas base y se controla con datos. Se siguen puntuaciones de seguridad psicológica a nivel de equipo, recurrencia de incidentes, tasa de cierre de acciones tras el posmortem, distribución de la carga de guardia, tiempo medio de recuperación y rotación lamentable, y se actúa sobre los números cuando un equipo se desvía. Se eliminan los incentivos al rescate en crisis con base en la evidencia, y se premia la prevención porque ahora se puede ver.
- **Nivel 5, Orquestación.** La cultura se mejora de forma continua e integrada con cómo la organización planifica, contrata y promueve. La seguridad es alta, el aprendizaje es rápido y las prácticas se adaptan a medida que cambian la evidencia y el contexto. La organización reequilibra la carga de guardia, actualiza los registros de decisión y evoluciona sus normas de forma deliberada, en lugar de esperar a que una crisis lo fuerce.

## Ideas para la reflexión

- ¿Dónde en nuestra organización la gente no se siente segura de decir «no lo sé» o «no estoy de acuerdo», y por qué?
- ¿Nuestras revisiones de incidentes cambian el sistema o solo asignan la culpa y pasan página?
- ¿Estamos premiando heroísmos que deberíamos ingenierar y eliminar?
- ¿Qué decisiones importantes de los últimos dos años no tienen un registro escrito de su razonamiento?
- ¿Cómo se distribuyen el trabajo de pegamento y la carga de guardia entre el equipo?
- ¿Nuestros valores declarados coinciden con lo que aquí realmente consigue ser promovido?

## Ideas fundamentales

- Los valores son el sistema operativo invisible detrás de cada decisión técnica; a gran escala, deben ser explícitos.
- La seguridad psicológica es el cimiento; sin ella, las demás prácticas se degradan.
- El aprendizaje sin culpa convierte el fracaso en mejora sistémica duradera.
- La responsabilidad clara («Quien lo construye, lo opera») acorta el bucle de retroalimentación de calidad.
- La cultura de escritura escala el criterio a través de husos horarios y rotación.
- El ritmo sostenible y la inclusión son multiplicadores de velocidad a largo plazo, no costes.

## Referencias y lecturas complementarias

- Amy C. Edmondson, *The Fearless Organization* y *Teaming*
- Investigación de Google re:Work / Project Aristotle sobre la eficacia de equipos
- Sidney Dekker, *The Field Guide to Understanding 'Human Error'*
- John Allspaw, «Blameless PostMortems and a Just Culture» (*Etsy Code as Craft*)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Gene Kim y col., *The Phoenix Project* y *The DevOps Handbook*
- Camille Fournier, *The Manager's Path*
- Will Larson, *An Elegant Puzzle: Systems of Engineering Management*
- Tom DeMarco y Timothy Lister, *Peopleware: Productive Projects and Teams*

