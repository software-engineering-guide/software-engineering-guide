# 6.2 Ingeniería de aprendizaje automático (MLOps)

## Visión general y motivación

La ingeniería de aprendizaje automático, conocida habitualmente como [MLOps](https://en.wikipedia.org/wiki/MLOps), es la disciplina que lleva el [aprendizaje automático](https://en.wikipedia.org/wiki/Machine_learning) fuera de los cuadernos de experimentación y los prototipos, y lo integra en sistemas de producción fiables, observables y mantenibles. El software tradicional se comporta de la forma en que su código lo prescribe. Un sistema de aprendizaje automático, en cambio, se comporta de la forma en que, conjuntamente, su código, sus datos y sus parámetros de modelo aprendidos lo determinan. Esa naturaleza triple hace que estos sistemas sean más difíciles de probar, más difíciles de reproducir y propensos a fallar de forma silenciosa cuando el mundo real se aleja de los datos sobre los que fueron entrenados. El MLOps traslada al aprendizaje automático el rigor de la ingeniería de software (control de versiones, pruebas, entrega continua y monitorización) , aplicándolo a esta realidad de tres componentes: código, datos y modelos.

En equipos grandes, el MLOps es lo que separa un modelo aislado que impresiona en una demostración de una flota de modelos que muchos equipos pueden construir, desplegar y operar con seguridad. Sin plataformas y prácticas compartidas, cada equipo reinventa desde cero las tuberías de datos, los bucles de entrenamiento y los procesos de despliegue, y el resultado son sistemas frágiles que nadie puede reproducir seis meses después. Las empresas dependen del MLOps para escalar decenas de modelos, cumplir los objetivos de nivel de servicio y responder a auditores que preguntan cómo se produjo una predicción concreta.

En el sector público y en las industrias reguladas, el MLOps suele ser, en la práctica, un requisito de cumplimiento disfrazado. La reproducibilidad, el linaje y el control de versiones son lo que permite a una agencia responder a una pregunta de peso legal: ¿qué modelo exacto, entrenado con qué datos y con qué código, generó la decisión que afectó a un ciudadano? Una práctica madura de MLOps mantiene esa pregunta respondible años después, lo que constituye al mismo tiempo buena ingeniería y salvaguardia jurídica.

*Véase también:* capítulo 8.1 (CI/CD y entrega), capítulo 9.2 (observabilidad y monitorización) y capítulo 6.6 (infraestructura y operaciones de IA).

## Principios fundamentales

- Tratar los datos, el código y los modelos como artefactos versionados de forma conjunta; la modificación de cualquiera de ellos altera el comportamiento del sistema.
- Automatizar el camino desde los datos hasta el modelo entrenado y su despliegue, de modo que sea repetible y auditable.
- Hacer que cada modelo sea trazable hasta los datos, el código y la configuración exactos que lo originaron.
- Evaluar los modelos con datos representativos y retenidos para validación antes del despliegue, y seguir evaluándolos después.
- Asumir que los modelos se degradan; vigilar desde el primer día la deriva (la divergencia progresiva de los datos en vivo o de las relaciones entrada-salida respecto a lo que el modelo vio en el entrenamiento), los problemas de calidad de los datos y el deterioro del rendimiento.
- Preferir tuberías sencillas y reproducibles a experimentos ingeniosos pero irreproducibles.
- Separar las preocupaciones de la velocidad de experimentación y la fiabilidad de producción, y tender un puente deliberado entre ambas.

## Recomendaciones

### Gestionar el ciclo de vida completo del ML de forma explícita

Definir e instrumentar cada etapa: ingesta y validación de datos, [ingeniería de características](https://en.wikipedia.org/wiki/Feature_engineering), entrenamiento, evaluación, despliegue y monitorización. Hacer explícitos los límites entre etapas para que cada una pueda ponerse a prueba, repetirse y auditarse. Evitar la falla recurrente en la que un modelo se entrena en un cuaderno improvisado y se transfiere, sin más, al equipo de operaciones. En su lugar, envolver todo el ciclo en una tubería orquestada que cualquier ingeniero autorizado pueda ejecutar desde un clonado limpio.

### Emplear almacenes de características, seguimiento de experimentos y registros de modelos

Un **almacén de características** (*feature store*) centraliza las definiciones de las características para que las mismas transformaciones se ejecuten tanto en entrenamiento como en servicio. Esto elimina el sesgo entre entrenamiento y servicio (las inconsistencias entre cómo se calculan las características para entrenar y cómo se calculan para las predicciones en vivo) y permite que los equipos reutilicen características en lugar de recalcularlas. El **seguimiento de experimentos** registra los parámetros, la versión de código, la versión de datos y las métricas de cada ejecución de entrenamiento, de modo que los resultados sean comparables y reproducibles. Un **registro de modelos** es el sistema de referencia autorizada de los modelos entrenados: contiene versiones, linaje, resultados de evaluación, estado de aprobación y etapa de despliegue. Juntos, estos tres pilares permiten responder a «¿qué cambió?» cuando el comportamiento se altera, y promocionar o revertir modelos a través de etapas gobernadas.

### Hacer que los datos y los modelos sean reproducibles y versionados, con linaje completo

Versionar los conjuntos de datos, no solo el código. Utilizar almacenamiento con direccionamiento por contenido o herramientas de versionado de datos para que cada ejecución de entrenamiento refiera a una instantánea inmutable. Fijar el código mediante *commits* de Git y bloquear los entornos con dependencias fijadas e imágenes de contenedor. Capturar el linaje de extremo a extremo: qué datos crudos alimentaron qué características, qué características y qué código generaron qué modelo, y en qué lugar se despliega ese modelo. Cuando ocurre un incidente o llega una auditoría, el linaje convierte lo que sería una pesadilla forense en una consulta sencilla. Registrar la aleatoriedad (semillas) y el hardware cada vez que los resultados dependan de ellos.

### Elegir patrones de despliegue acordes a la carga de trabajo

- **Por lotes** (*batch*): el cálculo se ejecuta de forma periódica sobre grandes volúmenes de datos. Es el más sencillo de operar, tolera latencia y resulta ideal para informes y decisiones periódicas.
- **En línea (tiempo real)**: responde a cada solicitud individual dentro de presupuestos estrictos de latencia; exige recuperación de características de baja latencia y una planificación de capacidad cuidadosa.
- **En flujo** (*streaming*): el cálculo opera de forma continua a medida que llegan los eventos; es apropiado para la detección de fraude y la vigilancia en tiempo real, donde la frescura de la información es crítica.
- **En el borde** (*edge*): los modelos se ejecutan en dispositivos o en hardware local por motivos de latencia, privacidad, conectividad o soberanía de datos; es frecuente en entornos gubernamentales y de campo.

Elegir el patrón más simple que satisfaga el requisito y diseñar el despliegue con pruebas en modo espejo, despliegues canario y revertir instantánea.

### Vigilar la deriva, el deterioro y la calidad de los datos

Instrumentar entradas y salidas en producción. Observar la **deriva de datos** (cambio en las distribuciones de entrada), la **[deriva conceptual](https://en.wikipedia.org/wiki/Concept_drift)** (cambio en la relación entre entradas y variable objetivo), los fallos de **calidad de datos** (valores nulos, cambios de esquema, fuentes aguas arriba rotas) y el **deterioro del rendimiento** medido frente a la verdad de referencia retrasada, cuando esta está disponible. Definir umbrales de alerta, redactar guías de respuesta y vincular la monitorización con los disparadores de reentrenamiento. La degradación silenciosa es el modo de fallo clásico del aprendizaje automático, y la monitorización es la única defensa eficaz.

## Compromisos: ventajas e inconvenientes

| Decisión | Opción A | Opción B | Compromiso |
|---|---|---|---|
| Patrón de servicio | Por lotes | En línea | Sencillez y coste frente a frescura y latencia |
| Cálculo de características | Almacén de características | Tuberías por modelo | Consistencia y reutilización frente a esfuerzo de configuración |
| Plataforma | Plataforma MLOps gestionada | Ensamble de herramientas de código abierto | Rapidez y soporte frente a flexibilidad y riesgo de dependencia |
| Reentrenamiento | Programado | Disparado por deriva | Previsibilidad frente a responsividad y complejidad |
| Rigor de reproducibilidad | Versionado completo de datos | Seguimiento ligero | Fuerza de auditoría frente a almacenamiento y esfuerzo |

El compromiso de fondo es entre la inversión presente y la fragilidad futura. La infraestructura pesada de reproducibilidad y monitorización cuesta esfuerzo al principio, pero previene el coste mucho mayor de fallos inexplicables, modelos irreproducibles y erosión de la confianza. Las plataformas gestionadas aceleran a los equipos, pero pueden crear dependencia de un proveedor; los conjuntos de código abierto ofrecen control a cambio de un trabajo real de integración. En las grandes organizaciones suele beneficiarse de un equipo de plataforma compartido que oculta esta complejidad tras *paved road* (caminos pavimentados por defecto).

## Pregunta para debatir en equipo

1. **¿Cómo sabremos que un modelo desplegado se ha degradado de forma silenciosa antes de que un cliente o ciudadano sufra un daño, y quién es el responsable de esa alerta?** La degradación silenciosa es el modo de fallo clásico del aprendizaje automático: el código sigue funcionando, el modelo sigue devolviendo puntuaciones con confianza, y la calidad se deteriora a medida que el mundo se aleja de los datos de entrenamiento. En un equipo grande con muchos modelos, esta pregunta debe resolverse por cada modelo, no una sola vez para toda la flota, porque cada uno tiene su propio perfil de deriva y su propio retraso de verdad de referencia. Traer a la reunión los monitores actuales de deriva de datos, deriva conceptual y roturas de calidad, los umbrales de alerta y la guía de respuesta que indica quién interviene. En entornos regulados, donde las etiquetas llegan con semanas de retraso, conviene discutir señales proxy que puedan vigilarse mientras tanto, porque esperar a la verdad de referencia retrasada significa esperar a descubrir el daño. Si no se nombra un único responsable de la alerta de deriva de un modelo, ese modelo está, en la práctica, sin monitorizar.

2. **Si un auditor nos pidiera reproducir una predicción concreta de hace dieciocho meses, ¿podríamos hacerlo de principio a fin?** La reproducibilidad es el requisito de cumplimiento oculto tras una buena ingeniería: permite a una agencia responder exactamente qué modelo, entrenado con qué datos y con qué código, generó una decisión que afectó a alguien. Traer un ejemplo real y tratar de trazarlo: la instantánea inmutable de datos, el *commit* de Git, las dependencias bloqueadas y la imagen de contenedor, las semillas registradas y el linaje desde los datos crudos, pasando por las características, hasta el modelo desplegado. La señal de alarma es que cualquier eslabón de esa cadena esté ausente o sea manual. En el sector público y en industrias reguladas, conviene fijar el período de retención que la ley exige y confirmar que el almacenamiento mantiene el linaje respondible durante todo ese lapso, porque un vacío convierte una consulta rutinaria en una emergencia forense.

3. **¿Cuál es nuestra norma para promocionar un modelo a producción y revertirlo, y está esa norma impuesta por el registro o solo respaldada por la confianza?** La promoción sin gobierno es cómo los experimentos de cuaderno filtran a producción y cómo un modelo defectuoso permanece porque nadie puede revertirlo con limpieza. Para muchos equipos, la diferencia entre madurez y fragilidad radica en si el registro de modelos gobierna la promoción con aprobación y evaluación obligatorias, o si un ingeniero puede empujar pesos a mano. Traer el camino de promoción actual, el mecanismo de reversión y la evidencia de que los despliegues en modo espejo o canario se ejecutan de verdad antes de derivar todo el tráfico. Discutir si el reentrenamiento es programado o disparado por deriva, y si los modelos reentrenados superan puertas de validación antes del despliegue, porque reentrenar sobre datos en vivo sin validación amplifica la deriva o el envenenamiento. La respuesta debe estar impuesta en la plataforma, no en una página de wiki a la que se confía en que nadie lee.

4. **¿Construimos nuestra plataforma MLOps sobre herramientas de código abierto, compramos una gestionada o combinamos ambas, y quién ha sopesado el riesgo de dependencia?** Esta elección fija el techo de velocidad con que cada modelo futuro llegará a producción y el grado de control que se conserva sobre los datos y las tuberías. Una plataforma gestionada lleva a los equipos a producción con rapidez y ofrece soporte, pero puede atrapar las definiciones de características, los registros de linaje y los artefactos de modelos en un formato propietario del que no se sale fácilmente; un conjunto ensamblado de código abierto mantiene la portabilidad a cambio de un trabajo real de integración y mantenimiento. Traer el coste total de propiedad de cada vía (licencia o desarrollo, almacenamiento, cómputo para reentrenamiento y el personal de plataforma para operarlo), una lectura honesta de la capacidad del equipo para sostener infraestructura y una prueba concreta de salida: ¿podría exportarse el registro, el almacén de características y el linaje y reconstruirse en otro lugar? En entornos empresariales y gubernamentales, añadir restricciones de contratación pública y reglas de soberanía de datos, porque una plataforma que almacena datos de entrenamiento en una región o un formato que el regulador prohíbe queda descartada, por conveniente que resulte.

5. **¿Deben el almacén de características y el registro de modelos ser una plataforma centralizada o federada por equipo, y qué nos cuesta hoy el sesgo entre entrenamiento y servicio?** Centralizar las definiciones de características elimina el sesgo entre entrenamiento y servicio (el caso en que una característica se calcula de una forma para entrenar y de otra para servir, una fuente silenciosa y costosa de pérdida de precisión) , pero una plataforma única puede convertirse en un cuello de botella que ralentiza a todos los equipos. La federación otorga autonomía a cada equipo, pero multiplica la tubería y la probabilidad de que dos equipos definan la misma característica de forma inconsistente. Traer evidencia de dónde el sesgo ya ha causado daño, cuántos equipos reutilizan características frente a cuántas las reconstruyen y los *paved road* que un equipo de plataforma compartido podría ofrecer. En una organización grande, pesar el beneficio de gobernanza de un único sistema de referencia auditable contra el coste de entrega de una cola central, y en entornos regulados priorizar el linaje centralizado que permite a un auditor trazar cualquier predicción hasta el código exacto de la característica que la generó.

6. **¿Hemos adaptado el patrón de despliegue de cada modelo a sus necesidades reales de latencia, frescura y soberanía, o hemos estandarizado todo en un único formato?** Los patrones por lotes, en línea, en flujo y en el borde implican costes y complejidades operativas muy distintas: elegir el equivocado supone malgastar infraestructura de tiempo real en un informe nocturno que nunca la necesitó, o privar a un detector de fraude de la frescura de la que depende. Decidir por cada carga de trabajo qué patrón justifica el requisito, y resistirse a estandarizar en la opción más compleja solo porque resulta moderna. Traer el presupuesto de latencia, el volumen, el coste de una respuesta obsoleta y el retraso de la verdad de referencia de cada modelo. En el sector público y en entornos de campo, sopesar deliberadamente el despliegue en el borde y en instalaciones locales, porque las reglas de soberanía de datos o la conectividad intermitente pueden obligar a llevar modelos a hardware local, y esa elección redefine la forma en que se versiona, monitorea y revierte cada modelo que se empuja allí.

## Lente sectorial

**Startup.** El recurso más escaso es la atención del equipo de ingeniería, por lo que conviene mantener el MLOps ligero y comprarlo. Seguir los experimentos en una herramienta sencilla alojada en la nube, anclar cada modelo desplegado a su instantánea de datos de entrenamiento y su *commit* de código en Git, y añadir un control de deriva económico en lugar de una plataforma completa. Posponer el almacén de características y las tuberías a medida hasta que un segundo o tercer modelo haga que la reutilización valga la pena; un conjunto frágil que no se puede mantener hundirá a la empresa más rápido que la falta de una capacidad.

**Pyme.** Lo más probable es que no haya un especialista en plataformas de ML y el presupuesto sea ajustado, por lo que conviene tratar el MLOps como algo integrado en las herramientas que ya se utilizan, no como un sistema que requiere plantilla propia. Preferir un servicio gestionado que se ocupe del versionado, el despliegue y la monitorización, y formular la disciplina como una cuestión de higiene de datos y reproducibilidad: saber qué modelo y qué datos generaron un resultado dado, y conservar la capacidad de revertir. Fomentar a los proveedores que permitan exportar datos y modelos, para que un cambio posterior siga siendo viable.

**Gran empresa.** El reto es la escala: decenas de modelos y muchos equipos. Se precisa un almacén de características compartido, un servicio de seguimiento de experimentos y un registro de modelos con puertas de promoción gobernadas, de modo que los equipos dejen de reinventar tuberías. Prever un equipo de plataforma que ofrezca *paved road* por defecto, estandarizar el linaje y la monitorización para que cada modelo sea auditable y cada incidente explicable, y gestionar la decisión construir-comprar y el riesgo de dependencia de forma deliberada, tras una interfaz que mantenga las herramientas subyacentes intercambiables. Imponer las puertas de validación y la reversión en la plataforma, no en la convención.

**Sector público.** La reproducibilidad, el linaje y el control de versiones son, en la práctica, requisitos de cumplimiento, por lo que deben tratarse como de primera clase desde el primer día. Versionar el conjunto de datos y el código exactos detrás de cada modelo desplegado, conservar ese linaje durante el período que la ley exige y poder reproducir cualquier predicción histórica que haya afectado a un ciudadano. Mantener a un humano revisando las decisiones de consecuencias importantes, sopesar el despliegue en el borde y en instalaciones locales donde las reglas de soberanía de datos lo exijan, y exigir que cualquier plataforma de un proveedor conceda plena portabilidad de datos, características y linaje.

## Ejemplos

**Startup.** Una pequeña empresa de analítica lanzó su primer modelo de predicción de abandono de clientes con una sola data scientist y un montaje ligero. Seguía los experimentos en una herramienta sencilla alojada en la nube, anclaba cada modelo desplegado a su instantánea de datos de entrenamiento y su *commit* de código en Git, y añadía un trabajo semanal básico que comparaba las entradas recientes con la distribución de entrenamiento. Cuando una fuente de datos cambió su formato de fecha y las predicciones empezaron a desviarse, ese control sencillo lo detectó en días, no tras una llamada de un cliente enfurecido, y el equipo pudo reproducir el último modelo en buen estado y revertir.

**Gran empresa.** Un banco minorista opera decenas de modelos de crédito y de detección de fraude. Ha estandarizado en un almacén de características compartido entre equipos, un servicio de seguimiento de experimentos y un registro de modelos con puertas de aprobación obligatorias. Cada modelo en producción se traza hasta su instantánea de datos de entrenamiento y su *commit* de código. Los modelos de fraude se despliegan como clasificadores en flujo; los de crédito, en lotes. Una capa de monitorización vigila la deriva de entrada y alerta cuando una fuente de datos cambia su esquema, lo que en una ocasión detectó un flujo aguas arriba roto antes de que corrompiera decisiones.

**Sector público.** Una agencia de prestaciones públicas emplea un modelo de aprendizaje automático para priorizar la revisión de expedientes. Dado que esas decisiones afectan al acceso de los ciudadanos a los servicios, la agencia versiona el conjunto de datos y el código exactos detrás de cada modelo desplegado, conserva ese linaje durante el período que la ley exige y puede reproducir cualquier predicción histórica bajo demanda. Los modelos se despliegan por lotes, con un humano que revisa los casos marcados, y un monitor de deriva obliga a una reevaluación obligatoria cada vez que la población que ingresa se desplaza, de modo que el modelo nunca se aplica, en silencio, fuera de las condiciones en que fue validado.

## Caso de negocio: motivaciones, retorno y coste total de propiedad

El MLOps se justifica por sí mismo al convertir experimentos frágiles en activos fiables. El retorno procede de un tiempo de llegada a producción más corto para nuevos modelos, menos incidentes costosos, menos infraestructura duplicada y la capacidad de operar muchos modelos con un pequeño equipo de plataforma. Un almacén de características y un registro compartidos pueden reducir drásticamente el tiempo de entrega por modelo, porque los equipos dejan de reconstruir la misma tubería.

El coste total de propiedad abarca la construcción o licencia de la plataforma, el almacenamiento de datos y modelos versionados, el cómputo para el reentrenamiento y el personal que lo todo opera. Confrontar ese coste con el de no adoptar el MLOps: modelos que no se pueden reproducir ni auditar, fallos silenciosos que dañan a clientes o ciudadanos, y hallazgos regulatorios. En entornos regulados, el coste de un modelo inexplicable en una auditoría puede eclipsar la inversión total en MLOps. Argumentar ante la dirección enmarcando el MLOps como reducción de riesgo y aceleración de la entrega, no como sobrecoste: un camino pavimentado que cada modelo futuro recorrerá.

## Antipatrón y trampas

- **Saltos del cuaderno a producción.** Desplegar modelos entrenados en cuadernos sin gobierno y sin reproducibilidad.
- **Sesgo entre entrenamiento y servicio.** Código de características distinto en entrenamiento y en servicio, que genera una pérdida silenciosa de precisión.
- **Sin versionado de datos.** Versionar el código pero no los datos, de modo que las ejecuciones no pueden reproducirse.
- **Desplegar y olvidar.** Poner un modelo en producción sin monitorización y descubrir la degradación solo cuando los usuarios se quejan.
- **Reentrenamiento en piloto automático.** Reentrenar automáticamente sobre datos en vivo sin validación, amplificando la deriva o el envenenamiento.
- **Infraestructura única por equipo.** Cada equipo construye su propia tubería, multiplicando el coste y la fragilidad.
- **Ignorar las etiquetas retrasadas.** Asumir que se puede medir la precisión de forma instantánea cuando la verdad de referencia llega con semanas de retraso.

## Modelo de madurez

1. **Iniciar.** Los modelos se construyen de forma ad hoc en cuadernos; el despliegue es manual; no hay versionado de datos ni de modelos; no hay monitorización; reproducir una predicción pasada es una conjetura.
2. **Desarrollar.** Aparece algún seguimiento de experimentos y un registro de modelos, pero las prácticas varían entre equipos; el despliegue es semiautomático; la monitorización básica cubre unos pocos modelos; el versionado de datos es parcial y el linaje presenta vacíos.
3. **Estandarizar.** Una plataforma compartida con almacén de características, registro, tuberías reproducibles y linaje de extremo a extremo está documentada y se aplica en toda la organización; la monitorización de deriva y calidad de datos opera en todos los modelos; la promoción y la reversión siguen un camino gobernado que cada equipo utiliza.
4. **Gobernar.** La flota se mide frente a líneas de base: tasas de deriva, roturas de calidad de datos, precisión del modelo frente a la verdad de referencia retrasada, sesgo entre entrenamiento y servicio, tiempo de llegada a producción y coste operativo por modelo se siguen como métricas; los umbrales de alerta y las puertas de validación se imponen sobre evidencia, y la salud de cada modelo se revisa en una cadencia fija con un responsable nombrado.
5. **Orquestar.** El ciclo de vida está plenamente automatizado, auditable y adaptativo; el reentrenamiento disparado por deriva se ejecuta tras puertas de validación; los *paved road* de autoservicio permiten a los equipos publicar con seguridad; la evaluación continua vincula el rendimiento del modelo con las métricas de negocio, y la plataforma se integra con la entrega, el riesgo y el cumplimiento, de modo que los modelos se retiran, reemplazan y redefinen con regularidad a medida que los datos y las condiciones cambian.

## Ideas para la discusión

- ¿Cómo se equilibra la libertad de experimentación con la reproducibilidad de producción?
- ¿Cuál es el disparador de reentrenamiento adecuado (programación, deriva o deterioro del rendimiento) para cada caso de uso?
- ¿Cuánto tiempo debe conservarse el linaje de datos y modelos, y qué impulsa ese requisito?
- ¿Deben el almacén de características y el registro ser plataformas centralizadas o federadas por equipo?
- ¿Cómo se monitoriza la precisión cuando las etiquetas de verdad de referencia llegan con grandes retrasos?
- ¿Cuándo vale la pena la complejidad operativa añadida del despliegue en el borde?

## Conclusiones clave

- El comportamiento del ML proviene del código más los datos más los modelos; versionar y gobernar los tres de forma conjunta.
- El almacén de características, el seguimiento de experimentos y el registro de modelos son el esqueleto del ML reproducible.
- El linaje hace que los modelos sean auditables y los incidentes explicables: esencial en entornos regulados.
- Elegir entre por lotes, en línea, en flujo o en el borde según las necesidades de latencia, frescura y soberanía.
- Los modelos se degradan; la monitorización de la deriva, la calidad de datos y el deterioro no es opcional.

## Referencias y lecturas adicionales

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley y cols., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil y cols., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson y Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.

