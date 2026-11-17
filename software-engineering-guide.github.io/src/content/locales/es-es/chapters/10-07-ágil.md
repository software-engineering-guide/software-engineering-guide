# 10.7 Ágil

## Presentación y motivación

[Ágil](https://en.wikipedia.org/wiki/Agile_software_development) es una mentalidad para entregar software (y valor) iterativa e incrementalmente, y en colaboración cercana con la gente que lo usará. Codificado en el *Manifiesto para el Desarrollo Ágil de Software* de 2001, se entiende mejor no como un proceso sino como un conjunto de **valores y principios**: priorizar a los individuos e interacciones, el software funcional, la colaboración con el cliente, y la respuesta al cambio, sobre los valores predeterminados pesados en planes, contratos, y documentación que vinieron antes. Los marcos como [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), y la Programación Extrema ([XP](https://en.wikipedia.org/wiki/Extreme_programming)) son *implementaciones* de esa mentalidad. Son puntos de partida útiles, pero no la mentalidad misma. Este capítulo complementa el capítulo 1.4 (formas de trabajar, que examina los métodos ampliamente) profundizando específicamente en Ágil.

Ágil está impulsado por la misma fuerza que anima los canales de descubrimiento y entrega (capítulos 11.1–11.2): los requisitos de software se *descubren*, no se conocen completamente por adelantado, y el mundo cambia más rápido de lo que un plan largo puede absorber. La entrega de gran explosión, que planifica todo primero, produce repetidamente sistemas que llegan tarde, exceden el presupuesto, y, lo peor de todo, están equivocados, porque todo el aprendizaje llega al final, cuando es más costoso actuar sobre él. La apuesta central de Ágil es simple: los ciclos cortos de construir software real y funcional y obtener retroalimentación real superan a los ciclos largos de especulación. Bien hecho, reduce el riesgo continuamente en lugar de aplazarlo.

Para los equipos grandes, la empresa, y el gobierno, Ágil es tanto poderoso como frecuentemente destrozado. Las empresas lo adoptan a través de cientos de equipos y a menudo lo reducen a ritual («ahora hacemos reuniones diarias») sin cambiar cómo se toman las decisiones o cómo se mide el valor. El gobierno ha adoptado Ágil deliberadamente, porque la entrega iterativa y centrada en el usuario demostrablemente reduce el riesgo de los grandes programas públicos: el U.S. Digital Service y su *Digital Services Playbook*, el Government Digital Service del Reino Unido y su Service Standard, y las reformas de contratación pública ágil todos surgieron en parte en respuesta a fallos de [cascada](https://en.wikipedia.org/wiki/Waterfall_model) de alto perfil. El premio es real. También lo es el modo de fallo de «ágil solo de nombre».

## Principios fundamentales

- **Valora los cuatro valores del Manifiesto** (la gente, el software funcional, la colaboración, y la capacidad de respuesta) sobre los artefactos de proceso.
- **Entrega software funcional frecuentemente** en incrementos pequeños; el software funcional es la medida primaria del progreso.
- **Da la bienvenida al cambio**, incluso tardío; la adaptabilidad es una función, no un fallo.
- **Construye en torno a equipos motivados, empoderados, y autoorganizados.**
- **Colabora continuamente con los usuarios y partes interesadas.**
- **Reflexiona y mejora** en una cadencia regular.
- **Sostén un ritmo humano** y la excelencia técnica: la velocidad sin oficio colapsa.

## Recomendaciones

### Ancla en los valores y principios, no en las ceremonias

La recomendación ágil más importante es liderar con el *por qué*. Un equipo que sostiene una reunión diaria, una revisión de sprint, y una retrospectiva, pero todavía se compromete con un alcance fijo en una fecha fija, oculta malas noticias, y nunca cambia el plan, no es ágil. Es cascada con reuniones. Usa los doce principios como una lista de comprobación para la agilidad genuina. ¿Estás entregando software funcional a menudo? ¿Puedes dar la bienvenida a un cambio en la próxima iteración? ¿El equipo decide *cómo* hacer el trabajo? ¿Está el cliente realmente en el ciclo? Si las ceremonias no producen esos resultados, arregla los resultados, no las ceremonias.

### Elige un marco como punto de partida, no una religión

Elige un marco que se ajuste al trabajo y adáptalo:

- **Scrum:** sprints con límite de tiempo, un atraso priorizado, y roles definidos (dueño de producto, scrum master, desarrolladores). Bueno para la entrega de funciones con un dueño de producto claro; débil cuando el trabajo está altamente impulsado por interrupciones.
- **Kanban:** flujo continuo con límites explícitos de trabajo en progreso y un sistema de extracción. Bueno para el soporte, las operaciones, y la llegada impredecible (y fundamentado directamente en la teoría de flujo y colas, véanse los capítulos 11.2, 11.3). Limitar el TEP acorta el tiempo de espera ([Ley de Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Programación Extrema (XP):** prácticas de ingeniería incluyendo el [desarrollo guiado por pruebas](https://en.wikipedia.org/wiki/Test-driven_development), la [programación en pareja](https://en.wikipedia.org/wiki/Pair_programming), la [integración continua](https://en.wikipedia.org/wiki/Continuous_integration), la refactorización, los lanzamientos pequeños. La columna vertebral técnica que hace sostenible a cualquier marco.
- **Scrumban** y mezclas: combinaciones pragmáticas hacia las que convergen muchos equipos maduros.

Los marcos son andamiaje. Mantén lo que ayuda, descarta lo que no, y nunca dejes que «el marco lo dice» anule «los principios dicen por qué».


### Insiste en la excelencia técnica

Ágil sin disciplina de ingeniería se degrada rápidamente en la producción rápida de código inmantenible, el «scrum oscuro», donde los equipos hacen sprint hacia un pozo de alquitrán de defectos y [deuda técnica](https://en.wikipedia.org/wiki/Technical_debt). Las prácticas de XP no son extras opcionales. La integración continua (capítulo 8.1), las pruebas automatizadas (capítulo 2.4), la refactorización, el desarrollo basado en tronco (capítulo 2.6), y el diseño limpio (capítulo 2.2) son lo que permite a un equipo seguir cambiando el software barato, que es toda la premisa de la agilidad. El ritmo sostenible importa por la misma razón: los equipos agotados no pueden sostener la calidad o la capacidad de respuesta.

### Escala con cuidado, y prefiere desescalar

Los marcos de escalado, como SAFe (el Marco Ágil Escalado), LeSS, Nexus, y Scrum@Scale, coordinan a muchos equipos hacia metas compartidas. Pueden ayudar, pero llevan una advertencia (haciendo eco del capítulo 1.4): los marcos de escalado pesados a menudo reintroducen exactamente la sobrecarga de mando y control, pesada en planes, que Ágil se suponía que debía eliminar. Antes de adoptar un marco grande, intenta *desescalar*. Organízate en torno a equipos independientes y alineados con flujo con propiedad clara y dependencias mínimas entre equipos (capítulo 1.2), para que necesites menos maquinaria de coordinación en primer lugar. Donde la coordinación sea genuinamente requerida, añade la estructura más ligera que funcione, y conéctala a resultados (OKR, objetivos y resultados clave, capítulo 11.1), no a producción.

### Haz real la agilidad en la empresa y el gobierno

La entrega adaptativa y las restricciones institucionales pueden coexistir, pero requiere diseño deliberado:

- **Gobernanza híbrida:** un núcleo de entrega adaptativa dentro de una envoltura de financiación/cumplimiento predictiva (capítulo 10.6), para que la iteración satisfaga en lugar de luchar contra la supervisión.
- **Contratación pública ágil:** contratos modulares y basados en resultados e incrementos más cortos en lugar de un único megacontrato de alcance fijo; aquí es donde el Ágil del sector público más a menudo tiene éxito o falla.
- **Cumplimiento sobre la marcha:** incorpora la auditoría, la accesibilidad (capítulo 5.3), y la seguridad (capítulo 4.1) en el incremento a través de la automatización y las funciones de aptitud (comprobaciones automatizadas que verifican continuamente las propiedades arquitectónicas y de calidad; capítulos 8.5, 1.6), no una puerta tardía.
- **Acceso real de usuario:** lo más difícil e importante. Los equipos necesitan contacto genuino con los ciudadanos o clientes, que las reglas de contratación pública y seguridad a menudo obstruyen.

### Mejora continuamente, y en serio

La retrospectiva es el motor de mejora de Ágil, y no vale nada si no produce ningún cambio. Ejecuta retrospectivas que generen un pequeño número de acciones concretas y con dueño, y realmente complétalas antes de la siguiente. Mide los resultados (¿el cambio movió un resultado clave? véase el capítulo 11.1) y el flujo (¿se están reduciendo los tiempos de espera? véanse los capítulos 11.2, 11.3). No midas la velocidad: es una señal de capacidad que se convierte en una mentira en el momento en que la usas como objetivo de productividad.

## Ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| **Ágil (adaptativo)** | Retroalimentación rápida; absorbe el cambio; valor temprano y continuo | Más difícil fijar alcance/costo por adelantado; exige cliente comprometido y disciplina |
| **Cascada (predictivo)** | Alcance predecible; amigable con contratos/auditoría | Retroalimentación tardía; riesgo de gran explosión; mal ajuste para requisitos inciertos |
| **Scrum** | Cadencia, roles, enfoque; ampliamente comprendido | Sobrecarga de ceremonia; lucha con el trabajo impulsado por interrupciones |
| **Kanban** | Flujo, límites de TEP, flexible; excelente para operaciones | Menos estructura; necesita disciplina para mantener los límites |
| **Escalado pesado (SAFe)** | Coordina a muchos equipos; familiar para las grandes organizaciones | Puede reintroducir el mando y control; pesado en ceremonia |
| **Desescalado / autonomía de equipo** | Menos sobrecarga de coordinación; equipos más rápidos | Requiere bajo acoplamiento y propiedad/plataforma sólida |

La tensión definitoria es **adaptabilidad frente a predictibilidad**, y la mala lectura clásica es que Ágil significa «sin plan». No lo significa. Significa planificar continuamente y comprometerse con *resultados y cadencia* mientras se deja flexionar el *alcance*. La otra trampa recurrente es tratar a Ágil como *solo* proceso (ceremonias) o *solo* ingeniería (XP). Necesita ambos.

## Preguntas para discutir con tu equipo

1. **En tu contexto empresarial o gubernamental, ¿son tus contratos modulares y basados en resultados, o la entrega está encerrada dentro de un único megacontrato de alcance fijo?** La contratación pública ágil es donde la agilidad del sector público más a menudo tiene éxito o falla, porque un único contrato de precio fijo y alcance fijo fuerza la cascada sin importar cómo llamen sus reuniones los equipos de entrega. Los contratos modulares y basados en resultados con incrementos más cortos dejan que el alcance flexione hacia un núcleo valioso dentro de una financiación fija, que es exactamente el patrón detrás de los éxitos modernos del sector público y el antídoto para los fallos de gran explosión pasados. Trae evidencia: mira tus contratos actuales y pregunta si un proveedor recibe pago por software funcional demostrado o por un alcance fijo firmado hace años. La respuesta debería moldear cómo estructuras la próxima contratación mucho más que qué marco adoptan internamente tus equipos. No puedes ser adaptativo en la entrega mientras tu contrato mandata una puesta en marcha distante y de todo o nada.

2. **¿Están la auditoría, la accesibilidad, y la seguridad incorporadas en cada incremento a través de la automatización, o atornilladas como una puerta tardía?** El cumplimiento sobre la marcha es lo que permite que la entrega adaptativa coexista con las restricciones institucionales: incorpora las comprobaciones en el incremento a través de la automatización y las funciones de aptitud en lugar de guardarlas para una carrera previa al lanzamiento. Una puerta de cumplimiento tardía reintroduce el riesgo de gran explosión que Ágil existe para eliminar, porque los problemas costosos aparecen al final cuando son más difíciles de arreglar. Trae evidencia: para tu último incremento, comprueba si la evidencia de accesibilidad, seguridad, y auditoría se verificó automáticamente en el canal o se difirió a una revisión manual antes del lanzamiento. La respuesta debería empujar estas propiedades hacia comprobaciones automatizadas continuas, para que la supervisión se satisfaga con el acto de construir en lugar de con una fase separada. Esto también es lo que mantiene honesto a un programa regulado entre auditorías en lugar de solo en las semanas antes de una.

3. **¿Cómo sabrías si tus equipos están haciendo sprint hacia la deuda técnica, y qué protege el ritmo sostenible bajo presión de lanzamiento?** Ágil sin disciplina de ingeniería se degrada en scrum oscuro, donde los equipos hacen sprint rápido hacia un pozo de alquitrán de defectos y código inmantenible, y los equipos agotados no pueden sostener la calidad o la capacidad de respuesta. Las prácticas de XP (integración continua, pruebas automatizadas, refactorización, desarrollo basado en tronco) son lo que permite a un equipo seguir cambiando el software barato, que es toda la premisa de la agilidad, así que no son extras opcionales para intercambiar cuando se avecina una fecha. Trae evidencia: rastrea si los tiempos de espera se están reduciendo o creciendo, si las tasas de defectos están subiendo, y si el equipo está silenciosamente trabajando más horas para cumplir cada sprint. La respuesta debería hacer innegociables la excelencia técnica y el ritmo humano, porque la velocidad comprada sacrificando el oficio colapsa en unas pocas iteraciones. Mide el flujo y los resultados, nunca la velocidad como objetivo, porque en el momento en que conviertes una señal de capacidad en una meta de productividad se convierte en una mentira.

4. **Antes de recurrir a un marco de escalado pesado, ¿has intentado reducir las dependencias entre equipos que crean la necesidad de coordinar en primer lugar?** Esto importa más para una organización grande, porque el reflejo cuando muchos equipos deben enviar juntos es comprar un marco como SAFe, LeSS, o Scrum@Scale, y la maquinaria de escalado pesado a menudo contrabandea de vuelta la sobrecarga de mando y control, pesada en planes, que Ágil existe para eliminar. La consideración en competencia es real: alguna coordinación genuinamente se requiere, y desescalar hacia equipos independientes y alineados con flujo exige bajo acoplamiento, propiedad clara, y una plataforma lo bastante madura para dejar que los equipos se autoatiendan, que quizás todavía no tengas. Trae evidencia a la discusión: mapea las dependencias reales que fuerzan a los equipos a esperarse mutuamente, y pregunta cuántas sobrevivirían a un rediseño deliberado de las fronteras de equipo y la propiedad de servicio. En programas empresariales y gubernamentales, donde un organigrama de docenas de equipos es común, la pregunta honesta es si estás añadiendo estructura de coordinación para compensar un diseño de arquitectura y equipo que en cambio podrías simplificar, para que necesites menos coordinación en absoluto.

5. **¿Tienen tus equipos contacto genuino y repetido con los ciudadanos o clientes para los que construyen, o la retroalimentación llega filtrada a través de intermediarios?** La colaboración con el cliente es uno de los cuatro valores del Manifiesto, y las iteraciones que carecen de contacto real con el usuario silenciosamente optimizan lo equivocado, que es el fallo más costoso que se supone que Ágil debe prevenir. La tensión es que el acceso directo es difícil de arreglar a escala y a menudo se obstruye por las mismas reglas de contratación pública, privacidad, y seguridad que las organizaciones grandes y públicas deben honrar, así que el camino fácil es sustituir un intermediario: un analista de negocio, un comité de partes interesadas, o el mazo de investigación del último trimestre. Trae evidencia: para tus últimos incrementos, cuenta cuántos se validaron con un usuario real realmente usando el software, y cuántos descansaron en la opinión de alguien sobre lo que quieren los usuarios. Para un servicio gubernamental, añade si tu prueba de usabilidad alcanzó a la gente más afectada, incluyendo a los usuarios de tecnología de asistencia y aquellos con baja confianza digital, porque un servicio público que funciona solo para la mayoría segura ha fallado su obligación de rendición de cuentas incluso si cada ceremonia corrió según el calendario.

6. **¿Se financian y gobiernan tus equipos en torno a resultados y cadencia, o en torno a un alcance fijo que silenciosamente fuerza el comportamiento de cascada detrás de las ceremonias?** Esta es la diferencia entre la agilidad real y el ágil falso, y se decide por encima del equipo, en cómo se libera el dinero y cómo se reporta el éxito, no en si ocurren las reuniones diarias. El impulso en competencia es que las funciones de finanzas, cartera, y supervisión están construidas para aprobar un alcance fijo contra un presupuesto fijo años por adelantado, y pedirles que financien un resultado con alcance flexible se siente como una pérdida de control que resistirán. Trae evidencia: rastrea cómo se financió una iniciativa actual y qué reporta, y comprueba si los equipos se miden por resultados entregados y flujo o por puntos de historia y adherencia a un alcance firmado hace mucho tiempo. En entornos empresariales y gubernamentales, conecta esto directamente con la envoltura de financiación y cumplimiento (capítulo 10.6): si el dinero está comprometido con una puesta en marcha distante y de todo o nada, los equipos no pueden ser adaptativos sin importar cuán fielmente realicen los rituales, y la corrección pertenece al modelo de gobernanza más que a los equipos de entrega.

## Perspectiva sectorial

**Startup.** Vive los valores y salta el debate del marco. Envía una porción funcional a usuarios reales cada semana, siéntate lo bastante cerca de los fundadores y clientes tempranos para que la retroalimentación llegue diariamente, y da la bienvenida a un cambio de dirección en el momento en que la evidencia diga que la apuesta actual está equivocada. Tu recurso más escaso es la atención de ingeniería, así que protege la excelencia técnica (integración continua, pruebas automatizadas, desarrollo basado en tronco) incluso bajo presión de lanzamiento, porque esa disciplina es lo que te mantiene capaz de pivotar barato la próxima semana.

**Pequeña empresa.** Sin un entrenador ágil y con un presupuesto ajustado, trata Ágil como un puñado de hábitos en lugar de un programa de transformación que dotas de personal: un ciclo semanal corto, un tablero visible con límites de trabajo en progreso, y una mejora concreta cada semana que realmente terminas. Apóyate en Kanban, que necesita poca ceremonia y se ajusta al trabajo impulsado por interrupciones, y adopta las prácticas incorporadas en las herramientas que ya compras en lugar de levantar un proceso pesado. Juzga el esfuerzo por si estás enviando software útil a los clientes más a menudo, no por cuán de cerca imitas a Scrum.

**Empresa.** El problema es coordinar a muchos equipos sin reintroducir el mando y control. Prefiere desescalar, es decir, reducir las dependencias entre equipos a través del diseño de equipo alineado con flujo y una plataforma sólida, antes de adoptar un marco de escalado pesado. Financia y gobierna en torno a resultados (OKR) y cadencia en lugar de alcance anual fijo y puntos de historia, haz innegociables las prácticas de ingeniería al estilo XP entre equipos, y gestiona la entrega como una cartera con métricas de flujo y medidas de resultado para que los grupos mejoren con evidencia en lugar de ritual.

**Gobierno.** Las reglas de contratación pública, la transparencia, y la rendición de cuentas pública moldean cada elección. Estructura contratos modulares y basados en resultados con incrementos más cortos en lugar de un único megacontrato de alcance fijo, ya que la contratación pública ágil es donde la agilidad del sector público más a menudo tiene éxito o falla. Incorpora la auditoría, la accesibilidad, y la seguridad en cada incremento a través de la automatización para que la supervisión se satisfaga con el acto de construir, publica el progreso y la evidencia de valor público a los organismos de supervisión, y lucha por el acceso genuino a los ciudadanos (incluyendo a los usuarios de tecnología de asistencia) en cada iteración, porque es la restricción que más a menudo se negocia fuera.

## Ejemplos

**Startup.** Una startup de cinco personas salta el debate de ceremonia y vive los valores ágiles directamente. Envía una porción funcional a usuarios reales cada semana, se sienta lo bastante cerca de los fundadores y clientes tempranos para que la retroalimentación llegue diariamente, y da la bienvenida a un cambio de dirección la próxima semana cuando la evidencia diga que la apuesta actual está equivocada. El equipo se niega a intercambiar la excelencia técnica por velocidad, así que la integración continua, las pruebas automatizadas, y el desarrollo basado en tronco son innegociables incluso bajo presión de lanzamiento, y cada retrospectiva del viernes produce un cambio concreto que el equipo realmente termina antes de la siguiente. Nunca rastrea la velocidad como objetivo, midiendo en cambio si el trabajo enviado movió la activación y si los tiempos de espera se están reduciendo.

**Empresa.** La iniciativa de transformación de 60 equipos de una telecomunicaciones inicialmente «hace Scrum» pero no ve mejora. Los equipos todavía reciben alcance anual fijo y reportan sobre la velocidad. Un reinicio reenfoca en los principios: los OKR trimestrales reemplazan los mandatos de función, los equipos se reorganizan para reducir las dependencias entre equipos (desescalado), y las prácticas de XP (CI, TDD, desarrollo basado en tronco) se vuelven innegociables. Los tiempos de espera caen, los defectos bajan, y, crucialmente, el negocio empieza a medir resultados en lugar de puntos de historia, conectando la entrega ágil al canal de descubrimiento (capítulo 11.1).

**Gobierno.** Un equipo de servicio digital reconstruye una aplicación de beneficios de cara al ciudadano usando Ágil dentro de una envoltura de gobernanza híbrida: incrementos de dos semanas entregando software funcional y probado con usuarios; la accesibilidad y seguridad incorporadas en cada incremento; y la contratación pública modular reemplazando un único contrato de precio fijo. Las pruebas de usabilidad reales con ciudadanos (incluyendo usuarios de tecnología de asistencia) en cada iteración atrapan problemas que el antiguo proceso de cascada habría enviado. El programa entrega un servicio usable temprano y muestra valor público medible a los organismos de supervisión. Este es el patrón detrás de los éxitos modernos del sector público, y el antídoto para los fallos de gran explosión pasados.

## Caso de negocio: motivaciones, ROI y TCO

El retorno de Ágil viene de la **reducción de riesgo y la realización de valor más rápida**. Al entregar software funcional temprano y a menudo, los equipos convierten la incertidumbre en evidencia continuamente, atrapando los fallos de cosa equivocada y no funcionará mientras son baratos, en lugar de en una puesta en marcha distante y costosa. La investigación detrás de la entrega moderna (los hallazgos de DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), en el capítulo 11.2) muestra que las prácticas que promueve Ágil (lotes pequeños, lanzamientos frecuentes, retroalimentación rápida, excelencia técnica) se correlacionan con mejor entrega *y* estabilidad *y* rendimiento organizacional. Los incrementos tempranos también empiezan a retornar valor antes, mejorando el tiempo y el tamaño total del ROI frente a un lanzamiento de gran explosión que no retorna nada hasta el final.

Sobre el [**costo total de propiedad**](https://en.wikipedia.org/wiki/Total_cost_of_ownership), Ágil baja el costo del cambio a lo largo de la vida de un sistema, siempre que la disciplina de ingeniería sea real. Su riesgo dominante es el *ágil falso*: ceremonia sin principio ni oficio, que añade sobrecarga de reuniones sin entregar ningún beneficio, y puede ser peor que una cascada honesta. Así que el caso de negocio es condicional. El ROI es alto cuando adoptas Ágil como mentalidad-más-ingeniería, y aproximadamente cero (o negativo) cuando lo adoptas como ritual. Presenta el caso al liderazgo enmarcando Ágil como reducción de riesgo continua y medición de resultados, no como «ir más rápido», e insistiendo en que la inversión incluya prácticas técnicas, no solo nuevas reuniones.

## Antipatrones y trampas

- **Ágil falso / de culto de carga:** ceremonias realizadas mientras las decisiones, la financiación, y la mentalidad permanecen en cascada.
- **Velocidad como productividad:** convertir una estimación de capacidad en un objetivo, lo cual la corrompe ([Ley de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Scrum oscuro:** hacer sprint sin excelencia técnica hacia código inmantenible y plagado de defectos.
- **Retrospectivas sin cambio:** reflexión que no produce acciones completadas.
- **Alcance fijo *y* fecha *y* costo:** llamarlo ágil mientras la calidad silenciosamente absorbe la presión.
- **Cliente ausente:** sin retroalimentación real de usuario, así las iteraciones optimizan lo equivocado.
- **Culto al marco:** «SAFe/Scrum lo dice» anulando los principios y el juicio del equipo.
- **Escalar antes de desescalar:** añadir marcos de coordinación pesados en lugar de reducir las dependencias.

## Modelo de madurez

- **Nivel 1, Iniciar.** Entrega en cascada o ad hoc; lanzamientos de gran explosión; el trabajo es reactivo y pesado en planes, sin retroalimentación iterativa ni sentido compartido de por qué Ágil podría ayudar.
- **Nivel 2, Desarrollar.** Unos pocos equipos adoptan ceremonias ágiles (reuniones diarias, sprints, retrospectivas), pero la práctica es inconsistente en toda la organización: la mentalidad y la disciplina de ingeniería van rezagadas respecto a los rituales, la velocidad se trata como producción, y el alcance todavía se fija por adelantado.
- **Nivel 3, Estandarizar.** Los valores y principios genuinamente guían el trabajo en toda la organización, documentados y esperados de cada equipo: la excelencia técnica al estilo XP (CI, pruebas automatizadas, refactorización, desarrollo basado en tronco) es práctica estándar, los equipos se autoorganizan, los clientes se comprometen en cada iteración, y las retrospectivas producen cambio concreto y completado.
- **Nivel 4, Gestionar.** La entrega se mide y controla contra líneas base: los equipos rastrean el tiempo de espera, la frecuencia de despliegue, la tasa de fallo de cambio, y la tasa de escape de defectos (las métricas de flujo y estabilidad al estilo DORA), junto a las medidas de resultado vinculadas a los resultados clave, y comparan cada una contra una línea base conocida. Las acciones retrospectivas se rastrean hasta su finalización, se monitorean las señales de ritmo sostenible como las horas extra y el agotamiento, y la velocidad nunca se usa como objetivo de productividad. Las decisiones de continuar o no descansan en esta evidencia en lugar de en la opinión.
- **Nivel 5, Orquestar.** La entrega adaptativa se integra con la planificación de negocio y riesgo en toda la organización: los resultados (OKR) impulsan la financiación y la cadencia, el diseño de equipo de baja dependencia (desescalado) minimiza la sobrecarga de coordinación, y la gobernanza híbrida satisface la supervisión sin ralentizar la entrega. La mejora continua es cultural en lugar de ceremonial, y la organización rutinariamente reajusta el alcance, reforma los equipos, y reequilibra su cartera a medida que cambian la evidencia y el panorama de riesgo.

## Ideas para el debate

1. Puntúa a tu equipo contra los doce principios ágiles: ¿dónde eres ágil en ceremonia pero no en sustancia?
2. ¿Se usa la velocidad en tu equipo como un pronóstico o como un objetivo, y qué le ha hecho eso al comportamiento?
3. ¿Qué prácticas técnicas de XP faltan, y cómo aparece su ausencia como defectos o cambio lento?
4. Antes de adoptar un marco de escalado, ¿podrías reducir en cambio las dependencias entre equipos?
5. En tu contexto, ¿qué específicamente bloquea el acceso real de usuario en cada iteración, y cómo podrías eliminarlo?
6. ¿Cuál fue el último cambio concreto que una retrospectiva realmente produjo?

## Puntos clave

- Ágil es una **mentalidad de valores y principios**, no un conjunto de ceremonias; los marcos son puntos de partida, no la meta.
- Entrega **software funcional frecuentemente**, da la bienvenida al cambio, y empodera a **equipos autoorganizados**.
- **La excelencia técnica (prácticas XP) es innegociable.** La agilidad sin ella se convierte en decadencia rápida.
- **Escala con cuidado; prefiere desescalar.** Reduce las dependencias antes de añadir marcos de coordinación.
- En la empresa/gobierno, combina la **entrega adaptativa con la gobernanza híbrida y la contratación pública ágil**, y lucha por el acceso real de usuario.
- El ROI es la **reducción de riesgo continua y el valor más temprano**, pero solo cuando Ágil es real, no ritual. Véanse los capítulos 1.4, 11.1, 11.2, 10.6, y 11.3.

## Referencias y lecturas adicionales

- Kent Beck et al., *Manifesto for Agile Software Development* y sus doce principios (agilemanifesto.org, 2001).
- Ken Schwaber y Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* y *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton y Manuel Pais, *Team Topologies* (diseño de equipo y desescalado).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidencia para las prácticas ágil/DevOps).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
