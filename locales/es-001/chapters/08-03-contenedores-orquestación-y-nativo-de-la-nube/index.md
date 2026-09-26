# 8.3 Contenedores, orquestación, y nativo de la nube

## Presentación y motivación

Un [contenedor](https://en.wikipedia.org/wiki/OS-level_virtualization) empaqueta una aplicación junto con sus dependencias en una única unidad portable y aislada. Se ejecuta de la misma manera en una laptop, en un entorno de prueba, y en producción. Las plataformas de orquestación, más prominentemente [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), programan y gestionan grandes cantidades de contenedores a través de flotas de máquinas. Manejan la colocación, el escalado, la salud, las redes, y la recuperación. [Nativo de la nube](https://en.wikipedia.org/wiki/Cloud-native_computing) es el estilo arquitectónico más amplio construido sobre estos fundamentos: aplicaciones diseñadas como servicios débilmente acoplados, desplegables independientemente, y escalables horizontalmente que asumen una infraestructura dinámica y autorreparable.

Para los equipos grandes, los contenedores y la orquestación resuelven un problema difícil. Necesitas ejecutar muchos servicios, construidos por muchos equipos, de forma confiable y eficiente en infraestructura compartida. Los contenedores dan a cada equipo un contrato consistente de empaquetado y tiempo de ejecución, lo cual retira la clase de fallos «funciona en mi máquina». La orquestación oculta las máquinas individuales detrás de un sustrato común, así que los equipos despliegan a una plataforma en lugar de a servidores. Esta estandarización es lo que te permite operar cientos o miles de servicios sin que cada equipo reinvente el despliegue, el escalado, y la resiliencia.

Los adoptantes empresariales y gubernamentales ganan portabilidad, resiliencia, y un camino lejos de la dependencia de proveedor único. A cambio, heredan complejidad real y nuevas responsabilidades de seguridad. Una plataforma de contenedores es poderosa precisamente porque es programable y dinámica, lo cual significa que tienes que gobernarla cuidadosamente. La procedencia de imágenes, el aislamiento multiinquilino, la política de red, y el costo se convierten todos en preocupaciones de nivel de plataforma. Los adoptantes del sector público cada vez más añaden requisitos de soberanía: control sobre dónde residen los datos y quién puede acceder a ellos. Eso hace que la capacidad de ejecutar cargas de trabajo consistentes a través de entornos elegidos sea una capacidad estratégica, no solo un detalle técnico.

## Principios fundamentales

- Empaqueta las aplicaciones como imágenes de contenedor pequeñas, de propósito único, e inmutables.
- Practica la higiene de imágenes: imágenes base mínimas, versiones fijadas, escaneadas en busca de vulnerabilidades, y firmadas.
- Diseña las aplicaciones para que sean sin estado y escalables horizontalmente donde sea posible, externalizando el estado.
- Trata el modelo de estado deseado de la plataforma de orquestación como la fuente de verdad y deja que se autorrepare.
- Aplica el aislamiento y el mínimo privilegio entre inquilinos, cargas de trabajo, y espacios de nombres.
- Sigue los principios de [doce factores](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), una metodología para construir aplicaciones desechables, con configuración externalizada, y escalables horizontalmente, y extiéndelos para las realidades de los sistemas distribuidos.
- Haz del costo una preocupación de ingeniería de primera clase y visible, no una ocurrencia tardía.
- Prefiere las abstracciones portables y basadas en estándares para preservar la flexibilidad estratégica.

## Recomendaciones

### Practica una higiene de imágenes rigurosa

La imagen de contenedor es tu unidad fundamental de confianza y despliegue, así que trátala de esa manera. Empieza desde imágenes base mínimas y confiables para reducir la superficie de ataque. Fija las versiones de dependencias e imágenes base para la reproducibilidad. Escanea cada imagen en busca de vulnerabilidades conocidas en el canal de construcción, y bloquea las que tienen hallazgos críticos. Firma las imágenes y verifica las firmas en el momento del despliegue, así solo se ejecutan imágenes aprobadas y no modificadas. Mantén un registro interno curado de imágenes base endurecidas a partir de las cuales construyen los equipos. Eso propaga automáticamente buenos valores predeterminados de seguridad.

### Usa los patrones de Kubernetes en lugar de reinventarlos

Kubernetes premia a los equipos que adoptan sus patrones establecidos, y castiga a los equipos que luchan contra su modelo. Usa manifiestos declarativos para el estado deseado. Añade sondas de salud para que la plataforma pueda detectar y reemplazar instancias no saludables. Fija solicitudes y límites de recursos para que el planificador pueda empaquetar cargas de trabajo con seguridad. Usa el autoescalado horizontal para la demanda elástica. Para la lógica operacional que debe correr continuamente, como gestionar una base de datos, rotar certificados, o reconciliar recursos personalizados, usa el patrón operador, que codifica el conocimiento operacional humano en software que vigila el estado y actúa. Resiste el impulso de construir orquestación a medida encima de la plataforma. Prefiere las construcciones nativas.

### Diseña la multiinquilinidad deliberadamente

Cuando muchos equipos comparten un clúster, el aislamiento es un requisito de seguridad y fiabilidad, no una cortesía. Usa los espacios de nombres como fronteras de inquilinidad. Aplica cuotas de recursos para que ningún inquilino pueda dejar sin recursos a otros. Aplica políticas de red para restringir el tráfico a lo explícitamente permitido. Usa el [control de acceso basado en roles](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) para limitar lo que cada equipo puede hacer. Para las cargas de trabajo con necesidades de aislamiento más fuertes, considera clústeres separados o aislamiento más fuerte. Decide temprano si tu modelo es multiinquilinidad suave (equipos internos confiables) o multiinquilinidad dura (cargas de trabajo mutuamente desconfiadas), porque los dos exigen controles muy distintos.

### Construye nativo de la nube, doce factores y más allá

La metodología de doce factores, con sus dependencias explícitas, configuración en el entorno, procesos sin estado, desechabilidad, y demás, sigue siendo una excelente línea base para los servicios que prosperan en una plataforma dinámica. Extiéndela para las realidades añadidas de los sistemas distribuidos. Diseña para el fallo parcial. Haz las operaciones idempotentes y reintentables. Expón la salud y la telemetría. Trata la observabilidad como una función incorporada en lugar de un añadido. Externaliza todo el estado a servicios de datos gestionados, para que las instancias de aplicación permanezcan desechables y escalables horizontalmente.

### Planifica estrategias multinube, híbridas, y soberanas pragmáticamente

La portabilidad es valiosa, pero persíguela con los ojos abiertos. Estandariza en abstracciones portables como contenedores, Kubernetes, y API abiertas, para que las cargas de trabajo puedan moverse si es necesario. Pero evita la trampa de rechazar cada servicio gestionado, lo cual intercambia productividad real por portabilidad hipotética. Para los requisitos híbridos y soberanos, diseña para que las mismas cargas de trabajo y canales puedan ejecutarse en una región elegida, un centro de datos privado, o una nube soberana que cumpla las reglas jurisdiccionales y de residencia de datos. Haz explícitas las fronteras de soberanía y residencia en la arquitectura y la política.

### Haz visible el costo con FinOps

En entornos de nube elásticos, el costo es una consecuencia directa de las decisiones de ingeniería, así que da a los ingenieros visibilidad y responsabilidad. Etiqueta los recursos para la asignación de costos. Atribuye el gasto a equipos y servicios. Muestra los datos de costo junto a las métricas de rendimiento. Dimensiona correctamente las cargas de trabajo, usa el autoescalado para ajustar la demanda, y recupera los recursos inactivos. Establece una práctica de FinOps que reúna a ingeniería, finanzas, y producto, para que el gasto en la nube se convierta en una responsabilidad compartida y continua en lugar de una sorpresa trimestral.

## Ventajas y desventajas

| Elección | Ventajas | Desventajas | Mejor ajuste |
|---|---|---|---|
| Kubernetes | Poderoso, portable, ecosistema enorme | Complejidad pronunciada; carga operacional | Muchos servicios a escala |
| Servicio de contenedores gestionado | Menos carga operacional; inicio más rápido | Algo de dependencia de proveedor; menos control | Equipos que quieren simplicidad |
| Un único clúster compartido | Uso eficiente de recursos | Aislamiento más difícil; radio de impacto | Inquilinos internos confiables |
| Clúster por inquilino | Aislamiento fuerte | Mayor costo y sobrecarga | Cargas de trabajo desconfiadas o reguladas |
| Portabilidad multinube | Flexibilidad; evita la dependencia | Servicios del mínimo común denominador | Mitigación de riesgo estratégico |
| Servicios gestionados profundos de una sola nube | Máxima productividad | Dependencia del proveedor | Equipos enfocados en velocidad |

La contrapartida general es capacidad frente a complejidad. Las arquitecturas Kubernetes y nativas de la nube entregan elasticidad, resiliencia, y velocidad. Pero imponen una carga operacional y cognitiva sustancial que los equipos pequeños rutinariamente subestiman. De la misma manera, perseguir la portabilidad [multinube](https://en.wikipedia.org/wiki/Multicloud) completa intercambia productividad por opcionalidad. La respuesta correcta depende de la escala y el riesgo. Las grandes organizaciones con muchos equipos y necesidades de gobernanza fuertes usualmente justifican la inversión. Los esfuerzos más pequeños a menudo están mejor servidos por servicios gestionados que ocultan la complejidad.

## Preguntas para discutir con tu equipo

1. **¿Firmas las imágenes y verificas las firmas en el momento del despliegue, y una vulnerabilidad crítica realmente bloquea la construcción?** La imagen es tu unidad de confianza, así que la cadena de suministro a su alrededor merece puertas duras, no advertencias. Decide si solo pueden ejecutarse imágenes firmadas y verificadas, si el escaneo bloquea los hallazgos críticos o meramente los registra, y quién mantiene el registro curado de imágenes base endurecidas a partir de las cuales construyen los equipos. Para las cargas de trabajo empresariales y gubernamentales esto frecuentemente es un requisito de cumplimiento, y también es tu mejor defensa contra una dependencia envenenada que llega a producción. Trae el estado actual: qué fracción de las imágenes en ejecución vienen de tu base endurecida, cuántas llevan CVE críticos sin parchear, y si actualmente puede programarse cualquier imagen sin firmar. Si un hallazgo crítico no detiene un despliegue, tu escáner es decoración.

2. **¿Cómo previenen las solicitudes, límites, y cuotas de recursos que una carga de trabajo prive a sus vecinos, sin dejar capacidad costosa inactiva?** En un clúster compartido, una carga de trabajo sin límites puede colapsar o estrangular todo a su alrededor, y las cuotas fijadas demasiado generosamente desperdician las ganancias de utilización que justifican la plataforma. Decide valores predeterminados sensatos, quién los ajusta, y cómo atrapas las cargas de trabajo sin ninguna solicitud fijada. A escala esto es tanto un control de fiabilidad como un control de costo, porque el dimensionamiento correcto es donde vive gran parte del ahorro de FinOps. Trae datos: la utilización actual del clúster, con qué frecuencia las cargas de trabajo son desalojadas o estranguladas, y qué espacios de nombres no tienen cuotas. La meta es un empaquetado denso y seguro, así que trata los límites faltantes como un defecto que la plataforma rechaza.

3. **¿Qué estado se permite que viva dentro de un contenedor, y a dónde va todo lo demás?** La resiliencia nativa de la nube depende de instancias desechables que la plataforma pueda reprogramar a voluntad, y eso solo se sostiene si el estado importante vive en servicios de datos gestionados en lugar de en el disco local del contenedor. Decide la regla explícitamente, porque el estado almacenado en un contenedor por accidente se convierte en pérdida de datos en la siguiente reprogramación. Para los equipos que migran aplicaciones más antiguas esto a menudo es la parte más difícil, ya que los servicios heredados asumen un sistema de archivos local estable. Trae un inventario: qué servicios escriben estado local, cuáles dependen de sesiones pegajosas o afinidad de nodo, y qué tomaría externalizar cada uno. Hasta que el estado sea externo, tienes contenedores que parecen elásticos pero en realidad no pueden moverse.

4. **Cuando muchos equipos comparten un clúster, ¿tu modelo de aislamiento se elige deliberadamente como multiinquilinidad suave o dura, y los controles coinciden con esa elección?** Los espacios de nombres separan a los equipos internos confiables, pero no contienen a una carga de trabajo que es activamente hostil o comprometida, y tratar la inquilinidad suave como si fuera dura es un incidente de seguridad esperando ocurrir. Decide por carga de trabajo si los inquilinos meramente necesitan un reparto justo o deben asumirse mutuamente desconfiados, luego ajusta los controles: espacios de nombres, cuotas, políticas de red, y RBAC para el caso suave, clústeres separados o aislamiento más fuerte para el caso duro. Para una organización grande esta decisión impulsa el costo directamente, porque un clúster por inquilino es mucho más costoso que los espacios de nombres compartidos, así que quieres gastar el presupuesto de aislamiento solo donde el modelo de amenaza lo exija. Trae el inventario de inquilinos: qué cargas de trabajo comparten un clúster hoy, cuáles manejan tráfico regulado o de cara al exterior, y dónde la política de red todavía es de permitir por defecto. En entornos empresariales y gubernamentales, mezclar cargas de trabajo desconfiadas bajo inquilinidad suave es exactamente el hallazgo que un auditor señalará, así que nombra la frontera antes de que lo hagan.

5. **¿Cuánto estás pagando por la portabilidad multinube, y alguna vez realmente la usarás?** Estandarizar en contenedores, Kubernetes, y API abiertas mantiene las cargas de trabajo movibles, pero rechazar cada servicio gestionado para preservar esa opción intercambia productividad real y diaria por portabilidad que la organización quizás nunca ejerza. Decide dónde la portabilidad es un requisito genuino, como una obligación de soberanía o salida que has firmado, frente a dónde es una manta de seguridad que ralentiza a cada equipo. La consideración en competencia es la velocidad: los servicios gestionados profundos envían funciones más rápido, y la arquitectura de mínimo común denominador es un impuesto permanente sobre cada equipo. Trae la evidencia: qué servicios gestionados has evitado y qué costó eso en tiempo de ingeniería, si alguna vez has movido una carga de trabajo entre proveedores, y qué obligan realmente tus contratos. Para los adoptantes gubernamentales y regulados, las reglas de residencia de datos y nube soberana pueden hacer la portabilidad innegociable, así que diseña para que los mismos manifiestos y canales se ejecuten en una región soberana y un enclave privado, pero sé honesto en que esto es un costo de cumplimiento en lugar de un seguro gratuito.

6. **¿Puede cada equipo ver lo que gasta, y alguien es dueño de la factura antes de que se convierta en una sorpresa?** En una plataforma elástica, el costo es una salida directa de las decisiones de ingeniería, sin embargo sin etiquetas de asignación de costo y tableros visibles el gasto se acumula en un fondo compartido del que nadie se siente responsable hasta que finanzas escala. Decide cómo atribuyes el costo a equipos y servicios, quién lo revisa, y si los ingenieros ven el costo junto a las métricas de rendimiento o solo se enteran una vez al trimestre. La tensión es entre la responsabilidad y la fricción: presiona demasiado el costo y cada decisión se convierte en una negociación de presupuesto, ignóralo y las cargas de trabajo inactivas y sobredimensionadas se componen silenciosamente. Trae los números: el gasto actual por equipo, cuánta capacidad está inactiva o sobredimensionada, y qué tan rápido se notaría una carga de trabajo desbocada. Para los presupuestos empresariales y gubernamentales, el gasto en la nube sin atribuir es tanto un fallo de gobernanza como un riesgo financiero real, así que levanta una práctica de FinOps que ponga a ingeniería, finanzas, y producto en la misma conversación en lugar de reconciliar después del hecho.

## Perspectiva sectorial

**Startup.** Recurre a un servicio de contenedores gestionado en lugar de un clúster Kubernetes autoalojado: con un par de servicios y sin un ingeniero de plataforma, los planos de control son una distracción que no puedes costear. Empaqueta imágenes pequeñas a partir de una base mínima, fija versiones, añade un escaneo de vulnerabilidades a la construcción, y empuja todo el estado a una base de datos gestionada para que las instancias permanezcan desechables. Salta los espacios de nombres, los operadores, y la portabilidad multinube hasta que realmente tengas los servicios y la gente para justificarlos.

**Pequeña empresa.** Sin un especialista de plataforma dedicado y con un presupuesto ajustado, apóyate fuertemente en servicios gestionados y deja que el proveedor opere la orquestación que de otro modo tendrías que dotar de personal. Trata lo básico de contenedores como tu piso de seguridad: imágenes mínimas, fijación de versiones, y un escaneo en el canal dan la mayor parte de la protección con poco esfuerzo. Favorece comprar una plataforma soportada sobre construir una, y mantén suficiente portabilidad, contenedores estándar y API abiertas, para no quedar atrapado si cambian los precios o los términos.

**Empresa.** La tarea es la gobernanza de plataforma entre muchos equipos: un equipo de plataforma central suministrando imágenes base endurecidas, puertas de firma y escaneo, inquilinidad por espacio de nombres con cuotas, política de red, y RBAC, más etiquetas de asignación de costo y un tablero de FinOps. Estandariza el contrato de despliegue para que cientos de servicios operen de la misma manera, y gestiona la seguridad, la multiinquilinidad, y el costo centralmente mientras los equipos se autoatienden en el despliegue. Financia adecuadamente al equipo de plataforma, porque una plataforma con recursos insuficientes se convierte en el cuello de botella que espera toda la organización.

**Gobierno.** La soberanía, la residencia de datos, y la rendición de cuentas pública moldean la arquitectura. Ejecuta las cargas de trabajo en contenedores estándar y Kubernetes para que los mismos canales corran en una región soberana y un enclave acreditado en las instalaciones, y codifica las fronteras de residencia y acceso como política en lugar de convención. Extrae las imágenes de un registro interno endurecido, aplica multiinquilinidad dura a los datos más sensibles, y mantén la portabilidad que te da resiliencia y poder de negociación, ya que las reglas de contratación pública a menudo prohíben la dependencia de un único proveedor.

## Ejemplos

**Startup.** Una startup de seis personas empaqueta sus dos servicios como imágenes de contenedor pequeñas construidas a partir de una base mínima, y las ejecuta en un servicio de contenedores gestionado en lugar de un clúster Kubernetes autoalojado, así nadie tiene que cuidar planos de control. Fijan las versiones de imagen base y añaden un escaneo de vulnerabilidades a su construcción, pero deliberadamente saltan las funciones de orquestación más pesadas hasta que realmente tengan más que un puñado de servicios. El estado vive en una base de datos Postgres gestionada, lo cual mantiene a los contenedores desechables y permite que la plataforma los reinicie o escale sin ninguna pérdida de datos.

**Empresa.** Una empresa de telecomunicaciones ejecuta varios cientos de [microservicios](https://en.wikipedia.org/wiki/Microservices) en clústeres Kubernetes compartidos. Un equipo de plataforma provee imágenes base endurecidas, aplica firma de imágenes y puertas de vulnerabilidad, y aísla las unidades de negocio en espacios de nombres con cuotas, políticas de red, y RBAC. Las etiquetas de asignación de costo y un tablero de FinOps atribuyen el gasto a cada línea de producto, y el autoescalado dimensiona correctamente la capacidad a la demanda. Los equipos de producto despliegan docenas de veces al día a una plataforma consistente sin gestionar servidores. La empresa mantiene control central sobre la seguridad y el costo.

**Gobierno.** Un servicio nacional de salud debe mantener los datos de la ciudadanía dentro de las fronteras nacionales y bajo control legal nacional. Ejecuta sus cargas de trabajo en una región de nube soberana usando contenedores estándar y Kubernetes, así los mismos canales y manifiestos también corren en un entorno acreditado en las instalaciones para los datos más sensibles. Las fronteras de residencia de datos y acceso se codifican como política, las imágenes se extraen de un registro interno endurecido, y la multiinquilinidad dura aísla las cargas de trabajo sensibles. La portabilidad a través de la región soberana y el enclave privado da al servicio resiliencia y poder de negociación sin sacrificar el cumplimiento.

## Caso de negocio: motivaciones, ROI y TCO

El ROI de los contenedores y la orquestación viene de una mayor utilización de recursos, despliegues más rápidos y confiables, escalado elástico que ajusta el gasto a la demanda, y resiliencia mejorada a través de la autorreparación. Estandarizar en una plataforma común reduce el esfuerzo duplicado entre equipos y acelera la incorporación, porque cada servicio sigue el mismo contrato de despliegue y operación.

El análisis de TCO debe ser honesto sobre la carga operacional. Los costos de adopción incluyen personal de ingeniería de plataforma, capacitación, herramientas de seguridad para imágenes y clústeres, y el esfuerzo continuo de operar la plataforma misma. El costo de no adoptar incluye el despliegue a medida inconsistente entre equipos, la mala utilización de infraestructura costosa, el escalado manual frágil, y la dificultad de cumplir con los requisitos de resiliencia y soberanía. Para el liderazgo, el caso descansa en la escala. Por debajo de un cierto número de servicios la complejidad puede no rendir frutos, y un servicio gestionado es más sabio. Pero a escala empresarial y gubernamental, una plataforma nativa de la nube gobernada típicamente es el fundamento más rentable y resiliente, siempre que financies adecuadamente al equipo de plataforma para operarla.

## Antipatrones y trampas

- **Imágenes gordas y sin escanear.** Las imágenes hinchadas construidas a partir de bases no confiables llevan vulnerabilidades innecesarias y ralentizan todo.
- **Kubernetes para todo.** Adoptar un orquestador complejo para un puñado de servicios simples compra complejidad sin beneficio.
- **Ignorar los límites de recursos.** Sin solicitudes y límites, una carga de trabajo puede privar o colapsar a sus vecinos.
- **Inquilinidad suave para cargas de trabajo hostiles.** Depender solo de los espacios de nombres para aislar inquilinos desconfiados es un incidente de seguridad esperando ocurrir.
- **Contenedores con estado por accidente.** Almacenar estado importante dentro de contenedores desechables lleva a la pérdida de datos en la reprogramación.
- **Ceguera de costo.** Tratar el gasto en la nube como sobrecarga fija en lugar de una salida de ingeniería lleva a facturas desbocadas.
- **Teatro de portabilidad.** Rechazar todos los servicios gestionados para preservar una portabilidad que la organización nunca realmente usará.

## Modelo de madurez

**Nivel 1: Iniciar.** Los contenedores se usan ad hoc, si acaso. Las imágenes se construyen a mano y sin escanear, el despliegue es manual y reactivo, y no hay plataforma compartida, visibilidad de costo, ni modelo de aislamiento.

**Nivel 2: Desarrollar.** Los equipos contenerizan aplicaciones y adoptan un orquestador, pero las prácticas varían entre grupos. El escaneo de imágenes, los límites de recursos, y la firma son inconsistentes, y el costo y la multiinquilinidad no se gobiernan sistemáticamente.

**Nivel 3: Estandarizar.** Una plataforma estandarizada está documentada y se aplica en toda la organización: imágenes base endurecidas, puertas de firma y escaneo, inquilinidad basada en espacios de nombres con cuotas y política de red, RBAC, y asignación de costo. Los patrones nativos de la nube y de doce factores son la norma esperada en lugar de una elección local.

**Nivel 4: Gestionar.** La plataforma se mide y controla contra líneas base. Rastreas la utilización del clúster, el porcentaje de imágenes en ejecución construidas a partir de la base endurecida, las vulnerabilidades críticas sin parchear, la frecuencia de despliegue y la tasa de fallo de cambio, las tasas de desalojo y estrangulamiento, y el costo por equipo y servicio contra el presupuesto. Las puertas se aplican con esta evidencia: los límites de recursos faltantes y las imágenes sin firmar se rechazan automáticamente, y la deriva del estándar dispara una acción en lugar de una advertencia.

**Nivel 5: Orquestar.** La plataforma es de autoservicio y autorreparable, integrada en toda la organización y adaptativa. FinOps dimensiona correctamente y recupera capacidad continuamente, la arquitectura portable soporta los requisitos híbridos y soberanos, y la plataforma mejora continuamente a partir del uso medido, retirando y reemplazando componentes a medida que cambian las cargas de trabajo, el costo, y el panorama de riesgo.

## Ideas para el debate

- ¿A qué escala adoptar Kubernetes deja de ser complejidad por sí misma y empieza a rendir frutos?
- ¿Dónde está la frontera correcta entre la multiinquilinidad suave y dura para tus cargas de trabajo?
- ¿Cuánto deberías invertir en portabilidad multinube frente a la productividad de los servicios gestionados profundos?
- ¿Cómo das a los ingenieros responsabilidad real de costo sin convertir cada decisión en una negociación de presupuesto?
- ¿Cuál es tu modelo de gobernanza para las imágenes base, y quién mantiene el registro endurecido?
- ¿Cómo moldean los requisitos de soberanía y residencia de datos tu arquitectura de plataforma?

## Puntos clave

- Los contenedores estandarizan el empaquetado y el tiempo de ejecución; la orquestación estandariza la operación a escala.
- La higiene de imágenes, es decir, imágenes mínimas, fijadas, escaneadas, y firmadas, es seguridad fundacional.
- Usa los patrones nativos de Kubernetes y los operadores en lugar de construir orquestación a medida.
- Elige un modelo de multiinquilinidad deliberadamente según cuánto se confían entre sí las cargas de trabajo.
- Sigue los doce factores y extiéndelos para las realidades de los sistemas distribuidos como el fallo parcial y la observabilidad.
- Trata el costo como una salida de ingeniería y gestiónalo continuamente a través de FinOps.

## Referencias y lecturas adicionales

- Adam Wiggins, *The Twelve-Factor App* (metodología).
- Brendan Burns, Joe Beda, y Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam y Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment y Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), definición y panorama de lo nativo de la nube.
