# 6.7 Agentes de IA y sistemas agénticos

## Presentación y motivación

Un **agente de IA** es un [modelo de lenguaje grande](https://en.wikipedia.org/wiki/Large_language_model) (LLM) envuelto en un bucle: se le asigna un objetivo, puede invocar herramientas, conserva una memoria de lo que ha hecho y decide por sí mismo el siguiente paso hasta que alcanza la meta o se rinde. Ese bucle es toda la diferencia entre un agente y las llamadas de prompt-respuesta del capítulo 6.3. Una sola llamada responde a una pregunta. Un agente lee el correo, consulta una base de datos, abre un ticket, verifica el resultado y lo vuelve a intentar. El modelo ya no se limita a generar texto: está eligiendo acciones dentro de tus sistemas.

Ese cambio transforma el problema de ingeniería. Cuando el modelo solo escribe palabras, una salida defectuosa es una frase mal construida. Cuando el modelo acciona herramientas, una salida defectuosa puede enviar un mensaje equivocado, borrar un registro o transferir dinero. Por eso un [agente inteligente](https://en.wikipedia.org/wiki/Intelligent_agent) se comprende mejor como un planificador de fiabilidad dudosa, alojado dentro de un sistema sí de confianza, y la mayor parte del esfuerzo de ingeniería consiste en acotar qué está autorizado a hacer ese planificador. Este capítulo se apoya directamente en los fundamentos de los LLM del capítulo 6.3, en las preocupaciones de confianza y rendición de cuentas del capítulo 6.5 y en las prácticas de plataforma del capítulo 6.6.

Para los equipos grandes, las implicaciones son tanto organizacionales como técnicas. Las empresas quieren agentes integrados en sistemas internos reales (gestión de incidencias, finanzas, registros de clientes), y con ello los agentes heredan los controles de acceso y las obligaciones de gestión del cambio correspondientes. En el sector público se añade la rendición de cuentas ante la ciudadanía: toda acción autónoma que afecte a un ciudadano debe ser explicable, supervisable y auditable *a posteriori*. El patrón es potente. Implementado sin disciplina, es la vía más rápida para automatizar los errores.

## Principios fundamentales

- Un agente es un modelo más un bucle, herramientas, memoria y un objetivo. El riesgo vive en el bucle, no en el texto.
- Acorde a la tarea la autonomía. Concede la menor libertad posible que permita cumplir el objetivo.
- Prefiere un flujo de trabajo fijo cuando los pasos ya están definidos. Recurre a la autonomía abierta solo cuando no lo estén.
- Considera cada herramienta como una superficie de ataque y concédele el mínimo privilegio necesario para funcionar.
- Incorpora un humano en el bucle para las acciones con consecuencias o irreversibles, y haz que revertir sea barato.
- Evalúa el éxito en la tarea, no en cómo se lee la transcripción.
- Traza cada ejecución. Una acción que no puedas reconstruir es una acción que no puedes gobernar.
- El diseño más simple que funciona suele ser el correcto. A menudo, eso no es un agente.

## Recomendaciones

### Empieza por un flujo de trabajo y añade autonomía solo donde sea imprescindible

El error más frecuente es recurrir a un agente autónomo cuando bastaría un flujo predefinido. Si ya conoces los pasos (extraer campos, validarlos, localizar un registro, redactar una respuesta), exprésalos como un flujo orquestado en el que el modelo llena huecos concretos. La autonomía se justifica cuando la ruta no puede predecirse de antemano: por ejemplo, investigación abierta o triaje entre múltiples herramientas posibles. Acota la autonomía a la tarea: limita el número de pasos, restringe el conjunto de herramientas a lo que el objetivo exige y establece una condición de parada clara. Una buena norma es dar al modelo exactamente tanta libertad como el problema demanda y no un grado de más.

### Haz del uso de herramientas la capacidad central, y hazlo seguro

El uso de herramientas (también llamado *function calling* o llamada de funciones) es lo que convierte a un modelo en agente. Define cada herramienta con un esquema preciso, valida cada argumento que el modelo suministra y aplica el [principio de mínimo privilegio](https://en.wikipedia.org/wiki/Principle_of_least_privilege): un agente de informes de solo lectura obtiene credenciales de solo lectura, nunca acceso de escritura que podría malversar. Ejecuta las herramientas en un [entorno aislado](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) para que una llamada incorrecta no alcance más allá de su radio de impacto. Prefiere muchas herramientas estrechas y de propósito único a pocas de alcance amplio, porque una herramienta estrecha es más fácil de razonar, de permisionar y de auditar. Es la misma contención que el capítulo 6.3 recomienda para el uso de herramientas en LLM, aquí elevada a elemento central.

### Emplea patrones explícitos de razonamiento y planificación

Los agentes funcionan mejor cuando su proceso de pensamiento está estructurado. En el patrón razonar-actuar (popularizado por la investigación ReAct), el modelo alterna entre razonar sobre la situación y ejecutar una acción, observa el resultado y vuelve a razonar. Para objetivos más complejos, haz que el modelo planifique primero (descomponga en subtareas) y luego ejecute, para que puedas inspeccionar e incluso aprobar el plan antes de que se invoque ninguna herramienta. Mantén estos bucles observables e interrumpibles. Un plan que se puede leer es un plan que se puede detener.

### Mantiene un humano en el bucle para las acciones con consecuencias

Decide, para cada herramienta y para cada acción, si el modelo puede actuar por sí mismo o si debe pedir permiso. Las acciones reversibles y de bajo riesgo (buscar, redactar) pueden ejecutarse sin supervisión. Las que tienen consecuencias o son irreversibles (enviar comunicaciones externas, mover dinero, modificar datos en producción, resolver el caso de un ciudadano) exigen una [puerta de control humano](https://en.wikipedia.org/wiki/Human-in-the-loop) con autoridad real para decir que no. Diseña para la reversibilidad siempre que sea posible: prefiere poner un cambio en una zona de ensayo antes que confirmarlo, y convierte el deshacer en una primera clase de función, de modo que un error cueste unos minutos, no una incidencia.

### Trata el modelo de seguridad como adversarial

Los agentes amplían la superficie de ataque descrita en el capítulo 4.2. La amenaza principal es la [inyección de prompt](https://en.wikipedia.org/wiki/Prompt_injection): instrucciones maliciosas ocultas en una página web, un documento o un correo electrónico que el agente lee y obedece. Íntimamente relacionada está el [problema del subdelegado confundido](https://en.wikipedia.org/wiki/Confused_deputy_problem), en el que un atacante engaña a un agente con privilegios para que malgaste su propio acceso legítimo, por ejemplo, exfiltrando datos a través de una herramienta que el agente está autorizado a invocar. Parte del supuesto de que cualquier contenido que el agente ingiera puede ser hostil. Separa las instrucciones de confianza de los datos no confiables, restringe las herramientas para que un agente secuestrado no alcance sistemas sensibles y no permitas nunca que la salida cruda de un modelo dispare una acción irreversible sin validación.

### Evalúa en el éxito de la tarea y pruebe regresiones ante la no determinación

Juzga a los agentes por si logran la tarea, no por si la transcripción suena inteligente. Construye un conjunto de evaluación con objetivos representativos y criterios de éxito verificables (¿el ticket recibió la prioridad correcta?, ¿el reembolso cumple la política?) y ejecútalo ante cada cambio de prompt, modelo o herramienta. Como los agentes son no deterministas, una sola pasada prueba poco: ejecuta cada caso varias veces y mide una tasa de éxito, no un sí o un no. Esto extiende la disciplina de evaluación offline y online de los capítulos 6.3 y 6.2 (ingeniería de aprendizaje automático y MLOps) a sistemas cuya salida es una secuencia de acciones.

### Traza cada ejecución para la observabilidad, el coste y el manejo de fallos

No puedes gobernar lo que no puedes ver. Traza cada ejecución del agente de principio a fin (capítulo 6.6): el objetivo, cada paso de razonamiento, cada llamada a herramienta con sus argumentos y resultado, los tokens consumidos y el resultado final. Esa traza es, a la vez, tu depurador, tu rastro de auditoría y tu medidor de costes. Establece presupuestos duros de pasos, tiempo y gasto, porque un agente que entra en bucle puede quemar latencia y dinero a gran velocidad. Maneja el fallo de forma explícita: reintenta con retroceso los errores transitorios de herramientas, pero detecta los bucles en los que el modelo repite una acción que falla y falla de forma segura en lugar de dar vueltas en vano.

## Compromisos: ventajas e inconvenientes

| Elección | Ventajas | Inconvenientes | Cuándo es adecuada |
|---|---|---|---|
| Flujo de trabajo fijo (el modelo rellena huecos) | Predecible, económico, fácil de probar y auditar | Rígido; se rompe ante rutas imprevistas | Cuando los pasos se conocen de antemano |
| Agente autónomo único | Flexible; maneja objetivos abiertos | Más difícil de controlar, evaluar y acotar | Cuando la ruta no puede predecirse |
| Orquestación multiagente | Paralelismo; roles especializados | Coste de coordinación, errores que se acumulan, mayor gasto | Cuando la tarea se descompone de verdad en partes independientes |
| Acción sin supervisión | Rápida, sin fricción | Los errores se ejecutan sin revisión | Cuando las acciones son reversibles y de bajo riesgo |
| Puerta de control humano | Seguridad, responsabilidad, reversibilidad | Más lenta; exige capacidad de revisión | Cuando las acciones tienen consecuencias o son irreversibles |

La tensión central es autonomía frente a control. Más autonomía abarca más situaciones, pero exige más salvaguardas, más evaluación y más dinero, y falla de formas más difíciles de prever. Los diseños multiagente seducen con su elegancia, pero cada agente añadido suma sobrecarga de coordinación y otro punto donde un pequeño error puede escalar hasta un resultado erróneo. Resuelve la tensión partiendo de la menor autonomía que resuelve el problema y añadiendo libertad solo cuando una tarea concreta te obliga, siempre emparejada con una salvaguarda equivalente.

## Preguntas para debatir con tu equipo

1. **¿Esta función necesita de verdad un agente, o bastaría un flujo de trabajo más seguro y económico?** La autonomía resulta tentadora, pero la mayoría de las tareas tienen pasos conocibles que un flujo orquestado resuelve con mucho menos riesgo. En un equipo grande, defaultear a agentes significa que cada grupo asume las cargas de evaluación, trazabilidad y seguridad que un diseño más simple habría evitado. Trae la tarea concreta y pregunta si sus pasos pueden predecirse; si pueden, un agente es probablemente sobre-ingeniería. Reserva la autonomía abierta para objetivos cuya ruta varía genuinamente en cada caso. La respuesta debería orientar la mayoría de funciones hacia un flujo de trabajo y dejar un pequeño conjunto deliberado como verdaderos agentes.

2. **Para cada herramienta que el agente puede invocar, ¿cuál es el peor escenario si un agente secuestrado la usa y qué lo impide?** La inyección de prompt y el ataque de subdelegado confundido convierten el propio acceso legítimo del agente en arma contra ti, así que la lente correcta es adversarial (capítulo 4.2). Inventaría cada herramienta, su alcance de privilegio y si una instrucción maliciosa infiltrada en el contenido ingerido podría alcanzarla. Para empresas que conectan agentes a sistemas internos, aquí es donde el mínimo privilegio, el entorno aislado y las puertas humanas en acciones irreversibles cobran sentido real. Trae la lista de herramientas y las credenciales que cada una ostenta. Si hay alguna acción con consecuencias que se puede alcanzar sin validación ni revisión humana, esa es la primera cosa que hay que corregir.

3. **¿Cómo sabríamos si la tasa de éxito de un agente bajó, cuando cada ejecución se ve plausible?** Los agentes son no deterministas, por lo que una transcripción que suena bien puede haber tomado la acción equivocada, y una ejecución en verde no prueba nada. Pregúntate si dispones de un conjunto de evaluación con resultados verificables, ejecutado varias veces por caso para producir una tasa de éxito en lugar de un simple aprobado. En despliegues de alto impacto o públicos, discute cómo las trazas de ejecución permiten reconstruir exactamente qué ocurrió cuando algo sale mal (capítulos 6.5 y 6.6). Si tu única señal es la queja del usuario, ya eres tarde. La respuesta debería financiar un andamiaje de evaluación antes de escalar, no después de una incidencia.

4. **¿Qué acciones de este agente son verdaderamente irreversibles, quién ostenta la autoridad para aprobarlas y disponemos de capacidad de revisión para sostener esa puerta?** La tentación es dejar que el modelo actúe sin supervisión en todo, pero una puerta humana es real solo si una persona nombrada con autoridad para decir que no está disponible cuando el agente lo solicita. En un equipo grande, una cola de aprobaciones sin dueño se convierte en un sello de goma, y la seguridad que diseñaste se evapora bajo el volumen. Trae la lista completa de acciones que el agente puede tomar, marca cada una como reversible o irreversible y estima el volumen diario de casos de baja confianza que caerían en un revisor. Pesa la fricción y el coste de personal de una puerta frente al alcance del daño de un error sin supervisión, y prefiere rediseñar una acción irreversible en una escalonada y revocable antes que añadir otro revisor. En entornos empresariales y públicos, vincula cada acción con consecuencias a un responsable concreto y a un registro de gestión del cambio, porque una acción autónoma que afecta a un ciudadano o un cliente y que ningún humano aprobó es exactamente el fallo que una auditoría detectará.

5. **¿Recurren a un diseño multiagente porque la tarea se descompone de verdad o porque se ve elegante?** Repartir el trabajo entre agentes especializados resulta seductor, pero cada agente extra añade sobrecarga de coordinación y otro punto donde un pequeño error se acumula hasta un resultado erróneo. Para una organización grande, el coste no es solo gasto y latencia: un sistema multiagente es mucho más difícil de trazar, evaluar y razonar cuando falla, así que la carga de gobernanza se multiplica con cada rol añadido. Trae la tarea y muestra, de forma concreta, qué partes se ejecutan en paralelo e independentemente, y luego compara la tasa de éxito medida y el coste de una versión multiagente frente a un agente único en el mismo conjunto de evaluación. Si el agente único gana o empata, el diseño elegante es sobre-ingeniería. En despliegues regulados o públicos, recuerda que cada agente en la cadena es otro componente que un organismo de supervisión debe poder inspeccionar, así que toda estructura que no puedas justificar es una responsabilidad añadida.

6. **¿Cuáles son los presupuestos duros de pasos, tiempo y gasto de un agente y cómo se detectaría un agente en bucle antes de que dispare el coste o la latencia?** Un agente que repite una acción que falla puede quemar dinero y tiempo sin previo aviso, así que la autonomía sin límites es un riesgo financiero tanto como de seguridad. En un equipo grande que ejecuta muchos agentes, un solo bucle mal comportado puede disparar la factura de la nube o agotar un límite de tasa que deja sin servicio a cada carga de trabajo, lo que convierte los límites por ejecución en una preocupación operativa compartida y no el problema de un solo equipo. Trae los presupuestos actuales de pasos, tiempo y tokens de cada agente, la alerta que se dispara cuando una ejecución los supera y la detección de bucles que falle de forma segura en lugar de dar vueltas. Pesa los presupuestos estrechos, que pueden cortar una tarea legítimamente difícil, frente a los holgados, que permiten que el coste se descontrole. En entornos empresariales y públicos donde el gasto debe preverse y justificarse, un agente cuyo coste es ilimitado es una partida que no se puede sostener en una revisión presupuestaria ni en una auditoría.

## Perspectiva por sector

**Startups.** Lanza un agente estrecho que toque tu valor central, sobre un modelo gestionado, con el conjunto mínimo de herramientas que cubra la tarea y un tope duro en pasos y gasto. Resistir la tentación del demo multiagente: tu escasa atención de ingeniería está mejor invertida acotando la autonomía de un solo agente y trazando sus ejecuciones que coordinando roles que no podrás mantener. Mantén cada acción con consecuencias detrás de una única puerta de «redactar, nunca enviar», de modo que un error cueste un clic para deshacerlo, no una incidencia.

**Pequeñas empresas.** No tienes a nadie que sostenga un andamiaje de evaluación ni un entorno aislado, así que prefiere agentes integrados en herramientas que ya confíes y activa solo la autonomía que puedas supervisar a simple vista. Trata cualquier agente que pueda enviar, pagar o borrar en tu nombre como algo que debes mantener inactivo hasta que una persona confirme cada acción, porque un mensaje automático equivocado a un cliente te cuesta la relación. Prioriza a los proveedores que te muestren lo que hizo el agente y te permitan desactivar la automatización.

**Gran empresa.** El problema es gobernar agentes en varios equipos: patrones compartidos para acotar la autonomía, credenciales de mínimo privilegio para las herramientas, entornos aislados, puertas de control humano y trazabilidad de extremo a extremo para que ningún grupo reinvente las salvaguardas. Integra los agentes en los sistemas internos bajo los mismos controles de acceso que tendría un humano, pone las acciones irreversibles tras aprobadores nombrados y gestión del cambio, y gestiona el portafolio con métricas de tasa de éxito, presupuestos por ejecución y pruebas adversariales de inyección. Estandariza la capa de trazabilidad y evaluación para que el comportamiento de cualquier agente pueda reconstruirse y auditarse.

**Sector público.** La contratación pública, la transparencia y la rendición de cuentas ante la ciudadanía acotan cada decisión. Limita a los agentes a recopilar hechos y redactar, y reserva toda decisión que afecte a un ciudadano a un humano responsable, porque la responsabilidad de una decisión del sector público no puede delegarse en un modelo. Registra cada ejecución para que un organismo de supervisión pueda ver qué fuentes se consultaron y qué se hizo, exigió que los proveedores divulguen las herramientas y limitaciones del agente, y demuestra mediante un conjunto de evaluación adversarial que el agente se niega a actuar más allá de su ámbito acotado.

## Ejemplos

**Startup.** Un estudio de analítica de cinco personas construye un agente de triaje de soporte. Lee un ticket entrante, consulta la documentación y o bien redacta una respuesta o bien deriva el ticket a un humano; ese es todo el conjunto de herramientas. Las credenciales son de solo lectura más una única acción de «crear borrador» que nunca envía sin que una persona pulse el botón de envío. Cada ejecución se traza para que los fundadores puedan ver por qué un ticket se derivó donde se derivó, y a diario un conjunto de evaluación con cincuenta tickets reales ejecuta el agente cinco veces cada uno para seguir la tasa de exactitud en la derivación. Cuando el demo multiagente ingenioso de un competidor los tienta, se mantienen en un agente único porque su tarea no se descompone.

**Gran empresa.** Un banco construye un agente para ayudar al personal de operaciones a conciliar pagos fallidos. Se integra en los sistemas internos bajo los mismos controles de acceso que un empleado humano, a través de credenciales de servicio de mínimo privilegio acotadas exclusivamente a la conciliación. El agente puede investigar con libertad (consultar balances, buscar historial de transacciones), pero cualquier acción que mueva dinero o edite un registro se pone en zona de ensayo y requiere un aprobador humano nombrado, en cumplimiento de la gestión del cambio. Los documentos ingeridos se tratan como no confiables para amortiguar la inyección de prompt, las herramientas se ejecutan en entornos aislados y cada ejecución se traza de extremo a extremo para la auditoría. Un conjunto de evaluación offline bloquea cada cambio de modelo o prompt, y los presupuestos por ejecución limitan pasos y gasto para que un agente en bucle no dispare coste ni latencia.

**Sector público.** Una agencia de prestaciones pilota un agente para ayudar a los funcionarios a compilar los hechos de una solicitud: recopilar registros, verificar reglas de elegibilidad y redactar un resumen. La agencia traza una línea infranqueable: el agente recopila y redacta, pero un funcionario humano toma y asume cada decisión que afecta a un ciudadano, porque la responsabilidad de una decisión pública no puede delegarse en un modelo (capítulo 6.5). Cada ejecución se registra en su totalidad, mostrando qué fuentes se consultaron y qué se redactó, para que un organismo de supervisión pueda auditar cualquier caso. La autonomía se acota deliberadamente a lectura y redacción, las herramientas son de mínimo privilegio y se ejecutan en entornos aislados, y un conjunto de evaluación adversarial confirma que el agente se niega a actuar más allá de recopilar hechos.

## Caso de negocio: motivaciones, retorno y coste total

Los agentes generan retorno automatizando trabajos de varios pasos que antes requerían a una persona saltando entre sistemas: triaje, conciliación, investigación y operaciones rutinarias. El valor se manifiesta como trabajo completado sin que un humano intervenga en cada paso, ciclos más rápidos y personal liberado para tareas de mayor criterio. Como los agentes se construyen sobre LLM y herramientas existentes, el tiempo hasta un prototipo funcional es corto, y es exactamente por eso que los equipos sobre-diseñan.

El coste total de propiedad es donde los agentes se diferencian de las funciones LLM sencillas. Encima del coste de inferencia, pagas por las integraciones de herramientas, el entresijado de entornos aislados y permisos, el andamiaje de evaluación, la pila de trazabilidad y observabilidad (capítulo 6.6) y los revisores humanos que sostienen las puertas de aprobación. Un agente que entra en bucle o está mal acotado suma un coste variable que puede dispararse sin aviso, de modo que los presupuestos de pasos y gasto son parte del diseño, no un añadido posterior. El coste de no adoptar es una operación más lenta y una labor manual que tus competidores ya automatizan. El coste de adoptar con descuido es una acción autónoma que envía el mensaje equivocado, filtra datos o toma una decisión sin rendición de cuentas. Presenta el caso ante la dirección emparejando un objetivo concreto de automatización con un plan concreto de salvaguardas, evaluación y supervisión humana, y sé honesto de que las salvaguardas son la mayor parte del coste.

## Antipatrones y riesgos

- **Un agente donde bastaba un flujo de trabajo.** Asumir todo el riesgo de la autonomía para una tarea cuyos pasos eran conocibles.
- **Herramientas y credenciales de alcance excesivo.** Una sola herramienta «haz de todo» en lugar de varias estrechas y de mínimo privilegio.
- **Ceguera ante la inyección de prompt.** Alimentar con contenido no confiable a un agente que ostenta privilegios reales.
- **Sin puerta humana en acciones irreversibles.** Dejar que el modelo envíe, pague o borre sin revisión.
- **Teatro multiagente.** Repartir una tarea simple entre varios agentes y pagar coste de coordinación sin beneficio alguno.
- **Evaluación a sensación.** Juzgar por cómo suena la transcripción en lugar de por la tasa de éxito de la tarea.
- **Bucles sin límites.** Sin tope en pasos, tiempo o gasto, un agente atascado quema dinero y latencia sin control.
- **Ejecuciones sin traza.** Sin registro de lo que el agente hizo, quedando en la incapacidad de depurar, auditar o rendir cuentas.

## Modelo de madurez

- **Nivel 1, Iniciar:** Los agentes se prototipan de forma ad hoc, con acceso a herramientas amplio y sin límites. El éxito se juzga por demos, de forma reactiva, después de que algo se rompe. No hay conjunto de evaluación, no hay trazabilidad y no hay puerta humana en acciones con consecuencias.
- **Nivel 2, Desarrollar:** Algunos agentes tienen bucles acotados y herramientas de mínimo privilegio, y existe una trazabilidad básica, pero la práctica varía de equipo a equipo. Un conjunto de evaluación manual detecta regresiones evidentes en algunos proyectos, mientras que en otros no existe. La aprobación humana resguarda las acciones irreversibles más evidentes, pero la cobertura es desigual y no documentada.
- **Nivel 3, Estandarizar:** Patrones compartidos gobiernan la autonomía, los permisos de herramientas, los entornos aislados y las puertas de control humano, documentados y aplicados en todos los equipos. Cada acción con consecuencias tiene puerta o validación, los agentes se trazan de extremo a extremo y un conjunto de evaluación automatizado con puntuación por tasa de éxito se ejecuta ante cada cambio. La inyección de prompt se trata como amenaza permanente con una respuesta definida.
- **Nivel 4, Gestionar:** El portafolio de agentes se mide y controla contra líneas base. La tasa de éxito por tarea, la tasa de resistencia a inyección, el coste y el número de pasos por ejecución, la latencia de aprobación humana y los incidentes de bucle o fallo se siguen como métricas; los umbrales de retroceso y de parada se ejecutan sobre esa evidencia, no sobre quejas. Los presupuestos por ejecución en pasos, tiempo y gasto se monitorizan, y una regresión en cualquier métrica desencadena acción antes de escalar, no después de una incidencia.
- **Nivel 5, Orquestar:** La autonomía se ajusta al riesgo de la tarea por política y se modula de forma continua a medida que llegan resultados. La evaluación continua offline y online vincula el comportamiento del agente con los resultados de negocio, y la organización retira, reescopúa o repermisiona agentes de forma rutinaria a medida que el panorama de riesgo cambia. La trazabilidad, los presupuestos de coste y los registros de auditoría son uniformes en todo el portafolio; las defensas contra inyección y subdelegado confundido se prueban de forma adversarial; la responsabilidad de las acciones autónomas es clara y auditable.

## Ideas para la reflexión

1. ¿Cuáles de tus funciones LLM actuales se han convertido en agentes sin que te dieras cuenta, y se ha acotado a propósito la autonomía de cada una?
2. Para cada herramienta del agente, ¿cuál es la forma más barata de que un atacante la abuse a través de contenido inyectado, y qué lo impide?
3. ¿Dónde has elegido diseños multiagente y puedes demostrar que el coste de coordinación compensó frente a un agente único?
4. ¿Qué acciones del agente son verdaderamente irreversibles, y podría rediseñarse cada una en una reversible o escalonada?
5. Si mañana un agente tomara una acción dañina, ¿podrías reconstruir exactamente qué hizo y quién era el responsable?

## Ideas clave

- Un agente es un LLM en un bucle con herramientas, memoria y un objetivo. El riesgo vive en el bucle y en las herramientas, no en el texto.
- Prefiere un flujo de trabajo fijo cuando los pasos ya están definidos; reserva la autonomía para objetivos genuinamente abiertos y acótala con firmeza.
- El uso de herramientas es la capacidad central. Dá a cada herramienta mínimo privilegio, un esquema validado y un entorno aislado.
- Pone las acciones con consecuencias y las irreversibles tras un humano con autoridad real, y diseña para que revertir sea barato.
- Trata a los agentes como adversarios: defiéndete de la inyección de prompt y del abuso de subdelegado confundido (capítulo 4.2).
- Evalúa la tasa de éxito de la tarea a lo largo de múltiples ejecuciones y traza cada ejecución para depurar, controlar costes y auditar (capítulos 6.5 y 6.6).
- A menudo, la respuesta correcta es no construir un agente.

## Referencias y lecturas complementarias

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (orientación de ingeniería sobre flujos de trabajo frente a agentes).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (incluyendo inyección de prompt y agencia excesiva).
- Simon Willison, sobre la inyección de prompt y el «trifecta mortal» para agentes de IA.
- Norman Hardy, *The Confused Deputy* (la formulación clásica del problema del subdelegado confundido).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell y Peter Norvig, *Artificial Intelligence: A Modern Approach* (agentes inteligentes y acción racional).

