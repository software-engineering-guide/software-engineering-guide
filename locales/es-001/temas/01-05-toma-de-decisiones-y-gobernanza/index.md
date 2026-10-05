# 1.5 Toma de decisiones y gobernanza

## Visión general y motivación

Todo sistema de software es la suma de miles de decisiones: qué base de [datos](https://en.wikipedia.org/wiki/Database), qué arquitectura, qué librería, si conviene construir internamente o recurrir a un proveedor externo, cuándo asumir deuda y cuándo liquidarla. La gobernanza es el conjunto de mecanismos que permiten tomar esas decisiones con rigor y coherencia, implicar a las personas adecuadas sin crear cuellos de botella y conservar el razonamiento para que los equipos sucesores no se vean condenados a volver a descubrirlo desde cero. En un equipo pequeño, las decisiones se toman en la conversación y viven en la memoria colectiva. A mayor escala, esa memoria se evapora: la gente se va, los equipos se reorganizan y el «por qué» de una elección crítica se pierde en el olvido, dejando a los que heredan el sistema entre imitarlo sin comprenderlo o eliminarlo a ciegas. Una buena gobernanza es el engranaje que hace que las decisiones sean visibles, deliberadas y duraderas a lo largo de una organización grande y en constante cambio.

El reto central para los equipos grandes es equilibrar autonomía y coherencia. Si se elevan todas las decisiones a un órgano central, se gana consistencia, pero a costa de unos cuello de botella asfixiantes y unos equipos desprovistos de iniciativa. Si se delegan todas las decisiones en la base, se gana agilidad, pero a costa del caos: tecnologías incompatibles, esfuerzos duplicados y los mismos errores repetidos una y otra vez. La respuesta madura no es ni la centralización ni la anarquía. Es un modelo por capas. Los equipos deciden lo más posible en su ámbito local, dentro de una «ruta trazada» bien delimitada, mientras que un proceso ligero y transparente rige las verdaderamente transversales y difíciles de revertir. El objetivo es que la buena decisión sea la opción fácil por defecto, y que la escasa atención de la gobernanza se destine solo a lo que realmente importa.

Las empresas y las administraciones públicas cargan con una responsabilidad amplificada. Deben dar cuenta a auditores, reguladores y organismos de supervisión que exigen decisiones documentadas y defendibles. Trabían con horizontes temporales largos, donde una elección arquitectónica pobre o un montón de [deuda técnica](https://en.wikipedia.org/wiki/Technical_debt) sin gestionar puede lastrar a la organización durante una década. Y sus obligaciones de adquisiciones y cumplimiento normativo convierten las decisiones entre construir y adquirir en decisiones especialmente trascendentes y difíciles de revertir. Para estas organizaciones, una toma de decisiones disciplinada y bien documentada no es burocracia por la burocracia. Es gestión del riesgo, memoria institucional y el cimiento de la rendición de cuentas.

## Principios fundamentales

- Documentar las decisiones y su razonamiento; una decisión sin justificación es un lastre.
- Descender las decisiones al nivel más bajo que disponga del contexto, dentro de unos límites claros.
- Ajustar el peso del proceso al peso y a la reversibilidad de la decisión.
- Distinguir entre decisiones reversibles («puerta de doble sentido») e irreversibles («puerta de sentido único») y gobernarlas de forma diferente.
- Preferir las rutas trazadas y los valores por defecto frente a las aprobaciones caso por caso.
- Tratar la deuda técnica como un portafolio gestionado, no como una falta de virtudes que hay que esconder.
- Hacer la gobernanza transparente; una toma de decisiones oculta engendra desconfianza y retrabajo.

## Recomendaciones

### Adoptar Registros de Decisiones de Arquitectura y un proceso de RFC con el tamaño justo

Un [Registro de Decisiones de Arquitectura](https://en.wikipedia.org/wiki/Architectural_decision) (RDA, por sus siglas en inglés, *Architecture Decision Record*) es un documento breve e inmutable que recoge una decisión significativa: su contexto, las opciones que se barajaron, la elección que se tomó y las consecuencias derivadas. Almacénalos en el control de versiones junto al código, para que el razonamiento viaje con el sistema. En las decisiones que requieren aportaciones previas, use un proceso de [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (*Request for Comments*, solicitud de comentarios) ágil: circule una propuesta, abra un periodo de comentarios acotado, decida y regístrelo. Mantenga ambos ligeros. El valor reside en el pensamiento y en el registro duradero, no en plantillas elaboradas. Juntos, los RDAs y los procesos de RFC convierten el razonamiento tácito y olvidado en una memoria institucional consultable.

### Gobernar mediante rutas trazadas, no mediante custodios de puertas

En lugar de revisar cada decisión individualmente, invierta en una «ruta trazada»: un conjunto de opciones bendecidas y plenamente soportadas (idiomas, marcos de trabajo, tuberías de despliegue y patrones aprobados) que los equipos pueden adoptar con mínima fricción y abundante apoyo. Los equipos que se mantienen en la ruta trazada necesitan poca gobernanza, porque la opción segura y conforme a la normativa es también la más fácil. Los que tienen un motivo legítimo para desviarse pueden hacerlo, pero asumen la responsabilidad adicional y una revisión ligera. Este modelo de «camino dorado» escala mucho mejor que una comisión central que aprueba todo, porque desplaza la gobernanza de la fiscalización caso por caso al diseño de buenos valores por defecto.

### Utilizar los comités de arquitectura con mesura y transparencia

Un comité de arquitectura, o su equivalente, tiene un papel legítimo para las decisiones de mayor envergadura, las más transversales o las más difíciles de revertir, y para fijar los estándares que definen la ruta trazada. Manténgalo con un alcance acotado, unos criterios publicados y un proceso rápido y consultivo, no un cuello de botella obligatorio para el trabajo ordinario. La misión del comité es velar por la coherencia y compartir conocimiento, no aprobar cada elección. Cuando un comité se convierte en una cola a la que todo proyecto debe esperar, ha fracasado. Delede enérgicamente y reserve la revisión central para las pocas decisiones que de verdad la merecen.

### Convertir la decisión entre construir, adquirir o adoptar en un análisis deliberado

Para cualquier capacidad significativa, pesen tres caminos: construirla internamente, adquirir un producto comercial o adoptar una solución de [código abierto](https://en.wikipedia.org/wiki/Open-source_software). Construya cuando esa capacidad sea un diferenciador genuino y sea central en su misión. Adquiera o adopte las capacidades que no le diferencian y que otros ya resuelven mejor. Cuenten con el [coste total de propiedad](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (CTP), no solo con el precio inicial. Adquirir un producto implica licencias, integración y riesgo de [vinculación al proveedor](https://en.wikipedia.org/wiki/Vendor_lock-in). Construir conlleva un mantenimiento y una dotación de personal perpetuos. Adoptar una solución de código abierto implica asumir obligaciones de soporte y seguimiento de seguridad. Registre la decisión y sus supuestos en un RDA para poder revisarla cuando cambien las circunstancias.

### Gestionar la deuda técnica como un portafolio

La deuda técnica no es inherentemente mala. A veces asumirla para desplegar antes es la elección acertada. Lo que sí es perjudicial es una deuda incontrolada, invisible y olvidada. Mantenga un inventario explícito de la deuda significativa. Para cada concepto, anote el coste que impone (el «interés» recurrente) y el coste de repararlo. Luego, adminístrelo como un portafolio financiero. Liquide la deuda de alto interés que frena al equipo cada día. Tolere la deuda de bajo interés en las zonas estables del sistema. Tómenla como una decisión consciente, no como un accidente. Reserve una proporción fija de capacidad para liquidar deuda, de modo que nunca se convierta en una crisis.

### Distinguir entre decisiones reversibles e irreversibles

No todas las decisiones merecen la misma deliberación. Las decisiones reversibles, las «puertas de doble sentido», son fáciles de deshacer, así que tómense rápido y a nivel local, por el propio equipo, con un sesgo hacia la acción. Demorarse en ellas es perder el tiempo y frenar el aprendizaje. Las decisiones irreversibles o costosas de revertir, las «puertas de sentido único» (un contrato de [API](https://en.wikipedia.org/wiki/API) público, un modelo de datos a gran escala, un compromiso plurianual con un proveedor) , merecen una deliberación pausada y rigurosa a nivel superior, con un razonamiento documentado. Clasificar las decisiones de esta forma es uno de los hábitos de gobernanza de mayor rentabilidad. Dirige la escasa atención a donde de verdad importa y desbloquea todo lo demás.

## Compromisos: ventajas y desventajas

| Enfoque de gobernanza | Ventajas | Desventajas |
| --- | --- | --- |
| Comité central que revisa todo | Máxima consistencia y supervisión | Cuello de botella grave; desmotiva a los equipos; lentitud |
| Ruta trazada con autonomía local | Escala con agilidad, ofrece un valor seguro por defecto, empodera a los equipos | Exige inversión previa en plataforma; puede haber algún desvío |
| Autonomía total sin gobernanza | Rapidez, gran sentimiento de propiedad | Fragmentación, duplicación de esfuerzos, repetición de errores |
| RDAs / RFC | Memoria duradera, mejores decisiones, transparencia | Sobrecarga de redacción; pierde valor si no se mantiene |

| Decisión de abastecimiento | Ventajas | Desventajas |
| --- | --- | --- |
| Construir | Control total, ajuste exacto, posibilidad de diferenciarse | Coste permanente de mantenimiento y dotación de personal |
| Adquirir | Rapidez, soporte del proveedor, alguien más lo mantiene | Coste de licencias, vinculación al proveedor, ajuste imperfecto |
| Adoptar (código abierto) | Sin cuota de licencia, código inspeccionable, comunidad activa | El soporte y la seguridad recaen sobre nosotros |

El compromiso unificador es el control frente a la velocidad, y la coherencia central frente a la autonomía local. Cada elección de gobernanza se sitúa en este continuo. La postura recomendada (rutas trazadas más delegación basada en la reversibilidad) compra deliberadamente la mayor parte de la agilidad de la autonomía a la vez que conserva la coherencia que de verdad importa. Lo consigue haciendo que la opción alineada sea la más fácil y reservando el proceso más exigente para las raras decisiones irreversibles.

## Preguntas para debatir con su equipo

1. **¿Quién decide si una decisión dada es una puerta de sentido único y cómo detectaremos los errores de clasificación en ambas direcciones?** Clasificar las decisiones por su reversibilidad es uno de los hábitos de gobernanza de mayor rendimiento, y su valor se desploma si clasificamos mal: tratar una decisión reversible como irreversible la sumerge en un análisis paralizante, y tratar una irreversible como reversible nos expone a desplegar un modelo de datos o un contrato de API público que no podremos deshacer a bajo coste. El riesgo competidor es que la persona más cercana al trabajo puede estar sesgada hacia la rapidez, mientras que un comité central puede estar sesgado hacia la cautela. Llevan ejemplos concretos al debate: ¿qué costaría, en tiempo y dinero, revertir cada decisión, y quién asume ese coste? En entornos empresariales y de la administración, los compromisos de adquisición y los datos a gran escala convierten muchas elecciones en puertas de sentido único que a primera vista parecían reversibles. Acuerden quién clasifica y creen el hábito de pedir una segunda opinión rápida en todo lo que se aproxime al límite, para que la atención escasa caiga donde revertir es verdaderamente caro.

2. **¿Quién es el responsable, quién financia y quién da soporte a la ruta trazada, y qué impide que se degrade en un comité de fiscalización?** Una ruta trazada solo funciona si los valores por defecto bendecidos son genuinamente bien soportados y más fáciles que las alternativas, y eso requiere una inversión sostenida que resulta fácil subfinanciar. El compromiso es claro: una ruta trazada sin recursos se convierte en un conjunto de mandatos sin soporte, que es exactamente la fiscalización que este modelo pretendía sustituir, y los equipos entonces la eluden. Aporten evidencias de la salud de la ruta: tasas de adopción, qué tan actualizados están las herramientas aprobadas, qué tan rápido responde el equipo de plataforma y con qué frecuencia los equipos solicitan un desvío. En organizaciones grandes y reguladas, la ruta trazada es también el medio por el que la opción conforme a la normativa se convierte en la más fácil, de modo que su financiación es una inversión en cumplimiento, no solo una comodidad. Fijen un responsable claro y un presupuesto estable, y midan si los equipos eligen la ruta porque de verdad es el camino más fácil.

3. **¿Dónde están los equipos eludiendo su gobernanza, y qué nos está diciendo esa TI no oficial?** Los equipos se apartan del camino oficial cuando este resulta más doloroso que el atajo, así que la TI no oficial generalizada es menos un problema de disciplina que una veredicto de diseño sobre la propia gobernanza. Las consideraciones en juego son reales: parte de la evasión es temeraria, y buena parte es una evitación racional de un comité que se ha convertido en una cola de varias semanas. Traigan las evidencias: qué aprobaciones se saltan, qué herramientas no oficiales se han extendido en silencio y cuánto tarda realmente el camino oficial. En contextos empresariales y de la administración, los riesgos son mayores, porque las herramientas no autorizadas pueden incumplir obligaciones de auditoría, seguridad y adquisiciones que tienen peso legal. Si el patrón muestra que la gente elude un cuello de botella, la solución es acelerar y ensanchar la ruta trazada y reducir el alcance del comité a las pocas decisiones transversales e irreversibles, no añadir más trámites de aprobación.

4. **¿Qué proporción de nuestra capacidad de entrega va realmente a liquidar deuda técnica, y podemos señalar los conceptos de mayor interés sobre los que debe concentrarse primero?** La deuda técnica se comporta como un interés compuesto: un impuesto silencioso sobre cada cambio futuro, y una organización grande puede arrastrarla durante años antes de que nadie note que el sistema se ha vuelto lento y frágil de modificar. La presión contrapuesta es directa: cada hora dedicada a liquidar deuda es una hora que no se invierte en funcionalidades que la dirección puede ver, así que es lo primero que se recorta cuando se aprieta un plazo. Llevan al debate evidencias reales: un inventario escrito de la deuda significativa, una estimación honesta del coste recurrente que cada concepto impone y del coste de repararlo, y la proporción real de capacidad reciente que se destinó a liquidar frente a trabajo nuevo. Para empresas y administraciones con horizontes decenales, la deuda no gestionada acaba forzando una reescritura costosa o un hallazgo en auditoría, así que traten una asignación permanente de capacidad para liquidarla como gestión del riesgo y definan quién la defiende cuando los plazos se aprietan.

5. **¿Cuando necesitemos el razonamiento de una decisión tomada hace dos años, de verdad podemos encontrarlo, y hay alguien que mantiene ese registro vivo?** Todo el valor de un Registro de Decisiones de Arquitectura está en que el razonamiento sobrevive a las personas que lo tomaron, y ese valor se derrumba si los RDAs se escriben una vez, nunca se consultan y quedan obsoletos en silencio. La tensión está entre la disciplina de redacción que exige capturar contexto, opciones y consecuencias en el momento de la decisión y la presión diaria de desplegar y pasar a lo siguiente. Traigan pruebas concretas al debate: elijan tres decisiones recientes de peso y comprueben si alguien puede localizar el razonamiento registrado en cuestión de minutos, y verifiquen si los RDAs obsoletos están marcados como tales en lugar de contradecir en silencio la práctica actual. En entornos empresariales y de la administración, ese registro consultable es exactamente la evidencia defendible que auditores y organismos de supervisión exigen, así que definan dónde residen los RDAs, quién los revisa y qué hace que una decisión sea suficientemente significativa para registrarse.

6. **¿Cuándo revisitamos por última vez una decisión importante de construir o adquirir frente a sus supuestos originales, y llegaríamos siquiera a percibir cuando esos supuestos caducan?** Las decisiones de abastecimiento son de las más costosas y difíciles de revertir que se toman, y los supuestos en los que se basan (la tarificación de un proveedor, la propia dotación de personal, la madurez de una opción de código abierto) se desactualizan en silencio mientras la decisión permanece congelada. Las consideraciones en juego pesan el coste hundido y la perturbación de cambiar frente al coste creciente de la vinculación al proveedor, un ajuste imperfecto o una carga de mantenimiento que ya no se desea. Traigan el RDA original con sus supuestos declarados, una estimación actual del coste total de propiedad de cada camino (incluyendo licencias, integración, dotación de personal y coste de salida) y cualquier señal, un cambio de precios o una degradación del soporte, que indique que un supuesto ha cambiado. Para compradores de la administración y del sector regulado, las normas de adquisiciones y los contratos plurianuales convierten estas puertas de sentido único especialmente vinculantes, así que fijen de antemano los desencadenantes y la periodicidad que obligarán a una decisión deliberada y no a una renovación ciega.

## Perspectiva sectorial

**Startup.** Gobiérnese casi de nada y aposté fuerte por la velocidad: para las decisiones reversibles, de doble sentido, decida en su puesto y siga adelante. Reserve su único hábito de gobernanza para el puñado de puertas de sentido único, un modelo de datos central o un proveedor fundamental, y capture cada una en un solo párrafo para que un compañero futuro no tenga que relitigarla desde cero. Omitan comités y rutas trazadas por completo, porque a su tamaño son una sobrecarga que no pueden permitirse y todo el equipo comparte ya el contexto.

**Pyme.** Sin un arquitecto en plantilla, hagan de la decisión entre construir y adquirir su pregunta central de gobernanza y respondan en función del coste total de propiedad, no de la preferencia. Por defecto, adquiera o adopte herramientas bien soportadas para todo lo que no sea su diferenciador central, porque el mantenimiento perpetuo es el coste que menos pueden permitirse llevar. Mantengan un registro de decisiones ligero para que el razonamiento de sus pocas elecciones trascendentes sobreviva a la salida de una persona clave.

**Gran empresa.** El problema es equilibrar autonomía y coherencia entre muchos equipos, así que inviertan en una ruta trazada bien financiada y reserven un comité de arquitectura estrecho y ágil para las decisiones verdaderamente transversales e irreversibles. Estándaricen los RDAs para que el razonamiento se convierta en memoria institucional consultable, y gestionen la deuda técnica y las decisiones de abastecimiento como portafolios con presupuestos estables. Midan si los equipos eligen la ruta porque es la más fácil y reducen cualquier comité que se haya degradado en una cola.

**Administración pública.** Aquí, las decisiones documentadas y defendibles no son opcionales: auditores y organismos de supervisión esperan ver el razonamiento, las opciones sopesadas y los supuestos de toda elección trascendental. Ejecuten la decisión entre construir y adquirir como un análisis documentado del coste total de propiedad, respeten las normas de adquisición que limitan la vinculación exclusiva a un proveedor y mantengan los RDAs como la evidencia trazable exigible ante auditoría. Tomen los horizontes temporales largos en serio, porque un modelo de datos o un compromiso con un proveedor tomado hoy puede vincular a la organización durante una década, así que clasifíquelo como puerta de sentido único y delibere en consecuencia.

## Ejemplos

**Startup.** Una startup de cuatro personas toma la mayor parte de sus decisiones en minutos, frente a frente en un espacio compartido, y para las decisiones reversibles esa rapidez es una ventaja real, de modo que resisten cualquier sobrecarga de gobernanza. Pero cuando eligen una base de datos y un modelo de datos que resultarán dolorosos de cambiar más adelante (una puerta de sentido único), se detienen a escribir una nota de un solo párrafo: las opciones, la elección y los supuestos que la sustentan. Un año después, al topar con límites de escalabilidad, esa nota les ahorra relitigar la cuestión desde cero. Gobiernan casi nada y reservan su único hábito ligero para las pocas decisiones que de verdad son caras de revertir.

**Gran empresa.** Los equipos de plataforma de una gran empresa estaban paralizados por un comité de arquitectura que debía aprobar cada elección de tecnología, creando colas de varias semanas. La empresa reestructuró la gobernanza en torno a una ruta trazada: un catálogo curado de idiomas, bases de datos y tuberías de despliegue aprobados y plenamente soportados que los equipos podían adoptar al instante. Los RDAs registraban cualquier decisión de desviarse, y una revisión rápida y consultiva cubría solo las opciones fuera de la ruta. El alcance del comité se redujo a la fijación de estándares y al puñado de decisiones verdaderamente transversales. La entrega se aceleró notablemente. La coherencia mejoró de hecho, porque el camino fácil era ahora el conforme a la normativa. Y el archivo de RDAs dotó a la organización de un registro consultable de por qué las cosas se habían construido como se habían construido.

**Administración pública.** Un departamento gubernamental se enfrentó a una decisión trascendental de construir o adquirir para una plataforma de gestión de casos, bajo estrictas normas de adquisición y auditoría. En lugar de decidir por preferencia, ejecutó un análisis documentado del coste total de propiedad en tres opciones: construcción a medida, adquisición de un producto comercial y adopción de una base de código abierto. Sopesó licencias, integración, mantenimiento a largo plazo, dotación de personal y vinculación al proveedor, y registró la decisión y sus supuestos en un RDA. Años después, cuando los términos de un proveedor cambiaron, el departamento revisó aquel RDA, constató que sus supuestos originales ya no se mantenían y volvió a decidir con pleno conocimiento del razonamiento previo, evitando una migración ciega y costosa. El razonamiento registrado era, además, exactamente la evidencia defendible que los auditores exigían.

## Justificación económica: motivaciones, retorno de la inversión y coste total de propiedad

Las decisiones son el coste de mayor apalancamiento y menor visibilidad en el software. Una sola elección arquitectónica o de abastecimiento, pobre e irreversible, puede imponer años de arrastre o una remediación de nueve ceros. Gobernar bien esa decisión (un par de horas de deliberación y un registro escrito) cuesta casi nada en comparación. El retorno de los RDAs y la delegación basada en la reversibilidad procede de dos fuentes: evitar errores costosos en las decisiones irreversibles y evitar deliberación y retrabajo innecesarios en todo lo demás. El razonamiento registrado también reduce drásticamente el coste recurrente de relitigar cuestiones ya zanjadas y de que los equipos tengan que reconstruir la intención tras sistemas heredados.

La deuda técnica hace concreto el argumento del coste total de propiedad. La deuda no gestionada se comporta exactamente como un interés compuesto: un impuesto creciente sobre cada cambio futuro, hasta que el sistema se vuelve efectivamente inmantenible y exige una reescritura costosa. Gestionar la deuda como un portafolio, con una asignación de capacidad estable para liquidar los conceptos de mayor interés, es mucho más barato que la crisis eventual. Una buena gobernanza es barata de adoptar, sobre todo la disciplina de poner las decisiones por escrito y la inversión inicial en una ruta trazada. Omitirla es caro: se paga en reescrituras evitables, sorpresas de vinculación al proveedor, fallos de auditoría y pérdida de memoria institucional. Para convencer a la dirección, enmarquen la gobernanza en su lenguaje: reducción de riesgos, retrabajo evitado, mayor agilidad de entrega a través de la ruta trazada y defensibilidad ante auditoría. Demuestren que el objetivo no es más proceso, sino mejor proceso orientado: escrutinio riguroso solo donde revertir es costoso, y agilidad sin fricciones en todo lo demás.

## Antipatrón y trampas

- Decisiones no documentadas: el razonamiento se pierde en el instante en que se marchan las personas que lo tomaron.
- Cuello de botella del comité de aprobación: un órgano central al que todo proyecto debe esperar.
- Un único proceso para todo: someter decisiones triviales y reversibles a una revisión pesada.
- Parálisis por análisis: atorarse en decisiones de doble sentido que se deshacen sin esfuerzo.
- [TI no oficial](https://en.wikipedia.org/wiki/Shadow_IT): equipos que esquivan la gobernanza por completo porque el camino oficial resulta demasiado doloroso.
- Deuda técnica invisible: deuda que nunca se inventaria, nunca se liquida, y que se acumula en silencio.
- Reflexo de construir todo o de adquirir todo: decidir el abastecimiento por inercia en lugar de por un análisis del coste total de propiedad.
- Teatro de gobernanza: documentos y comités que existen por apariencia pero no orientan las decisiones.

## Modelo de madurez

- **Nivel 1 (Iniciar):** Las decisiones son improvisadas y no se registran; la gobernanza está ausente o es un cuello de botella generalizado; la deuda técnica es invisible y el razonamiento de las elecciones se evapora cuando la gente se marcha.
- **Nivel 2 (Desarrollar):** Algunas decisiones se documentan y existe cierta revisión, pero la práctica es inconsistente entre equipos y el proceso suele no ajustarse al peso y a la reversibilidad de la decisión.
- **Nivel 3 (Estandarizar):** Los RDAs, la ruta trazada, la delegación basada en la reversibilidad y el inventario de deuda están documentados y aplicados en toda la organización, de modo que la opción conforme a la normativa es el valor fácil por defecto y el razonamiento es consultable.
- **Nivel 4 (Gestionar):** La gobernanza se mide frente a referencias de base: adopción de la ruta trazada, cobertura de RDAs, tiempo de ciclo de decisión, deuda como proporción de capacidad y tasa de excepciones fuera de la ruta se rastrean, y las decisiones de liquidar deuda o revisar el abastecimiento se activan con esa evidencia y no por crisis.
- **Nivel 5 (Orquestar):** La gobernanza se afina de forma continua y se integra con la planificación de la entrega y el riesgo; el escrutinio se orienta con precisión a las decisiones irreversibles; la deuda y las decisiones de abastecimiento se reequilibran activamente como portafolios y se retoman sobre la evidencia a medida que cambian las circunstancias.

## Ideas para el debate

- ¿Para nuestras decisiones recientes más importantes, podemos encontrar el razonamiento que las sustentó?
- ¿Dónde es nuestra gobernanza un cuello de botella, y dónde está ausente cuando se necesita?
- ¿Cuáles de nuestras decisiones actuales son puertas de sentido único y las estamos tratando como tales?
- ¿Qué proporción de nuestra capacidad se destina a liquidar deuda técnica y es suficiente?
- ¿Los equipos siguen la ruta trazada porque de verdad es el camino más fácil, o la eluden?
- ¿Cuándo revisitamos por última vez una decisión importante de construir o adquirir frente a sus supuestos originales?

## Ideas clave

- Documente las decisiones significativas y su razonamiento con RDAs; haga que el razonamiento sea duradero.
- Gobiérnense mediante rutas trazadas y valores por defecto, no mediante la fiscalización caso por caso.
- Ajuste el peso del proceso al peso y a la reversibilidad de la decisión: delegue las de doble sentido, delibere sobre las de sentido único.
- Analice construir, adquirir o adoptar en función del coste total de propiedad, y registre los supuestos.
- Gestione la deuda técnica como un portafolio explícito con una asignación permanente de capacidad para liquidarla.
- Mantenga la gobernanza transparente y ágil; dirija el escrutinio escaso a donde revertir es costoso.

## Referencias y lecturas adicionales

- Michael Nygard, «Documenting Architecture Decisions» (el patrón original del RDA)
- Gregor Hohpe, *The Software Architect Elevator* y *37 Things One Architect Knows*
- Cartas de Amazon a sus accionistas sobre las decisiones de tipo 1 y tipo 2 (puertas de sentido único frente a de doble sentido)
- Ward Cunningham, la metáfora original de la «deuda técnica»
- Martin Fowler, escritos sobre deuda técnica y arquitectura evolutiva
- Neal Ford, Rebecca Parsons y Patrick Kua, *Building Evolutionary Architectures*
- Nicole Forsgren, Jez Humble y Gene Kim, *Accelerate* (arquitectura de bajo acoplamiento y autonomía)
- ISO/IEC/IEEE 42010 sobre la descripción de la arquitectura

