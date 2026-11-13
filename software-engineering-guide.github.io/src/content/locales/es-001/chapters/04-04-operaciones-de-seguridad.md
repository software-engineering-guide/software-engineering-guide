# 4.4 Operaciones de seguridad

## Presentación y justificación

La prevención es necesaria, pero nunca suficiente. Adversarios decididos, vulnerabilidades inéditas y el simple error humano garantizan que algunas amenazas se colarán entre las defensas. Las operaciones de seguridad son la disciplina de encontrarlas a tiempo, responder con eficacia y alimentar con lo aprendido unas defensas cada vez más sólidas. Son la diferencia entre un incidente contenido en cuestión de minutos y otro que se pudre durante meses hasta que alguien por fin lo detecta.

En una organización grande, las operaciones de seguridad tienen que funcionar a escala y a velocidad. Miles de servicios generan un caudal inabarcable de registros. Cada semana se divulgan cientos de nuevas vulnerabilidades. Las desplegadas no cesan. Una operación manual, artesanal, no puede seguir el ritmo. La respuesta consiste en integrar la seguridad en el pipeline de entrega ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), automatizar la detección y la respuesta y forjar la musculatura necesaria para gestionar los incidentes con serenidad cuando lleguen. En el ámbito gubernamental, las operaciones de seguridad asumen además obligaciones legales: plazos mandatorios de notificación de incidentes, divulgación coordinada de vulnerabilidades y un rigor forense capaz de resistir el escrutinio judicial.

Este capítulo abarca la integración de la seguridad en el pipeline, la gestión de vulnerabilidades y la aplicación de parches, la respuesta a incidentes y la forense digital, la ejecución de la detección a través de [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) y SOAR, y la validación de las defensas mediante equipo rojo, equipo púrpura y [pruebas de penetración](https://en.wikipedia.org/wiki/Penetration_test).

## Principios fundamentales

- **Automatizar lo rutinario.** Las máquinas asumen el escaneo, la correlación y la respuesta repetitiva para que los humanos se concentren en el juicio.
- **Integrar la seguridad en el pipeline.** Las pruebas y los controles deben vivir en [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (integración y entrega continuas), ofreciendo retroalimentación rápida allí donde los ingenieros ya trabajan.
- **Partir del supuesto de brecha y prepararse.** Ensayar la respuesta a incidentes antes de necesitarla: el incidente no es el momento de improvisar.
- **Medir y reducir el tiempo.** El tiempo medio de detección y el tiempo medio de respuesta son las métricas que verdaderamente importan.
- **Aprender sin culpar.** Cada incidente y cada casi-incidente se convierte en una lección que fortalece el sistema, no en una búsqueda de culpables.
- **Validar las defensas de forma adversarial.** Probar la seguridad como lo haría un atacante real y corregir lo que encuentre.
- **La ingeniería de detecciones es un producto.** Tratar las detecciones como código: versionado, probado y mejorado de forma continua.

## Recomendaciones

### Integrar DevSecOps en el pipeline

Integrar pruebas de seguridad automatizadas directamente en la integración y entrega continuas para que la retroalimentación llegue a los ingenieros en cuestión de minutos:

- **SAST** (Análisis Estático de Aplicaciones de Seguridad) examina el código fuente en busca de patrones vulnerables en el momento del envío.
- **DAST** (Análisis Dinámico de Aplicaciones de Seguridad) explora la aplicación en ejecución en busca de defectos explotables.
- **SCA** (Análisis de Composición de Software) identifica dependencias con vulnerabilidades conocidas.
- **Escaneo de IaC** (infraestructura como código) comprueba las configuraciones inseguras antes de su despliegue.
- **Escaneo de secretos** impide que las credenciales se filtren al repositorio.

Ajustar estos herramientas con rigor para controlar los falsos positivos. Un escáner que grite lobo se ignora. Establecer controles basados en el riesgo: bloquear ante hallazgos de alta severidad y alta confianza, y registrar los demás sin detener la entrega. Lo que se busca es una señal rápida y fiable, no una avalancha de ruido.

### Gestionar vulnerabilidades y parches de forma sistemática

Un flujo constante de vulnerabilidades exige un proceso sistemático y priorizado, no un nuevo pánico con cada titular.

- Mantener un inventario de activos preciso para saber qué componentes podrían verse afectados por cada vulnerabilidad.
- Priorizar la remediación según el riesgo real: combinar severidad, explotabilidad (¿se está explotando en el mundo real?), exposición y criticidad del activo, en lugar de parchear solo por puntuación en bruto.
- Definir y hacer cumplir **acuerdos de nivel de servicio de remediación** por nivel de severidad, y medir su cumplimiento.
- Automatizar la aplicación de parches siempre que sea seguro, especialmente en infraestructura y dependencias.
- Poner en marcha un programa de **divulgación coordinada de vulnerabilidades** con un canal de recepción claro y, cuando proceda, un programa de [recompensas por reportes de vulnerabilidades](https://en.wikipedia.org/wiki/Bug_bounty_program), para que los investigadores externos puedan notificar defectos de forma responsable en lugar de publicarlos sin control.

### Preparar y ejecutar la respuesta a incidentes

Cuando llega un incidente, un proceso ensayado vale más que cualquier herramienta.

- Mantener un **plan de respuesta a incidentes** con roles definidos (coordinador del incidente, responsable de comunicaciones, investigadores), niveles de severidad y vías de escalado.
- Establecer fases claras: **preparación, detección y análisis, contención, erradicación, recuperación y revisión posterior al incidente.**
- Preservar la evidencia adecuadamente para la **forense digital**: capturar registros, memoria e imágenes de disco con una cadena de custodia documentada, de modo que los hallazgos sean válidos ante un tribunal y el análisis sea riguroso.
- Planificar **las comunicaciones ante una brecha** con antelación: quién notifica a los clientes, a los reguladores y al público, en qué plazo, con la participación de legal y relaciones públicas. Los plazos regulatorios (con frecuencia 72 horas o menos) empiezan a correr desde el descubrimiento.
- Realizar **simulacros en mesa** con regularidad para que el equipo conozca el plan antes de una crisis real, y celebrar revisiones posteriores al incidente sin culpas que produzcan mejoras concretas.

### Operar la detección con SIEM y SOAR e ingenierizar las detecciones

Concentrar las señales de seguridad y actuar sobre ellas a escala.

- Utilizar un **SIEM** (Sistema de Gestión de Información y Eventos de Seguridad) para agregar y correlacionar registros y eventos de todo el entorno, haciendo patrones sospechosos visibles.
- Utilizar **SOAR** (Orquestación, Automatización y Respuesta de Seguridad) para automatizar la triage y los protocolos de respuesta: enriquecer alertas, aislar hosts, revocar credenciales y abrir casos sin depender de una persona para los pasos rutinarios.
- Practicar la **ingeniería de detecciones**: tratar las reglas de detección como código versionado y probado, alineadas a un marco como [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), medir sus tasas de verdaderos y falsos positivos y mejorar de forma continua la cobertura de las técnicas reales de los adversarios.
- Garantizar un registro exhaustivo e intocable en aplicaciones e infraestructura; no se puede detectar lo que no se registra.

### Validar las defensas con equipo rojo, equipo púrpura y pruebas de penetración

Probar las defensas como lo haría un atacante es la única forma de saber si funcionan de verdad.

- Las **pruebas de penetración** ofrecen una evaluación enfocada y puntual de sistemas concretos, a menudo para cumplir requisitos de cumplimiento normativo.
- El **equipo rojo** simula un adversario realista que persigue objetivos en todo el entorno, probando no solo la prevención sino también la detección y la respuesta.
- El **equipo púrpura** reúne a atacantes (rojo) y defensores (azul) de forma colaborativa, de modo que cada ataque simulado mejora de inmediato las detecciones y los controles, convirtiendo un ejercicio en una capacidad duradera.
- Retroalimentar todos los hallazgos en la ingeniería de detecciones, la remediación y la formación.

## Compromisos: ventajas e inconvenientes

| Decisión | Ventajas | Inconvenientes |
|---|---|---|
| Controles de bloqueo en el pipeline | Impiden que los problemas conocidos lleguen a producción | La fricción y los falsos positivos frustran a los equipos |
| Escaneo no bloqueante | Menor fricción, entrega rápida | Los problemas pueden llegar a producción; exige disciplina para subsanarlos |
| Centro de operaciones de seguridad propio | Contexto profundo, control total | Costoso, difícil de mantener en turnos 24/7 |
| Detección y respuesta gestionadas | Cobertura 24/7, expertise disponible | Menor contexto, dependencia del proveedor |
| Parcheo automatizado | Rápido, cierra brechas con prontitud | Riesgo de cambios que rompen funcionalidad |
| Pruebas del equipo rojo frecuentes | Validación realista, detecta brechas reales | Costoso, muy demandante en recursos |
| Programa de recompensas por reportes | Descubrimiento con participación externa, buena cobertura | Carga de triage, costes de pago, ruido |

La tensión central es la velocidad frente a la certeza y la cobertura frente al coste. Los controles de bloqueo y el parcheo automatizado maximizan la seguridad, pero añaden fricción y riesgo. Los enfoques no bloqueantes avanzan más rápido, pero dependen del seguimiento posterior. La detección ininterrumpida es imprescindible a gran escala, pero resulta costosa de construir internamente, lo que empuja a muchas organizaciones hacia modelos híbridos. El camino sostenible automatiza lo rutinario con alta confianza, reserva la atención humana para el juicio genuino y ajusta el equilibrio con resultados medidos, no con el miedo.

## Preguntas para debatir con el equipo

1. **¿Cuáles son los plazos de remediación por nivel de severidad y qué los hace cumplir de verdad?** Un flujo constante de vulnerabilidades exige un proceso sistemático y priorizado, no un pánico nuevo con cada titular, y los acuerdos de nivel de servicio por nivel de severidad son la manera de mantener el ritmo. Fijar los plazos (por ejemplo, críticas en días, altas en semanas) y, igual de importante, cómo se mide el cumplimiento y quién es responsable cuando un plazo se incumple. Priorizar según el riesgo real, combinando severidad con explotabilidad en el mundo real, exposición y criticidad del activo, en lugar de parchear solo por puntuación CVSS. Traer el registro actual de hallazgos abiertos ordenados por antigüedad y severidad, porque las críticas sin parchear que superan su plazo son la prueba que de verdad importa. Si un plazo no tiene cumplimiento ni responsable, es un deseo, y escanear sin remediar solo acumula deuda de auditoría y una falsa sensación de seguridad.

2. **Cuando llega un incidente a las dos de la madrugada, ¿quién es el coordinador del incidente y cuánto tarda en activarse el reloj regulatorio?** Un proceso ensayado vale más que cualquier herramienta, por lo que se necesitan roles nombrados (coordinador del incidente, responsable de comunicaciones, investigadores), niveles de severidad definidos y vías de escalado escritas antes de la crisis. Los plazos regulatorios suelen ser de 72 horas o menos y corren desde el descubrimiento, así que conviene decidir con antelación quién notifica a los clientes, a los reguladores y al público, y confirmar que los departamentos legal y de comunicación están en el bucle. La preservación de la evidencia forense con una cadena de custodia documentada debe hacerse antes de reconstruir un host comprometido, o se pierde la capacidad de entender o demostrar lo ocurrido. Traer la fecha del último simulacro en mesa, porque si fue hace mucho o nunca, el plan no está probado. Para equipos gubernamentales, los plazos de notificación legal hacen que esto sea innegociable, así que hay que ensayar la vía de notificación, no solo la respuesta técnica.

3. **¿Qué acciones de respuesta rutinarias se delegarán en el SOAR sin intervención humana?** La automatización multiplica la capacidad de un equipo reducido para cubrir un entorno extenso, y la métrica que importa es el tiempo medio de respuesta, que los protocolos automatizados pueden reducir de horas a minutos. Decidir qué acciones de alta confianza (aislar un host, revocar una credencial, abrir un caso) se confían a la ejecución automática y cuáles exigen juicio humano. El riesgo es que un falso positivo dispare una acción disruptiva, por lo que hay que vincular la automatización a la calidad de la detección y ajustar sin descanso, porque un sistema que grita lobo se desactiva. Traer el volumen actual de alertas y la tasa de falsos positivos, porque esas cifras indican qué protocolos es seguro automatizar hoy. Si cada paso de respuesta espera a una persona, no se dará abasto a escala, y el tiempo de permanencia del intruso, que es lo que define el coste de una brecha, seguirá alto.

4. **¿Qué hallazgos del pipeline bloquean una liberación, cuáles solo se registran y quién mantiene la tasa de falsos positivos lo suficientemente baja para que los ingenieros sigan confiando en el control?** Un escáner que grite lobo se ignora, y una vez que los ingenieros pierden la fe en un control, presionan para eliminarlo; el valor de DevSecOps depende de la calidad de la señal, no de la cobertura bruta. La tensión es real: bloquear demasiado poco y llega código vulnerable a producción; bloquear demasiado y se añade fricción, se frena la entrega y se consume buena voluntad. Traer las tasas de verdaderos y falsos positivos de cada escáner (SAST, DAST, SCA, IaC y escaneo de secretos), con qué frecuencia los equipos anulan o suprimen un control y la antigüedad de los hallazgos que solo se registran sin subsanar. Para una empresa o entidad gubernamental con cientos de pipelines, fijar la política de bloqueo frente a registro de forma central y ajustarla con datos, porque controles que varían arbitrariamente de un equipo a otro generan tanto lagunas de auditoría como la sensación de que la seguridad es caprichosa.

5. **¿Qué confianza hay de que las detecciones siguen cubriendo las técnicas que usaría un atacante real, y quién las mantiene como código probado y versionado?** Las detecciones se degradan en silencio a medida que el entorno y los adversarios evolucionan, de modo que un conjunto de reglas que parecía exhaustivo el año pasado puede perder cobertura mucho antes de que un incidente revele la laguna. Tratar las detecciones como código, versionado, probado y mapeado a un marco como MITRE ATT&CK, es lo que separa una práctica de ingeniería de un montón de alertas obsoletas, pero compite por el mismo tiempo escaso del analista que la triage en vivo. Traer el mapa de cobertura ATT&CK actual, la tasa medida de verdaderos y falsos positivos de las principales detecciones y los resultados del último ejercicio del equipo púrpura, ya que la prueba colaborativa entre rojo y azul es la forma más rápida de comprobar qué detecciones realmente se activan. En entornos empresariales y gubernamentales donde un marco puede ser obligatorio, vincular cada detección a un responsable nombrado y a una periodicidad de revisión, porque una cobertura que nadie mantiene es una cobertura de la que solo se descubre la pérdida tras la brecha.

6. **¿Se construye la detección y la respuesta internamente, se contrata un servicio gestionado o se combina ambos, y se ha calculado cuánto cuesta la cobertura verdadera 24/7?** El tiempo de permanencia del intruso define el coste de la brecha, así que las horas sin cobertura (noches, fines de semana, festivos) son justo cuando un intruso no detectado causa más daño, y sin embargo mantener un centro de operaciones de seguridad 24/7 en propia casa es caro y difícil de sostener. El intercambio es contexto y control frente a coste y velocidad de cobertura: un equipo interno conoce el entorno en profundidad pero es lento y costoso de construir, mientras que un proveedor gestionado aporta expertise inmediato las veinticuatro horas a cambio de un contexto más fino y una dependencia del proveedor. Traer las horas de cobertura actuales, el tiempo medio de detección y respuesta fuera de horario, el volumen de alertas y una valoración honesta de si se puede contratar y retener a los analistas que exige un centro propio. Para el sector gubernamental y las empresas reguladas, ponderar requisitos de residencia de datos, habilitaciones de personal y obligaciones de notificación legal que el proveedor debe poder cumplir, y verificar que el contrato preserve el rigor forense y la cadena de custodia que exigen los procedimientos judiciales.

## Perspectiva sectorial

**Startup.** La velocidad y la supervivencia van primero, por lo que conviene adquirir seguridad como un subproducto de las herramientas que ya se usan en lugar de plantear operaciones. Conectar escáneres gratuitos al pipeline de integración para bloquear fugas de secretos y dependencias con vulnerabilidades conocidas en el momento del envío, enviar registros a un servicio gestionado de bajo coste con un puñado de alertas de alto valor y redactar un plan de incidente de una página (a quién llamar, cómo rotar credenciales, hacer una captura del host comprometido antes de reconstruirlo) antes de necesitarlo. El recurso más escaso es la atención del equipo de ingeniería, así que hay que automatizar lo rutinario y resistir la tentación de montar un centro de operaciones de seguridad que no se pueda sostener.

**Pequeña empresa.** Sin especialista en seguridad dedicado y con un presupuesto ajustado, conviene apoyarse en servicios de detección y respuesta gestionados y en las funciones de seguridad ya incorporadas en las plataformas que se usan. Tratar el parcheo y el inventario de activos como los hábitos de mayor impacto: saber lo que se ejecuta, mantenerlo actualizado y aplicar un plazo de remediación sencillo por nivel de severidad. Preferir proveedores que asuman la vigilancia 24/7, la recepción de divulgación coordinada y la captura forense, y ensayar la única cosa que no se puede externalizar: decidir quién declara un incidente y quién habla con los clientes.

**Empresa.** El reto es la consistencia entre muchos equipos y cientos de pipelines: una política común de bloqueo frente a registro, acuerdos de nivel de servicio de remediación aplicados en toda la organización, una plataforma SIEM y SOAR con detecciones medidas y ejercicios del equipo púrpura que convierten cada simulación en nueva cobertura. Gestionar las operaciones de seguridad como una cartera con paneles para el tiempo medio de detección y respuesta, el cumplimiento de los plazos y la precisión de las detecciones, y decidir de forma deliberada dónde la profundidad interna supera a la escala gestionada. Presupuestar explícitamente el coste humano de la triage y el ajuste, porque la automatización desplaza el esfuerzo, no lo elimina.

**Sector público.** Las reglas de contratación, la transparencia y la rendición de cuentas pública configuran cada decisión. Los plazos legales de notificación de incidentes y la divulgación coordinada de vulnerabilidades son obligaciones, no opciones, así que hay que ensayar la vía de notificación al organismo nacional de ciberseguridad con la misma minuciosidad que la respuesta técnica y preservar la evidencia forense bajo una cadena de custodia que resista el escrutinio judicial. Preferir contratos que mantengan la lógica de detección y los datos portables, exigir que cualquier proveedor gestionado cumpla los requisitos de residencia y habilitación y esperar que las evaluaciones del equipo rojo y el escaneo continuo alimenten un proceso de autorización en el que el público pueda confiar.

## Ejemplos

**Startup.** Una startup sin centro de operaciones de seguridad conecta escáneres gratuitos a su pipeline de integración para que las fugas de secretos y las dependencias con vulnerabilidades conocidas se detecten en el momento del envío, bloqueando solo ante hallazgos de alta confianza para que los dos ingenieros no se ahoguen en ruido. Escriben un plan de incidente de una página antes de necesitarlo: a quién llamar, cómo rotar credenciales y hacer una captura del host comprometido antes de reconstruirlo para poder aprender lo que ocurrió. Envían los registros a un servicio gestionado de bajo coste y configuran unas pocas alertas sobre los eventos que realmente señalarían una brecha, de modo que un problema aparezca en horas en lugar de en los meses que tarda en detectarse por casualidad.

**Empresa.** Una empresa de software como servicio ejecuta SAST, SCA, escaneo de IaC y escaneo de secretos en cada pipeline, bloqueando solo ante hallazgos de alta severidad y alta confianza y registrando el resto en un panel con acuerdos de nivel de servicio de remediación. Un SIEM alimenta una plataforma SOAR que aísla hosts y revoca credenciales ante alertas de alta confianza, reduciendo el tiempo medio de respuesta de horas a minutos. Ejercicios trimestrales del equipo púrpura contra técnicas MITRE ATT&CK generan directamente nuevas reglas de detección, cerrando de forma constante las lagunas de cobertura.

**Sector público.** Una agencia federal opera un centro de operaciones de seguridad con notificación de incidentes obligatoria a una autoridad nacional de ciberseguridad dentro de los plazos legales. Gestiona un programa de divulgación coordinada de vulnerabilidades con un canal público de recepción, como exige la política, y preserva la evidencia forense bajo procedimientos estrictos de cadena de custodia aptos para procedimientos judiciales. Las evaluaciones anuales del equipo rojo y el escaneo continuo de vulnerabilidades alimentan la autorización continua de la agencia y sus acuerdos de nivel de servicio de remediación basados en el riesgo.

## Justificación empresarial: motivaciones, retorno de la inversión y coste total de propiedad

Casi todo el argumento a favor de las operaciones de seguridad se reduce al tiempo de permanencia del intruso: cuanto más tiempo pasa un atacante sin ser detectado, mayor es el coste de la brecha. Los estudios muestran de forma consistente que los incidentes contenidos con rapidez cuestan mucho menos que los que se arrastran durante meses. El coste total de propiedad incluye herramientas (SIEM, SOAR, escáneres), personal propio o servicios gestionados para detección y respuesta, y el tiempo necesario para construir y ensayar los procesos de incidente. Frente a eso se sitúa el coste de no invertir: una brecha descubierta tarde, que se extiende por los sistemas, que atrae multas regulatorias, notificaciones obligatorias, litigios y daño reputacional, todo agravado por el caos de una respuesta no ensayada.

El retorno de la inversión proviene de una detección y respuesta más rápidas, de la automatización que permite a un equipo reducido cubrir un entorno extenso, y de las mejoras preventivas que retroalimentan cada incidente y cada ejercicio. DevSecOps en particular devuelve la inversión al captar problemas en el pipeline, donde son baratos, en lugar de en producción, donde son caros y públicos. Al presentar el caso a la dirección, hay que cuantificar el tiempo medio de detección y respuesta actual, mostrar cómo se vinculan al tiempo de permanencia y al coste, y enmarcar la automatización como una multiplicación de fuerzas que evita aumentar el personal en proporción al entorno. En el sector público, conviene subrayar que las obligaciones legales de notificación y divulgación hacen que unas operaciones maduras no sean opcionales.

## Antipatrón y errores frecuentes

- **Fatiga de alertas.** Tantas alertas que los analistas dejan de prestar atención y pasan por alto la que importa.
- **Escaneo sin remediación.** Generar hallazgos que nadie corrige, creando una falsa sensación de seguridad y deuda de auditoría.
- **Sin plan de incidentes.** Improvisar durante una crisis, perdiendo minutos críticos y manipulando mal la evidencia.
- **Destruir evidencia.** Reconstruir un host comprometido antes de capturar la evidencia forense, perdiendo la capacidad de entender o demostrar lo ocurrido.
- **Cultura de la culpa en las revisiones.** Castigar a quienes responden para que el siguiente incidente se oculte o se maneje de forma defensiva.
- **Pruebas de penetración solo para el auditor.** Una prueba anual puntual para cumplir un requisito, con hallazgos ignorados hasta el año siguiente.
- **Controles de bloqueo con muchos falsos positivos.** Erosionar la confianza hasta que los ingenieros exijan eliminar los controles por completo.
- **Detecciones de una vez y olvidadas.** Reglas que se degradan a medida que el entorno y los adversarios evolucionan, perdiendo cobertura en silencio.

## Modelo de madurez

**Nivel 1: Iniciar.** Las operaciones de seguridad son improvisadas y reactivas. La prueba de seguridad es manual y rara, no existe registro centralizado ni SIEM. No hay plan de incidentes, así que la respuesta se improvisa en el momento. El parcheo ocurre solo cuando una titular lo obliga, y las defensas nunca se prueban de forma adversarial.

**Nivel 2: Desarrollar.** Aparecen prácticas básicas, pero de forma inconsistente entre equipos. Algunos pipelines ejecutan escáneres y otros no, y el registro centralizado existe solo a parches. Existe un plan de incidentes básico, pero rara vez se ensaya; el parcheo sigue plazos laxos, y una prueba de penetración anual satisface el cumplimiento sin cambiar gran cosa. La cobertura y el rigor dependen del equipo al que se pregunte.

**Nivel 3: Estandarizar.** Las prácticas están documentadas y se aplican en toda la organización. El escaneo de DevSecOps con controles basados en el riesgo se aplica de forma consistente, un SIEM correlaciona eventos y los primeros protocolos SOAR ya operan. La respuesta a incidentes se ensaya con simulacros en mesa y revisiones sin culpas, los acuerdos de nivel de servicio de remediación por nivel de severidad se aplican con responsables nombrados, y la divulgación coordinada de vulnerabilidades y las pruebas del equipo rojo son la norma, no la excepción.

**Nivel 4: Gestionar.** Las operaciones se miden y controlan frente a líneas base. El tiempo medio de detección y respuesta, el cumplimiento de los plazos por nivel de severidad, la cobertura del escaneo, las tasas de verdaderos y falsos positivos de las detecciones y el tiempo de permanencia del intruso se siguen en paneles y se revisan con periodicidad. Las detecciones llevan precisión y recall medidos, mapeados a MITRE ATT&CK; las decisiones de automatización se basan en datos de falsos positivos, no en esperanza, y una métrica que se desvía de su línea base activa una respuesta definida en lugar de pasar desapercibida.

**Nivel 5: Orquestar.** Las operaciones de seguridad se mejoran de forma continua, se integran en toda la organización y se adaptan. La ingeniería de detecciones, los ejercicios del equipo púrpura, la remediación y la revisión de incidentes alimentan un mismo ciclo que se adapta a las nuevas técnicas de los adversarios a medida que aparecen. Los protocolos automatizados gestionan lo rutinario en todo el entorno, de modo que los humanos se concentran en el juicio; la seguridad se planifica junto a la entrega y el riesgo, y cada incidente y cada ejercicio fortalecen el sistema de forma medible, mientras las métricas clave siguen a la baja.

## Ideas para la reflexión

1. ¿Qué hallazgos del pipeline deben bloquear una liberación y cuáles solo registrar?
2. ¿Construir un centro de operaciones de seguridad propio, contratar detección y respuesta gestionada o combinar ambos, y por qué?
3. ¿Cómo se impide que las reglas de detección se degraden a medida que el entorno evoluciona?
4. ¿Con qué intensidad debe automatizarse el parcheo ante el riesgo de cambios que rompan la funcionalidad?
5. ¿Cómo es una revisión posterior al incidente genuinamente sin culpas en nuestra cultura?
6. ¿Cómo se mide si los ejercicios del equipo rojo y púrpura están mejorando de verdad las defensas?

## Conclusiones clave

- La prevención falla antes o después; las operaciones existen para detectar y responder con rapidez.
- Integrar SAST, DAST, SCA, escaneo de IaC y escaneo de secretos en el pipeline con controles basados en el riesgo.
- Priorizar el parcheo según la explotabilidad real y la criticidad del activo, bajo acuerdos de nivel de servicio que se hacen cumplir.
- Ensayar la respuesta a incidentes, preservar la evidencia forense y planificar las comunicaciones ante una brecha con antelación.
- Utilizar SIEM y SOAR para correlacionar y automatizar; tratar las detecciones como código ingenierizado y probado.
- Validar las defensas con pruebas de penetración, equipo rojo y equipo púrpura colaborativo.
- El tiempo de permanencia del intruso define el coste de la brecha, por lo que el tiempo medio de detección y respuesta son las métricas que verdaderamente importan.

## Referencias y lecturas adicionales

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin y otros, *Logging and Log Management* / literatura sobre SIEM
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, directrices sobre *Divulgación Coordinada de Vulnerabilidades* y especificación *CVSS*

