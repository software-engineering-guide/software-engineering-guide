# 12.6 Hoja de ruta de adopción

Este apéndice es una guía práctica para desplegar las prácticas de este libro *incrementalmente*. La instrucción individual más importante de toda la guía, repetida en cada capítulo, es **adopta incrementalmente; no hagas gran explosión**. Una transformación que intenta cambiar todo a la vez no cambia nada duraderamente: agota la buena voluntad, abruma a los equipos, y colapsa en la primera crisis. Una transformación que empieza con dolor real, entrega una victoria visible, y se compone desde ahí puede mover una organización de miles a lo largo de unos cuantos años.

Esta hoja de ruta te da principios de adopción, una secuencia basada en madurez desde los primeros 90 días hasta más de dos años, un marco de priorización con un ejemplo trabajado, victorias rápidas dominio por dominio, guía especial para la empresa y el gobierno, formas de medir el éxito, y los modos de fallo que evitar.

## Principios de adopción

Estos principios se sostienen sin importar tu tamaño, sector, o madurez inicial.

- **Empieza con el dolor, no con un marco.** Encuentra lo que más duele, ya sean lanzamientos lentos, interrupciones frecuentes, auditorías fallidas, o rotación, y arréglalo primero. El dolor crea la demanda y la cobertura política que un mandato de arriba hacia abajo nunca puede. Nadie resiste el alivio.
- **Caminos pavimentados sobre mandatos.** Haz que la forma recomendada sea la forma *más fácil*. Un camino dorado que es más rápido, más seguro, y mejor documentado gana la adopción por sus méritos; una política más lenta que la solución alternativa será evadida. Invierte en el camino pavimentado antes de dar de baja el camino de tierra.
- **Mide resultados, no actividad.** Rastrea si el cambio mejoró la entrega, la fiabilidad, la postura de seguridad, o los resultados del usuario, no cuántos equipos asistieron al entrenamiento o marcaron una casilla. Instrumenta antes de cambiar para poder probar el efecto.
- **Asegura el patrocinio ejecutivo, y mantenlo.** El cambio sostenido necesita un ejecutivo responsable que proteja el financiamiento, elimine los bloqueos, y mantenga la línea cuando la transformación se vuelva incómoda. El patrocinio no es un evento de lanzamiento; es una relación continua que debes reganar con resultados.
- **Voluntarios antes que reclutas.** Empieza con los equipos que *quieren* cambiar. Su éxito se convierte en la historia de referencia que atrae a la mayoría reacia. Forzar primero a los resistentes produce cumplimiento malicioso e historias de advertencia.
- **Hazlo reversible donde puedas.** Prefiere los cambios que puedas pilotear, medir, y revertir. Las decisiones reversibles de "puerta de doble vía" pueden moverse rápido; reserva el proceso pesado para lo genuinamente irreversible.
- **Muestra victorias temprano y a menudo.** Envía algo visible en semanas, no trimestres. El impulso es un recurso; gasta la primera victoria para financiar la siguiente.
- **Encuentra a los equipos donde están.** Una única barra de madurez aplicada uniformemente es injusta y desmoralizante. Secuencia por la disposición y el dolor de cada equipo.

## Secuenciación basada en madurez

Los horizontes de abajo son acumulativos: cada uno se construye sobre el anterior. Las fechas son guía, no fechas límite; una organización grande o fuertemente regulada puede ejecutar cada fase más tiempo. El patrón (*estabilizar, luego estandarizar, luego escalar, luego sostener*) se sostiene sin importar el ritmo.

### Primeros 90 días: Estabilizar y probar

Objetivo: establecer una línea base, elegir uno o dos problemas insignia, y entregar una primera victoria creíble con un equipo dispuesto.

- [ ] Nombra a un patrocinador ejecutivo responsable y una pequeña coalición guía.
- [ ] Establece la línea base de las cuatro métricas DORA (frecuencia de despliegue, tiempo de entrega, tasa de fallo de cambio, tiempo para restaurar) incluso si los números son aproximados.
- [ ] Ejecuta una evaluación ligera contra los modelos de madurez del capítulo 12.4 para encontrar las brechas más grandes.
- [ ] Elige uno o dos equipos piloto que se *ofrezcan voluntariamente* y tengan dolor real.
- [ ] Arregla un problema de alta visibilidad de extremo a extremo (por ejemplo, automatiza el despliegue de un equipo, o agrega SLO a un servicio crítico).
- [ ] Levanta un registro compartido de decisiones (ADR) y un lugar para publicar resultados.
- [ ] Acuerda cómo medirás el éxito *antes* de cambiar cualquier cosa.

### A los 6 meses: Estandarizar el patrón ganador

Objetivo: convertir el éxito del piloto en un patrón repetible y documentado y ofrecerlo como camino pavimentado a la siguiente cohorte de equipos.

- [ ] Publica el camino dorado del piloto como plantillas, pipelines, y documentación reutilizables.
- [ ] Establece un equipo de plataforma o habilitador (incluso uno virtual) para poseer y soportar el camino pavimentado.
- [ ] Extiende el patrón a tres a cinco equipos más, priorizando por impacto y disposición.
- [ ] Introduce puertas automatizadas de calidad y seguridad (linting, pruebas, SAST/SCA) en el pipeline compartido como predeterminados, no complementos.
- [ ] Inicia una práctica de revisión de incidentes sin culpa y publica autopsias internamente.
- [ ] Establece un foro de gobernanza ligero (revisión de arquitectura, administración de camino pavimentado) que desbloquee en lugar de vigilar.

### A los 12 meses: Escalar en toda la organización

Objetivo: hacer que el camino pavimentado sea el predeterminado para la mayoría del trabajo nuevo y empezar a retirar las peores prácticas heredadas.

- [ ] Expande el alcance del equipo de plataforma; publica un catálogo de servicios y tarjetas de puntuación.
- [ ] Establece líneas base en toda la organización: SLO para servicios de nivel 1, controles de seguridad en cada pipeline, verificaciones de accesibilidad en las construcciones de frontend.
- [ ] Rastrea las tasas de adopción por equipo y haz los datos visibles.
- [ ] Comienza la modernización deliberada de sistemas heredados en los sistemas de mayor riesgo usando patrones de higuera estranguladora y bifurcación por abstracción.
- [ ] Incorpora la medición en la planificación: los equipos revisan sus tendencias de DORA y fiabilidad en el ritmo normal de operación.
- [ ] Invierte en la habilitación (entrenamiento interno, mentoría, comunidades de práctica) para que la capacidad se propague más rápido que los mandatos.

### 2+ años: Sostener y mejorar continuamente

Objetivo: las prácticas son "cómo trabajamos", no un programa, y la organización las mejora sin impulso central.

- [ ] Retira el programa de transformación como una iniciativa nombrada; incorpora su trabajo en la gobernanza normal y las operaciones de plataforma.
- [ ] Trata el camino pavimentado como un producto con su propia hoja de ruta, usuarios, y métricas de satisfacción (encuestas de experiencia del desarrollador).
- [ ] Gestiona la deuda técnica y la modernización como un portafolio permanente, no un empujón único.
- [ ] Ejecuta reevaluaciones de madurez periódicas y ajusta los estándares hacia arriba conforme sube el piso.
- [ ] Protege contra la regresión: mantén el patrocinio, sigue midiendo, y renueva las prácticas conforme evolucionan la tecnología y las amenazas.

## Un marco de priorización

Siempre tendrás más mejoras por hacer que capacidad para hacerlas. Prioriza con un modelo simple y defendible en lugar de la voz más ruidosa en la sala.

Puntúa cada iniciativa candidata en tres dimensiones:

- **Impacto (1-5):** ¿Cuánto mejorará esto un resultado real (velocidad de entrega, fiabilidad, seguridad, costo, o valor del usuario), y para cuántos equipos o usuarios?
- **Esfuerzo (1-5):** ¿Cuánto trabajo, coordinación, y disrupción para entregarlo? (Más alto = más esfuerzo.)
- **Peso de riesgo (0.5-2.0):** Un multiplicador para la urgencia y la exposición. Los problemas de seguridad, cumplimiento, y seguridad física llevan un peso más alto; los agradables de tener llevan menos.

Una puntuación de clasificación útil es:

```
Prioridad = (Impacto × Peso de riesgo) ÷ Esfuerzo
```

Clasifica por prioridad descendente. Secuencia los elementos principales, pero siempre mantén al menos una "victoria rápida" de bajo esfuerzo en vuelo para sostener el impulso, y revisita las puntuaciones cada trimestre conforme cambian las condiciones.

### Ejemplo trabajado

| Iniciativa | Impacto | Esfuerzo | Peso de riesgo | Prioridad | Secuencia |
|---|---|---|---|---|---|
| Automatizar el despliegue para el servicio de mayor ingreso | 5 | 2 | 1.5 | 3.75 | Ahora |
| Agregar SLO y alertas a servicios de nivel 1 | 4 | 2 | 1.5 | 3.00 | Ahora |
| Introducir SAST/SCA en el pipeline compartido | 4 | 2 | 2.0 | 4.00 | Ahora |
| Desplegar un sistema de diseño a todos los frontends | 4 | 5 | 1.0 | 0.80 | Después |
| Migrar el lote del mainframe a la nube | 5 | 5 | 1.5 | 1.50 | Por fases |
| Estandarizar los ADR entre equipos | 3 | 1 | 1.0 | 3.00 | Ahora (victoria rápida) |
| Adoptar un nuevo lenguaje de programación en toda la organización | 2 | 5 | 0.5 | 0.20 | Diferir |

En este ejemplo, el trabajo del pipeline de seguridad encabeza la lista debido a su alto peso de riesgo y esfuerzo modesto, mientras que el cambio de lenguaje en toda la organización cae al fondo a pesar del entusiasmo, porque su impacto es bajo y su esfuerzo y disrupción son altos. El marco hace explícito y discutible ese intercambio, que es su valor real.

## Victorias rápidas dominio por dominio

Cada parte del libro tiene un primer paso de bajo costo y alta señal. Empieza aquí.

| Parte | Victoria rápida "empieza aquí" |
|---|---|
| **Fundamentos (cultura, equipos, proceso)** | Adopta ADR ligeros y ejecuta una retrospectiva sin culpa; haz visibles las decisiones y el aprendizaje. |
| **Oficio de la programación** | Activa un autoformateador y linter en CI como predeterminados aplicados, para que el estilo deje de ser un tema de revisión. |
| **Arquitectura** | Escribe una decisión de arquitectura de una página y un diagrama de contexto C4 para tu sistema más importante. |
| **Seguridad** | Agrega el escaneo de dependencias (SCA) y el escaneo de secretos al pipeline; habilítalos primero para un repositorio crítico. |
| **UX / diseño** | Ejecuta tres pruebas de usabilidad baratas en tu flujo de mayor tráfico; arregla el problema principal que observes. |
| **IA / AA** | Escribe un enmarcado del problema de una página y una verificación de preparación de datos antes de cualquier trabajo de modelo; define cómo evaluarás el éxito. |
| **Datos / analítica** | Define una única métrica "estrella polar" acordada y un tablero confiable; retira uno en conflicto. |
| **DevOps / plataforma** | Lleva a un equipo a un pipeline de construcción-prueba-despliegue completamente automatizado y documéntalo como la plantilla. |
| **Operaciones / fiabilidad** | Define los SLI y un SLO para tu recorrido de usuario más crítico; alerta sobre síntomas, no causas. |
| **Empresa / gobierno** | Mapea tus controles actuales a un marco (NIST CSF, ISO 27001, o SOC 2) y automatiza la evidencia para un control. |

## Guía especial para la empresa

Las organizaciones grandes y establecidas cargan escala, muchos equipos, legado profundo, y una sobrecarga pesada de gestión del cambio. Adapta la hoja de ruta en consecuencia.

- **Federa, no centralices todo.** Un solo equipo central no puede servir a cientos de equipos de producto. Usa un equipo de plataforma para proveer caminos pavimentados y equipos habilitadores para entrenar, mientras los equipos de producto retienen la propiedad. (Ver Team Topologies.)
- **Respeta la ley de Conway.** Tu arquitectura reflejará tu organigrama. Si quieres servicios desacoplados, necesitas equipos desacoplados y empoderados; reorganiza deliberadamente en lugar de luchar contra la veta.
- **Trata lo heredado como un portafolio.** No puedes modernizar todo. Clasifica los sistemas heredados por riesgo y valor de negocio, y aplica la migración de higuera estranguladora a los pocos que importan; congela o retira deliberadamente el resto.
- **La gestión del cambio es trabajo real.** A escala, la comunicación, el entrenamiento, y la alineación de incentivos no son sobrecarga: son la transformación. Presupuesta explícitamente para la habilitación, las comunidades de práctica, y el evangelismo interno.
- **Cuidado con el reflejo del mandato.** Las grandes organizaciones recurren por defecto a los memorandos de política. Resiste. Un mandato sin camino pavimentado produce marcado de casillas; un camino pavimentado sin mandato produce adopción genuina.
- **Alinea los incentivos y el financiamiento.** Cambia del financiamiento de proyectos a equipos de producto duraderos para que las mejoras sobrevivan más allá de la fecha de finalización de un proyecto. Premia los resultados, no la entrega.

## Guía especial para el gobierno

Las organizaciones del sector público agregan ciclos de adquisición, puertas de cumplimiento, gestión de contratistas, financiamiento de varios años, y obligaciones de transparencia. Estas son entradas de diseño, no excusas.

- **Diseña para el ATO desde el primer día.** La autorización para operar y las puertas de monitoreo continuo (según NIST RMF / 800-37) pueden dominar los cronogramas. Construye los controles de seguridad y la recolección de evidencia en el pipeline temprano para que el cumplimiento sea continuo, no una carrera tardía y bloqueante.
- **Compra incrementalmente.** Las adquisiciones de varios años y gran explosión institucionalizan el fallo de gran explosión contra el que advierte este libro. Prefiere la contratación modular, las adjudicaciones más pequeñas, y los enunciados de trabajo basados en resultados que permiten la iteración.
- **Gestiona a los proveedores e integradores como parte del equipo.** Gran parte de la ingeniería gubernamental la entregan contratistas. Escribe caminos pavimentados, puertas de calidad, y requisitos de transparencia en los contratos, y asegura la transferencia de conocimiento y código al gobierno para evitar el bloqueo y el riesgo de factor de autobús.
- **Planifica alrededor de los ciclos de financiamiento.** Las asignaciones anuales y de varios años restringen a qué puedes comprometerte. Secuencia el trabajo para que cada incremento financiado entregue valor independiente y no te deje varado a mitad de la transformación si cambia el financiamiento.
- **La accesibilidad y el lenguaje llano son obligaciones legales.** La Sección 508, la ADA, las WCAG, y los mandatos de lenguaje llano son requisitos, no mejoras. Incorpora las verificaciones de accesibilidad en los pipelines y la revisión de contenido en el flujo de trabajo.
- **La transparencia es una característica.** La FOIA, los mandatos de código abierto ("dinero público, código público"), y los estándares de servicio publicados significan que tu trabajo está sujeto al escrutinio público. Diseña para ello: registros claros, abiertos donde sea apropiado, y datos de desempeño publicados honestamente.
- **Sigue los patrones probados del sector público.** El U.S. Digital Services Playbook, el GOV.UK Service Standard, y USWDS codifican lecciones duramente ganadas; adóptalos en lugar de reinventar.

## Medir el éxito de la adopción

Mide tanto los indicadores *adelantados* (señales tempranas de que el cambio está arraigando) como los indicadores *rezagados* (los resultados que en última instancia te importan). Vigila la tendencia, no una sola lectura, y nunca dejes que una métrica se convierta en un objetivo para manipular.

| Tipo | Indicador | Qué te dice |
|---|---|---|
| Adelantado | Número de equipos en el camino pavimentado | Qué tan rápido se está extendiendo la adopción |
| Adelantado | Cobertura de puertas del pipeline (pruebas, SAST, a11y) | Qué tan incrustadas se han vuelto la calidad/seguridad |
| Adelantado | Puntuaciones de encuesta de experiencia del desarrollador | Si el camino pavimentado realmente ayuda |
| Adelantado | Porcentaje de decisiones capturadas como ADR | Si la cultura de escritura/aprendizaje es real |
| Rezagado | Frecuencia de despliegue (DORA) | Rendimiento de entrega |
| Rezagado | Tiempo de entrega para cambios (DORA) | Velocidad del commit a la producción |
| Rezagado | Tasa de fallo de cambio (DORA) | Calidad del proceso de entrega |
| Rezagado | Tiempo para restaurar el servicio (DORA) | Resiliencia operativa |
| Rezagado | Tendencia de frecuencia y severidad de incidentes | Mejora de la fiabilidad a lo largo del tiempo |
| Rezagado | Hallazgos de auditoría / fallos de control | Postura de cumplimiento |
| Rezagado | Retención y rotación | Si la cultura está mejorando |

Las cuatro métricas DORA son las medidas de resultado entre industrias más validadas para la entrega; trata la mejora en las cuatro juntas como la señal titular, y cuídate de mejorar una sacrificando otra.

## Modos de fallo comunes y cómo evitarlos

| Modo de fallo | Cómo se ve | Cómo evitarlo |
|---|---|---|
| **Despliegue de gran explosión** | Cambiar todo para todos a la vez; el programa colapsa bajo su propio peso. | Secuencia por dolor y disposición; pilotea, prueba, luego escala. |
| **Mandato sin camino pavimentado** | La política exige la nueva forma, pero la nueva forma es más lenta; los equipos cumplen en papel y la evaden. | Construye el camino más fácil y mejor *primero*; gana la adopción por mérito. |
| **Imitar un marco** | Copiar SAFe, el modelo Spotify, u otra estructura organizacional sin su contexto. | Empieza desde tu propio dolor y principios; adapta, no trasplantes. |
| **Medir actividad, no resultados** | Celebrar el entrenamiento completado y las casillas marcadas mientras la entrega y la fiabilidad no se mueven. | Instrumenta resultados (DORA, incidentes, valor del usuario) desde el principio. |
| **Transformación primero-la-herramienta** | Comprar una plataforma y esperar que la cultura la siga. | Lidera con prácticas y caminos pavimentados; las herramientas los sirven, no al revés. |
| **Perder el patrocinio** | El campeón ejecutivo se va o se desconecta; el programa se estanca. | Institucionaliza el cambio en la gobernanza normal; construye una coalición, no un punto único de fallo. |
| **Métricas de vanidad y manipulación** | Los números de cobertura o velocidad suben mientras la calidad cae. | Usa las métricas como señales con medidas de equilibrio; nunca como objetivos únicos. |
| **Hervir el océano en lo heredado** | Intentar modernizar todo, entregando nada. | Clasifica por riesgo y valor; estrangula a los pocos críticos, congela el resto. |
| **Fatiga de transformación** | Cambio interminable sin recompensa visible; los equipos se desconectan. | Envía victorias tempranas; protege el ritmo sostenible; deja que el programa termine y se convierta en trabajo normal. |
| **Ignorar el organigrama** | La nueva arquitectura lucha contra la estructura de equipo existente. | Aplica la maniobra de Conway inversa: moldea los equipos hacia la arquitectura que quieres. |

## La versión más corta posible

Si no recuerdas nada más de este apéndice:

1. Encuentra el mayor dolor y arréglalo con un equipo dispuesto.
2. Convierte esa corrección en un camino pavimentado que sea genuinamente más fácil que la forma antigua.
3. Mide el resultado, muestra la victoria, y úsala para financiar el siguiente paso.
4. Repite, ampliando el círculo, hasta que el camino pavimentado sea simplemente cómo trabajas.
5. Mantén el patrocinio, sigue midiendo, y nunca hagas gran explosión.

Ver el **capítulo 12.4** para los modelos de madurez que anclan las evaluaciones, y el **capítulo 12.2** para las listas de verificación de lanzamiento, revisión, y auditoría que ponen en operación cada paso.
