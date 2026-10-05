# 11.1 El pipeline de descubrimiento

## Presentación y motivación

El pipeline de descubrimiento es el flujo de trabajo que decide **qué construir y por qué**, y define **cómo se verá el éxito**, antes y junto a la entrega. Donde el pipeline de entrega (capítulo 11.2) convierte ideas validadas en software funcionando, el pipeline de descubrimiento convierte problemas, evidencia y estrategia en un conjunto priorizado y comprobable de resultados pretendidos. En la práctica moderna los dos corren continuamente y en paralelo, a menudo llamados desarrollo de *doble vía*, en lugar de como fases secuenciales. El descubrimiento sigue alimentando un suministro listo de trabajo con riesgo reducido y bien enmarcado a la entrega, y la entrega sigue alimentando datos de resultados del mundo real de vuelta al descubrimiento.

Para equipos grandes, un pipeline de descubrimiento débil es el modo de fallo más costoso en el software. Un equipo con excelente entrega y descubrimiento pobre construye lo incorrecto eficientemente: envía rápido, cumple sus objetivos de velocidad, y aun así no mueve ninguna métrica de negocio. El costo es invisible en los tableros de ingeniería y enorme en el balance general. El pipeline de descubrimiento es cómo haces ese costo visible: obliga a que los objetivos sean explícitos, medibles, y falsables antes de comprometer grandes inversiones.

Los contextos empresarial y gubernamental elevan lo que está en juego. Las empresas coordinan docenas de equipos contra una estrategia compartida, así que los objetivos locales desalineados se componen en portafolios desperdiciados. Los programas gubernamentales comprometen financiamiento público de varios años contra mandatos legislados, donde "construimos lo que decía el contrato" no es defensa si el resultado (ciudadanos atendidos, tiempos de espera reducidos, fraude prevenido) nunca se materializa. Un pipeline de descubrimiento disciplinado, expresado mediante objetivos, medidas, y requisitos de calidad explícitos, es cómo ambos mantienen su intención auditable.

## Principios fundamentales

- **Resultados sobre entregas.** Mide el cambio que creas para los usuarios y el negocio, no las características que envías.
- **Haz explícita y medible la intención.** Un objetivo que no puedes medir es una opinión que no puedes gestionar.
- **Reduce el riesgo antes de construir.** El experimento más barato vence a la opinión más confiada.
- **El descubrimiento y la entrega corren continuamente en paralelo**, no como puertas secuenciales.
- **Los atributos de calidad son requisitos, no ocurrencias tardías.** La fiabilidad, la seguridad, y la accesibilidad se descubren y especifican, no se esperan.
- **La alineación vence a la optimización local.** Los objetivos anidados conectan el trabajo del equipo con la estrategia.
- **Cierra el ciclo.** Los resultados entregados son evidencia que vuelve a entrar al descubrimiento.

## Recomendaciones

### Enmarca la dirección con OKR

Usa los **[Objetivos y Resultados Clave](https://en.wikipedia.org/wiki/OKR) (OKR)** para conectar la estrategia con la ejecución del equipo. Un *Objetivo* es una declaración cualitativa e inspiradora de un estado final deseado ("Hacer que la incorporación por primera vez sea sin esfuerzo"). Los *Resultados Clave* son el pequeño número (típicamente 2 a 4) de resultados medibles que prueban que se está cumpliendo el objetivo ("Aumentar la activación de 7 días del 40% al 60%"; "Reducir los tickets de soporte de incorporación en 30%"). Los resultados clave expresan **resultados**, no tareas: "enviar el nuevo asistente" es una tarea disfrazada de resultado.

Cascada los OKR por *alineación*, no por dictado: el liderazgo establece un pequeño número de objetivos de empresa; los equipos proponen resultados clave y sus propios objetivos que se elevan hacia ellos. Establécelos en una cadencia regular (comúnmente trimestral con un marco anual), revísalos a mitad de ciclo, y califícalos honestamente al final. Manténlos separados de las evaluaciones de desempeño: los OKR calificados para compensación rápidamente se manipulan a la baja. Ver el capítulo 10.1 sobre cómo se conectan los OKR con la gestión de portafolio y programas.

### Monitorea la salud con KPI

Distingue los **[Indicadores Clave de Desempeño](https://en.wikipedia.org/wiki/Performance_indicator) (KPI)** de los OKR. Los OKR describen el *cambio* que quieres este período; los KPI describen la *salud continua* que debes sostener sin importar qué estés cambiando (tiempo de actividad, tasa de conversión, costo por transacción, satisfacción del cliente). Una métrica puede ser ambas (un KPI que estás tratando activamente de mover se convierte en un resultado clave), pero la mayoría de los KPI son barandas que monitoreas, no objetivos hacia los que corres.

Clasifica cada métrica importante como **adelantada** (predictiva y accionable ahora, como las inscripciones de prueba) o **rezagada** (confirmatoria y lenta, como el ingreso anual). El descubrimiento se apoya en indicadores adelantados para guiar antes de que los indicadores rezagados confirmen. Cuidado con las métricas de vanidad que suben confiablemente pero no predicen nada (vistas de página crudas, usuarios registrados totales); prefiere métricas de proporción y cohorte que resisten la manipulación. Ver los capítulos 7.3 y 7.4 sobre la maquinaria de analítica y experimentación detrás de estas medidas.

### Especifica explícitamente los atributos de calidad del sistema

Los requisitos funcionales dicen qué hace el sistema. Los **atributos de calidad del sistema** (las "-idades": fiabilidad, rendimiento, escalabilidad, seguridad, accesibilidad, mantenibilidad, operabilidad) dicen qué tan bien debe hacerlo. Estos son rutinariamente subdescubiertos: todos los asumen, nadie los especifica, y salen a la superficie como incidentes de producción. Trátalos como salida de descubrimiento de primera clase. Identifica los **requisitos arquitectónicamente significativos** (las exigencias de calidad que moldean materialmente la arquitectura) para cada iniciativa. Cuantifícalos ("latencia p99 bajo 200 ms con 10x la carga actual"; "Pautas de Accesibilidad para el Contenido Web (WCAG) 2.2 AA"; "objetivo de tiempo de recuperación de 15 minutos"). Y donde puedas, codifícalos como **funciones de aptitud** automatizadas (verificaciones ejecutables que verifican continuamente un atributo de calidad) que el pipeline de entrega pueda comprobar. Este es el complemento del lado de descubrimiento al capítulo 3.1 (fundamentos de arquitectura) y al capítulo 3.5 (escalabilidad, rendimiento, resiliencia).

### Haz que cada objetivo sea SMART

Ya sea que escribas un resultado clave, un criterio de aceptación, o un objetivo de calidad, aplica la prueba **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)**:

- **Específico:** nombra un resultado claro e inequívoco.
- **Medible:** tiene una métrica y una fuente de verdad.
- **Alcanzable:** es realista dadas las restricciones y la evidencia.
- **Relevante:** se eleva hacia un objetivo superior y hacia el valor del usuario.
- **Con límite de tiempo:** tiene una fecha límite o de revisión.

"Mejorar el rendimiento" falla cada letra. "Reducir el tiempo mediano de pago de 8s a 3s para usuarios móviles para el final del T3, medido por monitoreo de usuario real" pasa las cinco. Los criterios SMART convierten la ambición vaga en una afirmación falsable que el descubrimiento puede probar y la entrega puede verificar.

### Ejecuta descubrimiento continuo e impulsado por evidencia

Estructura el descubrimiento como un pipeline repetible, no una fase única:

1. **Detectar.** Reúne señales: investigación de usuarios, datos de soporte, analítica, entradas de mercado y cumplimiento.
2. **Enmarcar.** Mapea oportunidades (un *árbol de oportunidad-solución* conecta un resultado deseado con las necesidades del usuario y las soluciones candidatas que podrían moverlo).
3. **Hipotetizar.** Declara los supuestos como afirmaciones falsables: "Creemos que [cambio] causará [resultado] para [segmento], y sabremos si [medida] se mueve."
4. **Experimentar.** Valida los supuestos más riesgosos con la prueba más barata: entrevistas, prototipos, pruebas de puerta falsa (anunciar una característica aún no construida para medir la demanda real), [experimentos A/B](https://en.wikipedia.org/wiki/A/B_testing) (comparaciones aleatorizadas de dos variantes, capítulo 7.4).
5. **Decidir.** Perseverar, pivotar, o abandonar, y alimentar a los sobrevivientes al backlog de entrega con sus criterios de éxito SMART adjuntos.

La salida del pipeline de descubrimiento no es una lista de características; es un flujo de *apuestas validadas y medibles* listas para la entrega.

## Ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| **Objetivos basados en resultados (OKR)** | Alinea a los equipos con el impacto; empodera la autonomía en el *cómo* | Difícil de escribir bien; tentador rellenar retroactivamente con tareas; atribución ruidosa |
| **Hojas de ruta de entrega/características** | Predecibles, fáciles de comunicar y contratar | Premian la entrega sobre el impacto; esconden el riesgo de lo incorrecto |
| **Descubrimiento pesado por adelantado** | Reduce el desperdicio de construcción; requisitos fuertes | Ralentiza el inicio; riesgo de parálisis por análisis; supuestos aún sin probar |
| **Descubrimiento continuo de doble vía** | Reduce el riesgo continuamente; retroalimentación rápida | Requiere capacidad de investigación y disciplina; más difícil de programar |
| **Atributos de calidad explícitos como objetivos SMART** | Previene sorpresas de "-idad"; auditable | Esfuerzo de cuantificar; puede sobre-restringir la exploración temprana |

La tensión central es **compromiso frente a aprendizaje**. Las empresas, y especialmente los gobiernos, a menudo necesitan compromisos firmes para presupuestar y contratar, lo que tira hacia hojas de ruta de entregas. Los buenos resultados necesitan espacio para aprender, lo que tira hacia OKR y experimentos. Resuélvelo así: comprométete firmemente con *problemas y resultados*, y sostén sueltamente las *soluciones*.

## Preguntas para discutir con tu equipo

1. **¿Quién en tu equipo realmente posee el descubrimiento, y tiene la capacidad de ejecutarlo continuamente en lugar de en un sprint único?** El desarrollo de doble vía funciona solo cuando alguien mantiene abierta la vía de descubrimiento cada semana en lugar de solo al inicio de un trimestre. En una organización grande, el descubrimiento a menudo no tiene un dueño dedicado, así que colapsa hacia quien tenga tiempo libre, que es nadie, y el equipo recurre por defecto a construir. Trae evidencia: cuenta cuántas de tus últimas diez características pasaron por una hipótesis documentada y una prueba barata antes de construirse, versus directo al backlog. En entornos empresariales y gubernamentales, donde una iniciativa desalineada puede desperdiciar múltiples trimestres de equipo, nombra a un dueño de producto o un trío (producto, diseño, ingeniería) responsable del ciclo detectar-enmarcar-hipotetizar-experimentar-decidir. Si nadie lo posee, dótalo de personal antes de discutir cualquier otra cosa.

2. **¿Cuáles de tus iniciativas actuales tienen requisitos arquitectónicamente significativos que nunca has cuantificado, y podrías codificar alguno como funciones de aptitud?** Las "-idades" (fiabilidad, rendimiento, seguridad, accesibilidad) se asumen y luego salen a la superficie como incidentes de producción. Recorre cada iniciativa activa, pregunta qué atributos de calidad moldean materialmente la arquitectura, y verifica si cada uno tiene un número y una fuente de verdad: "p99 bajo 200 ms con 10x la carga," "WCAG 2.2 AA," "objetivo de tiempo de recuperación de 15 minutos." Para la empresa y el gobierno, los requisitos de accesibilidad o seguridad no cuantificados crean exposición legal y de auditoría directa. La señal a traer son tus últimos tres incidentes: ¿cuántos se rastrearon hasta un atributo de calidad que nadie especificó? Donde puedas convertir un objetivo en una función de aptitud automatizada que el pipeline de entrega verifique, hazlo, porque un objetivo especificado pero no aplicado se desvía.

3. **La última vez que te comprometiste con una solución, ¿probaste primero el supuesto más riesgoso, o el más fácil?** Los equipos confiablemente validan el supuesto con el que están más cómodos y se saltan el que realmente mataría la idea. Para cada iniciativa, lista sus supuestos (deseabilidad, viabilidad, factibilidad) y clasifícalos por "qué tan muerta está esta idea si nos equivocamos aquí," luego apunta la prueba más barata a la parte superior de esa lista. Esto importa a escala porque un equipo confiado y sénior puede comprometer un trimestre de ingeniería a una creencia sin probar, y el costo permanece invisible hasta el lanzamiento. Trae el artefacto: tu última hipótesis declarada como "Creemos que [cambio] causa [resultado] para [segmento], medido por [métrica]," y pregunta si la probaste o simplemente la construiste. Si no puedes nombrar el supuesto más riesgoso, no estás listo para comprometer capacidad de construcción.

4. **¿Cuántos de tus resultados clave son resultados genuinos, y cuántos son tareas o fechas de lanzamiento vestidas de resultado?** El fallo individual más común en la planificación basada en resultados es rellenar retroactivamente los resultados clave con el trabajo que ya planeabas hacer ("lanzar el nuevo asistente") en lugar del cambio que ese trabajo se supone que debe causar ("elevar la activación de 7 días del 40% al 60%"). A escala esto silenciosamente derrota todo el propósito: docenas de equipos reportan verde mientras ninguna métrica de negocio se mueve, porque todos se calificaron a sí mismos por entregar. La atracción en competencia es real, las hojas de ruta de entregas son más fáciles de comunicar, contratar, y pronosticar, que es exactamente por qué se cuelan de vuelta. Trae tu conjunto actual de OKR y marca cada resultado clave como resultado o entrega, luego verifica si la calificación de OKR está entrelazada con la compensación, ya que los resultados atados al salario se manipulan a la baja rápidamente. Para portafolios empresariales y gubernamentales, donde el financiamiento se compromete contra objetivos declarados, una hoja de ruta de entregas sin medida de resultado es un hallazgo de auditoría esperando suceder; insiste en que cada iniciativa se comprometa firmemente con un problema y un resultado medible mientras sostiene sueltamente la solución.

5. **¿Cuáles de tus KPI seguirían subiendo incluso si el producto empeorara, y qué barandas protegen las métricas que estás tratando activamente de mover?** Cada métrica que elevas a un objetivo invita a la [Ley de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law): una vez que una medida se convierte en el objetivo, la gente optimiza la medida en lugar de la cosa que se suponía que representaba. Las métricas de vanidad (vistas de página crudas, usuarios registrados acumulados) suben confiablemente y no predicen nada, mientras que un solo resultado clave perseguido sin barandas puede cumplirse degradando algo que nunca nombraste. La tensión es que los indicadores adelantados te permiten guiar temprano pero son ruidosos y manipulables, mientras que los indicadores rezagados son confiables pero confirman demasiado tarde para actuar. Trae tu inventario de métricas clasificado como adelantado o rezagado y como objetivo o baranda, y pon a prueba cada objetivo preguntando "cómo podría un equipo astuto alcanzar este número mientras empeora el producto." En entornos regulados y públicos, publica las barandas junto con los objetivos, porque un organismo de supervisión que solo ve la métrica titular no puede distinguir el valor público genuino de un número manipulado.

6. **Cuando la entrega envía algo, ¿cómo vuelve realmente a entrar el resultado del mundo real al descubrimiento, o el ciclo permanece abierto?** El desarrollo de doble vía solo se compone si los resultados entregados fluyen de vuelta como evidencia para la siguiente ronda; cuando el ciclo permanece abierto, los equipos envían, celebran, y nunca aprenden si la apuesta valió la pena, así que los mismos supuestos sin probar recurren. En una organización grande el camino de retroalimentación es donde la responsabilidad es más probable que caiga en una brecha: la entrega posee el lanzamiento, la analítica posee el tablero, y nadie posee comparar el resultado clave prometido con el observado. Trae tus últimas diez iniciativas enviadas y pregunta, para cada una, si alguien verificó la métrica de resultado contra el objetivo SMART original y si esa verificación cambió una decisión subsiguiente. Para programas empresariales y gubernamentales que comprometen financiamiento de varios años, nombra la cadencia y el dueño para retirar o redefinir el alcance de características que fallaron en mover su métrica, porque una característica enviada que nadie revisita se convierte en costo permanente sin revisión responsable.

## Perspectiva sectorial

**Startup.** Con un equipo pequeño y poco margen de tiempo, tu pipeline de descubrimiento es deliberadamente ligero pero nunca se salta: un día de entrevistas con clientes y una prueba de puerta falsa cuestan casi nada contra las semanas que una construcción incorrecta quema. Elige un indicador adelantado que represente tu valor central, declara cada apuesta como una sola hipótesis falsable, y mata las ideas antes de escribir código en lugar de después. Los OKR formales son excesivos con cinco personas; un resultado medible honesto por ciclo es suficiente para evitar que la velocidad se convierta en movimiento sin progreso.

**Pequeña empresa.** Probablemente no tienes un investigador dedicado o analista de producto, así que trata el descubrimiento como un hábito, no un rol: unas cuantas conversaciones estructuradas con clientes reales y una métrica simple que ya recolectas. La pregunta de construir versus comprar domina, porque la mayoría de los atributos de calidad (fiabilidad, seguridad, accesibilidad) son más baratos de obtener de un proveedor reputado que de especificar y aplicar tú mismo. Escribe uno o dos objetivos SMART para poder saber si una herramienta comprada o una pequeña construcción realmente movió el resultado, y evita comprometer presupuesto escaso a características que nadie validó que se quieran.

**Empresa.** La escala convierte el descubrimiento en un problema de coordinación a través de docenas de equipos: sin una cadencia compartida de OKR y una definición común de "resultado," los objetivos locales derivan y se duplican, y las apuestas desalineadas se componen en portafolios desperdiciados. Estandariza cómo se cuantifican los requisitos arquitectónicamente significativos y codifícalos como funciones de aptitud para que los atributos de calidad se gobiernen, no se asuman. Gestiona el descubrimiento como un portafolio con criterios de cancelación explícitos y un ciclo que alimenta las métricas de resultado entregadas de vuelta al siguiente ciclo, para que el liderazgo guíe sobre el impacto en lugar de sobre un backlog de características.

**Gobierno.** La adquisición y el financiamiento de varios años exigen compromisos firmes, lo que tira fuertemente hacia contratos de entrega, sin embargo el valor público vive en los resultados: ciudadanos atendidos, tiempos de espera reducidos, carga disminuida. Enmarca los programas alrededor de resultados públicos medibles y atributos de calidad no negociables (accesibilidad WCAG, lenguaje llano, seguridad), y haz que la evidencia de descubrimiento, incluyendo las pruebas de usabilidad con usuarios de tecnología asistiva, sea parte del registro que los organismos de supervisión pueden auditar. Define el éxito como resultados del contribuyente o ciudadano en lugar de módulos entregados, para que "construimos lo que decía el contrato" nunca pueda sustituir un resultado que nunca se materializó.

## Ejemplos

**Startup.** Un equipo de cuatro personas en etapa semilla que construye una aplicación de programación para salones de belleza está tentado a construir un widget de reserva en línea porque unos cuantos usuarios ruidosos lo pidieron. En su lugar ejecutan una semana de descubrimiento: cinco entrevistas con dueños, un botón de "Reservar en línea" de puerta falsa en el sitio de marketing, y un solo indicador adelantado (porcentaje de citas que terminan en inasistencia). Las entrevistas y los datos de clics revelan que las inasistencias, no las reservas, son el dolor real, así que escriben un resultado clave SMART (reducir las inasistencias del 22% a menos del 10% para los salones piloto este trimestre) y envían primero una pequeña característica de depósito y recordatorio, matando el widget de reserva antes de escribir una línea de él.

**Empresa.** El grupo de pagos de un banco minorista reemplaza una hoja de ruta de conteo de características con tres OKR trimestrales, uno siendo "Hacer que los pagos cotidianos se sientan instantáneos" con resultados clave para el tiempo de confirmación de transferencia p95, la tasa de éxito al primer intento, y los contactos de soporte relacionados con pagos. Los atributos de calidad del sistema se especifican por adelantado (99.99% de disponibilidad, confirmación en menos de un segundo, alcance de PCI-DSS (Estándar de Seguridad de Datos de la Industria de Tarjetas de Pago) minimizado) y se cablean en la entrega como funciones de aptitud. El descubrimiento ejecuta entrevistas semanales con clientes y pruebas de puerta falsa antes de comprometer ingeniería. Dos características candidatas se cancelan en el descubrimiento por no mover los indicadores adelantados (ahorrando un estimado de dos trimestres de esfuerzo de construcción), mientras que una corrección de latencia más pequeña y menos glamorosa mueve más el resultado clave.

**Gobierno.** Una agencia tributaria nacional que moderniza la declaración en línea establece un objetivo de programa de "Reducir la carga de declarar para contribuyentes ordinarios," con resultados clave SMART: reducir el tiempo mediano para declarar de 45 a 20 minutos, elevar la finalización exitosa de autoservicio del 60% al 85%, y cumplir con WCAG 2.2 AA y estándares de lenguaje llano como atributos de calidad no negociables. Los KPI (tiempo de actividad durante la temporada de declaración, volumen del centro de llamadas) se monitorean como barandas. El descubrimiento usa pruebas de usabilidad moderadas con contribuyentes reales, incluyendo usuarios de tecnología asistiva, antes de cada lanzamiento. Como el éxito se define como resultados del contribuyente en lugar de módulos entregados, el programa puede mostrar a los organismos de supervisión valor público medible, no solo gasto.

## Caso de negocio: motivaciones, ROI y TCO

El retorno de un pipeline de descubrimiento está dominado por el **desperdicio evitado**. La experiencia de la industria, reflejada en programas de experimentos controlados en grandes empresas de tecnología, repetidamente encuentra que una gran proporción de las características construidas, a menudo citada alrededor de la mitad o más, no produce mejora medible o daña activamente la métrica objetivo. Supón que incluso un cuarto de la capacidad de construcción de un equipo va a ideas que el descubrimiento habría cancelado baratamente. El pipeline entonces se paga a sí mismo muchas veces: una semana de investigación de usuarios y una prueba de puerta falsa cuesta casi nada contra un trimestre de ingeniería, más la carga de mantenimiento continuo de una característica sin uso.

El enfoque del **[costo total de propiedad](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO) importa porque las características sin validar no son gratis después del lanzamiento. Cada característica enviada carga costos perpetuos: mantenimiento, pruebas, superficie de seguridad, soporte, y carga cognitiva (capítulo 10.4). Cancelar una mala idea en el descubrimiento evita no solo el costo de construcción sino toda la cola de propiedad. Los atributos de calidad explícitos siguen la misma lógica: especificar la fiabilidad y la accesibilidad como objetivos SMART por adelantado es mucho más barato que adaptarlos después de una interrupción, una brecha, o una demanda.

Para hacer el caso al liderazgo, cambia la conversación de "cuánto estamos enviando" a "cuánto estamos moviendo las métricas que importan," y muestra unos cuantos ejemplos concretos de características costosas que no movieron nada. El costo de adopción es modesto (capacidad de investigación, una cadencia de OKR, y la disciplina de escribir criterios SMART), y el riesgo principal de *no* adoptarlo es silencioso, no contado, y acumulativo.

## Antipatrones y trampas

- **Hojas de ruta de características disfrazadas de estrategia:** listas de entregas sin resultado o medida declarada.
- **Resultados clave que son tareas:** "lanzar X" en lugar de "mejorar Y en Z."
- **Teatro de OKR:** objetivos escritos, archivados, y nunca revisados ni calificados.
- **OKR manipulados a la baja o heroicos:** objetivos establecidos para garantizar el 100% (nada aprendido) o estiramientos de fantasía sin plan.
- **Atributos de calidad sin especificar:** fiabilidad, seguridad, y accesibilidad asumidas en lugar de cuantificadas, luego descubiertas en producción.
- **Métricas de vanidad:** medidas que siempre suben y no predicen nada.
- **Descubrimiento como una fase única:** un "sprint de descubrimiento" al principio, y luego ninguna validación continua.
- **Construir la solución antes de probar el supuesto:** saltarse el experimento más barato porque el equipo está confiado.
- **Fijación en métricas y [Ley de Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law):** una vez que una medida se convierte en el objetivo, deja de ser una buena medida; equilibra con KPI de baranda.

## Modelo de madurez

- **Nivel 1 (Iniciar):** El trabajo se define como características en una hoja de ruta y el éxito es "lo enviamos." No hay medidas explícitas de resultado ni objetivos de calidad; el descubrimiento sucede por accidente, si acaso, y las decisiones se guían por la opinión más ruidosa.
- **Nivel 2 (Desarrollar):** Los OKR y KPI existen para algunos equipos pero no otros; los objetivos se declaran aunque a menudo tienen forma de entrega; los atributos de calidad se nombran pero no se cuantifican. Un equipo puede ejecutar un "sprint de descubrimiento" único, y luego dejar de validar una vez que empieza la construcción, así que la práctica es real pero inconsistente en la organización.
- **Nivel 3 (Estandarizar):** Una cadencia consistente de OKR alineada a la estrategia, resultados clave SMART, y atributos de calidad especificados y comprobables están documentados y esperados en toda la organización. El descubrimiento es una actividad reconocida y dotada de personal con hipótesis y experimentos, y los requisitos arquitectónicamente significativos se identifican para cada iniciativa en lugar de asumirse.
- **Nivel 4 (Gestionar):** El portafolio se mide contra líneas base. Los indicadores adelantados y rezagados, la tasa de acierto del descubrimiento, y el resultado que cada apuesta enviada realmente movió se rastrean contra su objetivo SMART; las hipótesis se califican con evidencia y los criterios de cancelación se aplican; las funciones de aptitud reportan la conformidad de atributos de calidad continuamente, así que la deriva de un objetivo especificado de fiabilidad, rendimiento, o accesibilidad se detecta con datos en lugar de en un incidente.
- **Nivel 5 (Orquestar):** El descubrimiento continuo de doble vía está integrado con el portafolio, el riesgo, y el presupuesto; las apuestas validadas fluyen constantemente hacia la entrega y las métricas de resultado retroalimentan automáticamente para guiar la siguiente ronda. Los indicadores adelantados guían la inversión, y la organización rutinariamente retira, redefine el alcance, y reequilibra las iniciativas con base en evidencia, adaptando el pipeline mismo conforme cambian el mercado y las métricas.

## Ideas para el debate

1. Mira tu hoja de ruta actual: ¿cuántos elementos declaran un resultado medible versus solo una característica para enviar?
2. ¿Cuáles de los resultados clave de tu equipo son en realidad tareas disfrazadas, y cómo los reescribirías?
3. ¿Qué atributos de calidad del sistema depende tu producto que nunca se han cuantificado explícitamente?
4. ¿Cuál fue el experimento más barato que podría haber matado tu última característica fallida antes de construirla?
5. ¿Cómo resuelves la tensión entre los compromisos firmes que exige el presupuesto/adquisición y el aprendizaje que requieren los buenos resultados?
6. ¿Cuáles de tus KPI seguirían subiendo incluso si el producto estuviera empeorando?

## Puntos clave

- El pipeline de descubrimiento decide *qué* y *por qué*, y define el éxito **antes** de que la entrega comprometa recursos.
- Usa **OKR** para el cambio que quieres, **KPI** para la salud que sostienes, y clasifica las métricas como adelantadas o rezagadas.
- Trata los **atributos de calidad del sistema** como requisitos explícitos, cuantificados, y comprobables, no supuestos.
- Haz que cada objetivo, resultado clave, y criterio de aceptación sea **SMART**.
- Ejecuta el descubrimiento **continuamente y en paralelo** con la entrega; valida los supuestos más riesgosos baratamente.
- El ROI dominante es el **desperdicio evitado**: tanto el costo de construcción como el TCO perpetuo de características sin uso.
- Cierra el ciclo: las **métricas de resultado** entregadas (capítulo 11.2) son la evidencia principal para la siguiente ronda de descubrimiento.

## Referencias y lecturas adicionales

- *Measure What Matters*, de John Doerr (sobre OKR).
- *Radical Focus*, de Christina Wodtke (sobre OKR en la práctica).
- *Continuous Discovery Habits*, de Teresa Torres (árboles de oportunidad-solución, descubrimiento de doble vía).
- *Inspired* y *Empowered*, de Marty Cagan (descubrimiento de producto y equipos de resultados).
- *Lean Analytics*, de Alistair Croll y Benjamin Yoskovitz (indicadores adelantados, métricas de vanidad).
- *The Lean Startup*, de Eric Ries (construir-medir-aprender, aprendizaje validado).
- *Escaping the Build Trap*, de Melissa Perri (resultados sobre entregas).
- *Outcomes Over Output*, de Joshua Seiden.
- *Software Architecture in Practice*, de Bass, Clements, Kazman (atributos de calidad).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): origen de los criterios SMART.
