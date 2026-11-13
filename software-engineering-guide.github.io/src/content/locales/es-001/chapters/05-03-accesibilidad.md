# 5.3 Accesibilidad

## Visión general y fundamentos

La [accesibilidad](https://en.wikipedia.org/wiki/Accessibility) (abreviada habitualmente como «a11y») consiste en diseñar y construir software que personas con discapacidad puedan percibir, comprender, navegar y utilizar. Esto incluye a personas con ceguera o baja visión, con sordera o hipoacusia, con limitaciones motoras, con diferencias cognitivas o del aprendizaje, y quienes enfrentan restricciones temporales o situacionales, como un brazo roto, luz solar intensa o un entorno ruidoso. Una de cada cinco personas tiene alguna discapacidad, y todo el mundo se beneficia del diseño accesible en algún momento de su vida. No se trata de una concesión de nicho: es un estándar mínimo de calidad.

En equipos grandes, la accesibilidad debe integrarse en el sistema, no dejarse al buen criterio individual. Cuando numerosos equipos publican dentro de un mismo producto, un solo componente inaccesible (un campo de formulario sin etiqueta, un indicador de estado que solo usa color, una trampa de teclado en un cuadro de diálogo) puede dejar a un usuario con discapacidad fuera de todo un flujo. Incorporar la accesibilidad en los componentes compartidos, en los tokens de diseño, en las pipelines de pruebas y en los criterios de aceptación es la única forma de hacerla fiable a gran escala. Adaptarla con posterioridad es costoso y propenso a errores; diseñarla desde el inicio es económico y perdurable.

En el sector público, la accesibilidad es un requisito legal y una obligación cívica, no una opción. Los servicios públicos deben atender a cada ciudadano, y las personas con discapacidad a menudo no tienen un proveedor alternativo: si el sitio del gobierno no es accesible, no puede solicitar su pensión, tramitar su licencia o emitir su voto de otra manera. Las leyes y normas de todo el mundo exigen la accesibilidad a los organismos públicos y, cada vez más, también al sector privado. Este capítulo aborda la accesibilidad como tres cosas a la vez: un deber legal, un deber ético y, simplemente, buen diseño.

*Véase también:* capítulo 5.2 (diseño de interfaz y sistemas de diseño), capítulo 5.6 (ingeniería frontend) y capítulo 5.1 (fundamentos de experiencia de usuario).

## Principios clave

- La accesibilidad es un atributo de calidad de nivel base, como la seguridad y el rendimiento, no una función opcional.
- Los principios POUR: las interfaces deben ser **P**ercibibles, **O**perables, **E**ntendibles y **R**obustas.
- Empezar por [HTML semántico](https://en.wikipedia.org/wiki/Semantic_HTML); usar [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) solo para cubrir lagunas genuinas, nunca como sustituto de elementos nativos.
- Todo lo que se pueda usar con un ratón debe poder usarse solo con teclado.
- No transmitir información basándose únicamente en color, forma o posición.
- Las herramientas automatizadas detectan solo una fracción de los problemas; la revisión manual y la prueba con [tecnologías de apoyo](https://en.wikipedia.org/wiki/Assistive_technology) son imprescindibles.
- El diseño accesible es mejor diseño para todos (el [«efecto acera,»](https://en.wikipedia.org/wiki/Curb_cut) por el que las funciones creadas para personas con discapacidad benefician a todos los usuarios).
- Diseñar y probar con personas con discapacidad, no solo para ellas.

## Recomendaciones

### Diseñar y construir según WCAG, apuntando al estándar actual

Las [Pautas de Accesibilidad para el Contenido Web](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) son la referencia internacional. Las versiones 2.1 y 2.2 se organizan bajo los cuatro principios POUR, con criterios de éxito comprobables en niveles de conformidad A, AA y AAA. Apuntar al nivel AA como base: es lo que la mayoría de las leyes citan. La versión 2.2 añade criterios sobre visibilidad del foco, tamaño de los objetivos interactivos y reducción de la carga cognitiva. La WCAG 3.0 es una sucesora emergente, con una estructura diferente y aún en desarrollo. Manténganse al tanto, pero construyan bajo 2.2 AA hoy. Traten las pautas como un piso, no como un techo: cumplir cada criterio no garantiza una experiencia realmente usable.

### Usar HTML semántico y ARIA correcto

Los elementos HTML nativos (botones, enlaces, controles de formulario, encabezados, listas, puntos de referencia) vienen con semántica de accesibilidad integrada, comportamiento de teclado y compatibilidad con tecnologías de apoyo. Úsenlos primero. Recurren a los roles, estados y propiedades ARIA (Aplicaciones Rich Accesibles) solo para describir widgets personalizados que HTML no puede expresar, y sigan las Prácticas de Autoría ARIA. La primera regla de ARIA es sencilla: no usen ARIA si un elemento nativo lo resuelve. Un ARIA incorrecto es peor que no usar ninguno: desorienta activamente a los [lectores de pantalla](https://en.wikipedia.org/wiki/Screen_reader). Proporcien a cada página una estructura de encabezados lógica, etiquetas con significado, texto alternativo para imágenes, subtítulos y transcripciones para medios, y un vínculo programático entre cada etiqueta y su control.

### Garantizar la operabilidad por teclado y con tecnologías de apoyo

Cada elemento interactivo debe poder alcanzarse y operarse solo con el teclado, en un orden lógico, con un indicador de foco claramente visible. Eviten las trampas de teclado. Gestionen el foco de forma deliberada cuando el contenido cambia: desplacen el foco a un cuadro de diálogo al abrirlo, devuélvanlo al cerrarlo y anuncien las actualizaciones dinámicas a través de regiones activas. Prueben con tecnologías de apoyo reales: lectores de pantalla en escritorio y móvil, ampliación de pantalla, control por voz y acceso con conmutadores. Y respeten las preferencias del usuario, como la reducción del movimiento o el aumento de contraste.

### Probar con herramientas automatizadas, revisión manual y usuarios reales

Los escáneres de accesibilidad automatizados son valiosos y deben ejecutarse en la pipeline con cada cambio. Sin embargo, los estudios muestran consistentemente que detectan solo una minoría de los problemas reales, aproximadamente un tercio. El resto exige criterio humano: recorridos por teclado, pruebas con lector de pantalla, verificación de contraste y preguntarse si el contenido es realmente comprensible. Lo más importante de todo: incluyan a personas con discapacidad en las pruebas de usabilidad. Incorporen criterios de aceptación de accesibilidad en la definición de completitud de cada historia, para que los problemas se detecten en cada entrega y no en una auditoría previa al lanzamiento.

### Hacer de la accesibilidad una responsabilidad organizativa, no heroica

Integren la accesibilidad en el sistema de diseño para que los componentes se publicuen accesibles por defecto. Ofrezcan formación para que diseñadores, ingenieros, autores de contenido y directores de producto sepan cada uno qué les corresponde. Establezcan un estándar de accesibilidad, un responsable o centro de excelencia, y un proceso de remediación. Publiquen una declaración de accesibilidad y ofrezcan a los usuarios un canal para reportar barreras. Y adquieran de forma accesible: exijan que proveedores y componentes de terceros cumplan las normas y que aporten evidencia (como un informe de conformidad de accesibilidad).

## Ponderaciones: ventajas e inconvenientes

| Enfoque | Ventajas | Inconvenientes |
|---|---|---|
| Integrar la accesibilidad desde el inicio | Más económico, perdurable, mejor para todos | Exige formación y disciplina previas |
| Remediación o adaptación posterior | Difería el esfuerzo, libera un lanzamiento rápido | Mucho más costoso, frágil, con exposición legal en el interíno |
| Solo pruebas automatizadas | Rápido, económico, detecta regresiones en CI | Se pierde cerca de dos tercios de los problemas; genera falsa confianza |
| Pruebas manuales + tecnologías de apoyo | Detecta barreras de usabilidad reales | Más lento, requiere testers cualificados y dispositivos |
| Pruebas con usuarios con discapacidad | Fuente de verdad sobre la experiencia real | Esfuerzo y coste de reclutamiento; debe hacerse con respeto |

La ponderación central es la disciplina anticipada frente al coste diferido. La accesibilidad integrada es económica y mejora la calidad para todos; la accesibilidad remediada bajo presión legal es costosa, incompleta y estresante. A largo plazo no existe una verdadera compensación frente a la «velocidad»: un software inaccesible simplemente no funciona para un quinto de los usuarios. Eso es un defecto, no un ahorro.

## Preguntas para debatir con su equipo

1. **¿Las regresiones de accesibilidad fallan nuestra build como fallaría una prueba rota, y si no, por qué?** Los escáneres automatizados detectan apenas un tercio de los problemas, pero los que sí detectan (etiquetas ausentes, fallos de contraste, controles sin etiqueta) son baratos de atrapar en CI y caros de encontrar en una auditoría previa al lanzamiento. Tratar una regresión como un fallo de build es lo que transforma la accesibilidad de un esfuerzo heroico individual a una propiedad fiable del sistema, que es lo único que funciona cuando muchos equipos publican dentro de un mismo producto. Decidan qué comprobaciones son bloqueantes, cuáles son orientativas y quién puede anular un fallo. Aporten los resultados actuales del escáner y sus criterios de aceptación a la reunión. Si los criterios de accesibilidad no están escritos en la definición de completitud de cada historia, se depriorizarán en cuanto apriete el plazo.

2. **¿Cuál es nuestra norma para los widgets personalizados y quién revisa el ARIA antes de que se publique?** Los elementos HTML nativos ofrecen comportamiento de teclado y compatibilidad con tecnologías de apoyo sin coste, y un ARIA incorrecto es peor que ninguno porque desorienta activamente a los lectores de pantalla. Acuerden que el HTML semántico es la opción predeterminada y que cualquier widget personalizado (un desplegable a medida, un selector de fecha, un cuadro de diálogo) exige un recorrido por teclado y con lector de pantalla antes de fusionarse, siguiendo las Prácticas de Autoría ARIA. Esto es especialmente crítico en los componentes interactivos que muchos equipos reutilizan, porque un cuadro de diálogo roto con trampa de teclado puede dejar a usuarios con discapacidad fuera de todo un flujo. Aporten una lista de sus widgets personalizados y pregunten cuáles se han probado con un lector de pantalla real. Los que no lo han sido son pasivos ocultos en el código compartido.

3. **¿Cuál es nuestra política sobre las superposiciones de accesibilidad y cree alguien que sean una solución real?** Las superposiciones se venden como un script de una línea que hace que un sitio sea conforme, y resultan tentadoras cuando llega la presión legal y el plazo se aprieta. No entregan una conformidad genuina, pueden empeorar la experiencia para usuarios de tecnologías de apoyo y, en el sector público, dejan la obligación legal sin cumplir. Decidan explícitamente que invertirán en marcado semántico, soporte de teclado y pruebas con personas con discapacidad, en lugar de comprar un widget que tapa el problema. Aporten el coste de una suscripción a una superposición y compárenlo con el de integrar la accesibilidad en sus componentes y su pipeline de una vez. Plantearlo a tiempo evita una decisión de compra en pánico en el futuro que gasta dinero y no soluciona nada.

4. **¿Las personas con discapacidad forman parte de nuestro diseño y testing, o seguimos diseñando para un usuario imaginario que inventamos?** Los escáneres automatizados y hasta las auditorías expertas indican si el marcado es conforme; no dicen si un usuario con ceguera puede completar su pago o si una persona con discapacidad cognitiva puede comprender sus mensajes de error. Involucrar a participantes con discapacidad es la única fuente de verdad real, y transforma lo que se construye, pero plantea cuestiones concretas sobre cómo reclutar con equidad, cómo compensar su tiempo y cómo evitar tratar a un solo participante como portavoz de todas las discapacidades. Aporten su registro actual de investigación, sus prácticas de reclutamiento y pago, y un recuento honesto de cuántos estudios del último año incluyeron a participantes con discapacidad. En una organización grande, un panel recurrente con compensación justa y cobertura en necesidades de visión, audición, motricidad y cognición es lo que convierte esto de un gesto puntual en una entrada fiable; en el sector público, implicar al ciudadano al que se sirve suele ser parte de la obligación legal y cívica, no un capricho opcional.

5. **Cuando compramos o incrustamos un componente de terceros, ¿exigimos prueba de accesibilidad y quién la verifica?** Gran parte de lo que se publica en un producto de gran escala no se escribe en casa: un selector de fecha de una librería, un widget de pagos en un iframe, un paquete de gráficos, un módulo SaaS entero. Un solo componente incrustado inaccesible puede hacer fallar todo un flujo, por limpio que esté el propio código, y una vez integrado, reemplazarlo es costoso. Decidan que la accesibilidad es un requisito de adquisición, que los proveedores deben aportar un informe de conformidad de accesibilidad (un documento tipo VCAT o VPAT que indica cómo un producto se mide contra las WCAG) y que alguien con capacidad técnica valide la afirmación en lugar de archivarlo. Aporten un inventario de sus componentes de terceros y pregunten cuáles cuentan con evidencia de conformidad actual y creíble. En compras empresariales y públicas, escriban en el contrato la conformidad con WCAG 2.2 AA y el derecho a remediación, porque una promesa hecha antes de firmar es mucho más barata de exigir que una barrera descubierta después del lanzamiento.

6. **¿Cuál es nuestro nivel de conformidad objetivo, quién lo gestiona y cómo lo mantenemos actualizado a medida que avanzan los estándares?** WCAG 2.2 AA es el piso actual y la mayoría de las leyes lo citan, pero la versión 2.2 añadió criterios que muchos equipos no han adoptado y la WCAG 3.0 se aproxima con una estructura distinta. Sin un responsable nombrado, el estándar se degrada: equipos distintos apuntan a versiones diferentes, nadie rastrea la brecha y la conformidad se pudre en silencio entre auditorías. Decidan la versión y el nivel exacto a los que se construye, quién tiene autoridad para elevarlo y cómo los nuevos criterios llegan al sistema de diseño y a la definición de completitud. Aporten su objetivo declarado actual, evidencia de dónde los equipos lo cumplen de hecho y una hoja de ruta breve para adoptar los criterios 2.2 que se han omitido. En una organización grande o pública, un responsable de accesibilidad o centro de excelencia, una declaración de accesibilidad publicada y un plan documentado para la próxima versión del estándar son lo que permite responder a un regulador o a un tribunal con evidencia y no con buenas intenciones.

## Perspectiva por sector

**Startup.** Aquí la velocidad les favorece, porque la accesibilidad es más barata cuando la base de código es pequeña. Añadan un escáner de accesibilidad a su build y un recorrido por teclado a su checklist de pull request desde el primer sprint, y apoyen en HTML semántico para obtener soporte de teclado y lector de pantalla sin esfuerzo. Olviden las superposiciones y la herramienta pesada: la ventaja es que, cuando el equipo de adquisición de un cliente de tamaño mediano pide un informe de conformidad a mitad del ciclo de ventas, pueden responder en días en lugar de improvisar.

**Pequeña empresa.** Sin especialista en accesibilidad y con un presupuesto ajustado, compren accesibilidad en lugar de construirla: elijan una plataforma, tema o librería de componentes que ya cumpla y lo declare, y prefieran proveedores que publiquen una declaración de accesibilidad. Cúbran los básicos de alto valor ellos mismos con herramientas gratuitas, comprobaciones solo por teclado, un verificador de contraste y etiquetas claras en cada campo, porque esos son los que detectan las fallos que con más frecuencia excluyen a los clientes. Traten un flujo automatizado defectuoso o inutilizable como un cliente perdido, ya que una pequeña empresa rara vez ofrece un canal asistido como alternativa.

**Gran empresa.** A escala, el trabajo es hacer de la accesibilidad una propiedad del sistema entre muchos equipos. Publiquen componentes accesibles por defecto en el sistema de diseño, bloqueen las regresiones en CI, y creen un responsable o centro de excelencia con un proceso de remediación y formación para diseñadores, ingenieros y autores de contenido. Rastreen la conformidad en el tiempo como métrica, incorporen la conformidad con WCAG en las adquisiciones y gestionen los componentes de terceros como un portafolio, para que un widget incrustado no pueda hacer fallar en silencio un flujo compartido.

**Sector público.** La accesibilidad es un mandato legal y un deber cívico, ya que los ciudadanos con discapacidad a menudo no tienen un proveedor alternativo para una pensión, una licencia o un voto. Construyan según el estándar que cite su jurisdicción (por ejemplo, la Sección 508, la norma EN 301 549 o la Directiva de Accesibilidad de la Unión Europea, vinculadas a WCAG 2.2 AA), publiquen una declaración de accesibilidad con un canal para reportar barreras y prueben con el público con discapacidad al que se sirve. Rechacen las superposiciones como sustituto de una conformidad real y exijan a los proveedores que aporten evidencia creíble y el derecho a remediación en el contrato.

## Ejemplos

**Startup.** Un equipo de tres personas que construía una herramienta de contratación añadió un escáner de accesibilidad a su build y un recorrido rápido por teclado a su checklist de pull request desde el primer sprint, razonando que era más barato mantener la accesibilidad que corregirla después. Cuando el equipo de adquisición de un cliente de tamaño mediano pidió un informe de conformidad de accesibilidad a mitad de un ciclo de ventas, la empresa ya usaba HTML semántico, etiquetaba cada campo y tenía foco visible en todas partes, así que respondió en días, sin improvisar. Esa preparación ganó un contrato que un competidor perdió por el mismo requisito.

**Gran empresa.** Una gran cadena minorista enfrentó una demanda colectiva porque clientes con ceguera no podían completar la compra con un lector de pantalla. Más allá de la indemnización y los gastos legales, la compañía tuvo que remediarse bajo un cronograma supervisado por el tribunal. Después, reconstruyó la accesibilidad en su sistema de diseño y su pipeline de CI, añadió pruebas con lector de pantalla a la definición de completitud y formó a sus equipos. El nuevo flujo de compra accesible también mejoró la conversión y redujo los contactos con soporte para todos: las correcciones que ayudaron a los usuarios de lector de pantalla (etiquetas claras, mensajes de error comprensibles, orden lógico) beneficiaron a todos los usuarios.

**Sector público.** Un organismo de servicios sociales tenía la obligación legal de cumplir con WCAG 2.1 AA en su solicitud en línea. Las primeras pruebas con usuarios con ceguera y baja visión, usuarios solo por teclado y usuarios con discapacidad cognitiva revelaron que un indicador de «campo obligatorio» basado únicamente en color, un selector de fecha inaccesible y errores de validación sin anunciar impedían que las personas completaran su solicitud. Corregir estos problemas mediante marcado semántico, foco visible, anuncios de error en regiones activas y ayuda en [lenguaje claro](https://en.wikipedia.org/wiki/Plain_language) permitió a los ciudadanos con discapacidad tramitar su solicitud por primera vez de forma autónoma. Eso redujo la dependencia de la asistencia presencial y abarató el coste de servicio, al mismo tiempo que cumplía el mandato legal.

## Caso de negocio: motivaciones, ROI y coste total de propiedad

El caso de negocio se sostiene en el alcance de mercado, el riesgo legal, el coste de servicio y la calidad. Las personas con discapacidad y sus familias controlan un poder adquisitivo significativo; excluirlas renuncia a él. Los servicios accesibles reducen la necesidad de canales asistidos costosos (atención telefónica y presencial), lo que es un ahorro operativo directo, especialmente en el sector público. Y como las mejoras de accesibilidad (etiquetas claras, soporte de teclado, contenido legible, marcado robusto) benefician a todos, suelen elevar la finalización y la satisfacción globales.

En cuanto al coste total de propiedad, el coste de adopción son la formación, la herramienta y la integración de la accesibilidad en componentes y pipelines, todo modesto cuando se hace desde el inicio. El coste de no adoptar es grave y llega por varias vías: responsabilidad legal (demandas, indemnizaciones, remediación ordenada por tribunal, sanciones reguladoras), el gasto muy superior de la remediación bajo presión de plazo, el daño reputacional y el coste continuado de atender a usuarios excluidos a través de canales más caros. Remediar suele costar varias veces lo que habría supuesto diseñar desde el inicio.

Para presentar el caso a la dirección, empiecen por la obligación legal donde aplica (es innegociable para el sector público y cada vez más para el privado). Luego cuantifiquen la población alcanzable que están excluyendo, el coste del canal asistido que esa exclusión genera y las ganancias del «efecto acera» para todos. Posicionen la accesibilidad como gestión de riesgos y calidad, no como caridad.

## Antipatrónes y trampas

- **Accesibilidad como una casilla previa al lanzamiento**: una auditoría al final en lugar de una práctica continua, lo que garantiza una reingeniería costosa de última hora.
- **«Sopa de div»**: marcado no semántico con manejadores de clic en elementos genéricos, invisible para las tecnologías de apoyo.
- **Mal uso de ARIA**: adherir ARIA a un markup roto, lo que desorienta a los lectores de pantalla más que un marcado sencillo.
- **Información solo por color**: estado mostrado únicamente por color, invisible para usuarios con daltonismo.
- **Foco invisible**: eliminar los contornos de foco por estética, dejando a los usuarios de teclado a la deriva.
- **Trampas de teclado**: cuadros de diálogo y widgets que atrapan o pierden el foco.
- **Falsa confianza del escáner automático**: pasar un escáner y suponer que el producto es accesible.
- **Superposiciones de accesibilidad**: widgets de terceros de «una línea de fix» que no entregan conformidad real y pueden empeorar la experiencia.
- **Excluir a las personas con discapacidad de la investigación**: diseñar para un usuario con discapacidad imaginario en lugar de probar con personas reales.

## Modelo de madurez

**Nivel 1: Iniciar.** No hay práctica de accesibilidad. Los problemas solo se descubren cuando un usuario se queja o llega una demanda, y la respuesta es reactiva. El marcado no es semántico ni está probado, y nadie es responsable.

**Nivel 2: Desarrollar.** Existe conciencia y algunos equipos actúan: un escáner automatizado en un build, un recorrido por teclado en otro, una auditoría previa a un lanzamiento importante. La práctica es básica e inconsistente entre equipos; la accesibilidad sigue siendo una lista de verificación de última etapa y se deprioritiza con frecuencia bajo presión de plazo.

**Nivel 3: Estandarizar.** WCAG 2.2 AA es el estándar documentado y aplicado en toda la organización. La accesibilidad está integrada en el sistema de diseño para que los componentes se publiquen accesibles por defecto, se prueban de forma automática y manual, y se incorporan en la definición de completitud. Los equipos están formados, existe un responsable o centro de excelencia y se ha definido un proceso de remediación.

**Nivel 4: Gestionar.** La accesibilidad se mide y controla con datos frente a líneas base. La organización rastrea métricas de conformidad en el tiempo (tasa de aprobado del escáner, número de barreras abiertas por severidad, cobertura de pruebas con lector de pantalla de flujos críticos y tiempo hasta remediar), las publica por equipo en un panel de control y trata las regresiones como fallos de build, no como avisos orientativos. Se fijan objetivos frente a la línea base y se revisa el progreso, de modo que un equipo que se desvía es visible antes de que una auditoría lo descubra.

**Nivel 5: Orquestar.** La accesibilidad mejora de forma continua y se integra en toda la organización. Las personas con discapacidad participan en la investigación y las pruebas de forma recurrente, y la accesibilidad está embebida en la adquisición, los tokens de diseño y el CI. La organización se adapta a medida que avanzan los estándares (adoptando nuevos criterios de WCAG y preparándose para la 3.0) e influye en proveedores y socios para que toda la cadena de suministro sea conforme.

## Ideas para debatir

- ¿Cómo se evita que la accesibilidad se deprioritice cuando aprietan los plazos?
- ¿Cuál es la mezcla adecuada de pruebas automatizadas, manuales y de usuarios para su perfil de riesgo?
- ¿Cómo debe incorporarse la conformidad de accesibilidad en los contratos de proveedores y las adquisiciones?
- ¿Cómo se gestiona la brecha entre la conformidad con WCAG y la usabilidad genuina para personas con discapacidad?
- ¿Cómo deben prepararse los equipos para WCAG 3.0 mientras construyen bajo 2.2?
- ¿Cómo se recluta y compensa de forma justa y respetuosa a los participantes con discapacidad para la investigación?

## Ideas clave

- La accesibilidad es un atributo de calidad de nivel base y, para el sector público, un requisito legal.
- Diseñen con WCAG 2.2 AA como piso; usen los principios POUR como modelo mental.
- HTML semántico primero; ARIA solo para cubrir lagunas reales, y bien hecho.
- Las herramientas automatizadas detectan cerca de un tercio de los problemas; las pruebas manuales y con tecnologías de apoyo son imprescindibles.
- Prueben con personas con discapacidad, no solo para ellas.
- Integrar la accesibilidad es económico y perdurable; remediar es costoso y frágil.
- El diseño accesible es mejor diseño para todos: el efecto acera es real.

## Referencias y lecturas complementarias

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* y documentos complementarios Understanding y Techniques
- W3C, *Guía de Prácticas de Autoría WAI-ARIA*
- W3C Web Accessibility Initiative (WAI), materiales introductorios y tutoriales
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton y Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- Normas de la Sección 508 y guía de Section508.gov (EE. UU.)
- Norma europea EN 301 549 y Directiva de Accesibilidad de la Unión Europea
- Guías de accesibilidad de organismos públicos (por ejemplo, el manual de accesibilidad del GDS del Reino Unido)
- WebAIM, investigación y artículos, incluidas las anuales análisis de accesibilidad

