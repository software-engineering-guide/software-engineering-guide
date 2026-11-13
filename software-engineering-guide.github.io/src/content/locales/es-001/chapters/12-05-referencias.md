# 12.5 Referencias

Esta sección consolida el aparato de referencia de la guía: una tabla de correspondencia con el cuerpo de conocimiento SWEBOK, un índice de los estándares y marcos citados a lo largo del libro, y una bibliografía curada de lecturas recomendadas. Las fuentes por capítulo también aparecen en la sección *Referencias y lecturas adicionales* al final de cada capítulo.

---

# Tabla de correspondencia con SWEBOK

Esta guía está alineada con el **SWEBOK V4.0** (Cuerpo de Conocimiento de Ingeniería de Software) del IEEE Computer Society. Se cubren las 18 áreas de conocimiento; la tabla mapea cada una a los capítulos que la tratan, y la guía luego va mucho más allá de SWEBOK hacia la IA, los datos, la UX, DevOps, la sostenibilidad, el flujo, y la tecnología de interés público.

| Área de conocimiento SWEBOK V4.0 | Capítulos principales |
|---|---|
| 1. Requisitos de Software | 2.8, 11.1, 5.1 |
| 2. Arquitectura de Software | 3.1, 3.2, 3.3 |
| 3. Diseño de Software | 2.2, 3.1 |
| 4. Construcción de Software | 2.9, 2.1 |
| 5. Pruebas de Software | 2.4, 8.5 |
| 6. Operaciones de Ingeniería de Software | 9.1, 9.2, 9.3, 8.1 |
| 7. Mantenimiento de Software | 3.7, 3.6, 10.4 |
| 8. Gestión de Configuración de Software | 2.10, 2.6, 8.2 |
| 9. Gestión de Ingeniería de Software | 10.1, 10.6, 10.2 |
| 10. Proceso de Ingeniería de Software | 1.4, 10.7, 10.8 |
| 11. Modelos y Métodos de Ingeniería de Software | 2.12, 3.1, 2.2 |
| 12. Calidad de Software | 2.11, 2.4, 3.1 |
| 13. Seguridad de Software | 4.1, 4.2, 4.3, 4.4 |
| 14. Práctica Profesional de Ingeniería de Software | 10.5, 1.1, 1.3 |
| 15. Economía de la Ingeniería de Software | 10.10, 10.1, 9.4 |
| 16. Fundamentos de Computación | 2.13, 3.3, 3.4 |
| 17. Fundamentos Matemáticos | 2.13, 11.3 |
| 18. Fundamentos de Ingeniería | 2.13, 3.1 |

---

# Estándares y marcos

Este apéndice es un índice organizado de los estándares, marcos, y regulaciones reales referenciados a lo largo de la guía. Es una ayuda de navegación, no un manual de cumplimiento: siempre consulta la fuente autoritativa y, donde sea relevante, asesoría legal o de auditoría calificada para el texto actual y la aplicabilidad a tu contexto.

Las entradas se agrupan por dominio. Cada una nombra el estándar o marco, su organismo emisor, un alcance de una línea, y los capítulos o dominios donde es más relevante. Donde un nombre se abrevia comúnmente, se muestra la abreviatura. Los números de documento y títulos se dan solo donde están bien establecidos; no se incluyen URL.

## Cómo usar este apéndice

- Las **regulaciones** (por ejemplo, RGPD, HIPAA) son legalmente vinculantes dentro de su jurisdicción y sector. Establecen obligaciones, no solo buenas prácticas.
- Los **estándares** (por ejemplo, ISO/IEC 27001, WCAG) son especificaciones formales, a menudo certificables. Algunos son voluntarios; algunos son obligados por ley o contrato.
- Los **marcos** (por ejemplo, NIST CSF, NIST AI RMF) son guías estructuradas, usualmente voluntarias, que ajustas a tu perfil de riesgo.
- La aplicabilidad depende de la jurisdicción, el sector, los tipos de datos, y los términos contractuales. Muchas organizaciones deben satisfacer varios de estos a la vez.

## Seguridad y privacidad

| Estándar / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Requisitos para un Sistema de Gestión de Seguridad de la Información (SGSI). | 4.1-4.6 Seguridad y cumplimiento |
| ISO/IEC 27002 | ISO / IEC | Guía y conjunto de controles que respalda ISO/IEC 27001. | 4.1-4.4 Seguridad |
| ISO/IEC 27017 / 27018 | ISO / IEC | Controles de seguridad específicos de la nube (27017) y protección de PII en la nube (27018). | 4.3 Seguridad de infraestructura y nube; 4.5 Privacidad |
| Marco de Ciberseguridad del NIST (CSF) | Instituto Nacional de Estándares y Tecnología | Marco voluntario organizado alrededor de Gobernar, Identificar, Proteger, Detectar, Responder, Recuperar. | 4.1, 4.4 Fundamentos y operaciones de seguridad |
| NIST SP 800-53 | Instituto Nacional de Estándares y Tecnología | Catálogo de controles de seguridad y privacidad para sistemas de información. | 4.3, 4.6 Seguridad de la nube y cumplimiento |
| NIST SP 800-63 | Instituto Nacional de Estándares y Tecnología | Pautas de aseguramiento de identidad digital y autenticación. | 4.2, 4.3 Seguridad de aplicaciones e infraestructura |
| OWASP Top Ten | Open Worldwide Application Security Project | Los riesgos de seguridad más críticos de las aplicaciones web, actualizados periódicamente. | 4.2 Seguridad de aplicaciones |
| OWASP ASVS | Open Worldwide Application Security Project | Requisitos y pruebas graduados para verificar la seguridad de aplicaciones. | 2.4, 4.2 Pruebas y seguridad de aplicaciones |
| OWASP SAMM | Open Worldwide Application Security Project | Modelo de madurez para construir y evaluar un programa de seguridad de software. | 4.1 Fundamentos y cultura de seguridad |
| STRIDE | Originado en Microsoft | Taxonomía de modelado de amenazas para clasificar amenazas. | 4.2 Seguridad de aplicaciones |
| MITRE ATT&CK | MITRE | Base de conocimiento de tácticas y técnicas de adversarios para la detección y defensa. | 4.4 Operaciones de seguridad |
| SLSA | Open Source Security Foundation (OpenSSF) | Marco graduado para la integridad y procedencia de la cadena de suministro de software. | 4.2, 8.1, 10.3 Cadena de suministro y entrega |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Formatos estándar para listas de materiales de software. | 4.2, 10.3 Seguridad de aplicaciones y licenciamiento |
| PCI DSS | PCI Security Standards Council | Requisitos de seguridad para el manejo de datos de tarjetas de pago. | 4.2, 4.5, 4.6 Seguridad, privacidad, cumplimiento |

## Cumplimiento y gobierno

### Estados Unidos

| Regulación / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| HIPAA | Departamento de Salud y Servicios Humanos de EE. UU. | Salvaguardas para la información de salud protegida (PHI). | 4.5, 4.6 Privacidad y cumplimiento |
| SOX (Ley Sarbanes-Oxley) | Congreso de EE. UU. / SEC | Requisitos de reporte financiero y control interno para empresas públicas. | 4.6, 10.2 Cumplimiento y auditoría |
| FISMA | Congreso de EE. UU. | Requisitos de programa de seguridad de la información para agencias federales. | 4.3, 4.6 Seguridad de la nube y cumplimiento |
| FedRAMP | Administración de Servicios Generales de EE. UU. / Oficina de Gestión de Programa de FedRAMP | Autorización de seguridad estandarizada para servicios de nube usados por agencias federales. | 4.3, 4.6 Seguridad de la nube y cumplimiento |
| NIST SP 800-171 | Instituto Nacional de Estándares y Tecnología | Protección de información no clasificada controlada (CUI) en sistemas no federales. | 4.6 Cumplimiento (cadena de suministro de defensa) |
| CMMC | Departamento de Defensa de EE. UU. | Certificación de la madurez de ciberseguridad de contratistas de defensa. | 4.6 Cumplimiento (defensa) |
| FIPS 140-3 | Instituto Nacional de Estándares y Tecnología | Requisitos de seguridad para módulos criptográficos. | 4.3 Seguridad de infraestructura y nube |
| CCPA / CPRA | Estado de California | Derechos de privacidad del consumidor y obligaciones de negocio en California. | 4.5 Privacidad y protección de datos |

### Unión Europea y Reino Unido

| Regulación / estándar | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| RGPD | Unión Europea | Regulación integral sobre el procesamiento de datos personales. | 4.5, 4.6 Privacidad y cumplimiento |
| RGPD del Reino Unido / Ley de Protección de Datos de 2018 | Reino Unido | El régimen de protección de datos del Reino Unido posterior al Brexit. | 4.5, 4.6 Privacidad y cumplimiento |
| eIDAS | Unión Europea | Marco para la identificación electrónica y los servicios de confianza. | 4.2, 4.3 Seguridad |
| Directiva NIS2 | Unión Europea | Obligaciones de ciberseguridad para entidades esenciales e importantes. | 4.4, 4.6 Operaciones de seguridad y cumplimiento |
| DORA (Ley de Resiliencia Operativa Digital) | Unión Europea | Requisitos de resiliencia operativa para el sector financiero. | 9.1, 10.2 Fiabilidad y auditoría |
| Ley de IA de la UE | Unión Europea | Regulación basada en riesgo de los sistemas de IA (ver gobernanza de IA abajo). | 6.1, 6.5 Estrategia de IA e IA responsable |

## Accesibilidad

| Estándar | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Pautas para contenido web accesible, con niveles de conformidad A/AA/AAA. | 5.3 Accesibilidad; 5.1-5.6 UX y frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Roles, estados, y propiedades para aplicaciones de Internet ricas y accesibles. | 5.3, 5.6 Accesibilidad y frontend |
| Sección 508 | US Access Board / ley federal de EE. UU. | Requisitos de accesibilidad para las TIC federales de EE. UU., alineados con WCAG. | 5.3 Accesibilidad (gobierno de EE. UU.) |
| EN 301 549 | ETSI / CEN / CENELEC | Requisitos europeos de accesibilidad para la adquisición de TIC, alineados con WCAG. | 5.3 Accesibilidad (sector público de la UE) |
| ADA (Ley de Estadounidenses con Discapacidades) | Congreso de EE. UU. | Ley de derechos civiles que prohíbe la discriminación por discapacidad, aplicada a los servicios digitales. | 5.3 Accesibilidad |
| ISO/IEC 40500 | ISO / IEC | Adopción internacional de WCAG 2.0 como estándar formal. | 5.3 Accesibilidad |

## Gobernanza de IA

| Marco / regulación | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| Marco de Gestión de Riesgo de IA del NIST (AI RMF) | Instituto Nacional de Estándares y Tecnología | Marco voluntario para gobernar, mapear, medir, y gestionar el riesgo de IA. | 6.1, 6.5 Estrategia de IA e IA responsable |
| ISO/IEC 42001 | ISO / IEC | Requisitos para un Sistema de Gestión de IA (AIMS). | 6.1, 6.5 Gobernanza de IA |
| ISO/IEC 23894 | ISO / IEC | Guía sobre la gestión de riesgo específica de IA. | 6.5 IA responsable y de confianza |
| Ley de IA de la UE | Unión Europea | Obligaciones legales escalonadas por riesgo para proveedores e implementadores de sistemas de IA. | 6.1, 6.3, 6.5 Aplicaciones de IA y gobernanza |
| Principios de IA de la OCDE | Organización para la Cooperación y el Desarrollo Económicos | Principios basados en valores para la IA de confianza, influyentes en la política. | 6.5, 10.5 IA responsable y ética |

## Calidad y proceso

| Estándar / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Modelo de calidad de producto de software (idoneidad funcional, fiabilidad, seguridad, etc.). | 2.2, 2.4 Diseño y pruebas |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Procesos del ciclo de vida del software. | 1.4, 10.1 Formas de trabajar y gestión de programas |
| ISO 9001 | ISO | Requisitos para un Sistema de Gestión de Calidad general. | 10.2 Riesgo, auditoría, y aseguramiento |
| CMMI | ISACA / CMMI Institute | Modelo de madurez para la capacidad y mejora del proceso. | 10.1, 10.2 Gestión de programas y aseguramiento |
| Métricas DORA | DevOps Research and Assessment (Google Cloud) | Cuatro métricas clave de desempeño de entrega para equipos de software. | 8.1, 8.4, 9.1 Entrega, plataforma, fiabilidad |
| Marco SPACE | Investigadores de Microsoft / GitHub | Modelo multidimensional para medir la productividad del desarrollador. | 1.3, 8.4 Crecimiento y experiencia del desarrollador |
| ITIL | AXELOS / PeopleCert | Marco de prácticas de gestión de servicios de TI. | 9.1, 9.3 Fiabilidad y gestión de incidentes |

## Arquitectura

| Estándar / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Estándar para la descripción de arquitectura y los puntos de vista. | 2.7, 3.1 Documentación y fundamentos de arquitectura |
| TOGAF | The Open Group | Marco de arquitectura empresarial y método de desarrollo. | 3.1, 10.1 Arquitectura y gestión de portafolio |
| Modelo C4 | Comunidad (Simon Brown) | Enfoque de cuatro niveles para visualizar la arquitectura de software. | 2.7, 3.1 Documentación y arquitectura |
| arc42 | Comunidad (Starke / Hruschka) | Plantilla para estructurar la documentación de arquitectura. | 2.7, 3.1 Documentación y arquitectura |
| ADR | Práctica comunitaria | Registros ligeros de decisiones de arquitectura significativas. | 1.5, 2.7, 3.1 Toma de decisiones y documentación |

## Nube y DevOps

| Estándar / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Líneas base de configuración segura basadas en consenso para sistemas y nube. | 4.3, 8.2 Seguridad de infraestructura e IaC |
| Panorama y proyectos de CNCF | Cloud Native Computing Foundation | Ecosistema y estándares para la computación nativa de la nube (por ejemplo, Kubernetes). | 8.3 Contenedores y nativo de la nube |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Estándares abiertos para los formatos de imagen y tiempo de ejecución de contenedores. | 8.3 Contenedores y nativo de la nube |
| OpenTelemetry | Cloud Native Computing Foundation | Estándar neutral respecto al proveedor para la telemetría (trazas, métricas, registros). | 9.2 Observabilidad y monitoreo |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Motor de políticas de propósito general para la política como código. | 4.6, 8.2, 8.3 Cumplimiento, IaC, orquestación |
| Prácticas SRE | Google (ampliamente adoptado) | Enfoque basado en SLI/SLO/presupuesto de error para operar servicios confiables. | 9.1 Ingeniería de confiabilidad de sitio |
| Marco FinOps | FinOps Foundation | Prácticas para la gestión financiera de la nube y la responsabilidad de costo. | 9.4 Costo, sostenibilidad, software verde |

## Datos

| Estándar / marco | Organismo emisor | Alcance (una línea) | Capítulos / dominios principales |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Cuerpo de conocimiento que organiza las disciplinas de gestión de datos. | 7.1 Estrategia y gobernanza de datos |
| ISO/IEC 38505 | ISO / IEC | Gobernanza de los datos como activo organizacional. | 7.1 Gobernanza de datos |
| ISO 8000 | ISO | Estándares de calidad de datos y datos maestros. | 7.1, 7.2 Gobernanza e ingeniería de datos |
| Malla de datos | Comunidad (Zhamak Dehghani) | Enfoque descentralizado y orientado al dominio de los datos como producto. | 7.1, 7.2 Estrategia e ingeniería de datos |
| DCAM | EDM Council | Modelo de evaluación de capacidad de gestión de datos. | 7.1 Estrategia y gobernanza de datos |

## Notas sobre alcance y cambio

Los estándares y regulaciones evolucionan. Los números de versión (por ejemplo, WCAG 2.1 frente a 2.2, o los años de revisión de ISO) y los catálogos de control cambian con el tiempo, y siguen surgiendo nuevas leyes (como regulaciones de IA y resiliencia específicas del sector). Trata este apéndice como un mapa de partida: confirma la versión actual, la jurisdicción, y la aplicabilidad antes de confiar en cualquier entrada para una decisión de cumplimiento o adquisición. Donde los capítulos de la guía y este apéndice difieran en detalle, el documento fuente autoritativo siempre gobierna.


---

# Lecturas recomendadas

Este apéndice es una lista de lectura curada y anotada que abarca cada dominio de la guía. Favorece las obras que han moldeado la práctica a escala: clásicos reconocidos, referencias rigurosas, y los estándares y reportes contra los que se miden los equipos grandes, empresariales, y gubernamentales.

Cada entrada da el título y autor(es), seguido de una frase sobre por qué importa. La lista se organiza bajo las diez partes del libro. Lee selectivamente: elige las dos o tres obras más cercanas a tu dolor actual, no todo el estante. Donde una obra abarca varios dominios, se coloca donde es más útil; muchas pertenecen a varias partes.

Una nota sobre estándares: organismos como NIST, OWASP, W3C/WCAG, ISO, y el programa DORA publican documentos vivos que se revisan periódicamente. Cita y lee la versión actual; las anotaciones abajo describen su propósito duradero.

## Fundamentos: Cultura, Personas, y Proceso

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. El fundamento de investigación que muestra que el desempeño de entrega predice el desempeño organizacional, y define las métricas (ahora llamadas DORA) para medirlo.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Una novela de negocios que hace intuitivos el flujo, el trabajo en progreso, y las "Tres Vías" de DevOps tanto para líderes como para escépticos.
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**. Matthew Skelton y Manuel Pais. Un vocabulario práctico (equipos alineados a flujo, de plataforma, habilitadores, y de subsistema complicado) para diseñar organizaciones que producen buen software.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Marcos probados en campo para dimensionar equipos, gestionar el crecimiento organizacional, y tomar las decisiones recurrentes del liderazgo de ingeniería.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Define los arquetipos staff-plus y el camino de liderazgo técnico para quienes quieren impacto sin convertirse en gerentes.
- **The Manager's Path**. Camille Fournier. Una guía etapa por etapa desde líder técnico hasta ejecutivo que ancla los escalafones profesionales y la transición hacia la gestión.
- **The Staff Engineer's Path**. Tanya Reilly. Un compañero de la literatura staff-plus enfocado en el trabajo diario del liderazgo técnico, la influencia, y guiar sin autoridad.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco y Timothy Lister. El argumento duradero de que los problemas centrales del software son sociológicos, no técnicos.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. El origen de la ley de Brooks y la distinción entre complejidad esencial y accidental que todavía gobierna la dotación de personal y la programación.
- **The Fearless Organization: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. El fundamento de investigación para la cultura sin culpa y la seguridad que hace posible aprender del fracaso.
- **Thinking, Fast and Slow**. Daniel Kahneman. El relato definitivo del sesgo cognitivo, esencial para las entrevistas estructuradas, la calibración, y la toma de decisiones honesta.

## Oficio de la Programación y Calidad del Código

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt y David Thomas. El catálogo fundacional de hábitos profesionales (DRY, ortogonalidad, balas trazadoras) que define qué significa el oficio.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. El catálogo canónico de transformaciones que preservan el comportamiento y la disciplina de la mejora continua del código respaldada por pruebas.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Un estándar ampliamente usado (y debatido) para el nombramiento, las funciones, y la legibilidad que moldea las expectativas de revisión de muchos equipos.
- **Code Complete**. Steve McConnell. Un manual integral y referenciado por evidencia de prácticas de construcción que sigue siendo una línea base exhaustiva para la calidad de programación.
- **Test-Driven Development: By Example**. Kent Beck. La introducción original y práctica al ciclo rojo-verde-refactorizar y el diseño primero-la-prueba.
- **Working Effectively with Legacy Code**. Michael Feathers. El kit de herramientas definitivo para agregar pruebas a código que no las tiene y cambiarlo con seguridad, e indispensable para sistemas de larga vida.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman y Nat Pryce. Una demostración trabajada de TDD de afuera hacia adentro, simulacros, y la evolución de un diseño a través de pruebas.
- **A Philosophy of Software Design**. John Ousterhout. Un tratamiento agudo y con opinión de la complejidad, los módulos profundos, y la ocultación de información que desafía productivamente algo de la ortodoxia del "código limpio".

## Arquitectura y Sistemas

- **Designing Data-Intensive Applications**. Martin Kleppmann. La mejor referencia moderna individual sobre los intercambios del almacenamiento, la replicación, la partición, la consistencia, y el procesamiento de flujos a escala.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards y Neal Ford. Un amplio y actual estudio de los estilos arquitectónicos, las características, y el rol y la toma de decisiones del arquitecto.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Un tratamiento enfocado en decisiones de los intercambios de arquitectura distribuida, la granularidad de servicio, y la propiedad de datos.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Introduce las funciones de aptitud y la arquitectura diseñada para cambiar de forma segura con el tiempo.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. El origen de los contextos delimitados, el lenguaje ubicuo, y los agregados: el vocabulario del diseño de servicios moderno.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. La referencia para la descomposición, los límites de servicio, el despliegue, y las implicaciones organizacionales de los microservicios.
- **Monolith to Microservices**. Sam Newman. Un catálogo de patrones para la descomposición incremental, como la higuera estranguladora y la bifurcación por abstracción, sin una reescritura riesgosa de gran explosión.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. La referencia de patrones nombrados (repositorio, unidad de trabajo, y más) que dio un lenguaje compartido a los sistemas empresariales.
- **Enterprise Integration Patterns**. Gregor Hohpe y Bobby Woolf. El catálogo definitivo de patrones de mensajería que sustentan las arquitecturas guiadas por eventos y asíncronas.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. La fuente del disyuntor, el compartimento estanco, y otros patrones de estabilidad para sistemas que sobreviven la producción real.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). El catálogo históricamente decisivo de patrones orientados a objetos y un vocabulario de diseño compartido.

## Seguridad, Privacidad, y Confianza

- **Threat Modeling: Designing for Security**. Adam Shostack. La guía práctica y completa de STRIDE y el modelado de amenazas estructurado como práctica de ingeniería rutinaria.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. La referencia enciclopédica sobre cómo fallan los sistemas reales y cómo construir unos que resistan el ataque.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Un recorrido riguroso por el modelo de seguridad del navegador y las maneras sutiles en que las plataformas web traicionan los supuestos ingenuos.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Una guía de practicante para usar la criptografía correctamente y evitar los errores comunes y peligrosos.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). La síntesis de Google de la seguridad y la fiabilidad como propiedades entrelazadas diseñadas desde el principio.
- **Zero Trust Networks**. Evan Gilman y Doug Barth. Un tratamiento claro de los principios y la mecánica de la arquitectura de red de nunca confiar, siempre verificar.
- **OWASP Top 10**. OWASP Foundation. La línea base de consenso de los riesgos de seguridad de aplicaciones web más críticos, referenciada por la política y la auditoría en todo el mundo.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Una lista de verificación por niveles y comprobable de requisitos de seguridad adecuada para contratos y criterios de aceptación.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**. NIST. El catálogo de controles en el corazón de la seguridad federal de EE. UU. y la base para la autorización de FedRAMP y FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. La estructura ampliamente adoptada de identificar-proteger-detectar-responder-recuperar para organizar un programa de seguridad.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. La definición de referencia y las arquitecturas de referencia que anclan la mayoría de los programas de confianza cero empresariales y gubernamentales.

## UX, UI, y Diseño de Producto

- **The Design of Everyday Things**. Don Norman. El texto fundacional sobre las posibilidades de acción, los significantes, la retroalimentación, y el diseño centrado en el humano que aplica mucho más allá de los objetos físicos.
- **Don't Make Me Think, Revisited**. Steve Krug. El argumento conciso y duradero de la usabilidad autoevidente y el valor de las pruebas de usabilidad baratas y frecuentes.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. La referencia integral sobre el diseño de interacción, las personas, y el diseño dirigido por objetivos.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Un relato fundamentado de la construcción de sistemas de componentes consistentes y reutilizables y el lenguaje compartido detrás de ellos.
- **Refactoring UI**. Adam Wathan y Steve Schoger. Una guía práctica y basada en ejemplos del pulido visual para ingenieros que diseñan interfaces sin entrenamiento formal.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. La guía definitiva del diseño de contenido en lenguaje llano y enfocado en tareas.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Compañeros prácticos para construir interfaces que funcionan para todo el rango de habilidades humanas.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton y Whitney Quesenbery. Un puente guiado por principios entre los estándares de accesibilidad y la buena experiencia de usuario.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. El estándar referenciado internacionalmente (perceptible, operable, comprensible, robusto) detrás de la mayoría de las leyes de accesibilidad.
- **U.S. Web Design System (USWDS)**. Gobierno de EE. UU. Un ejemplo de trabajo de un sistema de diseño accesible y basado en estándares construido para servicios públicos a escala.

## Inteligencia Artificial y Aprendizaje Automático

- **Designing Machine Learning Systems**. Chip Huyen. La guía práctica líder para construir sistemas de AA de producción de extremo a extremo: datos, características, despliegue, y monitoreo.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Extiende la disciplina SRE (SLO, monitoreo, respuesta a incidentes) a los sistemas de aprendizaje automático.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. La referencia académica estándar para la teoría y los métodos que sustentan las redes neuronales modernas.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Una guía actual para diseñar, evaluar, y operar aplicaciones construidas sobre modelos base grandes.
- **Weapons of Math Destruction**. Cathy O'Neil. Un caso vívido para la responsabilidad algorítmica y los daños del mundo real de los modelos sin examinar, esencial para la IA del sector público.
- **Interpretable Machine Learning**. Christoph Molnar. Una referencia integral y disponible gratuitamente sobre los métodos de explicabilidad para los modelos y sus predicciones.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. El marco de referencia para gobernar, mapear, medir, y gestionar el riesgo de IA, cada vez más citado en la política y la adquisición.

## Datos, Analítica, y Perspectivas

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. Ralph Kimball y Margy Ross. La referencia canónica sobre los esquemas estrella y el modelado dimensional para la analítica.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. La guía autoritativa para ejecutar experimentos que producen resultados confiables y accionables a escala.
- **Fundamentals of Data Engineering**. Joe Reis y Matt Housley. Un mapa neutral respecto al proveedor del ciclo de vida de datos moderno y las prácticas de ingeniería detrás de él.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. El texto fundador del enfoque orientado al dominio y centrado en el producto para organizar los datos a escala.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Una guía práctica para la visualización de datos honesta y clara y comunicar perspectivas a los tomadores de decisiones.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. La obra fundacional sobre la integridad gráfica, la tinta de datos, y la ética de mostrar datos honestamente.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. El marco de referencia integral para la gobernanza de datos, la administración, la calidad, y la catalogación.
- **The Book of Why**. Judea Pearl y Dana Mackenzie. Una introducción legible a la inferencia causal, vital para pasar de la correlación a decisiones defendibles.

## Automatización, DevOps, e Ingeniería de Plataforma

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. El manual integral que traduce las "Tres Vías" en prácticas concretas para el flujo, la retroalimentación, y el aprendizaje continuo.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble y David Farley. El texto fundacional sobre los pipelines de despliegue, la automatización, y liberar software de forma segura y frecuente.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. La referencia sobre tratar la infraestructura como software: módulos, pruebas, inmutabilidad, y deriva.
- **Team Topologies**. Matthew Skelton y Manuel Pais. (Ver Fundamentos.) También esencial aquí para moldear los equipos de plataforma y la experiencia del desarrollador que proveen.
- **Kubernetes Patterns**. Bilgin Ibryam y Roland Huß. Un catálogo de patrones reutilizables para diseñar aplicaciones nativas de la nube en Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Cómo las prácticas de ingeniería como las pruebas, la revisión, las herramientas, y la gestión de dependencias escalan a decenas de miles de ingenieros a lo largo de décadas.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). El manifiesto conciso e influyente para construir servicios portables, escalables, y nativos de la nube.
- **DORA State of DevOps Report**. DORA / Google Cloud (anual). El programa de investigación continuo detrás de las cuatro métricas clave de entrega y las capacidades que impulsan el desempeño.

## Operaciones, Fiabilidad, y Observabilidad

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). El texto fundacional que define los SLI, SLO, presupuestos de error, y la disciplina de la ingeniería de la fiabilidad.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). El compañero práctico con ejemplos concretos, SLO trabajados, y guía de implementación.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. La definición moderna de la observabilidad, los datos de alta cardinalidad, y la depuración de lo desconocido-desconocido en producción.
- **Implementing Service Level Objectives**. Alex Hidalgo. Una guía exhaustiva y práctica para diseñar, medir, y usar bien los SLO y los presupuestos de error.
- **Release It!**. Michael T. Nygard. (Ver Arquitectura.) También fundacional aquí para los patrones de estabilidad de producción y la operación de sistemas resilientes.
- **The Art of Capacity Planning**. Arun Kejariwal y John Allspaw. Un enfoque basado en datos para pronosticar la demanda y planificar la capacidad de sistemas en crecimiento.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal y Nora Jones. El tratamiento definitivo de inyectar deliberadamente fallos para construir confianza en la resiliencia del sistema.
- **Google SRE Book, Chapter on Postmortems**. Google. El modelo ampliamente emulado para las autopsias sin culpa y aprender de los incidentes.

## Empresa, Gobierno, y el Interés Público

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. El estudio esencial de cómo se sostiene realmente el código abierto, y la carga del mantenedor detrás de las dependencias de las que dependen las empresas.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Un relato claro de por qué falla la tecnología del sector público y cómo la reforma enfocada en la entrega puede arreglarlo.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lecciones del Servicio Digital del Gobierno del Reino Unido sobre transformar los servicios públicos entregando, no planificando.
- **Project to Product**. Mik Kersten. El Marco de Flujo para cambiar las grandes empresas del financiamiento basado en proyectos a flujos de valor de producto duraderos.
- **Escaping the Build Trap**. Melissa Perri. Cómo las organizaciones confunden la entrega con el resultado, y cómo la gestión de productos lo arregla, con relevancia directa para la gobernanza de portafolio y programas.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Un conjunto conciso de jugadas para entregar servicios digitales gubernamentales efectivos y centrados en el usuario.
- **GOV.UK Service Manual and Service Standard**. Servicio Digital del Gobierno del Reino Unido. Un estándar de trabajo, publicado, para construir buenos servicios públicos, ampliamente emulado por otros gobiernos.
- **NIST SP 800-37: Risk Management Framework**. NIST. El marco de proceso detrás de la autorización para operar (ATO) y el monitoreo continuo en los sistemas federales de EE. UU.
- **The FinOps Foundation Framework**. FinOps Foundation. El modelo de referencia para la visibilidad, optimización, y responsabilidad de costo de la nube entre finanzas e ingeniería.

## Cómo usar esta lista

- **Empieza por tu dolor.** Si los despliegues son lentos y aterradores, lee *Accelerate*, *Continuous Delivery*, y los reportes de *DORA* antes que nada más.
- **Lee para la década, no para el sprint.** Prefiere las obras que explican principios duraderos sobre las atadas a una versión específica de una herramienta.
- **Verifica la edición actual de los estándares.** NIST, OWASP, WCAG, ISO, y DORA revisan sus publicaciones; trabaja siempre desde la última versión y anota la versión en tus propias políticas.
- **Construye un estante compartido.** Un equipo que ha leído dos o tres de estos libros en común discute menos y decide más rápido, porque comparte un vocabulario y un conjunto de puntos de referencia.
- **Ver también el capítulo 12.5** para el índice completo de estándares y marcos de referencia, y el **capítulo 12.6** sobre cómo secuenciar la adopción de las prácticas que describen estas obras.
