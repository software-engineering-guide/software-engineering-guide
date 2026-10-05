# 1.7 Estándares de ingeniería y excepciones

## Visión general y motivación

Un **estándar de ingeniería** es una regla documentada y consensuada sobre cómo se realiza el trabajo. Pensemos en ejemplos como «todos los servicios deben exponer un punto de verificación de salud» o «todas las páginas web públicas deben cumplir con las **[Pautas de Accesibilidad para el Contenido Web (WCAG)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) en su versión 2.2, nivel AA»). Un estándar no es una sugerencia ni una simple convención: es un compromiso institucional que la organización se impone a sí misma, idealmente verificable. Este capítulo abarca el ciclo de vida completo de los estándares: cómo una gran organización los **redacta, publica, adopta, hace cumplir y hace evolucionar**, y, con igual importancia, cómo gestiona los casos que legítimamente se sitúan fuera de ellos a través de un **proceso de excepciones** regulado (también llamado **proceso de exenciones**) : un permiso documentado y limitado en el tiempo para desviarse de un estándar por un motivo expuesto.

La motivación es clara: a escala, las normas informales dejan de funcionar. Cuando cinco ingenieros comparten una misma sala, «así hacemos las cosas aquí» se transmite por la conversación y por ósmosis. Cuando cinco mil ingenieros se reparten en decenas de equipos, tres zonas horarias y una década de rotación de personal, ese conocimiento tácito se fragmenta en cientos de hábitos locales incompatibles. Los estándares son la forma de escribir una lección aprendida a duras penas una sola vez, para que cada equipo la herede en lugar de reaprenderla a través de su propia incidencia. Reducen la [carga cognitiva](https://en.wikipedia.org/wiki/Cognitive_load), hacen que las [revisiones de código](https://en.wikipedia.org/wiki/Code_review) se centren en la sustancia y no en el estilo, permiten a las personas moverse entre equipos y ofrecen a auditores y reguladores algo concreto sobre lo que evaluar.

Pero los estándares tienen su propio modo de fracaso: la rigidez. Un estándar que no admite excepciones bloqueará, antes o después, trabajo legítimo: un prototipo exploratorio, una restricción de un proveedor, un caso genuinamente novedoso que los autores jamás contemplaron. Entonces los equipos o bien se paralizan, o bien (y es peor) ignoran el estándar en silencio, lo que corroe la credibilidad de *todos* los estándares. El remedio es aquel viejo aforismo: «la excepción confirma la regla». Un proceso de excepciones visible y riguroso es lo que mantiene los estándares a la vez creíbles y humanos. Este capítulo se apoya en los modelos de toma de decisiones y gobernanza (capítulo 1.5) y en los registros de decisión (capítulo 1.6), y alimenta directamente los estándares de codificación y estilo (capítulo 2.1), las listas de verificación (capítulo 12.2) y las plantillas (capítulo 12.3).

## Principios fundamentales

- **Un estándar enuncia un resultado y expone su razón de ser.** Regla más justificación; sin el *porqué*, nadie puede juzgar cuándo aplica de verdad.
- **Si no se puede verificar, aún no es un estándar.** Preferir enunciados comprobables sobre aspiraciones.
- **Los estándares son documentos vivos.** Están versionados, tienen dueño y fecha de revisión; no se graban en piedra y se abandonan.
- **Automatiza la ejecución donde se pueda; reserva la revisión humana para el juicio.** Las máquinas verifican lo mecánico; las personas, lo significativo.
- **Las desviaciones se esperan, no se estigmatizan, pero deben ser visibles.** Una exención honesta vale siempre más que el incumplimiento silencioso.
- **Limita en el tiempo toda excepción.** Una excepción permanente es un defecto del estándar: hay que identificarlo y corregir el estándar.
- **Palabras y ejemplos antes que jerga y mandatos.** La gente sigue los estándares que comprende y de los que puede tomar ejemplo.

## Recomendaciones

### Redacta estándares claros, comprobables y justificados

Un buen estándar es un documento breve, autosuficiente y de estructura predecible, de modo que el lector sepa dónde buscar. Adopta una **plantilla de estándar** (capítulo 12.3) y utilízala de forma uniforme. Las secciones esenciales incluyen:

- **Título e identificador:** un nombre estable y un número de referencia para su citación.
- **Estado:** borrador, activo, sustituido o retirado, con fecha.
- **La regla:** formulada como resultado, de manera clara e inequívoca, usando «debe», «recomendado» y «puede» con intención, según las convenciones de palabras clave para requisitos del **RFC 2119**.
- **Justificación:** *por qué* existe esta regla; el coste o riesgo que previene.
- **Ejemplos:** uno conforme y otro no conforme; lo concreto supera a lo abstracto.
- **Cómo se verifica:** la prueba automática, la regla del linter o el paso de revisión que la comprueba.
- **Dueño y fecha de revisión:** quién lo mantiene y cuándo se revisa de nuevo.

La justificación y el campo «cómo se verifica» son lo que distinguen un estándar real de un mero deseo. Si no puedes explicar por qué existe una regla, pregunta si debería existir. Si no puedes explicar cómo se verifica el cumplimiento, la regla se aplicará de forma inconsistente y generará resentimiento.

### Asocia a cada estándar una lista de verificación de buenas prácticas

Los estándares definen el destino. Una **lista de verificación de buenas prácticas**, una breve enumeración ordenada de pasos concretos o ítems a confirmar, ayuda a llegar a él y permite que cada persona verifique su cumplimiento antes de la revisión. Los manuales de ingeniería del sector público recurren con frecuencia a este patrón. **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** y **Digital Health and Care Wales (DHCW)** publican estándares de ingeniería acompañados de listas prácticas, y el **Servicio Digital del Gobierno del Reino Unido (GDS, por sus siglas en inglés)** asocia su Estándar de Servicio y su Código de Práctica Tecnológica a la guía accionable del Manual de Servicios. La lista es el estándar puesto en uso: «¿Has incluido una auditoría de accesibilidad? ¿Has probado con un lector de pantalla? ¿Has cubierto la navegación solo con teclado?». Véase el capítulo 12.2 para el patrón de listas de verificación en su conjunto.

### Publica los estándares donde la gente ya trabaja y mantén su visibilidad

Almacena los estándares en un sistema de [control de versiones](https://en.wikipedia.org/wiki/Version_control) (un repositorio de código fuente), en formato Markdown, renderizados en un sitio interno de búsqueda, de modo que obtengan historial, revisión mediante *pull requests* y diffs sin esfuerzo, el mismo argumento que se aplica a los registros de decisión (capítulo 1.6). Un único catálogo, una única plantilla, una única barra de búsqueda. La visibilidad importa tanto como el almacenamiento. Enlaza el estándar pertinente desde la plantilla de *pull request*, desde el mensaje de error del linter y desde el andamiaje del servicio, para que la regla correcta aparezca en el momento del trabajo y no en una carpeta que nadie visita.

### Ejecuta mediante automatización primero, revisión humana después

Hay dos formas de hacer cumplir un estándar y las organizaciones maduras las emplean ambas de forma deliberada:

- **Ejecución automatizada:** [linters](https://en.wikipedia.org/wiki/Lint_(software)), formateadores, [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis), política como código (por ejemplo, **Open Policy Agent, OPA**), controles de [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI) y **funciones de idoneidad arquitectónica** (pruebas automáticas que afirman que una propiedad de diseño sigue cumpliéndose). La automatización es constante, incansable, inmediata e irrefutable, lo que la hace ideal para la mayoría mecánica de los estándares (formateo, nomenclatura, reglas de dependencias, metadatos obligatorios).
- **Revisión humana:** revisión de código, comités de revisión arquitectónica y de seguridad, reservados para lo que las máquinas no pueden juzgar: si una abstracción es sólida, si una compensación es prudente, si la *intención* de un estándar se cumple aunque su letra resulte incómoda.

La regla de oro: **automatiza lo comprobable y dedica la atención humana, escasa por naturaleza, al juicio.** Cada estándar que se traslada de la revisión al CI libera a los revisadores para que se concentren en el pensamiento que solo ellos pueden hacer.

### Gestiona las desviaciones con un proceso documentado de excepciones o exenciones

Ningún estándar encaja en todo caso, así que diseña la salida de emergencia a propósito. Un buen proceso de excepciones especifica:

- **Quién puede conceder una exención:** una autoridad nombrada y responsable, proporcional al riesgo (un líder técnico para una desviación de estilo de bajo impacto; un comité de arquitectura o de seguridad para una exención de un control de seguridad). Esto se vincula directamente con el modelo de gobernanza del capítulo 1.5.
- **Qué debe registrarse:** el estándar del que se desvía, el motivo concreto, el alcance, los controles compensatorios o mitigaciones y el riesgo aceptado. Regístralo como un registro de decisión (capítulo 1.6) para preservar la justificación.
- **Un vencimiento obligatorio:** cada exención es **limitada en el tiempo** con una fecha de finalización explícita. Esta es la regla más importante: impide que una excepción temporal se convierta, en silencio, en política permanente.
- **Revisión periódica:** un propietario revisa las exenciones abiertas en un ciclo regular y las renueva con una justificación fresca, las cierra cuando el trabajo ya cumple, o, si la misma excepción se repite con frecuencia, la interpreta como evidencia de que el *estándar mismo* está mal calibrado y lo revisa.

Este último punto es el corazón de «la excepción confirma la regla». Una corriente constante de exenciones contra un mismo estándar no es un fracaso de disciplina. Es un dato. Indica que el estándar está mal calibrado, y la solución es evolucionar el estándar, no seguir concediendo excepciones.

### Trata los estándares como documentos vivos con una propiedad clara

Asigna a cada estándar un **propietario** (un rol, no solo una persona) responsable de mantenerlo actualizado, y un **ciclo de revisión** (al menos anual). Ofrece una vía ligera para que cualquiera proponga un cambio mediante un *pull request* o un **RFC (*Request for Comments*, solicitud de comentarios)**, una propuesta escrita que se circula para recopilar feedback antes de su adopción. Versiona los estándares, déjalos obsoletos de forma explícita y anuncia los cambios. Un catálogo de estándares que nunca se revisa degenera en folclore: se cita de forma selectiva y se confía en él muy poco.

## Compromisos: ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| **Muchos estándares detallados** | Consistencia, onboarding ágil, listos para auditoría | Rigidez; carga de mantenimiento; pueden adelantarse a la práctica |
| **Pocos estándares de alto nivel** | Flexibilidad; bajo mantenimiento | Inconsistencia; más debates repetidos por equipo |
| **Ejecución automatizada** | Constante, inmediata, incansable, escalable | Coste inicial; falsos positivos; ciega ante la intención |
| **Ejecución por revisión humana** | Juzga la intención y el matiz | Lenta, inconsistente, cuello de botella a escala |
| **Rigor sin excepciones** | Mensaje simple; nada que manipular | Bloquea trabajo legítimo; impulsa el incumplimiento silencioso |
| **Proceso de excepciones regulado** | Mantiene los estándares creíbles y humanos | Exige gobernanza, registros y seguimiento |

La tensión central es **consistencia frente a flexibilidad**. Un estándar existe para eliminar la variación; un proceso de excepciones existe para admitir la variación que es genuinamente justificada. Inclinar la balanza demasiado hacia la rigidez y la gente rodeará los estándares. Inclinarse demasiado hacia la laxitud y los estándares no significarán nada. El proceso de excepciones es la válvula de alivio que permite mantener una postura firme *y* ser honesto con la realidad.

## Preguntas para debatir con tu equipo

1. **¿Cuál es el número adecuado de estándares para tu escala, y están los tuyos derivando hacia la rigidez o hacia la inconsistencia?** El catálogo en sí es una compensación: muchos estándares detallados compran consistencia, onboarding ágil y preparación para auditorías, a costa de rigidez y carga de mantenimiento; pocos estándares de alto nivel mantienen la flexibilidad, pero dejan que cada equipo vuelva a debatir las mismas cuestiones. Para una gran empresa o un organismo gubernamental, el tamaño adecuado depende de cuánta variación puedas tolerar genuinamente frente a cuánto necesitan tus auditores y tu proceso de incorporación fijado. Aporta evidencia: cuántos estándares activos tienes, cuántos se revisaron el año pasado y con qué frecuencia los equipos vuelven a debatir lo que un estándar habría resuelto. Un catálogo que se adelanta a la práctica se convierte en folclore, y uno demasiado delgado traslada el coste a cada equipo. Decide deliberadamente qué merece un estándar y poda los que ya no justifican su existencia.

2. **¿Dónde se cumple la letra de un estándar automáticamente mientras su intención se viola en silencio, y cómo lo detectarás?** La automatización es constante, incansable y ciega ante la intención, lo que significa que un linter o una comprobación de política puede quedar en verde mientras el objetivo real (una abstracción sólida, una compensación prudente, una página genuinamente accesible) se pierde. La regla de oro es automatizar lo comprobable y dedicar la revisión humana al juicio, y lo difícil es acordar qué estándares tienen una intención que ninguna puerta de CI puede afirmar. Aporta ejemplos: estándares que la gente cumple a la letra mientras se anula su propósito, como un punto de verificación de salud que reporta «saludable» mientras el servicio está roto, o código que pasa el formateador pero que oscurece el significado. En entornos regulados, la intención importa más en los controles de seguridad y seguridad, donde una casilla verde puede ocultar un riesgo real. Decide qué estándares conservan un revisor humano específicamente para juzgar la intención, y redacta esos estándares en torno al resultado, para que tanto la máquina como el revisor apunten al mismo blanco.

3. **¿Quién es responsable del ciclo de retroalimentación de exenciones a estándares, y en qué momento una excepción recurrente te obliga a cambiar la regla?** Una corriente constante de exenciones contra un mismo estándar es un dato, no una falta de disciplina, y la señal se desperdicia si nadie es responsable de leerla y actuar. La contraparte es que revisar un estándar es trabajo real, por lo que resulta más fácil seguir convalidando exenciones que corregir la regla mal calibrada que hay debajo. Aporta los números: qué estándares generan más excepciones, si las exenciones están realmente limitadas en el tiempo y se revisan en un ciclo, y cuántas se han convertido en permanentes en silencio. En estándares críticos para la seguridad de personas y la seguridad informática en empresas y organismos gubernamentales, una exención debe registrar controles compensatorios, una mitigación, el riesgo aceptado y un vencimiento firme; de lo contrario, una desviación temporal se convierte en política no documentada que saldrá a la luz en la próxima auditoría. Asigna un propietario para revisar las exenciones abiertas, establece un umbral en el que las excepciones repetidas disparen una revisión del estándar y trata una excepción permanente como un defecto del estándar que hay que corregir.

4. **¿El estándar correcto aparece en el momento del trabajo o vive en una carpeta que nadie abre?** Un estándar que nadie encuentra se ejecuta por azar, y a escala la mayoría del incumplimiento no es desafío sino ignorancia: un ingeniero nunca supo que la regla existía o no pudo localizarla cuando importaba. La contraparte es el esfuerzo, pues incorporar un estándar en la plantilla de *pull request*, en el mensaje de error del linter y en el andamiaje del servicio implica trabajo real de integración que un único sitio central no cubre. Aporta evidencia sobre la visibilidad: cómo encuentran los ingenieros los estándares hoy en día, si un recién incorporado puede localizar en menos de un minuto la norma de accesibilidad o de seguridad que rige su tarea, y con qué frecuencia los revisadores citan un estándar que el autor simplemente no había visto. Para una gran empresa o un organismo gubernamental, los auditores preguntan cada vez más no solo si un estándar existe, sino si se comunicó y estaba accesible en el momento de la decisión; por tanto, trata la visibilidad como parte del estándar, no como un añadido, y mide si la gente puede acceder a la regla cuando la necesita.

5. **¿Quién es propietario de cada estándar activo, cuándo se revisó por última vez y cómo detectarías los que se han degradado en folclore sin que nadie lo notara?** Los estándares se deterioran en silencio: una regla escrita hace tres años para un marco tecnológico que ya no usas sigue en el catálogo, citada selectivamente y confiada muy poco, arrastrando la credibilidad de los estándares que siguen siendo correctos. Para una gran organización, el coste de la propiedad es el propio ciclo de revisión, que se percibe como sobrecarga hasta que una incidencia o una auditoría expone un estándar que ya no coincide con la realidad. Aporta los números al debate: cuántos estándares tienen un propietario nombrado (un rol, no una persona que ya se fue), cuántos se revisaron el año pasado, cuántos están formalmente obsoletos frente a simplemente desactualizados, y cuáles se citan más y cuáles menos. En entornos empresariales y gubernamentales, un auditor espera que cada estándar esté versionado, fechado y demostrablemente vigente; por tanto, acordad un ciclo de revisión mínimo, asignad un propietario responsable a cada estándar y retirad los que ya no justifican su existencia antes de que socaven la confianza en el resto.

6. **¿La autoridad para conceder una exención es realmente proporcional al riesgo del estándar exentado?** Una desviación de estilo y una desviación de un control de seguridad no son la misma decisión, y muchos organismos o bien derivan ambas a un comité de alto nivel (lo que paraliza el trabajo legítimo) o bien las dejan pasar por un solo líder técnico (lo que permite que se acepte un riesgo serio quien no tiene mandato para aceptarlo). La tensión es entre velocidad y responsabilidad: demasiada fricción de aprobación impulsa el incumplimiento silencioso, y muy poca permite que desviaciones graves se resuelvan en un hilo de chat. Aporta un mapa de tus estándares vinculados a sus autoridades de aprobación, junto con una muestra de exenciones concedidas recientemente, y comprueba si alguien exentó un control crítico de seguridad o de integridad sin el comité correspondiente, sin un control compensatorio, sin mitigación y sin un registro de riesgo aceptado. En el ámbito empresarial y gubernamental, esto es una cuestión de [segregación de funciones](https://en.wikipedia.org/wiki/Separation_of_duties) que los reguladores examinan directamente; por tanto, vincula cada clase de estándar a una autoridad nombrada proporcional a su riesgo y asegúrate de que la persona que acepta un riesgo es genuinamente responsable de sus consecuencias.

## Perspectiva por sector

**Startup.** Mantén el catálogo mínimo: escribe solo las pocas reglas cuya ausencia te perjudicaría de verdad, como la configuración del formateador, el requisito del punto de verificación de salud y «todas las páginas públicas deben ser navegables con teclado», y ejecuta cada una con un linter o un control de CI en lugar de una reunión de revisión. Omite el comité de exenciones: un *TODO* fechado en el código y una nota de una línea en el *pull request* es una exención limitada en el tiempo perfectamente válida a esta escala. Tu recurso más escaso es la atención de ingeniería, así que resiste la tentación de redactar estándares para problemas que aún no tienes.

**Pequeña empresa.** Sin un propietario de estándares dedicado y con un presupuesto ajustado, compra tus estándares en lugar de construirlos: adopta líneas de referencia publicadas como el Estándar de Servicio del GDS británico, las directrices de seguridad de OWASP o las reglas de lint recomendadas por tu marco, y aprovecha los controles ya incorporados en tus herramientas y tu CI alojado. Conserva una página breve de reglas locales para las pocas cosas genuinamente específicas de tu organización. Quien dirija la ingeniería concede y registra las excepciones en la pizarra de tareas, con fecha de vencimiento, de modo que incluso un proceso ligero mantenga la honestidad.

**Gran empresa.** La tarea es la gobernanza entre muchos equipos: un único catálogo, una única plantilla, justificación y ejemplos para cada estándar, y política como código que detenga la tubería de CI para la mayoría mecánica. Pon en marcha un proceso de exenciones cuya autoridad de aprobación sea proporcional al riesgo, limita en el tiempo cada excepción, revisa las exenciones abiertas en un ciclo regular y extrae de las exenciones recurrentes la señal de que un estándar necesita cambiar. Mide el porcentaje de estándares ejecutados de forma automática y el volumen y la antigüedad de las exenciones abiertas, y reporta ambos indicadores a la función de gobernanza, para que los estándares sigan siendo un sistema gestionado y no un cementerio.

**Organismo gubernamental.** Publica tus estándares de ingeniería de forma abierta, en la tradición de DHCW y GDS, y asocia cada uno a una lista de verificación que los equipos completan antes de una evaluación de servicio, de modo que el cumplimiento sea visible para el público y para los organismos de supervisión. Designa un responsable senior nombrado como autoridad para las exenciones de consecuencias relevantes, y exige que cada excepción registre el criterio específico, el control compensatorio o la mitigación interina, un plan de remediación y un vencimiento firme. Las normas de contratación y de transparencia convierten tus estándares y tus desviaciones en parte del registro público; por tanto, trata la auditabilidad y la trazabilidad como requisitos de diseño desde el principio.

## Ejemplos

**Startup.** Una *startup* de siete personas mantiene exactamente tres estándares escritos (una configuración de formateador compartida, un requisito de punto de verificación de salud y «todas las páginas públicas deben ser navegables con teclado»), cada uno ejecutado por un linter o un control de CI en lugar de una reunión de revisión. Cuando una ingeniera necesita desplegar un prototipo provisional que incumple el estándar de verificación de salud, no hay comité de exenciones: deja un *TODO* fechado en el código y una nota de una línea en el *pull request* indicando el motivo y cuándo lo corregirá. Esa es una exención limitada en el tiempo a escala de *startup*: honesta y visible, sin sobrecarga de proceso. Las tres comprobaciones se pagan solas al mantener la revisión de código centrada en la sustancia y no en el estilo.

**Gran empresa.** Un banco global mantiene un manual interno de ingeniería con unos cuarenta estándares activos, cada uno en una misma plantilla, con justificación, ejemplos y una lista de verificación de buenas prácticas vinculada. Aproximadamente el 70 % se ejecuta de forma automática: formateo, política de dependencias, metadatos de servicio obligatorios y controles de seguridad codificados como política como código que detiene la tubería de CI. Un equipo de pagos necesita desplegar sobre una base de datos que aún no soporta un cifrado mandatado. En lugar de bloquear el despliegue, presenta una exención que nombra el estándar, el control compensatorio (cifrado a nivel de [aplicación](https://en.wikipedia.org/wiki/Encryption)) y un vencimiento de noventa días. El comité de seguridad la concede y la registra. Noventa días después, la revisión revela que la plataforma ya soporta la función de forma nativa, y la exención se cierra. El estándar se mantuvo, el trabajo se desplegó y la desviación es plenamente rastreable para la próxima auditoría.

**Organismo gubernamental.** Una agencia nacional de salud, inspirada en el enfoque de DHCW y GDS, publica sus estándares de ingeniería de forma abierta, cada uno acompañado de una lista de verificación que los equipos completan antes de una evaluación de servicio. La accesibilidad a WCAG 2.2 nivel AA es un estándar firme, ejecutado por una auditoría automatizada en CI más una evaluación manual. Un sistema clínico legado no puede cumplir inmediatamente un criterio de accesibilidad sin arriesgar funcionalidad crítica para la seguridad del paciente. El equipo solicita una exención limitada en el tiempo. Un responsable senior nombrado la concede y registra el criterio específico, la mitigación interina (una línea telefónica de asistencia), el plan de remediación y un vencimiento de seis meses, generando exactamente la evidencia trazable y revisable que los organismos de supervisión exigen (capítulos 4.6 y 10.4).

## Caso de negocio: motivaciones, retorno de la inversión y coste total de propiedad

Un estándar cuesta el tiempo de redactarlo, automatizar su verificación y mantenerlo. El retorno se paga cada vez que la comprobación se ejecuta y cada vez que un ingeniero no tiene que detenerse a debatir una cuestión ya resuelta. Los estándares convierten un coste de decisión recurrente y distribuido en un coste de redacción de una sola vez, la misma economía que los registros de decisión (capítulo 1.6), amplificada porque un estándar gobierna miles de instancias futuras, no una elección pasada.

En cuanto al **coste total de propiedad (TCO)** (el coste completo de construir, operar y mantener un sistema a lo largo de su vida útil) , los estándares reducen los mayores conceptos del presupuesto: la incorporación de personal (los nuevos heredan consistencia en lugar de tener que descifrarla), el mantenimiento (el código uniforme es más barato de modificar) y la certificación (las auditorías son más baratas cuando el cumplimiento es verificable por máquina y las desviaciones ya están documentadas). El proceso de excepciones protege ese retorno de su principal amenaza: que los estándares se degraduen en folclore ignorado. Un proceso de exenciones creíble mantiene los estándares dignos de confianza, y los estándares dignos de confianza son los que la gente sigue de verdad. El coste de saltarse todo esto no aparece en ningún panel de control. Se manifiesta como incorporaciones lentas, calidad inconsistente y hallazgos de auditoría, y se compounda con cada equipo nuevo y cada salida.

## Antipatrrones y trampas

- **Reglas sin justificación:** un estándar que nadie comprende es un estándar que nadie aplica bien ni cuestiona con honestidad.
- **Estándares aspiracionales e incontrolables:** «el código debe ser mantenible» es un valor, no un estándar; no puede ejecutarse ni debatirse.
- **Sin proceso de excepciones:** obliga a una falsa elección entre bloquear el trabajo legítimo y tolerar el incumplimiento silencioso.
- **Excepciones permanentes:** exenciones sin vencimiento que se convierten, en silencio, en la política real y no documentada.
- **Exenciones sin registro:** desviaciones concedidas en un pasillo o en un hilo de chat, invisibles para la próxima auditoría y para el próximo ingeniero.
- **Ignorar la señal:** conceder la misma excepción una y otra vez en lugar de leerla como prueba de que el estándar necesita cambiar.
- **Ejecución por insistencia:** depender de que los revisadores detecten lo que un linter debería, desperdiciando juicio en lo mecánico.
- **Cementerio de estándares:** un catálogo redactado una vez, sin propietario, nunca revisado, citado selectivamente y de poca confianza.
- **Barrera jargónica:** estándares escritos para sus autores y no para sus lectores, sin ejemplos de los que tomar modelo.

## Modelo de madurez

- **Nivel 1 (Iniciación):** Los estándares son conocimiento tribal en la mente de los ingenieros seniors, aplicados de forma reactiva. La ejecución es una insistencia ad hoc en la revisión de código; las desviaciones son invisibles; «así lo hacemos aquí» varía según el equipo y según quién revise el cambio.
- **Nivel 2 (Desarrollo):** Algunos estándares están documentados, pero en formatos incongruentes y en ubicaciones dispersas, y su adopción varía enormemente de un equipo a otro. La ejecución es mayoritariamente manual. Las excepciones ocurren de forma informal, sin registros ni fechas de vencimiento.
- **Nivel 3 (Estandarización):** Un único catálogo, una única plantilla, justificación y ejemplos para cada estándar y listas de verificación de buenas prácticas, aplicados de forma consistente entre equipos. Ejecución automatizada para la mayoría mecánica. Un proceso de excepciones documentado con aprobadores nombrados, justificación registrada y exenciones con vencimiento.
- **Nivel 4 (Gestión):** El sistema de estándares se mide contra líneas de referencia. Se rastrea el porcentaje de estándares ejecutados de forma automática frente a los revisados por humanos, el volumen de exenciones por estándar, el tiempo de cierre y cuántas exenciones vencieron sin cerrarse, y se reporta todo a la función de gobernanza. La autoridad de aprobación es proporcional al riesgo y auditada; el ciclo de revisión y el vencimiento se ejecutan con base en evidencia, no en buena voluntad; un estándar cuya tasa de exenciones supera un umbral acordado se marca para revisión.
- **Nivel 5 (Orquestación):** Los estándares se presentan en el momento del trabajo y se ejecutan mediante política como código y funciones de idoneidad. Las exenciones se extraen como señal para que las excepciones recurrentes impulsen continuamente la evolución de los estándares, y el catálogo se reequilibra a medida que la práctica cambia. Los estándares, las listas de verificación y las exenciones forman un sistema vivo y adaptativo integrado en la incorporación, la entrega y la auditoría.

## Ideas para el debate

1. ¿Cuáles de tus estándares puedes formular con una regla comprobable *y* una justificación clara, y cuáles son, en realidad, simples aspiraciones?
2. ¿Qué porcentaje de tus estándares se ejecutan de forma automática frente a los que dependen de que un revisor los note? ¿Qué se necesitaría para trasladar diez más a la CI?
3. ¿Dónde ocurren las desviaciones hoy en día, y lo sabrías siquiera? ¿Están registradas y con vencimiento, o son silenciosas?
4. ¿Quién está autorizado a conceder una exención contra tu estándar más crítico en materia de seguridad de personas o de seguridad informática, y es esa autoridad proporcional al riesgo?
5. Mira tu estándar con más exenciones. ¿Es un problema de disciplina, o es que el estándar está simplemente mal?
6. ¿Cuándo se revisó por última vez cada estándar activo y quién es su propietario? ¿Cuáles se han convertido en folclore sin que nadie lo notara?

## Conclusiones clave

- Un estándar de ingeniería es una **regla formulada como resultado, con justificación, ejemplos y un método de verificación**: si no se puede comprobar, aún no es un estándar.
- Asocia a cada estándar una **lista de verificación de buenas prácticas** para que la gente pueda autoverificarse, siguiendo el patrón de los manuales del sector público (NHS Wales / DHCW, GDS del Reino Unido).
- Almacena los estándares en **control de versiones**, manténlos **vivos** con propietarios nombrados y fechas de revisión, y preséntalos en el momento del trabajo.
- **Automatiza lo comprobable** con linters, política como código y funciones de idoneidad; reserva la **revisión humana** para el juicio.
- Gestiona las desviaciones con un **proceso de excepciones documentado y con vencimiento**: aprobador nombrado, justificación registrada, vencimiento obligatorio, revisión periódica.
- Una excepción recurrente es una **señal para corregir el estándar**, no solo para seguir concediendo exenciones: «la excepción confirma la regla». Véanse los capítulos 1.5 (gobernanza), 1.6 (registros de decisión), 2.1 (estándares de codificación), 12.2 (listas de verificación) y 12.3 (plantillas).

## Referencias y lecturas adicionales

- Servicio Digital del Gobierno del Reino Unido (GDS), *Government Service Standard*, *Technology Code of Practice* y *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* y directrices de ingeniería.
- Digital Health and Care Wales (DHCW) / NHS Wales, estándares de ingeniería publicados y listas de verificación de buenas prácticas.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons y Patrick Kua, *Building Evolutionary Architectures* (funciones de idoneidad como gobernanza automatizada).
- Torin Sandall et al., documentación de *Open Policy Agent* (política como código).
- GitLab, *The GitLab Handbook*: un ejemplo público de estándares organizacionales vivos y versionados.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): estándares, legibilidad y ejecución automatizada a escala.
- Atul Gawande, *The Checklist Manifesto*: el caso de las listas de verificación como práctica profesional.

