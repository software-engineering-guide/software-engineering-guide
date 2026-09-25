# 2.15 Depuración de código y diagnóstico de fallos

## Panorama y motivación

Depurar es el oficio metódico de descubrir por qué un sistema se comporta de un modo incorrecto, y diagnosticar es esa misma habilidad aplicada a un sistema en producción bajo presión temporal. Ambas son la [método científico](https://en.wikipedia.org/wiki/Scientific_method) aplicado a los defectos: se observa un comportamiento inesperado, se formula una hipótesis sobre su causa, se diseña un experimento que pueda confirmarla o refutarla, y se deja que la evidencia, no la intuición, determine qué cambiar. Practicada así, la depuración es una destreza ingenieril que se puede aprender y enseñar. Practicada como folklore, se convierte en superstición: se cambian líneas al azar, se reinician servidores y se reza.

Para un equipo grande, la diferencia tiene un coste enorme. Un único defecto complejo puede atrapar a ingenieros de varios servicios, consumir turnos de guardia y paralizar una liberación. Cuando cada persona depura por instinto, ese esfuerzo no se acumula, porque nadie puede reproducir ni explicar lo que otro ya intentó. Cuando el equipo comparte un método (reproducir primero, aislar por búsqueda, capturar el fallo en una prueba que falle y, entonces, corregirlo), ese mismo esfuerzo se convierte en un proceso reproducible y en una suite de regresión que crece. La depuración se enlaza estrechamente con la estrategia de pruebas (capítulo 2.4), con la calidad del software (capítulo 2.11) y con los hábitos de construcción (capítulo 2.9) que hacen que el código sea, en primer lugar, diagnósticable.

En entornos empresariales y de sector público, los riesgos se elevan. Los defectos empresariales cruzan fronteras de servicios y de equipos, de modo que quien ve el síntoma rara vez es quien posee la causa. Los sistemas del sector público añaden restricciones que la mayoría de los ingenieros nunca encuentra: entornos aislados sin conexión de red, donde no se puede adjuntar un depurador a producción; compilaciones reproducibles que deben diagnosticarse a partir de artefactos; y registros de auditoría que deben documentar qué se cambió y por qué. En los tres casos, la meta es la misma: sustituir la suposición por la evidencia.

## Principios fundamentales

- **Reproducir antes de teorizar.** Un fallo que no se puede provocar a demanda es un rumor, no un defecto.
- **Depurar es contrastar hipótesis.** Se enuncia lo que se cree, y luego se diseña el experimento más barato que podría demostrar que se está equivocado.
- **Leer primero el error y la traza de pila.** El sistema suele indicar dónde se rompió antes de cambiar una sola línea.
- **Buscar en el espacio del problema, no recorrerlo.** Dividir a la mitad la región sospechosa en cada paso en lugar de leer de arriba a abajo.
- **Reducir al mínimo.** Despojar el caso hasta que solo quede el disparador esencial.
- **Un cambio a la vez.** Las ediciones en salvasocorro destruyen la evidencia que habría indicado cuál cambio importaba.
- **Capturar el defecto en una prueba que falle antes de corregirlo.** La corrección solo se demuestra cuando esa prueba pasa y se mantiene en verde.
- **Hallar la causa raíz, no el síntoma más cercano.** Un parche que oculta el síntoma deja el defecto listo para volver.

## Recomendaciones

### Reproducir el defecto de forma fiable antes de cambiar nada

La primera tarea es obtener una reproducción fiable: un conjunto de pasos o un caso automatizado que provoque el fallo a demanda. Sin ella, no se puede distinguir una corrección real de una coincidencia, porque el síntoma puede aparecer y desaparecer por razones que nunca se controlaron. Fijar con precisión los datos de entrada, el entorno, las versiones y el momento exacto. Si el fallo es intermitente, buscar la variable oculta que lo hace surgir (un registro de datos concreto, un umbral de reloj, una petición concurrente) hasta que la reproducción sea fiable. Una reproducción fiable es el artefacto de mayor valor en la depuración, porque todo lo que venga después se vuelve medible.

### Leer el error, los registros y la traza de pila antes de tocar código

Antes de formular una sola teoría, leer lo que el sistema ya dijo. La [traza de pila](https://en.wikipedia.org/wiki/Stack_trace) (el registro de la cadena de llamadas en el instante del fallo) suele nombrar el archivo, la línea y la secuencia que fallaron. El mensaje de la excepción, las líneas de registro a su alrededor y los valores en el ámbito actual reducen la búsqueda antes de haber cambiado nada. Los ingenieros pierden horas teorizando sobre causas que la traza de pila ya descartó en la primera línea. Tratar la salida del error como el primer testigo, leerla con atención y completitud, y solo entonces decidir qué investigar.

### Aislar mediante búsqueda binaria del espacio del problema

No recorrer el código de arriba a abajo. Buscarlo. Aplicar la [búsqueda binaria](https://en.wikipedia.org/wiki/Binary_search_algorithm): encontrar un punto donde el estado aún es correcto y otro donde ya es incorrecto, comprobar el punto medio y repetir, reduciendo la región sospechosa a la mitad en cada iteración. Esto convierte una búsqueda de mil líneas en diez preguntas. Cuando la regresión apareció a lo largo de un rango de commits, aplicar la misma idea al historial con bisección: `git bisect` recorre el rango de commits y se marca cada revisión como correcta o incorrecta hasta que señala el cambio exacto que introdujo el defecto. Automatizar la prueba de correcto/incorrecto y que la bisección se ejecute sola.

### Reducir a un ejemplo mínimo reproducible

Una vez que se puede provocar el fallo, reducirlo. Un [ejemplo mínimo reproducible](https://en.wikipedia.org/wiki/Minimal_reproducible_example) es el conjunto más pequeño de datos de entrada y de recorrido de código que sigue fallando: eliminar datos, funciones y pasos hasta que cualquier eliminación adicional haga que el fallo desaparezca. Reducir no es un trabajo gratuito; cada elemento que se elimina es una causa que se ha descartado, y el caso mínimo suele señalar directamente al defecto. Cuando la entrada es grande o estructurada, automatizar la reducción con [depuración por delta](https://en.wikipedia.org/wiki/Delta_debugging) (*delta debugging*), un algoritmo que elimina sistemáticamente fragmentos de una entrada que falla para encontrar el subconjunto mínimo que la provoca. Un ejemplo pequeño y autónomo es también el mejor informe de fallo para entregar a otro equipo.

### Instrumentar con registros y, después, usar un depurador interactivo

Ajustar la herramienta al problema. Los registros y la instrumentación selectiva son mejores cuando se necesita observar el comportamiento a lo largo del tiempo, entre procesos, o en un entorno que no se puede pausar. Un depurador interactivo, que permite poner puntos de interrupción, avanzar línea por línea e inspeccionar el estado en vivo, es el mejor recurso cuando se puede ejecutar el código en local y es necesario observar una ejecución concreta con detalle. Añadir instrumentación como un experimento deliberado ligado a una hipótesis, no como declaraciones sueltas de impresión por la pantalla, y eliminarla o elevarla a registro estructurado permanente una vez resuelto el defecto. En producción, recurrir a la depuración guiada por observabilidad: eventos de alta cardinalidad y trazas distribuidas (capítulo 9.2) permiten seguir una misma petición a través de muchos servicios, lo que suele ser la única forma de depurar un sistema distribuido al que no se puede adjuntar un depurador.

### Escribir una prueba que falle para capturar el defecto antes de corregirlo

Antes de escribir la corrección, escribir una prueba que falle a causa del defecto. Esto cumple tres funciones a la vez: demuestra que se comprende realmente la causa, define con exactitud qué significa «corregido», y se convierte en una salvaguarda permanente. Entonces se aplica la corrección y se observa cómo la prueba pasa. Esa prueba se une ahora a la suite como una barrera de [pruebas de regresión](https://en.wikipedia.org/wiki/Regression_testing), de modo que el mismo defecto no pueda regresar sin que se note. Esta práctica enlaza la depuración directamente con la estrategia de pruebas (capítulo 2.4): cada fallo difícil que se resuelve deja la suite más fuerte de lo que estaba, y una prueba inestable recibe el mismo tratamiento (reproducir la no determinismo y luego guardarse contra ella) en lugar de una anotación de reintento.

### Hallar la causa raíz y mantener el análisis exento de culpabilizaciones

Corregir el síntoma no es corregir el fallo. Rastrear el fracaso hasta su origen verdadero, preguntando el porqué en cada capa hasta llegar a una causa que pueda eliminarse y no solo enmascararse. Para los defectos que alcanzaron producción, realizar un análisis de causa raíz exento de culpabilizaciones como parte de la gestión de incidentes (capítulo 9.3): centrarse en las condiciones de sistema y de proceso que permitieron que el defecto llegara y sobreviviera, nunca en la persona que escribió la línea. La culpa hunde la información, y la depuración vive de la información. El resultado es tanto una corrección como un cambio en la forma en que esa clase de defecto se detecta antes la próxima vez.

## Compromisos: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Registros e instrumentación | Funciona en producción y en sistemas distribuidos; captura el comportamiento a lo largo del tiempo | Ruido, coste y proliferación de registros; puede alterar los tiempos de los defectos temporales |
| Depurador interactivo | Inspección precisa del estado en vivo; rápido para fallos locales | Inútil en producción restringida o aislada de red; puede enmascarar defectos de concurrencia |
| Disciplina de reproducir primero | Convierte la suposición en medición; permite una prueba que falle | Lento al inicio; algunos fallos son genuinamente difíciles de provocar |
| Búsqueda binaria y bisección | Aislamiento rápido, incluso en código desconocido | Exige una prueba fiable de correcto/incorrecto; difícil cuando los fallos interactúan |
| Reducción por depuración de delta | Reduce entradas enormes automáticamente al disparador | Coste de configuración; asume que el fallo es determinista |
| Corregir el síntoma ya | Restaura el servicio con rapidez bajo presión | Deja la causa raíz lista para volver; acumula deuda |

La tensión central es entre velocidad y certeza. Ante un incidente de producción, puede ser necesario detener la hemorragia primero (un *rollback* o un parche sintomático) para restablecer el servicio, y eso es legítimo. El error es quedarse en eso. Resolver la tensión separando las dos tareas: mitigar con rapidez para proteger a los usuarios, y luego reproducir, hallar la causa raíz y añadir la barrera de regresión antes de dar por cerrado el defecto. Una corrección sintomática sin seguimiento es un defecto con el que se ha decidido volver a encontrarse.

## Preguntas para debatir con el equipo

1. **Cuando alguien se enfrenta a un fallo difícil, ¿qué es lo primero que hace y es reproducir o suponer?** La respuesta honesta revela si el equipo tiene un método compartido o si hay un despacho lleno de folklores personales. Pedir a cada persona que narre en voz alta su último defecto difícil: ¿obtuvo una reproducción fiable primero, o empezó a cambiar código y a reiniciar cosas? Un equipo que reproduce primero puede pasar un fallo de persona a persona, porque la reproducción viaja; un equipo que supone no puede, porque cada intento es irrepetible. Esto importa más a medida que el equipo crece, ya que quien ve el síntoma tiende a no ser quien puede corregirlo. Si el hábito predeterminado es suponer, acordar como norma reproducir primero y hacer de una reproducción limpia el requisito para abrir un ticket de defecto.

2. **¿Los fallos que se corrigen vuelven, y se sabría si lo hicieran?** Un defecto que regresa es un defecto cuya causa raíz nunca se eliminó y cuya corrección nunca estuvo resguardada por una prueba. Recopilar los incidentes y los tickets reabiertos del último trimestre y contar cuántos fueron repeticiones o parientes cercanos de fallos anteriores. Cada repetición es evidencia de que el equipo parchó un síntoma, saltó la prueba que falla o detuvo el análisis de causa raíz demasiado pronto. La solución es una regla: ningún defecto se cierra hasta que una prueba que fallaba con el comportamiento antiguo pasa con el nuevo y se integra en la suite. Traer un fallo recurrente reciente y preguntar qué barrera lo habría detectado, porque esa barrera es lo que faltó.

3. **¿Se pueden depurar los sistemas de producción, dado cómo se está permitido intervenir en ellos?** En entornos empresariales y, sobre todo, del sector público, a menudo no se puede adjuntar un depurador, no se puede reproducir con datos reales y no se puede modificar un sistema en ejecución sin un registro de auditoría. Si la única técnica de depuración es un depurador interactivo en local, se está ciego justo donde están los fallos más difíciles. Preguntar qué evidencia deja realmente un fallo en producción: registros estructurados, trazas distribuidas (capítulo 9.2), volcados de memoria o artefactos de compilación reproducible. Decidir ahora qué es imprescindible capturar por defecto para que un incidente futuro sea diagnósticable, porque no se puede añadir instrumentación a un fallo que ya ocurrió. En entornos regulados, comprobar que la misma huella también cumple con las obligaciones de auditoría.

4. **Cuando un incidente de producción obliga a detener la hemorragia con rapidez, ¿cómo se garantiza que la causa raíz se descubre después?** Ante un incidente, un *rollback* o un parche sintomático es la primera medida correcta para proteger a los usuarios, pero el peligro es que el ticket se cierre en el momento en que el servicio se restablece y el defecto subyacente nunca se diagnostica. Para un equipo grande, aquí es donde se acumula la deuda de forma invisible, porque la misma clase de fallo reaparece en otro servicio y con otro ingeniero de guardia meses después. Revisar los últimos incidentes de gravedad máxima y comprobar cada uno: ¿siguió la mitigación con una reproducción, un análisis de causa raíz y una barrera de regresión, o la historia acabó en «servicio restablecido»? Acordar una regla explícita de que un incidente mitigado permanece abierto hasta que la causa raíz se comprende y se protege, y designar quién es responsable de ese seguimiento. En entornos empresariales y del sector público, vincular esto con el proceso de gestión de incidentes (capítulo 9.3) para que la revisión postincidente sea un paso obligatorio y auditable, no una cortesía que se pierde cuando estalla el siguiente incendio.

5. **¿Qué parte de un fallo se puede reconstruir a posteriori, y quién decidió qué se captura por defecto?** No se puede instrumentar un fallo que ya sucedió, de modo que la diagnósticabilidad de cualquier incidente queda fijada de antemano por los registros, trazas, métricas y volcados que se eligió emitir. La consideración contrapuesta es el coste y el ruido: los eventos de alta cardinalidad y la trazabilidad completa no son gratuitos, y el exceso de registro sepulta la señal mientras infla el almacenamiento y, en contextos regulados, la exposición en la retención de datos. Tomar un incidente real reciente, examinar qué evidencia dejó y trabajar hacia atrás para identificar lo que se habría querido capturar y cuánto costaría mantenerlo. Decidir deliberadamente qué señales están activas por defecto y cuáles son muestreadas o de opt-in, y registrar esa decisión para que sea una política, no una casualidad. Para un sistema empresarial o del sector público, añadir quién es responsable de ese presupuesto de observabilidad y si la huella capturada también cumple con las obligaciones de auditoría, privacidad y residencia de datos.

6. **¿Se trata la depuración como una destreza enseñada y medible, o los nuevos ingenieros la absorben por ósmosis?** La depuración es aprendible, pero la mayoría de los equipos nunca la enseñan de forma explícita, de modo que los juniors heredan el folklore que esté más cerca y el método de reproducir primero se difunde de forma desigual o no se difunde. La tensión es que la enseñanza deliberada (trabajar en conjunto en fallos difíciles, redactar hallazgos postincidente, seguir métricas) consume tiempo de los seniors que siempre parece necesario en otra parte. Traer dos cifras al debate: la tasa de defectos recurrentes y el tiempo hasta el diagnóstico, porque si no se pueden medir, no se puede saber si el método mejora o se degrada. Considerar si la incorporación incluye un ejercicio real de depuración y si los hallazgos de causa raíz realmente alimentan la detección temprana. En una organización grande o pública, una práctica de depuración documentada y medida también se convierte en evidencia del rigor ingenieril que auditores, reguladores y organismos de supervisión exigen cada vez más.

## Enfoque por sector

**Startup.** Con un puñado de ingenieros y sin holgura, el objetivo es hacer que los fallos sean baratos de reproducir e imposibles de olvidar, no construir un proceso pesado. Apoyarse en `git bisect`, una reproducción rápida en local y una prueba que falle por cada defecto corregido, porque ese hábito cuesta minutos y evita pagar dos veces por el mismo defecto mientras se intenta desplegar. Omitir los postmortem formales, pero nunca saltarse la prueba de regresión: es el único artefacto lo bastante pequeño como para permitírselo siempre y lo bastante valioso como para conservarlo siempre.

**Pyme.** Probablemente no hay un especialista dedicado a fiabilidad u observabilidad y el presupuesto de herramientas es ajustado, por lo que conviene priorizar lo que el stack ya ofrece: trazas de pila legibles, registros estructurados y la trazabilidad integrada en los marcos y servicios gestionados que se contratan. Al evaluar una plataforma nueva, pesar cuánto facilitan el diagnóstico de los fallos, porque una herramienta barata que oculta qué ocurrió cuesta mucho más en tiempo de suposición que la licencia ahorrada. Reproducir primero y un cambio a la vez son disciplinas gratuitas que rinden más rápido cuando a nadie le sobran horas.

**Empresa.** Los fallos complejos cruzan fronteras de servicios y de equipos, de modo que quien ve el síntoma rara vez posee la causa, y un método compartido importa más que la habilidad de cualquier individuo. Estandarizar reproducir primero, el aislamiento por búsqueda binaria, una prueba que falle antes de la corrección y postmortem exentos de culpabilizaciones entre equipos, e invertir en trazas distribuidas (capítulo 9.2) para que una petición pueda seguirse a través de servicios. Gestionar la depuración como una capacidad medible: seguir la tasa de defectos recurrentes y el tiempo hasta el diagnóstico, y devolver los hallazgos de causa raíz a la detección temprana para que la misma clase de fallo no recorra el mapa de servicios.

**Sector público.** Las normas de contratación, los entornos restringidos y la responsabilidad pública condicionan cómo se puede depurar. A menudo no se puede adjuntar un depurador a producción ni copiar datos de ciudadanos a un portátil, por lo que se debe diseñar para el diagnóstico desde lo que está permitido: compilaciones reproducibles, registros sintéticos en un enclave aislado y registros y trazas estructuradas capturadas por defecto. Registrar cada paso de diagnóstico y cada cambio en la huella de auditoría, y exigir que los proveedores expongan suficiente telemetría y reproducibilidad de compilación para investigar fallos de forma independiente, en lugar de depender de la palabra del proveedor.

## Ejemplos

**Startup.** Un equipo de cuatro ingenieros ve repetidamente que el checkout falla para una fracción de usuarios, pero nunca en pruebas. En lugar de suponer, un ingeniero captura una reproducción fiable reproduciendo el *payload* exacto de la petición fallida y luego lee la traza de pila que venía ignorando, que apunta a una llamada de análisis de fechas. Un `git bisect` rápido sobre los commits de la semana señala el cambio que cambió la librería de fechas. Escriben una prueba que falla con la marca de tiempo problemática, corrigen el analizador, ven la prueba pasar y la mantienen en la suite. La investigación completa tarda una tarde porque reprodujeron antes de teorizar, y el fallo no vuelve.

**Empresa.** Una plataforma de pagos observa tiempos de espera intermitentes que ningún equipo individual puede explicar, porque el síntoma aparece en el checkout y la causa vive a tres servicios de distancia. Los ingenieros de guardia usan trazas distribuidas (capítulo 9.2) para seguir una petición fallida a través de las fronteras de servicios y descubren una llamada aguas abajo que a veces se bloquea bajo carga concurrente, una clásica [condición de carrera](https://en.wikipedia.org/wiki/Race_condition) donde el resultado depende de un tiempo desafortunado entre hilos. Lo reproducen con una prueba de carga, lo capturan en una prueba de integración que falla, corrigen el bloqueo y realizan un postmortem exento de culpabilizaciones (capítulo 9.3) que añade un *span* de trazado y una alerta para que la próxima ocurrencia se detecte en minutos, no en días.

**Sector público.** Una agencia de prestaciones ejecuta su sistema de expedientes en un entorno aislado de red donde los ingenieros no pueden adjuntar un depurador a producción ni copiar datos de ciudadanos a sus portátiles. Un defecto de cálculo surge en la conciliación. El equipo depura desde lo que el entorno permite: registros estructurados, una compilación reproducible que pueden montar en un enclave de prueba aislado y registros sintéticos que recrean el caso fallido. Cada paso de diagnóstico se registra en la huella de auditoría, la corrección se entrega con una prueba que pasa de rojo a verde como evidencia, y el análisis de causa raíz alimenta una nueva verificación previa a la liberación. Como la reproducción usó datos sintéticos, ningún registro de ciudadano salió del perímetro.

## Argumento empresarial: motivaciones, retorno y coste total

El retorno de una depuración disciplinada se mide en horas de ingeniero no gastadas en suposiciones y en defectos que no vuelven. Un fallo intermitente sin diagnosticar puede consumir días de tiempo de seniors y escalaciones repetidas de guardia; un método de reproducir primero lo convierte en una tarea acotada y delegable, y el hábito de la prueba que falla impide que el mismo defecto facture otra vez el próximo trimestre. En una organización grande, el efecto compuesto de no volver a pagar por el mismo fallo es sustancial, y mejora directamente la tasa de fallo de cambios y el tiempo medio de recuperación que la dirección ya sigue.

El coste total de propiedad es sobre todo formación y herramienta, y es modesto. Se necesitan convenciones compartidas (reproducir primero, un cambio a la vez, una prueba que falle antes de la corrección), depuradores y trazas ya presentes en la cadena de herramientas, y la inversión en observabilidad descrita en el capítulo 9.2. El coste mayor y oculto es la alternativa: una cultura de superstición donde los ingenieros aplican cambios en salvasocorro, los síntomas se parchean y vuelven, y la carga de guardia crece sin límite. Solo reducir la sobrecarga de guardia a menudo justifica la inversión, y el argumento para la dirección se expresa más fácilmente como menos incidentes recurrentes y una recuperación más rápida a cambio de un coste único en hábitos e instrumentación.

## Antipatrones y riesgos

- **Depuración en salvasocorro:** cambiar muchas cosas a la vez, de modo que ni siquiera una corrección enseña algo sobre la causa.
- **Corregir sin reproducir:** declarar la victoria sobre un fallo que nunca se pudo provocar a demanda.
- **Ignorar la salida del error:** teorizar sobre causas que la traza de pila ya descartó.
- **Parche sintomático:** silenciar el síntoma mientras la causa raíz sobrevive y regresa.
- **Proliferación de impresiones de depuración:** salidas de depuración sueltas dejadas en el código, que añaden ruido en lugar de ser un experimento ligado a una hipótesis.
- **Saltarse la prueba de regresión:** corregir el fallo pero no dejar barrera, de modo que puede volver en silencio.
- **Reintentar pruebas inestables:** ocultar la no determinismo con reintentos en lugar de depurar la condición de carrera subyacente o el [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), un defecto que cambia o desaparece en cuanto se intenta observar.
- **Postmortem con culpabilizaciones:** castigar al autor, lo que hunde la información de la que depende la depuración.

## Modelo de madurez

- **Nivel 1, Iniciar:** La depuración es folklore individual y reactiva. Los ingenieros suponen, aplican cambios en salvasocorro y reinician. Los fallos se corrigen en el síntoma, las reproducciones son escasas y los mismos defectos se repiten. La producción es apenas diagnósticable, y nadie puede pasar un fallo a otra persona porque ningún intento es repetible.
- **Nivel 2, Desarrollar:** Algunos ingenieros reproducen de forma fiable, leen trazas de pila y usan depuradores, pero la práctica es inconsistente y varía de persona a persona y de equipo a equipo. Los registros existen, pero son ruidosos y no estructurados. Las correcciones a veces van acompañadas de una prueba que falla, a veces no, y el análisis de causa raíz solo ocurre cuando alguien insiste.
- **Nivel 3, Estandarizar:** Reproducir primero, aislar por búsqueda binaria, un cambio a la vez y una prueba que falle antes de la corrección son normas de equipo documentadas y aplicadas en toda la organización. La bisección y la reducción por depuración de delta son prácticas habituales. La producción cuenta con registros estructurados y trazas (capítulo 9.2), y los postmortem exentos de culpabilizaciones (capítulo 9.3) son la respuesta estándar ante todo defecto que escape.
- **Nivel 4, Gestionar:** La práctica de depuración se mide y controla frente a líneas base. La tasa de defectos recurrentes, el tiempo hasta el diagnóstico, el número de tickets reabiertos y el porcentaje de correcciones que se desplegaron con una prueba de regresión se siguen por equipo y se revisan en un calendario fijo. La reproducción y la finalización de la causa raíz se tratan como puertas de paso y no como buenas intenciones, y las tendencias frente a la línea base orientan la inversión en herramientas, formación y observabilidad.
- **Nivel 5, Orquestar:** La depuración es una destreza enseñada e integrada con la calidad (capítulo 2.11) y la gestión de incidentes (capítulo 9.3), y todo el ciclo se adapta de forma continua. La observabilidad se diseña de modo que la mayoría de los fallos en producción sean diagnósticables sin depurador, cada fallo resuelto fortalece la suite de regresión, y los hallazgos de causa raíz alimentan la detección temprana para que las clases de defecto se prevengan y no se vuelvan a diagnosticar. La organización reequilibra el esfuerzo a medida que sus sistemas y modos de fallo evolucionan, y la tasa de defectos recurrentes sigue bajando.

## Ideas para la reflexión

1. ¿Qué proporción de los fallos recientes se reprodujeron de forma fiable antes de que nadie tocara el código, y qué dice esa proporción sobre el método del equipo?
2. Cuando aparece una regresión, ¿el equipo recurre a la bisección o lee código a mano hasta que alguien lo encuentra?
3. ¿Cuánto se puede diagnosticar en el sistema de producción hoy, y qué se daría por haber capturado sobre un fallo que ya sucedió?
4. ¿Las correcciones se despliegan de forma consistente con una prueba que pasa de rojo a verde, y si no, dónde se rompe esa disciplina?
5. ¿Cómo se manejan las pruebas inestables: se depura la no determinismo o se tapona con reintentos?
6. ¿Se enseña la depuración de forma deliberada a los nuevos ingenieros o se les deja absorber folklore por ósmosis?

## Principales conclusiones

- Depurar es contrastar hipótesis: reproducir de forma fiable, leer el error y la traza de pila, y luego aislar por búsqueda binaria y bisección en lugar de recorrer.
- Reducir el fallo a un ejemplo mínimo reproducible, usando depuración por delta para entradas grandes, porque cada elemento eliminado es una causa descartada.
- Ajustar la herramienta al problema: instrumentación y trazas para producción y sistemas distribuidos (capítulo 9.2), depuradores interactivos para la investigación en local.
- Escribir una prueba que falle para capturar el defecto antes de corregirlo, de modo que la corrección se demuestre y el defecto quede resguardado para siempre (capítulo 2.4).
- Hallar y eliminar la causa raíz, realizar postmortem exentos de culpabilizaciones (capítulo 9.3) y tratar la depuración como una destreza aprendible, no como folklore.
- Cambiar una cosa a la vez; los cambios en salvasocorro y los parches sintomáticos destruyen la evidencia e invitan al defecto a regresar.

## Referencias y lectura complementaria

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller y Ralf Hildebrandt, «Simplifying and Isolating Failure-Inducing Input» (el algoritmo de depuración por delta)
- Brian W. Kernighan y Rob Pike, *The Practice of Programming* (capítulo sobre depuración)
- Andrew Hunt y David Thomas, *The Pragmatic Programmer* (capítulos sobre depuración y aserciones)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (capítulo sobre depuración)
- John Regehr, «Reducers Are Fuzzers» y escritos relacionados sobre reducción de casos de prueba
- Charity Majors, Liz Fong-Jones y George Miranda, *Observability Engineering* (depuración en producción con telemetría de alta cardinalidad y trazas)
- Betsy Beyer, Chris Jones, Jennifer Petoff y Niall Richard Murphy, eds., *Site Reliability Engineering* (postmortem exentos de culpabilizaciones y depuración en producción)

