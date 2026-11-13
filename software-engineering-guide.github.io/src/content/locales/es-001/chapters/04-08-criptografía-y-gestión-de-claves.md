# 4.8 Criptografía y gestión de claves

## Visión general y motivación

Casi todo sistema que se construye ya depende de la [criptografía](https://en.wikipedia.org/wiki/Cryptography), la práctica de proteger la información mediante técnicas matemáticas para que solo las partes destinatarias puedan leerla o confiar en ella. El tráfico web transita por canales cifrados, las contraseñas se almacenan en forma de hash, las actualizaciones de software se firman y los datos de los clientes reposan cifrados en disco. La buena noticia para la mayoría de los ingenieros es que nadie se les pide que inventen nada de esto. Lo difícil no es la matemática, sino emplear bloques de construcción probados con corrección y, sobre todo, gestionar las claves de las que dependen.

Este capítulo está escrito para ingenieros que no son criptógrafos, que es prácticamente todo el mundo. Se necesita suficiente comprensión para tomar decisiones acertadas, saber qué garantiza cada herramienta y evitar los errores que convierten algoritmos sólidos en un falso sentido de seguridad. En el capítulo 4.3 (infraestructura y seguridad en la nube) se mencionan el cifrado y la gestión de claves de pasada; aquí se profundiza en qué cifrar, cómo hacerlo y cómo ejecutar el ciclo de vida de las claves que lo hace posible.

En grandes empresas, la criptografía se extiende por miles de servicios, certificados y claves, y un solo certificado vencido o una clave perdida puede tumbar un sistema crítico o filtrar un almacén de datos. En el ámbito público, la criptografía suele estar regulada, validada y auditada, con reglas de clasificación de datos que dictan con exactitud qué claves protegen qué secretos y quién puede custodiarlas. En ambos contextos, el fracaso recurrente es el mismo: buenos algoritros saboteados por una gestión de claves descuidada.

## Principios fundamentales

- **No implemente su propia criptografía.** Utilice bibliotecas probadas, ampliamente revisadas y algoritmos estándar. Los esquemas caseros fallan de formas que solo los expertos logran detectar.
- **Los algoritmos son lo fácil; las claves son lo difícil.** La mayoría de los fallos reales se sitúan en el ciclo de vida de una clave.
- **Conozca lo que cada primitiva garantiza.** La confidencialidad, la integridad y la autenticidad son propiedades distintas que requieren herramientas distintas.
- **Cifre en tránsito y en reposo por defecto.** Que la protección sea la norma, no una opción que se active manualmente.
- **Separe la custodia de la clave del acceso a los datos.** Quien gestione una clave no debe tener, automáticamente, la capacidad de leer los datos que protege.
- **Planifique el cambio.** Los algoritmos se debilitan, las claves se filtran y los estándares evolucionan. Diseñe para la rotación y la migración desde el primer día.
- **Prefiera implementaciones validadas cuando sea necesario.** En entornos regulados y del sector público, elija módulos con una validación reconocida.

## Recomendaciones

### No implemente su propia criptografía

Esta es la regla de oro, y merece enunciarse primero. Nunca diseñe un algoritmo de cifrado propio, invente un protocolo casero ni implemente a mano una primitiva tomada de un artículo académico. La criptografía funcional parece simple, pero encierra modos de fallo sutiles (canales laterales de tiempo, oráculos de relleno, aleatoriedad débil) que solo sobreviven a años de revisión experta. Utilice bibliotecas consolidadas, como el módulo criptográfico estándar de su plataforma o una biblioteca de renombre, y emplee esas bibliotecas en su nivel de abstracción más alto. Recurra a los modos de cifrado autenticado y a las interfaces simplificadas que hacen que la opción segura sea la opción predeterminada, en lugar de ensamblar piezas a bajo nivel por su cuenta.

### Ajuste la primitiva a la garantía que necesita

Herramientas distintas ofrecen garantías distintas, y confundirlas es un error frecuente y peligroso. Conozca las tres familias principales.

- La **criptografía [de clave simétrica](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** emplea un único secreto compartido para cifrar y descifrar. Es rápida y protege la **confidencialidad**, pero ambas partes ya deben compartir la clave. AES es el caballo de batalla del sector.
- La **criptografía [de clave pública](https://en.wikipedia.org/wiki/Public-key_cryptography)** se apoya en un par de claves matématicamente vinculadas: una clave pública que cualquiera puede poseer y una clave privada que se mantiene en secreto. Resuelve el problema de la distribución de claves y hace posible las **firmas digitales**, que demuestran la **autenticidad** (quién lo envió) y la **integridad** (que no ha sido alterado).
- Una **[función hash criptográfica](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** produce una huella de tamaño fijo a partir de unos datos y permite verificar su **integridad**. El hash es unidireccional y no es cifrado. Para almacenar contraseñas, utilice una función de hash lenta y con sal, nunca un hash rápido y sin protección (véase el capítulo 4.2 sobre seguridad de aplicaciones).

La lección práctica es clara: el cifrado oculta los datos, pero no acredita quién los envió; el hash detecta alteraciones, pero no oculta nada. La mayoría de los sistemas reales combinan ambos enfoques, y por eso conviene apoyarse en bibliotecas que los integren de forma correcta.

### Cifre en tránsito con TLS actualizado

Proteja cada salto de red con [Seguridad en la Capa de Transporte](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), el protocolo que cifra los datos mientras viajan entre sistemas. Exija versiones modernas de TLS, desactive las obsoletas, elija conjos de cifrado robustos y valide los certificados correctamente, en lugar de desactivar las comprobaciones para que «funcione». Cifre también el tráfico interno entre servicios, no solo el borde público, porque una postura de confianza cero asume que la red interna es hostil. Automatice la emisión y la renovación de certificados para que TLS sea, en todas partes, la opción indolora por defecto.

### Cifre en reposo mediante cifrado por envoltura

Cifre los datos almacenados por defecto: bases de datos, almacenamiento de objetos, copias de seguridad y registros de auditoría. El patrón habitual es el **cifrado por envoltura**, en el que una **clave de cifrado de datos (DEK)** cifra los datos reales y una **clave de cifrado de claves (KEK)**, custodiada en un servicio de gestión de claves, cifra esa DEK. Esto permite rotar la clave maestra sin tener que recifrar terabytes de datos y mantiene la clave raíz de mayor poder dentro de un perímetro reforzado. Guarde junto a los datos únicamente la DEK envuelta y, en el momento de uso, obténgala y desénela.

### Dirija el ciclo de vida de las claves con deliberación

El ciclo de vida de una clave es la parte verdaderamente difícil de la criptografía y el origen de la mayoría de las brechas y las paradas. Dirija cada etapa con intención:

- **Generación:** cree las claves a partir de una fuente de aleatoriedad robusta y del tamaño adecuado.
- **Distribución:** lleve las claves a los sistemas que las necesitan sin exponerlas en el código, en archivos de configuración ni en chats.
- **Rotación:** sustituya las claves con periodicidad definida y sea capaz de rotar con rapidez ante un compromiso sospechoso.
- **Revocación:** invalide una clave o un certificado comprometidos con celeridad y asegúrese de que los sistemas honran la revocación.
- **Destrucción:** retire el material criptográfico antiguo de forma segura para que no pueda recuperarse.

Utilice un **servicio de gestión de claves (KMS)** para centralizar todo esto y recurra a un [módulo de seguridad de hardware](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), un dispositivo a prueba de manipulaciones que genera y custodia claves para que nunca salgan en texto claro, en el caso de las claves que exijan la mayor fiabilidad. Separe a quienes gestionan las claves de quienes leen los datos que protegen, de modo que la custodia de la clave imponga la separación de funciones. Esto se conecta directamente con las reglas de clasificación y custodia de datos del capítulo 4.5 (privacidad y protección de datos).

### Distinga la gestión de secretos de la gestión de claves

Se solapan, pero no son lo mismo. La **gestión de claves** rige las claves criptográficas y su ciclo de vida, normalmente dentro de un KMS o un HSM que realiza las operaciones criptográficas en su nombre, de modo que la clave en texto claro nunca abandona el dispositivo. La **gestión de secretos** rige las credenciales de aplicación (contraseñas de base de datos, tokens de API, certificados) que los servicios necesitan recuperar y utilizar en texto claro, normalmente desde un bóveda de secretos con accesos de vida breve y auditables. Utilice un KMS para las claves, un gestor de secretos para las credenciales y no pegue ni lo uno ni lo otro en el código fuente ni en archivos de entorno que se versionen en control de código.

### Automatice la PKI y los ciclos de vida de los certificados

La **infraestructura de clave pública (IPK)** es el sistema de autoridades de certificación, certificados y cadenas de confianza que vincula las claves públicas con identidades. A escala, el riesgo dominante de la IPK es el vencimiento sorpresivo de un certificado que tumba un servicio. Mantenga un inventario de cada certificado, vigile las fechas de caducidad y automatice la emisión y la renovación para que nadie dependa de la memoria humana. Los certificados de vida breve, renovados de forma automática, son más seguros que los de larga vida mantenidos a mano, porque la automatización elimina el punto de fallo humano. Los protocolos estándar en este ámbito facilitan la interoperabilidad entre proveedores (véase el capítulo 3.8 sobre interoperabilidad y estándares abiertos).

### Diseñe para la agilidad criptográfica y la migración postcuántica

Los algoritmos se debilitan con el tiempo y los estándares avanzan. La **agilidad criptográfica** significa diseñar los sistemas de modo que se puedan intercambiar algoritmos y tamaños de clave sin una reescritura costosa: abstraya la criptografía detrás de una interfaz pequeña, versionee los datos cifrados para saber qué algoritmo los produjo y mantenga un inventario criptográfico de qué se usa y dónde. Esto importa ahora mismo por la [criptografía postcuántica](https://en.wikipedia.org/wiki/Post-quantum_cryptography), la nueva familia de algoritmos diseñada para resistir los futuros ordenadores cuánticos. Los adversarios pueden recopilar datos cifrados hoy y descifrarlos mañana, por lo que los secretos de larga vida necesitan un plan de migración. No es preciso alarmarse, pero conviene tener claro el inventario y estar preparado para adoptar los algoritmos postcuánticos estandarizados a medida que las plataformas los incorporen.

### Prefiera implementaciones validadas cuando sea exigencia

En sistemas regulados y del sector público, usar un algoritmo robusto no basta: la implementación debe estar validada. El **FIPS 140** (Federal Information Processing Standard 140) es el estándar estadounidense para la validación de módulos criptográficos, y muchos contratos exigen criptografía validada según FIPS. En el ámbito público, también puede aplicarse la orientación nacional, como la suite de Algoritmos Comerciales de Seguridad Nacional (CNSA) de la NSA para sistemas clasificados. Verifique qué régimen le resulta aplicable antes de construir, porque incorporar módulos validados a posteriori resulta costoso. Esto se vincula con la evidencia de cumplimiento y la gobernanza del capítulo 4.6.

## Compromisos: ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| KMS gestionado por el proveedor | Sencillo, integrado, bajo coste operativo | El proveedor asume la custodia; menor control directo |
| Claves de titularidad del cliente / HSM | Custodia total, cumple los requisitos más estrictos | Sobrecarga operativa, riesgo de pérdida de las claves |
| Certificados de vida breve automatizados | Sin caducidades sorpresivas, revocación rápida | Requiere una inversión previa en automatización |
| Certificados de larga vida | Sencillos, menos piezas móviles | La gestión manual de caducidades provoca paradas |
| Cifrado por envoltura | Rotación de claves económica, protege la clave maestra | Más piezas móviles que hay que comprender |
| Agilidad criptográfica desde el inicio | Migraciones futuras baratas | Esfuerzo adicional de abstracción y diseño ahora |
| Adopción temprana de criptografía postcuántica | Protege secretos de larga vida | Herramientas inmaduras, claves más grandes, algún riesgo |

La tensión central es el control frente a la carga operativa. Custodiar las propias claves en un HSM ofrece la máxima autoridad y satisface los mandatos más estrictos, pero exige experiencia y crea un nuevo riesgo catastrófico: si se pierde la clave, se pierde el dato de forma irrecoverable. Los servicios gestionados eliminan esa carga, pero trasladan la custodia al proveedor. Se resuelve por capas: utilizar servicios gestionados con valores predeterminados sensatos para la mayoría de los sistemas y reservar las claves de titularidad del cliente y los HSM para los datos de mayor clasificación, donde el control adicional justifica el coste y el riesgo.

## Preguntas para debatir con su equipo

1. **¿Dispone de un inventario completo de sus claves, certificados y los algoritmos en los que confía?** No se puede rotar, migrar ni auditar lo que no se ve, y la mayoría de las organizaciones descubre que tiene mucho más material criptográfico disperso entre servicios de lo que nadie registra. Un inventario es el prerrequisito de toda decisión posterior: la vigilancia de caducidades de certificados, la rotación de claves, el alcance de FIPS y la planificación postcuántica dependen de él. Lleve una lista de sus certificados actuales y sus fechas de caducidad, pregunte quién es responsable de cada uno y qué se rompe cuando caduca. Para un parque de sistemas extenso, la respuesta honesta suele ser que no existe una única fuente de verdad, y construirla es el primer paso de mayor retorno. Si hoy no puede enumerar su criptografía, la agilidad y la rotación son aspiraciones, no capacidades.

2. **¿Puede rotar o revocar una clave comprometida con rapidez, y lo ha ensayado alguna vez?** La rotación y la revocación son las fases del ciclo de vida que solo importan bajo presión, y los equipos descubren habitualmente durante un incidente que una clave está hard-codeada en una decena de sitios o que la revocación no se propaga de verdad. Fije un tiempo objetivo para rotar una clave y revocar un certificado, y ensáyelo antes de necesitarlo. Cuente la historia de la última exposición de credenciales y repase qué requirió la rotación en la práctica. En sistemas de gran empresa y del sector público, una rotación no ensayada puede significar elegir entre una exposición prolongada y una parada autoinfligida. Si la rotación nunca se ha probado, asuma que no funciona.

3. **¿Dónde reside la custodia de las claves y garantiza la separación de funciones?** Quien pueda gestionar una clave y quien pueda leer los datos que protege no debe ser la misma persona, porque fusionar ambos poderes anula en silencio el propósito del cifrado en reposo. Esta decisión también determina si se usan claves gestionadas por el proveedor, claves de titularidad del cliente o HSM, cada una con distinto nivel de control y distinto riesgo operativo. Examine las políticas de claves actuales y compruebe si alguna identidad puede, a la vez, administrar una clave y acceder al texto claro que resguarda, lo cual es una brecha silenciosa muy frecuente. En datos regulados o clasificados, las reglas de custodia pueden dictarlas la propia clasificación de datos (capítulo 4.5) o un mandato normativo. Si la custodia y el acceso no están separados, el cifrado protege menos de lo que sugiere el panel de control.

4. **¿Cómo se recuperaría si la clave maestra que protege el cifrado por envoltura se perdiera o se destruyera?** Las claves de titularidad del cliente y los HSM confieren la custodia, pero también introducen un nuevo modo de fallo catastrófico: si se pierde la clave de cifrado de claves, todas las claves de cifrado de datos que envuelve se vuelven permanentemente inlegibles, junto con los datos que protegen. Pésese este riesgo contra el riesgo opuesto de una copia de seguridad tan amplia que reproduzca en silencio el mismo problema de custodia que se intentaba resolver. Examine los mecanismos de copia de seguridad y de depósito en garantía de las claves, el alcance del daño de cada clave maestra y la evidencia de que una restauración se ha ejecutado realmente, no solo documentado. En parques de gran empresa y del sector público, vincúlelo a las reglas de clasificación de datos: las claves más sensibles suelen prohibir copias informales, de modo que la recuperación debe diseñarse con intención, ensayarse con periodicidad y conciliarse con cualquier requisito normativo de demostrar que el material criptográfico retirado fue destruido.

5. **¿De qué modo están preparados sus sistemas para una migración postcuántica y qué secretos de larga vida migraría primero?** Los adversarios pueden recopilar tráfico y archivos cifrados hoy y descifrarlos cuando maduren los ordenadores cuánticos, por lo que todo secreto que deba permanecer confidencial durante años ya está expuesto a un futuro invisible. La presión contraria es que las herramientas postcuánticas siguen siendo jóvenes, las claves son más grandes y migrar demasiado pronto supone apostar por un algoritmo que puede cambiar antes de estabilizarse. Examine el inventario criptográfico, una lista de secretos ordenados por el tiempo que deben permanecer confidenciales y una valoración honesta de si la arquitectura puede intercambiar algoritmos sin reescribirse. En el ámbito público y regulado, los registros con mandatos de confidencialidad de varias décadas convierten esta cuestión en concreta, no teórica, y la contratación puede requerir pronto un plan de migración documentado y el soporte de los algoritmos postcuánticos estandarizados.

6. **Cuando la regulación exige criptografía validada, ¿sabe exactamente qué módulos entran en el alcance y si cumplen los requisitos?** Usar un algoritmo robusto no equivale a usar una implementación validada, y los equipos descubren con frecuencia, y tarde, que una biblioteca, un entorno de ejecución o un servicio en la nube no está cubierto por el perímetro de FIPS 140 que exige un contrato. La tensión reside en que los módulos validados pueden rezagar respecto a las bibliotecas actuales en características y velocidad, de modo que elegirlos condiciona el stack de formas que importan para la ingeniería. Lleve la lista de módulos criptográficos que cada sistema regulado invoca realmente, los certificados de validación que los cubren y el mandato concreto (FIPS 140, CNSA o norma sectorial) que se aplica. En programas de gran empresa y del sector público, decídalo antes de construir, porque incorporar módulos validados y reautilizar un sistema a posteriori resulta costoso, lento y a menudo obliga a rediseñar los mismos componentes que se daban por terminados.

## Perspectiva por sector

**Startup.** Apóyese por completo en los valores predeterminados probados de su plataforma y dedique cero horas de ingeniería a criptografía a medida. Active el cifrado en reposo gestionado, termine TLS con certificados renovados automáticamente, hash las contraseñas con una función lenta y con sal de una biblioteca estándar y guarde los secretos en el gestor de secretos de la plataforma, nunca en el repositorio de código. Su única decisión de diseño es una interfaz delgada alrededor de los pocos campos que debe cifrar a nivel de aplicación, para que un futuro paso fuera de las claves gestionadas por el proveedor no suponga una reescritura.

**Pequeña empresa o pyme.** No dispone de un criptógrafo y tiene poco ánimo de operar un HSM, así que compre custodia en lugar de construirla: use el KMS y el gestor de secretos que vienen con sus herramientas en la nube o SaaS. Enmarque el trabajo como higiene: ninguna clave en el código, el cifrado activado por defecto en todas partes y la vigilancia de caducidades de certificados para que nada venza por sorpresa. Reserve las claves de titularidad del cliente para los pocos datos que un contrato o un regulador las exijan de verdad.

**Gran empresa.** El reto es la escala y la consistencia entre miles de servicios, certificados y claves. Operes un KMS centralizado con cifrado por envoltura, automatice todo el ciclo de vida de los certificados para que ninguna caducidad se mantenga a mano y mantenga un único inventario criptográfico que alimente la rotación, el alcance de FIPS y la planificación postcuántica. Separe la custodia de la clave del acceso a los datos como un control a nivel de organización y convierta el cifrado en una capacidad de plataforma que cada equipo hereda, no en una tarea que cada equipo reinventa.

**Sector público.** La contratación, la validación y la auditoría condicionan cada decisión. Use únicamente módulos criptográficos validados según FIPS 140 y siga la orientación nacional, como la suite CNSA de la NSA, para los sistemas de mayor clasificación. Genere y custodie las claves en HSM que nunca liberan material de clave en texto claro, y vincule la custodia a la clasificación de datos para que las claves más sensibles reposen con personal debidamente habilitado, bajo una estricta separación de funciones. Los certificados operan sobre una IPK interna gestionada con ciclos de vida automatizados, y la evidencia continua de criptografía validada alimenta la autorización continua de la agencia. Documente un plan de migración postcuántica para los registros que deben permanecer confidenciales durante décadas y exija a los proveedores que declaren qué módulos están validados antes de comprometerse.

## Ejemplos

**Startup.** Un equipo reducido que desarrolla una aplicación de seguimiento de la salud se apoya por completo en valores predeterminados probados. Termina TLS con certificados renovados automáticamente, activa el cifrado en reposo en su base de datos gestionada y su almacenamiento de objetos con el KMS del proveedor y hash las contraseñas con una función lenta y con sal de una biblioteca estándar. En lugar de escribir criptografía propia, recurre a una llamada de cifrado autenticado de alto nivel para el único campo que debe cifrar a nivel de aplicación. Los secretos viven en el gestor de secretos de la plataforma, nunca en el repositorio. Le cuesta unas pocas tardes y elimina por completo una categoría de errores catastróficos.

**Gran empresa.** Un banco global opera un KMS centralizado y una flota de HSM, con un inventario criptográfico que rastrea cada clave y certificado entre miles de servicios. El cifrado por envoltura protege los datos de los clientes, con claves de datos envueltas por claves maestras que rotan según un calendario mientras los datos permanecen intactos. La emisión y la renovación de certificados están plenamente automatizadas, tras una parada en un servicio público que les enseñó el coste de un único certificado vencido. Los administradores de claves son un equipo aparte de los ingenieros de aplicaciones, de modo que la custodia impone la separación de funciones, y una capa de agilidad criptográfica les permite iniciar la prueba de algoritmos postcuánticos para archivos de larga vida.

**Sector público.** Una agencia nacional que gestiona registros clasificados emplea únicamente módulos criptográficos validados según FIPS 140 y sigue la orientación CNSA de la NSA para sus sistemas de mayor clasificación. Las claves se generan y custodian en HSM que nunca liberan material de clave en texto claro, y la custodia se vincula a la clasificación de datos para que las claves más sensibles reposen con personal debidamente habilitado, bajo una estricta separación de funciones. Los certificados operan sobre una IPK interna gestionada con ciclos de vida automatizados, y la evidencia continua de criptografía validada alimenta la autorización continua de la agencia. Un plan de migración postcuántica documentado protege los registros que deben permanecer confidenciales durante décadas.

## Justificación empresarial: motivaciones, retorno de inversión y coste total de propiedad

La criptografía es otro ámbito en el que una inversión modesta evita pérdidas catastróficas que darían titulares. El coste total de propiedad incluye un KMS o un HSM, herramientas de gestión de secretos y de certificados, y el tiempo de ingeniería para diseñar los ciclos de vida y mantener el inventario al día. Esos costes son reales, pero acotados. El coste de omitirlos es una brecha de datos sin cifrar, una parada de varias horas por un certificado vencido o una pérdida irrecoverable de datos por una clave mal gestionada, cada una de las cuales acarrea sanciones regulatorias, costes de notificación y un daño reputacional duradero.

El mayor retorno de inversión proviene de la automatización y la reutilización. Los ciclos de vida automatizados de certificados eliminan la causa más frecuente de parada autoinfligida. La gestión centralizada de claves con valores predeterminados sensatos hace que cada nuevo servicio herede el cifrado en tránsito y en reposo sin esfuerzo por equipo, convirtiendo la criptografía de un impuesto recurrente en una capacidad de plataforma. En el ámbito regulado y del sector público, los módulos validados y la evidencia automatizada reducen también el coste de las auditorías y las autorizaciones. Al presentar el caso a la dirección, exprese la idea con claridad: los algoritmos son gratuitos y probados, el riesgo reside en la gestión de claves y la operación de certificados, y una pequeña inversión automatizada ahí previene los fracasos costosos.

## Antipatrones y errores comunes

- **Implementar criptografía propia.** Algoritmos a medida o protocolos caseros que fallan de formas sutiles, solo apercibidas por expertos.
- **Claves y secretos embebidos en el código.** Credenciales pegadas en el código fuente, archivos de configuración o chats, donde se filtran y no pueden rotarse.
- **Cifrado sin disciplina de claves.** Activar el cifrado pero dejar el acceso a las claves de par en par o nunca rotarlas.
- **Confundir el hash con el cifrado.** Tratar un hash como reversible o almacenar contraseñas con un hash rápido en lugar de uno lento y con sal.
- **Ruleta de certificados.** Sin inventario, sin vigilancia de caducidades y paradas sorpresivas periódicas cuando un certificado expira.
- **Custodia de claves y acceso a datos fusionados.** Una misma identidad que puede a la vez administrar una clave y leer los datos que protege.
- **Sin plan de rotación.** Claves que nunca se han rotado y no pueden rotarse con rapidez bajo presión.
- **Criptografía sin agilidad.** Algoritros anclados tan profundamente en el sistema que intercambiarlos exige una reescritura, bloqueando cualquier migración futura.
- **Ignorar los mandatos de validación.** Usar algoritmos robustos en módulos no validados donde FIPS u otra norma exige validación.

## Modelo de madurez

- **Nivel 1, Iniciar:** El cifrado es inconsistente y a menudo inexistente, aplicado de forma reactiva cuando alguien detecta una brecha. Las claves y los secretos están embebidos en el código o se comparten de forma informal por chats y archivos de configuración. No hay inventario, no hay rotación y los certificados caducan por sorpresa; a veces, los equipos escriben criptografía propia.
- **Nivel 2, Desarrollar:** TLS y el cifrado en reposo están activados para los sistemas principales, y existe un KMS o un gestor de secretos, pero la adopción es desigual y varía de un equipo a otro. Algunos certificados se vigilan y otros no, la rotación es manual y rara, y no existe un inventario criptográfico que lo unifique todo.
- **Nivel 3, Estándarizar:** El cifrado en tránsito y en reposo es el valor predeterminado documentado y aplicado a toda la organización. Las claves residen en un KMS con rotación programada y cifrado por envoltura, la custodia de las claves está separada del acceso a los datos, los ciclos de vida de los certificados están automatizados, se mantiene un inventario criptográfico y se usan módulos validados allí donde la regulación lo exige.
- **Nivel 4, Gestionar:** El parque criptográfico se mide y controla frente a líneas base. Se rastrea el tiempo de antelación de caducidad de los certificados, el porcentaje de claves rotadas a tiempo, el tiempo medio para revocar una clave comprometida, la detección de secretos en código por período y la cobertura del inventario, y se revisan esas métricas frente a objetivos. La rotación y la revocación se ensayan con periodicidad y se registran los tiempos; las desviaciones activan acciones correctivas en lugar de pasar inadvertidas.
- **Nivel 5, Orquestar:** La criptografía es una capacidad de plataforma que cada servicio hereda por defecto y se mejora de forma continua, integrada en toda la organización. La rotación y la revocación son rápidas y se ejercitan con regularidad, los HSM protegen las claves de mayor fiabilidad y la agilidad criptográfica junto con un plan activo de migración postcuántica mantienen el parque adaptable a medida que evolucionan los algoritmos y los mandatos. La evidencia de cumplimiento se genera automáticamente y alimenta la autorización continua.

## Propuestas de debate

1. ¿Qué sistemas de su parque justifican claves de titularidad del cliente o HSM, dadas su carga operativa y el riesgo de pérdida catastrófica?
2. ¿Cómo construiría y mantendría una única fuente de verdad para cada clave y certificado que posee?
3. ¿Cuál es el tiempo realista para rotar una clave comprometida hoy, y qué lo frena?
4. ¿Dónde hace la arquitectura difícil el intercambio de un algoritmo criptográfico y cómo lo resolvería antes de una migración forzada?
5. ¿Qué secretos de larga vida importaría si un adversario los recopilara ahora y los descifrara años después?
6. ¿Acaban los secretos y las claves alguna vez en el código, la configuración o los registros, y cómo lo sabría?

## Conclusiones principales

- **No implemente su propia criptografía.** Use bibliotecas probadas y algoritmos estándar en la abstracción más segura disponible.
- **Los algoritmos son fáciles; la gestión de claves, difícil.** El ciclo de vida de una clave (generación, distribución, rotación, revocación, destrucción) es donde residen los fallos reales.
- **Conozca sus garantías:** la cifrado simétrico y de clave pública protege la confidencialidad, las firmas demuestran la autenticidad y la integridad, y el hash detecta alteraciones, pero no es cifrado.
- **Cifre en tránsito con TLS actualizado y en reposo con cifrado por envoltura**, como valor predeterminado de cada sistema.
- **Separe la custodia de la clave del acceso a los datos**, use un KMS para las claves y un gestor de secretos para las credenciales, y no embeba ninguno de los dos en el código.
- **Automatice los ciclos de vida de los certificados** para eliminar la parada por caducidad sorpresiva y mantenga un inventario criptográfico.
- **Diseñe para la agilidad criptográfica** y inicie un plan de migración postcuántica para los secretos de larga vida.
- **Prefiera implementaciones validadas** (FIPS 140 y la orientación nacional aplicable) allí donde la regulación o la clasificación lo exijan.

## Referencias y lectura complementaria

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, estándares de criptografía postcuántica (FIPS 203, 204 y 205).
- Niels Ferguson, Bruce Schneier y Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* y *Transport Layer Protection Cheat Sheet*.
- National Security Agency, orientación sobre la *Commercial National Security Algorithm (CNSA) Suite*.

