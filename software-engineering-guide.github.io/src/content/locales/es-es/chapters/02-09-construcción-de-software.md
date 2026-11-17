# 2.9 Construcción de software

## Resumen y motivación

La [construcción de software](https://en.wikipedia.org/wiki/Software_construction) es el punto en que el diseño se convierte en código en ejecución. Es el trabajo detallado de la codificación, la verificación, las [pruebas unitarias](https://en.wikipedia.org/wiki/Unit_testing), las [pruebas de integración](https://en.wikipedia.org/wiki/Integration_testing) y la [depuración](https://en.wikipedia.org/wiki/Debugging). La Guía del [Cuerpo de Conocimiento de la Ingeniería de Software](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) reconoce la construcción como un área de conocimiento autónoma, y con razón: aquí es donde se desarrolla la mayor parte del trabajo diario. Las decisiones que se toman línea a línea (cómo se contiene la complejidad, cómo se tratan los errores, con qué claridad se deja el código) determinan si un sistema podrá entenderse, modificarse y ser confiable durante años venideros.

En un equipo grande, la construcción es un esfuerzo colectivo, no una tarea solitaria. Cientos de ingenieros escriben en un mismo repositorio de código que sobrevivirá a la permanencia de cualquier persona en el equipo. Así que el listón no es «¿funciona en mi máquina hoy?». Es «¿podrá un desconocido modificarlo con seguridad dentro de cinco años?». La construcción conecta hacia arriba con los requisitos (capítulo 2.8) y el diseño (capítulo 2.2), que le dicen qué construir y cómo debe ser. Conecta a los lados con las normas de codificación (capítulo 2.1), las pruebas (capítulo 2.4) y la revisión de código (capítulo 2.5), que dan forma a cómo se expresa, se verifica y se inspecciona el trabajo. Una buena construcción convierte un diseño sólido en un activo mantenible. Una construcción deficiente convierte incluso el mejor diseño en una carga.

En entornos empresariales y de gobierno, la construcción tiene un peso especial. Estos sistemas son de larga vida, fuertemente regulados y a menudo críticos para la seguridad o para el ciudadano. La [programación defensiva](https://en.wikipedia.org/wiki/Defensive_programming), el tratamiento riguroso de errores y el código manifiestamente correcto no son concesiones; son requisitos de aseguramiento, auditoría y continuidad a lo largo de décadas y rotaciones de personal. El objetivo es código que comunique su intención, resista los fallos y pueda verificarse. Que el código simplemente funcione no basta.

## Principios fundamentales

- Minimizar la complejidad ante todo; el enemigo principal de la construcción a gran escala es el código que nadie puede comprender por completo.
- Anticipar el cambio; construir de modo que las modificaciones probables en el futuro queden localizadas y sean baratas de aplicar.
- Construir para la verificación; escribir código cuya corrección sea fácil de comprobar mediante pruebas, revisión y razonamiento.
- Reutilizar con criterio; construir sobre componentes existentes y confiables en lugar de reinventar, pero evitando acoplarse a las abstracciones equivocadas.
- Seguir normas; la coherencia en todo un repositorio reduce el costo cognitivo de cada cambio futuro.
- Tratar los errores y los estados inválidos de forma explícita; hacer visibles los modos de fallo en lugar de dejarlos en silencio.
- Mantener el código legible; la construcción es, ante todo, comunicación con quien lo mantendrá en el futuro, y en segundo lugar con el compilador.

## Recomendaciones

### Minimizar la complejidad como disciplina central

Haga de la reducción de la complejidad (tanto la esencial como la accidental) su objetivo primordial. Escriba funciones y módulos pequeños, de un solo propósito. Prefiera nombres claros a trucos ingeniosos. Mantenga la anidación superficial y el flujo de control lineal. Localice las decisiones de forma que comprender un fragmento de código no le obligue a sostener el sistema entero en la mente. La complejidad es lo que hace que los repositorios de gran tamaño sean lentos de modificar y peligrosos de tocar, así que valore cada elección según si añade complejidad o la elimina. Aplique los principios de diseño del capítulo 2.2 a pequeña escala también: alta cohesión, bajo acoplamiento y una clara [separación de responsabilidades](https://en.wikipedia.org/wiki/Separation_of_concerns) importan tanto en una sola función como en toda una arquitectura.

### Construir para el cambio y para la verificación

Piense de antemano en los cambios más probables (nuevas reglas de negocio, nuevas integraciones, nuevas regulaciones) e ísolelos tras interfaces estables para que el cambio se mantenga local. Al mismo tiempo, escriba código que sea fácil de verificar: [funciones puras](https://en.wikipedia.org/wiki/Pure_function) (mismas entradas siempre producen el mismo resultado, sin efectos secundarios) donde sea posible, estado oculto al mínimo y dependencias explícitas para que las pruebas puedan sustituirlas. El código que resulta difícil de probar suele ser, al mismo tiempo, difícil de entender y de cambiar. La probabilidad de prueba (capítulo 2.4) es una señal de diseño, no una preocupación exclusiva de control de calidad.

### Reutilizar con criterio y estandarizar

Recorra primero las librerías y componentes internos bien mantenidos antes de reescribir lógica fundamental, y úselos a través de interfaces claras (capítulo 2.3). Construya componentes reutilizables solo cuando exista un segundo caso de uso genuino, porque generalizar antes de tiempo es, en sí mismo, una forma de complejidad. Aplique de forma uniforme las normas de codificación y el estilo de su organización (capítulo 2.1), idealmente con formateadores y [analizadores de código](https://en.wikipedia.org/wiki/Lint_(software)) automatizados, de modo que todo el repositorio se lea como si un solo autor cuidadoso lo hubiera escrito.

### Programar de forma defensiva con criterio

Valide las entradas en los límites de confianza (peticiones externas, entrada y salida de archivos y red, datos del usuario) y trate todo lo que cruce esos límites como hostil hasta que se demuestre lo contrario. Sin embargo, dentro de un módulo bien probado, no ahogue cada línea con comprobaciones redundantes que oculten la lógica y silencien los fallos reales. La regla es sencilla: defiende en los límites, confía en su interior. Use [aserciones](https://en.wikipedia.org/wiki/Assertion_(software_development)) para documentar y aplicar invariantes que nunca deben ser falsas en un programa correcto. Use [excepciones](https://en.wikipedia.org/wiki/Exception_handling) y tratamiento de errores para condiciones que pueden ocurrir legítimamente en tiempo de ejecución. Mantenga ambos conceptos separados: las aserciones protegen suposiciones del programador; el tratamiento de errores gestiona los fallos esperados.

### Tratar los errores de forma explícita y fallar con seguridad

Para cada error, decida deliberadamente qué hacer: recuperar, reintentar, propagar o fallar rápido. Nunca trague una excepción en silencio ni ignore un código de retorno; un fallo suprimido regresa más adelante como un defecto misterioso. Incluya contexto en los mensajes de error y en los registros para que los fallos puedan diagnosticarse. En sistemas críticos para la seguridad o para el ciudadano, falle a un estado seguro y conocido en lugar de seguir operando en un estado corrupto. Dedique al camino de error el mismo pensamiento que al camino feliz, porque en producción es en el camino de error donde se gana o se pierde la confianza.

### Incorporar la calidad durante la construcción

La calidad se construye en el proceso, no se inspecciona después. Escriba pruebas unitarias junto con el código, ejecute [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis) y análisis de código de forma continua, y mantenga las funciones lo suficientemente pequeñas como para razonar sobre ellas. Use nombres que se expliquen por sí mismos y una estructura clara, para que sus comentarios expliquen el porqué, no el qué. [Refactorice](https://en.wikipedia.org/wiki/Code_refactoring) a medida que avanza para mantener el código habitable. La revisión de código (capítulo 2.5) es la red de seguridad humana, pero la mayor parte de la calidad debe estar presente antes de que la revisión siquiera comience.

### Elegir y estandarizar las herramientas de construcción

Estandarice el conjunto de herramientas (compiladores, sistemas de compilación, formateadores, analizadores, herramientas de análisis estático, depuradores, gestores de dependencias y configuraciones de entornos de desarrollo integrado) para que cada ingeniero trabaje en un entorno coherente y reproducible. Conecte estas herramientas en el flujo de trabajo para que las verificaciones de calidad no sean opcionales. Integre las herramientas de codificación asistida por IA de forma deliberada y trate su salida como un borrador que debe superar las mismas normas, revisiones y pruebas que cualquier otro código.

## Compensaciones: ventajas e inconvenientes

| Práctica | Ventajas | Inconvenientes |
|---|---|---|
| Minimización agresiva de la complejidad | Código legible, fácil de cambiar, bajo índice de defectos | Puede resultar lento; corre el riesgo de sobre-abstracción si se aplica mal |
| Comprobaciones defensivas extensas | Detección temprana de estados incorrectos, límites robustos | Sobrecarga la lógica; puede enmascarar defectos reales si se abusa |
| Aserciones para invariantes | Documenta y aplica suposiciones | Desactivadas en algunas compilaciones de producción; no sustituyen al tratamiento de errores |
| Reutilización intensiva de librerías | Menos código propio; entregas más rápidas | Riesgo de dependencias, acoplamiento, exposición en la cadena de suministro |
| Normas y análisis estrictos | Repositorio uniforme, de baja fricción | Costo inicial de configuración; puede resultar rígido para los individuos |
| Construir para la probabilidad de prueba | Código verificable y fácil de cambiar | Puede añadir una indirection que algunos perciben como ceremonia |

La compensación central en la construcción es la velocidad a corto plazo frente a la capacidad de cambio a largo plazo. Atajar los caminos (omitir el tratamiento de errores, tolerar la complejidad, ignorar las normas) se siente más rápido en el momento, y casi siempre resulta más caro a lo largo de la vida del sistema. El fracaso opuesto es la sobre-ingeniería: demasiada defensividad, abstracción especulativa y generalidad que nadie necesita. Una construcción competente se sitúa en el medio: tan simple como sea posible, tan defensiva como exijan los límites, y nada más.

## Preguntas para discutir con su equipo

1. **¿Cuál es la definición compartida y concreta de «demasiada complejidad» y dónde la hacemos cumplir antes de integrar?** «Minimizar la complejidad» es la disciplina central de la construcción, pero como eslogan pierde toda discusión ante un plazo de entrega. En un equipo grande, donde cientos de personas escriben en un mismo repositorio, la complejidad debe ser medible; por eso conviene acordar señales que se traduzcan en acción: longitud de funciones, profundidad de anidación, complejidad ciclomática y número de elementos que un lector debe sostener en la mente para comprender un cambio. Lleva al encuentro el peor infractor que tengan y pregúntese si su revisión actual habría detectado el problema. La respuesta debe convertirse en una puerta del flujo de trabajo o en un punto de la lista de revisión, porque un umbral aplicado por una herramienta vale más que un principio sostenido por la voluntad, y ahorra a su próximo incorporación la lenta acumulación de código que nadie se atreve a tocar.

2. **En producción, ¿los caminos de error se comportan como los diseñamos y cuándo los hemos ejercitado a propósito por última vez?** Las recomendaciones de construcción dicen que dedique al camino de error el mismo pensamiento que al camino feliz, y sin embargo el camino de error suele ser el código que menos se prueba. En un sistema crítico para el ciudadano o para la seguridad, es allí donde se gana o se pierde la confianza. Una excepción tragada o un código de retorno ignorado se convierte en semanas después en un defecto misterioso, y «fallar a un estado seguro» es una promesa que no puede cumplir si nunca ha visto cumplirse. Lleve el historial de incidentes: ¿cuántos cortes de servicio pasados se remontan a un error tragado o a un camino de recuperación sin probar? La acción concreta es probar los fallos a propósito (inyectar la tarjeta declinada, el tiempo agotado, la entrada malformada) y exigir que cada error sea manejado, registrado con contexto o propagado, nunca desechado en silencio.

3. **¿Qué partes del repositorio resultan difíciles de probar y qué nos dice esa dificultad sobre el diseño?** El código que se resiste a las pruebas suele esconder estado, acoplarse a las dependencias equivocadas o hacer demasiado a la vez, de modo que la probabilidad de prueba es una señal de diseño, no una preocupación de control de calidad que llega después. En un sistema empresarial de larga vida, esto importa porque los módulos que hoy resultan dolorosos de probar son los que un desconocido temerá modificar dentro de cinco años. Lleve la clase o el servicio al que su equipo teme escribir pruebas y pregúntese por qué: ¿hay estado oculto, ¿las dependencias son imposibles de sustituir, ¿la función cumple tres tareas a la vez? La respuesta debe orientar la refactorización hacia funciones puras, dependencias explícitas y unidades pequeñas de un solo propósito, porque hacer el código verificable es el mismo trabajo que hacerlo comprensible y barato de cambiar.

4. **¿Cuándo reutilizamos una librería externa y cuándo construimos la capacidad nosotros mismos, y quién asume el riesgo de cadena de suministro que eso implica?** Recurrir a una librería de confianza es más rápido que reinventar lógica fundamental, pero cada dependencia que se añade es código que no se controla, no se audita con facilidad y debe parchearse el día en que se compromete. En un equipo grande, el peligro es que cien ingenieros traen cada uno sus propias dependencias transitivas hasta que nadie puede decir con certeza qué ejecuta realmente el repositorio. Lleve el inventario de dependencias y pregunte tres cosas concretas: cuántas librerías están sin mantenimiento, cuántas llevan vulnerabilidades conocidas y cuántas envuelven lógica tan simple que conviene poseerla. La consideración contraria es real, porque escribir la propia criptografía o el propio manejo de fechas casi siempre es peor que usar una librería contrastada, de modo que el objetivo es una política de reutilización deliberada y no la evitación en bloque. En entornos empresariales y de gobierno, añada la dimensión de la contratación y el cumplimiento de licencias, porque una dependencia no revisada puede arrastrar una licencia incompatible con las obligaciones o una procedencia que ningún auditor aceptará.

5. **¿Cómo sometemos el código generado por IA a las mismas normas de construcción que el código escrito por humanos y cómo distinguimos ambos cuando importa?** Los asistentes de codificación por IA producen borradores plausibles con rapidez, y la tentación es tratar su salida como terminada porque compila y luce idiomática. La norma del capítulo es que el código generado supera las mismas revisiones, pruebas y normas que cualquier otro, y un equipo grande debe hacer operativa esa regla y no aspiracional. Lleva ejemplos de cambios asistidos por IA que se integraron recientemente y pregúntese si cada uno traía pruebas, superó el análisis estático y fue verdaderamente comprendido por el humano que lo envió, o si se dejó pasar por confianza. La presión contraria es la velocidad, porque estos asistentes son genuinamente productivos y frenar cada sugerencia hasta detenerse se echa a perder la ventaja. En contextos regulados y de gobierno, añada la dimensión de la procedencia y la rendición de cuentas, porque puede ser necesario atestiguar quién responde de una línea de código y si un fragmento generado arrastra una cuestión de licencia o de derechos de autor que no puede resolverse.

6. **¿El conjunto de herramientas de construcción está realmente estandarizado y aplicado en el flujo de trabajo, o los individuos siguen trabajando con configuraciones incompatibles?** Un conjunto de herramientas compartido (formateador, analizador, herramienta de análisis estático, sistema de compilación y gestor de dependencias) permite a un ingeniero moverse con seguridad entre servicios que no conoce, porque el código suena a una sola voz y las verificaciones son idénticas en todas partes. Cuando hay deriva, cada equipo reinventa su propia configuración, el tiempo de revisión se consume en debates de estilo y los defectos que el analizador de un equipo habría detectado se escapan en otro. Lleve la lista de repositorios que no ejecutan las verificaciones estándar en cada envío y pregúntese por qué cada uno se eximió. La tensión es que un esquema único puede resultar rígido para equipos con necesidades genuinamente distintas, así que decida dónde la uniformidad justifica la fricción y dónde una excepción documentada es aceptable. Para una gran empresa o un organismo público, vincule esto con la reproducibilidad y la auditoría, porque una compilación que no puede reproducirse a nivel de byte desde un conjunto de herramientas controlado es una que no podrá defenderse ante un evaluador años después.

## Perspectiva por sector

**Startup.** La velocidad manda, así que instale un formateador y un analizador compartido desde el primer día, valide las entradas en su único límite externo y mantenga la lógica interna limpia en lugar de defensiva en cada línea. Omita la abstracción especulativa y los procesos pesados: con dos o tres ingenieros, todo el equipo sostiene el repositorio en su cabeza y el riesgo real es la complejidad que sobrevive a esa memoria compartida. Apóyese en librerías de confianza para todo lo que sea fundamental, para escribir el mínimo de código que pueda poseer bien.

**Pyme.** Sin ingeniero de compilación dedicado y con un presupuesto ajustado, prefiera convenciones que las herramientas existentes apliquen de forma gratuita: un formateador y un analizador que vengán con el lenguaje, valores por defecto sensatos y un pequeño conjunto de reglas que todos puedan recordar. Adquiera o adopte librerías bien mantenidas en lugar de construir infraestructura que no pueda sostener. Destine su disciplina limitada a las dos cosas que más duelen cuando se descuidan: validar la entrada en el límite y nunca tragar un error en silencio.

**Empresa.** Con cientos de ingenieros escribiendo en código compartido, la prioridad es la uniformidad y la aplicación: un conjunto de herramientas estandarizado conectado al flujo de trabajo, puertas de análisis estático y reglas de validación en los límites aplicadas en todas partes para que las personas se muevan con seguridad entre servicios. Gestione el riesgo de dependencias y de cadena de suministro como un proceso gobernado, no como improvisación de cada equipo, y use aserciones para codificar invariantes de dominio que deben mantenerse en todos los equipos. Trate las normas de construcción como el sustrato que mantiene un repositorio habitable a lo largo de décadas y rotaciones de personal.

**Sector público.** Los sistemas de larga vida y críticos para el ciudadano convierten la construcción disciplinada en asunto de aseguramiento y rendición de cuentas. Aísle las reglas volátiles, como la legislación, tras interfaces estables para que los cambios se mantengan locales y sean trazables hacia los requisitos. Valide de forma defensiva toda entrada que toque al ciudadano. Que los caminos de error fallen a un estado seguro que nunca emita una evaluación incorrecta en silencio. Cada módulo se entrega con pruebas unitarias que sirvan como evidencia de auditoría. Dado que la construcción es estandarizada y bien documentada, nuevos funcionarios públicos pueden mantener con seguridad código escrito por predecesores que abandonaron el cargo hace tiempo.

## Ejemplos

**Startup.** Un equipo de tres ingenieros en una startup configura un formateador y un analizador compartidos desde el primer día y los ejecuta en cada envío, de modo que el repositorio suena a una sola voz incluso al incorporar contratados. Valida las entradas en el límite de su API y trata todo lo que llega del exterior como hostil, pero mantiene la lógica interna limpia en lugar de ahogarla en comprobaciones redundantes. Cuando un webhook de pagos empieza a fallar, la corrección es rápida porque ninguna excepción se tragó en silencio y el mensaje de error incluye contexto suficiente para señalar la causa directamente. Todo el conjunto se configuró en una tarde y les ahorró la lenta acumulación de complejidad que habría convertido la primera semana de su próximo incorporación en un calvario.

**Empresa.** Una compañía global de pagos aplica un conjunto de herramientas compartido entre cientos de ingenieros: formateo y análisis automáticos en cada envío, puertas de análisis estático en el flujo de trabajo y una norma de que todas las entradas externas se validan en los límites de servicio. La lógica de dominio usa aserciones para aplicar invariantes como «una entrada del libro mayor siempre equilibra», mientras que condiciones de ejecución como una tarjeta declinada se tratan como resultados explícitos y registrados. Como las normas son uniformes y los errores nunca se tragan en silencio, los ingenieros se mueven con seguridad entre servicios desconocidos y los incidentes en producción pueden diagnosticarse directamente desde los registros.

**Sector público.** Una agencia fiscal nacional construye un sistema de liquidación de larga vida, concebido para operar durante décadas bajo una legislación cambiante. La construcción aísla cada regla fiscal tras una interfaz estable, de modo que los cambios legislativos anuales se mantienen locales y son trazables hacia los requisitos (capítulo 2.8). La validación defensiva protege toda entrada que toca al ciudadano. Los caminos de error fallan a un estado seguro que nunca emite una liquidación incorrecta en silencio. Cada módulo se entrega con pruebas unitarias que doblan como evidencia de auditoría. Gracias a que la construcción es estandarizada y bien documentada, nuevos funcionarios públicos pueden mantener con seguridad el código que escribieron predecesores que ya no están.

## Justificación de negocio: motivaciones, retorno y costo total de propiedad

El retorno de una construcción disciplinada es la capacidad perdurable de modificar software de forma barata y segura, y es allí donde se decide la mayor parte del costo total de propiedad de un sistema. Los estudios de la economía del software muestran de forma consistente que la mayor parte del costo de vida de un sistema es el de mantenimiento, y que ese costo lo domina la comprensibilidad y la maleabilidad del código. Minimizar la complejidad, tratar los errores de forma explícita y seguir normas reduce directamente el costo de cada cambio futuro y de cada incidente en producción.

El costo de adoptar es modesto y en su mayor parte inicial: se fijan las normas, se conectan los analizadores y las herramientas de análisis estático, y se forma el hábito de escribir código verificable y defensivo. El costo de la negligencia, en cambio, se acumula. La complejidad se deposita hasta que el código se vuelve lento de cambiar y arriesgado de tocar. Los errores silenciosos se convierten en incidentes de producción caros. El estilo inconsistido multiplica el esfuerzo de cada revisión y de cada incorporación. Para presentar el caso ante la dirección, vincule la calidad de la construcción con la tasa de fallo por cambios, el tiempo medio de recuperación, la tasa de defectos que escapan y el tiempo de incorporación, todos ellos mejorados de forma directa por la disciplina de construcción.

## Antipatrrones y errores frecuentes

- **Arrastre de complejidad:** acumular código ingenioso, fuertemente anidado o disperso hasta que nadie lo comprende.
- **Tragar errores en silencio:** bloques de captura vacíos y códigos de retorno ignorados que convierten los fallos en misterios futuros.
- **Exceso de programación defensiva:** comprobaciones redundantes por todas partes que enterran la lógica y enmascaran defectos reales.
- **Confundir aserciones con tratamiento de errores:** usar aserciones para condiciones de tiempo de ejecución o excepciones para invariantes del programador.
- **Construcción por copia y pega:** duplicar lógica en lugar de reutilizarla, de modo que una corrección debe aplicarse en muchos sitios.
- **Generalidad especulativa:** construir abstracciones y configurabilidad para necesidades que nunca llegan.
- **Ignorar las normas:** cada ingeniero codifica a su manera, multiplicando la carga cognitiva en todo el repositorio.
- **Construcción sin pruebas:** escribir código sin pruebas que lo acompañen, posponiendo la verificación a una fase que nunca llega.

## Modelo de madurez

- **Nivel 1 (Iniciación):** La construcción es ad hoc y reactiva; la complejidad y el tratamiento de errores varían según la persona; hay pocas normas y los fallos silenciosos son frecuentes.
- **Nivel 2 (Desarrollo):** Existen normas de codificación, formateadores y analizadores, y se espera un tratamiento básico de errores y pruebas unitarias, pero la práctica es irregular y cada equipo la aplica de forma distinta.
- **Nivel 3 (Estandarización):** La minimización de la complejidad, la validación en los límites, el tratamiento explícito de errores y la probabilidad de prueba están documentados y aplicados a nivel de organización, en el flujo de trabajo y en la revisión, de modo que todo el repositorio se lee como si un solo autor cuidadoso lo hubiera escrito.
- **Nivel 4 (Gestión):** La calidad de la construcción se mide frente a líneas base; el equipo sigue la complejidad ciclomática, la tasa de defectos que escapan, la tasa de fallo por cambios, la cobertura del camino de error y los hallazgos de la revisión, y actúa sobre las tendencias y no sobre opiniones.
- **Nivel 5 (Orquestación):** La construcción mejora de forma continua y se integra en toda la organización; los patrones defensivos, las normas y las métricas alimentan la refactorización y las herramientas; los asistentes de IA operan bajo las mismas puertas de calidad, y la práctica se adapta a medida que cambian los lenguajes, las regulaciones y los riesgos.

## Ideas para la discusión

- ¿Dónde se acumula la complejidad accidental en su repositorio y qué hábitos de construcción la generan?
- ¿Cuál es la regla real de su equipo para dónde validar la entrada y dónde confiar en ella?
- ¿Distinguen sus ingenieros las aserciones del tratamiento de errores y es esa distinción coherente?
- ¿Cuánta de su calidad se construye durante la construcción y cuánta se detecta después, en la revisión o en las pruebas?
- ¿Cómo decide cuándo reutilizar una librería y cuándo construir la capacidad, teniendo en cuenta el riesgo de cadena de suministro?
- ¿Cómo debe someterse el código generado por IA a las mismas normas de construcción que el código escrito por humanos?

## Ideas clave

- La construcción es donde el diseño se convierte en código mantenible; minimizar la complejidad es su disciplina central.
- Construir para el cambio y para la verificación: el código probable de prueba es código comprensible.
- Defienda en los límites, confíe en su interior y nunca trague un error en silencio.
- Use aserciones para invariantes y tratamiento de errores para condiciones esperadas en tiempo de ejecución; no confunda ambos.
- Estandarice herramientas y estilo, reutilice con criterio y construya la calidad en el proceso en lugar de inspeccionarla después.

## Referencias y lecturas complementarias

- IEEE Computer Society, *SWEBOK Guide (Guía del Cuerpo de Conocimiento de la Ingeniería de Software)*, área de conocimiento de Construcción de Software
- Steve McConnell, *Code Complete: Un manual práctico de construcción de software*
- Robert C. Martin, *Clean Code: Un manual de artesanía ágil para el desarrollo de software*
- Andrew Hunt y David Thomas, *The Pragmatic Programmer: Desarrollo de software más allá de los límites*
- Martin Fowler, *Refactoring: Mejorar el diseño del código existente*
- John Ousterhout, *A Philosophy of Software Design*

