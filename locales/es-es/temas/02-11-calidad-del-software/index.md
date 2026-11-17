# 2.11 Calidad del software

## Visión general y motivación

La [calidad del software](https://en.wikipedia.org/wiki/Software_quality) mide en qué medida un sistema cumple con las necesidades declaradas y las expectativas razonables de quien lo usa. Y eso implica mucho más que preguntarse si funciona: implica que el sistema sea fiable, seguro, mantenible, usable, eficiente y adecuado a su propósito a lo largo del tiempo. La calidad es un concepto más amplio que la prueba. La prueba (capítulo 2.4) es una actividad que revela defectos; la calidad es la disciplina completa de construir la cosa correcta con excelencia y de tener, con evidencias, la certeza de haberlo hecho. Un sistema puede superar todas sus pruebas y, aun así, ser de baja calidad si es difícil de mantener, inaccesible o inadecuado a lo que los usuarios realmente necesitan.

En un equipo grande, la calidad no puede residir en la cabeza de una sola persona ni en las costumbres de un solo grupo. Cientos de ingenieros, múltiples productos y sistemas de larga vida requieren una definición compartida de calidad, procesos explícitos para asegurarla y mediciones que indiquen si mejora o se deteriora. Sin todo ello, «calidad» se convierte en una aspiración difusa que pierde ante cualquier plazo de entrega, y los defectos se acumulan hasta que todo cambio se vuelve lento y arriesgado.

En entornos empresariales y públicos, la magnitud del riesgo crece. Los sistemas regulados, de seguridad crítica o orientados al ciudadano tienen que demostrar su calidad, no simplemente declararla: procesos documentados, evidencia trazable y verificación independiente suelen ser obligatorios. La mala calidad conlleva costos directos de orden financiero, legal y reputacional, y en algunos ámbitos pone vidas en peligro. Una disciplina deliberada de calidad, edificada sobre modelos, procesos, medición y cultura, es lo que convierte la calidad de un accidente en un resultado gestionado.

## Principios fundamentales

- La calidad es la adecuación al propósito más la conformidad con los requisitos; defínase ambas de forma explícita.
- La calidad se construye, no se prueba al final: la verificación descubre defectos, pero la prevención evita que surjan.
- Distinga el [aseguramiento de la calidad](https://en.wikipedia.org/wiki/Quality_assurance) (¿son sólidos nuestros procesos?) del [control de la calidad](https://en.wikipedia.org/wiki/Quality_control) (¿es bueno este producto?).
- La verificación pregunta: «¿Lo construimos bien?». La validación pregunta: «¿Construimos la cosa correcta?».
- Mida la calidad con un conjunto reducido de indicadores significativos; trátelos como señales, no como metas.
- El costo de un defecto aumenta cuanto más tarde se detecta; por eso hay que adelantar las actividades de calidad.
- La calidad es una propiedad de toda la organización y de su cultura, no una puerta de acceso al final del proceso.

## Recomendaciones

### Adopte un modelo de calidad compartido, como la norma ISO/IEC 25010

Dote a su organización de un vocabulario común para la calidad adoptando un modelo reconocido de calidad del producto. La norma [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) define características como la idoneidad funcional, la eficiencia de rendimiento, la compatibilidad, la usabilidad, la fiabilidad, la seguridad, la mantenibilidad y la portabilidad. Úselo para hacer de la calidad una noción concreta: para cada sistema, decida qué características importan más y qué significa «suficientemente bueno» en cada una. Estas características de calidad del producto son los mismos **atributos de calidad** que orientan la arquitectura (capítulo 3.1). La calidad y la arquitectura son dos vistas de una misma preocupación, por lo que deben compartir una sola lista de prioridades, no dos listas rivales.

### Separe el aseguramiento de la calidad del control de la calidad

Trate el aseguramiento de la calidad (AC) y el control de la calidad (CC) como actividades distintas, pero complementarias. El AC tiene un enfoque procesal y preventivo: mejora la manera en que se ejecuta el trabajo mediante estándares, revisiones, criterios de completitud y formación, de modo que los defectos sean menos probables desde el origen. El CC tiene un enfoque de producto y es de naturaleza detectiva: inspecciona productos de trabajo reales, como pruebas, [revisión de código](https://en.wikipedia.org/wiki/Code_review) y auditorías, para captar los defectos que sí llegaron a introducirse. Una organización madura invierte en ambos, pero apuesta por el AC, porque prevenir un defecto cuesta mucho menos que encontrarlo y repararlo.

### Ejecute procesos explícitos de gestión de la calidad del software

Convierta la calidad en un proceso gestionado, no en una esperanza silenciosa. Para trabajos significativos, redacte un plan de calidad que establezca las características de calidad objetivo, las actividades de aseguramiento y control, los criterios de aceptación y quién es el responsable. Intégrelo en las prácticas que ya existen: la revisión de código (capítulo 2.5) como control y como vía de intercambio de conocimiento, la estrategia de pruebas (capítulo 2.4) como red de seguridad automatizada, y el [análisis estático](https://en.wikipedia.org/wiki/Static_program_analysis) como inspección continua. Revise periódicamente los datos de calidad y actúe según las tendencias, en lugar de limitarse a reaccionar ante incidentes.

### Practique la verificación y la validación como disciplinas distintas

La verificación confirma que los productos de trabajo cumplen sus especificaciones, de modo que los inputs correctos en cada etapa produzcan las salidas correctas, mediante revisiones, análisis estático y pruebas contra requisitos. La validación confirma que el sistema terminado cumple realmente las necesidades del usuario y su uso previsto, mediante pruebas con usuarios, pruebas de aceptación, pilotos y retroalimentación en campo. Se necesita ambas. Un sistema puede ser correcto respecto a una especificación defectuosa (verificado, pero no válido), o puede abordar una necesidad real y, aun así, contener defectos (válido, pero no verificado). En entornos regulados, la [verificación y validación](https://en.wikipedia.org/wiki/Verification_and_validation) independientes (V&V) por parte de un organismo distinto de los desarrolladores pueden ser un requisito.

### Mida la calidad con indicadores significativos

Elija un conjunto reducido de indicadores que reflejen tanto los resultados de calidad como sus causas impulsoras, y obsérvelos a lo largo del tiempo. Medidas útiles incluyen la densidad de defectos, la tasa de fuga de defectos (los detectados en producción frente a los encontrados antes de la publicación), el tiempo medio de detección y de reparación, la tasa de fallo por cambio, señales de salud del código como la complejidad y la duplicación, y señales de validación como los problemas reportados por usuarios y la conformidad de accesibilidad. Evite los indicadores vanidosos o manipulables: un indicador que se convierte en meta deja de medir la realidad. Acompañe las cifras con señales cualitativas provenientes de revisiones y de la retroalimentación de usuarios.

### Caracterice y gestione los defectos de forma sistemática

Trate los defectos como datos, no como fuegos que apagar. Clasifíquelos por gravedad, tipo y causa raíz. Síguelos desde su detección hasta su resolución. Busque patrones para poder prevenir su recurrencia. Emplee técnicas como el [análisis de causa raíz](https://en.wikipedia.org/wiki/Root_cause_analysis) y la categorización de defectos para distinguir los errores aislados de las debilidades sistémicas. Haga que lo aprendido retroalimente el AC, mediante estándares actualizados, pruebas añadidas y mejores revisiones, para que la misma clase de defecto no vuelva. Un defecto corregido sin comprender su causa es un defecto que se ha invitado a volver.

### Gestione el costo de la calidad de forma deliberada

Comprenda la economía de la calidad a través de las categorías clásicas: costos de prevención (formación, estándares, buen diseño, herramientas), costos de evaluación (revisiones, pruebas, auditorías) y costos de fallo (retrabajo interno antes de la publicación, más los fallos externos detectados por los usuarios, que son mucho más caros). Desplace la inversión hacia la prevención y la evaluación temprana, porque cada unidad monetaria allí invertida evita muchas más en costos de fallo más adelante. Haga visibles esos costos, para que «no tenemos tiempo para la calidad» se vea por lo que es: una decisión de gastar más en el fallo.

### Cultive una cultura de calidad

Haga de la calidad una responsabilidad de todos, asumida por los equipos que construyen el software, en lugar de delegarla en un departamento de AC aguas abajo que la inspecciona al final. Los líderes deben recompensar los resultados de calidad, crear un ambiente seguro para reportar defectos y casi-incidentes, y tratar los datos de calidad como una herramienta de aprendizaje, no como un látigo. Un enfoque sin culpas saca los problemas a la luz pronto; uno que señala culpables los oculta hasta que resultan caros.

## Compromisos: ventajas y desventajas

| Práctica / decisión | Ventajas | Desventajas |
|---|---|---|
| Modelo de calidad formal (ISO 25010) | Vocabulario compartido; prioridades explícitas | Sobrecarga si se aplica de forma dogmática |
| Fuerte aseguramiento de la calidad (prevención) | Menos defectos; menor costo total | Inversión inicial; retorno visible más lento |
| Fuerte control de la calidad (inspección) | Detecta defectos que se escapan | Costoso; encuentra defectos tarde |
| V&V independiente | Alta garantía; objetividad | Costoso; más lento; puede resultar adverso |
| Métricas de calidad abundantes | Visibilidad; alerta temprana | Riesgo de manipulación; sobrecarga de medición |
| Equipo de AC dedicado | Enfoque y especialización | Puede descargar la responsabilidad de los desarrolladores |
| Calidad asumida por los equipos | Propiedad; retroalimentación rápida | Exige disciplina y competencia en todo el equipo |

El compromiso central es la inversión frente a la garantía, condicionada por el momento temporal. La prevención cuesta ahora para evitar costos de fallo mayores en el futuro. Por eso, el nivel económicamente correcto de calidad no es el máximo, sino el punto en que el costo marginal de una garantía adicional se equipara al costo de fallo que evita. Ese punto está alto en sistemas de seguridad crítica y bajo en herramientas internas de baja criticidad. La otra tensión recurrente es la propiedad. Los grupos centrales de AC construyen especialización, pero pueden liberar a los desarrolladores de su responsabilidad. La calidad asumida por los equipos fomenta la propiedad, pero exige competencia y disciplina en todas partes.

## Preguntas para discutir con el equipo

1. **Cuando la misma clase de defecto aparece dos veces, ¿realizamos un análisis de causa raíz o simplemente lo corregimos de nuevo?** Un defecto corregido sin comprender su causa es un defecto que se ha invitado a volver, y en un equipo grande la misma causa raíz puede manifestarse en múltiples servicios antes de que nadie conecte los puntos. Tratar los defectos como datos (clasificados por gravedad, tipo y causa, y analizados en busca de patrones) es lo que distingue a un equipo que se vuelve progresivamente más fiable de uno que se mantiene ocupado corrigiendo el mismo error una y otra vez. Traiga a la reunión su gestor de defectos y busque firmas recurrentes: ¿cuántos incidentes recientes comparten una causa que nunca se abordó de forma sistémica? La respuesta debe alimentar la prevención, de modo que una causa recurrente impulse un estándar actualizado, un asistente compartido nuevo, una prueba adicional o una mejor lista de verificación, porque así es como una corrección en un punto detiene a toda una clase de defectos.

2. **¿Es seguro en nuestro equipo reportar un defecto o un casi-incidente, y qué ocurre con quien lo señala?** La calidad es una propiedad de la cultura, y un enfoque sin culpas saca los problemas a la luz pronto, mientras que uno que señala culpables los oculta hasta que resultan caros, lo que, en un sistema regulado o orientado al ciudadano, puede significar un fallo público o una sanción. Esto importa más aún a gran escala, donde el ingeniero más próximo a un riesgo suele ser de nivel junior y el incentivo para callar es fuerte. Traiga señales honestas: ¿los casi-incidentes se registran y se discuten, o desaparecen? ¿Las postmortem nombran causas o nombran personas? La acción es convertir los datos de calidad en una herramienta de aprendizaje, no en un látigo, recompensar a quienes sacan los problemas a la luz y ejecutar postmortem sin culpas, porque no se puede prevenir lo que el equipo teme reportar.

3. **¿Puede la validación realmente detener una publicación, y quién ostenta esa autoridad cuando se acerca un plazo?** La verificación (¿lo construimos bien?) y la validación (¿construimos la cosa correcta?) son disciplinas distintas, y la validación solo tiene fuerza si un fallo de accesibilidad, una prueba de acceptance fallida o una investigación de usuario reveladora pueden bloquear verdaderamente el lanzamiento. En entornos empresariales y públicos, eso suele ser obligatorio, a veces mediante verificación y validación independientes por parte de un organismo separado de los desarrolladores, y «lo publicamos de todos modos» no es una respuesta que un órgano de supervisión acepte. Traiga sus últimas publicaciones: ¿alguna señal de calidad llegó a detener una, o la barrera siempre cede ante la fecha? Si la validación nunca ha bloqueado una publicación, es decorativa, y la solución es redactar criterios de aceptación en el plan de calidad desde el inicio, designar quién toma la decisión de ir o no ir, y otorgar a esa decisión una autoridad real e independiente de la presión de entrega.

4. **¿Conocemos realmente nuestro costo de mala calidad y estamos desplazando deliberadamente el gasto del fallo hacia la prevención?** El costo de mala calidad (CMC) es el dinero perdido por retrabajo interno, incidentes en producción, correcciones de emergencia, carga de soporte, usuarios perdidos y sanciones regulatorias, y casi siempre es mayor que el gasto visible en revisiones y pruebas. En un equipo grande, los costos de fallo se dispersan entre canales de incidentes, colas de soporte y retrabajo que nadie registra como tal, por lo que permanecen invisibles hasta que alguien los suma. La tensión es que la prevención cuesta dinero ahora, en un ciclo presupuestario, para evitar costos de fallo que caen después y en el presupuesto de otra persona, lo que hace que el compromiso sea fácil de posponer indefinidamente. Traiga cifras reales: número y costo de incidentes, horas de retrabajo, tasa de fuga de defectos y la distribución actual del gasto entre prevención, evaluación y fallo, y decida si la mezcla debe desplazarse hacia lo anterior. En sistemas empresariales y de gobierno, donde la mayor parte del costo de vida se produce tras la primera publicación, ponga el CMC delante de quienes manejan el presupuesto, porque un número que un órgano de supervisión puede ver es mucho más difícil de sacrificar que un apelo vago a «la calidad».

5. **¿Cuáles de nuestras métricas de calidad se han convertido silenciosamente en metas, y qué comportamiento están impulsando ahora?** Un indicador que se convierte en meta deja de medir la realidad: perseguir un porcentaje de cobertura produce pruebas escritas para mover el número, no pruebas que detecten defectos. A gran escala esto es peligroso, porque un panel destacado compartido entre decenas de equipos fija los incentivos para todos ellos, y una métrica manipulable propaga la manipulación a la vez en todos lados. La consideración contraria es que todavía se necesita medir, así que la respuesta rara vez es «eliminar el indicador», sino «acompañarlo de un contrasinal y leerlo junto con evidencia cualitativa de revisiones y usuarios». Traiga su conjunto actual de métricas y, para cada una, pregúntese qué podría hacer alguien bajo presión para moverla sin mejorar la calidad, y si ya se ha visto que ocurre. En entornos regulados y orientados al ciudadano, sea especialmente cauto con las métricas de conformidad que parecen en verde mientras la validación subyacente (accesibilidad, resultados reales de usuarios) nunca se ejerció genuinamente, porque un auditor, eventualmente, probará la realidad detrás del número.

6. **¿Quién es el propietario de la calidad aquí: los equipos que escriben el código, o un grupo separado al final, y en qué estamos invirtiendo realmente?** La propiedad condiciona todo lo que viene después, porque un silo de AC aguas abajo permite a los desarrolladores descargar la responsabilidad del código que escriben, mientras que la calidad asumida por los equipos construye sentido de propiedad a costa de exigir competencia y disciplina en cada equipo. A gran escala esto no es un o-un-otro: el modelo sostenible suele ser que los equipos asuman la calidad a través de la revisión de código y las pruebas automatizadas, respaldados por un grupo central pequeño que mantiene los estándares, ejecuta el aseguramiento de la calidad como mejora de procesos y ofrece acompañamiento, en lugar de inspeccionar la calidad al final. Traiga un mapa honesto de dónde ocurre actualmente el trabajo de calidad, quién es responsable cuando un defecto se escapa, y dónde están realmente el presupuesto y el personal, frente a dónde dice la retórica que vive la calidad. En organizaciones empresariales y de gobierno, añada el requisito de verificación y validación independientes: algunos regímenes de garantía exigen una parte separada, por lo que decida deliberadamente qué controles pertenecen a los equipos de entrega y cuáles deben permanecer independientes para satisfacer la auditoría.

## Perspectiva por sector

**Startup.** La velocidad pesa más que el ceremonial, así que nombre las dos o tres características de calidad que en realidad protegen su producto, usualmente fiabilidad y mantenibilidad, y que el pulido espere. Que la calidad la asuma todo el equipo con revisión de código y un conjunto modesto de pruebas automatizadas, en lugar de crear un grupo de AC que no puede cubrir con personal. Cuando la misma clase de error aparece dos veces, dedique veinte minutos a un análisis rápido de causa raíz y añada un asistente compartido más una prueba, para que deje de recidivar en lugar de corregirse a mano cada vez. Ese pequeño hábito de prevención mantiene la tasa de fallo por cambio baja mientras todavía se avanza rápido.

**Pequeña empresa.** Sin un especialista en calidad dedicado y con un presupuesto ajustado, apóyese en la calidad que viene integrada en las herramientas y plataformas que compra, en lugar de en un proceso que debe ejecutar usted. Al elegir software, trate las evidencias de calidad del proveedor como parte de la compra: postura de seguridad, accesibilidad, rapidez de soporte y con qué frecuencia sus versiones rompen cosas. Registre un puñado de señales baratas y honestas (incidentes en producción, problemas reportados por clientes, tiempo de reparación) en lugar de un programa de métricas elaborado que nadie pueda mantener.

**Gran empresa.** El trabajo es lograr coherencia entre muchos equipos: adopte un modelo de calidad compartido como la ISO/IEC 25010, separe el aseguramiento de la calidad (proceso) del control de la calidad (producto) y ejecute revisiones periódicas del costo de la calidad que desplace el gasto hacia la prevención. Que la calidad siga siendo propiedad de los equipos de entrega, respaldados por un grupo central pequeño que mantiene estándares y paneles de control de la tasa de fuga de defectos, la tasa de fallo por cambio y las tendencias de salud del código. Estandarice el vocabulario y las barreras para que los equipos dejen de reinventar la práctica de calidad, pero déjelos libertad para alcanzar esas barras a su manera.

**Sector público.** La contratación, la transparencia y la rendición de cuentas ante la ciudadanía fijan el marco, por lo que redáctese los requisitos de calidad en los contratos y exíjanse evidencias documentadas y trazables, no meras afirmaciones. Espérese la verificación y validación independientes por un organismo separado de los desarrolladores, la conformidad obligatoria de accesibilidad y los registros de defectos con gravedad y causa raíz integrados en la pista de auditoría. Informe las cifras de costo de mala calidad (retrabajo, recursos de apelación, fallos de servicio) a los órganos de supervisión, y otorgue a la validación la autoridad real de bloquear una publicación que fallaría a los ciudadanos que dependen de ella.

## Ejemplos

**Startup.** Una startup de cinco personas decide que, para su producto inicial, fiabilidad y mantenibilidad son las características de calidad que importan, y deja el pulido perfecto de detalles para más adelante. La calidad es responsabilidad de todo el equipo: la revisión de código y un conjunto modesto de pruebas automatizadas son los controles, y no hay un grupo de AC al que enviar defectos. Cuando la misma clase de error aparece dos veces, dedican veinte minutos a un rápido análisis de causa raíz y añaden un asistente compartido más una prueba, para que deje de recidivar en lugar de corregirse a mano cada vez. Ese pequeño hábito de prevención mantiene su tasa de fallo por cambio baja mientras siguen a toda velocidad.

**Gran empresa.** Una gran firma de servicios financieros adopta la ISO/IEC 25010 como su vocabulario de calidad y, para cada producto, registra niveles objetivo de fiabilidad, seguridad y mantenibilidad. Los equipos asumen la calidad: la revisión de código y las pruebas automatizadas son controles en el pipeline, mientras un grupo central pequeño ejecuta el AC manteniendo estándares y ofreciendo acompañamiento. Un panel de calidad registra la tasa de fuga de defectos, la tasa de fallo por cambio y las tendencias de salud del código. Los defectos se clasifican y se analiza su causa raíz, y las causas recurrentes impulsan actualizaciones en bibliotecas compartidas y listas de verificación. La dirección revisa trimestralmente los datos de costo de la calidad y ha desplazado el gasto hacia la prevención, reduciendo tanto los incidentes en producción como el costo de repararlos.

**Sector público.** Una agencia nacional que gestiona una plataforma de prestaciones orientada al ciudadano opera bajo un régimen de garantía que exige evidencias documentadas de calidad. Ejecuta un proceso formal de gestión de la calidad con un plan de calidad por publicación, más verificación y validación independientes por un equipo separado de los desarrolladores. La verificación coteja cada producto de trabajo contra requisitos trazables a la política. La validación incluye pruebas de conformidad de accesibilidad e investigación con ciudadanos reales, y cualquiera de ambas puede bloquear una publicación. Los defectos se registran con gravedad y causa raíz como parte de la pista de auditoría, y las cifras de costo de mala calidad (retrabajo, recursos de apelación y fallos de servicio) se envían a los órganos de supervisión para justificar la inversión continua en prevención.

## Caso de negocio: motivaciones, retorno de inversión y costo total de propiedad

El retorno de la calidad es un menor costo total de propiedad y un ritmo de entrega constante. El costo de la calidad tiene dos caras. El gasto bueno, la prevención y la evaluación, es visible y controlable: diseño, estándares, revisiones, pruebas y herramientas. El costo de mala calidad es mayor, pero a menudo permanece oculto: retrabajo interno, incidentes en producción, correcciones de emergencia, soporte al cliente, usuarios perdidos, sanciones regulatorias y daño reputacional. Estudios que se remontan a *Quality Is Free* (La calidad es gratuita) de Crosby han hallado de forma consistente que el costo total de la mala calidad supera con creces al de prevenir, y que los defectos se encarecen mucho más cuanto más tarde se detecten: un problema encontrado en diseño cuesta una fracción del mismo problema encontrado en producción.

Para la dirección, el argumento no es «gastar más en calidad». Es «gastar antes para gastar menos en total». Cuantifique el CMC con sus propios datos (número y costo de incidentes, horas de retrabajo, tasa de fuga de defectos) y muestre cómo la prevención y la evaluación temprana lo reducen. Conecte la calidad con resultados de negocio: la fiabilidad retiene clientes, la mantenibilidad mantiene el cambio futuro barato, y la seguridad y la accesibilidad lo mantienen fuera de problemas legales. En sistemas empresariales y públicos de larga vida, donde la mayor parte del costo cae después de la primera publicación, las dimensiones de mantenibilidad y fiabilidad dominan el costo de vida. Eso convierte la inversión temprana en calidad en una de las decisiones de mayor palanca que puede tomar.

## Antipatrrones y trampas

- **Calidad como barrera final:** inspeccionar la calidad al final en lugar de construirla durante el proceso, de modo que los defectos se encuentran cuando son más caros.
- **Confundir la prueba con la calidad:** suponer que pasar las pruebas equivale a alta calidad, ignorando la mantenibilidad, la usabilidad y la adecuación al propósito.
- **AC como silo separado:** un equipo aguas abajo que «es propietario de la calidad», permitiendo que los desarrolladores descarguen su responsabilidad sobre el código que escriben.
- **Teatro de métricas:** perseguir porcentajes de cobertura o conteos de defectos como metas, lo que invita a la manipulación y oculta la calidad real.
- **Verificación sin validación:** construir la especificación correctamente sin comprobar nunca que la especificación responde a necesidades reales.
- **Sin análisis de causa raíz:** corregir defectos de forma aislada sin abordar la causa sistémica, de modo que la misma clase recidive.
- **Ignorar el costo de mala calidad:** tratar la calidad como un gasto puro porque los costos de fallo están ocultos y no se miden.

## Modelo de madurez

**Nivel 1 (Iniciar).** La calidad es indefinida y esporádica. Depende de la diligencia individual, se verifica en gran parte con pruebas manuales al final, y los defectos se manejan de forma reactiva a medida que surgen. No hay modelo compartido, no hay métricas y no hay línea entre aseguramiento y control.

**Nivel 2 (Desarrollar).** Aparecen prácticas básicas: revisión de código, pruebas automatizadas y un registro de defectos. Se recogen algunos datos de calidad, pero de forma irregular, y cada equipo lo hace a su manera. La calidad sigue viéndose sobre todo como prueba, la prevención es mínima, la verificación ocurre y la validación es informal.

**Nivel 3 (Estandarizar).** La organización adopta un modelo de calidad compartido (como la ISO/IEC 25010), separa el AC del CC y ejecuta procesos de gestión de la calidad con planes de calidad y criterios de aceptación, documentados y aplicados de forma consistente entre equipos. La verificación y la validación son distintas y deliberadas, y los defectos se clasifican y se les analiza la causa raíz según un esquema acordado.

**Nivel 4 (Gestionar).** La calidad se mide y controla contra líneas base. Un conjunto reducido de indicadores significativos se sigue en el tiempo (densidad de defectos, tasa de fuga de defectos, tiempo medio de detección y reparación, tasa de fallo por cambio y señales de salud del código como la complejidad y la duplicación), y el costo de la calidad se cuantifica en prevención, evaluación y fallo. Los criterios de aceptación y las barreras de calidad se aplican con base en evidencia, no en opinión, las tendencias se revisan en un calendario fijo, y la validación puede bloquear una publicación de forma genuina.

**Nivel 5 (Orquestar).** La calidad es una disciplina culturalmente asumida y en mejora continua, integrada con la planificación de negocio y de riesgo. La prevención es el énfasis, los datos de costo de la calidad guían dónde va la inversión, y los hallazgos de causa raíz previenen la recurrencia de forma sistemática. Los equipos asumen la calidad de principio a fin, los indicadores alimentan la mejora continua, y la organización adapta su práctica de calidad a medida que los productos, los riesgos y la regulación evolucionan. Esto se alinea con los niveles superiores de los modelos de madurez del capítulo 10.8.

## Ideas para el debate

- ¿Qué características de calidad de la ISO/IEC 25010 importan más para sus sistemas, y qué es «suficientemente bueno» en cada una?
- ¿En qué punto de la mezcla prevención-evaluación-fallo se sitúa su organización, y debería desplazarla?
- ¿Distinguen en la práctica entre verificación y validación, o fusionan ambas bajo «pruebas»?
- ¿La calidad es propiedad de los equipos que construyen el software o está delegada en un grupo separado, y qué cambiaría si la trasladaran?
- ¿Cuál es su verdadero costo de mala calidad, y podría medirlo con suficiente precisión como para sostener el caso de negocio?
- ¿Cuáles de sus métricas de calidad son señales genuinas y cuáles se han convertido en metas manipulables?

## Ideas clave

- La calidad es más amplia que la prueba: es la adecuación al propósito más la conformidad, a través de características como fiabilidad, seguridad y mantenibilidad.
- Use un modelo de calidad compartido (ISO/IEC 25010) para que los atributos de calidad sean explícitos y se alineen con la arquitectura (capítulo 3.1).
- Separe el aseguramiento de la calidad (prevenir, proceso) del control de la calidad (detectar, producto), y apueste por la prevención.
- Practique la verificación (se construyó bien) y la validación (se construyó la cosa correcta) como disciplinas distintas.
- Mida la calidad con pocos indicadores significativos y caracterice los defectos por gravedad y causa raíz para prevenir la recurrencia.
- Gestione el costo de la calidad: la prevención y la evaluación temprana son mucho más baratas que el fallo, especialmente en sistemas de larga vida.
- Cultive una cultura de calidad sin culpas en la que los equipos asuman la calidad, respaldados por la revisión de código (capítulo 2.5) y la estrategia de pruebas (capítulo 2.4).

## Referencias y lectura complementaria

- IEEE Computer Society, *SWEBOK Guide (Guía del cuerpo de conocimiento de la ingeniería de software)*, área de conocimiento de calidad del software.
- ISO/IEC 25010, *Ingeniería de sistemas y de software: Requisitos de calidad de sistemas y software y evaluación (SQuaRE): Modelos de calidad de sistema y de software*.
- Serie ISO/IEC 25000 (SQuaRE), *Requisitos de calidad del producto de software y evaluación*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain* (*La calidad es gratuita: El arte de hacer la calidad cierta*).
- W. Edwards Deming, *Out of the Crisis* (*Fuera de la crisis*).
- Capers Jones y Olivier Bonsignour, *The Economics of Software Quality* (*La economía de la calidad del software*).
- Gerald Weinberg, *Quality Software Management* (*Gestión de la calidad del software*).
- ISO/IEC/IEEE 12207, *Ingeniería de sistemas y de software: Procesos del ciclo de vida del software* (contexto de procesos de AC y V&V).

