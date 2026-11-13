# 5.2 Diseño de interfaz y sistemas de diseño

## Visión general y motivación

El [diseño de interfaz de usuario (UI)](https://en.wikipedia.org/wiki/User_interface_design) es el oficio de dar forma a lo que la gente ve y toca: distribución, [tipografía](https://en.wikipedia.org/wiki/Typography), color, espaciado, controles y estados. Un [sistema de diseño](https://en.wikipedia.org/wiki/Design_system) toma ese oficio y lo convierte en un activo compartido, reutilizable y gobernado: un conjunto documentado de principios, componentes, patrones y tokens del que todo equipo puede servirse, para que el producto en su conjunto tenga un aspecto y un comportamiento coherentes. El diseño de UI decide cómo debe verse una pantalla. Un sistema de diseño decide cómo diez mil pantallas repartidas entre muchos equipos mantienen su coherencia.

En una gran organización, el sistema de diseño es la inversión de mayor impacto en calidad de interfaz y velocidad de entrega. Sin uno, cada equipo reinventa los botones, los formularios, los diálogos modales y el tratamiento de errores, cada vez ligeramente distinto, cada uno mantenido por separado, cada uno roto por separado. Los usuarios pagan esa factura en forma de confusión y desconfianza; el negocio, en esfuerzo duplicado y calidad desigual. Un sistema de diseño convierte las decisiones de diseño de una sola vez en capital reutilizable: se resuelven la [accesibilidad](https://en.wikipedia.org/wiki/Accessibility), la [adaptabilidad](https://en.wikipedia.org/wiki/Responsive_web_design) y la marca una única vez en un componente, y cada equipo hereda el resultado.

El ámbito empresarial y el gubernamental añaden dos presiones específicas. Primero, la escala: cientos de aplicaciones, muchas desarrolladas por proveedores o adquiridas mediante fusiones, todas las cuales deben sentirse como parte de una misma organización. Segundo, la longevidad y el cambio: las marcas se renuevan, los organismos se reorganizan y una plataforma puede necesitar servir a varias marcas o subagencias a partir de una sola base de código. Un sistema de diseño bien arquitecturado, con una tematización y una tokenización adecuadas, convierte esos cambios de gran alcance en manejables en lugar de catastróficos.

## Principios fundamentales

- La coherencia reduce la [carga cognitiva](https://en.wikipedia.org/wiki/Cognitive_load); un botón debe verse y comportarse igual en todas partes.
- Las decisiones de diseño son activos: captúrense una vez como componentes y tokens reutilizables.
- Los tokens son la fuente de la verdad para las decisiones visuales; los componentes consumen tokens, nunca valores codificados.
- La accesibilidad y la adaptabilidad se construyen dentro de los componentes, no se añaden pantalla a pantalla.
- Un sistema de diseño es un producto con usuarios (desarrolladores y diseñadores), no un entregable de una sola vez.
- La jerarquía visual guía la atención: el tipo, el color y el espacio deben hacer evidente qué es lo importante.
- La gobernanza mantiene coherente al sistema; la contribución lo mantiene vivo.

## Recomendaciones

### Estructure el sistema por capas: tokens, componentes, patrones

Los tokens de diseño son valores con nombre y agnósticos de plataforma para color, espaciado, tipografía, radios, elevación y movimiento: las decisiones atómicas. Constrúyalos en niveles: una paleta primitiva (valores en bruto), tokens semánticos (`color-action-primary`, `space-inset-md`) que portan significado, y tokens a nivel de componente donde realmente se necesiten. Los componentes consumen los tokens semánticos, de modo que un solo cambio se propaga a todas partes. Sobre los componentes se sitúan los patrones: composiciones probadas como una tabla de datos, un formulario de varios pasos o un estado vacío. Documente las tres capas en un mismo lugar, con ejemplos en vivo y orientaciones de uso.

### Domine los fundamentos visuales

Establezca una escala tipográfica con jerarquía clara y generoso interlineado para la legibilidad, y limite el número de tamaños y pesos. Defina el color como un sistema, con suficiente contraste para la accesibilidad (véase el capítulo de accesibilidad) y roles semánticos, en lugar de tonos sueltos repartidos por la interfaz. Use una escala de espaciado y una cuadrícula de diseño para que el alineado y el ritmo se mantengan consistentes sin tanteos pantalla por pantalla. La jerarquía visual debe hacer obvios de un vistazo la acción primaria y la información más relevante.

### Diseñe de forma responsiva y con enfoque móvil

Diseñe primero para la ventana más pequeña razonable y luego mejore para pantallas más grandes. Esto obliga a priorizar el contenido y los controles esenciales. Use diseños fluidos y unidades relativas para que las interfaces se adapten a cualquier pantalla, en lugar de saltar entre unos pocos puntos de corte fijos. Asegúrese de que los objetivos táctiles sean lo bastante grandes y de que las interacciones funcionen con el dedo, con el ratón y con el teclado. En el ámbito gubernamental, asuma que una parte significativa de los usuarios accede desde dispositivos pequeños, antiguos o de bajo coste.

### Haga de la entrega entre diseño y desarrollo, y de la paridad, una prioridad de primera clase

Un sistema de diseño solo rinde frutos cuando la interfaz que llega al usuario coincide con el diseño previsto y sigue coincidiendo. Apunte a una única fuente de la verdad: los tokens exportados desde la herramienta de diseño fluyan directamente al código, para que diseñadores e ingenieros referencien los mismos valores. Proporcione una biblioteca de componentes en código que los ingenieros realmente usen, con los mismos nombres y propiedades que los componentes de diseño. Emplee pruebas de regresión visual (comparación automática de la interfaz renderizada contra imágenes de referencia aprobadas) y controles de revisión de diseño para detectar desviaciones. Y mida la «paridad entre diseño y código» como una métrica explícita de salud: el porcentaje de interfaz construida a partir de componentes del sistema frente a código único.

### Apoye la tematización y la marca blanca a escala empresarial

Diseñe desde el principio para múltiples marcas si existe la menor posibilidad de necesitarlas. Dado que los componentes consumen tokens semánticos, un tema no es más que un conjunto distinto de valores de tokens, de modo que una renovación de marca o una nueva submarca se convierte en un cambio de datos, no en una reescritura de código. Apoye temas claro y oscuro, modos de alto contraste y marca por inquilino a través del mismo mecanismo. Mantenga la lógica de marca fuera de los componentes y transfírala a los conjuntos de tokens y a la configuración.

### Gobiérnese el sistema como un producto

Asigne al sistema de diseño un equipo dedicado, una hoja de ruta, versionado, un registro de cambios y un canal de soporte. Defina con claridad cómo los equipos aportan nuevos componentes y cómo se revisan y promueven. Equilibre el control central (para preservar coherencia y accesibilidad) con un modelo de contribución (para que el sistema evolucione con necesidades reales y no se convierta en un cuello de botella). Comunique las deprecaciones y migraciones con claridad y brinde a los equipos consumidores tiempo suficiente de anticipación.

## Compromisos: ventajas e inconvenientes

| Decisión | Ventajas | Inconvenientes |
|---|---|---|
| Crear un sistema de diseño | Coherencia, velocidad, accesibilidad resuelta una vez, renovación de marca más sencilla | Coste inicial y continuado, requiere equipo dedicado |
| Adoptar un sistema del mercado | Arranque rápido, patrones probados | Aspecto genérico, más difícil de adaptar a marca y necesidades propias |
| Gobernanza central estricta | Coherencia, calidad y accesibilidad garantizadas | Puede crear cuellos de botella, sensación de burocracia |
| Modelo de contribución abierta | Evoluciona con necesidades reales, responsabilidad compartida | Riesgo de desviación e inconsistencia sin revisión |
| Tokenización y tematización intensivas | Renovaciones de marca baratas y soporte multimarca | Mayor abstracción, curva de aprendizaje más pronunciada |

Los sistemas de diseño intercambian coste inicial y de gobernanza por coherencia y velocidad a largo plazo. Para un producto pequeño con un solo equipo, la inversión puede no compensarse. Para una gran organización con muchos equipos y productos de larga vida, la pregunta no es si se necesita un sistema, sino cuánto invertir y cómo gobernarlo. El arrepentimiento más frecuente es invertir de menos en gobernanza y en herramientas de paridad: el sistema existe en papel, pero los equipos se alejan de él en silencio.

## Preguntas para debatir con el equipo

1. **¿Cómo está estructurada nuestra arquitectura de tokens y está prohibido que los componentes usen valores codificados?** Todo el beneficio de un sistema de diseño (renovaciones de marca a bajo coste, tematización multimarca, accesibilidad resuelta una sola vez) depende de que los componentes consuman tokens semánticos como `color-action-primary` en lugar de tonos y valores en píxeles repartidos por el código. Fijemos ahora los niveles: una paleta primitiva, tokens semánticos que porten significado y tokens a nivel de componente solo donde realmente se necesiten. La sobreabstracción es un riesgo real, así que acordemos cuántas capas son demasiadas y cómo un desarrollador encuentra rápidamente el token correcto. Aportemos como evidencia un registro de colores y espaciados codificados en nuestro base de código que demuestre la desviación. Si la lógica de marca está impregnada en los componentes, una renovación de marca se convierte en una reescritura de código en lugar de un cambio de configuración, que es precisamente el desastre que la tokenización pretende evitar.

2. **¿Cómo medimos y defendemos la paridad entre diseño y código, y qué herramientas detectan la desviación automáticamente?** Un sistema de diseño que existe solo como archivo de diseño es una hoja de pegatinas: los ingenieros lo reconstruyen todo de todos modos y la interfaz publicada se aleja poco a poco de la intención. Acordemos una métrica explícita de paridad (el porcentaje de interfaz construida a partir de componentes del sistema frente a código único) e integremos pruebas de regresión visual en la integración continua, para que las pantallas renderizadas se comparen contra referencias aprobadas. Esto importa a escala empresarial y gubernamental porque cientos de aplicaciones, muchas construidas por proveedores o heredadas por fusiones, deben sentirse como parte de una sola organización. Aportemos la cifra actual de paridad y una lista de los componentes propios que los equipos siguen reconstruyendo. Si nadie es responsable de la métrica ni de la suite de regresión, la desviación ya está ganando en silencio.

3. **¿Cómo gobernamos la contribución, la depreciación y la migración para que el sistema ni frene a los equipos ni se fragmente?** Un control central estricto garantiza coherencia y accesibilidad, pero puede convertir al equipo del sistema de diseño en un cuello de botella que los equipos esquivan; la contribución abierta mantiene el sistema vivo, pero arriesga variantes divergentes sin revisión. Definamos la vía de contribución: cómo un equipo propone un componente nuevo, quién lo revisa y cómo se promueve. Igualmente, acordemos cómo se comunican los cambios incompatibles, porque las deprecaciones sin soporte de migración y tiempo de anticipación hacen que los equipos consumidores se paralicen o forquen el sistema. Aportemos ejemplos de componentes que los equipos construyeron fuera del sistema y preguntémonos por qué no los aportaron de vuelta. La respuesta suele revelar si la gobernanza es un servicio o un obstáculo.

4. **¿Cómo garantizamos que la accesibilidad se resuelve una vez dentro de los componentes y qué impide que un equipo publique un componente inaccesible a medida?** El argumento más fuerte a favor de un sistema de diseño es que el contraste cromático, los estados de foco, la operación por teclado y la semántica para lectores de pantalla se resuelvan una vez y se hereden en todas partes, pero esa promesa se derrumba en el momento en que los equipos fabrican sus propios controles. En una gran organización es donde reside el mayor riesgo legal y reputacional, porque un único formulario de pago o selector de fechas inaccesible puede bloquear a usuarios reales y generar reclamaciones en todos los productos que lo copiaron. Pensemos en el equilibrio entre la aplicación central (componentes accesibles junto con un analizador o una puerta de revisión que rechace el marcado en crudo) y la autonomía del equipo, y decidamos dónde está la línea roja. Aportemos los resultados de una auditoría de accesibilidad, una lista de componentes con su estado de conformidad y el recuento de controles propios que los equipos reconstruyeron fuera del sistema. En entornos empresariales y gubernamentales esto no es un detalle: obligaciones como WCAG, Section 508 y EN 301 549 convierten la conformidad en un requisito de contratación y auditoría, de modo que una biblioteca de componentes con conformidad documentada es en sí misma un activo de cumplimiento.

5. **¿Cuántas marcas, inquilinos y temas debe servir este sistema, y hemos arquitecturado la capa de tokens para eso ahora en lugar de tener que adaptarla después?** La tematización es barata si se diseñó para ella y brutal si no, porque una marca o inquilino no previsto obliga a reintroducir la lógica de marca en los componentes y deshace todo el sentido de la tokenización. Para un equipo grande, esta decisión condiciona años de trabajo: una plataforma que debe servir a varias marcas, un tema claro y otro oscuro, un modo de alto contraste y marca por inquilino necesita una capa de tokens semánticos lo bastante limpia para que un tema sea solo un conjunto distinto de valores. Equilibremos esa flexibilidad con la sobreabstracción, pues un árbol de tokens que nadie puede navegar es en sí mismo un fracaso. Aportemos la hoja de ruta de marcas e inquilinos que podamos prever, el número de temas en juego hoy y los componentes que ya filtran lógica específica de marca. En contextos empresariales y gubernamentales, las fusiones, adquisiciones y reorganizaciones de organismos añaden con frecuencia marcas que no se planearon, por lo que arquitecturar para la multimarca desde el principio es la diferencia entre un cambio de datos y una reescritura que dura años.

6. **¿Cómo migraremos las aplicaciones heredadas y las construidas por proveedores al sistema, y cómo financia al equipo del sistema de diseño para que sobreviva al próximo ciclo presupuestario?** Un sistema de diseño solo entrega su retorno cuando los productos reales lo adoptan, y las aplicaciones más difíciles de convertir son precisamente las antiguas y las externalizadas que más lo necesitan, y el equipo que lo mantiene suele ser el primero en recortarse cuando los presupuestos se aprietan. En una gran organización hay que decidir entre una migración masiva de un solo golpe y una incremental, y cómo lograr que los proveedores construyan sobre los componentes del sistema en lugar de en paralelo. Aportemos un inventario de aplicaciones con su puntuación actual de paridad, una estimación del esfuerzo de migración por aplicación y las palancas contractuales que se tienen sobre los proveedores. En entornos empresariales y gubernamentales, incorporemos la conformidad con el sistema de diseño en los términos de contratación para que el nuevo trabajo de los proveedores aterrice en el sistema por defecto, y financie al equipo de mantenimiento como infraestructura compartida y duradera, porque un sistema que pierde a sus custodios en una reorganización retrocede a la fragmentación en el plazo de un año.

## Perspectiva por sector

**Startup.** Con dos o tres ingenieros y sin holgura de horizonte, no construya un sistema gobernado. Dedique un par de días a definir un pequeño conjunto de tokens semánticos para color, espaciado y tipografía, más una docena de componentes compartidos, todo en un único archivo que todo el equipo referencia. Apóyese en una biblioteca de componentes estándar para las partes difíciles y no deje nada codificado, de modo que la primera renovación de marca con criterio de diseño sea un cambio de tokens y no una reescritura.

**Pequeña empresa.** Sin diseñador dedicado y con presupuesto ajustado, compre en lugar de construir: adopte una biblioteca de componentes o un kit de interfaz probado y tematícelo con ligereza a su marca. El objetivo es un producto coherente y accesible sin tener que dotar de un equipo de sistema de diseño, así que prefiera un sistema que ofrezca accesibilidad y adaptabilidad de serie. Resista la tentación de forkearlo, porque una copia personalizada que no puede mantenerse se convierte en un pasivo en cuanto el proyecto original avanza.

**Empresa.** El problema es la coherencia entre muchos equipos y productos de larga vida, así que trate el sistema de diseño como infraestructura compartida gobernada, con equipo dedicado, versionado y hoja de ruta. Ponga la paridad entre diseño y código como métrica real, integre pruebas de regresión visual en la integración continua y arquitectura la capa de tokens para múltiples marcas y temas desde el principio. Presupueste explícitamente el coste de gobernanza y migración, y gestione la adopción como un portafolio en lugar de suponer que los equipos se sumarán al sistema por su cuenta.

**Administración pública.** Las normas de contratación, la transparencia y la rendición de cuentas pública condicionan cada decisión. La conformidad con estándares de accesibilidad como WCAG, Section 508 y EN 301 549 es un requisito legal, no una preferencia, de modo que una biblioteca de componentes con conformidad documentada se convierte en un activo de cumplimiento. Prefiera o extienda un sistema de diseño público compartido para que los ciudadanos encuentren los mismos patrones en todos los servicios, incorpore el uso del sistema de diseño en los contratos con proveedores y publique componentes y orientaciones de forma abierta para que los organismos y sus suministradores puedan adoptarlos y ser evaluados contra ellos.

## Ejemplos

**Startup.** Una startup de dos ingenieros no dejaba de reconstruir botones y campos de formulario ligeramente distintos en cada pantalla nueva, y el producto empezaba a tener un aspecto de remiendos. En lugar de un sistema pesado, dedicaron dos días a definir un pequeño conjunto de tokens de diseño semánticos para color, espaciado y tipografía, más unas doce componentes compartidos, todo en un único archivo que todo el equipo referenciaba. Como no había nada codificado, cuando su primera contratación con sensibilidad de diseño propuso una paleta más pulida, la renovación fue un cambio de tokens que se implantó en toda la aplicación en una tarde, en lugar de un tedioso trabajo pantalla por pantalla.

**Empresa.** Una compañía de software global con decenas de equipos de producto construyó un sistema de diseño tokenizado con una biblioteca de componentes compartida en código. Los tokens semánticos les permitieron lanzar una renovación completa de marca en todas las plataformas en cuestión de semanas, en lugar de un interminable proceso de varios años por equipo, porque el cambio fue un nuevo conjunto de tokens y no miles de ediciones de color codificado. La paridad entre diseño y código, seguida como métrica en un tablero, aumentó a medida que los equipos reemplazaban componentes propios, lo que redujo el mantenimiento duplicado de la interfaz.

**Administración pública.** Un gobierno nacional creó un sistema de diseño común para los servicios públicos (componentes, patrones y accesibilidad integrados) e impuso su uso en todos los organismos. Un ciudadano que pasa de un servicio fiscal a un servicio sanitario y a un servicio de licencias se encuentra con el mismo encabezado, los mismos controles de formulario y los mismos patrones de error, lo que genera confianza y acorta la curva de aprendizaje. Los organismos y sus proveedores publican más rápido y con mayor accesibilidad porque los problemas difíciles se resuelven de forma centralizada, y el gobierno puede actualizar orientaciones o corregir problemas de accesibilidad una sola vez y verlos propagarse a todos lados.

## Casos de negocio: motivaciones, retorno y coste total de propiedad

El retorno de un sistema de diseño proviene de eliminar la duplicación y acelerar la entrega. En lugar de que cada equipo diseñe y construya los mismos componentes, los compone a partir de una biblioteca compartida, lo que acelera mediblemente la entrega y libera a diseñadores e ingenieros para el trabajo propio del producto. La accesibilidad y la adaptabilidad, resueltas una vez en los componentes, ahorran el coste de remediación proyecto por proyecto. Las renovaciones de marca y la tematización que antes llevaban años ahora llevan semanas.

En cuanto al coste total de propiedad, el coste de adopción es un equipo dedicado, herramientas y el esfuerzo para que los productos existentes se migren al sistema. El coste de no adoptar se paga de forma continua: construcción y mantenimiento duplicados entre equipos, interfaces inconsistentes e inaccesibles que generan riesgo de soporte y legal, y renovaciones de marca lentas y caras. Dado que la duplicación se reparte en los presupuestos de muchos equipos, resulta fácil pasarla por alto: un sistema de diseño hace ese coste oculto visible y lo recoge en un solo lugar.

Para presentar el caso a la dirección, cuantifiquemos el trabajo de componentes duplicado entre equipos, la ganancia en tiempo de llegada al mercado gracias a la composición y el coste y la duración de la última renovación de marca frente a lo que un sistema tokenizado permitiría. Presentemos el sistema como infraestructura compartida con una métrica de adopción medible (porcentaje de paridad), para que su valor se pueda seguir en el tiempo en lugar de simplemente afirmarse.

## Antipatrones y errores frecuentes

- **Sistema de diseño como hoja de pegatinas:** un archivo de diseño estático sin componentes en código, de modo que los ingenieros reconstruyen todo de todos modos.
- **Valores codificados por todas partes:** colores y espaciados repartidos por el código, haciendo imposible la tematización y las renovaciones de marca.
- **Ausencia de gobernanza:** el sistema se fragmenta a medida que los equipos añaden variantes divergentes; la coherencia se erosiona.
- **Gobernanza sin contribución:** el equipo central se convierte en un cuello de botella y los equipos lo esquivan.
- **Ignorar la paridad:** la interfaz codificada se aleja de la intención de diseño y nadie mide la brecha.
- **Sobreabstracción:** tantos tokens y capas que nadie encuentra ni utiliza el adecuado.
- **Lógica de marca impregnada en los componentes:** convierte la multimarca y la tematización en una reescritura de código en lugar de un cambio de configuración.
- **Cambios incompatibles sin soporte de migración:** los equipos consumidores se paralizan o forkean el sistema.

## Modelo de madurez

**Nivel 1: Iniciar.** Cada equipo construye su interfaz de forma ad hoc y reactiva. No hay componentes compartidos, el aspecto y el comportamiento son inconsistentes, y los colores y el espaciado están codificados pantalla a pantalla. Cada renovación de marca es un tedioso trabajo manual, pantalla por pantalla.

**Nivel 2: Desarrollar.** Existe una guía de estilo o biblioteca de componentes compartida, pero es parcial, opcional y a menudo desincronizada entre diseño y código. Algunos equipos la usan, otros no, y las prácticas básicas varían enormemente de un equipo a otro.

**Nivel 3: Estandarizar.** Un sistema de diseño tokenizado, con biblioteca de código mantenida, documentación y gobernanza, está documentado y aplicado en toda la organización. Los componentes consumen tokens semánticos, se admite la tematización, y la accesibilidad y la adaptabilidad se construyen en lugar de añadirse pantalla a pantalla.

**Nivel 4: Gestionar.** El sistema se mide y controla con datos frente a líneas base. La paridad entre diseño y código se sigue como métrica explícita con objetivos por producto, las pruebas de regresión visual se ejecutan en la integración continua para detectar desviaciones, y la conformidad de accesibilidad se mide contra estándares en lugar de suponerse. Los tableros de adopción muestran la cobertura de componentes por equipo, y el coste y la duración de las renovaciones de marca se registran para que la mejora sea visible en el tiempo.

**Nivel 5: Orquestar.** El sistema de diseño es un producto de mejora continua, integrado en toda la organización y adaptable al cambio. Tiene versionado, hoja de ruta y un modelo de contribución funcional, de modo que evoluciona con necesidades reales. Las renovaciones de marca y los nuevos temas son cambios de tokens rutinarios, la tematización multi-marca y multi-inquilino es lo normal, y el equipo jubila, reaborda y promueve patrones en función de datos de uso, alimentando herramientas de diseño y líneas de entrega desde una única fuente de la verdad.

## Ideas para debatir

- ¿Cómo se equilibra la gobernanza central con la autonomía de los equipos sin fragmentar ni crear cuellos de botella?
- ¿Cuál es la métrica adecuada para la «paridad entre diseño y código» y cómo se mantiene honesta?
- ¿Cuándo debe permitirse a un equipo construir un componente a medida en lugar de usar el del sistema?
- ¿Cómo se financia y dota de personal a un sistema de diseño para que sobreviva a los ciclos presupuestarios y a las reorganizaciones?
- ¿Cuánta flexibilidad de tematización justifica el coste añadido de abstracción?
- ¿Cómo se migran las aplicaciones heredadas y las construidas por proveedores a un sistema compartido?

## Conclusiones clave

- Un sistema de diseño convierte las decisiones de diseño de una sola vez en capital reutilizable y gobernado.
- Estructurelo por capas (tokens, componentes, patrones), con los componentes consumiendo tokens semánticos.
- Construya la accesibilidad y la adaptabilidad dentro de los componentes para que cada equipo las herede.
- Trate la paridad entre diseño y código como una métrica de salud medible, no como una suposición.
- La tokenización convierte las renovaciones de marca y la tematización multimarca en un cambio de datos, no en una reescritura.
- Gobiérnese el sistema como un producto con hoja de ruta, versionado y modelo de contribución.
- A escala empresarial y gubernamental, un sistema compartido es la inversión de mayor impacto en interfaz disponible.

## Referencias y lecturas adicionales

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, escritos sobre tokens de diseño y gobernanza de sistemas de diseño
- W3C Design Tokens Community Group, especificación de formato
- Sistemas de diseño gubernamentales (p. ej., Government Design System del Reino Unido, U.S. Web Design System) como implementaciones de referencia

