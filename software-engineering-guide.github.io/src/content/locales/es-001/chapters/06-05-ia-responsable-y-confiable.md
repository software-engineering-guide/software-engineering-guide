# 6.5 Inteligencia artificial responsable y fiable

## Visión general y motivación

La inteligencia artificial responsable y fiable consiste en diseñar y operar sistemas de IA que sean equitativos, transparentes, responsables, seguros y respetuosos con la privacidad. También implica poder demostrar todo ello a las personas afectadas y a los organismos reguladores. A medida que la IA asume decisiones que condicionan la vida de las personas (contrataciones, concesión de préstamos, determinación de prestaciones) , la pregunta ya no es solo «¿funciona?», sino «¿es correcto y podemos justificarlo?». Un sistema que es preciso en promedio puede ser injusto con un subgrupo, incomprensible para quien lo padece o inseguro ante un mal uso. La confianza se gana abordando estas dimensiones de forma deliberada, no confiando en que se resuelvan solas.

En equipos grandes, la IA responsable no puede ser tarea de una sola persona ni un casillero que se marca al final del proceso. Debe integrarse en el diseño, la evaluación, la implantación y la gobernanza de los sistemas, con responsabilidades claras y vías de escalado bien definidas. A gran escala, sesgos menores y lagunas de supervisión afectan a muchísimas personas. Un solo fallo mediático puede dañar la reputación y provocar la intervención de la ley. Los marcos de gobernanza existen precisamente porque las buenas intenciones improvisadas no escalan.

Las administraciones públicas y las organizaciones sujetas a regulación tienen obligaciones vinculantes. La normativa emergente, como el [Reglamento de IA de la Unión Europea](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), establece requisitos graduados según el nivel de riesgo. Estándares como el Marco de Gestión de Riesgos de IA del NIST y la norma ISO/IEC 42001 ofrecen metodologías estructuradas para cumplirlos. Las instituciones públicas deben evitar la discriminación contraria a derecho, ofrecer vías para impugnar decisiones automatizadas y ser transparentes sobre el uso de la IA en el ejercicio de las funciones públicas. En estos contextos, la IA responsable es a la vez un deber ético y una exigencia jurídica.

*Véase también:* capítulo 6.1 (Estrategia y preparación en IA), capítulo 10.5 (Ética, rendición de cuentas e interés público) y capítulo 4.5 (Privacidad y protección de datos).

## Principios fundamentales

- La equidad es un objetivo de diseño que debe medirse y gestionarse, no darse por sentado.
- Las personas afectadas por decisiones de IA tienen derecho a una explicación y a un medio para impugnarlas.
- La responsabilidad recae en las personas y en la organización, nunca en el modelo.
- La privacidad y la seguridad deben diseñarse desde el origen, incluida la protección contra el mal uso y el abuso.
- La gobernanza debe seguir marcos reconocidos para que sea defendible y auditable.
- La supervisión humana debe ser significativa, con autoridad real para anular y detener el sistema.
- Hay que considerar los costes más amplios de la IA, incluido su impacto ambiental.

## Recomendaciones

### Detectar y mitigar sesgos e inequidades

Defina qué significa equidad en su contexto. Existen varias definiciones matemáticas, a veces contradictorias, y la adecuada depende de la decisión y del marco legal aplicable. Pruebe los modelos en busca de diferencias de rendimiento entre grupos protegidos y vulnerables, con datos representativos. Hágalo antes de la implantación y siga haciéndolo después, porque el [sesgo](https://en.wikipedia.org/wiki/Algorithmic_bias) puede surgir a medida que las poblaciones evolucionan. Mitíguelo con mejores datos, recodificación de pesos, restricciones o cambiando la forma en que se emplea el sistema, y documente los compromisos que aceptó. Eliminar un atributo protegido no elimina el sesgo, pues los sustitutos siguen operando. Trate la equidad como una disciplina continua de medición y gestión, no como una verificación puntual.

### Proporcione explicabilidad, interpretabilidad y transparencia

Adapte el nivel de explicación a la magnitud de la decisión y al destinatario. En decisiones de alto impacto, ofrezca a las personas afectadas un motivo claro, en lenguaje accesible, que puedan comprender y sobre el que puedan actuar. Para la gobernanza interna, conserve suficiente [interpretabilidad](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) técnica para depurar y defender el sistema. Prefiera modelos intrínsecamente interpretables cuando el riesgo es alto y la interpretabilidad es alcanzable. Cuando los modelos complejos sean inevitables, utilice técnicas de explicación siendo honesto sobre sus limitaciones. Sea transparente sobre cuándo se está empleando IA, especialmente en la interacción con la ciudadanía.

### Gobierne con marcos reconocidos

Adopte un enfoque de gobernanza estructurado en lugar de inventar uno propio. El **Marco de Gestión de Riesgos de IA del NIST** organiza el trabajo en torno a gobernar, contextualizar, medir y gestionar el riesgo de IA. El **Reglamento de IA de la UE** clasifica los sistemas por nivel de riesgo e impone obligaciones proporcionales, con requisitos estrictos para usos de alto riesgo. La **ISO/IEC 42001** define un sistema de gestión de IA que puede auditarse y certificarse. Alinee sus sistemas con estos marcos. Mantenga documentación como fichas de modelo y fichas de datos (resúmenes normalizados que recogen propósito, rendimiento y limitaciones de un modelo o conjunto de datos). Realice evaluaciones de riesgo antes de la implantación y conserve un inventario de sistemas de IA con su nivel de riesgo y sus responsables. Una buena gobernanza asigna roles, competencias de decisión y vías de escalado con claridad.

### Garantice supervisión humana, responsabilidad y recurso de apelación

Mantenga a un ser humano en control efectivo de las decisiones de alto impacto, con autoridad real y la información necesaria para anular la decisión del sistema, no como un mero trámite. Asigne una responsabilidad clara: nombre a la persona que responde ante la sociedad por el comportamiento de cada sistema. Conceda a las personas afectadas por decisiones automatizadas el derecho a una explicación y un procedimiento operativo para apelar ante un humano que pueda modificar el resultado. Registre las decisiones y sus fundamentos para poder tramitar recursos y auditorías de forma justa y expedita.

### Proteja la privacidad, la seguridad y frente al mal uso

Minimice los datos personales que recoge y utiliza, establezca una base jurídica y aplique técnicas de privacidad adecuadas a la sensibilidad de la información. Realice pruebas con un [equipo rojo](https://en.wikipedia.org/wiki/Red_team) (un grupo que simula ataques) antes y después de la implantación para detectar formas de manipulación, elusión de salvaguardas o uso que cause daño, y corrija lo que encuentre. Establezca medidas contra la generación de contenido dañino, la fuga de datos sensibles o la facilitación de abuso. Planifique para incidentes: monitorización, respuesta y divulgación. Considere el [doble uso](https://en.wikipedia.org/wiki/Dual-use_technology) (la misma capacidad al servicio de fines benévolos y perversos) y los usos indebidos a valle, no solo el uso previsto.

### Tenga en cuenta el coste ambiental

La formación y la inferencia de modelos de gran tamaño consumen una cantidad considerable de energía y agua. mida y reporte la huella de los principales trabajos de IA. Prefiera modelos y hardware más eficientes cuando cumplan con las necesidades del caso. Ajuste el tamaño del modelo a la tarea en lugar de recurrir por defecto al más grande, y integre el coste ambiental en las decisiones de arquitectura y adquisición.

## Dilemas: ventajas e inconvenientes

| Tensión | Un extremo | El otro extremo |
|---|---|---|
| Precisión vs. equidad | Máxima precisión media | Resultados equitativos entre grupos |
| Rendimiento vs. interpretabilidad | Modelos complejos y potentes | Modelos explicables y defendibles |
| Automatización vs. supervisión | Eficiencia y escalabilidad | Control y responsabilidad humana |
| Utilidad de los datos vs. privacidad | Modelos más ricos con más datos | Minimización y protección de datos |
| Capacidad vs. seguridad | Funcionalidad amplia y abierta | Comportamiento restringido y vigilado |
| Velocidad vs. gobernanza | Implante rápido | Revisión y documentación rigurosas |

Rara vez hay solución sin contrapartida. Mejorar la equidad puede costar algo de precisión. La interpretabilidad puede sacrificar rendimiento. La gobernanza consume tiempo. El camino responsable es tomar estos compromisos de forma consciente, documentarlos y, cuando el riesgo es alto, inclinarse por las personas afectadas y la defensibilidad. Presentar la gobernanza como un freno a la innovación es una falsa dicotomía. El riesgo de IA sin gestionar es en sí mismo una amenaza para la innovación sostenible.

## Pautas para el debate en equipo

1. **¿Qué sistemas de IA en funcionamiento clasificaría el Reglamento de IA de la UE como de alto riesgo, y estamos cumpliendo hoy esas obligaciones?** La legislación graduada por riesgo ya es vinculante, no hipotética, y un sistema que decide contrataciones, préstamos o prestaciones puede conlleva requisitos estrictos que ya podríamos estar incumpliendo. En una organización grande, esta pregunta obliga a un inventario honesto en lugar de la cómoda suposición de que la gobernanza «ya está cubierta». Presente su lista de sistemas de IA con sus niveles de riesgo y responsables, contrastada con el Reglamento de IA de la UE, el Marco de Gestión de Riesgos de IA del NIST y la ISO/IEC 42001, según proceda. La señal de alarma es cualquier sistema de alto impacto sin clasificación de riesgo, sin evaluación de impacto y sin ficha de modelo ni de datos. En instituciones públicas que ejercen funciones de autoridad, incumplir obligaciones no es un pendiente de agenda: es una exposición jurídica, y la respuesta debe activar las evaluaciones y la documentación que esos sistemas exigen.

2. **Cuando uno de nuestros modelos deniega algo a alguien, ¿esa persona puede obtener un motivo comprensible y llegar a un humano que realmente pueda revertir la decisión?** El derecho a la explicación y un recurso de apelación operativo son lo que distingue a una IA responsable de una caja negra que daña a las personas sin ofrecerles ningún recurso. La equidad medida en promedio puede seguir fallando al individuo, y la interpretabilidad añadida después del despliegue suele ser una mera apariencia. Tome una decisión concreta ya implantada y trazúla: el motivo que recibe la persona afectada, el canal de apelación y si la persona que lo resuelve tiene autoridad real y el registro suficiente para anular. En entornos públicos y regulados, la vía de recurso es a menudo un requisito legal, no una cortesía. Si el motivo es ininteligible o la apelación desemboca en una mera formalidad, ese es el hueco que debe cerrarse antes de la siguiente versión.

3. **¿Quién es la persona concreta y nombrada que responde cuando un modelo causa daño, y tiene realmente autoridad para detenerlo?** La responsabilidad recae en personas y en la organización, nunca en el modelo, pero ese principio es vacío hasta que se asocia a cada sistema un nombre y esa persona puede, de hecho, activar el interruptor. En un equipo grande, la responsabilidad difusa significa que, cuando aparece un fallo de equidad o una elusión de salvaguardas, todos suponen que otro vigila. Presente su mapa de responsabilidades, sus vías de escalado y evidencia de que la supervisión es significativa: ¿el responsable nombrado recibe la información y la autoridad para anular o detener el sistema, o solo asiente? Discutan cómo se realizan las pruebas con equipos rojos para descubrir mal usos y abusos que aún no se han imaginado, porque probar solo el uso previsto pasa por alto los fallos que acaban en titulares. La respuesta debe dejar sin ningún sistema de alto impacto a un responsable que pueda detenerlo.

4. **Para cada modelo de alto impacto, ¿qué definición de equidad elegimos, quién la aprobó y sostienen realmente los indicadores de subgrupo en producción?** La equidad tiene varias definiciones matemáticas que se contradicen entre sí: un modelo que cumple con tasas de falsos positivos iguales puede violar la igualdad de resultados, y elegir una definición es un juicio de valor que no debe dejarse a quien escribe el bucle de entrenamiento. En un equipo grande, un valor por defecto no examinado esconde la elección dentro del código y hace que cada grupo downstream herede una decisión que nadie debatió. Presente la métrica de equidad que optimizaron, los grupos protegidos y vulnerables en los que probaron, los datos representativos utilizados y la deriva observada desde el lanzamiento, ya que eliminar un atributo protegido no elimina los sustitutos que mantienen vivo el sesgo. En entornos corporativos y públicos, nombre a la persona con autoridad para aceptar un compromiso de equidad y documentarlo, porque un regulador o un defensor del pueblo preguntará quién decidió que esa definición de equidad era la adecuada para quienes se les denegó un préstamo, una prestación o un empleo. Si no se monitorean indicadores de subgrupo tras el despliegue, considere el modelo como no medido, no como justo.

5. **¿Con cuántos datos personales mínimos puede operar cada sistema, y lo hemos sometido a pruebas con equipo rojo para el mal uso y el doble uso que preferiríamos no contemplar?** La privacidad y la seguridad deben diseñarse desde el origen, y el modo más eficaz de reducir tanto el riesgo de brecha como la superficie de ataque es recopilar y retener menos datos desde el principio, aunque los equipos suelen acumular entradas «por si acaso sirven más adelante». En una organización grande, cada campo adicional es una cuestión de base jurídica, una obligación de retención y un objetivo más valioso para un atacante o para una elusión. Presente el inventario de datos y la base jurídica de cada sistema, los resultados de las pruebas de equipo rojo frente a manipulación, filtración y generación de contenido dañino, y una lista honesta de capacidades de doble uso donde la misma función que ayuda a un usuario legítimo también sirve a quien actúa de mala fe. En contextos regulados y públicos, vincule todo esto con su plan de respuesta a incidentes: monitorización, actuación y divulgación, porque una institución pública que filtra datos sensibles o publica un sistema susceptible de elusión enfrenta deberes estatutarios, no solo la incomodidad de la noticia. Si las pruebas con equipo rojo solo ejercitaron la vía prevista, lo que probaron fue la demostración, no el sistema.

6. **¿Medimos y asumimos la huella ambiental de nuestros principales trabajos de IA, o «elegir el modelo más grande» es un coste por defecto que nadie ve?** La formación y la inferencia de modelos de gran tamaño consumen energía y agua reales, y recurrir por defecto al modelo más grande para tareas que uno menor resolvería convierte un atajo de ingeniería en un coste recurrente que la organización nunca visualiza en sus paneles. En un equipo grande que gestiona muchos trabajos, las ineficiencias menores por llamada se acumulan hasta configurar una huella que se convierte en un problema de adquisición y de reporting a medida que se intensifican las expectativas de divulgación. Presente la huella medida de sus cargas de trabajo más intensivas, una comparación de tamaños de modelo frente a la precisión que la tarea realmente exige y las opciones de hardware e inferencia que podrían ajustarse. En entornos corporativos y públicos, conecte esto con los compromisos de sostenibilidad y los criterios de adquisición, ya que las instituciones públicas cada vez más deben reportar su impacto ambiental y justificar el gasto, y una huella no medida es una cifra que algún día se les pedirá y no podrán presentar. Decidan si el coste ambiental es un factor formal en la elección de modelo o reconozcan que hoy no lo es.

## Perspectiva sectorial

**Startups.** No pueden plantear un comité de gobernanza, así que apliquen la versión ligera que aun así cuenta. Elijan modelos interpretables cuando la decisión sea de alto impacto, redacten una ficha de modelo de una página, prueben resultados diferenciados entre los grupos que pueden medir y registren las decisiones para poder revisar la equidad a medida que crezcan. Toda decisión desfavorable debe tener un motivo claro y una vía de revisión humana. Omitir esto no es agilidad: es un pasivo que no pueden permitirse si una sola decisión injusta llega a la prensa o a un regulador.

**Pequeñas empresas.** Sin un especialista dedicado, trate la IA responsable como una cuestión de compra: prefiera proveedores que documenten pruebas de equidad, ofrezcan fichas de modelo y de datos, y permitan informar al cliente cuando hay IA en juego. Sepa qué datos personales recogen sus herramientas y si tienen una base jurídica para usarlos. Cuando una respuesta automatizada incorrecta pueda dañar a un cliente, mantenga a una persona en el bucle en lugar de confiar en una herramienta que no puede inspeccionar ni explicar.

**Grandes empresas.** El reto es la gobernanza a escala entre múltiples equipos: mapee cada sistema al Marco de Gestión de Riesgos de IA del NIST, al Reglamento de IA de la UE y a la ISO/IEC 42001; mantenga un inventario con niveles de riesgo y responsables nombrados; y exija pruebas de equidad, seguridad y privacidad antes y después del lanzamiento. Normalice las fichas de modelo y de datos, las pruebas de equipo rojo y los procedimientos de recurso para que los equipos dejen de reinventar lo mismo. Presupuesto explícito para gobernanza, supervisión e interpretabilidad, y trate el riesgo de IA sin gestionar como una amenaza para la licencia de operación.

**Administración pública.** Las reglas de contratación, la transparencia y la rendición de cuentas pública condicionan cada elección. Publique una nota de transparencia en lenguaje accesible, realice una evaluación de impacto antes del despliegue y conserve la toma de decisión humana significativa en cualquier acción que afecte a un ciudadano, con una vía de recurso operativa. Exija a los proveedores que divulguen las limitaciones del modelo y garanticen la portabilidad de datos, evite la discriminación contraria a derecho, nombre a un responsable designado para cada sistema y reporte la huella ambiental de los trabajos significativos.

## Ejemplos

**Startup.** Una pequeña empresa de créditos que desarrollaba una funcionalidad de evaluación crediticia inicial no podía constituir un comité de gobernanza, así que ejecutó la versión ligera que aun así importaba. Los dos fundadores firmaron conjuntamente la aprobación del modelo, lo probaron en busca de resultados diferenciados entre los grupos que podían medir y redactaron una breve ficha de modelo de una página que cubría datos, límites y riesgos conocidos. Optaron por un modelo más simple y interpretable para poder ofrecer a cualquier solicitante denegado un motivo claro y un camino hacia una revisión humana, y registraron las decisiones para poder revisar la equidad a medida que crecían.

**Gran empresa.** Un banco que desplegaba un modelo de crédito constituyó un comité de gobernanza de IA, clasificó el modelo como de alto riesgo e impuso pruebas de equidad entre grupos demográficos antes y después del lanzamiento. Documentó el modelo en una ficha de modelo. Ofreció a los solicitantes denegados un motivo en lenguaje accesible y un recurso ante un subvencionador humano, y sometió el sistema a pruebas de equipo rojo frente a la manipulación. Eligió un modelo algo menos preciso pero más interpretable, porque debía explicar y defender cada decisión ante los reguladores.

**Administración pública.** Una agencia pública que utilizaba IA para ayudar a asignar recursos de inspección alineó su programa con el Marco de Gestión de Riesgos de IA del NIST y con las disposiciones pertinentes de la normativa de IA aplicable. Publicó una nota de transparencia que describía el funcionamiento del sistema y sus salvaguardas. Realizó una evaluación de impacto antes del despliegue, mantuvo la decisión humana significativa en cualquier acción que afectara a un ciudadano y puso a disposición un procedimiento de recurso. La equidad se monitorizó de forma continua, el coste ambiental del trabajo se reportó y se nombró a un funcionario responsable ante la sociedad del sistema.

## Caso de negocio: motivaciones, retorno y coste total de propiedad

La IA responsable protege tanto como crea valor. El retorno es, en gran medida, un coste evitado: menos reclamaciones por discriminación, sanciones reguladoras y desastres reputacionales; auditorías más fluidas; y mayor confianza del usuario y del público, lo que impulsa la adopción. Los sistemas fiables son también más robustos, porque la disciplina que produce equidad y seguridad produce también una mejor ingeniería.

El coste total de propiedad incluye personal de gobernanza, pruebas de equidad y seguridad, documentación, pruebas de equipo rojo, procesos de supervisión y el rendimiento que a veces se sacrifica por interpretabilidad o equidad. Pese a ello, contraste con el coste de no invertir: responsabilidad jurídica, cierres forzados, pérdida de confianza pública y el coste mucho mayor de añadir gobernanza a posteriori tras un fallo. En contextos regulados, la inversión en IA responsable se vuelve cada vez más innegociable. Presente el caso a la dirección enmarcándolo como gestión de riesgo y licencia de operación: la condición de posibilidad para desplegar IA a escala.

## Antipatrones y trampas

- **Equidad por omisión.** Asumir que un modelo es justo porque ignora atributos protegidos.
- **Teatro de la explicabilidad.** Producir explicaciones que no reflejan realmente cómo se toman las decisiones.
- **Supervisión de trámite.** Revisión humana nominal sin autoridad ni información real para anular.
- **Gobernanza a posteriori.** Añadir documentación y revisión después del diseño y el despliegue.
- **Sin vía de recurso.** Dejar a las personas afectadas sin forma de impugnar una decisión automatizada.
- **Ignorar el mal uso.** Probar solo el uso previsto y pasar por alto las elusiones y los abusos.
- **Ceguera ante la huella.** Recurrir por defecto al modelo más grande sin atención a su coste ambiental.

## Modelo de madurez

1. **Iniciación.** No hay pruebas de equidad, explicaciones ni gobernanza; la responsabilidad no está definida; los problemas de sesgo, mal uso y privacidad solo aparecen después del daño, y no existe inventario de sistemas de IA ni de sus riesgos.
2. **Desarrollo.** Algunas pruebas de sesgo, fichas de modelo y pruebas de equipo rojo se realizan en sistemas individuales, pero la práctica es inconsistente entre equipos; la supervisión es improvisada; marcos como el Marco de Gestión de Riesgos de IA del NIST y el Reglamento de IA de la UE se conocen, pero solo se aplican de forma parcial.
3. **Estandarización.** La gobernanza está documentada y se aplica en toda la organización: los sistemas están alineados con marcos reconocidos y la ISO/IEC 42001, cada uno tiene un nivel de riesgo y un responsable nombrado, y las pruebas de equidad, seguridad y privacidad, las fichas de modelo y de datos, las vías de recurso y las pruebas de equipo rojo para sistemas de alto riesgo son obligatorias, no opcionales.
4. **Gestión.** El programa se mide y controla con datos: indicadores de equidad por subgrupo, hallazgos de seguridad y elusiones, volumen de recursos y tasas de revocación, tasas de anulación por supervisión y huella de carga de trabajo se siguen frente a líneas de base y umbrales; la deriva y los resultados diferenciados activan acciones definidas; las decisiones de sí o no se toman con evidencia, no con certificaciones verbales.
5. **Orquestación.** La IA responsable mejora de forma continua y se integra en toda la organización: la monitorización de equidad, seguridad y mal uso opera en producción, la gobernanza está incorporada al ciclo de entrega, el coste ambiental es un criterio formal en la elección de modelo, y la organización adapta sus controles a medida que evolucionan la ley, el riesgo y la capacidad, con la responsabilidad asumida por todos y no por un solo equipo.

## Pautas de reflexión

- ¿Qué definición de equidad aplica a una decisión concreta y quién la decide?
- ¿Qué cantidad de precisión o rendimiento es aceptable sacrificar por equidad o interpretabilidad?
- ¿Qué hace que la supervisión humana sea significativa y no un mero trámite?
- ¿Cómo deben diseñarse los recursos contra decisiones automatizadas para que sean justos y expeditos?
- ¿Cómo se realiza la prueba con equipo rojo para descubrir mal usos que aún no se han imaginado?
- ¿Debe el coste ambiental influir en la elección de modelo y cómo se ponderaría?

## Ideas clave

- La IA fiable es equitativa, explicable, responsable, segura y respetuosa con la privacidad, por diseño.
- La equidad y la seguridad son disciplinas continuas de medición y gestión, no comprobaciones puntuales.
- Alinee la gobernanza con el Marco de Gestión de Riesgos de IA del NIST, el Reglamento de IA de la UE y la ISO/IEC 42001 para ser defendible y auditable.
- Mantenga supervisión humana significativa, responsabilidad clara y un derecho real al recurso.
- Diseñe para la privacidad y contra el mal uso, y asuma el coste ambiental.

## Referencias y lecturas adicionales

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Unión Europea, *Reglamento de Inteligencia Artificial (Artificial Intelligence Act)*.
- ISO/IEC 42001, *Tecnología de la información, Sistemas de gestión de inteligencia artificial*.
- Solon Barocas, Moritz Hardt y Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Armas de destrucción matemática* [trad. de *Weapons of Maths Destruction*].
- Emma Strubell, Ananya Ganesh y Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.

