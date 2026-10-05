# 7.5 Ciencia de la decisión y cultura basada en datos

## Presentación y motivación

La ciencia de la decisión es la práctica de conectar los datos con decisiones reales, recurriendo a la estadística, la ciencia del comportamiento y el juicio para ayudar a la gente a elegir bien bajo incertidumbre. Una cultura basada en datos es la condición organizacional en la que esto ocurre por defecto: la gente recurre a la evidencia, razona cuidadosamente sobre causa y efecto, comunica la incertidumbre con honestidad, y actualiza sus creencias cuando los datos lo justifican. Este capítulo es deliberadamente la culminación de la secuencia de datos, porque toda la estrategia, la ingeniería, la analítica y la experimentación que lo preceden no valen nada si no cambian las decisiones para mejor.

Para los equipos grandes, aquí es donde las inversiones en datos fallan con más frecuencia, no en los canales sino en la última milla de la perspectiva a la acción. Las empresas gastan fuertemente en plataformas y tableros y aun así toman decisiones importantes por jerarquía, hábito, o el presentador más confiado. Un modo de fallo común es el teatro de datos: análisis elaborados producidos para verse rigurosos mientras la decisión real se tomó de antemano y los datos se seleccionaron cuidadosamente para justificarla. El gobierno añade apuestas y escrutinio altos. Las decisiones de política justificadas por afirmaciones causales débiles pueden malasignar dinero público y dañar a la ciudadanía, y la exigencia de rendición de cuentas hace del razonamiento honesto sobre la evidencia una obligación cívica, no solo buena práctica.

Los problemas difíciles aquí son cognitivos y culturales, no técnicos. La gente confunde la [correlación con la causalidad](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation), ignora los [factores de confusión](https://en.wikipedia.org/wiki/Confounding) (variables ocultas que impulsan tanto la supuesta causa como el efecto), se ancla en el primer número que ve, y lee las estimaciones puntuales como certezas. Y en el impulso por volverse basada en datos, las organizaciones pueden derivar hacia la vigilancia: medir a los individuos tan intrusivamente que destruyen la confianza y provocan la manipulación. Construir una cultura de medición genuina significa acertar en el razonamiento, comunicar la incertidumbre con fidelidad, y medir sistemas y resultados sin convertir los datos en una herramienta de control sobre las personas.

## Principios fundamentales

- El propósito de los datos es mejores decisiones, no la producción de informes.
- Decide qué cambiaría tu opinión antes de mirar los datos.
- La correlación no es causalidad; interroga los factores de confusión antes de actuar.
- Comunica la incertidumbre con honestidad; una estimación puntual sin un rango engaña.
- Sé basado en datos, no esclavo de los datos; el juicio y el contexto todavía importan.
- Mide para aprender y mejorar sistemas, no para vigilar y castigar individuos.
- Actualiza las creencias cuando la evidencia lo justifique; cambiar de opinión es una fortaleza.
- La [seguridad psicológica](https://en.wikipedia.org/wiki/Psychological_safety) es un prerrequisito para el análisis honesto y el disenso.

## Recomendaciones

### Conecta los datos con las decisiones y evita el teatro de datos

Vincula el análisis a una decisión específica desde el principio: ¿qué haremos de manera distinta según lo que encontremos? Antes de recopilar datos, declara la decisión, las opciones, y qué evidencia favorecería a cada una, idealmente qué resultado cambiaría tu opinión. Esto protege contra el teatro de datos, donde el análisis meramente decora una decisión ya tomada. Si ningún hallazgo realista alteraría la elección, no gastes en el análisis. Toma la decisión de juicio con honestidad y dilo. Insiste en que las presentaciones lideren con la decisión y la recomendación, no con un recorrido de gráficos.

### Razona cuidadosamente sobre la causalidad

La mayoría de las preguntas de negocio y política son causales (¿producirá esta acción este resultado?), pero la mayoría de los datos disponibles son observacionales y están plagados de factores de confusión. Enseña a los equipos la diferencia entre correlación y causalidad, y las trampas: variables de confusión, [sesgo de selección](https://en.wikipedia.org/wiki/Selection_bias), causalidad inversa, y correlación espuria. Prefiere los experimentos aleatorizados para las afirmaciones causales donde sea factible. Donde los experimentos sean imposibles, usa técnicas cuidadosas de [inferencia causal](https://en.wikipedia.org/wiki/Causal_inference) y declara tus supuestos explícitamente en lugar de deslizarte de «asociado con» a «causa». Sé especialmente escéptico de una historia convincente construida sobre una única correlación.

### Comunica la incertidumbre a las partes interesadas

Los números presentados como estimaciones puntuales precisas invitan a la falsa confianza. Comunica rangos, intervalos de confianza o creíbles, y los supuestos clave detrás de cualquier cifra. Usa lenguaje claro y visuales honestos (barras de error, rangos, bandas de escenario) para que quienes toman decisiones capten qué se sabe y qué no. Distingue lo que muestran los datos, lo que infieres, y lo que asumes. Calibra la confianza a la evidencia: presenta un pronóstico basado en datos escasos exactamente como eso. La incertidumbre comunicada con honestidad construye más confianza que la falsa precisión, porque sobrevive al contacto con la realidad.

### Construye una cultura de medición sin vigilancia

Crea un entorno donde los equipos rutinariamente definan métricas de éxito, midan resultados, y aprendan de ellos, pero apunta la medición a sistemas, procesos y resultados en lugar de al monitoreo de individuos. Las métricas usadas para vigilar y clasificar a las personas se manipulan, crían miedo, y destruyen la honestidad que las buenas decisiones requieren (una dinámica capturada por la [ley de Goodhart](https://en.wikipedia.org/wiki/Goodhart's_law): una medida que se convierte en un objetivo deja de ser una buena medida). Favorece las métricas agregadas y orientadas a resultados. Involucra a los equipos en la elección de sus propias medidas, y separa las métricas de aprendizaje de la evaluación de desempeño. Protege la seguridad psicológica para que la gente saque a la luz malas noticias y disienta temprano.

### Fomenta hábitos de datos saludables y alfabetización

Eleva la alfabetización de datos ampliamente para que la gente pueda leer un gráfico críticamente, cuestionar la definición de una métrica, y detectar una afirmación engañosa. Normaliza preguntar «¿cómo sabemos eso?» y «¿qué cambiaría nuestra opinión?». Premia a la gente por actualizar sus puntos de vista a la luz de la evidencia y por ejecutar experimentos que fallan de forma informativa. Haz que sea seguro decir «los datos no nos lo dicen» en lugar de fabricar certeza. Los líderes marcan el tono: cuando cambian decisiones basándose en evidencia y admiten incertidumbre, la cultura sigue.

### Protégete contra el sesgo y el mal uso

Vigila los sesgos predecibles: el [sesgo de confirmación](https://en.wikipedia.org/wiki/Confirmation_bias) al seleccionar datos de apoyo, el [sesgo de supervivencia](https://en.wikipedia.org/wiki/Survivorship_bias) al ignorar lo que falta, anclarse en un número inicial, y el sesgo de retrospectiva en los postmortems. Incorpora la revisión de abogado del diablo, el preregistro de lo que esperas encontrar, y perspectivas diversas en los análisis importantes. Toma en serio la ética de datos (equidad, transparencia y evitar el daño), especialmente cuando las decisiones afectan el sustento, los beneficios o los derechos de las personas.

## Ventajas y desventajas

| Elección | Ventajas | Desventajas | Mejor ajuste |
|---|---|---|---|
| Impulsado por datos (los datos deciden) | Reduce el sesgo, consistente | Ignora el contexto, se manipula, frágil | Dominios bien comprendidos |
| Basado en datos (datos más juicio) | Equilibra evidencia y contexto | Más lento, requiere juicio | Decisiones complejas o novedosas |
| Experimentar para causalidad | Evidencia causal fuerte | Costoso, lento, no siempre factible | Elecciones reversibles de alto riesgo |
| Inferencia observacional | Usa los datos disponibles | Riesgo de confusión, afirmaciones más débiles | Cuando los experimentos son imposibles |
| Métricas de resultado/sistema | Impulsa la mejora, poca manipulación | Menos responsabilidad individual | Culturas de aprendizaje |
| Vigilancia individual | Visibilidad granular | Manipulación, miedo, confianza erosionada | Rara vez justificada |

La tensión definitoria es rigor frente a velocidad y factibilidad. Los experimentos aleatorizados dan la evidencia causal más fuerte, pero cuestan tiempo y a menudo son imposibles para elecciones estratégicas o de política de una sola vez, donde el juicio cuidadoso sobre los factores de confusión y los supuestos explícitos deben bastar. La segunda tensión es entre la medición y la confianza: cuanto más granularmente midas a los individuos, más puedes ver y menos comportamiento honesto obtienes. Una cultura madura se inclina hacia el juicio basado en datos y la medición agregada orientada a resultados. Acepta una precisión aparente ligeramente menor a cambio de decisiones que se sostienen y una fuerza laboral que dice la verdad.

## Preguntas para discutir con tu equipo

1. **¿Declaras qué cambiaría tu opinión antes de mirar los datos, y esa pregunta está escrita en tus documentos de decisión?** La protección más fuerte del capítulo contra el teatro de datos es nombrar la decisión, las opciones, y la evidencia que favorecería a cada una, idealmente el resultado que voltearía tu elección, antes de recopilar datos. Si ningún hallazgo realista alteraría la decisión, el movimiento honesto es saltarse el análisis y tomar la decisión de juicio abiertamente. Para empresas y agencias donde una única elección estratégica o de política puede desperdiciar más de lo que cuesta un programa entero de analítica, esta disciplina tiene alto apalancamiento. Trae una decisión reciente y pregunta si algún hallazgo podría haberla cambiado, o si los gráficos meramente decoraron una conclusión ya alcanzada. Si «¿qué cambiaría nuestra opinión?» no es una pregunta estándar en tus documentos de decisión, hazla una, e insiste en que las presentaciones lideren con la recomendación, no con un recorrido de gráficos.

2. **Cuando aparece una correlación convincente, ¿cómo interrogas los factores de confusión antes de actuar, y prefieres un experimento donde sea factible?** El capítulo advierte que la mayoría de las preguntas de negocio y política son causales mientras que la mayoría de los datos disponibles son observacionales y están llenos de factores de confusión, sesgo de selección, y causalidad inversa. Sus propios ejemplos repiten una trampa: los clientes comprometidos se autoseleccionan en una función o programa, así que la correlación en bruto con menor deserción o mayor consecución de empleo se desvanece bajo una comparación controlada. Actuar sobre esa correlación significa una campaña o política costosa y mal dirigida. Trae una decisión reciente que descansó en una única correlación y pregunta qué variable oculta podría impulsar ambos lados. Donde un experimento sea factible, prefiérelo; donde no lo sea, usa métodos cuidadosos de inferencia causal y declara tus supuestos explícitamente en lugar de deslizarte de «asociado con» a «causa».

3. **¿Tus métricas apuntan a mejorar sistemas y resultados, o a monitorear individuos, y has separado las métricas de aprendizaje de la evaluación de desempeño?** El capítulo traza una línea clara: la medición apuntada a las personas se manipula, cría miedo, y destruye la honestidad que las buenas decisiones requieren, una dinámica que la ley de Goodhart predice una vez que una medida se convierte en un objetivo. Favorece las métricas agregadas y orientadas a resultados, involucrando a los equipos en la elección de sus propias medidas, y protegiendo la seguridad psicológica para que la gente saque a la luz malas noticias temprano. Para entornos gubernamentales y empresariales, vigilar al personal de primera línea erosiona la confianza que hace posible en primer lugar los datos precisos. Trae la pregunta concreta: ¿cuáles de tus métricas podrían usarse para clasificar o castigar individuos, y la gente las manipularía bajo presión? Si las métricas de aprendizaje y la evaluación de desempeño están enredadas juntas, sepáralas, para que la medición impulse la mejora en lugar del comportamiento defensivo.

4. **Cuando un número llega a quien toma la decisión, ¿llega como un rango con sus supuestos adjuntos, o como una estimación puntual que invita a la falsa confianza?** El capítulo argumenta que la incertidumbre comunicada con honestidad construye más confianza que la falsa precisión, porque sobrevive al contacto con la realidad, sin embargo el impulso hacia una única cifra confiada es fuerte cuando un líder quiere una respuesta limpia. Para un equipo grande la presión en competencia es real: los rangos y las barras de error pueden leerse como evasivos para los ejecutivos que premian la decisión, así que los analistas aprenden a despojar las advertencias para ser escuchados. Trae un informe reciente y comprueba si distinguió lo que los datos muestran, lo que inferiste, y lo que asumiste, y si un pronóstico construido sobre datos escasos fue etiquetado exactamente como eso. En entornos empresariales y gubernamentales, donde una cifra puede terminar en un paquete para la junta, una presentación de presupuesto, o un testimonio público, una estimación puntual presentada como certeza es un pasivo, así que acuerda un estándar interno de que las cifras consecuentes lleven un rango, los supuestos clave, y una declaración clara de confianza.

5. **¿Es genuinamente seguro aquí decir «los datos no nos lo dicen», y quién tiene permitido desafiar cómo se define una métrica?** El capítulo trata la alfabetización de datos y la seguridad psicológica como prerrequisitos: la gente necesita leer un gráfico críticamente, preguntar «¿cómo sabemos eso?», y admitir incertidumbre sin penalización, o la cultura fabrica certeza falsa por defecto. La tensión para una organización grande es que la alfabetización amplia toma tiempo y presupuesto reales de capacitación, y cuestionar la métrica favorita de una persona superior puede sentirse limitante para la carrera, así que los números no examinados viajan hacia arriba sin ser desafiados. Trae evidencia sobre quién en la sala realmente puede interrogar la definición y procedencia de una métrica, y recuerda la última vez que alguien fue premiado en lugar de castigado por actualizar su punto de vista o reportar un fallo informativo. Para organismos empresariales y gubernamentales, donde una medida mal definida puede impulsar la financiación o el reporte público, nombra explícitamente quién tiene la posición para cuestionar una métrica y protégelo cuando la use.

6. **¿Cómo proteges los análisis importantes contra el sesgo predecible, y incorporas el disenso antes de una decisión en lugar de después?** El capítulo enumera las trampas que corrompen silenciosamente la evidencia: el sesgo de confirmación al seleccionar datos de apoyo, el sesgo de supervivencia al ignorar lo que falta, anclarse en un número inicial, y el sesgo de retrospectiva en los postmortems. La consideración en competencia es la velocidad, ya que la revisión de abogado del diablo, el preregistro de lo que esperas encontrar, y las perspectivas diversas todos ralentizan una decisión y son lo primero que se recorta bajo presión de plazo. Trae un análisis reciente de alto riesgo y pregunta qué habría salido a la luz si alguien hubiera sido asignado a argumentar el caso opuesto, y si el equipo escribió sus expectativas antes de ver los resultados. En contextos empresariales y especialmente gubernamentales, donde las decisiones afectan el sustento, los beneficios o los derechos de las personas, trata la ética de datos y el disenso estructurado como requisitos permanentes en los análisis consecuentes, no extras que un trimestre ocupado puede silenciosamente eliminar.

## Perspectiva sectorial

**Startup.** Sin analistas y con solo unas pocas semanas de fondos por apuesta, tu ciencia de la decisión es un hábito más que una función: antes de un compromiso grande, pregunta qué resultado cambiaría tu opinión y si un experimento barato puede responderlo más rápido que una reunión. Protégete firmemente contra apostar el trimestre a una única correlación llamativa, porque un equipo diminuto no puede recuperarse de una hoja de ruta mal dirigida. Mantenlo ligero, una línea escrita en el documento de decisión que nombre la señal que te haría detenerte, no una revisión formal que nunca ejecutarás.

**Pequeña empresa.** Probablemente no tienes un especialista en datos y compras analítica dentro de herramientas que ya usas, así que el riesgo es confiar en el tablero de un proveedor sin cuestionar cómo se define una métrica o si su comparación es justa. Gasta tu atención escasa en el razonamiento en lugar de en las herramientas: separa la correlación de la causalidad en la una o dos decisiones que realmente mueven el negocio, y declárate el rango honesto antes de comprometer efectivo que no puedes recuperar. Cuando una herramienta ofrece automatizar una decisión, mantén a una persona en el ciclo donde una decisión equivocada te costaría un cliente.

**Empresa.** A través de muchos equipos el problema es la consistencia y la gobernanza: una expectativa compartida de que los análisis nombren la decisión y los criterios de cancelación por adelantado, que las afirmaciones causales declaren sus supuestos, y que las cifras consecuentes lleven rangos en los paquetes de la junta y las auditorías. Separa las métricas de aprendizaje de la evaluación de desempeño en toda la organización para que la medición no se agrie en vigilancia y manipulación. Invierte en alfabetización de datos amplia y en prácticas de revisión como el abogado del diablo y el preregistro, para que un presentador confiado no pueda sustituir a la evidencia a escala.

**Gobierno.** La contratación pública, la transparencia y la rendición de cuentas pública elevan las apuestas en cada afirmación causal, porque una política justificada por una correlación espuria malasigna dinero público y puede dañar a la ciudadanía. Prefiere diseños de comparación rigurosos para la evaluación de programas, comunica los efectos como rangos con supuestos declarados a los organismos de supervisión, y documenta el razonamiento para que una auditoría pueda seguirlo. Apunta la medición a los resultados del programa en lugar de vigilar a los trabajadores de casos, y da al público un relato claro de cómo la evidencia moldeó la decisión.

## Ejemplos

**Startup.** Una startup en etapa previa a la Serie A notó que los usuarios que se unían a su foro comunitario desertaban mucho menos, y los fundadores estaban listos para apuntar toda la hoja de ruta a las funciones del foro. Antes de comprometerse, alguien preguntó qué cambiaría sus opiniones, y una mirada rápida mostró que los clientes ya comprometidos eran simplemente los que se molestaban en unirse al foro. Ejecutaron un pequeño experimento en lugar de apostar el trimestre a una correlación, e hicieron de «¿qué cambiaría nuestra opinión?» una pregunta estándar en sus documentos de decisión.

**Empresa.** Una firma de servicios financieros notó que los clientes que usaban una función particular tenían mucha menor deserción y casi lanzó una campaña costosa para empujar a todos hacia ella. Una revisión de ciencia de la decisión señaló el factor de confusión obvio: los clientes ya comprometidos se autoseleccionaban en la función. Un experimento controlado entonces mostró que la función en sí tenía poco efecto causal sobre la deserción. La firma evitó una gran inversión mal dirigida, y el liderazgo adoptó «¿qué cambiaría nuestra opinión?» como una pregunta estándar antes de los grandes gastos.

**Gobierno.** Una agencia pública que evaluaba un programa de empleo se resistió a afirmar el éxito a partir de la estadística en bruto de que los participantes encontraban trabajo a una tasa alta, reconociendo que las personas motivadas se autoseleccionan en tales programas. Usó un diseño de comparación riguroso y comunicó el efecto estimado como un rango con supuestos declarados a los organismos de supervisión. La medición se centró en los resultados del programa en lugar de vigilar a los trabajadores de casos, lo cual preservó la confianza de primera línea mientras aún impulsaba la rendición de cuentas y la mejora.

## Caso de negocio: motivaciones, ROI y TCO

El ROI de la ciencia de la decisión es el costo evitado de decisiones equivocadas confiadas y la calidad mejorada de las decisiones que una organización toma miles de veces. Una única elección estratégica o de política importante justificada por una correlación espuria puede desperdiciar mucho más que el costo entero de construir buenas prácticas de decisión. Una mejor calibración (saber lo que sabes y lo que no sabes) te permite dimensionar apuestas apropiadamente y evitar tanto compromisos imprudentes como la parálisis. En conjunto, una cultura basada en datos se compone: cada equipo tomando decisiones ligeramente mejores y mejor razonadas es un apalancamiento enorme.

El costo de adopción es principalmente cultural y educativo: capacitación en alfabetización de datos, tiempo para el análisis y la revisión cuidadosos, y la disposición del liderazgo a cambiar decisiones y admitir incertidumbre. Es más barato en dólares que las plataformas de capítulos anteriores pero más difícil de instalar, porque pide a la gente poderosa que se gobierne por la evidencia. Pésalo contra el costo de no adoptar: teatro de datos que desperdicia el esfuerzo analítico, decisiones impulsadas por la voz más confiada, afirmaciones causales que colapsan al contacto con la realidad, y, donde la vigilancia se afianza, una fuerza laboral que manipula métricas y oculta malas noticias. Al liderazgo, el caso es simple. Toda la inversión previa en datos solo rinde frutos si la última milla de la perspectiva a la decisión es sólida, y la ciencia de la decisión es esa última milla.

## Antipatrones y trampas

- Teatro de datos: análisis producido para justificar una decisión ya tomada.
- Deslizarse de «correlacionado con» a «causa» sin interrogar los factores de confusión.
- Presentar estimaciones puntuales como certezas, ocultando el rango de incertidumbre.
- Sesgo de confirmación: buscar solo datos que apoyen una conclusión preferida.
- Decisiones HiPPO (la opinión de la persona mejor pagada) que anulan la evidencia.
- Convertir las métricas en vigilancia individual, provocando manipulación y miedo.
- La ley de Goodhart en acción: una métrica objetivo que deja de medir lo que importa.
- Castigar a la gente por fallos informativos, matando la honestidad y la experimentación.

## Modelo de madurez

1. **Iniciar.** Las decisiones corren por jerarquía e intuición, y gana la voz más fuerte o más superior. La correlación se trata libremente como causalidad, la incertidumbre se ignora, y las pocas métricas en uso vigilan individuos y se manipulan.
2. **Desarrollar.** Algunos equipos consultan datos y muestran conciencia de las trampas causales, pero el análisis a menudo es selectivo, producido para justificar una decisión ya tomada. La incertidumbre rara vez se comunica, y las prácticas de medición son inconsistentes de equipo a equipo.
3. **Estandarizar.** La organización documenta y aplica una práctica compartida: los análisis se vinculan a una decisión nombrada con criterios predefinidos, los equipos distinguen la correlación de la causalidad y prefieren experimentos para las afirmaciones causales, los números llevan rangos y supuestos declarados, y la medición se apunta a los resultados en lugar de a los individuos, con la seguridad psicológica protegida.
4. **Gestionar.** La calidad de la decisión se mide y controla contra líneas base. La organización rastrea con qué frecuencia los análisis nombraron una señal de cancelación antes de que llegaran los datos, el porcentaje de cifras consecuentes que se enviaron con un rango comunicado, cuántas afirmaciones causales descansaron en experimentos frente a mera correlación, y si las decisiones se revirtieron por evidencia. Las prácticas de protección contra el sesgo como el preregistro y la revisión de abogado del diablo se auditan, y las métricas que empiezan a manipularse se atrapan y se retiran.
5. **Orquestar.** El razonamiento sólido se mejora continuamente y se integra en toda la organización. «¿Qué cambiaría nuestra opinión?» es rutinario antes de cualquier decisión importante, el rigor causal y la incertidumbre honesta son normas culturales, y los líderes visiblemente actualizan según la evidencia y admiten lo que se desconoce. La medición impulsa el aprendizaje sin vigilancia, las prácticas de decisión se adaptan a medida que cambian la organización y sus riesgos, y cada nivel decide mejor como resultado.

## Ideas para el debate

- ¿Dónde en tu organización se usan los datos para decorar decisiones ya tomadas?
- ¿Qué decisión reciente descansó en una correlación que podría no ser causal?
- ¿Cuán honestamente comunican tus informes la incertidumbre, y quién resiste los rangos?
- ¿Tus métricas apuntan a mejorar sistemas o a monitorear individuos?
- ¿Cuándo fue la última vez que un líder cambió visiblemente una decisión por los datos?
- ¿Cómo evitas que la búsqueda de la medición se incline hacia la vigilancia?

## Puntos clave

- El objetivo de los datos son mejores decisiones; protégete contra el teatro de datos.
- Declara qué cambiaría tu opinión antes de mirar los datos.
- Nunca confundas la correlación con la causalidad; interroga los factores de confusión y prefiere los experimentos.
- Comunica la incertidumbre con honestidad; la falsa precisión destruye la confianza cuando falla.
- Sé basado en datos, no esclavo de los datos; el juicio y el contexto todavía importan.
- Mide sistemas y resultados para aprender, no individuos para vigilar.
- Protege la seguridad psicológica para que la gente actualice creencias y saque a la luz malas noticias.

## Referencias y lecturas adicionales

- Daniel Kahneman, «Thinking, Fast and Slow».
- Judea Pearl y Dana Mackenzie, «The Book of Why».
- Douglas W. Hubbard, «How to Measure Anything».
- Nate Silver, «The Signal and the Noise».
- Cathy O'Neil, «Weapons of Math Destruction».
- Darrell Huff, «How to Lie with Statistics».
- Philip Tetlock y Dan Gardner, «Superforecasting».
- Charles Wheelan, «Naked Statistics».
