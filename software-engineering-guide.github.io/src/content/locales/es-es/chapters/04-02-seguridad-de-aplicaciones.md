# 4.2 Seguridad de aplicaciones

## Panorama y motivación

La seguridad de aplicaciones es el punto donde las amenazas abstractas se encuentran con el código concreto. La mayoría de las violaciones que llegan a los titulares se remontan a una vulnerabilidad a nivel de aplicación: una inyección, un flujo de autenticación defectuoso, un secreto expuesto o una dependencia comprometida. En equipos numerosos que despliegan decenas de servicios, lo difícil no es saber que esas fallas existen. Lo difícil es prevenir de forma consistente en una base de código extensa, escrita por miles de manos a lo largo de muchos años.

Para las empresas, la seguridad de aplicaciones es cuestión de confianza del cliente y obligación regulatoria. Una falla en el flujo de inicio de sesión o en el camino de pago puede desencadenar fraude, multas y la divulgación obligatoria de una violación de datos. Los sistemas gubernamentales enfrentan los mismos riesgos técnicos, pero con datos de mayor envergadura: elegibilidad de prestaciones, registros fiscales, datos del sistema de justicia penal e infraestructura nacional. En ambos contextos, la aplicación es la puerta principal, y los atacantes la exploran de forma constante y automática.

Este capítulo abarca las prácticas que mantienen las aplicaciones resilientes: conocer y defenderse de las clases de vulnerabilidad comunes, validar entradas y codificar salidas, acertar en la autenticación y la autorización, gestionar los secretos y proteger la cadena de suministro de software, que cada vez más determina la superficie de ataque real.

*Véase también:* el capítulo 4.1 (fundamentos de seguridad, modelado de amenazas y ciclo de vida del desarrollo seguro), el capítulo 10.3 (cadena de suministro de código abierto y licencias) y el capítulo 10.2 (SBOM, riesgo y garantía).

## Principios clave

- **Nunca confíes en la entrada.** Trata toda la información que cruza una frontera de confianza como hostil hasta que sea validada.
- **Valores seguros por defecto.** La vía segura debe ser la más sencilla; la conducta insegura debe exigir un esfuerzo deliberado y visible.
- **Fallar hacia el cierre.** Cuando una verificación de seguridad no puede completarse, se deniega el acceso en lugar de permitirlo.
- **Defensa en profundidad a nivel de aplicación.** Combinar validación, codificación, parametrización y protecciones del marco de trabajo; no depender de un solo mecanismo.
- **Mínimo privilegio para identidades y tokens.** Delimitar las credenciales con precisión y hacer que caduquen con rapidez.
- **Tus dependencias son tu código.** Eres responsable de la seguridad de todo lo que distribuyes, incluidos los componentes de terceros y de código abierto.
- **Estándares en lugar de improvisación.** Utilizar marcos de trabajo contrastados, como el [OWASP](https://en.wikipedia.org/wiki/OWASP) (Proyecto Mundial Abierto de Seguridad de Aplicaciones, por sus siglas en inglés) y su ASVS, en lugar de inventar controles propios.

## Recomendaciones

### Conocer y defenderse de los OWASP Top 10, verificar con el ASVS

Los OWASP Top 10 constituyen la lista de referencia del sector sobre los riesgos más críticos en aplicaciones web: control de acceso defectuoso, fallos criptográficos, inyección, diseño inseguro, configuración errónea de seguridad, componentes vulnerables, fallos de autenticación, fallos de integridad de datos, fallos en la registro y falsificación de solicitud del lado del servidor. Trátalos como un conocimiento indispensable para cada ingeniero, no como un documento de cumplimiento que se archiva y se olvida.

Para contar con un estándar riguroso y comprobable, adoptar el **Estándar de Verificación de Seguridad de Aplicaciones de OWASP (ASVS)**. El ASVS define requisitos de seguridad en tres niveles de garantía y proporciona controles concretos y auditables para diseñar y probar en función de ellos. Seleccionar el nivel adecuado al riesgo de cada aplicación y verificar el cumplimiento frente a él.

### Validar entradas y codificar salidas

Las vulnerabilidades de inyección siguen siendo de las más dañinas precisamente porque son tan fáciles de introducir. Defenderse con controles en capas:

- **Validar entradas** mediante listas permisivas estrictas (tipo, longitud, formato y rango esperados). Rechazar en lugar de sanitizar siempre que sea posible.
- **Utilizar consultas parametrizadas** y [sentencias preparadas](https://en.wikipedia.org/wiki/Prepared_statement) para todo el acceso a la base de datos; nunca construir sentencias SQL por concatenación de cadenas. Emplear constructores de consultas seguros y mapeadores objeto-relacionales (ORM) correctamente.
- **Codificar salidas** de forma contextual. HTML, atributos de HTML, JavaScript, URLs y CSS cada uno requiere una codificación distinta. Confiar en la codificación automática del marco de trabajo y comprender sus límites.
- **Prevenir la [injeción de scripts entre sitios](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** mediante codificación de salida complementada con una estricta Política de Seguridad de Contenido como segunda capa.
- **Prevenir la inyección de comandos y de plantillas** evitando la ejecución de procesos externos con datos no fiables y utilizando plantillas sin lógica o en entornos aislados.

### Acertar en la autenticación y la autorización

La autenticación demuestra quién es el usuario. La autorización decide qué puede hacer. Ambas fallan con frecuencia, así que hay que acertar.

- Preferir protocolos consolidados: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** para la autorización delegada y **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** para la autenticación. No construirlas desde cero.
- Imponer la **autenticación multifactor (MFA)**, especialmente para el acceso con privilegios y el acceso de administración.
- Almacenar contraseñas únicamente como hashes con sal y con un algoritmo moderno, lento y resistente a la memoria (como [Argon2](https://en.wikipedia.org/wiki/Argon2) o [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Nunca almacenar ni registrar credenciales en texto plano.
- Gestionar las **sesiones** con cuidado: generar tokens criptográficamente fuertes, establecer banderas seguras y HttpOnly en las cookies, rotar los tokens al cambiar el nivel de privilegio y hacer caducar las sesiones inactivas.
- Imponer la **autorización en el servidor para cada solicitud**, verificando que el principal autenticado sea propietario del recurso o tenga permiso para acceder a él. La autorización rota a nivel de objeto (acceder al registro de otro usuario alterando un identificador) es una de las fallas de API más frecuentes y graves.
- Centralizar la lógica de autorización allí donde sea posible para que la política sea consistente y auditable.

### Gestionar secretos y rotar claves

Los secretos incorporados en el código fuente son una causa crónica de violaciones. Cultivar un hábito disciplinado en torno a la gestión de secretos:

- Almacenar los secretos en un gestor de secretos o bóveda dedicada, nunca en el código fuente, en archivos de configuración ni en variables de entorno que se versionen en un sistema de control de versiones.
- Escanear automáticamente los commits y los repositorios en busca de secretos filtrados, y bloquear los fusiones que los introduzcan.
- Rotar claves y credencias periódicamente e inmediatamente ante cualquier sospecha de exposición. Preferir credenciales de vida corta y emisión automática frente a credenciales estáticas de larga duración.
- Aplicar el principio de mínimo privilegio a cada secreto: delimitarlo exactamente a lo que necesita.
- Cifrar los secretos en reposo y en tránsito, y auditar el acceso a ellos.

### Proteger la cadena de suministro de software

Las aplicaciones modernas se construyen en su mayoría con componentes de terceros, lo que convierte a la cadena de suministro en una superficie de ataque prioritaria.

- Mantener un **Software Bill of Materials (SBOM)** para cada aplicación, de modo que se sepa con exactitud lo que se distribuye y se pueda reaccionar con rapidez cuando aparezca una nueva vulnerabilidad.
- Escanear las dependencias de forma continua (Análisis de Composición de Software, o SCA, por sus siglas en inglés) y remediarse los componentes vulnerables conocidos con prontitud.
- Fijar y verificar las versiones de las dependencias; emplear archivos de bloqueo y registros de confianza.
- Adoptar **SLSA** (Niveles de suministro para artefactos de software) para elevar la integridad de la construcción y generar **atestados de procedencia** que describan cómo se construyeron los artefactos.
- **Firmar los artefactos** y verificar las firmas antes del despliegue, de modo que se pueda confiar en que lo que se ejecuta es lo que se construyó.
- Proteger el propio sistema de compilación; una pipeline de integración continua comprometida puede inyectar código malicioso en cada consumidor aguas abajo.

## Compromisos: ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| Adquirir o adoptar un proveedor de identidad (OIDC) | Probado a gran escala, MFA integrado, menos código crítico para asegurar | Dependencia del proveedor, esfuerzo de integración, coste |
| Construir autenticación a medida | Control total, sin dependencia externa | Extremadamente fácil de hacer mal, alto mantenimiento |
| Validación estricta por lista permisiva | Bloquea clases completas de vulnerabilidades | Puede afectar a casos legítimos de extremo, mayor esfuerzo inicial |
| Credenciales de vida corta | Ventana de exposición mínima, revocación automática | Requiere infraestructura de emisión robusta |
| Actualización agresiva de dependencias | Menos vulnerabilidades conocidas | Inestabilidad, posibles cambios incompatibles, carga de pruebas |
| SBOM + firmas + procedencia | Respuesta rápida ante incidentes, confianza verificable | Inversión en herramientas y procesos, cambio cultural |

El compromiso recurrente es entre el rigor anticipado y la exposición continua. Construir autenticación a medida o descuidar la higiene de dependencias parece más rápido hoy y resulta enormemente caro mañana. Adoptar estándares contrastados y controles automatizados de la cadena de suministro cuesta esfuerzo ahora, pero convierte un riesgo ilimitado e impredecible en uno gestionable y acotado. En equipos numerosos, el efecto multiplicador de la automatización es lo que más importa: un control aplicado una vez en una plantilla de camino pavimentado protege a cada servicio que la utiliza.

## Preguntas para debatir con el equipo

1. **¿Qué controles del ASVS se integrarán en el marco de trabajo de camino pavimentado para que los ingenieros los hereden sin esfuerzo?** La jugada de mayor apalancamiento para un equipo numeroso es hacer que la vía segura sea el comportamiento por defecto, de modo que un control escrito una vez en un marco de trabajo compartido proteja a cada servicio que lo adopte. Decidir cuáles de los requisitos del ASVS (consultas parametrizadas, codificación de salida, banderas seguras de sesión, comprobaciones de autorización en el servidor) deben vivir en la plantilla y no en la memoria de cada ingeniero. Para carteras empresariales y gubernamentales, decidir también qué aplicaciones necesitan el nivel 2 del ASVS y cuáles el nivel 3, y vincularlo con la sensibilidad de los datos que cada una maneja. Presentar una lista de los servicios y señalar cuáles ya heredan estos valores por defecto y cuáles reimplementan la seguridad a mano, porque en las soluciones caseras es donde se esconden las inyecciones y los controles de acceso defectuosos. Si los valores seguros viven únicamente en una página de wiki, se saltarán bajo presión de entrega, por lo que deben estar en código.

2. **¿Cómo se detectará y corregirá la autorización rota a nivel de objeto en cada API, y no solo en las nuevas?** Acceder al registro de otro usuario alterando un identificador es una de las fallas de API más frecuentes y graves, y se oculta en puntos de acceso antiguos que preceden a los estándares actuales. La regla es la autorización en el servidor para cada solicitud y cada objeto, pero lo difícil es verificar que se cumple a lo largo de una base de código extensa y de años de antigüedad, escrita por muchas manos. Decidir si se centralizará la lógica de autorización, se añadirán pruebas automatizadas que intenten el acceso entre inquilinos, o se ejecutarán pruebas dirigidas primero contra las APIs de mayor riesgo. Presentar un inventario de los puntos de acceso que exponen identificadores de objeto y clasificarlos por la sensibilidad de lo que devuelven. Sin un barrido deliberado, se seguirá distribuyendo esta falla y solo se descubrirá cuando un investigador o un atacante la encuentre.

3. **¿Cuál es el plan ante la próxima vulnerabilidad generalizada de dependencias: con qué rapidez se podrá encontrar y parchear cada servicio afectado?** Cuando una falla crítica aparece en una biblioteca popular, las empresas con un SBOM preciso identifican los servicios afectados en horas, mientras que otras pasan semanas buscando, y esa diferencia de velocidad decide cuánto daño se sufre. Decidir ahora si se produce un Software Bill of Materials para cada artefacto, si el escaneo de dependencias se ejecuta en cada pipeline, y quién toma la decisión del parche de emergencia. Para compradores regulados y del sector público, los SBOM y la procedencia firmada son cada vez más una condición para hacer negocios, por lo que esta preparación también protege la facturación. Traer la respuesta honesta a un ejercicio: elegir una biblioteca en uso generalizado y cronometrar cuánto tarda en listar cada servicio que la incorpora. Si la respuesta se mide en días, invertir en inventario y firma antes de que el próximo incidente lo exija.

4. **¿Cómo se pasará de secretos estáticos de larga vida a credenciales de vida corta emitidas automáticamente, y qué sistemas lo impiden hoy?** Los secretos incorporados y de larga duración son una causa crónica de violaciones, y la solución, credenciales de vida corta emitidas bajo demanda, depende de infraestructura de emisión que los sistemas antiguos a menudo no pueden utilizar. En un equipo numeroso, el peligro está en la adopción desigual: una plataforma moderna rota claves a la hora mientras que un servicio heredado sigue distribuyendo una contraseña de base de datos estática en un archivo de configuración. Decidir qué cargas de trabajo pueden consumir un gestor de secretos o un sistema de identidad de carga de trabajo ahora, cuáles necesitan inversión previa y quién es responsable del procedimiento de rotación en el momento en que se sospeche una clave filtrada. Presentar un inventario de cada credencial en uso, su tiempo de vida, su radio de impacto si se expone y si el escaneo de commits la detectaría antes de fusionar. En entornos empresariales y gubernamentales, vincular esto con la auditoría: los examinadores esperan cada vez más evidencia de rotación, acceso delimitado y registro de acceso para cada secreto, y una credencial estática que no se puede rotar sin tiempo de inactividad es una observación de auditoría a la espera de ser escrita.

5. **¿Dónde sigue habiendo autenticación casera o inconsistente y cuál es el plan para consolidar en protocolos contrastados?** Construir autenticación es una de las formas más fáciles de introducir fallas sutiles y explotables, y sin embargo la mayoría de las plataformas extensas albergan al menos un flujo de inicio de sesión heredado que precede a la decisión de estandarizar en OAuth 2.0 y OIDC. Las presiones contrarias son reales: migrar un flujo antiguo arriesga romper a usuarios e integraciones existentes, mientras que dejarlo en su sitio mantiene un objetivo de alto valor subprotegido. Decidir si se consolidará en un único proveedor de identidad, si se impondrá la MFA de forma uniforme y se fijará un plazo para retirar cada flujo artesanal, o si se aceptarán excepciones documentadas con controles compensatorios. Presentar un mapa de cada ruta de autenticación en la plataforma, cuáles imponen MFA, cuáles almacenan contraseñas con un hash moderno resistente a la memoria y cuáles son de construcción propia. Para carteras empresariales y gubernamentales, añadir la dimensión del cumplimiento: estándares como el NIST SP 800-63 fijan expectativas concretas para la garantía de identidad, y un flujo artesanal que no pueda demostrarlas no superará una auditoría ni una revisión de autorización de operación.

6. **¿Cómo se verificará que estos controles se sostienen en producción y se puede demostrarlo con evidencia, no con afirmaciones?** Escribir un valor seguro por defecto no es lo mismo que saber que cada servicio aún lo respeta, y los controles se degradan silenciosamente a medida que cambia el código, se acumulan excepciones y se despliegan nuevos puntos de acceso. En un equipo numeroso, la pregunta es la cobertura: qué servicios ejecutan análisis estático, escaneo de dependencias y pruebas dinámicas o de penetración, y cómo se sabe que los que los omiten no son las aplicaciones de mayor riesgo. Decidir qué verificación es obligatoria en el pipeline y qué es periódica, quién triagea los hallazgos y qué evidencia se conserva para demostrar que un control fue probado y superado en una fecha dada. Presentar el mapa de cobertura actual, el tiempo medio de remediación por severidad y la lista de aplicaciones sin prueba reciente. En contextos regulados y gubernamentales, esta evidencia no es opcional: los auditores, los oficiales autorizadores y los investigadores de brechas piden prueba de que los controles fueron verificados, y una política sin registros de prueba rara vez los satisface.

## Perspectiva por sector

**Startup.** Con dos o tres ingenieros y sin especialista de seguridad, el apalancamiento está en heredar seguridad en lugar de construirla: adoptar un proveedor de identidad OIDC gestionado desde el primer día y obtener MFA y restablecimiento seguro de contraseñas sin escribir código crítico de seguridad que no se puede permitirse fallar. Confiar en el ORM del marco de trabajo para que las consultas se parametrizen por defecto, mantener los secretos en el gestor de la plataforma en lugar de en archivos `.env` que un compañero podría comprometer por accidente, y activar el escaneo automático de dependencias que abre solicitudes de cambio cuando una biblioteca necesita parche. Ninguna de estas medidas frena al equipo, y significa que una clave filtrada o una inyección no terminará con la empresa antes de que tenga clientes.

**Pequeña empresa.** Probablemente no hay especialista de seguridad de aplicaciones ni presupuesto holgado, por lo que conviene adquirir controles incrustados en las herramientas y plataformas ya contratadas en lugar de dotar de una función dedicada. Elegir un proveedor de identidad alojado con MFA incluido, una base de datos gestionada que oriente hacia el acceso parametrizado y un host de repositorios que escanee los commits en busca de secretos filtrados de serie. Concentrar la atención escasa en las bases de los OWASP Top 10 que causan la mayoría de las violaciones reales, y preferir proveedores que distribuyan valores seguros que no se puedan desactivar con facilidad.

**Empresa.** A lo largo de muchos equipos, el desafío es la consistencia: integrar los controles del ASVS en marcos de trabajo de camino pavimentado para que cada nuevo servicio herede de forma automática consultas parametrizadas, codificación de salida, sesiones seguras y autorización en el servidor. Producir SBOM precisos y ejecutar escaneos de dependencias en toda la plataforma para que la próxima vulnerabilidad generalizada de una biblioteca sea cuestión de horas, no de semanas, y centralizar la política de autorización para que el acceso entre inquilinos sea testeable. Estándarizar en un único proveedor de identidad con MFA impuesto y gestionar la seguridad de aplicaciones como una cartera gobernada, con niveles del ASVS clasificados por riesgo y evidencia auditada.

**Sector público.** Las reglas de contratación, la transparencia y la rendición de cuentas pública moldean los controles que hay que demostrar, no solo implementar. Verificar los servicios orientados al ciudadano frente al OWASP ASVS en un nivel acorde a la sensibilidad de los datos, firmar cada artefacto desplegado y atestiguar su procedencia según SLSA para cumplir con los mandatos de cadena de suministro, y emitir credenciales de vida corta desde una bóveda central con registro completo de accesos. Esperar poder mostrar a auditores y oficiales autorizadores una cadena de custodia documentada desde el código fuente hasta producción, y alinear la garantía de identidad con estándares publicados como el NIST SP 800-63.

## Ejemplos

**Startup.** Un equipo SaaS de tres ingenieros omite construir su propio login y adopta un proveedor de identidad OIDC gestionado desde el día uno, obteniendo MFA y restablecimiento seguro de contraseñas sin escribir código crítico de seguridad que no se puede permitirse fallar. Se apoya en el ORM del marco de trabajo para que las consultas se parametrizen por defecto, mantiene los secretos en el gestor de la plataforma en lugar de en archivos `.env` que un compañero podría comprometer por accidente y activa el escaneo automático de dependencias que abre una solicitud de cambio cuando una biblioteca necesita parche. Nada de esto frena al equipo, y significa que una clave filtrada o una inyección no terminará con la empresa antes de que tenga clientes.

**Empresa.** Una plataforma de comercio electrónico que atiende a decenas de millones de compradores estandariza la autenticación en OIDC a través de un único proveedor de identidad, imponiendo MFA para el personal y autenticación reforzada para cambios de alto valor en las cuentas. Todo el acceso a la base de datos transita por un ORM configurado para parametrizar consultas, y una Política de Seguridad de Contenido respalda la codificación de salida. Tras una vulnerabilidad ampliamente divulgada en una popular biblioteca de registro, el SBOM de la empresa le permite identificar cada servicio afectado en horas y parchearlos en dos días, mientras competidores sin inventarios pasaron semanas buscando.

**Sector público.** Una agencia federal de prestaciones construye servicios orientados al ciudadano verificados frente al OWASP ASVS nivel 2, con nivel 3 para los componentes que manejan los registros más sensibles. Los secretos residen en una bóveda central que emite credenciales de vida corta; el escaneo de commits bloquea cualquier clave filtrada. Cada artefacto desplegado se firma y su procedencia se atestigua según SLSA, cumpliendo un mandato federal de cadenas de suministro de software verificables y ofreciendo a los auditores una cadena de custodia clara desde el código fuente hasta producción.

## Caso de negocio: motivaciones, retorno de inversión y coste total de propiedad

La inversión en seguridad de aplicaciones reduce la categoría de violación más probable y más costosa. El coste total de propiedad incluye herramientas (escáneres, gestores de secretos, proveedores de identidad), tiempo de ingeniería para remediar hallazgos y la leve fricción de los valores seguros por defecto. Frente a eso, pesar el coste de omitirla: las violaciones por inyección y control de acceso defectuoso exponen rutinariamente millones de registros, desencadenando multas regulatorias, notificación obligatoria, pérdidas por fraude, sprints de remediación y un daño reputacional que frena los ingresos durante años.

El retorno de inversión es más fuerte cuando los controles son automatizados y reutilizables. Una integración de identidad bien configurada, una capa de consultas endurecida en un marco de trabajo compartido y un pipeline que bloquea dependencias vulnerables protegen a toda la plataforma a un coste marginal por servicio. Los controles de cadena de suministro, en particular, han pasado de opcionales a esenciales: una dependencia comprometida puede convertir a cada uno de los clientes en víctima, y los reguladores y los compradores empresariales exigen cada vez más SBOM y procedencia firmada como condición para hacer negocios. Al presentar el caso ante la dirección, vincular la inversión a riesgos específicos y nombrados y a requisitos de contratación y cumplimiento que bloquean ingresos si no se cumplen.

## Antipatrónes y trampas

- **Crear criptografía o autenticación propias.** Casi siempre produce fallas sutiles y explotables.
- **Validación solo en el cliente.** Bailable trivialmente; el servidor debe volver a validar todo.
- **Sanitización por lista negativa.** Intentar eliminar caracteres «malos» en lugar de permitir solo los «buenos»; los atacantes encuentran las grietas.
- **Secretos en el código fuente o en archivos de entorno.** La causa más frecuente de filtración de credenciales.
- **Ignorar la autorización en el acceso a objetos.** Asumir que un usuario autenticado puede acceder a cualquier objeto cuyo identificador pueda adivinar.
- **Dependencias de configuración y olvido.** No actualizar componentes de terceros hasta que una violación lo obliga.
- **Tratar los Top 10 como meta final.** Son un suelo, no un estándar integral; usar el ASVS para la profundidad.
- **Registro de datos sensibles.** Contraseñas, tokens e información personal identificable (PII) en los registros son una violación a punto de ocurrir.

## Modelo de madurez

**Nivel 1: Iniciar.** La seguridad de aplicaciones depende del conocimiento individual de cada desarrollador y solo reacciona después de los incidentes. No hay controles estándar. Los secretos permanecen en el código. Las dependencias rara vez se actualizan. La autenticación es casera y arbitraria, y las fallas de inyección o de control de acceso se encuentran por suerte y no por proceso.

**Nivel 2: Desarrollar.** Aparecen prácticas básicas, pero varían de un equipo a otro. La conciencia de los OWASP Top 10 se extiende, hay algunas protecciones a nivel de marco de trabajo y existe un gestor de secretos, aunque su uso es desigual. El escaneo de dependencias se ejecuta ocasionalmente. Los sistemas nuevos adoptan un proveedor de identidad estándar, mientras que los servicios antiguos mantienen sus flujos de login caseros intactos.

**Nivel 3: Estandarizar.** Los controles están documentados y se imponen en toda la organización. Se fijan requisitos basados en el ASVS por nivel de riesgo, las consultas parametrizadas y la codificación de salida son la norma, y un proveedor de identidad central con MFA es obligatorio. Los secretos se gestionan y escanean automáticamente, se producen SBOM y el escaneo de dependencias se ejecuta en cada pipeline.

**Nivel 4: Gestionar.** La práctica se mide y controla frente a líneas base. La cobertura de escaneos y pruebas, el tiempo medio de remediación por severidad, el porcentaje de servicios que heredan los valores por defecto de camino pavimentado, la antigüedad de la rotación de credenciales y secretos y la conformidad con el ASVS se siguen en paneles de control. Las excepciones se registran con fecha de caducidad, el alejamiento de la línea base activa una acción, y los despliegues se condicionan a umbrales de seguridad definidos en lugar de a juicios discrecionales.

**Nivel 5: Orquestar.** La seguridad mejora de forma continua e integrada en toda la organización. Los valores seguros están integrados en los marcos de trabajo de camino pavimentado para que la vía sea automática, las credenciales de vida corta se usan en todas partes y la garantía completa de la cadena de suministro con firma y procedencia (SLSA) es estándar. La verificación es continua, la respuesta a nuevas vulnerabilidades es rápida y se mide, y cada incidente retroalimenta las plantillas compartidas, de modo que una única corrección endurece toda la plataforma.

## Ideas para el debate

1. ¿Dónde debe residir la lógica de autorización para ser a la vez consistente y mantenible a lo largo de muchos servicios?
2. ¿Con qué agresividad hay que actualizar dependencias, dado el compromiso entre exposición e inestabilidad?
3. ¿Qué nivel del ASVS es apropiado para cada clase de aplicación en la cartera?
4. ¿Cómo eliminar los secretos de larga vida sin crear infraestructura de emisión frágil?
5. ¿Qué haría falta para que la organización produzca y consuma SBOM y procedencia de cada artefacto?
6. ¿Cómo mantener los valores seguros por defecto para que no se desactiven bajo presión de entrega?

## Conclusiones clave

- Los OWASP Top 10 son un conocimiento indispensable; el ASVS aporta el estándar comprobable.
- Superponer validación de entradas, parametrización y codificación de salida para derrotar inyección y XSS.
- Utilizar protocolos contrastados (OAuth 2.0, OIDC) e imponer MFA; nunca construir autenticación desde cero.
- Imponer la autorización en el servidor para cada solicitud y cada objeto.
- Mantener los secretos fuera del código, gestionarlos de forma central y rotar hacia credenciales de vida corta.
- La cadena de suministro es una superficie de ataque prioritaria; emplear SBOM, SCA, firma y procedencia (SLSA).
- Los controles automatizados y reutilizables protegen a toda la plataforma a un coste marginal por servicio.

## Referencias y lectura adicional

- OWASP, *Top 10 de Riesgos de Seguridad de Aplicaciones Web*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Serie de Guías de Referencia Rápida* (Validación de Entradas, Autenticación, Autorización, Gestión de Secretos)
- Dafydd Stuttard y Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- Instituto Nacional de Estándares y Tecnología, *SP 800-63: Directrices de Identidad Digital*
- Cloud Native Computing Foundation y OpenSSF, *Marco SLSA* y *Guía de Seguridad de Cadena de Suministro*

