# 4.3 Seguridad de la infraestructura y la nube

## Resumen y justificación

Las aplicaciones se ejecutan sobre infraestructura, y hoy en día esa infraestructura es, en su mayor parte, basada en la nube, definida por software y en constante cambio. Un solo ingeniero puede aprovisionar una base de datos, abrir un enlace de red o conceder un permiso con un único comando, a una escala y velocidad que el control de cambios tradicional nunca contempló. Precisamente esa capacidad es la razón por la que la mala configuración, y no exploits exóticos, es la causa principal de las brechas en la nube. Un contenedor de almacenamiento expuesto a Internet por accidente o un rol de acceso con permisos excesivamente amplios pueden poner al descubierto toda la información de una organización en cuestión de segundos.

En grandes empresas, la infraestructura en la nube abarca múltiples proveedores, miles de cuentas y un mosaico de servicios gestionados, contenedores y funciones serverless. La superficie de ataque no es un perímetro estático; es un conjunto vivo, extenso y ramificado de recursos e identidades. En el sector público, esa misma complejidad se enfrenta a regímenes estrictos de autorización, requisitos de residencia de datos y fronteras de clasificación que condicionan cada decisión arquitectónica. En ambos contextos, la capa de identidad se ha convertido en el nuevo perímetro: quién puede hacer qué, sobre qué recurso y bajo qué condiciones.

Este capítulo aborda cómo asegurar esa base: la [gestión de identidades y acceso](https://en.wikipedia.org/wiki/Identity_management) (IAM), la [segmentación de red](https://en.wikipedia.org/wiki/Network_segmentation), el [cifrado](https://en.wikipedia.org/wiki/Encryption) y la [gestión de claves](https://en.wikipedia.org/wiki/Key_management), la seguridad de las cargas de trabajo en contenedores y [serverless](https://en.wikipedia.org/wiki/Serverless_computing), y la gestión continua de la postura de seguridad que impide que una flota de recursos en la nube, en permanente movimiento, derive hacia el peligro.

## Principios fundamentales

- **La identidad es el perímetro.** Las decisiones de acceso se basan en una identidad robusta y una autorización granular, no en la ubicación de red.
- **El principio del menor privilegio, siempre.** Cada identidad, humana o de máquina, recibe los permisos mínimos necesarios y nada más.
- **Segmentar para confinar.** Dividir redes y cargas de trabajo de modo que un compromiso en un ámbito no se propague libremente.
- **Cifrado en todo momento.** Proteger los datos en tránsito y en reposo por defecto, con una gestión rigurosa de las claves.
- **Inmutable y declarativo.** Definir la infraestructura como código (IaC), desplegar de forma inmutable y tratar cualquier desviación como un defecto.
- **Verificación continua.** La postura de seguridad no es una auditoría puntual; hay que escanear y hacer cumplir las políticas de forma ininterrumpida.
- **Configuración segura por defecto.** El estado predeterminado de cualquier recurso debe estar bloqueado, no abierto.

## Recomendaciones

### Diseñar la gestión de identidades y acceso de manera deliberada

La IAM es el componente más importante de la seguridad en la nube y, al mismo tiempo, el que más a menudo se gestiona de forma deficiente.

- Utilizar el [control de acceso basado en roles](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) para otorgar permisos según la función del puesto y el [control de acceso basado en atributos](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) cuando se necesiten decisiones más finas y contextualizadas (según etiquetas, entorno, clasificación de datos o momento del día).
- Eliminar las credenciales estáticas de larga duración a favor de tokens de corta vigencia, emitidos automáticamente, y de la federación de identidad de cargas de trabajo.
- Exigir la [autenticación multifactor](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA) para todo acceso humano y una autenticación robusta para las acciones con privilegios elevados.
- Aplicar el principio del menor privilegio con rigor: partir del cero y añadir permisos de forma deliberada. Revisar y recortar periódicamente los permisos en desuso, ya que tienden a acumularse.
- Separar funciones para que ninguna identidad pueda, simultáneamente, proponer y aprobar cambios sensibles.
- Utilizar cuentas o proyectos dedicados para crear fronteras firmes entre entornos (producción, homologación, desarrollo) y entre unidades de negocio.

### Segmentar redes y microsegmentar cargas de trabajo

En redes planas, el atacante se desplaza lateralmente con libertad una vez dentro. Dividir y confinar es la clave.

- Segmentar a nivel de red en niveles y zonas, permitiendo únicamente el tráfico que cada nivel necesita legítimamente.
- Aplicar **microsegmentación** para que cada carga de trabajo se comunique solo con los pares específicos que requiere, mediante políticas conscientes de la identidad en lugar de reglas de subred amplias.
- Denegar por defecto el tráfico este-oeste; las reglas de permiso deben ser explícitas.
- Situar los almacenes de datos sensibles en subredes privadas, sin exposición directa a Internet, accesibles solo a través de rutas controladas.
- Utilizar conectividad privada hacia los servicios gestionados en lugar de canalizar el tráfico a través de Internet cuando sea posible.

### Cifrar datos y gestionar las claves correctamente

El cifrado no es más fuerte que la gestión de claves que lo sustenta.

- Cifrar **en tránsito** con [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Protocolo de seguridad de capa de transporte) actualizado, en todas partes, incluido el tráfico interno entre servicios.
- Cifrar **en reposo** por defecto para todo almacenamiento, bases de datos y copias de seguridad.
- Gestionar las claves mediante un **Servicio de Gestión de Claves (KMS)** y emplear un [Módulo de Seguridad de Hardware](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM) para las claves de mayor nivel de garantía y para cumplir requisitos regulatorios.
- Rotar las claves según un calendario definido y permitir la rotación rápida ante una sospecha de compromiso.
- Controlar y auditar quién puede usar y gestionar las claves de forma independiente a quién puede acceder a los datos, de modo que la custodia de las claves refuerce la separación de funciones.
- Considerar las claves gestionadas por el cliente cuando la regulación o los compromisos contractuales exijan que la organización sea la titular de las claves en lugar del proveedor.

### Asegurar contenedores, Kubernetes y serverless

Cada modelo de cómputo trae consigo sus propios riesgos.

- **Contenedores:** construir sobre imágenes base mínimas y de confianza; escanear las imágenes en busca de vulnerabilidades antes del despliegue; ejecutar como usuario no privilegiado; hacer los sistemas de archivos de solo lectura siempre que sea posible; y nunca incrustar secretos en las imágenes.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** habilitar RBAC y acotar con precisión las cuentas de servicio; aplicar políticas de red para la microsegmentación; utilizar controladores de admisión y motores de políticas para hacer cumplir los estándares; restringir los contenedores privilegiados; aislar las cargas de trabajo sensibles; y mantener el plano de control y los nodos actualizados.
- **Serverless:** aplicar el principio del menor privilegio a cada rol de ejecución de las funciones (una fuente habitual de permisos excesivos); validar todas las entradas de eventos; gestionar los secretos a través del almacén de secretos de la plataforma; y supervisar patrones de invocación anómalos.

Sea cual sea el modelo, mantener el runtime actualizado y las imágenes al día. Un contenedor es tan seguro como el software que contiene.

### Gestionar la postura de seguridad en la nube de forma continua

La nube cambia demasiado rápido para que las auditorías manuales periódicas puedan dar respuesta.

- Adoptar herramientas de **Gestión de Postura de Seguridad en la Nube (CSPM)** para detectar de forma continua configuraciones erróneas, exposiciones públicas y violaciones de políticas en todas las cuentas.
- Definir la política de seguridad como código e imponerla en el momento del despliegue, de modo que las configuraciones incorrectas se bloqueen antes de que lleguen al entorno.
- Preferir la prevención (controles que impiden la mala configuración) a la detección (alertas a posteriori) y combinar ambas estrategias.
- Mantener un inventario preciso de recursos e identidades; no se puede proteger lo que no se ve.
- Seguimiento y remediación de la deriva entre la infraestructura declarada como código y el estado real en ejecución.

## Compromisos: ventajas e inconvenientes

| Decisión | Ventajas | Inconvenientes |
|---|---|---|
| RBAC | Simple, comprensible, fácil de auditar | Poco granular; proliferación de roles a gran escala |
| ABAC | Granularidad fina, contextual, escalable con etiquetas | Complejo de diseñar y razonar |
| Claves gestionadas por el proveedor (KMS) | Sencillas, integradas, bajo esfuerzo operativo | El proveedor tiene la custodia; menor control |
| Claves gestionadas por el cliente / HSM | Control total, cumplimiento de requisitos estrictos | Coste operativo; riesgo de pérdida de claves |
| Controles preventivos | Evitan la mala configuración antes de que ocurra | Pueden bloquear trabajo legítimo; requieren calibración |
| Solo CSPM de detección | Flexible, no bloqueante | El daño puede producirse antes de la detección |
| Microsegmentación | Contención eficaz del movimiento lateral | Complejidad operativa, proliferación de políticas |

El compromiso dominante es entre control y carga operativa. Los controles más estrictos (claves gestionadas por el cliente, microsegmentación rigurosa, ABAC) reducen el riesgo, pero exigen experiencia y mantenimiento que los equipos pequeños tienen dificultades para sostener. El nivel adecuado depende de la sensibilidad de los datos y de las regulaciones aplicables. Un enfoque pragmático aplica fuertes valores de configuración segura por defecto para todos, reserva una mayor rigurosidad para los sistemas de mayor riesgo y prioriza los controles preventivos automatizados que hacen de la opción segura la opción predeterminada, no una disciplina manual.

## Preguntas para debatir con el equipo

1. **Dónde se trazarán las fronteras firmes entre cuentas o proyectos y qué pertenece a cada una?** Las cuentas y proyectos dedicados crean el mayor grado de contención que la nube ofrece: un compromiso en desarrollo no alcanza a producción, y una unidad de negocio no puede tocar los datos de otra. Definir el esquema de fronteras antes de que la flota crezca hasta miles de cuentas, porque retrotraer el aislamiento sobre una estructura plana es lento y arriesgado. En entornos corporativos y públicos, estas fronteras se alinean con la separación de entornos, la clasificación de datos y los límites de radio de impacto que los auditores esperan ver. Traer un diagrama actual de qué cargas de trabajo comparten cuenta en la actualidad y marcar dónde un rol con permisos demasiado amplios abarca producción y no producción. Si datos sensibles residen en la misma cuenta que cargas de trabajo experimentales, esa es la frontera que hay que resolver primero.

2. **¿Cuál es el estándar para quién puede gestionar claves y quién puede acceder a los datos cifrados?** El cifrado no es más fuerte que su gestión de claves, y separar la custodia de las claves del acceso a los datos convierte al KMS en un punto de ejecución de la separación de funciones. Decidir quién puede crear, rotar y usar claves, y asegurarse de que ese conjunto no se solape con las personas que pueden leer los datos que esas claves protegen. Para sistemas regulados y del sector público, esta decisión suele condicionar la elección entre claves gestionadas por el proveedor y claves gestionadas por el cliente o HSMs, que ofrecen más control pero también más riesgo operativo de pérdida. Revisar las políticas de claves actuales y comprobar si alguna identidad puede, a la vez, gestionar una clave y leer los datos que protege, porque esa es una brecha silenciosa muy frecuente. Si la custodia y el acceso no están separados, el cifrado en reposo protege menos de lo que el panel de control sugiere.

3. **Cómo se harán ineludibles los valores seguros por defecto en la zona de aterrizaje, más que meramente recomendados?** La mala configuración, no los exploits exóticos, es la causa principal de las brechas en la nube, y la solución es establecer controles preventivos que bloquen una base de datos abierta a Internet o un contenedor sin cifrar antes de que se despliegue, no alertar después del hecho. Decidir qué políticas se impondrán en el momento del despliegue (sin almacenamiento público, cifrado activado por defecto, etiquetado obligatorio) y cuáles solo se detectarán y reportarán. Para un equipo grande, codificar estos controles en las zonas de aterrizaje y en las plantillas de infraestructura como código significa que cada cuenta nueva hereda la protección sin esfuerzo adicional por equipo, convirtiendo la seguridad de un impuesto recurrente en una inversión puntual de plataforma. Traer los hallazgos de los últimos meses de configuraciones erróneas y plantearse cuáles habría impedido un control preventivo. Si la gestión de postura es solo de detección, el daño puede ocurrir antes de que nadie vea la alerta, por lo que conviene trasladar los controles de mayor impacto a la prevención.

4. **Cómo se eliminarán las credenciales estáticas de larga duración sin romper la automatización que depende de ellas en silencio?** Las claves de acceso embebidas que nunca expiran son una de las causas más frecuentes de brechas en la nube, porque una sola clave filtrada en un script, un log o un repositorio otorga al atacante un acceso duradero. El tirón opuesto es el operativo: trabajos de CI heredados, tareas cron e integraciones con terceros suelen asumir que existe una clave estática, y migrar a tokens de corta vigencia o a la federación de identidad de cargas de trabajo requiere tiempo de ingeniería que nadie ha presupuestado. Para un equipo grande, una ruta de migración compartida (emitir tokens automáticamente, fijar un estándar de caducidad y alarmar ante cualquier nueva clave de larga duración) evita que cada grupo invente su propia solución más débil. Traer un inventario de cada credencial estática en uso, su antigüedad, su radio de impacto y si el sistema que alimenta puede aceptar identidad federada hoy. En entornos corporativos y públicos, vincular el plazo con los ciclos de auditoría y autorización, porque una credencial que sobrevive a la persona que la creó es exactamente el hallazgo que frena una autorización continua.

5. **Cuando un recurso está mal configurado o una clave se compromete, ¿cuánto tarda en detectarse, contenerse y remediarse, y se ha medido ese tiempo?** Un contenedor público o un rol con permisos excesivos es tan peligroso como la ventana durante la que permanece abierto, por lo que el tiempo medio de detección y remediación es la métrica que realmente acota la exposición. La tensión está entre los controles preventivos que impiden el error en el momento del despliegue y la gestión de postura de detección que capta lo que se escapa, y hacen falta cifras honestas de ambas en lugar de la suposición tranquilizadora de que los controles preventivos lo cubren todo. Traer los hallazgos de configuraciones erróneas y derivas del último trimestre con timestamps, el tiempo mediano desde la introducción hasta la remediación y el historial de simulación de rotación ante un compromiso de claves. En flotas de miles de cuentas en entornos corporativos y públicos, acordar quién es responsable de la remediación de un hallazgo que ningún equipo asume claramente, porque una alerta sin un responsable asignado se convierte en un incidente.

6. **Cómo se mantendrá la coherencia de la postura de seguridad en múltiples nubes, cuentas y equipos sin frenar a todos?** Las flotas multicloud y multicuenta se fragmentan con rapidez: cada proveedor tiene su propio modelo de IAM, sus propios valores por defecto y sus propias herramientas de postura, de modo que una política impuesta en un lugar se relaja silenciosamente en otro. El compromiso está entre el control central que garantiza la coherencia y la autonomía local que permite la velocidad de los equipos, y inclinarse demasiado hacia un lado crea un cuello de botella en la entrega o deja que los estándares se dispersen. Traer un mapa de cobertura actual: qué cuentas heredan los controles de la zona de aterrizaje, cuáles no están gestionadas y dónde el mismo control se expresa de tres formas distintas en distintos proveedores. Para una organización grande o del sector público, añadir la perspectiva de la auditoría, porque los auditores esperan un estándar coherente y defendible aplicado en todas partes, y un control que existe en la nube principal pero no en la secundaria es una brecha que un atacante determinado o un evaluador encontrará primero.

## Perspectiva por sector

**Startup.** La velocidad y la supervivencia priman, así que apoyarse por completo en valores seguros que vienen de serie: cifrado en reposo activado, contenedores de almacenamiento privados hasta que un humano los abre, MFA en la cuenta raíz e identidad de carga de trabajo del proveedor en lugar de claves de acceso pegadas. No implantar una plataforma de CSPM ni diseñar microsegmentación a mano que no se pueda mantener; un único control preventivo que bloquee una base de datos abierta a Internet aporta la mayor parte de la protección con una tarde de trabajo. Mantener todo como infraestructura como código desde el principio para que el endurecimiento escale con la organización en lugar de convertirse en una reescritura posterior.

**Pyme.** Sin ingeniero de seguridad dedicado y con un presupuesto ajustado, preferir servicios gestionados cuyos valores por defecto ya están endurecidos y cuya gestión de claves se resuelve por uno, en lugar de construir una disciplina de KMS propia. Considerar la seguridad en la nube como una cuestión de higiene de configuración: saber qué contenedores y bases de datos existen, mantenerlos privados, exigir MFA y activar los controles de postura nativos del proveedor que no suponen coste adicional. Al adquirir herramientas, priorizar aquellas que señalan la exposición pública y el almacenamiento sin cifrar de forma inmediata, porque estos dos errores causan la mayoría de las brechas evitables.

**Gran empresa.** El verdadero problema es la coherencia en miles de cuentas y múltiples equipos, por lo que el trabajo es de plataforma: zonas de aterrizaje que provisionan cada cuenta endurecida, controles preventivos aplicados como política en código y escaneo CSPM continuo para detectar deriva. Estandarizar el modelo de IAM, las reglas de custodia de claves y la línea base de segmentación para que los grupos dejen de reinventar versiones más débiles, y medir la postura en toda la flota en lugar de fiarse de la palabra de cada equipo. Presupuestar el esfuerzo de ingeniería continuo para mantener las políticas al día a medida que los proveedores añaden servicios y la flota crece.

**Sector público.** Las normas de contratación, los requisitos de residencia de datos y los regímenes de autorización condicionan cada decisión, por lo que los controles de seguridad duplican su función como evidencia de auditoría. Preferir la gestión de claves validada por FIPS con la custodia separada del acceso a los datos, regiones aisladas que mantienen los datos dentro de los límites nacionales e imágenes de contenedor firmadas y escaneadas con control de admisión estricto. Publicar las salvaguardas que se pueda, integrar la gestión continua de postura directamente en la evidencia de autorización continua y exigir a los proveedores que divulguen sus valores de configuración por defecto y que soporten los controles de segmentación y custodia que las fronteras de clasificación exigen.

## Ejemplos

**Startup.** Una pequeña startup opera todo en una única cuenta de nube y no puede dotarse de un equipo de plataforma, por lo que se apoya en valores seguros de serie: cifrado en reposo activado por defecto, contenedores de almacenamiento privados hasta que un humano los abre y MFA obligatorio en la cuenta raíz. En lugar de claves de acceso estáticas pegadas en CI, usa la identidad de carga de trabajo del proveedor para que el pipeline obtenga credenciales de corta vigencia automáticamente. Un único control preventivo gratuito que detecta cualquier base de datos abierta a Internet la protege del error más común y más costoso en la nube, con un coste de una tarde de configuración.

**Gran empresa.** Una empresa de medios que opera miles de cuentas en dos proveedores de nube impone un patrón de zona de aterrizaje: cada cuenta se provisiona desde una plantilla con cifrado en reposo activado por defecto, sin acceso público al almacenamiento, etiquetado obligatorio y una línea base de políticas de control. El CSPM escanea de forma continua en busca de deriva y la federación de identidad de cargas de trabajo ha eliminado las claves de larga duración en los sistemas de CI. Cuando un desarrollador intenta por accidente abrir una base de datos a Internet, una política preventiva bloquea el cambio y genera automáticamente una incidencia.

**Sector público.** Una agencia vinculada a la defensa opera en una región de nube aislada con residencia de datos impuesta por política, de modo que ningún dato abandona los límites nacionales. Las claves más sensibles residen en HSMs validados por FIPS, con la custodia separada del acceso a los datos para garantizar la separación de funciones. Los clústeres de Kubernetes emplean políticas de red estrictas y controles de admisión; cada imagen de contenedor se escanea y firma antes de poder ejecutarse. La gestión continua de postura alimenta directamente la evidencia de autorización continua de la agencia.

## Caso empresarial: motivaciones, retorno y coste total de propiedad

La seguridad de la infraestructura en la nube es donde una pequeña inversión previene pérdidas catastróficas de las que hablan los titulares. El coste total de propiedad incluye las herramientas de CSPM, los servicios de gestión de claves, el tiempo de ingeniería para diseñar IAM con menor privilegio y la segmentación, y el esfuerzo continuo de mantener las políticas actualizadas. Esos costes son reales, pero modestos. El coste de omitirlos es un único recurso mal configurado que expone toda una base de datos de clientes, junto con las multas regulatorias, los costes de notificación y el daño a la marca que perdura. Las brechas por mala configuración en la nube están entre los incidentes más frecuentes y más evitables de la industria.

La automatización y la reutilización multiplica el retorno. Codificar los valores seguros por defecto en las zonas de aterrizaje y en las plantillas de infraestructura como código significa que cada cuenta y cada carga de trabajo nuevas heredan la protección sin esfuerzo adicional por equipo, convirtiendo la seguridad de un impuesto manual recurrente en una inversión puntual de plataforma. Para el sector público y las empresas reguladas, una postura de seguridad sólida también reduce el coste de las auditorías y la autorización continua al generar evidencia de forma automática. Al presentar el caso a la dirección, destacar que la capa de identidad y configuración es hoy el vector de brecha principal, que la mala configuración es prevenible y que los controles preventivos reducen tanto el riesgo como la fricción de la revisión manual.

## Antipatrón y errores frecuentes

- **Permisos genéricos.** Conceder acceso `*` amplio «para que funcione» y nunca afinarlo.
- **Claves estáticas de larga duración.** Claves de acceso embebidas en scripts y CI que nunca caducan y que acaban filtrándose.
- **Redes planas.** Sin segmentación, de modo que un host comprometido alcanza todo.
- **Público por accidente.** Almacenamiento y bases de datos expuestas a Internet por valores por defecto o por descuido.
- **Cifrado sin disciplina de claves.** Activar el cifrado pero dejar el acceso a las claves sin restricciones o sin rotarlo nunca.
- **Secretos en las imágenes.** Credenciales incrustadas en imágenes de contenedor que se propagan a todos los entornos donde se ejecuta la imagen.
- **Roles serverless sobrepermesionados.** Funciones con muchos más permisos de los que necesitan porque se omitió el acotamiento.
- **Postura solo de auditoría.** Detectar configuraciones erróneas a posteriori en lugar de prevenirlas en el momento del despliegue.
- **Ignorar la deriva.** Dejar que el entorno en ejecución diverja de la infraestructura como código hasta que nadie sabe cuál es el estado real.

## Modelo de madurez

**Nivel 1: Iniciar.** Aprovisionamiento manual a cargo de quien necesite un recurso. Permisos genéricos amplios y claves estáticas de larga duración. Redes planas sin segmentación. Cifrado aplicado de forma inconsistente, si es que se aplica. Sin gestión de postura; las configuraciones erróneas solo afloran después de que un incidente obliga a la pregunta.

**Nivel 2: Desarrollar.** Aparecen algunos roles de IAM y MFA, y el cifrado en reposo se activa para los almacenes principales, pero la práctica varía de un equipo a otro. Existen niveles básicos de red sin denegación por defecto. Las revisiones de configuración se realizan periódicamente y de forma manual. La infraestructura está parcialmente definida como código, por lo que el endurecimiento depende del equipo que provisionó la cuenta.

**Nivel 3: Estandarizar.** RBAC y ABAC con credenciales de corta vigencia y menor privilegio documentados y aplicados en toda la organización. La segmentación usa denegación por defecto en el tráfico este-oeste. El cifrado en tránsito y en reposo está activado por defecto, con claves en KMS según un calendario de rotación y la custodia separada del acceso a los datos. El endurecimiento de contenedores y Kubernetes es un estándar, y el CSPM se ejecuta contra políticas definidas aplicadas de forma coherente en todas las cuentas.

**Nivel 4: Gestionar.** La postura se mide, no se da por supuesta. Se siguen métricas nombradas frente a líneas base y objetivos: la proporción de identidades dentro de su línea base de menor privilegio, el tiempo medio de detección y remediación de configuraciones erróneas y derivas, la cobertura de controles preventivos y CSPM en las cuentas, el cumplimiento de la rotación de claves y el número de credenciales estáticas de larga duración que persisten. Los hallazgos se priorizan según su radio de impacto, la remediación tiene un responsable y un objetivo de nivel de servicio, y la tendencia de esas cifras orienta dónde debe ir el siguiente esfuerzo de endurecimiento.

**Nivel 5: Orquestar.** Los valores seguros por defecto están integrados en las zonas de aterrizaje y la infraestructura como código, de modo que cada recurso nace endurecido, y los controles se adaptan a medida que la flota y el panorama de amenazas evolucionan. La microsegmentación usa políticas conscientes de la identidad; las claves gestionadas por el cliente y los HSMs protegen los sistemas de mayor garantía con separación de custodia. Los controles preventivos bloquean la mala configuración en el momento del despliegue, la deriva se detecta y remedia automáticamente, y la evidencia de postura alimenta la autorización continua de forma automática. La seguridad está integrada con la entrega y la planificación del riesgo, y la organización retira y reajusta controles con regularidad a medida que los proveedores, los servicios y las regulaciones cambian.

## Propuestas de debate

1. ¿En qué contextos el ABAC justifica su complejidad frente a quedarse con RBAC en su entorno?
2. ¿Cómo se eliminan las credenciales de larga duración sin romper la automatización heredada?
3. ¿Cuál es la proporción adecuada entre controles preventivos y gestión de postura de detección?
4. ¿Qué sistemas justifican el coste operativo de las claves gestionadas por el cliente o los HSMs?
5. ¿Cómo se impide que los permisos de menor privilegio se acumulen en silencio y vuelvan a un estado de sobreprivilegio?
6. ¿Cómo debería la complejidad multicloud modificar el enfoque para mantener una postura y una política coherentes?

## Puntos clave

- La identidad es el nuevo perímetro; invertir en IAM con menor privilegio y credenciales de corta vigencia.
- Segmentar redes y microsegmentar cargas de trabajo para confinar cualquier compromiso.
- Cifrar en tránsito y en reposo por defecto, y gestionar las claves con KMS/HSM y separación de la custodia.
- Endurecer contenedores, Kubernetes y serverless; mantener runtime e imágenes actualizados.
- Priorizar los controles preventivos frente a la detección a posteriori y gestionar la postura de forma continua.
- Integrar los valores seguros por defecto en las zonas de aterrizaje y la infraestructura como código para que la protección escale de forma automática.
- La mala configuración, no los exploits exóticos, es la causa principal de las brechas en la nube, y es prevenible.

## Referencias y lecturas adicionales

- Instituto Nacional de Estándares y Tecnología de EE. UU., *SP 800-207: Arquitectura Zero Trust*
- Centro de Seguridad de Internet, *CIS Benchmarks* (proveedores de nube, Kubernetes, Docker)
- Alianza de Seguridad en la Nube, *Cloud Controls Matrix* y *Guía de Seguridad para la Computación en la Nube*
- NIST, *SP 800-190: Guía de Seguridad de Contenedores de Aplicación*
- Liz Rice, *Seguridad de Contenedores*
- Marco Lancini y otros, *Postura de seguridad y detección en la nube* (literatura de ingeniería)
- Pilares de seguridad de Well-Architected de cada proveedor (como orientación arquitectónica neutral al proveedor)

