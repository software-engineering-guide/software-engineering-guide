# 2.3 Interfaces de programación de aplicaciones y diseño de interfaces

## Visión general y motivación

Una [API](https://en.wikipedia.org/wiki/API) (interfaz de programación de aplicaciones) es el contrato mediante el cual un componente de software ofrece su capacidad a otro. Es el punto de encuentro entre equipos, sistemas y organizaciones, y es lo más duradero y costoso que se puede concebir mal. La firma de una función interna se puede refactorizar con total libertad. Una API publicada es otra cosa: es una promesa dirigida a consumidores que quizá nunca se conozca, y romperla es romper a quienes dependen de ella. A medida que las organizaciones descomponen los [monolitos](https://en.wikipedia.org/wiki/Monolithic_application) en servicios y abren sus capacidades a socios externos y al público, la API se convierte en la principal superficie de producto y en el mayor riesgo de integración.

Para equipos de gran envergadura, las APIs son lo que permite que cada persona trabaje con autonomía. Una bien diseñada permite cambiar los componentes internos sin coordinarse con cada uno de los consumidores, que es, en esencia, el propósito de un límite de servicio. Una mal diseñada filtra detalles internos, obliga a un despliegue sincronizado y convierte un conjunto de servicios en un monolito distribuido: servicios separados por la arquitectura, pero tan acoplados que deben compilarse y desplegarse conjuntamente. La calidad del diseño de su API determina en gran medida hasta qué punto sus equipos pueden moverse con independencia.

En entornos empresariales y del sector público, las APIs asumen además obligaciones de cumplimiento normativo, seguridad y longevidad. Una API del sector público puede estar obligada a seguir [estándares abiertos](https://en.wikipedia.org/wiki/Open_standard), mantener estabilidad durante años y atender a desarrolladores externos con los que no es posible coordinarse. Las APIs empresariales sustentan integraciones con socios bajo acuerdos de nivel de servicio contractuales. Todo ello eleva el listón en cuanto a disciplina de versionado, [compatibilidad hacia atrás](https://en.wikipedia.org/wiki/Backward_compatibility), gobernanza y experiencia del desarrollador.

## Principios clave

- Diseñe el contrato primero. La interfaz es una decisión de producto deliberada, no un subproducto de la implementación.
- Optimice para la experiencia del consumidor, no para su propia conveniencia.
- Trate la compatibilidad hacia atrás como un compromiso. Los cambios incompatibles requieren una nueva versión y una vía de migración.
- Haga que lo fácil sea lo correcto: valores predeterminados sensatos, errores previsibles, convenciones consistentes.
- Diseñe para el fallo. La [idempotencia](https://en.wikipedia.org/wiki/Idempotence) (una petición repetida produce el mismo efecto que una sola), los reintentos, la paginación y el [control de tasa](https://en.wikipedia.org/wiki/Rate_limiting) son preocupaciones de primer orden, no añadidos de última hora.
- Elija el estilo de protocolo que se ajuste a la interacción, no al capricho de moda.
- gobierne las APIs como productos, con propietarios, ciclos de vida y documentación.

## Recomendaciones

### Trabaje con enfoque API-first y basado en contratos

Defina y revise el contrato de la API, incluyendo sus recursos, operaciones, esquemas y semántica de errores, antes de escribir la implementación. Utilice una especificación legible por máquina de modo que el contrato pueda generar documentación, plantillas de cliente y servidor, servidores simulados y validaciones. Así, los consumidores pueden comenzar a integrarse contra el simulado mientras usted construye, y el contrato se convierte en la única fuente de verdad frente a la que ambas partes prueban.

### Eliga el estilo de interacción con deliberación

Elija entre [REST](https://en.wikipedia.org/wiki/REST) (transferencia de estado representacional), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) y [mensajería orientada a eventos](https://en.wikipedia.org/wiki/Event-driven_architecture) en función de la naturaleza de la interacción, no de preferencias personales. Utilice REST para interfaces orientadas a recursos, de amplia interoperabilidad y aptas para almacenamiento en caché. Use GraphQL cuando distintos clientes necesiten lecturas flexibles y agregadas sobre un grafo enriquecido. Emplee gRPC para llamadas de alto rendimiento y fuertemente tipadas entre servicios internos. Recurra a la mensajería orientada a eventos para flujos de trabajo asíncronos y desacoplados y para propagar cambios de estado. Muchos sistemas de gran escala emplean varios estilos a la vez, cada uno donde encaja.

### Versione y deprecie con disciplina

Adopte una estrategia de versionado explícita y una política de deprecación publicada: cómo clasifica los cambios, cuánto tiempo mantiene versiones antiguas y cómo notifica a los consumidores. Trace una línea clara entre cambios compatibles hacia atrás (añadir campos opcionales, nuevos endpoints) y cambios incompatibles (eliminar o renombrar campos, cambiar tipos o semánticas). Nunca reaproveche el significado de un campo existente. Otorgue a los consumidores ventanas de solapamiento para migrar y comuníqueles los plazos con antelación suficiente.

### Haga que la semántica de errores sea consistente y legible por máquina

Devuelva errores estructurados y previsibles: códigos estables y legibles por máquina, mensajes comprensibles para el humano y suficiente contexto para actuar sobre ellos, sin filtrar información interna sensible. Utilice la misma semántica de estados en cada endpoint, de modo que los clientes puedan manejar los errores de forma uniforme. Documente cada error con el que un consumidor pueda encontrarse.

### Integre idempotencia, paginación y control de tasa

Haga que las operaciones de escritura sean seguras ante reintentos mediante la aceptación de claves de idempotencia, de modo que un cliente que reintente tras un temporizador agotado no genere un doble cargo ni una creación duplicada. Pagine cada endpoint de listado desde el primer día y prefiera la paginación por cursores para conjuntos de datos extensos o en constante cambio. Establezca y documente límites de tasa, y devuelva al cliente el estado actual del límite para que pueda reducir su ritmo de forma gradual.

### Governe las APIs e invierta en la experiencia del desarrollador

Trate cada API como un producto, con un propietario, un ciclo de vida y una entrada en el catálogo. Establezca una revisión de diseño o un comité de estándares de API para que las interfaces mantengan la coherencia entre equipos. Invierta en la experiencia del desarrollador: documentación de referencia precisa, guías de inicio rápido, ejemplos, un entorno de pruebas y un registro de cambios. En un ecosistema amplio, un portal o catálogo que haga las APIs descargables y descubribles es imprescindible.

## Compensaciones: ventajas y desventajas

| Estilo | Mejor para | Ventajas | Desventajas |
|---|---|---|---|
| REST / HTTP | APIs públicas y orientadas a recursos | Universal, apto para caché, sencillo, interoperable | Exceso o insuficiencia de datos; muchos viajes de ida y vuelta; contratos débiles si no se especifican |
| GraphQL | Lecturas flexibles para clientes diversos | Consultas definidas por el cliente; un único endpoint; esquema fuerte | Complejidad en caché y control de tasa; riesgo de consultas costosas; mayor complejidad del servidor |
| gRPC | Llamadas internas de alto rendimiento | Rápido, compacto, fuertemente tipado, con streaming | Pobre compatibilidad con navegadores; menos legible para el humano; herramientas más pesadas |
| Orientado a eventos | Flujos asíncronos y desacoplados | Acoplamiento débil; escalable; resistente | Dificultad para razonar sobre el estado; consistencia eventual; complejidad operativa |

Las estrategias de versionado suponen un compromiso entre estabilidad y mantenimiento. Soportar muchas versiones antiguas protege a los consumidores, pero multiplica el código que hay que mantener y probar. La compatibilidad hacia atrás sacrifica la libertad propia por la estabilidad del consumidor, normalmente el intercambio correcto para una API de uso amplio. La perspectiva general: el coste de una mala decisión de API lo pagan todos los consumidores a lo largo de toda la vida de la interfaz. Por eso conviene invertir más esfuerzo en el diseño del límite que en casi cualquier otro lugar.

## Preguntas para debatir con su equipo

1. **¿Cómo clasifican un cambio como compatible hacia atrás o como incompatible, y qué control automático detecta una rotura silenciosa antes de que se despliegue?** Este capítulo traza una línea tajante: añadir campos opcionales y nuevos endpoints es seguro, mientras que eliminar o renombrar campos, cambiar tipos o reaprovechar el significado de un campo rompe a los consumidores. En un equipo amplio, quien introduce el cambio rara vez ve a todos los consumidores, de modo que un ajuste «menor» puede romper silenciosamente a socios con los que nunca se comunica. Lleva a la reunión la señal concreta: ¿ejecutan controles automáticos de compatibilidad de contrato en la integración continua frente a la especificación publicada, o se fían de que alguien recuerde la norma? En entornos empresariales y del sector público, donde un cambio incompatible obliga a una migración coordinada entre todos los socios y puede abarcar cambios de proveedor y de administración, el coste escala con el número de consumidores. Definan las reglas de clasificación e incorporen un punto de control de compatibilidad, de modo que un cambio incompatible haga fallar la compilación en lugar de una integración.

2. **¿Qué primitivas de fiabilidad (claves de idempotencia, paginación y control de tasa) son obligatorias en cada nuevo endpoint desde el primer día?** El capítulo sostiene que son preocupaciones de primer orden, porque añadir una clave de idempotencia a un endpoint de cobro ya en producción o incorporar paginación a una lista que ya está en uso es en sí mismo un cambio incompatible. Un ecosistema amplio lo amplifica: un endpoint que funciona en pruebas se colapsa ante el volumen real de datos, y una escritura no idempotente convierte un leve fallo de red en cargos duplicados. Lleve a la discusión la evidencia de qué endpoints actuales carecen de estos elementos y qué ocurriría ante una tormenta de reintentos. Hagan que los valores predeterminados sean innegociables para los nuevos endpoints: paginación por cursores en cada listado, claves de idempotencia en cada escritura, límites de tasa documentados que devuelvan su estado actual. Así convierten una migración forzada futura en un hábito de diseño de una sola vez.

3. **¿Diseñan y revisan el contrato realmente antes de escribir la implementación, o la interfaz se escapa del código?** La recomendación API-first pide una especificación legible por máquina, revisada de antemano, que genere documentación, plantillas y servidores simulados y permita a los consumidores integrarse contra el simulado mientras se construye. Cuando el contrato va a la zaga de la implementación, la interfaz expone la estructura de la base de datos interna y se desplaza cada vez que lo hace la implementación, que es el antipatrón más grave de este capítulo. La señal a examinar: ¿un consumidor puede empezar a integrarse contra su simulado hoy mismo, o debe esperar a que el backend esté funcionando? Para APIs públicas y de socios, donde la interfaz es la superficie de producto y lo más caro de mal diseñar, dedicar un día al contrato ahorra semanas de intercambio de soporte. Hagan que la revisión del contrato sea un paso obligatorio antes de iniciar la implementación.

4. **Cuando dos equipos necesitan exponer la misma capacidad, ¿qué estilo de interacción prevalece y quién tiene la autoridad para negarse a un cuarto protocolo?** Este capítulo indica elegir REST, GraphQL, gRPC o mensajería orientada a eventos según la adecuación de la interacción, pero a gran escala el riesgo real es que cada equipo elija su favorito y los consumidores se enfrenten a una convención distinta en cada endpoint. Una gran organización paga esa fragmentación en bibliotecas de cliente, portales, monitorización y en la carga cognitiva de cada integrador que ahora debe aprender cuatro idiomáticos en vez de uno. Lleva al debate el inventario de protocolos ya en producción, la interacción para la que cada uno se eligió y los consumidores que abarcan más de uno. La consideración contraria es legítima: un valor predeterminado compartido reduce la dispersión, pero un mandato rígido obliga a forzar problemas de forma gRPC en un hueco de forma REST. Nombran el organismo de estándares o la revisión de arquitectura que gestiona el proceso de excepción, porque en entornos empresariales y del sector público la proliferación de estilos se convierte en un impuesto permanente sobre la integración y en un problema difícil de revertir una vez que los socios dependen de cada uno.

5. **¿Cuál es su política de deprecación publicada y pueden demostrar que honran el periodo de soporte que anuncian?** El capítulo trata el versionado y la deprecación como disciplina: una política escrita sobre cuánto tiempo viven las versiones antiguas, cómo se notifica a los consumidores y qué solapamiento reciben para migrar. Una promesa que no se puede cumplir es peor que ninguna, porque un ecosistema amplio incluye consumidores a los que nunca se habla que seguirán llamando a una versión retirada hasta que se rompan en producción. Lleva a la discusión la evidencia: cuántas versiones activas se mantienen hoy, el uso real de cada una, si se puede identificar qué consumidores aún llaman a un endpoint deprecado y con cuánta antelación se anunció su última retirada. La presión contrapuesta es entre el coste de mantenimiento y la estabilidad del consumidor, y ambas son reales. Para socios empresariales bajo niveles de servicio contractuales y APIs del sector público que deben sobrevivir a cambios de administración y de proveedor, la ventana de soporte es un compromiso que puede superar la vida del equipo que lo estableció; decidan quién lo posee y cómo se verifica que una retirada es segura antes de que ocurra.

6. **¿Cómo saben que la experiencia del desarrollador es buena, o lo suponen porque la API funciona para ustedes?** Este capítulo presenta cada API como un producto cuya adopción depende de documentación de referencia precisa, guías de inicio rápido, ejemplos, un entorno de pruebas, un registro de cambios y un catálogo descargable. Los equipos confunden habitualmente que «la API funciona» con «la API es usable», y la brecha se manifiesta en tickets de soporte, integraciones fallidas y consumidores que renuncian en silencio. Lleva señales medibles en lugar de opiniones: tiempo hasta la primera llamada exitosa para un integrador nuevo, volumen de tickets de soporte por endpoint, el grado de desactualización de la documentación publicada frente al contrato en vivo, y si un recién llegado puede autoatenderse desde el portal sin escribir a su equipo. La tensión es que la documentación y los portales consumen esfuerzo real que compite con el lanzamiento de funcionalidades, pero en un ecosistema amplio una mala experiencia del desarrollador transfiere el coste de integración a cientos de consumidores a la vez. En el sector público, donde una API abierta atiende a desarrolladores externos con los que no se puede coordinar y la transparencia suele estar mandatada, una interfaz usable, bien documentada y descargable forma parte de la obligación de rendición de cuentas, no un extra.

## Perspectiva por sector

**Startup.** Con dos o tres ingenieros y sin tiempo para ceremonias, mantenga el contrato ligero pero real: una única especificación legible por máquina contra la que sus dos clientes piloto puedan integrarse mientras se construye. No es momento de montar un portal de API, un catálogo ni un comité de gobernanza, pero sí fijen los dos hábitos que resultan dolorosos de añadir después: claves de idempotencia en las escrituras y paginación por cursores en los listados, porque incorporarlos a un endpoint ya en producción es un cambio incompatible que no se pueden permitir. Prefiera un único estilo de interacción, casi siempre REST, para no arrastrar dispersión de protocolos al primer año.

**Pequeña y mediana empresa.** Sin un especialista en APIs y con un presupuesto ajustado, apoye en herramientas que generen documentación, servidores simulados y plantillas de cliente a partir de una especificación, de modo que un generalista pueda mantener la interfaz sin un conocimiento profundo de protocolos. Pese bien la opción de comprar frente a construir: un portal de API o una plataforma de gestión de API de catálogo le da control de tasa, claves y un portal para desarrolladores que de otro modo tendría que construir a medida. Mantenga la superficie pequeña y las convenciones consistentes, pues cada endpoint adicional y cada formato de error singular es algo que un equipo reducido debe sostener para siempre.

**Empresa.** En varias equipos autónomos, el problema central es la consistencia sin convertirse en cuello de botella: una guía de estilo compartida, una revisión de estándares de API, un catálogo que haga las interfaces descargables y controles automáticos de compatibilidad hacia atrás en la integración continua, de modo que una rotura silenciosa haga fallar la compilación en lugar de una integración. Gobiernes cada API como un producto con un propietario nominal, un ciclo de vida y una política de deprecación publicada, y mida la adopción, la carga de soporte y la frecuencia de cambios incompatibles para que el portafolio se mantenga sano. Estándarice los estilos de interacción y las reglas de versionado a nivel de organización, porque a esa escala la fragmentación es el default costoso.

**Sector público.** Las reglas de contratación, los mandatos de estándares abiertos y la rendición de cuentas pública condicionan cada elección. Publique el contrato de forma abierta, cumpla los estándares abiertos mandados y proporcione un entorno de pruebas y documentación de referencia para que los desarrolladores externos, con los que no es posible coordinarse, se integren por sí mismos. Trate la compatibilidad hacia atrás a largo plazo como un requisito de política, pues las integraciones deben sobrevivir a cambios de administración y de proveedor, y los cambios incompatibles deben ser raros, fuertemente gobernados y anunciados con amplia antelación. Mantenga la API y su documentación lo suficientemente transparentes para soportar el escrutinio público y de auditoría, y evite formatos propietarios que atraparían a una futura administración.

## Ejemplos

**Startup.** Una startup en fase semilla que publica su primera API externa redacta el contrato como una especificación legible por máquina antes de programar, para que sus dos clientes piloto puedan integrarse contra un simulado mientras el backend aún se construye. Aun con solo un puñado de consumidores, añade claves de idempotencia al endpoint de cobro y paginación por cursores a cada listado, porque incorporarlos una vez que los socios dependen de la API supondría un cambio incompatible que no puede permitirse. El contrato anticipado cuesta un día y ahorra semanas de idas y venidas de soporte.

**Empresa.** Una gran compañía de pagos expone una API REST pública a miles de comercios. Cada endpoint de escritura acepta una clave de idempotencia, de modo que un reintento por red nunca genera un cargo duplicado. Cada endpoint de listado usa paginación por cursores. Los errores llevan códigos estables documentados en una referencia pública. Una política formal de deprecación garantiza una ventana de soporte prolongada para cualquier versión, con aviso anticipado y guías de migración. Esta disciplina es una ventaja competitiva: los integradores confían en que la API no les fallará bajo sus pies.

**Sector público.** Un servicio digital nacional publica una API abierta para datos de ciudadanos, siguiendo los estándares abiertos mandados y un proceso de diseño API-first. El contrato se especifica y se revisa antes de la construcción, se publica en el catálogo central de APIs del gobierno y se sirve junto a un entorno de pruebas, para que los desarrolladores de terceros, que no pueden coordinarse individualmente, se integren por sí mismos. La compatibilidad hacia atrás a largo plazo es un requisito de política, porque las integraciones deben sobrevivir a cambios de administración y de proveedor. Los cambios incompatibles, por tanto, son escasos y fuertemente gobernados.

## Justificación de negocio: motivaciones, retorno de inversión y coste total de propiedad

Un buen diseño de API reduce el coste de integración, que suele ser el mayor al conectar sistemas y incorporar socios. Con una API clara, estable y bien documentada, los consumidores integran en días sin un solo ticket de soporte. Una mala API genera una carga de soporte interminable, integraciones fallidas y daño reputacional. Cuando la API es el propio producto, la experiencia del desarrollador impulsa directamente la adopción y los ingresos.

El mayor coste oculto son los cambios incompatibles. Cada uno de ellos obliga a una migración coordinada entre todos los consumidores, equipos internos y socios externos por igual, y el coste total escala con el número de consumidores y la dificultad de que se desplacen al unísono. Invertir de antemano en diseño basado en contratos, compatibilidad hacia atrás y disciplina de versionado evita esos eventos de migración forzada, costosos y a escala de toda la organización. Cuando hable con la dirección, presente la calidad de la API como el punto de palanca para la autonomía de los equipos, el crecimiento del ecosistema de socios y la evitación de migraciones forzada onerosas. Registre el tiempo de integración, el volumen de tickets de soporte y la frecuencia de cambios incompatibles como su evidencia.

## Antipatrones y errores habituales

- **APIs de primero la implementación:** la interfaz filtra la estructura de la base de datos interna y cambia cada vez que lo hace la implementación.
- **Cambios incompatibles silenciosos:** reaprovechar un campo o endurecer una validación sin subir de versión rompe a los consumidores de forma impredecible.
- **Interfaces verbosas:** diseños que requieren muchos viajes de ida y vuelta para una sola operación lógica, perjudicando el rendimiento y la usabilidad.
- **Convenciones inconsistentes:** cada endpoint inventa su propio sistema de nombres, su formato de error y su paginación, de modo que los clientes no pueden generalizar.
- **Sin paginación ni control de tasa:** endpoints que funcionan en pruebas y se colapsan ante el volumen o la carga real.
- **Escrituras no idempotentes:** los reintentos producen duplicados; un leve fallo de red corrompe los datos.
- **Proliferación de versiones:** demasiadas versiones activas sin deprecación, multiplicando el mantenimiento hasta hacerlo ingovernable.
- **La documentación como añadido de última hora:** referencias no documentadas o desactualizadas que trasladan todo el coste de integración a los consumidores.

## Modelo de madurez

- **Nivel 1, Iniciar:** las APIs emergen de la implementación como un subproducto; no hay convenciones compartidas; la interfaz filtra la estructura interna de la base de datos; los cambios incompatibles son frecuentes, no anunciados y se descubren cuando la integración de un consumidor falla.
- **Nivel 2, Desarrollar:** algunos equipos siguen convenciones REST básicas, versionan de forma informal y redactan documentación a mano, pero la práctica es inconsistente entre equipos; la idempotencia, la paginación y el control de tasa aparecen en algunos endpoints y no en otros; los consumidores siguen aprendiendo las peculiaridades de cada API caso por caso.
- **Nivel 3, Estandarizar:** el diseño basado en contratos con especificaciones legibles por máquina está documentado y se aplica a toda la organización; una política de deprecación publicada, una semántica de errores consistente y la obligatoriedad de idempotencia, paginación por cursores y control de tasa se aplican a cada nuevo endpoint; una guía de estilo compartida y una revisión de estándares de API mantienen las interfaces consistentes entre equipos.
- **Nivel 4, Gestionar:** el portafolio de APIs se mide y controla frente a líneas base: controles automáticos de compatibilidad hacia atrás en la integración continua detienen cada cambio, y se registra el tiempo hasta la primera llamada exitosa, el volumen de tickets de soporte por endpoint, la frecuencia de cambios incompatibles, el número de versiones activas y el uso por endpoint, de modo que las decisiones de deprecación y diseño se apoyen en evidencia en lugar de opinión. Cada API es un producto gobernado en un catálogo con un propietario nominal, y las métricas disparan una acción cuando un servicio se desvía de sus objetivos.
- **Nivel 5, Orquestar:** la estrategia de API se mejora de forma continua e integrada a lo largo de toda la organización; el catálogo, el portal, las reglas de versionado y los puntos de control de compatibilidad operan como un único sistema; la organización retira, consolida y redefine el alcance de las interfaces con regularidad, basándose en la adopción y el coste medidos; los estándares de estilo de interacción y versionado se adaptan a medida que el ecosistema, los socios y la tecnología evolucionan, y los cambios incompatibles son escasos y bien gestionados.

## Ideas para la discusión

- ¿Cómo deciden cuándo una API interna es lo bastante estable para publicarse de forma externa?
- ¿Cuál es el periodo de soporte adecuado para versiones deprecadas en su contexto, y quién asume ese coste?
- ¿Dónde deberían GraphQL o gRPC sustituir a REST internamente y dónde añadirían más complejidad que valor?
- ¿Cómo se impone la consistencia de la API entre muchos equipos autónomos sin convertirse en un cuello de botella?
- ¿Cómo deberían las APIs consumibles por IA y las interfaces de herramientas para agentes modificar sus convenciones de diseño?
- ¿Qué controles automáticos pueden detectar cambios incompatibles hacia atrás antes de que se desplieguen?

## Puntos clave

- Diseñe el contrato primero; la API es un producto y una promesa de larga duración.
- La compatibilidad hacia atrás protege a los consumidores; los cambios incompatibles requieren una nueva versión y una vía de migración.
- Elija REST, GraphQL, gRPC o eventos según la adecuación de la interacción, no según la moda.
- Integre idempotencia, paginación, control de tasa y errores consistentes desde el primer día.
- Governe las APIs como productos, con propietarios, catálogos y una experiencia del desarrollador sólida.

## Referencias y lectura complementaria

- Roy Fielding, *Estilos arquitectónicos y el diseño de software basado en red para arquitectura* (tesis doctoral)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* y *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- Especificación OpenAPI; JSON Schema (como estándares de referencia)
- Martin Kleppmann, *Diseño de aplicaciones intensivas en datos*

