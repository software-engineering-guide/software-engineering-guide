# 12.2 Listas de verificación

Estas listas de verificación son referencias rápidas, prácticas y listas para usar. Copia cualquier lista en una plantilla de solicitud de extracción, una página de wiki, un ticket, o una agenda de reunión de revisión, y adapta los elementos a tu contexto. Trata cada elemento como algo que una persona puede verificar y responder sí o no. Una lista de verificación es una ayuda de memoria y un estándar compartido, no un sustituto del juicio; elimina los elementos que no aplican y agrega los elementos que tu dominio requiere.

Guía para usarlas bien:

- Mantén las listas de verificación lo suficientemente cortas para que la gente realmente las complete. Si una lista de verificación se salta rutinariamente, es demasiado larga o demasiado genérica.
- Automatiza cualquier elemento que una máquina pueda verificar (formato, pruebas, escaneos) para que los humanos gasten su atención en elementos de juicio.
- Versiona tus listas de verificación y revísalas periódicamente. Una lista de verificación que nunca cambia probablemente no se está usando.
- Distingue los elementos bloqueantes de los elementos consultivos cuando la distinción importa para tu proceso.

## Lista de verificación de revisión de código

Para el revisor que examina el cambio de otra persona.

- [ ] El cambio hace lo que dice su descripción y el ticket enlazado.
- [ ] El alcance se enfoca en una única preocupación lógica; los cambios no relacionados se separan.
- [ ] El diseño se ajusta a la arquitectura existente y no introduce un acoplamiento más fácil de evitar.
- [ ] Los casos límite, las rutas de error, y los modos de fallo se manejan, no solo el camino feliz.
- [ ] Existen pruebas, son significativas, y fallarían si el comportamiento regresara.
- [ ] Los nombres, la estructura, y los comentarios hacen el código comprensible para un lector futuro.
- [ ] No se confirman secretos, credenciales, tokens, o datos personales.
- [ ] La entrada sensible a la seguridad se valida, codifica, o parametriza apropiadamente.
- [ ] Las interfaces públicas, los contratos, y la compatibilidad hacia atrás se preservan o se versionan intencionalmente.
- [ ] El registro, las métricas, y el reporte de errores son adecuados para operar el cambio en producción.
- [ ] La documentación, los manuales de operación, y la configuración se actualizan para coincidir con el cambio.
- [ ] La retroalimentación se separa en problemas bloqueantes versus sugerencias, y se expresa sobre el código.

## Lista de verificación del autor de la solicitud de extracción

Para el autor antes de solicitar revisión.

- [ ] La PR es lo suficientemente pequeña y enfocada para revisar cuidadosamente en una sola sesión.
- [ ] La descripción declara qué cambió, por qué, y cómo se verificó.
- [ ] El ticket, incidencia, o documento de diseño enlazado da a los revisores el contexto necesario.
- [ ] Todas las verificaciones automatizadas pasan localmente o en CI (construcción, linting, formato, pruebas, escaneos).
- [ ] El comportamiento nuevo y cambiado está cubierto por pruebas.
- [ ] Las refactorizaciones mecánicas se separan de los cambios de comportamiento.
- [ ] La autorrevisión está completa: has leído tu propio diff línea por línea.
- [ ] No queda código de depuración, bloques comentados, secretos, o archivos sueltos.
- [ ] Las migraciones de base de datos, las banderas de características, y los cambios de configuración están documentados y son reversibles.
- [ ] Los cambios disruptivos se señalan explícitamente con una ruta de migración.
- [ ] Se incluyen capturas de pantalla, grabaciones, o salida de muestra donde ayudan a la revisión.
- [ ] Se solicitan los revisores correctos y cualquier aprobador basado en rol requerido.

## Definición de terminado

El estándar compartido que un elemento de trabajo debe cumplir antes de considerarse completo.

- [ ] Los criterios de aceptación en el ticket se cumplen todos y son demostrables.
- [ ] El código se revisa entre pares y lo aprueban los revisores requeridos.
- [ ] Las pruebas automatizadas están escritas, pasan, y se fusionan con el cambio.
- [ ] El código se fusiona en la línea principal y se despliega limpiamente a través del pipeline.
- [ ] No quedan abiertos defectos conocidos del umbral de severidad acordado.
- [ ] La documentación, el texto de ayuda, y los manuales de operación se actualizan.
- [ ] La observabilidad está en su lugar: existen los registros, métricas, y alertas relevantes.
- [ ] Se han considerado y abordado las implicaciones de seguridad y privacidad.
- [ ] Se cumplen los requisitos de accesibilidad para el cambio donde es orientado al usuario.
- [ ] Las banderas de características están configuradas y se acuerda el plan de despliegue.
- [ ] El dueño de producto o interesado ha aceptado el resultado.
- [ ] Cualquier trabajo de seguimiento se captura como tickets rastreados, no se deja implícito.

## Preparación para la puesta en marcha en producción

Antes de enviar un cambio significativo o un servicio nuevo a producción.

- [ ] El plan de despliegue está documentado, incluyendo pasos escalonados o canario y criterios de éxito.
- [ ] El plan de retroceso está documentado, probado, y puede ejecutarse rápidamente.
- [ ] Las pruebas de capacidad y carga muestran que el sistema cumple la demanda esperada y pico.
- [ ] El monitoreo, los tableros, y las alertas están en vivo y validados antes del lanzamiento.
- [ ] La cobertura de guardia está programada y los respondientes conocen el sistema.
- [ ] Existen manuales de operación para los escenarios de fallo y operativos más probables.
- [ ] Las dependencias, integraciones, y terceros se confirman listos y se entienden los límites de tasa.
- [ ] La revisión de seguridad y las aprobaciones requeridas están completas.
- [ ] La migración de datos, si la hay, se prueba de extremo a extremo con un retroceso verificado.
- [ ] Las banderas de características permiten deshabilitar el cambio sin un redespliegue.
- [ ] Se obtienen las aprobaciones legales, de privacidad, y de cumplimiento donde se requiere.
- [ ] El plan de comunicaciones cubre a los interesados, el soporte, y los clientes.
- [ ] Se toma una decisión de continuar/no continuar por dueños nombrados contra criterios explícitos.

## Lista de verificación de revisión de seguridad / modelado de amenazas

Para evaluar la postura de seguridad de un cambio o sistema.

- [ ] Los límites de confianza y los flujos de datos están identificados y documentados.
- [ ] La autenticación se aplica en cada punto de entrada que la requiere.
- [ ] Las verificaciones de autorización aplican el privilegio mínimo para cada acción y recurso.
- [ ] Toda la entrada externa se valida, y la salida se codifica para su destino.
- [ ] Los secretos se almacenan en una bóveda gestionada, nunca en código o configuración, y son rotables.
- [ ] Los datos se cifran en tránsito y en reposo según lo requiere la clasificación.
- [ ] Las dependencias se escanean por vulnerabilidades conocidas y se mantienen actuales.
- [ ] Los riesgos de inyección, deserialización, y SSRF se mitigan para la entrada no confiable.
- [ ] Los eventos relevantes de seguridad se registran sin grabar datos sensibles.
- [ ] La limitación de tasa, las cuotas, y las protecciones contra el abuso protegen los puntos finales expuestos.
- [ ] Los mensajes de error no filtran trazas de pila, detalles internos, o información sensible.
- [ ] Las amenazas identificadas mediante STRIDE o similar se registran con mitigaciones o riesgo aceptado.
- [ ] Las pruebas de seguridad (SAST, DAST, o pruebas de penetración) se planifican o completan.

## Lista de verificación de privacidad y protección de datos (estilo DPIA)

Para el procesamiento que involucra datos personales o sensibles.

- [ ] Los datos personales recolectados se inventarían, clasifican, y minimizan a lo necesario.
- [ ] La base legal o autoridad para cada propósito de procesamiento está documentada.
- [ ] La limitación de propósito se aplica: los datos se usan solo para los propósitos declarados.
- [ ] Los períodos de retención están definidos y la eliminación o anonimización se automatiza.
- [ ] Los derechos del titular de datos (acceso, corrección, eliminación, portabilidad) pueden cumplirse.
- [ ] El consentimiento, donde se usa, se da libremente, específicamente, y es revocable.
- [ ] Los terceros y procesadores están sujetos a términos adecuados de protección de datos.
- [ ] Las transferencias transfronterizas tienen un mecanismo legal de transferencia apropiado.
- [ ] El acceso a los datos personales está restringido, registrado, y revisado.
- [ ] Los riesgos de privacidad para los individuos se evalúan y mitigan o escalan.
- [ ] Los procesos de detección y notificación de brechas de datos están definidos.
- [ ] La privacidad por diseño y las elecciones predeterminadas están documentadas para la característica.
- [ ] El oficial de protección de datos o revisor de privacidad ha aprobado donde se requiere.

## Lista de verificación de accesibilidad (WCAG)

Para interfaces orientadas al usuario, alineadas a los principios WCAG.

- [ ] Todo el contenido es alcanzable y operable usando solo un teclado.
- [ ] El orden de enfoque es lógico y hay un indicador de enfoque visible.
- [ ] El contraste de color del texto cumple la proporción objetivo (típicamente 4.5:1 para el texto del cuerpo).
- [ ] Las imágenes y el contenido no textual tienen texto alternativo significativo.
- [ ] Los campos de formulario tienen etiquetas asociadas y mensajes de error claros.
- [ ] Los encabezados, puntos de referencia, y la estructura están marcados semánticamente.
- [ ] Los componentes interactivos exponen el nombre, rol, y estado correctos a la tecnología asistiva.
- [ ] El contenido se reajusta y permanece usable al 200% de zoom y en pantallas pequeñas.
- [ ] Los límites de tiempo son ajustables, y el contenido en movimiento o de reproducción automática puede pausarse.
- [ ] El color no es el único medio de transmitir información.
- [ ] Los medios tienen subtítulos y, donde se necesita, transcripciones o audiodescripción.
- [ ] La interfaz se prueba con un lector de pantalla y herramientas de accesibilidad automatizadas.

## Lista de verificación de revisión de diseño de API

Antes de publicar o cambiar una API.

- [ ] El nombramiento de recursos y operaciones es consistente y predecible.
- [ ] El contrato se especifica en un esquema legible por máquina (por ejemplo OpenAPI).
- [ ] La estrategia de versionamiento está definida y la compatibilidad hacia atrás se preserva o gestiona.
- [ ] La paginación, el filtrado, y la ordenación siguen convenciones consistentes.
- [ ] Las respuestas de error usan estructura, códigos, y mensajes accionables consistentes.
- [ ] La autenticación y autorización se especifican para cada operación.
- [ ] La validación de entrada y los límites de tamaño están definidos y se aplican.
- [ ] La idempotencia está definida para las operaciones donde se esperan reintentos.
- [ ] Los límites de tasa, las cuotas, y el comportamiento de estrangulamiento están documentados.
- [ ] Los tiempos de espera, los reintentos, y la semántica de fallo son claros para los clientes.
- [ ] La exposición de datos sensibles en las respuestas se minimiza y justifica.
- [ ] La documentación incluye ejemplos para cada operación y caso de error.
- [ ] La política de obsolescencia y los cronogramas de desactivación están definidos.

## Lista de verificación de revisión de decisión de arquitectura (ADR)

Para revisar un registro de decisión de arquitectura propuesto.

- [ ] El contexto y el problema que se resuelve se declaran claramente.
- [ ] La decisión se declara sin ambigüedad como una única elección.
- [ ] Se consideraron y compararon al menos dos alternativas realistas.
- [ ] Las consecuencias, tanto positivas como negativas, están documentadas.
- [ ] Los impactos no funcionales (rendimiento, seguridad, costo, operabilidad) se abordan.
- [ ] La decisión se alinea con los principios existentes y los ADR previos, o los reemplaza explícitamente.
- [ ] Se consultó a los equipos e interesados afectados.
- [ ] Se evalúan la reversibilidad y el costo del cambio.
- [ ] Los supuestos y restricciones se hacen explícitos.
- [ ] El estado (propuesto, aceptado, reemplazado) se establece y se fecha.
- [ ] La decisión es descubrible y está enlazada desde los sistemas relevantes.
- [ ] Cualquier acción de seguimiento o migración se captura como trabajo rastreado.

## Lista de verificación de respuesta a incidentes

Durante un incidente de producción activo.

- [ ] Declara el incidente y asigna un único comandante de incidente.
- [ ] Evalúa y comunica la severidad, el alcance, y el impacto al cliente.
- [ ] Abre un canal de comunicación dedicado y un registro de incidente.
- [ ] Asigna roles claros: comandante, líder de comunicaciones, y líder de operaciones.
- [ ] Prioriza la mitigación y la restauración del servicio sobre el análisis de causa raíz.
- [ ] Publica actualizaciones de estado regulares a los interesados en una cadencia establecida.
- [ ] Captura una línea de tiempo de eventos, acciones, y decisiones conforme suceden.
- [ ] Escala a respondientes adicionales o proveedores cuando se necesite.
- [ ] Notifica a legal, seguridad, y cumplimiento si están involucrados datos o regulación.
- [ ] Verifica la corrección y confirma que el sistema se ha recuperado completamente.
- [ ] Cierra formalmente el incidente y comunica la resolución.
- [ ] Programa la autopsia sin culpa antes de que la gente se disperse.

## Lista de verificación de autopsia

Para la revisión retrospectiva después de un incidente.

- [ ] La revisión es sin culpa y se enfoca en los sistemas y factores contribuyentes.
- [ ] Se documenta una línea de tiempo factual y con marca de tiempo del incidente.
- [ ] El impacto al cliente y al negocio se cuantifica (duración, alcance, costo).
- [ ] La detección se analiza: cómo y cuándo se notó el problema.
- [ ] La respuesta se analiza: qué ayudó y qué ralentizó la recuperación.
- [ ] Se identifican las causas contribuyentes, no solo una única causa raíz.
- [ ] Se registra lo que salió bien, así como lo que salió mal.
- [ ] Los elementos de acción son específicos, asignados a dueños, y tienen fechas límite.
- [ ] Los elementos de acción abordan la prevención, la detección, y la mitigación.
- [ ] Los elementos de seguimiento se rastrean hasta completarse en el backlog normal.
- [ ] La autopsia se comparte ampliamente para que otros puedan aprender de ella.
- [ ] Los patrones sistémicos entre incidentes se revisan periódicamente.

## Lista de verificación de preparación de guardia

Antes de que alguien tome un turno de guardia.

- [ ] El respondiente tiene acceso a todos los sistemas, tableros, y herramientas que necesita.
- [ ] Las alertas llegan al respondiente confiablemente y están probadas.
- [ ] Las rutas de escalación y los contactos secundarios de guardia se conocen y están actuales.
- [ ] Existen manuales de operación para las alertas más comunes y más severas.
- [ ] El respondiente ha completado la incorporación o la observación acompañada para estos sistemas.
- [ ] Los cambios recientes, los incidentes en curso, y los problemas conocidos se transfieren.
- [ ] Los umbrales de alerta están ajustados para minimizar el ruido y las alertas falsas.
- [ ] El respondiente sabe cómo declarar un incidente y contactar al comandante.
- [ ] El acceso a producción es posible desde el entorno de trabajo del respondiente.
- [ ] Los canales de comunicación y los contactos de interesados están documentados.
- [ ] El calendario de guardia está publicado y la cobertura no tiene brechas.
- [ ] La compensación, las expectativas, y los límites de carga de trabajo para la guardia son claros.

## Lista de verificación de definición de SLO

Al definir un objetivo de nivel de servicio.

- [ ] El recorrido del usuario o la capacidad que el SLO protege está claramente identificado.
- [ ] Los indicadores de nivel de servicio (SLI) se definen como cantidades claras y medibles.
- [ ] Los SLI se miden desde la perspectiva del usuario donde sea posible.
- [ ] El objetivo se establece en un nivel que los usuarios realmente necesitan, no 100%.
- [ ] La ventana de medición (por ejemplo 28 días móviles) está especificada.
- [ ] El presupuesto de error derivado del objetivo se calcula y se entiende.
- [ ] Una política define qué sucede cuando se agota el presupuesto de error.
- [ ] Las fuentes de datos para los SLI son confiables y están instrumentadas.
- [ ] Las alertas están atadas a la tasa de consumo, no solo a las violaciones de umbral.
- [ ] Los dueños e interesados acuerdan que el SLO es realista y significativo.
- [ ] El SLO está documentado y visible en un tablero.
- [ ] Existe un calendario para revisar y revisar los SLO conforme evoluciona el servicio.

## Lista de verificación de pipeline de CI/CD

Para un pipeline de integración y entrega continua.

- [ ] Cada commit activa una construcción y ejecución de pruebas automatizadas.
- [ ] El pipeline falla rápido y reporta los resultados claramente a los autores.
- [ ] El linting, el formato, y el análisis estático se ejecutan automáticamente.
- [ ] Las pruebas unitarias, de integración, y de extremo a extremo relevantes se ejecutan en el pipeline.
- [ ] El escaneo de seguridad y dependencias se ejecuta en cada construcción.
- [ ] Los artefactos de construcción están versionados, son inmutables, y se almacenan en un registro.
- [ ] Los secretos se inyectan de forma segura y nunca se imprimen en los registros.
- [ ] Los despliegues son automatizados y repetibles a través de los entornos.
- [ ] La estrategia de despliegue (canario, azul-verde, rodante) está definida y se usa.
- [ ] El retroceso es automatizado o una única acción documentada.
- [ ] Los permisos del pipeline siguen el privilegio mínimo y son auditables.
- [ ] La configuración del pipeline se almacena en control de versiones como código.
- [ ] La procedencia de la construcción y una lista de materiales de software se producen donde se requiere.

## Lista de verificación de revisión de infraestructura como código

Para revisar la infraestructura definida como código.

- [ ] Los cambios se expresan enteramente en código y se aplican a través del pipeline.
- [ ] Se revisa un plan o salida de ensayo antes de aplicar.
- [ ] El estado se almacena de forma segura con bloqueo para prevenir cambios concurrentes.
- [ ] Los recursos siguen convenciones de nombramiento, etiquetado, y propiedad.
- [ ] Se usan roles y políticas de IAM de privilegio mínimo, sin comodines donde se pueda evitar.
- [ ] La exposición de red se minimiza; sin acceso público no intencionado.
- [ ] Los secretos y valores sensibles se referencian desde una bóveda, no se codifican de forma fija.
- [ ] El cifrado está habilitado para el almacenamiento, las bases de datos, y el tránsito.
- [ ] Los cambios son idempotentes y seguros de reaplicar.
- [ ] El radio de explosión se entiende; los cambios destructivos se señalan.
- [ ] Se considera el impacto de costo del cambio.
- [ ] Los módulos son reutilizables, versionados, y probados.
- [ ] La detección de deriva está en su lugar para capturar cambios fuera de banda.

## Lista de verificación de liberación de modelo de IA/AA

Antes de liberar un modelo de aprendizaje automático a producción.

- [ ] El uso pretendido, alcance, y limitaciones del modelo están documentados.
- [ ] La procedencia, licenciamiento, y consentimiento de los datos de entrenamiento y evaluación se verifican.
- [ ] Los datos y el modelo están versionados y son reproducibles.
- [ ] El rendimiento se evalúa en datos de prueba representativos y reservados.
- [ ] La equidad y el sesgo se evalúan a través de los subgrupos relevantes.
- [ ] El modelo se evalúa contra el titular o una línea base.
- [ ] Los modos de fallo, casos límite, y el comportamiento fuera de distribución se entienden.
- [ ] Los riesgos de seguridad, mal uso, y salida dañina se evalúan y mitigan.
- [ ] El monitoreo de la deriva, la calidad de datos, y la degradación del rendimiento está en su lugar.
- [ ] Existe un retroceso o respaldo a un modelo previo o ruta basada en reglas.
- [ ] Se provee supervisión humana o apelación para decisiones consecuentes.
- [ ] La revisión de privacidad cubre los datos de entrenamiento y las entradas y salidas de inferencia.
- [ ] Se publica una ficha de modelo o documentación equivalente para los interesados.

## Lista de verificación de calidad de pipeline de datos

Para un pipeline de datos que alimenta la analítica o los productos.

- [ ] Los esquemas de datos fuente se validan y los cambios de esquema se detectan.
- [ ] La ingesta maneja correctamente los registros tardíos, duplicados, y fuera de orden.
- [ ] Las verificaciones de calidad de datos (completitud, unicidad, rangos) se ejecutan automáticamente.
- [ ] Los registros fallidos se ponen en cuarentena y salen a la superficie, no se descartan silenciosamente.
- [ ] Las transformaciones se prueban con entradas representativas y de caso límite.
- [ ] El pipeline es idempotente y seguro de reejecutar después de un fallo.
- [ ] La frescura y la latencia de las salidas se monitorean contra las expectativas.
- [ ] El linaje está documentado para que los consumidores sepan de dónde vienen los datos.
- [ ] Los datos personales y sensibles se clasifican, enmascaran, o restringen apropiadamente.
- [ ] Los rellenos y el reprocesamiento están soportados y documentados.
- [ ] Las alertas notifican a los dueños de fallos y violaciones de calidad.
- [ ] Las políticas de retención y eliminación se aplican a los datos almacenados.
- [ ] Los consumidores descendentes y los SLA están documentados.

## Lista de verificación de admisión de código abierto y revisión de licencias

Antes de adoptar un componente de código abierto.

- [ ] La licencia del componente está identificada y está en la lista aprobada.
- [ ] Las obligaciones de licencia (atribución, copyleft, avisos) se entienden y se cumplen.
- [ ] Se confirma la compatibilidad de licencia con tu modelo de distribución.
- [ ] El proyecto está activamente mantenido y tiene una comunidad sana.
- [ ] Se verifican las vulnerabilidades conocidas y la versión es actual.
- [ ] La dependencia y sus dependencias transitivas están inventariadas.
- [ ] Se revisan la postura de seguridad y el historial de incidentes pasados.
- [ ] El componente cubre una necesidad real sin duplicación significativa.
- [ ] Se consideran el costo de salida y la reemplazabilidad del componente.
- [ ] El componente se registra en la lista de materiales de software.
- [ ] Un dueño nombrado es responsable de rastrear las actualizaciones y avisos.
- [ ] Se siguen las políticas de contribución hacia atrás y bifurcación interna si se modifica.

## Lista de verificación de riesgo de proveedor / tercero

Antes de incorporar un proveedor o servicio externo.

- [ ] La necesidad de negocio y los datos a los que accederá el proveedor están claramente definidos.
- [ ] La postura de seguridad del proveedor se evalúa (certificaciones, auditorías, cuestionario).
- [ ] Los términos de procesamiento de datos, la propiedad, y la eliminación a la salida son contractualmente claros.
- [ ] Los subprocesadores y las ubicaciones de datos del proveedor se divulgan y son aceptables.
- [ ] Se verifica el cumplimiento con las regulaciones relevantes.
- [ ] Los compromisos de tiempo de actividad, soporte, y SLA están documentados.
- [ ] Las obligaciones y cronogramas de notificación de brechas están en el contrato.
- [ ] El acceso tiene alcance de privilegio mínimo y es revocable.
- [ ] Se evalúan la continuidad de negocio y el impacto del fallo del proveedor.
- [ ] Existe un plan de salida y migración de datos para evitar el bloqueo.
- [ ] Se entienden los costos, los términos de renovación, y las cláusulas de cambio de precio.
- [ ] El proveedor se agrega al registro de riesgo con una fecha de revisión.

## Lista de verificación de preparación de cumplimiento gubernamental (estilo ATO / FedRAMP)

Para sistemas que requieren autorización formal para operar.

- [ ] El límite del sistema y los flujos de datos están definidos y diagramados.
- [ ] Los datos se categorizan por nivel de impacto y sensibilidad.
- [ ] La línea base de control aplicable se selecciona y ajusta.
- [ ] Un plan de seguridad del sistema documenta cómo se implementa cada control.
- [ ] Los controles se implementan, evidencian, y mapean al plan.
- [ ] El monitoreo continuo y el escaneo de vulnerabilidades están operativos.
- [ ] Un plan de acción e hitos rastrea los hallazgos abiertos hacia la remediación.
- [ ] El control de acceso, el registro de auditoría, y la gestión de identidad cumplen los requisitos.
- [ ] El cifrado usa algoritmos aprobados y módulos validados.
- [ ] Un plan de respuesta a incidentes está documentado y probado.
- [ ] Un plan de contingencia y recuperación ante desastres está documentado y probado.
- [ ] Se completa una evaluación o auditoría independiente de los controles.
- [ ] El funcionario autorizante tiene la evaluación de riesgo necesaria para otorgar la autorización.
- [ ] Los disparadores de reautorización y la cadencia de autorización continua están definidos.
