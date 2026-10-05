# 4.5 Privacidad y protección de datos

## Visión general y justificación

La seguridad protege los datos frente a accesos no autorizados. La privacidad plantea una pregunta distinta: ¿deberías estar recopilando, utilizando y conservando esos datos en primer lugar, y las personas a quienes se refieren tienen alguna voz al respecto? Ambas áreas se solapan, pero no son lo mismo. Es posible lograr una seguridad impecable y, aun así, vulnerar la privacidad. Lo haces al acumular datos que no tienes derecho a retener, utilizarlos con finalidades a las que nadie ha consentido o trasladarlos entre fronteras de un modo que la ley prohíbe. En equipos de gran envergadura, la privacidad es una restricción de diseño: afecta a todo servicio que maneja información personal, y hoy eso significa prácticamente todos.

Las consecuencias son graves y van en aumento. La regulación en materia de privacidad se ha extendido a todo el mundo, con multas proporcionales a la facturación y con derechos exigibles que las personas pueden ejercer sobre sus datos. Para las grandes empresas, un mal manejo de los datos personales conlleva acciones regulatorias, demandas colectivas y la pérdida de la confianza del cliente, algo costoso de reconstruir. Para el sector público, la responsabilidad es aún mayor: los ciudadanos no pueden elegir otro proveedor para sus datos de fiscalidad, sanidad o prestaciones, de modo que el Estado les debe una obligación de cuidado especial. Y las filtraciones de datos erosionan la confianza pública de la que la administración depende.

Este capítulo aborda la privacidad como una disciplina de ingeniería. Abordamos el diseño de la privacidad desde el origen, la minimización y la conservación responsable de los datos, la clasificación y protección de categorías sensibles como la [información de identificación personal](https://en.wikipedia.org/wiki/Personally_identifiable_information) (IIP) y la [información de salud protegida](https://en.wikipedia.org/wiki/Protected_health_information) (ISP), el manejo del consentimiento y de la base jurídica, y la gestión de las transferencias transfronterizas y los requisitos de residencia de datos que cada vez condicionan más la arquitectura.

*Véase también:* capítulo 4.6 (cumplimiento y gobernanza), capítulo 7.1 (estrategia y gobernanza de datos) y capítulo 4.1 (fundamentos y cultura de seguridad).

## Principios clave

- **[Privacidad por diseño](https://en.wikipedia.org/wiki/Privacy_by_design) y por defecto.** Intégrala desde el inicio y establece que la configuración más protectora de la privacidad sea la predeterminada.
- **[Minimización de datos](https://en.wikipedia.org/wiki/Data_minimization).** Recopila solo lo que realmente necesitas, consérvalo el tiempo que estrictamente haga falta y compártelo únicamente en la medida necesaria.
- **Limitación de la finalidad.** Utiliza los datos solo para las finalidades concretas que se expusieron al recopilarlos.
- **Base jurídica válida.** Cuenta con una justificación legal legítima para cada actividad de tratamiento.
- **Derechos de las personas.** Respeta los derechos de acceso, rectificación, supresión y portabilidad que tienen sobre sus datos.
- **Transparencia.** Informa de forma clara y accesible qué datos se recogen, para qué y con quién se comparten.
- **Responsabilidad rendida.** Debes poder *demostrar* el cumplimiento, no simplemente *afirmarlo*.

## Recomendaciones

### Diseñar la privacidad desde el origen

La privacidad que se añade como un aditamento a un sistema ya terminado resulta costosa e incompleta. Intégrala desde el principio.

- Realiza **Evaluaciones de Impacto en la Protección de Datos (EIPD)** para todo sistema o funcionalidad nueva que trate datos personales a gran escala o conlleva un riesgo elevado, identificando y mitigando los riesgos de privacidad antes de empezar a desarrollar.
- Establece por defecto configuraciones protectoras de la privacidad: consentimiento previo y voluntario para todo tratamiento no esencial, el mínimo de campos de datos y el menor plazo de conservación razonable.
- Involucra a especialistas en privacidad desde la fase de diseño, junto con el modelado de amenazas de seguridad, para que ambos aspectos se consideren en la etapa de definición de los límites de confianza.
- Mantén un **mapa o inventario de datos**: qué datos personales posees, dónde se almacenan, con qué finalidad y hacia dónde fluyen. No puedes proteger ni rendir cuentas de datos que no eres capaz de ver.

### Minimizar, conservar y eliminar con responsabilidad

Cada dato personal que retienes es una responsabilidad tanto como un activo.

- **Minimiza la recopilación:** cuestiona cada campo. Si no lo necesitas para una finalidad declarada, no lo recopiles.
- **Define plazos de conservación** por tipo de dato y por finalidad, y aplícalos mediante eliminación automatizada. Los datos que se guardan «por si acaso» son datos que esperan a ser filtrados o requeridos por una orden judicial.
- **Garantiza el derecho a la supresión:** diseña la capacidad de localizar y eliminar los datos de una persona en todos los sistemas, incluidos los respaldos y las copias descendentes, dentro de los plazos legales. Esto es mucho más viable si se integra desde el diseño que si se añade a posteriori.
- **[Anonimiza](https://en.wikipedia.org/wiki/Data_anonymization) o agrega** los datos destinados a análisis y pruebas, para que la información identificable no se propague a entornos secundarios.

### Clasificar y proteger los datos sensibles

No todos los datos personales conllevan el mismo nivel de riesgo, y algunas categorías tienen un peso jurídico especial.

- Clasifica los datos en niveles, distinguiendo la **IIP** (información de identificación personal), la **ISP** (información de salud protegida), los datos financieros y las categorías especiales (como etnia, religión, salud, datos biométricos u orientación sexual), que gozan de una protección jurídica reforzada.
- Aplica un nivel de protección proporcional a la sensibilidad: controles de acceso más estrictos, cifrado y monitorización reforzada para los niveles más sensibles.
- Utiliza la **[tokenización](https://en.wikipedia.org/wiki/Tokenization_(data_security))** para sustituir valores sensibles (como números de tarjeta o identificadores nacionales) por tokens no sensibles, reduciendo el número de sistemas que acceden a los datos crudos y, con ello, el alcance del cumplimiento normativo.
- Aplica la **[seudonimización](https://en.wikipedia.org/wiki/Pseudonymization)** para separar los identificadores del resto del registro, de modo que los datos sean menos directamente atribuibles, reduciendo el riesgo y conservando al mismo tiempo su utilidad.
- Oculta los datos sensibles en registros, mensajes de error, análisis y entornos no productivos.

### Manejar el consentimiento y la base jurídica de forma correcta

Tratar datos personales exige una base jurídica válida, y el consentimiento es solo una de varias.

- Identifica y documenta la **base jurídica** de cada actividad de tratamiento: consentimiento, ejecución de un contrato, obligación legal, interés vital, misión de interés público o interés legítimo, según el régimen aplicable.
- Cuando la base jurídica sea el consentimiento, asegúrate de que sea **libre, específico, informado e inequívoco**, con un mecanismo de retirada tan sencillo como el de concesión. Las casillas preseleccionadas y el consentimiento global no son válidos.
- Registra el consentimiento: qué aceptó la persona, cuándo y en qué términos, para que puedas demostrarlo.
- Respeita la **limitación de la finalidad**: no reutilices datos para una finalidad incompatible con la que motivó su recogida sin obtener una base jurídica nueva.
- Respeta señales como [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) y las solicitudes de baja allí donde la lo exige.

### Gestionar la transferencia transfronteriza y la residencia de datos

Dónde residen y circulan físicamente los datos es hoy una preocupación arquitectónica de primer orden.

- Conoce los requisitos de **residencia de datos**: algunas jurisdicciones exigen que ciertos datos permanezcan dentro de las fronteras nacionales, y algunos datos públicos deben alojarse en entornos soberanos o acreditados.
- Para las **transferencias transfronterizas**, asegúrate de que existe un mecanismo jurídico válido (decisiones de adecuación, cláusulas contractuales tipo o equivalente) y de que está documentado.
- Diseña la arquitectura desde el principio para garantizar la residencia: almacenamiento anclado a regiones, localización de datos y un control riguroso de dónde fluyen los respaldos, los registros y los datos de análisis, ya que estos suelen trasladar datos a otras fronteras sin que nadie lo note.
- Controla a los subprocesadores y terceros: un proveedor que traslade datos al extranjero puede incumplir tus obligaciones de residencia a tu nombre.

## Compromisos: ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| Minimización agresiva de datos | Menor riesgo, menor impacto ante una fuga, cumplimiento más sencillo | Puede limitar los análisis y las opciones futuras de producto |
| Conservación prolongada | Historial rico para análisis, ML y resolución de disputas | Mayor responsabilidad legal, mayor exposición ante filtraciones, complejidad en la eliminación |
| Tokenización | Reduce el alcance del cumplimiento normativo, protege los datos crudos | Añade complejidad al sistema; exige un almacén de tokens seguro |
| Configuración por consentimiento previo | Mayor confianza, cumplimiento inequívoco | Menor volumen de datos, métricas de crecimiento más difíciles de alcanzar |
| Residencia regional de datos | Cumple los mandatos legales, refuerza la confianza en la soberanía | Complejidad arquitectónica, mayor coste, infraestructura duplicada |
| Lago de datos centralizado | Potencia analítica, fuente única | Riesgo concentrado, dificultad para aplicar la limitación de la finalidad |

La tensión fundamental es entre la inclinación del negocio por acumular datos y la responsabilidad legal que esos datos representan. Los equipos de producto y análisis tienden a recopilar más y a conservar durante más tiempo. La disciplina de la privacidad tira en la dirección opuesta. La resolución madura consiste en replantear el dato como una responsabilidad que debe justificarse, no como un activo que hay que acumular. Cada decisión de recopilación y de conservación debe justificar el riesgo que genera. La residencia de datos añade una dimensión de coste frente a cumplimiento: atender a los requisitos de soberanía puede multiplicar la infraestructura, pero en algunos mercados y en el contexto público es simplemente innegociable.

## Preguntas para debatir con tu equipo

1. **¿Cuál es el plazo de conservación de cada categoría de datos personales y qué mecanismo garantiza la eliminación?** Los datos que se guardan «por si acaso» son datos que esperan a ser filtrados o requeridos por una orden judicial; cada campo y cada registro debe tener un ciclo de vida definido, atado a su finalidad. Fija los plazos por tipo de dato y aplícalos mediante eliminación automatizada, no confiando en que nadie recuerde hacerlo. Para una gran empresa, esto reduce a la vez la exposición ante una fuga y el coste de almacenamiento; para el sector público, se alinea con la obligación legal de no retener los datos de los ciudadanos más allá de lo que la ley permite. Trae una muestra de los registros más antiguos que conservas y pregunta quién los sigue necesitando y bajo qué base; la respuesta honesta suele ser que nadie. Si la eliminación es manual o inexistente, los datos se acumulan indefinidamente y tu responsabilidad legal crece en silencio en el balance.

2. **¿Qué campos sensibles puedes tokenizar o seudonimizar para reducir a la vez el riesgo y el alcance del cumplimiento normativo?** Sustituir números de tarjeta o identificadores nacionales por tokens confina los valores crudos a un almacén reducido y de control estricto, lo que reduce drásticamente los sistemas en alcance de auditorías como PCI-DSS. La seudonimización separa los identificadores del resto del registro, bajando el riesgo y manteniendo la utilidad para análisis y pruebas. Decide qué valores de alta sensibilidad justifican un almacén de tokens (a pesar de la complejidad añadida y la necesidad de protegerlo) y cuáles bastan con un enmascarado en registros y entornos no productivos. Trae un mapa de dónde fluyen hoy los valores sensibles en su forma cruda, porque cada sistema que los toca es un sistema que debes proteger y auditar. Para datos regulados o del sector público, esta reducción de alcance es una de las pocas medidas que abarata y protege a la vez, así que prioriza los campos más sensibles.

3. **Antes de que se lance tu próxima funcionalidad, ¿qué la obliga a someterse a una Evaluación de Impacto en la Protección de Datos y quién es el responsable de realizarla?** La privacidad que se añade a posteriori a un sistema terminado resulta costosa e incompleta; por eso una EIPD debe llevarse a cabo a tiempo, junto con el modelado de amenazas de seguridad, cuando el diseño todavía se puede modificar con escaso coste. Define el disparador (nuevo tratamiento a gran escala, datos de categorías especiales, una finalidad nueva) y asigna una persona responsable para que no se pierda entre las presiones de entrega. Una EIPD rigurosa puede detectar una recopilación excesiva antes del lanzamiento: por ejemplo, sustituir la ubicación precisa por la zona aproximada sin pérdida de producto. Trae una funcionalidad inminente y recórrela: qué datos personales recopila, por qué, y si un diseño menos intrusivo consigue el mismo objetivo. En servicios públicos de los que los ciudadanos no pueden prescindir, esta verificación anticipada forma parte de la obligación de cuidado: debe ser un punto de control, no una consideración de última hora.

4. **Cuando los datos personales cruzan una frontera (incluidos a través de respaldos, registros y subprocesadores) , ¿qué mecanismo jurídico cubre cada cruce y puedes demostrarlo?** Las normas de residencia y de transferencia condicionan hoy la arquitectura tanto como cualquier requisito de rendimiento, y los cruces que sorprenden a los equipos rara vez son los obvios: un registro enviado a una herramienta de observabilidad extranjera, un respaldo replicado a una región más barata o un subprocesador que, en silencio, transfiere datos al extranjero. En una gran organización las presiones opuestas son reales, porque la infraestructura anclada a regiones cuesta más y duplica operaciones, pero una sola transferencia ilegal puede invalidar la entrada en un mercado o desencadenar una orden de ejecución. Trae un mapa actual de flujos de datos que identifique cada lugar donde los datos personales reposan o viajan físicamente, el mecanismo jurídico aplicable a cada frontera que cruzan (decisión de adecuación, cláusulas contractuales tipo o equivalente) y la lista de subprocesadores con su ubicación. En contextos públicos o de datos soberanos, trata la residencia como una restricción arquitectónica innegociable y no como una cláusula contractual: hay registros que jamás pueden salir de entornos nacionales acreditados, y la entidad responsable no puede delegar esa obligación en un proveedor.

5. **¿Qué base jurídica sustenta cada actividad de tratamiento y podrías defender esa elección ante un regulador mañana?** El consentimiento es solo una de varias bases jurídicas, y muchos equipos recurren a él por defecto cuando el contrato, la obligación legal, la misión de interés público o el interés legítimo serían opciones más honestas y sostenibles. A gran escala esto importa, porque una base débil o inadecuada puede invalidar todo un flujo de datos, y desentramar un tratamiento que no tenías derecho a realizar es infinitamente más costoso que elegir la base correcta desde el principio. Weigh los factores en abierto: el consentimiento otorga control a las personas, pero puede retirarse y debe ser libre, específico y no agrupado; el interés legítimo, en cambio, evita la fatiga del consentimiento, pero exige un análisis de ponderación documentado. Trae un registro que asocie cada actividad de tratamiento con su base jurídica declarada, la evidencia que la respalda y cómo procederías si la retiraras o la cambiaras ante un cuestionamiento. En el sector público, la mayor parte del tratamiento esencial se sustenta en la misión de interés público más que en el consentimiento, así que delimita con precisión dónde comienza el consentimiento opcional y revocable, porque confundir ambos erosiona la confianza que los ciudadanos no pueden evitar extender.

6. **Si una persona ejerciera hoy su derecho de acceso, supresión o portabilidad, ¿podrías cumplirlo en todos los sistemas dentro del plazo legal?** Los derechos individuales son fáciles de prometer en una política de privacidad y difíciles de cumplir en una arquitectura que ha dispersado copias de datos personales por respaldos, cachés, almacenes analíticos y servicios descendentes. Para un gran equipo, este es el momento en que el cumplimiento abstracto se convierte en una prueba concreta de ingeniería: un plazo legal incumplido es tanto una incidencia notificable como una señal de que no eres capaz de ver tus propios datos. El factor compensatorio es el coste y la complejidad, porque construir una eliminación y una exportación genuinas entre sistemas es un trabajo real, pero la alternativa es un cumplimiento manual, lento, propenso a errores, que no escala y que, en la práctica, incumple la ley. Realiza un recorrido honesto de una solicitud real, desde su recepción hasta su cierre, incluyendo cómo se alcanzan los respaldos y los terceros, y cronómétralo contra el plazo legal. En servicios públicos de los que la ciudadanía no puede irse, considera el cumplimiento de derechos autoasistido, completo y auditable como parte de la obligación de cuidado, no como una funcionalidad para programar más adelante.

## Perspectiva por sector

**Emprendimiento.** Con un equipo pequeño y poco capital de maniobra, trata la privacidad como un seguro barato, no como un programa que no puedes sostener. Recopila solo los campos que tu funcionalidad central necesita, mantén un inventario de datos en una hoja de cálculo sencilla para que puedas responder de verdad a una solicitud de supresión y mantén correos electrónicos y tokens fuera de los registros. Un flujo de consentimiento claro y una supresión real te costarán una tarde; adaptarlos a posteriori, tras la primera demanda de un cliente empresarial o de un regulador, costará muchísimo más, y los datos recopilados en exceso son una responsabilidad de la que no obtienes nada a cambio de retenerlos.

**Pequeña empresa.** Sin un especialista en privacidad y con un presupuesto ajustado, apóyate en los controles de privacidad ya integrados en las herramientas que adquieres y prefiere proveedores que ofrezcan transparencia en el manejo de datos y claridad sobre la residencia. Encuadra la decisión como comprar frente a construir: casi nunca vas a desarrollar tokenización ni cumplimiento de derechos por tu cuenta, así que elige plataformas que ofrezcan reglas de conservación, exportación y supresión de serie. Conoce qué datos personales posees y dónde un registro erróneo o perdido te costaría un cliente, y documenta una base jurídica para cada uso, aunque el documento sea breve.

**Gran empresa.** A gran escala, el problema es la coherencia entre muchos equipos: un mapa de datos compartido, niveles de clasificación estandarizados y conservación aplicada de forma obligatoria, para que ningún grupo se convierta en el eslabón débil. Asigna presupuesto de ingeniería de forma explícita para la supresión entre sistemas, los almacenes de tokens y la arquitectura consciente de la residencia, y gestiona los subprocesadores de forma centralizada para que un solo proveedor no pueda incumplir una obligación de transferencia en tu nombre. Integra las EIPD como punto de control en el proceso de entrega y mide tu postura en materia de privacidad, porque auditores y reguladores te pedirán que demuestres el cumplimiento, no que lo afirmes.

**Sector público.** Las reglas de contratación, los deberes de transparencia y la rendición de cuentas pública condicionan cada decisión, y como los ciudadanos no pueden trasladar sus datos de fiscalidad, sanidad o prestaciones a otro lugar, la obligación de cuidado es más exigente. Ancla los registros sensibles en entornos nacionales acreditados, incluidos los respaldos y los datos de análisis; vincula a cada proveedor contractualmente a las mismas obligaciones de residencia y supresión; y documenta una base jurídica (normalmente la misión de interés público) para el tratamiento esencial, reservando los usos opcionales a un consentimiento separado y revocable. Publica descripciones en lenguaje claro de qué datos se recogen y por qué, y garantiza que el cumplimiento de los derechos se realiza de forma fiable dentro de los plazos estatutarios, porque una falla de privacidad en el sector público corroe la confianza pública de la que el servicio depende.

## Ejemplos

**Emprendimiento.** Una aplicación de consumo en fase inicial recopila únicamente los datos que de verdad necesita, porque cada campo adicional es una responsabilidad que preferiría no tener que defender. Mantiene un inventario de datos en una hoja de cálculo sencilla para poder responder de verdad a una solicitud de supresión, evita que correos electrónicos y tokens aparezcan en los registros y establece una regla de conservación básica para purgar los datos de cuentas inactivas desde hace tiempo. Diseñar un flujo de consentimiento claro y una supresión funcional ahora le cuesta una tarde; adaptarlos a posteriori, tras la primera demanda de un cliente empresarial o de un regulador, costará mucho más.

**Gran empresa.** Una aplicación de consumo a nivel mundial realiza una EIPD antes de lanzar una nueva funcionalidad de recomendaciones y descubre que recopilaría la ubicación precisa de forma innecesaria; el equipo decide recurrir a la zona aproximada, reduciendo el riesgo sin perder ninguna capacidad de producto. Los números de tarjeta se tokenizan, de modo que solo un almacén reducido y de control estricto almacena los valores crudos, lo que reduce drásticamente el alcance de la empresa para el [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (norma de seguridad de datos de la industria de tarjetas de pago). Reglas automatizadas de conservación purgan los datos de cuentas inactivas según su calendario, y un flujo de autogestión permite a los usuarios exportar y suprimir sus datos dentro del plazo legal en todos los sistemas, incluidos los respaldos.

**Sector público.** Un servicio nacional de salud clasifica todos los registros de pacientes como ISP y datos de categorías especiales, aplicando controles de acceso estrictos, cifrado y registro de auditoría. La política de residencia de datos mantiene todos los registros dentro de las fronteras nacionales, incluidos los respaldos y los datos de análisis, y cada proveedor queda vinculado contractualmente a las mismas obligaciones. Los ciudadanos tienen una base jurídica documentada (misión de interés público) para el tratamiento esencial, mientras que los usos opcionales de investigación exigen un consentimiento separado y revocable, registrado y honrado. Un mapa de datos sustenta la capacidad de responder a las solicitudes de acceso y supresión dentro de los plazos estatutarios.

## Justificación empresarial: motivación, retorno y coste total de propiedad

La inversión en privacidad suele presentarse como un mero coste de cumplimiento, pero eso infravalora su alcance. El coste total de propiedad incluye los procesos de EIPD, las herramientas de cartografía e inventario de datos, la infraestructura de tokenización y conservación, y la ingeniería necesaria para dar soporte a los derechos individuales y a la residencia. Pesa esto frente al coste de no invertir, que es severo y cada vez más probable. Las multas por incumplimiento de privacidad alcanzan hoy porcentajes de la facturación mundial, los grandes incidentes desencadenan demandas colectivas y los reguladores han demostrado que actúan. Más allá de las multas, un mal manejo de la privacidad destruye la confianza del cliente que sustenta los ingresos. Y remediar una falla de privacidad a posteriori (adaptar la supresión, desentramar flujos de datos no autorizados) cuesta mucho más que construirlo desde el principio.

El retorno también tiene una dimensión positiva real. Una privacidad sólida es un diferenciador competitivo y, en mercados regulados y en el ámbito público, es un requisito previo para poder concursar a negocio alguno. La minimización de datos reduce directamente la exposición ante una fuga y el coste de almacenamiento, y la tokenización acorta el alcance costoso de auditorías como PCI-DSS. Al presentar el caso ante la dirección, expón la privacidad de dos formas: como gestión de la responsabilidad ajustada al riesgo, con exposición regulatoria real, y como un activo de confianza que abre mercados. Destaca que la privacidad por diseño es mucho más barata que la privacidad por litigio, y que los datos acumulados sin finalidad son una responsabilidad que yace en el balance, esperando a materializarse.

## Antipatrónes y errores frecuentes

- **Recopilarlo todo y decidirlo después.** Acumular datos sin finalidad definida, maximizando la responsabilidad sin obtener ningún beneficio.
- **Conservación por inacción.** No eliminar nada porque no existe ningún calendario, de modo que los datos se acumulan indefinidamente.
- **Teatro del consentimiento.** Casillas preseleccionadas, consentimiento global o patrones oscuros que son jurídicamente nulos y erosionan la confianza.
- **Supresión que ignora los respaldos.** Eliminar del almacén primario pero dejar copias en respaldos, registros y sistemas analíticos.
- **IIP en registros y datos de prueba.** Difundir datos sensibles en entornos de menor control, donde es fácil que se expongan.
- **Ignorar los flujos de datos.** Pasar por alto que los registros, los respaldos, los datos analíticos y los subprocesadores trasladan datos a otras fronteras.
- **La privacidad como asunto solo jurídico.** Tratarla como un trámite burocrático en lugar de una restricción de diseño de ingeniería.
- **Sin mapa de datos.** Ser incapaz de responder a dónde residen los datos personales, lo que hace imposible tanto el cumplimiento de derechos como la respuesta ante una fuga.

## Modelo de madurez

**Nivel 1: Iniciar.** La privacidad se gestiona de forma reactiva, o no se gestiona. Los datos personales se recopilan sin inventario, sin minimización ni límites de conservación. El consentimiento es un añadido de última hora, no existe ningún proceso para atender solicitudes de acceso o supresión, y no se considera en qué lugar físico residen los datos.

**Nivel 2: Desarrollar.** Aparecen prácticas básicas, pero de forma desigual entre equipos. Existe una política de privacidad y se captura un consentimiento básico, con cierto nivel de awareness sobre la conservación. Las solicitudes de derechos se atienden de forma manual y lenta; la clasificación de datos es informal; un equipo mapea sus datos y otro recopila sin control. Ninguna práctica se aplica de forma coherente en toda la organización.

**Nivel 3: Estandarizar.** La privacidad por diseño está documentada y se aplica en toda la organización. Se realizan EIPD para los proyectos de mayor riesgo, los datos están cartografiados y clasificados por niveles, y los calendarios de conservación se ejecutan mediante eliminación automatizada. Se documenta una base jurídica para cada actividad de tratamiento, los mecanismos de consentimiento son válidos, las solicitudes de derechos se resuelven dentro de los plazos y la residencia se aborda para los datos sujetos a regulación.

**Nivel 4: Gestionar.** El programa de privacidad se mide y controla frente a líneas de base definidas. Se rastrea el tiempo de respuesta a las solicitudes de derechos frente a los plazos legales, la cobertura de las políticas de conservación y la antigüedad de los registros más antiguos, el número de campos de datos personales en alcance y cuántos de ellos están tokenizados o seudonimizados, el porcentaje de EIPD completadas en las funcionalidades que las requieren y el número de flujos transfronterizos sin gestionar que aparecen en las auditorías. Las métricas se vinculan a umbrales definidos, de modo que una desviación (una solicitud de derechos que se aproxima a su plazo, una transferencia inesperada, una deriva en la conservación) dispara una respuesta documentada en lugar de pasar inadvertida.

**Nivel 5: Orquestar.** La privacidad es una restricción de ingeniería por defecto que mejora de forma continua y se integra en toda la organización. La minimización, la tokenización y la conservación automatizada son estándar; las solicitudes de derechos se resuelven de forma autoasistida y completa en todos los sistemas, incluidos los respaldos; y los flujos de datos y la residencia se monitorizan y aplican de forma continua. La postura en materia de privacidad se adapta a medida que cambian la regulación, los mercados y la arquitectura, alimentando lecciones que retroalimentan el diseño, de modo que la línea de base sigue subiendo y no solo se sostiene.

## Ideas para el debate

1. ¿Cómo se resuelve la tensión entre los equipos de análisis, que quieren más datos, y la privacidad, que quiere menos?
2. ¿Qué arquitectura realista permite honrar la supresión en almacenes primarios, respaldos y copias descendentes?
3. ¿Qué base jurídica encaja con cada una de vuestras actividades de tratamiento y podéis defender esa elección?
4. ¿Cómo se mantiene a los datos personales fuera de los registros y los entornos no productivos sin obstaculizar la depuración?
5. ¿Qué requisitos de residencia de datos se aplican a vuestros mercados y cómo los complican los respaldos y los datos analíticos?
6. ¿Cómo deben combinarse la privacidad y el modelado de amenazas de seguridad en una única actividad de diseño?

## Ideas esenciales

- La privacidad regula si y cómo se utilizan los datos personales; es distinta de la seguridad y complementaria a ella.
- Intégrala desde el origen mediante EIPD y configuraciones predeterminadas protectoras.
- Minimiza la recopilación, aplica calendarios de conservación y construye una capacidad real de supresión.
- Clasifica IIP, ISP y categorías especiales, y protégelas de forma proporcional mediante tokenización y enmascarado.
- Establece y documenta una base jurídica; asegúrate de que el consentimiento sea libre, específico y revocable.
- Trata la residencia de datos y la transferencia transfronteriza como restricciones arquitectónicas de primer orden.
- El dato es una responsabilidad tanto como un activo; acumularlo sin finalidad es un riesgo a la espera de materializarse.

## Referencias y lecturas complementarias

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- Unión Europea, *Reglamento General de Protección de Datos (RGPD)*: texto y orientaciones
- Instituto Nacional de Estándares y Tecnología (NIST), *Privacy Framework* y *SP 800-122* (Guía para la protección de la información de identificación personal)
- ISO/IEC 27701, *Gestión de la información de privacidad*
- Daniel Solove, *Understanding Privacy*
- OCDE, *Directrices de privacidad* y *Principios de Práctica de Información Justa (FIPPs)*
- Ley de Privacidad del Consumidor de California (CCPA/CPRA): texto estatutario y orientaciones del regulador

