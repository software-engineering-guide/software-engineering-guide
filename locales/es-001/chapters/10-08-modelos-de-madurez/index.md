# 10.8 Modelos de madurez

## Presentación y motivación

Un [modelo de madurez](https://en.wikipedia.org/wiki/Maturity_model) es una manera estructurada de evaluar cuán capaz y consistente es tu práctica en algún dominio, y de describir un camino para mejorarla. Define una pequeña escalera de niveles. En la parte inferior, el trabajo es ad hoc y reactivo. En la superior, se mide, gestiona, y optimiza continuamente. Cada peldaño tiene características observables contra las que puedes comprobar.

Los modelos de madurez convierten una pregunta vaga («¿somos buenos en esto?») en una respuesta repetible («estamos en el nivel 2 aquí, nivel 4 allá, y esto es lo que requeriría el nivel 3»). Este libro usa un modelo de cinco niveles en cada capítulo y los consolida en el capítulo 12.4. Este capítulo trata de la disciplina misma: cómo funcionan los modelos, cuándo ayudan, y cómo engañan.

La razón por la que importan es simple. Las grandes organizaciones no pueden mejorar lo que no pueden ver. A través de docenas de equipos, la capacidad varía enormemente e invisiblemente. Algunos equipos tienen excelentes pruebas y seguridad débil; otros tienen lo contrario. Un modelo de madurez te da un vocabulario compartido y una vara de medir común, para que las brechas se vuelvan comparables, la inversión pueda priorizarse, y el progreso pueda rastrearse con el tiempo en lugar de meramente afirmarse. Ejemplos conocidos incluyen CMMI ([Integración del Modelo de Madurez de Capacidad](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), para el proceso), el modelo DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (rendimiento de entrega de software), OWASP SAMM (Modelo de Madurez de Garantía de Software) y BSIMM (Modelo de Madurez de Construcción de Seguridad Incorporada) para la seguridad de software, TMMi (Integración del Modelo de Madurez de Pruebas, para las pruebas), el modelo de Fluidez Ágil, y los modelos de madurez de gestión de datos, más incontables tarjetas de puntuación internas.

Para la empresa y especialmente el gobierno, los modelos de madurez llevan un peso particular. La contratación gubernamental ha usado durante mucho tiempo los niveles de evaluación CMMI como una calificación de proveedor, y marcos como el CMMC estadounidense ([Certificación del Modelo de Madurez de Ciberseguridad](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) vinculan la madurez de ciberseguridad directamente con la elegibilidad para el trabajo de defensa. Eso da a los modelos de madurez dientes reales. También crea el riesgo central de este capítulo: cuando un nivel se convierte en una puerta o un objetivo, la gente optimiza para la evaluación en lugar de la capacidad subyacente. Bien usados, los modelos de madurez son un espejo. Mal usados, son teatro.

## Principios fundamentales

- **La madurez es un medio, no un fin.** La meta es la capacidad y los resultados, no un número de nivel.
- **Evalúa para aprender, no para puntuar.** La autoevaluación honesta supera a una evaluación halagadora.
- **Más alto no siempre es mejor.** El objetivo correcto depende del riesgo, el contexto, y el costo.
- **Mide por dominio, no una única calificación global.** La capacidad es desigual; un único número la oculta.
- **Prioriza primero las brechas de madurez más baja y riesgo más alto.**
- **Cuidado con la [Ley de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Una vez que un nivel es un objetivo, deja de medir la capacidad.
- **Vuelve a evaluar periódicamente.** La madurez deriva a medida que cambian la gente, los sistemas, y las amenazas.

## Recomendaciones

### Elige el modelo correcto para el dominio

Ajusta el modelo a la capacidad que quieres mejorar, y prefiere los modelos establecidos y basados en evidencia sobre los inventados donde existan:

- **Proceso y entrega:** CMMI (madurez de proceso amplia), el modelo de capacidad DORA (rendimiento de entrega, fundamentado en investigación, capítulo 11.2).
- **Seguridad:** OWASP SAMM y BSIMM (prácticas de seguridad de software), CMMC (ciberseguridad de defensa).
- **Pruebas y calidad:** TMMi.
- **Ágil y formas de trabajar:** el modelo de Fluidez Ágil (capítulo 10.7).
- **Datos:** modelos de madurez de gestión de datos (DMM, DCAM).

Para el uso interno, una escala simple de cuatro o cinco niveles aplicada por capacidad (como hace este libro) a menudo es más accionable que un marco externo pesado. Reserva los modelos formales y evaluados para donde sean contractualmente requeridos.

### Evalúa honestamente y por capacidad

Ejecuta evaluaciones que produzcan verdad, no comodidad. Involucra a la gente que hace el trabajo. Recopila evidencia en lugar de opiniones. Puntúa cada capacidad por separado, para que la imagen refleje la realidad: fuerte aquí, débil allá. Una autoevaluación usada para guiar la mejora vale más que una evaluación externa usada para ganar una insignia, porque la primera premia la franqueza y la segunda premia la presentación. El capítulo 12.4 provee una autoevaluación consolidada a través de cada dominio de este libro; úsala como instrumento inicial.

### Usa la madurez para priorizar, no para castigar

La salida de una evaluación es un atraso de mejora priorizado, no una tarjeta de reporte para la culpa. Combina la madurez con el riesgo. Una capacidad de nivel 1 en un área de bajo riesgo puede estar bien. Una capacidad de nivel 2 en un área crítica para la seguridad o el cumplimiento es urgente. Dirige la inversión hacia las brechas donde la baja madurez se encuentra con el alto riesgo, y conecta el trabajo con los resultados (capítulo 11.1) para que la mejora se mida por resultados, no por subir la escalera por sí misma.

### Fija los niveles objetivo deliberadamente: más alto no es gratis

Cada nivel arriba cuesta esfuerzo y a menudo añade peso de proceso. El objetivo correcto rara vez es «nivel 5 en todas partes». Es el nivel donde la capacidad extra todavía justifica el costo extra para el riesgo de ese dominio. Las capacidades reguladas y críticas para la seguridad pueden genuinamente necesitar los peldaños superiores, y la auditoría a menudo requiere al menos un nivel 3 «definido». Muchas otras están bien servidas en el nivel 3 y solo acumularían burocracia empujando más allá. Decide los objetivos por capacidad, y deja de subir cuando el retorno ajustado al riesgo lo haga.

### Protégete contra el teatro de madurez

El único modo de fallo que destruye el valor de los modelos de madurez es optimizar para la puntuación. Vigila las evaluaciones que califican generosamente, la evidencia ensamblada solo para la evaluación, o las afirmaciones de «nivel 5» que los incidentes de producción contradicen. Mantén la evaluación vinculada al comportamiento observable y los resultados reales. Rota o comprueba externamente la cordura de tus evaluadores. Trata una autopuntuación sospechosamente alta como un olor. En el momento en que el nivel se convierte en la meta, el modelo deja de decirte la verdad.

## Ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| **Modelos formales evaluados (CMMI, CMMC)** | Comparables, reconocidos contractualmente, rigurosos | Costosos; invita a la manipulación; puede osificar el proceso |
| **Tarjetas de puntuación internas ligeras** | Rápidas, accionables, baja sobrecarga | Menos comparables externamente; fácil de sesgar |
| **Modelos de capacidad basados en evidencia (DORA)** | Vinculados a resultados reales; respaldados por investigación | Alcance más estrecho; necesita métricas reales |
| **Una única calificación de madurez global** | Simple de comunicar | Oculta la capacidad desigual; engaña |
| **Evaluación por capacidad** | Priorización precisa y accionable | Más esfuerzo; sin un único número destacado |

La tensión central es **evaluación como espejo frente a evaluación como objetivo**. El mismo modelo que ayuda a un equipo a verse claramente se vuelve contraproducente en el instante en que un nivel se vincula a la recompensa, la elegibilidad, o el estatus. Cuanto más importa un nivel, más energía fluye hacia la apariencia de madurez en lugar de la sustancia.

## Preguntas para discutir con tu equipo

1. **¿Deberíamos mantener una autoevaluación interna franca separada de cualquier nivel evaluado contractualmente, y quién posee cada uno?** Cuando un nivel CMMC o CMMI bloquea los ingresos, la evaluación y la verdad se separan, porque la energía fluye hacia pasar en lugar de mejorar. Para una gran empresa o un proveedor gubernamental, esa brecha es donde se oculta el riesgo: pasas la auditoría y permaneces expuesto. Lleva dos libros a propósito. Mantén la evaluación formal para la elegibilidad, y mantén una tarjeta de puntuación interna franca por la que nadie sea premiado por inflar. Nombra un dueño para cada una, y trata cualquier distancia entre ellas como una señal para investigar, no para tapar. Trae los incidentes recientes, los casi accidentes, y el deterioro posterior a la evaluación a la reunión como evidencia de qué libro dice la verdad.

2. **Para cada dominio, ¿estamos adoptando un modelo establecido y basado en evidencia o inventando nuestra propia tarjeta de puntuación, y es esa la decisión correcta?** Los modelos establecidos (DORA para la entrega, SAMM o BSIMM para la seguridad, TMMi para las pruebas) llevan investigación y comparabilidad externa que una rejilla casera no puede igualar. Una escala interna ligera de cuatro niveles es más rápida y accionable, y a menudo es la mejor elección para la dirección interna. La trampa es inventar un marco pesado y a medida que tiene toda la ceremonia de un modelo formal y ninguna de la base de evidencia. Decide por dominio: reserva los modelos formales evaluados para donde un contrato los requiera, usa los modelos basados en evidencia donde existan y se ajusten, y mantén una escala simple por capacidad para todo lo demás. Trae la lista de dominios, marca qué modelo usa cada uno hoy, y desafía cada tarjeta de puntuación inventada.

3. **¿Quién ejecuta nuestras evaluaciones, cómo atraparíamos la calificación generosa, y con qué frecuencia volvemos a evaluar?** Una evaluación que se califica a sí misma se halaga a sí misma, y la madurez deriva a medida que cambian la gente, los sistemas, y las amenazas, así una evaluación de dos años a menudo es ficción. Rota a los evaluadores o trae una comprobación de cordura externa, y trata una autopuntuación sospechosamente alta como un olor que perseguir, no una victoria que celebrar. Fija una cadencia de reevaluación vinculada a cuán rápido cambia cada dominio: la seguridad más a menudo que, digamos, la documentación. Recopila evidencia e involucra a la gente que hace el trabajo en lugar de recolectar opiniones de gerentes. Si tu respuesta es que un equipo se puntúa a sí mismo una vez al año sin contraverificación, estás midiendo comodidad, no capacidad.

4. **¿Qué nivel de madurez objetivo realmente necesita cada capacidad, y dónde empujar más alto solo nos compraría peso de proceso?** Más alto no es gratis: cada nivel arriba cuesta esfuerzo y usualmente añade ceremonia, así una meta general de nivel 5 en todas partes drena un presupuesto finito de mejora hacia burocracia que algunos dominios nunca repagarán. Para una organización grande el objetivo correcto varía por capacidad, porque un área de bajo riesgo sentada en el nivel 2 puede ser perfectamente segura mientras un área crítica para la seguridad o el cumplimiento en el mismo nivel es una emergencia. Trae una clasificación de riesgo por capacidad, una estimación honesta de qué cuesta el siguiente peldaño en esfuerzo y proceso, y cualquier piso de auditoría o contractual, ya que muchas auditorías requieren al menos un nivel 3 definido. En entornos empresariales y gubernamentales, algunas capacidades reguladas genuinamente necesitan los peldaños superiores mientras la mayoría están bien servidas en el nivel 3, así que decide los objetivos deliberadamente, capacidad por capacidad, y deja de subir cuando el retorno ajustado al riesgo lo haga.

5. **La última vez que subimos un nivel de madurez, ¿realmente mejoró el resultado que se suponía debía proteger, o solo se movió la puntuación?** Un nivel que sube mientras los incidentes, el tiempo de espera, o las tasas de defectos se mantienen planos es la Ley de Goodhart en acción: una vez que el número se convierte en el objetivo, deja de medir la capacidad. Para un equipo grande esto se cuela fácilmente, porque una evaluación exitosa se siente como progreso incluso cuando la producción cuenta una historia distinta. Vincula el nivel de cada capacidad a una métrica de resultado real antes de invertir, luego trae la evidencia de antes y después a la discusión: incidentes por trimestre, tasa de fallo de cambio, tiempo de recuperación, lo que sea que la capacidad exista para mejorar. En carteras empresariales y gubernamentales donde un nivel evaluado bloquea la elegibilidad, la brecha es peligrosa, porque el nivel puede subir con evidencia ensamblada mientras la práctica subyacente silenciosamente se deteriora, y la primera prueba de eso es una brecha, interrupción, o auditoría fallida.

6. **¿Comunicamos una única calificación de madurez destacada o una imagen por capacidad, y alguna vez se vinculan los niveles a la recompensa, la clasificación, o el estatus de equipo?** Un único número general es fácil de presentar al liderazgo y oculta exactamente la desigualdad que importa, porque una entrega fuerte puede enmascarar una capacidad de seguridad de nivel 1; un mapa de calor por capacidad es más trabajo pero muestra dónde la baja madurez se encuentra con el alto riesgo. La pregunta más difícil es cómo se usan las puntuaciones, porque en el momento en que un nivel se vincula a la recompensa o clasificación de un equipo, el reporte honesto muere y el esfuerzo fluye hacia la apariencia de madurez en lugar de la sustancia. Trae el mapa de calor, y un relato franco de cada lugar donde un nivel actualmente alimenta una revisión de desempeño, una decisión de presupuesto, o una tarjeta de puntuación de proveedor. Para las empresas y proveedores gubernamentales, donde los niveles evaluados pueden bloquear los ingresos y la elegibilidad, sé explícito sobre qué calificaciones llevan consecuencias y cuáles existen solo para dirigir, porque una imagen de madurez que la gente es premiada por inflar deja de describir la realidad.

## Perspectiva sectorial

**Startup.** Un modelo pesado evaluado es sobrecarga que no puedes costear con poco fondo de operación. Ejecuta una autoevaluación de una hora en una escala simple a través de un puñado de capacidades, arregla solo la brecha de madurez más baja que bloquea algo concreto (digamos, el cuestionario de seguridad de tu primer cliente empresarial), y deja el resto en paz. La evaluación debería costar una tarde, no un consultor, y su salida es una única acción siguiente en lugar de una puntuación alta uniforme que ni necesitas ni puedes financiar.

**Pequeña empresa.** Sin un evaluador dedicado y con un presupuesto ajustado, toma prestado un modelo público ligero en lugar de encargar un marco a medida: una lista de comprobación corta de entrega o seguridad que puedas autopuntuar. Trátalo como una conversación anual sobre dónde un punto débil te costaría un cliente, no un programa permanente. Mantenlo barato y directo, porque una puntuación halagadora que pagaste a un proveedor para producir vale menos que una franca que hiciste tú mismo en una tarde.

**Empresa.** El valor es una tarjeta de puntuación compartida por capacidad aplicada consistentemente entre muchos equipos, para que las brechas se vuelvan comparables y el presupuesto de mejora fluya hacia donde la baja madurez se encuentra con el alto riesgo. Protégete fuertemente contra el teatro de madurez una vez que los niveles alimenten el presupuesto o el estatus: rota o comprueba externamente la cordura de los evaluadores, y gestiona los resultados como un mapa de calor que dirige la inversión en camino pavimentado (capítulo 4.2) en lugar de una tabla de clasificación que rankea a los equipos y mata el reporte honesto.

**Gobierno.** Un nivel de madurez a menudo es una puerta literal aquí: CMMC para el trabajo de defensa, una evaluación CMMI como calificación de proveedor. Cumple el nivel requerido con capacidad genuina, y mantén una autoevaluación interna franca separada de la evaluación formal para que el piso de auditoría nunca se convierta silenciosamente en el techo. Documenta la evidencia transparentemente para los evaluadores, y trata cualquier distancia entre el nivel certificado y la práctica real como un riesgo responsable que cerrar, no papeleo que archivar.

## Ejemplos

**Startup.** Una startup SaaS de diez personas ejecuta una autoevaluación de una hora contra una escala simple de cuatro niveles que cubre la entrega, las pruebas, la seguridad, y la guardia. Encuentra la entrega y las pruebas en el nivel 3 pero la seguridad estancada en el nivel 1, que importa porque está a punto de firmar su primer cliente empresarial con un cuestionario de seguridad. Así que los fundadores pasan el mes siguiente elevando solo la seguridad a un nivel 2 defendible y dejan el resto en paz, en lugar de perseguir una puntuación alta uniforme que todavía no necesitan ni pueden permitirse.

**Empresa.** Una firma de servicios financieros evalúa sus 40 equipos con una tarjeta de puntuación ligera por capacidad (entrega, pruebas, seguridad, observabilidad, guardia). El mapa de calor revela que la madurez de seguridad se retrasa más donde la exposición regulatoria es más alta, así el equipo de plataforma financia primero las herramientas de seguridad de camino pavimentado (capítulo 4.2) para esos equipos. Porque la evaluación se usa para priorizar la inversión en lugar de rankear equipos, los gerentes reportan honestamente. La reevaluación un año después muestra movimiento real, y, crucialmente, menos incidentes de seguridad, no solo puntuaciones más altas.

**Gobierno.** Un contratista de defensa debe alcanzar un nivel CMMC requerido para licitar trabajo, y un integrador de sistemas sostiene una evaluación CMMI como calificación de contrato. Aquí el nivel de madurez es una puerta literal a los ingresos. La versión bien operada trata el nivel requerido como un piso para la capacidad genuina y mantiene una autoevaluación interna franca separada de la evaluación formal. La versión mal operada ensambla evidencia para la evaluación y deja que la práctica real se deteriore al día siguiente, pasando la auditoría mientras permanece expuesta.

## Caso de negocio: motivaciones, ROI y TCO

El retorno de la evaluación de madurez viene de la **inversión dirigida**. Los presupuestos de mejora son finitos. Gastados a ciegas, financian lo que sea más ruidoso. Una evaluación de madurez te muestra dónde la capacidad es más débil contra el riesgo, así el mismo gasto compra más reducción de riesgo y más mejora de resultado. La evaluación misma es barata, solo días de revisión estructurada y basada en evidencia, comparada contra el costo de programas de mejora mal asignados o, peor, una brecha de capacidad no detectada que aparece como una brecha, interrupción, o auditoría fallida.

Sobre el **costo total de propiedad**, la disciplina es de bajo costo cuando la mantienes ligera y de alto costo cuando se endurece en burocracia de evaluación. El costo oculto dominante es el *teatro de madurez*: el esfuerzo gastado produciendo la apariencia de madurez no retorna nada y puede enmascarar el riesgo real, que es ROI negativo. Para presentar el caso al liderazgo, presenta la madurez como una lente de riesgo e inversión, un mapa de calor que convierte «mejora todo» en «mejora estas tres cosas primero», y presupuesta explícitamente contra la tentación de perseguir niveles por sí mismos. Donde un nivel se requiere contractualmente (CMMC, CMMI), el ROI es directo: es el precio de la elegibilidad, y la meta es cumplirlo con capacidad real en lugar de pretensión costosa.

## Antipatrones y trampas

- **El nivel como meta:** perseguir un número en lugar de la capacidad que se supone que representa.
- **Teatro de madurez:** ensamblar evidencia para una evaluación mientras la práctica real se deteriora.
- **Una calificación global:** una única puntuación de madurez que oculta una desigualdad peligrosa.
- **Más alto siempre es mejor:** empujar cada capacidad al nivel 5 sin importar el riesgo o costo.
- **Evaluar una vez, nunca más:** una evaluación única tratada como verdad permanente.
- **Rankear equipos para culpar:** usar la madurez para el castigo, lo cual mata el reporte honesto.
- **Culto al modelo:** seguir la ceremonia de un marco pesado más allá del punto de utilidad.
- **Ignorar los resultados:** subir la escalera mientras la entrega, la fiabilidad, o la seguridad no mejoran.

## Modelo de madurez

- **Nivel 1, Iniciar.** Sin noción compartida de madurez; la capacidad se asume, es desigual, y no se mide; cualquier evaluación es reactiva, disparada por un incidente o una demanda de auditoría en lugar de planificada.
- **Nivel 2, Desarrollar.** Unos pocos equipos ejecutan evaluaciones ad hoc contra alguna escala, pero el modelo, la cadencia, y el rigor varían de equipo a equipo; los resultados se usan inconsistentemente y la evidencia es escasa, así puntuar por apariencia es un riesgo siempre presente.
- **Nivel 3, Estandarizar.** Un único modelo por capacidad y cadencia de evaluación están documentados y se aplican en toda la organización; las evaluaciones están basadas en evidencia, involucran a la gente que hace el trabajo, y alimentan un atraso de mejora priorizado en lugar de una tarjeta de reporte.
- **Nivel 4, Gestionar.** La madurez se mide y controla con datos: el nivel de cada capacidad se rastrea contra una línea base, se vincula a una métrica de resultado (incidentes, tiempo de espera, tasa de fallo de cambio), y se vuelve a evaluar en una cadencia fija, así la deriva y la calificación generosa aparecen como números en lugar de opiniones, y los objetivos se fijan deliberadamente por dominio contra el riesgo y el costo.
- **Nivel 5, Orquestar.** La evaluación se integra en toda la organización y se mejora continuamente: la madurez, el riesgo, y los resultados informan la inversión como una imagen adaptativa, los objetivos se reequilibran a medida que cambian las amenazas y el contexto, los evaluadores se rotan o se comprueban externamente como cuestión de rutina, y la práctica activamente retira la ceremonia que ya no se gana su costo.

## Ideas para el debate

1. ¿Cuáles de tus capacidades estás asumiendo que son maduras sin evidencia?
2. ¿Dónde coincide tu madurez más baja con tu riesgo más alto, y ahí es donde va tu presupuesto de mejora?
3. ¿Es algún nivel de madurez en tu organización un objetivo o una puerta? ¿Qué comportamiento ha producido eso?
4. ¿Cuál es el nivel objetivo correcto para cada capacidad, y dónde subir más solo añadiría burocracia?
5. ¿Reportarían tus equipos su madurez honestamente, o la manera en que usas las puntuaciones castiga la franqueza?
6. Cuando «mejoraste la madurez» por última vez, ¿realmente cambiaron los resultados?

## Puntos clave

- Un modelo de madurez evalúa la capacidad contra una escalera de niveles y describe un camino para mejorar: un espejo, no un trofeo.
- Elige modelos establecidos y basados en evidencia por dominio (CMMI, DORA, SAMM/BSIMM, CMMC); una escala ligera por capacidad a menudo es más accionable.
- **Evalúa honestamente, por capacidad**, y usa los resultados para **priorizar por riesgo**, no para rankear o culpar.
- **Más alto no siempre es mejor:** fija los niveles objetivo deliberadamente contra el riesgo y el costo.
- Cuidado con el **teatro de madurez** y la **Ley de Goodhart**: un nivel que se convierte en un objetivo deja de medir la capacidad.
- Véase el capítulo 12.4 para la autoevaluación de madurez consolidada de este libro, y la sección de madurez propia de cada capítulo.

## Referencias y lecturas adicionales

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (orígenes de la madurez del proceso de software).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (pensamiento de capacidad, no de nivel de madurez, para la entrega).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defense, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore y Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, «Maturity Model» (bliki), sobre sus usos y abusos.
