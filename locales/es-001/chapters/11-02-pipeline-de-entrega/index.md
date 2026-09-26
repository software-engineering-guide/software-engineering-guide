# 11.2 El pipeline de entrega

## Presentación y motivación

El pipeline de entrega es el flujo de trabajo que convierte una idea validada en software funcionando en manos de los usuarios (de manera confiable, repetible, y medible) y luego alimenta los datos de resultado resultantes de vuelta al descubrimiento (capítulo 11.1). Es el camino industrializado desde un commit de código hasta un cambio en producción hasta un efecto medido en los usuarios y el negocio. Donde el descubrimiento responde *qué y por qué*, la entrega responde *cómo lo enviamos de manera segura, qué tan rápido, y si realmente funcionó*.

Este capítulo es deliberadamente integrador. La mecánica vive en detalle en otros lugares: la estrategia de pruebas (capítulo 2.4), la automatización de pruebas y procesos (capítulo 8.5), la [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) y la [entrega continua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) y las estrategias de despliegue (capítulo 8.1), la infraestructura como código (capítulo 8.2), la fiabilidad y los SLO (objetivos de nivel de servicio, capítulo 9.1), y la experimentación (capítulo 7.4). Aquí los ensamblamos en un solo pipeline de extremo a extremo y, de manera crucial, adjuntamos las **métricas de resultado** que te dicen si toda la máquina está produciendo valor en lugar de simplemente producir lanzamientos.

Para equipos grandes, el pipeline de entrega es la inversión de mayor apalancamiento en efectividad de ingeniería. Una década de investigación, más prominentemente el programa DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) resumido en *Accelerate*, muestra que los equipos con pipelines de entrega rápidos, automatizados, y de bajo riesgo superan en rendimiento *y* en estabilidad *y* en resultados organizacionales. La creencia histórica de que la velocidad y la seguridad se contraponen es empíricamente falsa. En las empresas, un pipeline fuerte es lo que permite que cientos de ingenieros se integren sin colapsar en caos de fusión y teatro de lanzamiento manual. En el gobierno, reemplaza lanzamientos trimestrales de alta ceremonia, todo-o-nada, de "gran explosión" (históricamente una causa principal de programas fallidos) con cambios pequeños, reversibles, y auditables que satisfacen las obligaciones de control de cambios *a través* de la automatización en lugar de a pesar de ella.

## Principios fundamentales

- **Automatiza todo lo repetible.** Los pasos manuales son lentos, propensos a errores, y no auditables.
- **Lotes pequeños, lanzamientos frecuentes.** Los cambios pequeños son más fáciles de revisar, probar, enviar, y revertir.
- **Construye la calidad dentro.** Las pruebas y puertas rápidas y automatizadas capturan defectos antes de producción, no después.
- **Separa el despliegue de la liberación.** Envía código a oscuras; activa las características con banderas cuando estén listas.
- **Haz que todo sea reversible.** El retroceso rápido y la exposición progresiva convierten el despliegue de una apuesta en un experimento.
- **El pipeline es la fuente de verdad.** Si no está en el control de versiones y el pipeline, no sucedió.
- **Mide resultados, no solo entregas.** El conteo de despliegues es una entrega; una métrica movida es un resultado.

## Recomendaciones

### Automatiza la suite de pruebas y aplícala como puerta

La automatización de pruebas es la base que hace segura a la entrega rápida. Implementa un portafolio de pruebas equilibrado y mayormente automatizado (capítulo 2.4): muchas pruebas unitarias rápidas, menos pruebas de integración y de contrato, un pequeño número de pruebas de extremo a extremo, más verificaciones automatizadas de seguridad (SAST/DAST/SCA: análisis estático, dinámico, y de composición de software), accesibilidad, y rendimiento. Ejecútalas como **puertas de calidad** en el pipeline para que ningún cambio llegue a producción sin pasarlas. Mantén la suite rápida y confiable: una suite lenta o inestable se evade, lo que derrota su propósito (capítulo 8.5). Apunta a que el pipeline dé a un desarrollador una señal clara de aprobado/reprobado dentro de minutos de un commit.

### Practica la integración continua y la entrega continua

**Integración continua (CI):** cada desarrollador fusiona cambios pequeños en la línea principal frecuentemente (idealmente diariamente), y cada fusión activa una construcción y ejecución de pruebas automatizada. Esto se apoya mejor en el desarrollo basado en tronco (capítulo 2.6), que mantiene las ramas de vida corta y la integración continua. **Entrega continua (CD):** cada cambio que pasa el pipeline está *siempre en un estado liberable* y puede desplegarse a demanda. El **despliegue continuo** va un paso más allá: cada cambio que pasa se despliega a producción automáticamente. Elige el nivel de automatización apropiado a tu perfil de riesgo; los entornos regulados pueden detenerse en la entrega continua con un paso de promoción controlado (capítulo 8.1), pero aun así deberían automatizar todo hasta esa puerta.

### Despliega de manera segura con estrategias progresivas

Desacopla el **despliegue** (código ejecutándose en producción) de la **liberación** (usuarios experimentando el cambio), y expón los cambios gradualmente:

- Las **[banderas de características](https://en.wikipedia.org/wiki/Feature_toggle)** te permiten desplegar código a oscuras y liberarlo a segmentos a demanda, y revertir instantáneamente activando la bandera.
- Las **liberaciones canario** enrutan un pequeño porcentaje del tráfico a la nueva versión, vigilando las métricas de salud antes de ampliar.
- Los **despliegues azul-verde** mantienen dos entornos y cambian el tráfico atómicamente, con retroceso instantáneo.
- Los **despliegues rodantes** reemplazan instancias incrementalmente.
- La **entrega progresiva** combina banderas, canarios, y análisis automatizado para promover o revertir con base en señales en vivo.

Empareja cada estrategia con retroceso automatizado activado por violaciones de SLO o consumo de presupuesto de error (la tasa a la que los fallos consumen el presupuesto de falta de fiabilidad permitido; capítulo 9.1). Ver el capítulo 8.1 para la mecánica.

### Instrumenta métricas de resultado: mide el pipeline y el impacto

Un pipeline de entrega que envía rápido pero envía lo incorrecto es desperdicio rápido. Mide en tres niveles:

1. **Flujo de entrega, las cuatro métricas DORA:**
   - *Frecuencia de despliegue:* qué tan a menudo liberas a producción.
   - *[Tiempo de entrega](https://en.wikipedia.org/wiki/Lead_time) para cambios:* del commit a la producción.
   - *Tasa de fallo de cambio:* porcentaje de liberaciones que causan una degradación.
   - *Tiempo de recuperación de despliegue fallido:* qué tan rápido restauras el servicio (anteriormente MTTR, tiempo medio de recuperación).
   Los intérpretes de élite despliegan a demanda, con tiempos de entrega bajo una hora, tasas de fallo bajas, y recuperación en minutos. Agrega **métricas de flujo** del pensamiento de flujo de valor (tiempo de ciclo, [trabajo en progreso](https://en.wikipedia.org/wiki/Work_in_process), eficiencia de flujo) para ver dónde espera el trabajo.

2. **Fiabilidad y calidad, SLI y SLO** (indicadores y objetivos de nivel de servicio; capítulo 9.1): ¿el servicio está cumpliendo sus objetivos de fiabilidad y compromisos de atributos de calidad (capítulo 11.1) después de cada cambio?

3. **Resultados de negocio y de usuario** (capítulos 7.3-7.4): ¿el cambio movió los resultados clave y KPI que el descubrimiento definió? Aquí es donde la liberación se encuentra con el experimento: envía detrás de una bandera, mide contra un control, y conserva solo lo que gana.

### Cierra el ciclo de vuelta al descubrimiento

El acto final del pipeline de entrega no es el despliegue; es la **evidencia**. Las métricas de resultado (si la activación subió, si el tiempo de pago bajó, si los tickets de soporte disminuyeron) fluyen de vuelta al pipeline de descubrimiento (capítulo 11.1) como la base para la siguiente ronda de apuestas. Cuando el descubrimiento y la entrega se unen mediante este ciclo de retroalimentación, la organización se convierte en un sistema de aprendizaje: las hipótesis se envían, se miden, y se escalan o revierten, continuamente.

### Haz que la entrega sea auditable y gobernada

En entornos empresariales y gubernamentales, trata el pipeline en sí como un control de cumplimiento. Como cada cambio fluye a través del control de versiones y un pipeline automatizado, obtienes un rastro de auditoría inmutable "gratis": quién cambió qué, qué pruebas y aprobaciones lo condicionaron, y cuándo se desplegó. Codifica la separación de funciones, las revisiones requeridas, y las verificaciones de política como **política como código** (reglas de gobernanza expresadas en una forma controlada por versión, aplicable por máquina; capítulo 8.2) para que el control de cambios se aplique automáticamente y se evidencie continuamente (capítulos 4.6 y 10.2), en lugar de reconstruirse manualmente antes de una auditoría.

## Ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| **Despliegue continuo (automático a producción)** | Retroalimentación más rápida; lotes más pequeños; menos esfuerzo manual | Exige pruebas maduras, monitoreo, retroceso; difícil en puertas reguladas |
| **Entrega continua con promoción manual** | Punto de control humano/de cumplimiento; amigable con auditorías | Más lenta; riesgo de acumular cambios en la puerta |
| **Banderas de características** | Separación de despliegue/liberación; retroceso instantáneo; segmentación | Deuda de banderas y complejidad combinatoria si no se podan |
| **Canario / entrega progresiva** | Limita el radio de explosión; promoción guiada por datos | Necesita observabilidad fuerte y gestión de tráfico |
| **Azul-verde** | Cambio y retroceso instantáneos | Duplica el costo del entorno; las migraciones con estado/datos son delicadas |
| **Proceso de lanzamiento manual pesado** | Se siente controlado; familiar para los auditores | Lento, propenso a errores, no reproducible, mal auditado en la práctica |

La creencia histórica del intercambio, *ve más rápido y romperás más*, es la clave a retirar. La evidencia muestra que las prácticas que aumentan la velocidad (automatización, lotes pequeños, pruebas rápidas, reversibilidad) son las *mismas* prácticas que aumentan la estabilidad. Los intercambios reales tienen que ver con la **inversión y la granularidad de control**, no con velocidad frente a seguridad.

## Preguntas para discutir con tu equipo

1. **¿Cuál es tu perfil de riesgo real, y justifica detenerte en la entrega continua en lugar de ir hacia el despliegue continuo?** Elegir el nivel de automatización es una decisión real, no un predeterminado. El despliegue continuo da la retroalimentación más rápida y los lotes más pequeños, sin embargo exige pruebas maduras, observabilidad fuerte, y retroceso instantáneo, así que un contexto regulado puede racionalmente detenerse en una puerta de promoción controlada. Trae evidencia: tu tasa de fallo de cambio, tu tiempo de recuperación, y la confiabilidad de tu suite de pruebas, porque esos te dicen si el automático a producción es seguro hoy. Para la empresa y el gobierno, automatiza todo hasta la puerta y haz de la puerta misma política como código, para que el paso humano agregue control sin agregar esfuerzo manual. Si aún no puedes confiar en que el pipeline capture un mal cambio, invierte en puertas y observabilidad antes de accionar el interruptor.

2. **¿Puede tu pipeline producir la evidencia de auditoría que un regulador pediría, sin que nadie la reconstruya a mano?** Trata el pipeline en sí como un control de cumplimiento. Cada cambio debería llevar un rastro inmutable de quién cambió qué, qué pruebas y aprobaciones lo condicionaron, y cuándo se desplegó, generado automáticamente. En la empresa y el gobierno, codifica la separación de funciones y las revisiones requeridas como política como código para que el control de cambios se aplique y se evidencie continuamente en lugar de ensamblarse en pánico antes de una auditoría. La señal a traer: elige un cambio de producción reciente e intenta producir su rastro completo de aprobación y pruebas en cinco minutos. Si no puedes, estás pagando por preparación manual de auditoría y cargando riesgo que la automatización eliminaría.

3. **Cuando un lanzamiento empieza a degradarse en producción, ¿qué activa un retroceso, y es automático?** La reversibilidad es lo que hace que la velocidad sea racional en lugar de imprudente, así que el disparador de retroceso merece diseño explícito. Decide si una violación de SLO o el consumo de presupuesto de error retrocede automáticamente, o si un humano debe notar, decidir, y actuar mientras los usuarios sufren. Trae tus últimos incidentes y mide la brecha entre "la métrica empezó a degradarse" y "el cambio se revirtió"; esa brecha es tu radio de explosión real. Para equipos grandes que envían muchas veces al día, el retroceso manual no escala, y las banderas más el análisis canario te permiten promover o revertir con señales en vivo. Si tu respuesta es "alguien recibe una alerta y lo resuelve", estás tratando cada despliegue como una apuesta irreversible.

4. **Cuando envías una característica, ¿mides si realmente movió la métrica que se suponía que debía mover, o cuentas el despliegue y sigues adelante?** Un pipeline que envía rápido pero nunca verifica el impacto es desperdicio rápido, y la brecha entre entrega y resultado es donde la mayor parte de la inversión en entrega se filtra silenciosamente. Para una organización grande, cientos de lanzamientos a la semana hacen tentador tratar la frecuencia de despliegue como el marcador, sin embargo la frecuencia mide movimiento, no valor; la atracción en competencia es que la medición de resultados cuesta instrumentación, un grupo de control, y la disciplina de dejar apagada una característica perdedora. Trae el puñado de características enviadas recientemente y, para cada una, la métrica objetivo que definió el descubrimiento, la medición antes-y-después, y qué hiciste cuando no se movió. En portafolios empresariales y gubernamentales, nombra quién revisa los resultados en una cadencia fija y quién tiene la autoridad para retirar una característica que se envió pero nunca dio resultado, porque un cambio que nadie es responsable de medir es uno que nadie apagará jamás. La prueba honesta es si puedes señalar una característica que revertiste *porque* la evidencia dijo que perdió.

5. **¿Cuánto tiempo toma tu pipeline en darle a un desarrollador una señal de aprobado/reprobado, y confían lo suficiente en las pruebas como para no rodearlas?** La velocidad de retroalimentación y la confianza en la suite son lo que hace que las puertas de calidad realmente condicionen en lugar de ser evadidas, y ambas se erosionan silenciosamente conforme crece una base de código. Para un equipo grande, una suite que toma cuarenta minutos o falla intermitentemente una de cada diez ejecuciones entrena a cientos de ingenieros a fusionar en rojo, deshabilitar verificaciones, o reejecutar hasta obtener verde, lo que silenciosamente elimina la seguridad que justificó ir rápido en primer lugar; las consideraciones en competencia son la cobertura y el realismo de las pruebas frente a la velocidad y estabilidad de la retroalimentación, y presionar cualquiera demasiado fuerte socava a la otra. Trae la duración actual del pipeline, la tasa de reejecución por inestabilidad, y cualquier evidencia de puertas siendo saltadas o marcadas como no bloqueantes. Para contextos empresariales y gubernamentales donde esas puertas también llevan verificaciones SAST, DAST, y de política que satisfacen el cumplimiento, una puerta evadida es tanto un riesgo de calidad como una brecha de auditoría, así que mide si la puerta es genuinamente obligatoria o meramente consultiva. Si los desarrolladores no pueden articular por qué confían en una construcción verde, la puerta es decoración.

6. **¿Quién posee mantener consistente el camino de entrega a través de los equipos y podar la deuda de banderas de características, o cada equipo está reinventando su propio pipeline?** Conforme crece una organización, la entrega o converge en un camino pavimentado compartido o se fragmenta en docenas de pipelines a medida con puertas incompatibles, rastros de auditoría desiguales, y banderas que sobreviven a su propósito. La tensión es real: un camino pavimentado central te da consistencia, gobernanza, y economías de escala, pero un mandato que ignora las restricciones genuinas de un equipo cría pipelines fantasma y resentimiento, así que el camino pavimentado tiene que ser lo suficientemente bueno para que los equipos se unan voluntariamente. Trae un inventario de cuántos pipelines distintos existen hoy, cómo se gobierna la creación y eliminación de banderas, y cuánto varían el tiempo de entrega y la calidad de auditoría entre tus mejores y peores equipos. En entornos empresariales y gubernamentales, agrega el ángulo de cumplimiento: los pipelines inconsistentes significan que la separación de funciones y la evidencia de control de cambios se prueban de manera diferente (o no se prueban en absoluto) en cada equipo, y un solo camino pavimentado auditado con política como código convierte eso de una apuesta por equipo en una garantía organizacional. Si nadie posee eliminar las banderas obsoletas, la deuda combinatoria eventualmente hará el sistema imposible de probar.

## Perspectiva sectorial

**Startup.** La velocidad es supervivencia, así que compra tu pipeline en lugar de construirlo: conecta el desarrollo basado en tronco a un ejecutor de CI alojado, condiciona cada fusión a pruebas unitarias rápidas y un escaneo de seguridad, y despliega directo a producción detrás de un servicio de banderas de características alojado. Sáltate el equipo de plataforma y las herramientas a medida; tu recurso más escaso es la atención de ingeniería, y un pipeline que un solo generalista puede mantener vence a uno elaborado que nadie tiene tiempo de arreglar. Rastrea las cuatro métricas DORA en un tablero simple desde el primer día para que aprendas tu flujo temprano y puedas mostrar a los inversionistas que envías diariamente sin romper cosas.

**Pequeña empresa.** Sin un ingeniero de lanzamiento dedicado y un presupuesto ajustado, trata la entrega como algo que ensamblas a partir de servicios gestionados en lugar de un sistema que dotas de personal: CI/CD gestionado, una herramienta de banderas alojada, y una plataforma de nube que maneja el despliegue y el retroceso por ti. Resiste construir infraestructura de pipeline personalizada que no puedes darte el lujo de mantener, y mantén el camino lo suficientemente simple para que quien esté de guardia pueda entenderlo bajo presión. Prefiere herramientas que hagan disponible la entrega progresiva y el retroceso de un clic desde el principio, porque esas son las capacidades que convierten un despliegue de viernes aterrador en uno rutinario.

**Empresa.** El problema central es la consistencia a través de muchos equipos: un pipeline de camino pavimentado soportado con puertas automatizadas de prueba, seguridad, y política como código a las que los equipos se unen voluntariamente en lugar de reinventar. Estandariza la interfaz para que las métricas DORA y SLO sean comparables en la organización, presupuesta explícitamente la capacidad de plataforma que mantiene el camino pavimentado, y gestiona las banderas de características y las regresiones de tiempo de entrega como activos gobernados en lugar de folclore por equipo. La gobernanza y la auditoría viajan automáticamente cuando cada cambio fluye a través del mismo camino versionado y condicionado.

**Gobierno.** Las reglas de adquisición, la transparencia, y la responsabilidad pública dan forma al pipeline, así que favorece la entrega continua que se detiene en una puerta de promoción automatizada que aplica la separación de funciones y las aprobaciones requeridas como política como código. Haz del pipeline mismo el control de cumplimiento: cada cambio lleva un rastro de auditoría inmutable que satisface las obligaciones de control de cambios y autoridad para operar sin reconstrucción manual. Reemplaza los lanzamientos de "gran explosión" de alta ceremonia con cambios pequeños, reversibles, y desacoplados para que puedas pilotear un flujo orientado al público en una región, medir las tasas de error y finalización, y retroceder en minutos si se degrada.

## Ejemplos

**Startup.** Un equipo de tres ingenieros que envía una herramienta de analítica B2B empieza desplegando a mano los viernes por la tarde, lo que significa un lanzamiento aterrador una vez a la semana y un fin de semana de temor. En una tarde conectan el desarrollo basado en tronco con un pipeline de GitHub Actions: pruebas unitarias rápidas, un linter, y un escaneo de seguridad condicionan cada fusión, y una construcción aprobada se despliega directo a producción detrás de banderas de LaunchDarkly. La frecuencia de despliegue salta de semanal a varias veces al día, y porque cada característica nueva se envía a oscuras y se activa para un cliente amigable primero, una exportación CSV rota se captura y se apaga en minutos en lugar de convertirse en un incidente de lunes. Rastrean las cuatro métricas DORA en un tablero simple para poder mostrar a los inversionistas que el equipo envía diariamente sin romper cosas.

**Empresa.** Una aseguradora global consolida 40 equipos en un pipeline de camino pavimentado compartido (una cadena de herramientas predeterminada, soportada y preintegrada a la que los equipos se unen; capítulo 8.4): desarrollo basado en tronco, puertas automatizadas de prueba y seguridad, y despliegue canario con retroceso automatizado ante violación de SLO. La frecuencia de despliegue sube de mensual a muchas veces por día; el tiempo de entrega cae de seis semanas a menos de un día; la tasa de fallo de cambio baja porque los lotes son pequeños y las puertas están automatizadas. Crucialmente, las características de producto ahora se envían detrás de banderas y se miden contra controles, así que la aseguradora puede atar cada lanzamiento a su efecto sobre la tasa de finalización de cotizaciones, conectando el pipeline de entrega directamente con los resultados clave del lado de descubrimiento del capítulo 11.1.

**Gobierno.** Una agencia pública reemplaza los lanzamientos trimestrales de "gran explosión" (cada uno un fin de semana de pasos manuales y una fuente frecuente de interrupciones) con un pipeline de entrega continua que se detiene en una puerta de promoción automatizada que aplica la separación de funciones y las aprobaciones requeridas como política como código. Cada cambio lleva un rastro de auditoría inmutable que satisface las obligaciones de control de cambios y ATO (autoridad para operar) de la agencia (capítulo 4.6). Los lanzamientos se vuelven pequeños, frecuentes, y reversibles; el tiempo de recuperación cae de días a minutos; y como el despliegue está desacoplado de la liberación mediante banderas, la agencia puede pilotear un nuevo flujo de beneficios con una región antes del despliegue nacional, midiendo las tasas de finalización y error antes de comprometerse.

## Caso de negocio: motivaciones, ROI y TCO

El retorno de la inversión en el pipeline de entrega está entre los mejor evidenciados en el software. Un tiempo de entrega más rápido y una mayor frecuencia de despliegue significan que las ideas llegan a los usuarios (y empiezan a devolver valor, o a corregirse) antes. Una tasa de fallo de cambio más baja y una recuperación más rápida significan menos tiempo de inactividad, menos apagar incendios, y menos daño reputacional y regulatorio. La investigación DORA vincula estas capacidades con un rendimiento comercial y organizacional superior, no meramente comodidad de ingeniería. El efecto compuesto importa: un equipo que envía y aprende diariamente itera de 20 a 30 veces más a menudo que uno que envía mensualmente, y esa tasa de aprendizaje es decisiva a lo largo de la vida de un producto.

En el [costo total de propiedad](https://en.wikipedia.org/wiki/Total_cost_of_ownership), la automatización desplaza el costo del esfuerzo manual perpetuo a una inversión de pipeline única más mantenimiento. Un lanzamiento manual consume horas de ingeniero sénior cada vez, escala mal, y produce evidencia de auditoría débil. Un pipeline automatizado amortiza ese costo, y luego lo *reduce* conforme crece el volumen, todo mientras produce evidencia más fuerte continuamente. La reversibilidad reduce el costo del fallo mismo: cuando cualquier cambio puede revertirse en segundos, el costo esperado de un mal despliegue colapsa, que es lo que hace que ir rápido sea racional en lugar de imprudente.

Para hacer el caso al liderazgo, mide la línea base actual con las cuatro métricas DORA y las horas manuales gastadas por lanzamiento, luego cuantifica el esfuerzo eliminado y el tiempo de inactividad evitado. El costo de adopción es real, a saber la ingeniería del pipeline, la inversión en pruebas, y una capacidad de plataforma/camino pavimentado (capítulo 8.4), pero el costo de *no* invertir se paga continuamente en retroalimentación lenta, riesgo del día de lanzamiento, agotamiento del ingeniero, y dolor de auditoría. El argumento decisivo es el vínculo de descubrimiento: un pipeline de entrega rápido y medido es lo que hace que las apuestas validadas del pipeline de descubrimiento sean realmente comprobables en producción.

## Antipatrones y trampas

- **Medir la entrega, no el resultado:** celebrar los conteos de despliegue mientras las métricas objetivo permanecen planas.
- **Suites de pruebas lentas o inestables:** puertas que los desarrolladores aprenden a ignorar o evadir.
- **Lanzamientos de gran explosión, infrecuentes:** lotes grandes que son riesgosos, difíciles de depurar, y difíciles de revertir.
- **Despliegue y liberación confundidos:** sin banderas de características, así que cada despliegue es una apuesta irreversible frente al usuario.
- **Teatro de lanzamiento manual:** listas de verificación ejecutadas a mano que son lentas, inconsistentes, y mal auditadas.
- **Pipeline automatizado, sin observabilidad:** enviar rápido sin capacidad de detectar o diagnosticar regresiones.
- **Deuda de banderas de características:** banderas nunca eliminadas, acumulándose en complejidad combinatoria imposible de probar.
- **Manipular las métricas DORA:** dividir despliegues para inflar la frecuencia en lugar de mejorar el flujo.
- **Sin ciclo de retroalimentación:** los resultados nunca se miden, así que la entrega nunca informa el siguiente ciclo de descubrimiento.

## Modelo de madurez

- **Nivel 1 (Iniciar):** Lanzamientos manuales, infrecuentes, de alta ceremonia; las pruebas son mayormente manuales y se ejecutan a mano; el éxito se mide como "se envió"; los retrocesos son dolorosos e improvisados; ninguna idea compartida de cómo debería funcionar la entrega.
- **Nivel 2 (Desarrollar):** Algunos equipos levantan CI con construcciones automatizadas y unas cuantas pruebas; los lanzamientos están programados; existe monitoreo básico; las prácticas varían de equipo a equipo y las métricas DORA aún no se rastrean, así que la entrega es mejor en bolsas pero inconsistente en la organización.
- **Nivel 3 (Estandarizar):** Un pipeline de camino pavimentado documentado se aplica en toda la organización: entrega continua con puertas automatizadas de prueba y seguridad, despliegue progresivo con retroceso, y separación de funciones aplicada como política como código. El pipeline provee un rastro de auditoría inmutable, y cada equipo sigue el mismo camino versionado en lugar de uno a medida.
- **Nivel 4 (Gestionar):** El pipeline se mide y controla contra líneas base. Las cuatro métricas DORA (frecuencia de despliegue, tiempo de entrega, tasa de fallo de cambio, tiempo de recuperación), el cumplimiento de SLO, el consumo de presupuesto de error, y las métricas de flujo como el tiempo de ciclo y el trabajo en progreso se rastrean contra objetivos, y las puertas y retrocesos se disparan con umbrales medidos en lugar de juicio. La deuda de banderas, las tasas de pruebas inestables, y las regresiones de tiempo de entrega se monitorean, y cada decisión de continuar o no se toma con evidencia.
- **Nivel 5 (Orquestar):** La entrega se mejora continuamente e integra con la planificación de descubrimiento y riesgo. El despliegue continuo funciona donde es apropiado con entrega progresiva y retroceso automatizado; las características se envían como experimentos medidos cuyas métricas de resultado retroalimentan la siguiente ronda de apuestas; el rendimiento DORA de élite se sostiene entre equipos mediante el camino pavimentado; y la organización reajusta adaptativamente las puertas, umbrales, y capacidad conforme cambian la carga, el riesgo, y la mezcla de producto.

## Ideas para el debate

1. ¿Cuáles son tus cuatro métricas DORA actuales, y dónde está el mayor cuello de botella en tu flujo de commit a producción?
2. ¿Puedes separar el despliegue de la liberación hoy? Si no, ¿qué cambiarían las banderas de características sobre tu riesgo?
3. ¿Cuánto tiempo toma tu suite de pruebas, y confían los desarrolladores lo suficiente en ella como para no evadirla?
4. Cuando enviaste tu última característica, ¿mediste si movió la métrica que se suponía que debía mover?
5. En un contexto regulado, ¿tu proceso de control de cambios ralentiza la entrega *o* se aplica automáticamente a través del pipeline?
6. ¿Qué banderas de características en tu base de código deberían haberse eliminado hace meses?

## Puntos clave

- El pipeline de entrega convierte ideas validadas en software funcionando y medido, y retroalimenta los resultados al descubrimiento (capítulo 11.1).
- Automatiza todo el camino: **puertas de prueba** rápidas, **CI/CD**, e **infraestructura como código**, con el pipeline como fuente de verdad.
- **Separa el despliegue de la liberación** y usa estrategias progresivas (banderas, canario, azul-verde) con retroceso automatizado.
- Mide en tres niveles: métricas **DORA/flujo**, **fiabilidad/SLO**, y **resultados de negocio/usuario**.
- La velocidad y la estabilidad son **complementos**, no intercambios: las prácticas que entregan una entregan la otra.
- El pipeline también es un **control de cumplimiento**: la automatización produce un rastro de auditoría inmutable y continuo.
- El ROI es rápido, bien evidenciado (DORA), y compuesto; el costo principal de no invertir se paga continuamente.

## Referencias y lecturas adicionales

- *Accelerate: The Science of Lean Software and DevOps*, de Nicole Forsgren, Jez Humble, Gene Kim (las métricas DORA y la evidencia).
- *Continuous Delivery*, de Jez Humble y David Farley (el texto fundacional).
- *The DevOps Handbook*, de Kim, Humble, Debois, Willis.
- *The Phoenix Project*, de Gene Kim, Kevin Behr, George Spafford (narrativa sobre el flujo).
- *Site Reliability Engineering*, de Beyer, Jones, Petoff, Murphy, eds. (SLI/SLO, presupuestos de error).
- *Team Topologies*, de Matthew Skelton y Manuel Pais (caminos pavimentados y diseño de equipos de entrega).
- *Feature Flags / progressive delivery*, escritos de Pete Hodgson y las comunidades de LaunchDarkly/Split.
- Google DORA, informes *Accelerate State of DevOps* (anuales).
- Kim, Gene, *The Unicorn Project* (vista de experiencia del desarrollador sobre el flujo).
- Reinertsen, Donald, *The Principles of Product Development Flow* (tamaño de lote, colas, economía de flujo).
