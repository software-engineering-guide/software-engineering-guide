# 12.1 Glosario

Este glosario define los términos y siglas usados a lo largo de la guía. Las entradas se agrupan alfabéticamente. Cuando una entrada tiene una sigla común, se muestra entre paréntesis. Las definiciones son intencionalmente concisas; consulta el capítulo correspondiente para un tratamiento más completo.

## A

**[ABAC (Control de Acceso Basado en Atributos)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Un modelo de autorización que otorga acceso con base en atributos evaluados del usuario, el recurso, la acción, y el entorno (por ejemplo, departamento, nivel de autorización, hora del día) en lugar de roles fijos. Ofrece control granular y guiado por políticas al costo de mayor complejidad que RBAC.

**[Accesibilidad (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: La práctica de diseñar y construir software para que las personas con discapacidades puedan percibirlo, entenderlo, navegarlo, e interactuar con él. El numerónimo "a11y" abrevia las 11 letras entre "a" y "y" en inglés (accessibility).

**ADR (Registro de Decisión de Arquitectura)**: Un documento breve y versionado que captura una única decisión arquitectónica o técnica significativa, su contexto, las opciones consideradas, y sus consecuencias. Los ADR crean un historial duradero y revisable de por qué un sistema es como es.

**Agregado**: En el Diseño Guiado por el Dominio, un grupo de objetos de dominio tratado como una sola unidad para los cambios de datos, con una entidad actuando como la raíz del agregado que aplica los invariantes. Los agregados definen límites de consistencia y transacción.

**[API (Interfaz de Programación de Aplicaciones)](https://en.wikipedia.org/wiki/API)**: Un contrato definido a través del cual una pieza de software solicita servicios o datos de otra. Las API bien diseñadas ocultan el detalle de implementación y proveen interfaces estables y versionadas.

**API-primero**: Un enfoque de desarrollo en el que el contrato de la API se diseña y acuerda antes de la implementación, para que los consumidores y proveedores puedan trabajar en paralelo contra una especificación compartida.

**arc42**: Una estructura abierta y basada en plantillas para documentar la arquitectura de software, organizada en doce secciones que cubren el contexto, las restricciones, los bloques de construcción, el tiempo de ejecución, el despliegue, y las decisiones.

**[ARIA (Aplicaciones de Internet Ricas y Accesibles)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Una especificación del W3C que define roles, estados, y propiedades que hacen que los componentes web dinámicos y personalizados sean comprensibles para las tecnologías asistivas como los lectores de pantalla.

**ASR (Requisito Arquitectónicamente Significativo)**: Un requisito que tiene un efecto medible y de amplio alcance sobre la arquitectura, como una restricción de rendimiento, disponibilidad, seguridad, o regulatoria. Los ASR impulsan las decisiones de diseño más consecuentes.

**ASVS (Estándar de Verificación de Seguridad de Aplicaciones)**: Un estándar de OWASP que provee una lista de verificación graduada de requisitos y pruebas de seguridad para diseñar, construir, y verificar aplicaciones seguras.

**[Autoescalado](https://en.wikipedia.org/wiki/Autoscaling)**: El ajuste automático del número de instancias de cómputo en ejecución (o su tamaño) en respuesta a la carga, para que la capacidad siga a la demanda sin intervención manual. Complementa, pero no reemplaza, la planificación de capacidad deliberada.

**[Disponibilidad](https://en.wikipedia.org/wiki/Availability)**: La proporción de tiempo en que un sistema está operativo y capaz de atender solicitudes, a menudo expresada en "nueves" (por ejemplo, 99.9%). Es un objetivo de fiabilidad central codificado en los SLO y SLA.

## B

**Contrapresión**: Un mecanismo de control de flujo en el que un componente bajo carga señala a los productores río arriba que se ralenticen, previniendo colas sin límite y el fallo en cascada. Es central para los sistemas de transmisión y guiados por mensajes confiables.

**[BDD (Desarrollo Guiado por Comportamiento)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Una práctica colaborativa que expresa los requisitos como ejemplos concretos y legibles por humanos de comportamiento (a menudo en forma Dado/Cuando/Entonces) que a la vez sirven como pruebas de aceptación automatizadas.

**BFF (Backend para Frontend)**: Un patrón arquitectónico en el que se construye un servicio backend dedicado para un tipo específico de frontend o cliente, ajustando la forma y agregación de datos a las necesidades de ese cliente.

**[BI (Inteligencia de Negocio)](https://en.wikipedia.org/wiki/Business_intelligence)**: Las herramientas, procesos, y prácticas para recolectar, integrar, y analizar datos de negocio para respaldar el reporte, los tableros, y la toma de decisiones.

**Autopsia sin culpa**: Una revisión de incidente que se enfoca en las causas sistémicas y el aprendizaje en lugar de la culpa individual, bajo la premisa de que la gente actúa razonablemente dada la información y los incentivos que tenía.

**[Despliegue azul-verde](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Una estrategia de liberación que ejecuta dos entornos de producción idénticos ("azul" y "verde"), enrutando el tráfico a uno mientras se actualiza el otro, permitiendo un cambio y retroceso casi instantáneos.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Una función de clasificación ampliamente usada para la búsqueda de texto completo que puntúa qué tan bien coincide un documento con una consulta usando la frecuencia del término, la frecuencia inversa de documento, y la longitud del documento. Es el predeterminado de clasificación léxica en muchos motores de búsqueda.

**Contexto delimitado**: En el Diseño Guiado por el Dominio, un límite explícito dentro del cual un modelo de dominio particular y su lenguaje ubicuo se aplican consistentemente. Previene que los conceptos se confundan a través de diferentes partes de un sistema grande.

**Caché de construcción**: Un almacén de salidas de construcción previamente calculadas, indexado por las entradas que las produjeron, para que el trabajo sin cambios se reutilice en lugar de reconstruirse. Una caché de construcción remota compartida permite que todo un equipo y su CI reutilicen los resultados de los demás.

**[Factor de autobús](https://en.wikipedia.org/wiki/Bus_factor)**: El número de personas que tendrían que perderse (metafóricamente "atropelladas por un autobús") antes de que un proyecto se estanque por falta de conocimiento esencial. Un factor de autobús bajo señala experiencia concentrada y no documentada, y riesgo organizacional.

## C

**[Política de expulsión de caché](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: La regla que usa una caché para decidir qué entrada eliminar cuando está llena, como el menos recientemente usado (LRU) o el menos frecuentemente usado (LFU). La política moldea la tasa de aciertos y, con ella, el valor de la caché.

**[Invalidación de caché](https://en.wikipedia.org/wiki/Cache_invalidation)**: El problema de eliminar o actualizar datos en caché una vez que la fuente subyacente cambia, para que los lectores no vean valores obsoletos. Es famosamente uno de los problemas más difíciles de la computación.

**[Estampida de caché](https://en.wikipedia.org/wiki/Cache_stampede)**: Un modo de fallo en el que muchos clientes fallan la caché para la misma clave a la vez y todos golpean el origen juntos, abrumándolo. La coalescencia de solicitudes y la expiración escalonada lo previenen. También llamado manada estampida.

**Liberación canario**: Una técnica de despliegue que expone una nueva versión a un pequeño subconjunto de usuarios o tráfico primero, monitorea problemas, y luego expande progresivamente el despliegue si las métricas se mantienen sanas.

**[Teorema CAP](https://en.wikipedia.org/wiki/CAP_theorem)**: Un principio que establece que un almacén de datos distribuido puede garantizar como máximo dos de Consistencia, Disponibilidad, y Tolerancia a Particiones simultáneamente; como las particiones son inevitables, los diseñadores efectivamente intercambian consistencia por disponibilidad durante ellas.

**[Modelo C4](https://en.wikipedia.org/wiki/C4_model)**: Un enfoque ligero para visualizar la arquitectura de software en cuatro niveles de abstracción: Contexto del Sistema, Contenedores, Componentes, y Código.

**[CD (Entrega Continua / Despliegue Continuo)](https://en.wikipedia.org/wiki/Continuous_delivery)**: La Entrega Continua mantiene el software en un estado liberable para que pueda desplegarse en cualquier momento con una aprobación manual; el Despliegue Continuo libera automáticamente cada cambio que pasa el pipeline.

**[CDN (Red de Entrega de Contenido)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Una red geográficamente distribuida de servidores perimetrales que almacenan en caché y sirven contenido cerca de los usuarios, recortando la latencia y descargando la infraestructura de origen.

**Prompting de cadena de pensamiento**: Una técnica de prompting que pide a un modelo de lenguaje que trabaje a través de pasos de razonamiento intermedios antes de dar una respuesta final, mejorando el rendimiento en problemas de múltiples pasos al costo de una salida más larga y lenta.

**[CI (Integración Continua)](https://en.wikipedia.org/wiki/Continuous_integration)**: La práctica de fusionar frecuentemente los cambios de los desarrolladores en una línea principal compartida, cada fusión validada por una construcción y suite de pruebas automatizada para detectar problemas de integración temprano.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: El pipeline combinado de Integración Continua y Entrega/Despliegue Continuo que automatiza la construcción, prueba, y liberación de software.

**CMMC (Certificación del Modelo de Madurez de Ciberseguridad)**: Un programa del Departamento de Defensa de EE. UU. que certifica la madurez de ciberseguridad de los contratistas que manejan información de contratos federales e información no clasificada controlada.

**[Cohesión](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: El grado en que los elementos dentro de un módulo pertenecen juntos y sirven un propósito único y bien definido. La alta cohesión, emparejada con bajo acoplamiento, es un sello distintivo del diseño mantenible.

**Ventana de contexto**: La cantidad máxima de texto, medida en tokens, que un modelo de lenguaje puede considerar a la vez, abarcando su entrada y salida. Es un presupuesto escaso que el diseño de prompts y contexto debe gestionar deliberadamente.

**[Ley de Conway](https://en.wikipedia.org/wiki/Conway's_law)**: La observación de que la estructura de un sistema tiende a reflejar la estructura de comunicación de la organización que lo construye. La "maniobra de Conway inversa" moldea deliberadamente los equipos para producir una arquitectura deseada.

**Core Web Vitals**: Un conjunto de métricas de rendimiento web centradas en el usuario definidas por Google (como Largest Contentful Paint, Interaction to Next Paint, y Cumulative Layout Shift) que miden la carga, la interactividad, y la estabilidad visual.

**[Costo del retraso](https://en.wikipedia.org/wiki/Cost_of_delay)**: El costo económico de no tener algo terminado todavía, expresado como valor perdido por unidad de tiempo. Hacerlo explícito convierte la priorización de opinión en aritmética, y sustenta reglas de secuenciación como primero el trabajo ponderado más corto.

**[Acoplamiento](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: El grado de interdependencia entre módulos o servicios. El acoplamiento suelto limita el efecto ondulatorio del cambio y es un objetivo central de la buena arquitectura.

**CQRS (Segregación de Responsabilidad de Comando y Consulta)**: Un patrón que separa el modelo usado para cambiar el estado (comandos) del modelo usado para leer el estado (consultas), permitiendo que cada uno se optimice y escale independientemente.

**[CVE (Vulnerabilidades y Exposiciones Comunes)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Un catálogo público de vulnerabilidades de seguridad divulgadas, cada una asignada con un identificador único para que las herramientas y equipos puedan referenciar el mismo defecto sin ambigüedad.

**CWV**: Ver Core Web Vitals.

## D

**[DAST (Pruebas Dinámicas de Seguridad de Aplicaciones)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Pruebas de seguridad que sondean una aplicación en ejecución desde afuera, sin acceso al código fuente, para encontrar vulnerabilidades que aparecen en tiempo de ejecución.

**Proporción de tinta-datos**: Un principio de Edward Tufte que sostiene que un gráfico debería gastar la mayor parte de su tinta en los datos mismos y poco en la decoración, eliminando líneas de cuadrícula, bordes, y adornos que no informan.

**[Malla de datos](https://en.wikipedia.org/wiki/Data_mesh)**: Una arquitectura de datos descentralizada y un modelo operativo que trata los datos como un producto poseído por equipos de dominio, respaldado por infraestructura de plataforma de autoservicio y gobernanza federada.

**[Visualización de datos](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: La práctica de codificar datos en forma visual (posición, longitud, color, y similares) para que los patrones, comparaciones, y tendencias se vuelvan perceptibles y las decisiones estén mejor informadas.

**[DDD (Diseño Guiado por el Dominio)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Un enfoque de diseño de software que centra el modelo en el dominio de negocio, usando un lenguaje ubicuo compartido, contextos delimitados, y bloques de construcción como entidades, objetos de valor, y agregados.

**Tokens de diseño**: Valores nombrados y agnósticos de plataforma (colores, espaciado, tipografía, y similares) que codifican decisiones de diseño para que puedan compartirse consistentemente a través de un sistema de diseño y múltiples productos.

**DevEx / DevX (Experiencia del Desarrollador)**: La calidad general de la interacción diaria de un desarrollador con las herramientas, plataformas, y procesos, abarcando la fricción, la velocidad de retroalimentación, y la carga cognitiva.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Una cultura y conjunto de prácticas que unen el desarrollo de software y las operaciones para acortar los ciclos de entrega, aumentar la frecuencia de despliegue, y mejorar la fiabilidad mediante la automatización y la propiedad compartida.

**DORA (DevOps Research and Assessment)**: Un programa de investigación y sus cuatro métricas de entrega ampliamente usadas (frecuencia de despliegue, tiempo de entrega para cambios, tasa de fallo de cambio, y tiempo para restaurar el servicio) usadas para comparar el desempeño de entrega de software.

**DPIA (Evaluación de Impacto de Protección de Datos)**: Una evaluación estructurada, requerida bajo el RGPD para el procesamiento de alto riesgo, que identifica y mitiga los riesgos de privacidad antes de que un proyecto continúe.

**Deriva (configuración)**: La divergencia gradual del estado real de un sistema respecto a su estado declarado o pretendido, comúnmente causada por cambios manuales; la Infraestructura como Código y GitOps buscan detectarla y corregirla.

**Deriva (modelo)**: En el aprendizaje automático, la degradación del rendimiento del modelo a lo largo del tiempo conforme cambian las propiedades estadísticas de los datos de entrada (deriva de datos) o la relación que se modela (deriva de concepto).

**[DR (Recuperación ante Desastres)](https://en.wikipedia.org/wiki/Disaster_recovery)**: La estrategia, los procedimientos, y la infraestructura para restaurar el servicio y los datos después de un evento disruptivo mayor, típicamente gobernado por objetivos RTO y RPO.

**[DRY (No Te Repitas)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Un principio de diseño que establece que cada pieza de conocimiento debería tener una única representación autoritativa, reduciendo la duplicación y el riesgo de actualizaciones inconsistentes.

## E

**Tráfico este-oeste**: Tráfico de red entre servicios dentro de un sistema o centro de datos, en contraposición al tráfico norte-sur entre el sistema y los clientes externos. Una malla de servicios típicamente gobierna el tráfico este-oeste.

**[Computación de borde](https://en.wikipedia.org/wiki/Edge_computing)**: Ejecutar cómputo y almacenamiento cerca de donde se producen o consumen los datos en lugar de en una ubicación central, para recortar la latencia y el ancho de banda. Las redes de entrega de contenido son una forma temprana y extendida.

**[Elasticidad](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: La capacidad de un sistema de adquirir y liberar recursos automáticamente en respuesta a la demanda cambiante, para que la capacidad siga de cerca la carga.

**[ELT (Extraer, Cargar, Transformar)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Un patrón de integración de datos que carga primero los datos crudos en un almacén destino y los transforma ahí, explotando la escala de los almacenes de datos y lakehouses modernos.

**[Incrustación (embedding)](https://en.wikipedia.org/wiki/Word_embedding)**: Una representación de texto, imágenes, u otros datos como un vector numérico denso, posicionado para que los elementos similares se sienten cerca unos de otros. Las incrustaciones potencian la búsqueda semántica, la búsqueda vectorial, y la generación aumentada por recuperación.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: El estándar europeo que especifica los requisitos de accesibilidad para productos y servicios de TIC, referenciado por la adquisición del sector público en toda la UE y alineado con las WCAG.

**Presupuesto de error**: La cantidad permisible de falta de fiabilidad permitida por un SLO durante un período; cuando se agota, los equipos priorizan el trabajo de fiabilidad sobre las características nuevas. Reconcilia la tensión entre la velocidad y la estabilidad.

**[ETL (Extraer, Transformar, Cargar)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Un patrón de integración de datos que extrae datos de las fuentes, los transforma en una forma destino, y los carga en un destino como un almacén de datos.

**[Ley de IA de la UE](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Regulación de la Unión Europea que clasifica los sistemas de IA por riesgo e impone obligaciones en consecuencia, prohibiendo ciertos usos y regulando fuertemente los sistemas de alto riesgo.

**[Consistencia eventual](https://en.wikipedia.org/wiki/Eventual_consistency)**: Un modelo de consistencia en sistemas distribuidos en el que las réplicas pueden divergir temporalmente pero convergen al mismo estado una vez que las actualizaciones dejan de propagarse.

## F

**[Bandera de característica / interruptor de característica](https://en.wikipedia.org/wiki/Feature_toggle)**: Un mecanismo para habilitar o deshabilitar funcionalidad en tiempo de ejecución sin redesplegar, usado para despliegues graduales, experimentación, y control operativo.

**Almacén de características**: Un sistema centralizado para definir, almacenar, y servir características de aprendizaje automático curadas consistentemente tanto para el entrenamiento como para la inferencia, reduciendo la duplicación y el desajuste entrenamiento/servicio.

**[FedRAMP (Programa Federal de Gestión de Riesgo y Autorización)](https://en.wikipedia.org/wiki/FedRAMP)**: Un programa del gobierno de EE. UU. que estandariza la evaluación de seguridad, la autorización, y el monitoreo continuo para los servicios de nube usados por agencias federales.

**Prompting de pocos ejemplos (few-shot)**: Suministrar a un modelo de lenguaje un puñado de ejemplos trabajados en el prompt para demostrar la tarea deseada y el formato de salida, en contraposición al prompting sin ejemplos (zero-shot), que da instrucciones sin ejemplos.

**FinOps**: Una disciplina y práctica cultural que trae responsabilidad financiera al gasto variable de nube, dando a los equipos de ingeniería, finanzas, y negocio propiedad compartida del costo y el valor.

**[FISMA (Ley de Modernización de la Seguridad de la Información Federal)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Legislación de EE. UU. que requiere que las agencias federales implementen, documenten, y monitoreen programas de seguridad de la información, operacionalizada en gran parte mediante la guía del NIST.

**Eficiencia de flujo**: La proporción del tiempo de entrega total que un elemento de trabajo pasa siendo trabajado activamente en lugar de esperando, calculada como el tiempo que agrega valor dividido entre el tiempo de entrega total. La mayoría de los sistemas son sorprendentemente bajos, a menudo por debajo del 15 por ciento.

**Principio de cuatro ojos**: Un control que exige que una acción significativa sea revisada o aprobada por al menos dos personas, reduciendo la probabilidad de error o mala conducta.

**[Prueba difusa (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Una técnica de prueba automatizada que alimenta entradas malformadas, aleatorias, o inesperadas a un programa para descubrir fallos, defectos de seguridad, y defectos de casos límite.

## G

**[RGPD (Reglamento General de Protección de Datos)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: La regulación de la Unión Europea que gobierna el procesamiento de datos personales, otorgando derechos a los individuos e imponiendo obligaciones a los controladores y procesadores, con sanciones significativas por incumplimiento.

**GitOps**: Un modelo operativo que usa Git como la única fuente de verdad para la infraestructura y las aplicaciones declarativas, con automatización que reconcilia continuamente el sistema en vivo con el estado confirmado.

**Camino dorado / camino pavimentado**: Una forma predeterminada, bien soportada, y con opinión de construir y entregar software dentro de una organización, diseñada para hacer que la elección segura, conforme, y confiable sea la más fácil.

**Registro dorado**: En la gestión de datos maestros, la versión única, reconciliada, y autoritativa de una entidad de negocio (como un cliente) ensamblada a partir de múltiples sistemas fuente mediante reglas de coincidencia y supervivencia.

**[Tipado gradual](https://en.wikipedia.org/wiki/Gradual_typing)**: Un enfoque de sistema de tipos que permite que el tipado estático y dinámico coexistan en una base de código, para que los tipos puedan agregarse incrementalmente a un programa de tipado dinámico. Las sugerencias de tipo y los verificadores de tipo opcionales son ejemplos comunes.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Un lenguaje de consulta y tiempo de ejecución para API que permite a los clientes solicitar exactamente los datos que necesitan en una sola llamada, usando un esquema fuertemente tipado.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Un marco de llamada a procedimiento remoto de alto rendimiento y primero-el-contrato que usa HTTP/2 y, típicamente, Protocol Buffers para la comunicación eficiente entre servicios.

## H

**Construcción hermética**: Una construcción que depende solo de entradas explícitamente declaradas y está aislada del entorno anfitrión, para que produzca la misma salida en cualquier lugar. La hermeticidad es la base de las construcciones reproducibles y el almacenamiento en caché confiable.

**[HSM (Módulo de Seguridad de Hardware)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Un dispositivo de hardware resistente a manipulaciones que genera, almacena, y usa claves criptográficas, proveyendo protección de claves más fuerte que los enfoques solo de software.

**[HIPAA (Ley de Portabilidad y Responsabilidad del Seguro Médico)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Legislación de EE. UU. que, entre otras cosas, establece requisitos para salvaguardar la información de salud protegida (PHI) y gobierna su uso y divulgación.

**Escalado horizontal**: Aumentar la capacidad agregando más instancias o nodos ("escalar hacia afuera") en lugar de hacer un solo nodo más poderoso. Sustenta la mayoría de las arquitecturas resilientes a gran escala.

## I

**[IaC (Infraestructura como Código)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: La práctica de definir y aprovisionar infraestructura mediante configuración legible por máquina y controlada por versión en lugar de procesos manuales, permitiendo la repetibilidad y la revisión.

**[IAM (Gestión de Identidad y Acceso)](https://en.wikipedia.org/wiki/Identity_management)**: El marco de políticas y tecnologías que asegura que las identidades correctas tengan el acceso correcto a los recursos correctos en los momentos correctos.

**IDP / IdP**: "IDP" comúnmente denota una Plataforma de Desarrollador Interna, la capa de herramientas de autoservicio que abstrae la infraestructura para los equipos de producto; "IdP" denota un Proveedor de Identidad, un servicio que autentica usuarios y emite aserciones. El contexto desambigua los dos.

**[Idempotencia](https://en.wikipedia.org/wiki/Idempotence)**: Una propiedad mediante la cual realizar una operación múltiples veces tiene el mismo efecto que realizarla una vez, esencial para los reintentos seguros en sistemas y API distribuidos.

**[i18n (Internacionalización)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Diseñar y construir software para que pueda adaptarse a diferentes idiomas, regiones, y convenciones culturales sin cambios de ingeniería. El numerónimo abrevia las 18 letras entre "i" y "n" en inglés (internationalization).

**Artefacto inmutable**: Una salida de construcción que, una vez producida y versionada, nunca se modifica; cualquier cambio produce una nueva versión. La inmutabilidad hace que las liberaciones sean reproducibles y permite construir una vez y promover el mismo artefacto a través de los entornos.

**InnerSource**: La aplicación de prácticas de desarrollo de código abierto (transparencia, repositorios compartidos, y contribución entre equipos) dentro de una sola organización.

**Deriva de IaC**: Ver Deriva (configuración).

**[Índice invertido](https://en.wikipedia.org/wiki/Inverted_index)**: La estructura de datos central de un motor de búsqueda, que mapea cada término a la lista de documentos que lo contienen, para que las consultas puedan responderse sin escanear cada documento.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Un estándar internacional que especifica los requisitos para un Sistema de Gestión de Seguridad de la Información (SGSI), proveyendo un marco certificable para gestionar el riesgo de seguridad de la información.

**ISO/IEC 42001**: Un estándar internacional que especifica los requisitos para un Sistema de Gestión de IA, dando a las organizaciones un marco certificable para gobernar el desarrollo y uso responsable de la IA.

## J

**[JWT (Token Web JSON)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Un formato de token compacto, firmado (y opcionalmente cifrado) usado para transmitir afirmaciones entre partes, comúnmente para la autenticación y autorización en sistemas web y de API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Un método de flujo de trabajo lean que visualiza el trabajo en un tablero, limita el trabajo en progreso, y gestiona el flujo para mejorar el rendimiento y la previsibilidad.

**[KISS (Mantenlo Simple, Tonto)](https://en.wikipedia.org/wiki/KISS_principle)**: Un principio de diseño que favorece la solución más simple que satisface la necesidad, bajo la premisa de que la complejidad innecesaria aumenta el costo y el riesgo.

**KMS (Servicio de Gestión de Claves)**: Un sistema para crear, almacenar, rotar, y controlar el acceso a las claves criptográficas, a menudo respaldado por módulos de seguridad de hardware.

**[KPI (Indicador Clave de Desempeño)](https://en.wikipedia.org/wiki/Performance_indicator)**: Una medida cuantificable usada para rastrear el progreso hacia un objetivo específico de negocio u operativo.

## L

**Lakehouse**: Una arquitectura de datos que combina el almacenamiento de bajo costo y flexible de un data lake con las características de gestión, transacciones, y rendimiento de un almacén de datos.

**[Tiempo de entrega](https://en.wikipedia.org/wiki/Lead_time)**: El tiempo transcurrido desde que se solicita (o confirma) un cambio hasta que se entrega en producción; una métrica de entrega DORA central.

**[Privilegio mínimo](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Un principio de seguridad que otorga a cada usuario, proceso, o sistema solo el acceso mínimo requerido para realizar su función, limitando el daño de un compromiso o error.

**[Ley de Little](https://en.wikipedia.org/wiki/Little's_law)**: Un resultado de la teoría de colas que establece que el número promedio de elementos en un sistema estable es igual a la tasa de llegada promedio multiplicada por el tiempo promedio que cada elemento pasa en el sistema. Vincula el trabajo en progreso, el rendimiento, y el tiempo de entrega.

**[LLM (Modelo de Lenguaje Grande)](https://en.wikipedia.org/wiki/Large_language_model)**: Un modelo de aprendizaje automático entrenado en corpus de texto muy grandes para predecir y generar lenguaje, capaz de tareas como el resumen, la traducción, y la generación de código.

**[l10n (Localización)](https://en.wikipedia.org/wiki/Language_localisation)**: Adaptar el software internacionalizado a una configuración regional específica, incluyendo la traducción, el formato, y las convenciones culturales. El numerónimo abrevia las 10 letras entre "l" y "n" en inglés (localization).

## M

**[MDM (Gestión de Datos Maestros)](https://en.wikipedia.org/wiki/Master_data_management)**: La disciplina y las herramientas para crear y mantener una vista única, autoritativa, y consistente de las entidades de negocio centrales (como clientes o productos) a través de los sistemas.

**MITRE ATT&CK**: Una base de conocimiento pública y curada de tácticas y técnicas de adversarios del mundo real, ampliamente usada para planificar ejercicios de equipo rojo, guiar la ingeniería de detección, y describir amenazas en un vocabulario compartido.

**Tiempo Medio de Recuperación (MTTR)**: El tiempo promedio tomado para restaurar el servicio después de un fallo; una métrica común de fiabilidad y gestión de incidentes.

**[Programación en mafia (mob programming)](https://en.wikipedia.org/wiki/Mob_programming)**: Una práctica en la que todo un equipo trabaja junto en la misma tarea en la misma computadora, rotando quién escribe, para compartir conocimiento y tomar decisiones colectivamente.

**[MLOps (Operaciones de Aprendizaje Automático)](https://en.wikipedia.org/wiki/MLOps)**: El conjunto de prácticas que despliegan, monitorean, y mantienen de manera confiable y eficiente los modelos de aprendizaje automático en producción, extendiendo los principios de DevOps al ciclo de vida del AA.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Un único repositorio de control de versiones que contiene el código de muchos proyectos o de toda la organización, permitiendo herramientas compartidas y cambios atómicos entre proyectos al costo de herramientas de escalado especializadas.

**mTLS (TLS mutuo)**: Una configuración de Transport Layer Security en la que ambas partes presentan y verifican certificados, así que cada una autentica a la otra. Es un predeterminado para el tráfico de servicio a servicio en una malla de servicios y redes de confianza cero. Ver también [autenticación mutua](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Prueba de mutación](https://en.wikipedia.org/wiki/Mutation_testing)**: Una técnica que introduce deliberadamente pequeños defectos ("mutantes") en el código para verificar si la suite de pruebas los detecta, midiendo la efectividad real de la suite.

## N

**[NDCG (Ganancia Acumulada Descontada Normalizada)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Una métrica de calidad de clasificación que premia colocar resultados altamente relevantes cerca de la parte superior de una lista de resultados, normalizada para que las puntuaciones sean comparables entre consultas. Es un elemento básico de la evaluación de relevancia de búsqueda.

**[NIST (Instituto Nacional de Estándares y Tecnología)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Una agencia federal de EE. UU. cuyas Publicaciones Especiales y marcos son estándares ampliamente referenciados para la ciberseguridad, la privacidad, y la IA.

**NIST AI RMF (Marco de Gestión de Riesgo de IA)**: Un marco voluntario del NIST para identificar, evaluar, y gestionar los riesgos asociados con los sistemas de IA a través de su ciclo de vida, organizado alrededor de las funciones Gobernar, Mapear, Medir, y Gestionar.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Un catálogo del NIST de controles de seguridad y privacidad para los sistemas de información federales, ampliamente usado como línea base mucho más allá del gobierno.

**NIST SP 800-171**: Una publicación del NIST que especifica los requisitos para proteger la información no clasificada controlada (CUI) en sistemas no federales, central para el cumplimiento de contratistas de defensa.

**[NFR (Requisito No Funcional)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Un requisito que describe cómo debería comportarse un sistema (sus cualidades como el rendimiento, la seguridad, la fiabilidad, o la usabilidad) en lugar de qué funciones realiza.

**Tráfico norte-sur**: Tráfico de red entre un sistema y sus clientes externos (entrando y saliendo del centro de datos o clúster), en contraposición al tráfico este-oeste entre servicios internos. Una puerta de enlace de API típicamente gobierna el tráfico norte-sur.

## O

**Observabilidad**: El grado en que el estado interno de un sistema puede inferirse a partir de sus salidas externas, típicamente logrado mediante telemetría: métricas, registros, y trazas.

**[OKR (Objetivos y Resultados Clave)](https://en.wikipedia.org/wiki/OKR)**: Un marco de establecimiento de objetivos que empareja un objetivo cualitativo con unos cuantos resultados clave medibles para alinear y enfocar una organización.

**OpenTelemetry (OTel)**: Un estándar abierto y conjunto de herramientas neutral respecto al proveedor para generar, recolectar, y exportar datos de telemetría (trazas, métricas, y registros) de software.

**OPA (Open Policy Agent)**: Un motor de políticas de código abierto y propósito general que evalúa políticas (escritas en el lenguaje Rego) para aplicar reglas de autorización y configuración a través de la pila, permitiendo la política como código.

**OSPO (Oficina de Programa de Código Abierto)**: Una función organizacional que coordina la estrategia, gobernanza, cumplimiento, y compromiso comunitario de código abierto, gestionando tanto el consumo como la contribución.

**[OWASP (Proyecto Abierto de Seguridad de Aplicaciones Web Mundial)](https://en.wikipedia.org/wiki/OWASP)**: Una comunidad sin fines de lucro que produce recursos de seguridad de aplicaciones ampliamente usados y disponibles gratuitamente, incluyendo el OWASP Top Ten y el ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Una extensión del teorema CAP que establece que si hay una Partición, un sistema intercambia Disponibilidad por Consistencia, de lo contrario (Else, en operación normal) intercambia Latencia por Consistencia.

**[PCI DSS (Estándar de Seguridad de Datos de la Industria de Tarjetas de Pago)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Un estándar de seguridad mantenido por la industria de tarjetas de pago que especifica los requisitos para las organizaciones que almacenan, procesan, o transmiten datos de titulares de tarjetas.

**[Prueba de penetración](https://en.wikipedia.org/wiki/Penetration_test)**: Un ataque simulado y autorizado a un sistema por probadores hábiles para encontrar y demostrar vulnerabilidades explotables antes de que lo hagan atacantes reales, entregado como hallazgos priorizados y accionables.

**[PII (Información de Identificación Personal)](https://en.wikipedia.org/wiki/Personal_data)**: Información que puede identificar a un individuo específico, ya sea sola o combinada con otros datos; su manejo se gobierna por leyes de privacidad y política interna.

**Ingeniería de plataforma**: La disciplina de construir y operar plataformas internas de autoservicio y caminos dorados que reducen la carga cognitiva y aceleran los equipos de producto.

**POUR**: Los cuatro principios guía de las Pautas de Accesibilidad al Contenido Web: el contenido debe ser Perceptible, Operable, Comprensible, y Robusto (por sus siglas en inglés).

**Revisión de preparación para producción**: Una verificación estructurada, ejecutada antes de que un servicio entre en vivo o asuma la propiedad de guardia, que confirma que cumple los estándares de observabilidad, fiabilidad, seguridad, manuales de operación, y soporte operativo.

**[Ingeniería de prompts](https://en.wikipedia.org/wiki/Prompt_engineering)**: La práctica de diseñar y refinar las instrucciones, el contexto, y los ejemplos dados a un modelo de lenguaje para obtener una salida confiable y de alta calidad, tratada como una disciplina de ingeniería versionada y probada en lugar de ensayo y error.

**[Inyección de prompt](https://en.wikipedia.org/wiki/Prompt_injection)**: Un ataque en el que una entrada elaborada hace que un modelo de lenguaje ignore sus instrucciones pretendidas y siga las del atacante en su lugar, el análogo de la era de la IA a los defectos de inyección. Es un riesgo de seguridad central de las aplicaciones LLM.

**Prueba basada en propiedades**: Una técnica de prueba que verifica que las propiedades declaradas se sostienen a través de muchas entradas generadas automáticamente, en lugar de depender solo de ejemplos elegidos a mano.

**Solicitud de extracción (PR) / solicitud de fusión (MR)**: Un conjunto propuesto de cambios enviado para revisión y discusión antes de fusionarse en una rama compartida, la unidad principal de revisión de código en la mayoría de los flujos de trabajo.

**Equipo púrpura**: Un ejercicio colaborativo en el que los equipos de seguridad ofensivos (rojo) y defensivos (azul) trabajan juntos en tiempo real, para que los ataques y las detecciones destinadas a capturarlos se ajusten uno contra el otro.

## Q

**Puerta de calidad**: Un punto de verificación automatizado en un pipeline que debe pasarse (por ejemplo, cumplir umbrales de cobertura, seguridad, o rendimiento) antes de que un cambio pueda avanzar.

**[Quórum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: En sistemas distribuidos, el número mínimo de nodos que deben estar de acuerdo para que una operación (como una lectura o escritura) se considere exitosa, usado para mantener la consistencia a pesar de los fallos.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Un modelo de asignación de responsabilidades que etiqueta a cada participante en una tarea o decisión como Responsable, Rinde cuentas, Consultado, o Informado.

**[RAG (Generación Aumentada por Recuperación)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Una técnica que fundamenta la salida de un modelo de lenguaje recuperando primero documentos o datos relevantes y suministrándolos como contexto, mejorando la precisión y reduciendo la alucinación.

**[RBAC (Control de Acceso Basado en Roles)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Un modelo de autorización que asigna permisos a roles y roles a usuarios, simplificando la administración al gestionar el acceso a nivel de rol.

**[Equipo rojo](https://en.wikipedia.org/wiki/Red_team)**: Un grupo que emula un adversario realista, a menudo contra toda una organización y sin avisar a los defensores, para probar la detección y respuesta en lugar de meramente enumerar vulnerabilidades. En contraste con un equipo azul (defensivo).

**[Datos de referencia](https://en.wikipedia.org/wiki/Reference_data)**: Listas de códigos y clasificaciones controladas y de cambio lento usadas para categorizar otros datos, como códigos de país, monedas, y valores de estado. Gobernarlos como un vocabulario compartido y versionado mantiene los sistemas consistentes.

**Rego**: El lenguaje declarativo de políticas usado por Open Policy Agent para expresar reglas para decisiones de autorización y configuración.

**[REST (Transferencia de Estado Representacional)](https://en.wikipedia.org/wiki/REST)**: Un estilo arquitectónico para aplicaciones en red que usa operaciones sin estado sobre HTTP en recursos direccionables, valorado por su simplicidad y amplias herramientas.

**[Proxy inverso](https://en.wikipedia.org/wiki/Reverse_proxy)**: Un servidor que se sienta frente a uno o más servicios backend y reenvía las solicitudes del cliente hacia ellos, comúnmente proveyendo terminación TLS, balanceo de carga, caché, y un único punto de entrada.

**[RFC (Solicitud de Comentarios)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Una propuesta escrita circulada para retroalimentación antes de una decisión o cambio técnico significativo, fomentando la transparencia y la propiedad compartida. (El término también nombra la serie de documentos de estándares de Internet.)

**[ROI (Retorno de Inversión)](https://en.wikipedia.org/wiki/Return_on_investment)**: Una medida del valor ganado de una inversión en relación con su costo, usada para justificar y priorizar las decisiones de ingeniería y tecnología.

**[RPA (Automatización Robótica de Procesos)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: "Robots" de software que automatizan tareas repetitivas y basadas en reglas interactuando con las interfaces de usuario y sistemas existentes como lo haría una persona.

**RPO (Objetivo de Punto de Recuperación)**: La cantidad máxima aceptable de pérdida de datos medida en tiempo (por ejemplo, "hasta cinco minutos"), definiendo con qué frecuencia deben protegerse los datos.

**RTO (Objetivo de Tiempo de Recuperación)**: La duración máxima aceptable para restaurar un servicio después de una disrupción, guiando el diseño y la inversión en recuperación ante desastres.

## S

**Saga**: Un patrón para gestionar la consistencia de datos a través de servicios en una transacción distribuida secuenciando transacciones locales y emitiendo acciones compensatorias cuando falla un paso.

**[SAFe (Marco Ágil Escalado)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Un marco para aplicar prácticas ágiles y lean a través de grandes empresas, coordinando muchos equipos; valorado por su estructura y criticado por su posible pesadez.

**[SAST (Pruebas Estáticas de Seguridad de Aplicaciones)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Pruebas de seguridad que analizan el código fuente, el bytecode, o los binarios sin ejecutarlos para encontrar vulnerabilidades temprano en el desarrollo.

**SBOM (Lista de Materiales de Software)**: Un inventario formal y legible por máquina de los componentes y dependencias en una pieza de software, usado para gestionar el riesgo de cadena de suministro y vulnerabilidades.

**SCA (Análisis de Composición de Software)**: Herramientas que identifican componentes de código abierto y de terceros en una base de código y marcan vulnerabilidades conocidas y riesgos de licencia.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Un marco ágil que organiza el trabajo en iteraciones de duración fija (sprints) con roles, eventos, y artefactos definidos para entregar incrementos de valor.

**[Sección 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Una ley de EE. UU. que exige que las agencias federales hagan accesible su tecnología electrónica y de información para las personas con discapacidades, en la práctica alineada con las WCAG.

**Búsqueda semántica**: Búsqueda que coincide por significado en lugar de palabras clave exactas, típicamente comparando incrustaciones de la consulta y los documentos. A menudo se combina con la búsqueda léxica en un enfoque híbrido.

**[Malla de servicios](https://en.wikipedia.org/wiki/Service_mesh)**: Una capa de infraestructura dedicada, usualmente implementada con proxies sidecar, que maneja las preocupaciones de comunicación de servicio a servicio como TLS mutuo, reintentos, tiempos de espera, cambio de tráfico, y observabilidad, manteniéndolas fuera del código de la aplicación.

**Sidecar**: Un proceso o contenedor auxiliar desplegado junto a una instancia de aplicación principal para proveer capacidades de soporte (como un proxy de malla de servicios) sin cambiar la aplicación misma.

**[SIEM (Gestión de Información y Eventos de Seguridad)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Un sistema que agrega y correlaciona registros y eventos de seguridad a través de un entorno para permitir la detección, alertas, e investigación.

**[SLA (Acuerdo de Nivel de Servicio)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Un compromiso formal entre un proveedor de servicio y sus clientes que especifica los niveles de servicio esperados y las consecuencias de no cumplirlos.

**SLI (Indicador de Nivel de Servicio)**: Una medida cuantitativa de algún aspecto de la calidad del servicio, como la latencia de la solicitud o la tasa de error, que alimenta los SLO.

**SLO (Objetivo de Nivel de Servicio)**: Un valor objetivo o rango para un SLI que define el nivel deseado de fiabilidad, formando la base de los presupuestos de error.

**SLSA (Niveles de Cadena de Suministro para Artefactos de Software)**: Un marco de requisitos de seguridad graduados para mejorar la integridad y procedencia de los artefactos de software a través del proceso de construcción y liberación.

**SOAR (Orquestación, Automatización, y Respuesta de Seguridad)**: Herramientas y prácticas que automatizan y coordinan las operaciones de seguridad, como los manuales de triaje y respuesta, para mejorar la velocidad y la consistencia.

**SOC 2 (Controles de Sistema y Organización 2)**: Un marco y reporte de auditoría, basado en los Criterios de Servicios de Confianza de la AICPA, que evalúa los controles de una organización de servicio para la seguridad, disponibilidad, integridad de procesamiento, confidencialidad, y privacidad.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Cinco principios de diseño orientado a objetos (Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de Interfaces, e Inversión de Dependencias) que promueven código mantenible y flexible.

**[SOX (Ley Sarbanes-Oxley)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Legislación de EE. UU. que establece requisitos para el reporte financiero y los controles internos en las empresas públicas, con implicaciones para los sistemas de TI que respaldan los datos financieros.

**SPACE**: Un marco para medir la productividad del desarrollador a través de cinco dimensiones: Satisfacción y bienestar, Desempeño (Performance), Actividad, Comunicación y colaboración, y Eficiencia y flujo, advirtiendo contra las medidas de una sola métrica.

**[SRE (Ingeniería de Confiabilidad de Sitio)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Una disciplina que aplica enfoques de ingeniería de software a las operaciones, usando SLO, presupuestos de error, y automatización para ejecutar sistemas confiables a escala.

**SSDF (Marco de Desarrollo de Software Seguro)**: El marco del NIST (SP 800-218) de prácticas de desarrollo seguro de alto nivel, abarcando preparar la organización, proteger el software, producir software bien asegurado, y responder a las vulnerabilidades.

**[Análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis)**: Examinar el código fuente, bytecode, o binarios sin ejecutarlos para encontrar defectos, violaciones de estilo, y fallos de seguridad, típicamente mediante linters, verificadores de tipo, y analizadores dedicados cableados en el editor y el pipeline.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Una taxonomía de modelado de amenazas que categoriza las amenazas como Suplantación, Manipulación, Repudio, Divulgación de información, Denegación de servicio, y Elevación de privilegio.

## T

**[TCO (Costo Total de Propiedad)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: El costo completo de vida útil de un sistema o decisión, incluyendo la adquisición, la operación, el mantenimiento, y el eventual retiro, no solo el precio inicial.

**[TDD (Desarrollo Guiado por Pruebas)](https://en.wikipedia.org/wiki/Test-driven_development)**: Una práctica de escribir una prueba automatizada que falla antes que el código que la hace pasar, y luego refactorizar, en ciclos cortos y repetidos para guiar el diseño y asegurar la cobertura.

**[Deuda técnica](https://en.wikipedia.org/wiki/Technical_debt)**: El costo futuro implícito de elegir una solución expedita ahora en lugar de una mejor que tomaría más tiempo, que debe gestionarse deliberadamente en lugar de acumularse inconscientemente.

**TF-IDF (Frecuencia de Término-Frecuencia Inversa de Documento)**: Un esquema de ponderación clásico que puntúa la importancia de un término para un documento por qué tan a menudo aparece ahí, compensado por qué tan común es en todo el corpus. Sustenta gran parte de la clasificación de búsqueda léxica.

**[Teoría de restricciones](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Un enfoque de gestión que sostiene que el rendimiento de un sistema está limitado por un único cuello de botella en cualquier momento, así que los esfuerzos de mejora deberían enfocarse en esa restricción hasta que se mueva a otro lugar.

**[Modelado de amenazas](https://en.wikipedia.org/wiki/Threat_model)**: Una práctica estructurada de identificar, enumerar, y priorizar las amenazas potenciales a un sistema para que las defensas puedan diseñarse desde el principio.

**Trabajo penoso (toil)**: En SRE, el trabajo operativo manual, repetitivo, y automatizable que escala linealmente con un servicio y no provee valor duradero; reducirlo libera capacidad para la ingeniería.

**Desarrollo basado en tronco**: Una práctica de control de fuente en la que los desarrolladores integran cambios pequeños frecuentemente en una única rama compartida, minimizando las ramas de larga vida y el dolor de fusión.

**[Inferencia de tipos](https://en.wikipedia.org/wiki/Type_inference)**: Una característica de lenguaje que deduce los tipos de las expresiones automáticamente, dando gran parte de la seguridad del tipado estático sin requerir que cada tipo se escriba a mano.

**[Sistema de tipos](https://en.wikipedia.org/wiki/Type_system)**: El conjunto de reglas que usa un lenguaje para asignar y verificar tipos, capturando clases enteras de error antes de que el programa se ejecute y documentando la intención. Los sistemas de tipos van de dinámicos a estáticos y de débiles a fuertes.

## U

**Lenguaje ubicuo**: En el Diseño Guiado por el Dominio, un vocabulario compartido y preciso usado consistentemente por los desarrolladores y los expertos de dominio, y reflejado directamente en el código y los modelos.

**[UAT (Prueba de Aceptación del Usuario)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Pruebas realizadas por los usuarios finales o sus representantes para confirmar que un sistema satisface las necesidades del negocio antes de que se acepte para la liberación.

**[UX / UI (Experiencia de Usuario / Interfaz de Usuario)](https://en.wikipedia.org/wiki/User_experience)**: La Experiencia de Usuario es la calidad general de la interacción de una persona con un producto; la Interfaz de Usuario es la superficie visual e interactiva específica a través de la cual ocurre esa interacción.

## V

**[Objeto de valor](https://en.wikipedia.org/wiki/Value_object)**: En el Diseño Guiado por el Dominio, un objeto inmutable definido enteramente por sus atributos en lugar de una identidad distinta, como una cantidad de dinero o un rango de fechas.

**[Mapeo de flujo de valor](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Una técnica para dibujar cada paso desde la idea hasta el valor entregado, distinguiendo el tiempo que agrega valor del tiempo de espera, para que los cuellos de botella, las transferencias, y los ciclos de retrabajo se vuelvan visibles y mejorables.

**[Base de datos vectorial](https://en.wikipedia.org/wiki/Vector_database)**: Un almacén de datos optimizado para indexar y buscar vectores de incrustación de alta dimensión por similitud, una columna vertebral común de la búsqueda semántica y la generación aumentada por recuperación.

**Escalado vertical**: Aumentar la capacidad haciendo un solo nodo más poderoso ("escalar hacia arriba"), lo cual es simple pero en última instancia limitado por la máquina más grande disponible.

**[VCS (Sistema de Control de Versiones)](https://en.wikipedia.org/wiki/Version_control)**: Una herramienta, como Git, que registra los cambios a los archivos a lo largo del tiempo para que el historial pueda revisarse, las ramas puedan mantenerse, y el trabajo pueda coordinarse.

**[Escaneo de vulnerabilidades](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Inspección automatizada de sistemas, contenedores, o código contra bases de datos de debilidades y configuraciones erróneas conocidas. Es amplio y barato, y complementa la profundidad de las pruebas de penetración manuales.

## W

**[WCAG (Pautas de Accesibilidad al Contenido Web)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Un conjunto de pautas del W3C internacionalmente reconocidas, organizadas alrededor de los principios POUR y los niveles de conformidad A, AA, y AAA, para hacer accesible el contenido web.

**Mapa de Wardley**: Una técnica de estrategia visual que posiciona las capacidades por su valor para los usuarios y su madurez evolutiva, para informar las decisiones de construir/comprar e inversión.

**Límite de trabajo en progreso (WIP)**: Un tope sobre cuántos elementos pueden estar en una etapa dada de un flujo de trabajo a la vez, una práctica central de Kanban que mejora el flujo exponiendo los cuellos de botella y frenando la sobrecarga de demasiado trabajo paralelo.

**WSJF (Primero el Trabajo Ponderado Más Corto)**: Un método de priorización que secuencia el trabajo dividiendo su costo del retraso entre su duración estimada, para que los elementos más cortos, más sensibles al tiempo, y de mayor valor se hagan primero.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Una vulnerabilidad web en la que un atacante inyecta scripts maliciosos que se ejecutan en los navegadores de otros usuarios, potencialmente robando datos o secuestrando sesiones.

## Y

**[YAGNI (No Lo Vas a Necesitar)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Un principio que aconseja contra construir funcionalidad por especulación, bajo la premisa de que las necesidades anticipadas a menudo no se materializan y agregan costo y complejidad.

## Z

**[Confianza cero](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Un modelo de seguridad que no asume ninguna confianza implícita basada en la ubicación de red y verifica continuamente cada solicitud de acceso contra la identidad, el dispositivo, y el contexto, siguiendo la máxima "nunca confíes, siempre verifica".
