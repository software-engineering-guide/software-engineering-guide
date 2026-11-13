# 10.6 Gestión de proyectos

## Presentación y motivación

La [gestión de proyectos](https://en.wikipedia.org/wiki/Project_management) es la disciplina de convertir la intención en resultados entregados bajo restricciones. Coordinas a la gente, el alcance, el calendario, el costo, el riesgo, y la calidad para que el trabajo realmente termine y entregue valor. En el software a menudo se trata con sospecha, atada a planes pesados y [diagramas de Gantt](https://en.wikipedia.org/wiki/Gantt_chart) que la realidad ignora. Pero la necesidad subyacente nunca desaparece. Alguien debe asegurarse de que el trabajo correcto ocurra en el orden correcto, las dependencias se gestionen, los riesgos aparezcan temprano, y las [partes interesadas](https://en.wikipedia.org/wiki/Project_stakeholder) sepan qué esperar. La pregunta no es *si* gestionar proyectos, sino *cuán ligera y adaptativamente* puedes hacerlo mientras aún cumples tus obligaciones.

¿Por qué tratar esto explícitamente? Los proyectos de software fallan a tasas alarmantes, y fallan mucho más a menudo por razones de gestión que por razones puramente técnicas: alcance poco claro, dependencias sin gestionar, riesgo no abordado, partes interesadas ausentes, y la fantasía de estimaciones precisas de largo alcance. Los programas grandes están especialmente expuestos: con muchos equipos, proveedores, y horizontes multitrimestrales, los pequeños fallos de coordinación se componen. La buena gestión de proyectos es en gran medida la práctica de hacer compromisos honestamente, descomponer el trabajo sensatamente, y crear retroalimentación rápida para que los problemas aparezcan mientras todavía son baratos de arreglar.

Los contextos empresariales y gubernamentales elevan las apuestas y cambian las restricciones. Las empresas gestionan carteras de iniciativas entrelazadas contra la estrategia y los ciclos de presupuesto (capítulo 10.1). Los gobiernos añaden reglas de contratación pública, asignaciones multianuales, gestión de contratistas, y rendición de cuentas pública. Ahí, el valor predeterminado histórico (contratos grandes, de alcance fijo, en [cascada](https://en.wikipedia.org/wiki/Waterfall_model)) tiene un largo historial de fallo costoso y visible. Este capítulo cubre los fundamentos que aplican a través de los enfoques predictivo, adaptativo, e híbrido. El capítulo 10.7 (Ágil) profundiza en la entrega adaptativa, y el capítulo 10.1 cubre la gestión de cartera y programa por encima del proyecto individual.

## Principios fundamentales

- **Gestiona los resultados, no la actividad.** Terminado significa valor entregado, no tareas cerradas.
- **Descompón y secuencia.** El trabajo pequeño, ordenado, y consciente de dependencias supera a los planes de gran explosión.
- **Las estimaciones son rangos, no promesas.** Comunica la incertidumbre honestamente.
- **Expón el riesgo temprano y continuamente.** El problema más barato es el que se atrapa primero.
- **Ajusta el método al trabajo.** Predictivo, adaptativo, o híbrido: ajusta a la incertidumbre y las restricciones.
- **Haz transparente el estado.** El flujo visible supera a los informes tranquilizadores.
- **Las partes interesadas son parte del equipo.** La ausencia del cliente es un riesgo de proyecto.

## Recomendaciones

### Elige lo predictivo, adaptativo, o híbrido deliberadamente

No hay un modelo de entrega universalmente correcto; hay un ajuste entre el método y el contexto:

- **Predictivo (impulsado por plan, «cascada»):** el alcance se fija por adelantado, luego se derivan el calendario y el costo. Conviene al trabajo con requisitos genuinamente estables y bien comprendidos y restricciones externas duras (certificación regulatoria, integración física). Su modo de fallo es fingir que los requisitos de software son estables cuando no lo son.
- **Adaptativo ([ágil](https://en.wikipedia.org/wiki/Agile_software_development)):** el alcance flexiona; el tiempo y el costo se fijan en iteraciones cortas que entregan software funcional y absorben el aprendizaje. Conviene a la mayoría del trabajo de producto y servicio digital, donde los requisitos se descubren (capítulos 11.1, 10.7).
- **Híbrido:** un núcleo adaptativo dentro de una envoltura de gobernanza predictiva, común y a menudo correcto en la empresa y el gobierno, donde la financiación, el cumplimiento, y la contratación exigen hitos y auditoría mientras la entrega se beneficia de la iteración.

Los marcos como [PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) (el Cuerpo de Conocimiento de Gestión de Proyectos, del [Project Management Institute](https://en.wikipedia.org/wiki/Project_Management_Institute)) y [PRINCE2](https://en.wikipedia.org/wiki/PRINCE2) (PRojects IN Controlled Environments) codifican la práctica predictiva e híbrida. El punto es tomar prestada su disciplina (roles, riesgo, puertas de etapa) sin importar ceremonia que el trabajo no necesita.

### Gestiona el alcance contra la triple restricción

El alcance, el calendario, y el costo se mueven juntos, acotados por la calidad: el clásico [«triángulo de hierro».](https://en.wikipedia.org/wiki/Project_management_triangle) No puedes fijar los tres y añadir alcance gratis. Algo cede, y fingir lo contrario es cómo empiezan las [marchas de la muerte](https://en.wikipedia.org/wiki/Death_march_(project_management)). Haz explícitas las contrapartidas, y decide *cuál* variable flexiona. Los métodos adaptativos fijan el tiempo y el costo y flexionan el alcance. Los contratos de precio fijo fijan el alcance y el costo, y en realidad flexionan la calidad o el calendario a menos que los gestiones. Controla la [dilatación del alcance](https://en.wikipedia.org/wiki/Scope_creep) con un proceso de cambio ligero (capítulo 12.3), y prefiere *reducir el alcance a un núcleo valioso* sobre deslizar todo.

### Estima honestamente, en rangos, y vuelve a pronosticar

La estimación es donde los proyectos más a menudo se mienten a sí mismos. Trata las estimaciones como rangos probabilísticos, no números únicos, y ensánchalos para el trabajo distante y poco comprendido (el [«cono de incertidumbre»](https://en.wikipedia.org/wiki/Cone_of_Uncertainty)). Prefiere los métodos relativos y empíricos: el rendimiento histórico y el tiempo de ciclo (capítulos 11.2, 11.3) pronostican mejor que las conjeturas heroicas de abajo hacia arriba. Donde puedas, reemplaza la estimación con la *medición*. Un equipo que cierra 8 elementos/semana tomará aproximadamente 5 semanas para 40 elementos, sin importar los puntos de historia (de nuevo la [Ley de Little](https://en.wikipedia.org/wiki/Little%27s_law): el rendimiento y el trabajo en progreso, no las estimaciones, fijan el tiempo de entrega). Vuelve a pronosticar continuamente a medida que llega la realidad. Un plan que nunca cambia no se está gestionando.

### Gestiona las dependencias y la ruta crítica

A escala, el riesgo dominante rara vez es la velocidad de un único equipo. Son las *dependencias entre equipos y proveedores*. Mapéalas explícitamente, identifica la [ruta crítica](https://en.wikipedia.org/wiki/Critical_path_method) (la secuencia que determina el final más temprano posible), y ataca primero las dependencias más largas y riesgosas. Reduce el acoplamiento donde puedas (una dependencia eliminada vale más que una dependencia rastreada) y usa interfaces y contratos claros para que los equipos puedan avanzar en paralelo (capítulos 1.2, 2.3). Para los programas entre equipos, una sincronización regular de dependencias y riesgo supera a un informe de estado que nadie lee.

### Ejecuta un registro de riesgo vivo

La gestión de riesgo es la actividad de gestión de proyectos de mayor apalancamiento, y la más a menudo saltada. Mantén un [registro de riesgo](https://en.wikipedia.org/wiki/Risk_register) simple y vivo: cada riesgo con su probabilidad, impacto, dueño, y mitigación o contingencia (capítulo 12.3). Revísalo regularmente, retira los riesgos que han pasado, y añade nuevos a medida que emergen. Distingue los riesgos (podrían pasar) de los problemas (ya están pasando) y las decisiones (capítulo 1.6). La meta no es un documento. Es un hábito de mirar adelante, para que anticipes los problemas en lugar de descubrirlos en el plazo.

### Involucra a las partes interesadas y comunica transparentemente

La mayoría de los fallos de proyecto «sorpresa» eran visibles temprano para alguien a quien no se escuchó. Identifica a las partes interesadas, comprende sus preocupaciones, y mantenlas genuinamente involucradas. La ausencia del cliente es en sí misma un riesgo principal. Comunica el estado a través de *flujo transparente* (tableros visibles, gráficos de acumulación, software funcional demostrado) en lugar de informes verde-amarillo-rojo que premian el optimismo. Escala honesta y tempranamente. Un proyecto bien operado hace que las malas noticias viajen rápido.

## Ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| **Predictivo / cascada** | Alcance y costo predecibles; amigable con contratos y auditoría | Mal ajuste para requisitos inciertos; retroalimentación tardía; riesgo de gran explosión |
| **Adaptativo / ágil** | Retroalimentación rápida; absorbe el cambio; valor temprano | Más difícil fijar alcance/costo por adelantado; necesita cliente comprometido |
| **Híbrido** | Iteración dentro de la gobernanza; se ajusta a la empresa/gobierno | Tensión entre cadencias; puede heredar ambos conjuntos de sobrecarga |
| **Estimaciones detalladas por adelantado** | Comodidad para planificadores y financiadores | Precisamente equivocadas; costosas de producir; se degradan rápido |
| **Pronóstico empírico (métricas de flujo)** | Fundamentado, autocorrectivo | Requiere historial y disciplina; se ve menos «cierto» |
| **Ceremonia pesada de riesgo/proceso** | Exhaustivo; bueno para programas de alto riesgo | Ralentiza a los equipos pequeños; puede convertirse en marcar casillas |

La tensión central es **predictibilidad frente a adaptabilidad**. Los financiadores, contratos, y auditorías quieren compromisos firmes. El trabajo de software incierto necesita espacio para aprender. Resuélvela de la manera en que lo hace Ágil (capítulo 10.7): comprométete firmemente con los resultados y plazos mientras dejas que el alcance flexione, y usa la gobernanza híbrida para satisfacer la supervisión sin congelar la entrega.

## Preguntas para discutir con tu equipo

1. **¿Cómo envolverás a los equipos de entrega adaptativa en una envoltura de gobernanza predictiva sin heredar la sobrecarga de ambos?** El híbrido es común y a menudo correcto en la empresa y el gobierno, donde los ciclos de financiación, el cumplimiento, y la contratación exigen hitos y auditoría mientras la entrega se beneficia de la iteración. El riesgo es real: un híbrido mal diseñado hereda la documentación pesada de la cascada y las ceremonias de ágil a la vez, y los equipos sienten la fricción de dos cadencias luchando entre sí. Trae evidencia: mapea dónde caen realmente tus puertas de financiación, puntos de comprobación de cumplimiento, e hitos de contrato, y comprueba si cada uno exige un documento que el trabajo de entrega no produce de otra manera. La respuesta debería dejar que la iteración satisfaga la supervisión en lugar de luchar contra ella, alimentando incrementos funcionales demostrados y un registro de riesgo vivo hacia el ritmo de gobernanza en lugar de detenerse a ensamblar informes separados. Toma prestada la disciplina de un marco como PRINCE2 sin importar ceremonia que el trabajo no necesita.

2. **¿Es el estado de tu proyecto flujo transparente, o informes verde-amarillo-rojo que premian el optimismo?** La mayoría de los fallos sorpresa eran visibles temprano para alguien a quien no se escuchó, y el estado de sandía (verde afuera, rojo adentro) es cómo las malas noticias honestas permanecen enterradas hasta el plazo. Reemplaza los informes tranquilizadores con tableros visibles, gráficos de acumulación, y software funcional demostrado, y haz que escalar temprano sea un acto seguro en lugar de un riesgo de carrera. Trae evidencia: mira tu último proyecto problemático y pregunta cuándo existió la primera señal de advertencia frente a cuándo la escuchó el liderazgo. La ausencia del cliente es en sí misma un riesgo principal, así que comprueba si una parte interesada comprometida está genuinamente en el ciclo o si estás construyendo confiadamente hacia lo equivocado. Un proyecto bien operado hace que las malas noticias viajen rápido, y la corrección es tanto cultural como de herramientas.

3. **¿Conoces el núcleo mínimo valioso al que reducirías el alcance si el calendario y el costo dejaran de moverse?** El alcance, el calendario, y el costo se mueven juntos acotados por la calidad, y cuando los financiadores fijan los tres, la calidad se convierte en la válvula de escape silenciosa y empiezan las marchas de la muerte. Los métodos adaptativos fijan el tiempo y el costo y flexionan el alcance, lo cual solo funciona si ya has decidido qué porción entrega valor real y qué funciones son negociables. Trae evidencia: para tu lanzamiento actual, ¿puedes nombrar el núcleo que debe enviarse y la lista que cortarías primero, o cada función se trata silenciosamente como obligatoria? La respuesta debería permitirte reducir el alcance a un núcleo valioso en lugar de deslizar todo, y debería resolverse antes de que llegue la presión, no improvisarse en el plazo. Controla el resto con un proceso de cambio ligero para que la dilatación del alcance no se coma el margen con el que contabas.

4. **¿Qué dependencia entre equipos está en tu ruta crítica ahora mismo, y quién es dueño de eliminarla o reducir su riesgo?** A escala la amenaza dominante rara vez es la velocidad de un equipo; es la secuencia de dependencias entre equipos y proveedores que fija el final más temprano posible. Si nadie puede nombrar la dependencia de ruta crítica actual, estás gestionando el progreso local mientras lo que realmente gobierna tu fecha deriva sin vigilancia. Trae evidencia: un mapa de dependencias que muestre qué traspasos alimentan a cuáles, dónde corre la cadena más larga, y qué enlaces todavía están sin construir o contractualmente bloqueados, más un dueño nombrado para cada enlace riesgoso. Apunta a atacar primero las dependencias más largas y riesgosas y a eliminar el acoplamiento donde puedas, porque una dependencia eliminada vale más que una dependencia rastreada. En programas empresariales y gubernamentales los enlaces más difíciles a menudo cruzan fronteras de proveedor o agencia, así que nombra al dueño responsable de cada lado y confirma que el contrato le permita actuar, o la dependencia permanecerá sin resolver hasta convertirse en un retraso público.

5. **¿Cómo vuelves a pronosticar a medida que llega la realidad, y con qué rapidez un deslizamiento se vuelve visible para la gente que financia el trabajo?** Un plan que nunca cambia no se está gestionando; se está defendiendo, y una fecha de número único defendida más allá de la evidencia es cómo los proyectos se deslizan en silencio hasta el plazo. Reemplaza la estimación con la medición donde puedas, pronosticando a partir del rendimiento histórico y el tiempo de ciclo en lugar de conjeturas heroicas de abajo hacia arriba, y ensancha el rango para el trabajo distante y poco comprendido. Trae evidencia: tu tasa de finalización semanal real, el tamaño actual del atraso, y la finalización proyectada que se deriva de ellos, comparada con la fecha que actualmente cree el liderazgo. La respuesta debería dar a los financiadores una proyección honesta y que se estrecha que ven cada ciclo en lugar de una fecha fija que se sostiene hasta que colapsa. En el gobierno y otros entornos vinculados a asignaciones, un pronóstico que expone el deslizamiento temprano te permite reajustar el alcance o la línea base dentro de las reglas, mientras un deslizamiento oculto se convierte en un fallo de supervisión y un titular.

6. **¿Cuál es el proceso más ligero que todavía cumple tus obligaciones genuinas, y dónde se ha desligado la ceremonia de reducir el riesgo?** Tanto la subgestión como la sobregestión llevan un costo real: caos, retrabajo, y dependencias perdidas en un lado, y marcar casillas que ralentiza la entrega sin bajar el riesgo en el otro. La tensión es que la auditoría, el cumplimiento, y los términos de contrato imponen requisitos reales, sin embargo los equipos tienden a mantener cada ritual mucho después de que dejó de ganarse su lugar. Trae evidencia: para cada informe, puerta, y reunión recurrente, nombra la obligación o riesgo específico que aborda, y señala cualquiera que nadie pueda rastrear a ninguno. La respuesta debería permitirte retirar la ceremonia que solo produce tranquilidad mientras preservas los artefactos que satisfacen a un auditor o financiador real. En contextos empresariales y gubernamentales, mapea cada ceremonia a la regla específica de asignaciones, contratación pública, o regulatoria a la que sirve, para que puedas defender recortar el resto ante la supervisión en lugar de adivinar qué exige el cumplimiento.

## Perspectiva sectorial

**Startup.** Gestiona con casi ninguna ceremonia pero disciplina real. Divide el lanzamiento en porciones pequeñas y ordenadas, comprométete con una fecha de lanzamiento mientras dejas que el alcance flexione hacia un núcleo valioso, y da a los fundadores un rango en lugar de una fecha única, volviendo a pronosticar semanalmente a partir de cuántas porciones realmente cierras. Un registro de riesgo de diez líneas en un documento compartido que nombre la única dependencia que podría hundir la fecha, con un dueño y un respaldo, vale más que cualquier herramienta, porque tu recurso más escaso es la atención y un deslizamiento que detectas tarde puede acabar con la empresa.

**Pequeña empresa.** No tienes un gerente de proyecto y poco margen, así que apóyate en las herramientas que ya operas en lugar de levantar una oficina de gobernanza. Rastrea el trabajo en un único tablero visible, mantén una lista de riesgo corta y viva, y prefiere comprar un producto de programación o tickets sobre construir un proceso desde cero. Decide por adelantado qué única función debe enviarse para que valga la pena el lanzamiento, porque cuando el calendario se aprieta no tendrás gente de sobra para negociar el alcance en el momento.

**Empresa.** El problema es la coordinación entre muchos equipos, proveedores, y ciclos de financiación. Envuelve a los equipos adaptativos en una envoltura de gobernanza predictiva, alimenta los incrementos demostrados y un registro de riesgo vivo hacia el ritmo de hitos en lugar de ensamblar informes separados, y mantén un mapa de dependencias entre equipos para que la ruta crítica se gestione en lugar de descubrirse. Estandariza las estimaciones basadas en rangos y vueltas a pronosticar empíricamente en toda la cartera para que el liderazgo compare los proyectos con proyecciones honestas y que se estrechan en lugar de fechas fijas optimistas.

**Gobierno.** Las reglas de contratación pública, las asignaciones multianuales, y la rendición de cuentas pública moldean cada elección. Prefiere incrementos modulares y basados en resultados entregados adaptativamente bajo un marco de gobernanza que satisfaga las asignaciones y la supervisión, en lugar de un único contrato en cascada de precio fijo y alcance fijo con una puesta en marcha distante. Un registro de riesgo vivo e incrementos transparentes y demostrados dan a los auditores y legisladores visibilidad real, y flexionar el alcance hacia un núcleo valioso dentro de una financiación fija te permite enviar capacidad útil temprano en lugar de arriesgar todo en una fecha.

## Ejemplos

**Startup.** Una startup de siete personas corriendo para enviar su primer producto pagado gestiona el proyecto con casi ninguna ceremonia pero disciplina real. Divide el lanzamiento en porciones pequeñas y ordenadas, se compromete con una fecha de lanzamiento mientras deja que el alcance flexione hacia un núcleo valioso en lugar de prometer cada función, y da a los fundadores un rango en lugar de una fecha única, volviendo a pronosticar semanalmente a partir de cuántas porciones realmente cierra el equipo. Un registro de riesgo de diez líneas en un documento compartido nombra la única dependencia que podría hundir la fecha, una integración de pagos inacabada, con un dueño y un respaldo, así la mayor amenaza se vigila en lugar de descubrirse en el plazo.

**Empresa.** Un banco que reemplaza su plataforma de originación de préstamos ejecuta un programa híbrido: una envoltura predictiva con hitos de financiación trimestrales y puertas de cumplimiento, envolviendo equipos adaptativos que entregan incrementos funcionales cada dos semanas. Un mapa de dependencias entre equipos expone que un servicio de identidad compartido está en la ruta crítica. Así que el programa lo secuencia primero y reduce su riesgo, evitando una cascada tardía. Las estimaciones se expresan como rangos y se vuelven a pronosticar mensualmente a partir del rendimiento real, así el liderazgo ve una proyección honesta y que se estrecha en lugar de una fecha fija que se desliza silenciosamente.

**Gobierno.** Una agencia abandona un único contrato en cascada de precio fijo y alcance fijo (el patrón detrás de varios fallos públicos) por contratación modular: incrementos más pequeños y basados en resultados entregados adaptativamente bajo un marco de gobernanza que satisface las asignaciones y la supervisión. Un registro de riesgo vivo e incrementos transparentes y demostrados dan a los auditores y legisladores visibilidad real. Porque el alcance flexiona hacia un núcleo valioso dentro de una financiación fija, el programa puede enviar capacidad útil temprano en lugar de arriesgar todo en una puesta en marcha distante (capítulos 10.1, 10.3).

## Caso de negocio: motivaciones, ROI y TCO

El retorno de una buena gestión de proyectos está dominado por el **fallo evitado**. Los grandes proyectos de software son mucho más propensos a llegar tarde, exceder el presupuesto, o cancelarse que a alcanzar un plan fijo original, y las pérdidas son enormes: costo hundido, más valor renunciado, más, en el gobierno, daño público y político. Las disciplinas aquí (estimación honesta, gestión de dependencias, trabajo temprano de riesgo, partes interesadas comprometidas, y alcance adaptativo) son exactamente las que mueven un proyecto fuera de la curva de fallo. Incluso un recorte modesto en la probabilidad de un exceso o cancelación mayor empequeñece el costo de gestionar bien el proyecto.

Sobre el **costo total de propiedad**, la gestión ligera y adaptativa baja el costo a través de la vida del trabajo. La retroalimentación rápida atrapa errores costosos temprano. La entrega incremental empieza a retornar valor antes, lo cual mejora el tiempo del ROI. El flujo transparente reduce la sobrecarga de reporte que impone la gobernanza pesada. Tanto la *sub*gestión (caos, retrabajo, dependencias perdidas) como la *sobre*gestión (ceremonia que ralentiza la entrega) llevan un costo real. La meta es el proceso más ligero que cumpla tus obligaciones reales. Presenta el caso al liderazgo contrastando el costo completo de un proyecto problemático reciente con el costo casi cero de un registro de riesgo, un mapa de dependencias, y pronósticos honestos basados en rangos.

## Antipatrones y trampas

- **Planes de todo fijo:** el alcance, calendario, y costo todos bloqueados, con la calidad como la válvula de escape silenciosa.
- **Estimaciones como promesas:** fechas de número único tratadas como compromisos, luego defendidas más allá de la evidencia.
- **Ignorar las dependencias:** gestionar la velocidad de cada equipo mientras la ruta crítica entre equipos se desliza.
- **Teatro del registro de riesgo:** un documento creado una vez y nunca revisitado.
- **Estado de sandía:** verde por fuera, rojo por dentro; el optimismo premiado sobre la honestidad.
- **Cliente ausente:** ninguna parte interesada comprometida, así se construye confiadamente lo equivocado.
- **Entrega de gran explosión:** todo integrado y liberado al final, maximizando el riesgo (contraste el capítulo 11.2).
- **Proceso por sí mismo:** ceremonia e informes que consumen esfuerzo sin reducir el riesgo.

## Modelo de madurez

- **Nivel 1 (Iniciar):** Los proyectos corren con heroísmo y esperanza; el alcance, el riesgo, y las dependencias se gestionan ad hoc si acaso; las estimaciones son números únicos defendidos más allá de la evidencia; las sorpresas llegan en el plazo.
- **Nivel 2 (Desarrollar):** Existe planificación básica, reporte de estado, y una lista de riesgo en algunos proyectos pero no en otros; el método de entrega se elige por hábito en lugar de ajuste; la estimación y el rastreo de dependencias varían por equipo, así la práctica es inconsistente en toda la organización.
- **Nivel 3 (Estandarizar):** Un enfoque documentado se aplica en toda la organización: el método de entrega se elige para ajustarse al trabajo, el alcance se gestiona contra la triple restricción, se espera un registro de riesgo vivo y un mapa de dependencias en cada proyecto, y las estimaciones se basan en rangos y se vuelven a pronosticar con partes interesadas comprometidas.
- **Nivel 4 (Gestionar):** La entrega se mide y controla contra líneas base. El rendimiento, el tiempo de ciclo, la exactitud del pronóstico, las tasas de cierre de dependencias y riesgo, y la varianza de calendario y costo se rastrean por proyecto y se agregan a través de la cartera; las proyecciones son empíricas y que se estrechan; los deslizamientos aparecen temprano y disparan el reajuste de alcance o línea base con base en evidencia en lugar de optimismo.
- **Nivel 5 (Orquestar):** La gestión de proyectos se integra con la planificación de cartera, financiación, y riesgo y se mejora continuamente. La gobernanza híbrida satisface la supervisión sin ralentizar la entrega, las dependencias entre equipos y proveedores se gestionan proactivamente, las retrospectivas alimentan el cambio medido de vuelta a la práctica, y la organización adapta sus métodos y reequilibra el trabajo a medida que cambian las restricciones y prioridades.

## Ideas para el debate

1. ¿Qué método de entrega (predictivo, adaptativo, híbrido) realmente necesita cada una de tus iniciativas actuales, y coincide con lo que estás usando?
2. Cuando te comprometiste por última vez con una fecha, ¿fue un rango o un número único, y cómo moldeó eso las expectativas?
3. ¿Cuál es la dependencia de ruta crítica entre tus equipos ahora mismo, y quién es dueño de reducir su riesgo?
4. ¿Es tu registro de riesgo un hábito vivo o un documento de una sola vez?
5. ¿Dónde está la calidad silenciosamente absorbiendo la presión cuando el alcance, calendario, y costo están todos fijos?
6. ¿Cómo cambiarían tus pronósticos si reemplazaras la estimación con el rendimiento medido?

## Puntos clave

- La gestión de proyectos convierte la intención en resultados entregados bajo la restricción de alcance-calendario-costo-calidad.
- **Ajusta el método al trabajo:** predictivo, adaptativo, o híbrido, y prefiere la gobernanza híbrida en la empresa/gobierno.
- Trata las **estimaciones como rangos**, vuelve a pronosticar a partir de **métricas de flujo empíricas**, y no dejes que las fechas de número único se conviertan en mentiras.
- Las **dependencias y el riesgo** son los modos de fallo dominantes a escala: mapea y gestiona ambos continuamente.
- Mantén a las **partes interesadas comprometidas** y el estado **transparente**; haz que las malas noticias viajen rápido.
- El ROI es el fallo evitado; el proceso más ligero que cumpla tus obligaciones gana. Véanse los capítulos 10.7 (Ágil), 10.1 (gestión de cartera y programa), 11.2 (entrega), y 11.3 (teoría de colas).

## Referencias y lecturas adicionales

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (por qué añadir gente a un proyecto tardío lo retrasa más).
- Tom DeMarco y Timothy Lister, *Peopleware* y *Waltzing with Bears* (gestión de riesgo).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (pronóstico empírico).
- Standish Group, *CHAOS Report* (resultados de proyectos de software, leer críticamente).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (entrega moderna del sector público).
- Bent Flyvbjerg y Dan Gardner, *How Big Things Get Done* (entrega de megaproyectos).
