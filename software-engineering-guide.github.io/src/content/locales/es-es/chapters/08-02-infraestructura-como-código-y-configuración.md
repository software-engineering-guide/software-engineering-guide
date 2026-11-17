# 8.2 Infraestructura como código y configuración

## Presentación y motivación

La [infraestructura como código](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) significa definir y aprovisionar infraestructura (redes, servidores, bases de datos, balanceadores de carga, permisos) a través de archivos de definición legibles por máquina en lugar de clics manuales en la consola o scripts ad hoc. La [gestión de configuración](https://en.wikipedia.org/wiki/Configuration_management) extiende la misma idea a los ajustes y el estado de los sistemas una vez que existen. Juntas convierten la infraestructura de un artefacto artesanal y frágil en un producto versionado, revisable, y reproducible de la misma disciplina de ingeniería que usas para el código de aplicación.

Para los equipos grandes, la IaC no es una conveniencia sino una necesidad. Cuando cientos de ingenieros necesitan entornos y miles de recursos deben mantenerse consistentes a través de regiones y cuentas, el aprovisionamiento manual no puede mantener el ritmo y no puede mantenerse correcto. La infraestructura configurada humanamente deriva, tarde o temprano, hacia servidores «copo de nieve» únicos que nadie comprende del todo y que no pueden reconstruirse de forma confiable después de un fallo. Codificar la infraestructura la hace consistente, auditable, y desechable. Cualquier entorno puede recrearse a partir de su definición, y cualquier cambio es un diff revisable.

Las organizaciones empresariales y gubernamentales ganan un beneficio más, decisivo: la gobernanza aplicable. Los requisitos de seguridad y cumplimiento, como el cifrado en reposo, la segmentación de red, las regiones aprobadas, y el etiquetado para la asignación de costos, pueden incrustarse directamente en el código y comprobarse automáticamente antes de que se aprovisione nada. En lugar de auditar la infraestructura después del hecho y perseguir violaciones, evitas que la infraestructura no conforme llegue a existir nunca. Este cambio de la detección a la prevención es la razón central por la que la IaC se ha vuelto fundacional para la práctica de plataforma moderna.

## Principios fundamentales

- Prefiere las definiciones declarativas que describen el estado deseado sobre los scripts imperativos que describen pasos.
- Almacena todas las definiciones de infraestructura en control de versiones, revisadas como cualquier otro código.
- Trata la infraestructura como inmutable: reemplaza en lugar de modificar en su lugar.
- Haz que el aprovisionamiento sea idempotente para que aplicar la misma definición repetidamente produzca el mismo resultado.
- Detecta y reconcilia la deriva, el entorno en vivo divergiendo de su definición declarada, continuamente; el código, no el sistema en vivo, es la fuente de verdad.
- Compón la infraestructura a partir de módulos reutilizables y versionados en lugar de copiar y pegar.
- Codifica la política como código, reglas organizacionales expresadas como código comprobable por máquina, para que las barandillas sean automáticas, no consultivas.
- Mantén los secretos fuera de las definiciones; referéncialos desde un gestor de secretos dedicado.

## Recomendaciones

### Elige herramientas declarativas y estructúralas en torno a módulos

Adopta una herramienta de IaC declarativa, como [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, o una opción nativa de la nube como CloudFormation, y estandarízala en toda la organización para evitar un panorama de herramientas fragmentado. La práctica arquitectónica clave es la modularidad: construye módulos pequeños, bien documentados, y versionados que capturen patrones comunes (una red conforme, una base de datos endurecida, un servicio estándar). Los equipos entonces componen los entornos a partir de estos módulos en lugar de escribir recursos crudos. Esto propaga automáticamente buenos valores predeterminados y ajustes de seguridad y reduce drásticamente la duplicación.

### Gestiona el estado deliberadamente

Las herramientas declarativas rastrean el mapeo entre el código y los recursos reales en un archivo de estado. Almacena el estado remotamente en un backend compartido, cifrado, y con control de acceso, y usa bloqueo para que las modificaciones concurrentes no puedan corromperlo. Nunca mantengas el estado en una laptop, y nunca lo edites a mano excepto como una acción de recuperación de último recurso. El estado es sensible, porque puede contener metadatos de recursos y secretos, así que protégelo en consecuencia.

### Construye infraestructura inmutable con imágenes doradas

En lugar de parchear servidores en ejecución, cocina una «imagen dorada» versionada (una imagen de máquina o contenedor preconfigurada y endurecida) y despliega instancias frescas a partir de ella. Cuando necesites un cambio o parche, construye una nueva imagen y despliégala, retirando las instancias antiguas. Esto elimina la deriva de configuración, hace trivial la reversión, y mantiene cada instancia idéntica y rastreable hasta una construcción conocida como buena. Los canales de imagen automatizados deberían incluir el endurecimiento y escaneo de seguridad, así el cumplimiento se incorpora a nivel de imagen.

### Detecta y reconcilia la deriva de configuración

La deriva ocurre cuando el entorno en vivo diverge de su definición, usualmente porque alguien hizo un cambio manual de emergencia. Ejecuta detección de deriva regular que compare el estado real con el estado declarado y señale las diferencias. Trata la deriva como un defecto: reconcilia actualizando el código y volviendo a aplicar, no dejando el cambio manual en su lugar. Para los sistemas que necesitan aplicación continua de configuración, usa una herramienta de gestión de configuración que converja continuamente los hosts hacia su estado declarado.

### Adopta GitOps y el despliegue basado en extracción

En el modelo GitOps, un repositorio Git contiene el estado deseado declarado del sistema, y un agente automatizado que corre dentro del entorno objetivo continuamente extrae ese estado y reconcilia el sistema en vivo para que coincida. Esto invierte el modelo tradicional de empuje. Ningún sistema externo necesita credenciales permanentes para cambiar el entorno, porque el entorno extrae su propia configuración. GitOps te da un rastro de auditoría completo (cada cambio es un commit), reversión fácil (revierte el commit), y una corrección de deriva fuerte (el agente reafirma continuamente el estado deseado). Es especialmente poderoso para [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) y para organizaciones que quieren una única fuente de verdad revisable.

### Aplica barandillas con política como código

Expresa las reglas organizacionales, como regiones permitidas, cifrado obligatorio, etiquetas requeridas, y exposición pública prohibida, como políticas comprobables por máquina usando una herramienta como Open Policy Agent (OPA) o un motor de política nativo de plataforma como Sentinel. Ejecuta estas comprobaciones en el canal antes del aprovisionamiento, para que las violaciones se bloqueen automáticamente. La política como código convierte la intención de un equipo de seguridad en un control ejecutable y aplicado uniformemente, y escala a miles de cambios de una manera que la revisión manual nunca podría.

## Ventajas y desventajas

| Elección | Ventajas | Desventajas | Mejor ajuste |
|---|---|---|---|
| IaC declarativa (Terraform/Pulumi) | Reproducible, revisable, detectable ante deriva | Curva de aprendizaje; complejidad de gestión de estado | Casi todos los equipos a escala |
| Scripts imperativos | Familiar; flexible para casos únicos | No idempotente; difícil de auditar y repetir | Casos estrechos y transicionales |
| Inmutable + imágenes doradas | Sin deriva; reversión trivial | Sobrecarga del canal de construcción de imágenes | Flotas que necesitan consistencia |
| Gestión de configuración mutable | Control continuo de grano fino | Riesgo de deriva; convergencia más lenta | Hosts heredados o de larga vida |
| GitOps (basado en extracción) | Rastro de auditoría fuerte; autorreparable | Requiere un agente dentro del clúster y disciplina de Git | Kubernetes y nativo de la nube |
| Política como código | Barandillas automáticas y uniformes | Esfuerzo de redacción de política por adelantado | Entornos regulados |

La tensión principal es entre flexibilidad y control. Los enfoques manuales e imperativos se sienten más rápidos para un único cambio, pero acumulan inconsistencia oculta que se vuelve paralizante a escala. La infraestructura declarativa, inmutable, y gobernada por política pide más inversión por adelantado y un cambio cultural real, ya que los ingenieros tienen que dejar de hacer cambios rápidos en la consola, pero repaga esa inversión muchas veces en fiabilidad, auditabilidad, y la capacidad de reconstruir cualquier cosa a demanda.

## Preguntas para discutir con tu equipo

1. **¿Quién es dueño de la biblioteca de módulos compartida, y cómo llega una mejora en un módulo a cada equipo que lo usa?** Los módulos solo rinden frutos si las correcciones y los valores predeterminados endurecidos se propagan, y eso requiere propiedad clara y versionado real, no una carpeta de la que todos copian. Decide quién mantiene los módulos de red conforme y base de datos endurecida, cómo los versionas (versionado semántico con un registro de cambios), y cómo los equipos extraen actualizaciones sin un simulacro de incendio. A escala esto es la diferencia entre arreglar una mala configuración una vez y perseguirla a través de mil recursos editados a mano. Trae evidencia: cuántas copias distintas del mismo patrón existen hoy, cuánto tarda una corrección de seguridad en llegar a cada entorno, y si los equipos fijan las versiones de módulo o las dejan flotar. Si un parche crítico no puede llegar a todo el patrimonio en días, tu modularidad es cosmética.

2. **¿Cuál es tu cadencia de detección de deriva, y qué pasa realmente cuando se encuentra deriva?** La deriva es el entorno en vivo divergiendo silenciosamente de su estado declarado, usualmente por un cambio de consola de emergencia, y tolerarla convierte tu código en ficción. Decide con qué frecuencia comparas el estado real con el estado declarado (nocturno es un valor predeterminado razonable) y, más importante, decide la respuesta: reconcilia actualizando el código y volviendo a aplicar, nunca dejando el cambio manual en su lugar. En entornos regulados esto es un requisito de control, porque los auditores necesitan que el estado declarado coincida con la realidad continuamente. Trae tus números actuales: cuántos recursos derivan cada semana, cuánto tiempo permanecen derivados, y si alguien es responsable de cerrarlos. Trata cada deriva como un defecto con un dueño, o la garantía de fuente de verdad se erosiona hasta que nadie confía en el código.

3. **¿Te has movido a GitOps y reconciliación basada en extracción, o un sistema externo todavía tiene credenciales permanentes para cambiar producción?** En el modelo de extracción, un agente dentro del entorno objetivo reconcilia continuamente el sistema en vivo con Git, lo cual elimina la necesidad de que cualquier sistema externo tenga acceso de escritura, y reafirma el estado deseado para que la deriva se autocorrija. Esa es una postura fuerte de seguridad y auditoría, ya que cada cambio es un commit y ningún operador necesita credenciales permanentes de producción. El costo es real: un agente dentro del clúster que operar y disciplina estricta de Git, así que pésalo contra tu automatización actual basada en empuje. Trae la lista de quién y qué puede actualmente mutar producción directamente, y qué rastro de auditoría dejan esos cambios. Para Kubernetes y enclaves de alta garantía este cambio usualmente vale la pena; para un puñado de recursos estáticos puede ser excesivo.

4. **¿Cómo se almacena, bloquea, y controla el acceso a tu estado de infraestructura, y qué pasa el día que se corrompe o se pierde?** El estado es el mapa entre tu código y los recursos reales, así que un archivo de estado perdido o dañado puede dejar a una herramienta ciega ante recursos que creó y tentar a alguien hacia una reaplicación destructiva. Para un equipo grande el riesgo se multiplica, porque muchos ingenieros aplicando contra un estado compartido necesitan un backend remoto, cifrado, y bloqueado para que las ejecuciones concurrentes no puedan destruirse entre sí. Pesa la conveniencia de un único estado grande contra el radio de impacto que crea, y considera dividir el estado por entorno o por dominio para que un único error no pueda derribar todo. Trae los hechos: dónde vive el estado hoy, si el bloqueo se aplica, quién puede leerlo (puede contener secretos), y si alguna vez has ensayado una recuperación. En entornos empresariales y gubernamentales, trata el backend de estado como un activo sensible y con control de acceso con su propia copia de seguridad, registro de auditoría, y runbook de recuperación, porque perderlo es perder tu registro de lo que existe.

5. **Cuando una emergencia genuina exige un cambio manual, ¿cuál es la ruta de rotura de vidrio sancionada, y cómo se incorpora ese cambio de vuelta al código?** Toda práctica madura de IaC eventualmente encuentra el incidente de las 3 de la madrugada donde esperar un canal no es aceptable, y la pregunta honesta no es si alguna vez ocurren cambios manuales sino cómo los contienes. Decide de antemano quién puede saltarse el canal, qué se le permite tocar, cómo se registra la acción, y el plazo para el cual el cambio debe reconciliarse en código o revertirse. Sin ese acuerdo, la excepción de emergencia se convierte silenciosamente en el hábito cotidiano y el ClickOps regresa por la puerta trasera. Trae evidencia: cuántos cambios fuera de banda ocurrieron el último trimestre, cuánto tiempo permaneció cada uno sin reconciliar, y si la detección de deriva realmente los atrapó. Para organismos regulados y públicos, un procedimiento de rotura de vidrio documentado con registro automático a menudo es un requisito de control, porque los auditores esperan tanto que las emergencias sean posibles como que cada una deje un rastro y devuelva el sistema a su estado declarado.

6. **¿Cuánto de tu línea base de seguridad y cumplimiento se expresa como política que automáticamente bloquea un mal cambio, frente a reglas que viven en un documento y dependen de que alguien las recuerde?** Las barandillas escritas como prosa en una wiki se violan rutinariamente, porque dependen de que cada ingeniero las lea y aplique bajo presión de plazo, mientras las mismas reglas expresadas como política como código rechazan un cambio no conforme antes de que se aprovisione. Para una organización grande esta es la única manera en que la intención de un equipo de seguridad escala a miles de cambios sin convertirse en un cuello de botella de revisión. Pesa el costo por adelantado de redactar y mantener las políticas contra el costo recurrente de la revisión manual y la remediación posterior, y decide qué controles (cifrado, regiones aprobadas, etiquetas obligatorias, sin exposición pública) son lo bastante innegociables para aplicarse como puertas duras. Trae la lista de tus reglas de línea base actuales y marca cuáles están automatizadas frente a consultivas, más con qué frecuencia se viola cada una en la práctica. En contextos empresariales y gubernamentales, la política automatizada convierte una auditoría de semanas de recolección manual de evidencia en una consulta contra controles aplicados, y convierte el cumplimiento de detección en prevención.

## Perspectiva sectorial

**Startup.** La velocidad gana, así que pon toda tu pila en un único repositorio declarativo (Terraform es un valor predeterminado común), mantén el estado en un backend gestionado y cifrado, y enruta cada cambio a través de una solicitud de extracción incluso con un equipo de tres. Salta el aparato pesado de plataforma: sin equipo central de módulos, sin motor de política todavía, solo control de versiones y la disciplina de nunca hacer clic en la consola. Eso solo te da entornos reproducibles que puedes derribar para ahorrar dinero y reconstruir para la próxima demostración.

**Pequeña empresa.** Sin un especialista de plataforma dedicado, apóyate en servicios gestionados y cualquier IaC que tu proveedor de nube o proveedor ya soporte en lugar de levantar herramientas a medida que no puedes mantener. Favorece comprar una plataforma alojada cuyos valores predeterminados sensatos (cifrado, copias de seguridad, parches) se manejen por ti sobre construir un canal de imagen dorada que no tienes a nadie que opere. Enmarca la meta estrechamente: mete tu puñado de recursos críticos en código para poder reconstruirlos después de un fallo o un contratista que se va.

**Empresa.** El problema central es la consistencia entre muchos equipos, cuentas, y regiones, así que invierte en una biblioteca de módulos compartida y versionada, estado remoto bloqueado, y política como código aplicada en el canal. Un equipo de plataforma central publica módulos y barandillas endurecidos mientras los equipos de producto se autoatienden dentro de ellos, y la detección de deriva corre continuamente para que miles de recursos se mantengan en un estado conocido. Presupuesta el costo continuo de mantener los módulos y políticas, porque su valor viene de una corrección o un valor predeterminado endurecido propagándose en todas partes a la vez.

**Gobierno.** Las reglas de contratación pública, la acreditación, y la rendición de cuentas pública te empujan hacia la infraestructura inmutable, los commits firmados, y la reconciliación GitOps dentro de un enclave acreditado, así que ningún operador tiene credenciales permanentes para cambiar producción. Codifica la línea base de seguridad requerida en imágenes doradas y política como código, y deja que el historial de commits sirva como evidencia de auditoría a prueba de manipulación y continuamente disponible. Favorece las herramientas abiertas y portables sobre los formatos propietarios que te atrapan, y haz explícito el procedimiento de rotura de vidrio y su registro para que los cambios de emergencia todavía satisfagan los requisitos de control de configuración.

## Ejemplos

**Startup.** Una startup de cinco personas define toda su configuración de AWS, es decir, la VPC, la base de datos, y el servicio de contenedores, en un único repositorio de Terraform con el estado guardado en un backend S3 cifrado y bloqueo a través de DynamoDB. Cada cambio pasa por una solicitud de extracción, así que incluso un ingeniero de guardia solitario puede ver exactamente qué cambiará antes de ejecutar apply. Cuando necesitan un entorno de staging fresco para una gran demostración, copian un pequeño módulo y lo levantan en minutos, y lo derriban igual de rápido para mantener baja la factura de la nube.

**Empresa.** Un minorista multinacional gestiona infraestructura a través de varias cuentas y regiones de la nube. Un equipo de plataforma central publica módulos de Terraform versionados para redes conformes, bases de datos, y andamiaje de servicio, y aplica políticas OPA que rechazan cualquier recurso que carezca de cifrado o etiquetas de asignación de costo. Los equipos de producto aprovisionan sus propios entornos de autoservicio, pero cada cambio fluye a través del canal, donde la política se comprueba automáticamente. La detección de deriva corre cada noche y abre tickets para cualquier cambio manual, manteniendo miles de recursos continuamente en un estado conocido y conforme.

**Gobierno.** Una agencia de defensa que opera en un entorno de alta garantía construye imágenes doradas endurecidas que incrustan la línea base de seguridad requerida, y despliega solo instancias inmutables a partir de esas imágenes. Toda la infraestructura se declara en Git y se reconcilia mediante un agente GitOps dentro del enclave acreditado, así que ningún operador tiene credenciales permanentes para cambiar producción directamente. Cada cambio es un commit firmado. Esto da a los auditores un historial completo y a prueba de manipulación y satisface los requisitos de monitoreo continuo y control de configuración sin recolección manual de evidencia.

## Caso de negocio: motivaciones, ROI y TCO

El ROI de la IaC viene de la velocidad, la fiabilidad, y la reducción de riesgo. Los entornos que antes tomaban semanas de aprovisionamiento manual impulsado por tickets pueden crearse en minutos, lo cual libera a los ingenieros y acelera los proyectos. La reproducibilidad recorta drásticamente el tiempo de recuperación después de fallos, porque cualquier entorno puede reconstruirse a partir del código. La aplicación automatizada de política reduce la frecuencia y el costo de los incidentes de seguridad y los hallazgos de auditoría, que para las organizaciones reguladas pueden ser sustanciales.

En el libro mayor del TCO, los costos de adopción incluyen herramientas, capacitación, construir una biblioteca de módulos y política, y la disciplina de dejar de hacer cambios manuales. El costo de no adoptar es más empinado y se compone con el tiempo: infraestructura copo de nieve que nadie puede reconstruir, aprovisionamiento lento y propenso a errores, malas configuraciones de seguridad que llevan a brechas, y auditorías que consumen semanas de esfuerzo manual. Para el liderazgo, enmarca la IaC como convertir la infraestructura de un pasivo sin gestionar en un activo gobernado y reproducible, y como el mecanismo que hace que la seguridad y el cumplimiento sean automáticos en lugar de aspiracionales.

## Antipatrones y trampas

- **ClickOps en producción.** Hacer cambios a mano en la consola garantiza la deriva y destruye la reproducibilidad.
- **Secretos en el código.** Codificar credenciales de forma fija en los archivos de definición los filtra al historial de versiones y al estado.
- **Definiciones monolíticas y no modularizadas.** Una configuración enorme única que nadie se atreve a cambiar se vuelve tan frágil como la configuración manual que reemplazó.
- **Estado sin gestionar.** Los archivos de estado locales o sin bloquear llevan a la corrupción e infraestructura perdida.
- **Deriva tolerada.** Dejar los cambios manuales en su lugar erosiona la garantía de fuente de verdad hasta que el código es ficción.
- **Política como documentación.** Las reglas que viven en una wiki en lugar de una comprobación automatizada se violan rutinariamente.
- **Proliferación de copiar y pegar.** Duplicar la configuración entre equipos significa que las correcciones y mejoras nunca se propagan.

## Modelo de madurez

**Nivel 1: Iniciar.** La infraestructura se aprovisiona manualmente a través de la consola y scripts ad hoc. Los entornos son inconsistentes, no documentados, y no pueden reproducirse de forma confiable, y la recuperación de un fallo es lenta e incierta.

**Nivel 2: Desarrollar.** Algo de infraestructura está codificada, pero las prácticas varían por equipo. La gestión de estado es inconsistente, la deriva es común, los secretos a veces se filtran a las definiciones, y la política se aplica, si acaso, a través de la revisión manual.

**Nivel 3: Estandarizar.** La IaC declarativa es el estándar documentado en toda la organización, construida a partir de módulos compartidos y versionados con estado gestionado, remoto, y bloqueado. La política como código aplica barandillas en el canal, los secretos se referencian desde un gestor dedicado, y la detección de deriva corre en una cadencia regular.

**Nivel 4: Gestionar.** La práctica se mide contra líneas base. Rastreas la tasa de deriva y el tiempo medio de reconciliación, la adopción de versiones de módulo entre equipos, las violaciones de política bloqueadas frente a las escapadas, el tiempo de espera de aprovisionamiento, y el porcentaje de recursos realmente bajo código. Estas métricas bloquean los cambios y dirigen dónde inviertes, así que las decisiones descansan en evidencia en lugar de anécdota.

**Nivel 5: Orquestar.** La infraestructura es inmutable e impulsada por GitOps, autorreparable ante la deriva, con evidencia de cumplimiento producida automáticamente. La biblioteca de módulos y política mejora continuamente a partir del uso real y los incidentes, y la práctica de infraestructura está integrada con la planificación de seguridad, costo, y entrega para que todo el patrimonio se adapte a medida que cambian los requisitos.

## Ideas para el debate

- ¿Dónde debería situarse la línea entre los módulos gobernados centralmente y la autonomía del equipo para definir infraestructura personalizada?
- ¿Cómo manejas el cambio de emergencia genuino que debe saltarse el canal, sin normalizar el ClickOps?
- ¿Cuál es la estrategia correcta para gestionar y asegurar el estado a través de muchas cuentas y equipos?
- ¿Cuándo se justifica todavía la gestión de configuración mutable frente a la infraestructura completamente inmutable?
- ¿Cómo mantienes alineada la biblioteca de política como código con los requisitos de seguridad y regulatorios en evolución?
- ¿Cómo se ve una ruta de migración realista para la infraestructura heredada que precede a la IaC?

## Puntos clave

- Define la infraestructura declarativamente, versiónala, y trátala como código revisable y reproducible.
- Construye a partir de módulos pequeños y versionados para propagar buenos valores predeterminados y eliminar la duplicación.
- Prefiere la infraestructura inmutable y las imágenes doradas para abolir la deriva y simplificar la reversión.
- Gestiona el estado deliberadamente y mantén los secretos fuera de las definiciones.
- Adopta GitOps para un rastro de auditoría fuerte y una reconciliación autorreparable.
- Aplica barandillas con política como código para que el cumplimiento se prevenga en su existencia, no se audite después del hecho.

## Referencias y lecturas adicionales

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, y Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, y John Willis, *The DevOps Handbook*.
- Weaveworks, escritos fundacionales sobre «GitOps» (Alexis Richardson et al.).
- Documentación de Open Policy Agent y el lenguaje de política Rego.
- NIST Special Publication 800-53, controles de seguridad y privacidad (familia de gestión de configuración).
