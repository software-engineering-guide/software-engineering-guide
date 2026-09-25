# 2.1 Normas y estilo de programación

## Descripción general y motivación

Las normas de programación son esas convenciones compartidas que permiten a muchas personas escribir código como si lo hubiera redactado un único autor minucioso. Abarcan la nomenclatura, el formato, la estructura de los archivos, los patrones idiomáticos, el manejo de errores y los paradigmas que un equipo prefiere. En un equipo reducido, el criterio individual puede bastar. En un equipo grande (cientos o miles de ingenieros, decenas de contratistas, una rotación constante) , la inconsistencia se convierte en un impuesto que se paga con cada lectura, cada revisión y cada incorporación. Las normas convierten innumerables discusiones menores sobre estilo en una decisión puntual que, una vez tomada, una máquina ejecuta por ti.

En grandes organizaciones, los riesgos son concretos. El código se lee mucho más de lo que se escribe. En entornos empresariales y gubernamentales, una línea de código puede ser leída por auditores, revisores de seguridad y mantenedores años después de que su autor haya abandonado la organización. Un estilo uniforme reduce el coste mental de esa lectura, acorta la superficie de error y hace que el análisis automatizado funcione de forma fiable en los [analizadores estáticos](https://en.wikipedia.org/wiki/Lint_(software)) (herramientas que detectan automáticamente posibles errores y violaciones de estilo), los escáneres de seguridad y las herramientas de [refactorización](https://en.wikipedia.org/wiki/Code_refactoring). Cuando existe regulación, como en los servicios financieros, la salud, la defensa y los sistemas del sector público, las normas también forman parte de la evidencia que demuestra que un repositorio es mantenible y está bajo control.

El enfoque moderno consiste en tratar el estilo como una cuestión resuelta y automatizada, no como un asunto de juicio humano permanente. Los formatadores y los linters se ejecutan en el editor, en los ganchos de precommit y en la [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI, el proceso automatizado de compilación y prueba que se dispara con cada cambio). Las máquinas imponen el estilo, de modo que la atención en la revisión puede dedicarse al diseño y a la corrección. El objetivo no es la uniformidad por sí misma: es la eliminación de la fricción. Debería ser posible moverse entre servicios y equipos sin tener que reaprender lo básico.

## Principios fundamentales

- La consistencia supera a la preferencia individual: un único estilo acordado, aplicado en todas partes, vale más que el estilo «mejor» aplicado de forma desigual.
- Automatizar el cumplimiento. Los formatadores y los linters son la fuente de verdad, no los comentarios de revisión sobre espacios o sangrías.
- Optimizar para el lector y el mantenedor, no para el autor original.
- Preferir las convenciones que la comunidad del lenguaje ya ha adoptado antes que normas propias inventadas.
- Hacer que la norma sea fácil de adoptar: proporcionar configuraciones compartidas, plantillas y herramientas, no un PDF que nadie lee.
- Las reglas de estilo deben ser pocas, defendibles y unívocas; toda regla que no tenga un mecanismo de ejecución es solo una sugerencia.
- La nomenclatura es la decisión de legibilidad de mayor impacto y merece una orientación explícita.

## Recomendaciones

### Adoptar una guía de estilo canónica por lenguaje

Para cada lenguaje que se utilice, se adoptará una guía de estilo ampliamente reconocida como punto de partida (por ejemplo, la guía de la comunidad o del proveedor de ese lenguaje) y se documentarán únicamente las desviaciones que la organización necesite. No conviene inventar un estilo propio desde cero. Se publicará la elección en un lugar central y fácil de encontrar, y se versionará como código.

### Hacer que los formatadores sean un default innegociable

Se utilizará un formateador automático con criterio definido para cada lenguaje que disponga de uno, con una configuración única compartida que se incluya en el repositorio. El formato nunca debería ser motivo de debate en la revisión, porque se aplica automáticamente al guardar y se verifica en la CI. Cuando un lenguaje no cuente con un formateador sólido, se seleccionará una configuración de linter y se tratará de la misma manera.

### Ejecutar los linters como puertas de control, no como consejos

Se configurarán los linters con un conjunto de reglas acordado, se hará que las violaciones detengan la compilación y se mantendrá ese conjunto de reglas bajo [control de versiones](https://en.wikipedia.org/wiki/Version_control) para que cualquier cambio pase por revisión. Se separarán las reglas corregibles automáticamente (se aplican sin intervención) de las que requieren criterio humano (se marcan y bloquean). Las reglas nuevas se introducirán primero en modo de advertencia, se liquidará el backlog de incumplimientos y, solo entonces, se promocionarán a nivel de error.

### Aplicar el control en varias capas

Se proporcionará integración con el editor para retroalimentación inmediata, ganchos de precommit para la ejecución local y controles en la CI como puerta de control definitiva. Cuanto antes se detecte una violación, menor es el coste. La CI debe ser el último baluarte, porque los ganchos locales pueden saltarse.

### Establecer reglas explícitas de nomenclatura

Se estandarizará la convención de mayúsculas y minúsculas según el lenguaje, se exigirán nombres que revelen su intención, se prohibirán las abreviaturas engañosas y se definirán convenciones para booleanos, colecciones, unidades y operaciones asíncronas. Se escribirá el vocabulario del dominio en un glosario compartido para que el mismo concepto tenga el mismo nombre en todas partes.

### Gestionar la consistencia en entornos políglota con intención

En un repositorio que abarca varios lenguajes, se buscará la coherencia de conceptos (patrones de manejo de errores, estructura de registros, disposición del proyecto) aunque la sintaxis difiera. Se ofrecerán configuraciones por lenguaje desde un repositorio central, de modo que un servicio nuevo herede las normas automáticamente mediante plantillas o andamiajes de arranque.

### Codificar los patrones idiomáticos y los paradigmas

Hay que ir más allá del formato. Se documentarán los patrones idiomáticos preferidos: cómo se manejan los errores, cómo se estructuran los módulos, cuándo se usan excepciones en lugar de tipos de resultado, junto con los paradigmas que los equipos priorizan. Ahí es donde residen de verdad la legibilidad y la mantenibilidad.

## Compensaciones: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Formateador automático estricto, sin configuración | Acaba todo debate sobre formato; consistencia inmediata; incorporación trivial | Algunas decisiones impopulares son innegociables; el primer cambio genera un diff enorme |
| Linter configurable con reglas propias | Adaptado a las necesidades de la organización; permite codificar reglas reales de prevención de errores | Deriva de la configuración; debates estériles sobre reglas; carga de mantenimiento |
| Estándar comunitario adoptado tal cual | Familiar para los nuevos ingresos; ecosistema de herramientas potente; bajo mantenimiento | Puede no encajar con restricciones propias de la organización; ocasionales normas incómodas |
| Norma interna a medida | Se ajusta exactamente a la organización | Costoso de redactar y mantener; desconocido para los nuevos ingresos; herramientas limitadas |
| Autonomía por equipo | Alta moral local; contexto específico | Fragmentación; movilidad entre equipos dolorosa; herramientas inconsistentes |

Los defaults ejecutados automáticamente sacrifican algo de autonomía individual a cambio de grandes beneficios colectivos: menos fricción en la revisión, una incorporación más rápida y una automatización fiable. El principal riesgo consiste en sobreingeniar el estándar hasta acumular cientos de reglas que frenan a todos sin prevenir defectos reales. Conviene mantener el conjunto de reglas pequeño y basado en evidencia, y apoyarse en un estándar existente para que el mantenimiento siga siendo barato.

## Cuestiones para debatir en equipo

1. **¿Qué reglas del linter deben detener la compilación y cómo se promociona una regla de advertencia a error sin paralizar a todo el mundo?** Este capítulo sostiene que cada regla necesita un mecanismo de ejecución y que las nuevas deben llegar en modo de advertencia, liquidar su backlog y, solo entonces, pasar a error. En un equipo grande, activar una regla como error en un repositorio con deudas pendientes bloquea cientos de cambios no relacionados de la noche a la mañana. Hay que llevar a la reunión datos concretos: el número actual de incumplimientos de cada regla candidata y si es corregible automáticamente o requiere juicio humano. En entornos empresariales y gubernamentales, la línea de paso o fallo también alimenta los puntos de control de auditoría, de modo que un conjunto de reglas ambiguo debilita la postura de cumplimiento. Conviene planear un despliegue escalonado: corregir automáticamente lo que sea posible, presupuestar la limpieza y, entonces, habilitar el bloqueo.

2. **¿Al aplicar un formateador por primera vez al código heredado, cómo se evita que ese reformato destroce el historial de blame y ahogue las revisiones?** La tabla de compensaciones advierte del gran diff inicial y la sección de antipatrónes señala la mezcla de commits de reformato con cambios lógicos. Un reformato masivo reescribe miles de líneas y hace que el blame apunte al reformato en lugar del autor real, lo que perjudica a quien depura años después. El reformato debe realizarse como un commit aislado y claramente etiquetado, y registrarse en un archivo de ignorancia del blame para que el historial siga siendo útil. Para los auditores que rastrean quién cambió qué, ese aislamiento es la diferencia entre evidencia nítida y ruido. Hay que acordar el orden de ejecución antes de tocar el código, no después.

3. **¿Quién es responsable del glosario de nomenclatura y del vocabulario del dominio, y cómo se incorpora un término nuevo?** El capítulo califica la nomenclatura como la decisión de legibilidad de mayor impacto y pide que el vocabulario del dominio se escriba en un glosario compartido. Sin un responsable designado, el mismo concepto adopta tres nombres distintos en tres equipos, y las herramientas de análisis estático y de búsqueda pierden fiabilidad. Hay que llevar ejemplos de conceptos que ya tengan nombres conflictivos en el repositorio como señal concreta. Se asignará un único responsable y un camino de propuesta ágil, de modo que añadir o renombrar un término sea un cambio pequeño y revisado, no una discusión en cada solicitud de fusión. La respuesta cambia la incorporación: un nuevo ingeniero lee un solo glosario en lugar de deducir la intención a partir de código inconsistente.

4. **¿Se adopta al pie de la letra una guía de estilo comunitaria o del proveedor para cada lenguaje, y dónde se justifican de verdad las desviaciones propias?** Este capítulo sostiene que se tome un estándar existente como base y se documenten únicamente las desviaciones que la organización necesite, porque un estándar a medida es costoso de redactar y ajeno a los nuevos ingresos. La tensión opuesta es real: una restricción interna (una regla de seguridad, un marco heredado, una norma de accesibilidad) a veces entra genuinamente en conflicto con el estándar comunitario, y cada desviación que se mantiene es una regla que se hereda y se mantiene para siempre. Hay que llevar a la reunión la lista de desviaciones propuestas, cada una con la restricción concreta que la motiva, y estar dispuesto a descartar toda desviación que sea solo cuestión de gusto. En entornos empresariales y gubernamentales, una base que coincida con la comunidad del lenguaje también significa que los contratistas y los nuevos proveedores llegan ya fluentes, lo que acorta la incorporación y fortalece la evidencia de mantenibilidad que buscan los auditores.

5. **¿En un repositorio políglota, qué convenciones son verdaderamente universales y cuáles deben permanecer locales a cada lenguaje, y cómo se evita que las configuraciones por repositorio se dispersen?** El capítulo pide coherencia de conceptos (manejo de errores, estructura de registros, disposición del proyecto) entre lenguajes, aunque la sintaxis difiera, y que las configuraciones por lenguaje se sirvan desde un repositorio central para que los nuevos servicios hereden las normas automáticamente. La tensión es que imponer los patrones de un lenguaje a otro produce código forzado y no idiomático, mientras que dejar que cada equipo bifurque su propia configuración termina con que «la norma» no signifique nada. Hay que llevar un inventario de las configuraciones de linter y formateador por repositorio y un diff que muestre cuánto se han alejado ya entre sí, como señal concreta. En una gran organización con decenas de servicios, hay que decidir el mecanismo de distribución (plantillas, andamiajes, un paquete de configuración compartido) para que un cambio de regla se propague una sola vez en lugar de copiarse a mano en cada repositorio.

6. **¿Cuándo es legítimo desactivar una regla, quién revisa la supresión y cómo se evitan que las desactivaciones masivas vacíen la norma?** La sección de antipatrónes señala que la supresión masiva en línea es señal de que una regla es incorrecta o de que un equipo se ha rendido, pero una política rígida de «ninguna excepción» empuja a escribir peor código solo para satisfacer al linter. Hay que acordar un camino ligero: una supresión debe llevar una justificación, situarse en el alcance más estrecho posible y ser visible en la revisión en lugar de esconderse en un archivo de ignorancia global. Hay que llevar el conteo actual de supresiones por regla y por repositorio, porque una regla suprimida cientos de veces dice algo sobre la regla, no sobre el código. En el trabajo regulado y del sector público, las supresiones masivas sin justificación debilitan directamente el relato de auditoría, ya que el pipeline ya no puede demostrar que el código fusionado pasó genuinamente las puertas de control acordadas.

## Perspectiva por sector

**Startup.** La velocidad manda: el día uno se adopta el formateador y el linter comunitarios para el único lenguaje y se conectan en un gancho de precommit y en la CI antes de que llegue el segundo ingeniero. No se escriba un estilo propio que no haya tiempo de mantener: la configuración que viaja dentro del repositorio es la norma entera. Cuando se añada un segundo lenguaje, se buscará la guía canónica de ese lenguaje en lugar de inventar convenciones desde cero.

**Pequeña empresa.** Sin especialista en herramientas dedicado y con presupuesto ajustado, se confía por completo en el formateador gratuito y con criterio definido que viene con el lenguaje o junto a él, y se aceptan sus valores por defecto sin ajustarlos. Es un caso claro de comprar en lugar de construir: mantener un conjunto de reglas a medida cuesta tiempo que no se tiene, mientras que un formateador de mercado no cuesta nada y acaba el debate de estilo de inmediato. Se mantiene la configuración en el repositorio para que el siguiente contratista, el que se contrate el año próximo, la herede sin una sola conversación.

**Gran empresa.** A gran escala, la tarea es la gobernanza entre muchos equipos: un repositorio central de normas de ingeniería que alberga las configuraciones compartidas de formateador y linter por lenguaje, servicios nuevos generados desde plantillas que incorporan esas configuraciones y puertas de control en la CI que bloquean las fusiones no conformes. Se versiona el conjunto de reglas como código y se canalizan los cambios a través de una revisión periódica, de modo que las normas evolucionen de forma deliberada y no por deriva. La recompensa es que los ingenieros se mueven entre equipos a código familiar y que las herramientas automatizadas producen señal fiable porque todo repositorio es consistente.

**Sector público.** La contratación y la rendición de cuentas configuran la decisión: se establece un conjunto de normas de estilo y reglas de seguridad específico como parte de los requisitos de autorización para operar, y se hace que el pipeline emita un informe que muestre que cada cambio fusionado pasó las puertas de control acordadas, como evidencia de auditoría. Porque el formateador se aplica automáticamente, el código de varios proveedores y contratistas se ve uniforme, lo que protege la tarea de mantenimiento a largo plazo del sector público mucho después de que finalicen los contratos. Se priorizan las bases comunitarias reconocidas antes que reglas a medida, para que la norma sea transparente y cualquier proveedor futuro pueda adoptarla sin depender de un proveedor concreto.

## Ejemplos

**Startup.** Un equipo de cuatro personas adopta el formateador y el linter comunitarios de su único lenguaje el mismo día uno, conectándolos en un gancho de precommit y en la CI para que nadie discuta sobre espacios en una revisión. Como la configuración viaja dentro del repositorio, el quinto y el sexto ingreso lo heredan automáticamente y nunca ven un comentario de formato. Cuando el equipo añade más adelante un segundo lenguaje, recurre a la guía estándar de ese lenguaje en lugar de inventar un estilo propio que no tiene tiempo de mantener.

**Gran empresa.** Un gran banco gestiona servicios en Java, Python y TypeScript repartidos entre decenas de equipos. Publica un repositorio central de «normas de ingeniería» que alberga las configuraciones compartidas de formateador y linter para cada lenguaje. Los servicios nuevos se generan desde una plantilla que incorpora esas configuraciones, de modo que todo repositorio nace conforme. La CI bloquea las fusiones ante cualquier violación y una revisión trimestral gobierna los cambios de reglas. El tiempo de incorporación de los ingenieros que se mueven entre equipos se reduce notablemente, porque todo repositorio se ve familiar.

**Sector público.** Un organismo público que moderniza un sistema heredado establece un conjunto de reglas de accesibilidad y seguridad como parte de sus requisitos de autorización para operar (la aprobación formal necesaria para ejecutar el sistema en producción). El cumplimiento de estilo se convierte en parte de la evidencia de auditoría: el pipeline produce un informe que demuestra que todo el código fusionado pasó las puertas de [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis) acordadas. Como el formateador se aplica automáticamente, los contratistas de varios proveedores producen código visualmente coherente, lo que facilita la labor de mantenimiento a largo plazo del organismo una vez finalizados los contratos.

## Caso empresarial: motivaciones, retorno y coste total

El coste de adoptar normas es, en gran parte, único: elegir guías, conectar las herramientas y aplicar un gran commit inicial de reformato. El coste recurrente es bajo, porque la ejecución es automatizada. El coste de *no* adoptar normas es recurrente y compuesto: cada revisión pierde minutos en estilo, cada incorporación es más lenta, las herramientas de análisis estático producen ruido y el código inconsistente oculta defectos. En una gran organización, esos minutos se acumulan en pérdidas equivalentes a puestos a tiempo completo.

El retorno se manifiesta en una latencia de revisión menor, menos comentarios de revisión sobre estilo, una incorporación más rápida y una señal más alta de las herramientas automatizadas. En entornos regulados, hay un retorno adicional en la preparación para auditoría: controles demostrables y ejecutados reducen el esfuerzo y el riesgo de las revisiones de cumplimiento. Para presentar el caso a la dirección, conviene enmarcar las normas como una palanca de bajo coste y alto impacto sobre la productividad del desarrollador y la postura de auditoría, y poner un número al coste actual de la inconsistencia mediante el análisis de comentarios de revisión y datos de encuestas de incorporación.

## Antipatrónes y trampas

- **Estilo debatido en la revisión de código:** señal de que la ejecución no está automatizada; hay que trasladar la regla a una herramienta.
- **El documento de normas sin leer:** una página de wiki sin ejecución es una decoración; toda regla necesita un mecanismo.
- **Explosión de reglas:** cientos de reglas pedantes que frenan el trabajo sin prevenir defectos.
- **Deriva de configuración:** cada repositorio bifurca su propia configuración de linter hasta que «la norma» no significa nada.
- **Reformatear todo el repositorio en medio de un trabajo funcional:** mezclar commits de reformato con cambios lógicos destruye la revisión y el historial de culpa; los reformatos grandes deben hacerse en commits aislados y claramente etiquetados.
- **Ignorar el linter con supresiones masivas:** la desactivación en línea extendida es señal de que la regla es incorrecta o de que un equipo se ha rendido.
- **Normas sin dueño:** sin un responsable claro, las reglas nunca evolucionan y se degradan.

## Modelo de madurez

- **Nivel 1, Iniciar:** el estilo es individual y reactivo; no hay configuraciones compartidas; el formato se discute en la revisión y lo decide quien más le importe ese día.
- **Nivel 2, Desarrollar:** los equipos individuales adoptan un formateador y un linter, pero las configuraciones y los conjuntos de reglas varían de equipo a equipo y de repositorio a repositorio, de modo que la consistencia se detiene en el límite de cada equipo.
- **Nivel 3, Estandarizar:** hay configuraciones centrales compartidas por lenguaje, documentadas y ejecutadas en toda la organización; la CI bloquea las fusiones no conformes; los nuevos repositorios heredan las normas automáticamente mediante plantillas o andamiajes.
- **Nivel 4, Gestionar:** el estándar se mide y controla con datos: las tasas de violación, los conteos de supresión, los comentarios de revisión sobre estilo y el tiempo de incorporación se跟踪an contra líneas de base, y los cambios de regla se promocionan o retiran con base en esa evidencia, no en opiniones.
- **Nivel 5, Orquestar:** los estándares mejoran de forma continua y se integran en toda la organización; los patrones idiomáticos políglotas y el vocabulario del dominio están documentados y ejecutados, la ejecución es casi indolora y el conjunto de reglas se adapta a medida que evolucionan los lenguajes, las herramientas y las necesidades de la organización.

## Ideas para el debate

- ¿Dónde se traza la línea entre una regla ejecutada y una guía documentada que confía en el criterio del ingeniero?
- ¿Cómo debe manejar la organización una norma comunitaria muy apreciada que entra en conflicto con una restricción interna genuina?
- ¿Quién es dueño de los estándares y cómo se proponen, debaten y despliegan los cambios de reglas sin causar interrupciones?
- ¿En un repositorio políglota, qué convenciones deben ser verdaderamente universales y cuáles deben permanecer locales a cada lenguaje?
- ¿Cómo se aplican los estándares a un gran código heredado sin un reformato masivo disruptivo?
- ¿Qué papel deben jugar las herramientas asistidas por IA en la sugerencia o ejecución de patrones idiomáticos más allá del formato mecánico?

## Ideas clave

- Tratar el estilo como un problema automatizado y resuelto para que los humanos revisen diseño y corrección.
- Adoptar estándares comunitarios existentes y documentar únicamente las desviaciones.
- Ejecutar el control en las capas del editor, el precommit y la CI, con la CI como puerta de control definitiva.
- Mantener el conjunto de reglas pequeño, defendible y gobernado centralmente.
- La nomenclatura y los patrones idiomáticos, no los espacios, son donde se gana de verdad la legibilidad.

## Referencias y lecturas complementarias

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt y David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell y Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* y guías de estilo por lenguaje (como ejemplos de referencia)

