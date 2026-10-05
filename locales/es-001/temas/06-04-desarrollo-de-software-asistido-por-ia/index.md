# 6.4 Desarrollo de software asistido por IA

## Visión general y justificación

Los asistentes de código con inteligencia artificial ya pueden generar código, completar funciones, redactar pruebas, explicar sistemas poco familiares y ayudar a [refactorizar](https://en.wikipedia.org/wiki/Code_refactoring). Bien utilizados, aceleran el trabajo rutinario. Abaten la barrera de entrada a lenguajes y marcos de trabajo desconocidos. Liberan al desarrollador de la carga del código repetitivo.

Mal utilizados, provocan un daño real. Pueden inundar una base de código con fragmentos que se ven plausibles pero contienen errores sutiles. Pueden abrir brechas de seguridad, generar riesgos de licencia y mermar las competencias de los ingenieros que se apoyan en ellos sin criterio. El desarrollo asistido por IA es a un tiempo una herramienta de productividad genuina y un riesgo genuino. La diferencia reside casi por completo en la disciplina de ingeniería que lo rodea.

En equipos grandes, el reto es lograr consistencia y seguridad a escala. Cuando cientos de desarrolladores emplean asistentes, los pequeños hábitos individuales se suman en resultados organizacionales. Si todos aceptan las sugerencias sin cuestionarlas, la carga de revisión y la tasa de defectos se disparan. Si, en cambio, se establecen normas claras, buenas configuraciones predeterminadas y una verificación rigurosa, esas mismas herramientas elevan la capacidad de entrega sin comprometer la calidad. La historia de la productividad, además, es más matizada de lo que sugieren las afirmaciones de los proveedores. Las ganancias reales varían enormemente según la tarea, y una medición ingenua, como contar sugerencias aceptadas, resulta engañosa.

En entornos corporativos y gubernamentales, las restricciones son aún más estrictas. El código que interactúa con sistemas regulados, manipula datos sensibles o ejecuta infraestructura crítica no puede confiarse solo porque lo produjo una IA. El origen de la licencia importa cuando el código generado puede reflejar datos de entrenamiento sujetos a licencias restrictivas. Algunas organizaciones deben mantener su código fuente en sus propias instalaciones y no pueden enviarlo a servicios externos en absoluto. Definir normas claras y ejecutables para el uso de asistencia con IA ya forma parte de una dirección de ingeniería responsable. Entre los asistentes disponibles, las herramientas construidas sobre los modelos Claude de Anthropic son una opción de referencia junto a otras; las prácticas descritas aquí aplican con cualquiera que se elija.

*Véase también:* capítulo 2.5 (revisión de código y colaboración), capítulo 2.4 (estrategia de pruebas) y capítulo 6.5 (IA responsable y de confianza).

## Principios clave

- El ingeniero, no el asistente, responde ante cada línea que se compromete en el repositorio.
- El código generado por IA es un borrador que debe revisarse y verificarse, nunca un producto terminado que puede tomarse por válido.
- El esfuerzo de verificación debe escalar con el riesgo del código, no con la confianza que transmite el resultado.
- La productividad debe medirse por resultados que importan (valor entregado, calidad, tiempo de ciclo), no por conteo de sugerencias.
- Protegerse de riesgos de seguridad y de licenciamiento que el código generado puede introducir.
- Preservar y desarrollar la competencia del ingeniero humano; no dejar que los asistentes la vacíen de contenido.
- Ser transparentes sobre dónde y cómo se emplea la asistencia con IA.

## Recomendaciones

### Emplear la programación asistida como herramienta de borrador y exploración

Orientar a los asistentes hacia tareas donde brillan y donde los errores son baratos de detectar: código repetitivo, andamiaje de pruebas, conversiones de formato, explicación de código poco familiar y exploración de enfoques. Tratar su产出 como un primer borrador. Permanecer en el asiento del conductor. Leer, comprender y editar cada sugerencia en lugar de aceptarla en piloto automático. En dominios poco conocidos, usar el asistente para aprender, pero contrastar sus afirmaciones con documentación autorizada. Los asistentes pueden inventar interfaces de programación y describir un comportamiento de manera errónea con total seguridad.

### Revisar, probar y verificar el código generado por IA como entrada de confianza cuestionada

Conceder al código generado por IA la misma escrutinización que se le daría al código de un integrante nuevo del equipo, o incluso más. Un revisor humano debe comprenderlo lo suficiente como para poder explicarlo y mantenerlo en el tiempo. «La IA lo escribió» nunca es una respuesta aceptable a «¿por qué funciona esto?». Exigir pruebas y tener especial cuidado con las pruebas generadas por IA que simplemente asientan el comportamiento actual en lugar del comportamiento esperado. Ejecutar [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis), escaneos de seguridad y comprobaciones de dependencias. En código de alto riesgo (autenticación, [criptografía](https://en.wikipedia.org/wiki/Cryptography), lógica financiera, sistemas de seguridad), tratar el resultado de la IA como un punto de partida que exige verificación experta por parte de un humano, nunca como autoridad.

### Medir la productividad con honestidad y establecer expectativas realistas

Evitar métricas de vanidad como la tasa de aceptación o las líneas generadas. Fijar la mirada en señales de entrega y calidad a lo largo del tiempo: tiempo de ciclo, tasa de fallo por cambio, tasa de defectos que escapan a producción y percepción de efectividad reportada por los propios desarrolladores. Las ganancias son reales pero desiguales: grandes para algunas tareas, insignificantes o incluso negativas para otras. El tiempo ahorrado en redactar código puede perderse de nuevo en revisarlo y depurarlo. Ajustar las expectativas ante la dirección en consecuencia, para que la inversión se sostenga en la evidencia y no en el hype, y para que ningún equipo sufra presión de aceptar sugerencias inseguras solo para cumplir una métrica.

### Gestionar los riesgos de seguridad y de licenciamiento

Escanear el código generado en busca de vulnerabilidades y patrones inseguros. Los asistentes pueden reproducir formas de codificación inseguras heredadas de sus datos de entrenamiento. Nunca pegar credenciales, contraseñas ni datos sensibles en los prompts enviados a servicios externos. Preferir herramientas que cumplan los requisitos de manipulación de datos, incluido el despliegue en las propias instalaciones o en entornos privados cuando el código fuente no pueda salir del perímetro. Atender también el tema de la licencia: el código generado puede asemejarse a material licenciado presente en los datos de entrenamiento, por lo que deben usarse herramientas y políticas que reduzcan ese riesgo, conservar el rastro de procedencia donde sea posible y derivar cualquier caso dudoso a revisión legal. Seguir el rastro de procedencia de las dependencias que el asistente sugiere, ya que puede recomendar paquetes abandonados o maliciosos.

### Establecer normas de equipo, transparencia y mantenimiento de competencias

Publicar orientaciones claras sobre cuándo y cómo puede emplearse la asistencia con IA, qué datos no deben compartirse en ningún caso y qué nivel de verificación exige cada grado de riesgo. Fomentar la transparencia sobre las contribuciones asistidas por IA allí donde importan para la revisión y la responsabilidad. Mantener afiladas las competencias humanas con intención deliberada. Asegurar que los ingenieros, sobre todo los junior, sigan aprendiendo los fundamentos en lugar de externalizar su comprensión. Rotar a las personas por tareas que construyan experiencia profunda y tratar el exceso de dependencia como un riesgo real a largo plazo para la capacidad del equipo.

## Compensaciones: ventajas y desventajas

| Dimensión | Beneficio de la asistencia con IA | Riesgo de la asistencia con IA |
|---|---|---|
| Velocidad | Código repetitivo y borradores más rápidos | Tiempo perdido revisando código incorrecto |
| Incorporación | Entrada más fácil a nuevos lenguajes o marcos | Comprensión superficial, APIs inventadas |
| Calidad | Más pruebas, refactorizaciones más rápidas | Código plausible pero con errores sutiles |
| Seguridad | Puede sugerir correcciones y escanear | Puede introducir vulnerabilidades |
| Competencias | Libera tiempo para tareas de mayor valor | Erosiona los fundamentos si se abusa |
| Licenciamiento | Reutilización más rápida de patrones comunes | Riesgo en procedencia y exposición a licencias |

La compensación central es la velocidad frente a la verificación. La IA desplaza el esfuerzo de escribir a revisar. El saldo neto depende de si las prácticas de revisión y verificación son lo bastante sólidas para captar lo que el asistente hace mal. Una revisión débil conduce a la degradación de la calidad. Una revisión fuerte y normas claras capturan la ventaja.

## Preguntas para debatir en el equipo

1. **¿Qué partes de nuestra base de código están fuera de toda asistencia con IA y cómo garantizamos ese límite?** La confianza uniforme es una trampa: aplicar el mismo escrutinio ligero a la autenticación, la criptografía, la lógica financiera y los sistemas de seguridad que al código repetitivo es la forma en que los errores sutiles y plausibles alcanzan las rutas críticas. Para un equipo grande, una lista explícita de módulos excluidos o reservados a revisión experta convierte el juicio individual en un salvaguarda organizacional. Traer el mapa de riesgos de la base de código, la política vigente (si la hay) y cómo se impedirá en la práctica que el código generado llegue a un módulo restringido: controles en el pipeline, reglas de propiedad o puertas de revisión. En entornos de defensa, regulados o de seguridad crítica, ciertos módulos deben excluir la asistencia con IA de forma total. La respuesta debe escalar el esfuerzo de verificación al riesgo del código, nunca a la confianza con que el resultado se presenta.

2. **¿Cuáles son las tendencias reales de fallo por cambio y de defectos escapados desde que adoptamos los asistentes, y las estamos midiendo o las estamos suponiendo?** Las afirmaciones de productividad de los proveedores y los conteos de aceptación son métricas de vanidad que engañan, porque el tiempo ahorrado en redactar código puede perderse de nuevo en revisarlo y depurarlo. Para que la dirección invierta en base a la evidencia y no al hype, hacen falta señales de entrega y calidad a lo largo del tiempo: tiempo de ciclo, tasa de fallo por cambio, tasa de defectos que escapan y percepción de efectividad por parte de los desarrolladores. Traer los datos reales que se tengan y ser honesto donde no los haya. El riesgo a vigilar es que los equipos, presionados por cumplir una métrica, acepten sugerencias inseguras. La respuesta debe sustituir el conteo de sugerencias por medidas de resultado y establecer expectativas en las que las ganancias son reales pero desiguales: grandes para unas tareas, negativas para otras.

3. **Si el código generado reproduce material con licencia restrictiva de los datos de entrenamiento o introduce una dependencia riesgosa, ¿quién lo detecta y cuándo?** El código generado puede asemejarse a material licenciado o recomendar paquetes abandonados o maliciosos, y esa exposición se incorpora al producto con o sin que nadie la haya notado. En entornos corporativos y gubernamentales, la procedencia de licencias y el riesgo de la cadena de suministro tienen peso legal que un «la IA lo escribió» no sostiene. Traer los controles actuales de detección de secretos, verificación de licencias y rastreo de procedencia de dependencias, e identificar en qué punto del pipeline opera cada uno. Discutir qué mecanismo deriva el código dudoso a revisión legal y quién asume esa decisión. Si los secretos pueden pegarse en herramientas externas o si los paquetes no verificados pueden integrarse sin cuestionamiento, cerrar esas lagunas antes de escalar el uso de asistentes en el equipo.

4. **¿Cómo evitamos que los ingenieros, sobre todo los junior, externalicen su comprensión hacia el asistente en lugar de aprender los fundamentos?** La atrofia de competencias es un riesgo lento que no aparece en la velocidad de este trimestre y que, años después, se manifiesta en un equipo incapaz de depurar, diseñar o revisar sin un prompt. En una organización grande, la tensión es real: los asistentes permiten a los ingenieros junior entregar más rápido hoy, y la presión de cumplir metas de entrega compite con el trabajo más lento de construir experiencia profunda. Traer evidencia sobre cómo crecen realmente las personas: qué proporción de junior puede explicar el código que integraron, cuánto problema sin asistencia exige aún el proceso de incorporación y si las revisiones detectan comprensión superficial o simplemente dan por bueno un resultado que funciona. Rotar deliberadamente a las personas por tareas que construyan maestría y tratar el exceso de dependencia como un riesgo de capacidad, no como una deficiencia personal. En el sector público y en sistemas críticos de larga vida útil, la plantilla puede necesitar construir y verificar sistemas durante décadas sin herramientas del proveedor, de modo que una ruta de formación que garantice el dominio directo de los fundamentos es un requisito de continuidad, no una concesión.

5. **¿Qué asistentes estamos autorizados a emplear dados los requisitos de ubicación del código fuente y los datos, y cómo impedimos que un secreto llegue nunca a un prompt?** Los requisitos de manipulación de datos determinan la herramienta antes que la productividad: un asistente que transmite el código fuente a un servicio externo puede quedar descartado de entrada, cualquiera que sea su capacidad. En un equipo grande, la tensión es entre la conveniencia de la mejor herramienta alojada y el requisito de que el código propietario, las credenciales y los datos sensibles nunca salgan del perímetro. Traer el mapa de clasificación de datos, las opciones de despliegue que ofrece cada herramienta candidata (alojada, privada, en las propias instalaciones) y los controles concretos que impiden que los secretos lleguen a un prompt: escaneo antes del commit, filtrado de prompts y formación del equipo. Decidir qué herramientas son válidas para qué clase de código y hacer que el límite sea ejecutable, no meramente orientativo. En entornos regulados, de defensa o clasificados, un despliegue en las propias instalaciones o en un entorno aislado de red puede ser la única opción conforme a la normativa, y enviar código fuente a cualquier servicio externo debe prohibirse y bloquearse técnicamente, no solo desaconsejarse.

6. **¿Cómo convertimos hábitos individuales dispersos en normas organizacionales coherentes y quién es responsable de la política a medida que evolucionan las herramientas?** Cuando cientos de desarrolladores improvisan cada uno su propio enfoque, los pequeños hábitos se acumulan en resultados organizacionales, y es la verificación inconsistente la que deja pasar defectos y exposiciones. La consideración opuesta es la autonomía: los equipos resienten mandatos centralizadores pesados, pero un libre albedrío produce calidad desigual y ninguna salvaguarda compartida. Traer la orientación actual (si la hay), evidencia de su nivel de cumplimiento y una propuesta de buenas configuraciones predeterminadas integradas en el pipeline para que el camino seguro sea el camino fácil. Nombrar un responsable que mantenga la política al día, ya que los asistentes cambian cada pocos meses, y una norma de divulgación para que los revisores sepan cuándo la asistencia con IA ha dado forma a una contribución. Para una empresa o entidad pública, vincular las normas a la auditoría y la rendición de cuentas: un estándar documentado y aplicado que un auditor puede inspeccionar vale más que una práctica no escrita que varía por equipo y desaparece cuando se va una persona clave.

## Perspectiva por sector

**Startup.** Con un puñado de ingenieros y sin margen para desperdiciar, recurrir a asistentes alojados para código repetitivo, pruebas y marcos de trabajo poco familiares, y dejar que aceleren el trabajo rutinario. Mantener una regla innegociable: un humano que comprende el cambio revisa cada integración, porque una línea sutilmente incorrecta en una base de código de cinco personas no tiene dónde esconderse ni a nadie más que la detecte. Añadir un detector de secretos y una verificación de licencias desde el principio; son de coste mínimo y evitan errores caros que no se pueden permitir reparar después.

**Pequeña empresa.** Probablemente no hay un especialista en seguridad y el presupuesto es ajustado, por lo que preferir asistentes integrados en herramientas ya de confianza antes que una instalación a medida que habrá que mantener. Enmarcar el riesgo en términos simples: nunca pegar datos de clientes ni credenciales en un prompt externo, y tratar el código generado que toca facturación o autenticación como un borrador a verificar, no como una respuesta final. Elegir proveedores cuyos términos de manejo de datos se puedan leer de verdad y cuyas funciones de IA puedan desactivarse si se comportan mal.

**Empresa.** El problema es la consistencia y la seguridad a lo largo de muchos equipos: normas compartidas por nivel de riesgo, revisión humana obligatoria y escaneos en el pipeline, y métricas honestas de entrega y calidad en lugar de conteos de aceptación. Estandarizar las elecciones de herramienta y el modelo de despliegue para que el código propietario permanezca dentro del perímetro, presupuestar el coste de revisión y corrección que los asistentes trasladan a los revisores y excluir o restringir explícitamente los módulos de alto riesgo. Gestionar la asistencia con IA como una capacidad gobernada con un responsable, no como un mosaico de hábitos individuales.

**Sector público.** Las normas de adquisición, la transparencia y la rendición de cuentas pública condicionan cada decisión. Preferir despliegue en las propias instalaciones o en entornos privados donde el código fuente y los datos sensibles no puedan salir del perímetro, prohibir el envío de código a servicios externos y exigir la divulgación de contribuciones asistidas por IA para que las decisiones sean auditables. Mandatar escaneos de seguridad y de licencias en todo el código generado, excluir la asistencia con IA de módulos de seguridad crítica y clasificados y mantener una ruta de formación que asegure que la plantilla pública pueda construir y verificar sistemas sin herramientas del proveedor a lo largo de la vida útil de los sistemas que gestiona.

## Ejemplos

**Startup.** Una startup de SaaS de seis ingenieros adoptó asistentes de código con IA para acelerar el trabajo rutinario. Recurrió a ellos para código repetitivo, pruebas y código de marcos poco familiares, pero mantuvo la regla firme de que un humano que comprendía el cambio debía revisar cada solicitud de integración y añadió un detector de secretos y una verificación de licencias al pipeline. En el código de facturación y autenticación, los ingenieros trataron la salida de la IA como un borrador grueso a verificar línea por línea, no como algo confiable. Vigilaron el tiempo de ciclo y los defectos escapados en lugar de contar sugerencias aceptadas, y mantuvieron las ganancias sin dejar que la calidad se resintiera.

**Empresa.** Una gran compañía de comercio electrónico desplegó asistentes de código con IA con salvaguardas. Prohibió los secretos en los prompts. Exigió la revisión humana, con el revisor en la obligación de comprender el código. Añadió escaneo de seguridad en el pipeline y optó por un despliegue privado para que el código propietario nunca saliera de su entorno. Midió el impacto mediante el tiempo de ciclo y la tasa de fallo por cambio en lugar de los conteos de aceptación. Encontró ganancias sólidas en código repetitivo y pruebas, pero exigió revisión experta para el código de pago, donde trató la salida de la IA como de confianza cuestionada.

**Sector público.** Una organización de software de defensa permitió la asistencia con IA únicamente a través de una herramienta en las propias instalaciones que mantenía el código clasificado y sensible dentro de su perímetro. Prohibió el envío de código fuente a cualquier servicio externo. Exigió la divulgación de contribuciones asistidas por IA en la revisión de código y mandató escaneos de seguridad y de licencias en todo el código generado. Excluyó por completo la asistencia con IA de ciertos módulos de seguridad crítica. Los ingenieros junior siguieron una ruta de formación que les aseguraba el dominio directo de los fundamentos, de modo que la plantilla no perdiera la capacidad de construir y verificar sistemas sin asistencia.

## Justificación empresarial: motivaciones, retorno de la inversión y coste total de propiedad

La motivación es la entrega más rápida y la reducción de la carga rutinaria, para que el talento de ingeniería, escaso de por sí, se concentre en el diseño, el juicio y los problemas difíciles. El retorno se manifiesta como una reducción del tiempo de ciclo para tareas adecuadas y una mejora en la experiencia del desarrollador, pero solo allí donde la verificación sostiene la calidad. Las afirmaciones de retorno basadas en el conteo de sugerencias son engañosas y deben rechazarse.

El coste total de propiedad incluye la licencia de la herramienta, el despliegue seguro o en las propias instalaciones, el escaneo de seguridad y de licencias, y el a menudo subestimado coste de revisar y corregir la salida de la IA. El coste de *no* adoptar es competitivo: los pares pueden entregar más rápido y atraer al talento que espera disponer de herramientas modernas. El coste de adoptar sin cuidado es la erosión de la calidad, incidentes de seguridad y exposición legal. Presentar el caso ante la dirección con un piloto que mida resultados reales de entrega y calidad, acompañado de un plan concreto de normas, verificación y protección de datos.

## Antipatrónes y trampas

- **Aceptación en piloto automático.** Comprometer sugerencias sin leerlas ni comprenderlas.
- **Métricas de vanidad.** Juzgar el éxito por la tasa de aceptación o las líneas generadas.
- **Secretos en prompts.** Pegar credenciales o datos sensibles en herramientas externas.
- **Confiar en pruebas de la IA.** Aceptar pruebas generadas que fijan el comportamiento actual en lugar del comportamiento esperado.
- **Ignorar la procedencia.** Pasar por alto los riesgos de licencia y de dependencias en el código generado.
- **Atrofia de competencias.** Dejar que los junior externalicen su comprensión y nunca aprendan los fundamentos.
- **Confianza uniforme.** Aplicar el mismo escrutinio bajo a código de seguridad crítica que al código repetitivo.

## Modelo de madurez

1. **Iniciación.** Los individuos usan asistentes de forma ad hoc y reactiva; no hay política ni medición; los secretos y la propiedad intelectual corren riesgo, y el código generado se integra con el escrutinio que cada persona le dé por casualidad.
2. **Desarrollo.** Existen orientaciones básicas de uso y reglas de datos, y se ejecuta algún escaneo de seguridad, pero la práctica es inconsistente entre equipos: la profundidad de verificación varía según la persona, las afirmaciones de productividad son anecdóticas y el código de alto riesgo no se restringe de forma fiable.
3. **Normalización.** Las normas por nivel de riesgo están documentadas y aplicadas en toda la organización: revisión humana obligatoria, escaneos de seguridad y de licencias en el pipeline, despliegue seguro o en las propias instalaciones donde sea necesario, prácticas de divulgación y una lista explícita de módulos excluidos o reservados a revisión experta.
4. **Gestión.** La práctica se mide y controla frente a líneas de base: el tiempo de ciclo, la tasa de fallo por cambio y la tasa de defectos que escapan se registran antes y después de la adopción; el coste de revisión y corrección se cuantifica; los incidentes de filtración de secretos y de exposición a licencias se contabilizan; y las decisiones de adopción o ampliación de herramientas se toman en base a esa evidencia, no a afirmaciones del proveedor.
5. **Orquestación.** La asistencia con IA se mejora de forma continua y se integra en toda la organización: la verificación está integrada en el pipeline como el camino predeterminado, el desarrollo de competencias es deliberado y trazable, la política se actualiza a medida que las herramientas cambian cada pocos meses, y la organización reevalúa, sustituye y delimita de nuevo el alcance de los asistentes a medida que la evidencia y el panorama de riesgos evolucionan.

## Ideas para la reflexión

- ¿Cómo deben diferirse los requisitos de verificación entre el código repetitivo y el código de seguridad crítica?
- ¿Qué métricas de productividad reflejan de verdad el valor de la asistencia con IA en su contexto?
- ¿Cuándo, en su caso, deben divulgarse las contribuciones asistidas por IA?
- ¿Cómo se previene la erosión de competencias, especialmente en los ingenieros junior?
- ¿Qué requisitos de manipulación de datos determinan qué herramientas se pueden usar?
- ¿Cómo se gestionan los riesgos de licenciamiento y procedencia del código generado?

## Conclusiones fundamentales

- El ingeniero sigue siendo el responsable; la salida de la IA es un borrador de confianza cuestionada que debe verificarse.
- Escalar la verificación al riesgo, y nunca confiar en código de seguridad crítica generado por IA sin revisión experta.
- Medir resultados reales de entrega y calidad, no conteos de sugerencias.
- Protegerse de los riesgos de seguridad, filtración de datos y licenciamiento con políticas y herramientas.
- Establecer normas claras y preservar deliberadamente la competencia de ingeniería humana.

## Referencias y lecturas adicionales

- Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (sobre expectativas realistas y medición).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (sobre la comprensión frente al artefacto de código).
- Titus Winters, Tom Manshreck y Hyrum Wright, *Software Engineering at Google*.
- GitClear y estudios sectoriales afines sobre tendencias de calidad del código asistido por IA.

