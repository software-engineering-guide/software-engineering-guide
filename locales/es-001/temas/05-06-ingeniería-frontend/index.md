# 5.6 Ingeniería de frontend

## Visión general y motivación

La ingeniería de frontend es la disciplina de construir la capa orientada al usuario final del software: el código que se ejecuta en el navegador o en el dispositivo y que convierte diseños, contenidos y datos en una interfaz funcional. Abarca decisiones sobre frameworks y arquitectura, estrategias de renderizado, gestión del estado, rendimiento y resiliencia ante la enorme diversidad de navegadores, dispositivos y condiciones de red del mundo real. El frontend es el punto donde todo el trabajo anterior (experiencia de usuario, diseño, contenido, accesibilidad, internacionalización) llega con éxito al usuario o se desmorona por completo.

Para equipos grandes, el frontend es un reto singular porque se expone a un entorno que la organización no controla. Los navegadores, dispositivos, conexiones y ajustes de los usuarios varían enormemente, y la plataforma (la web) evoluciona de forma continua. A gran escala, las decisiones arquitectónicas se acumulan. Un framework elegido hoy condiciona la contratación, el rendimiento y el mantenimiento durante años, y miles de decisiones pequeñas sobre el tamaño del bundle y el renderizado suman hasta configurar la experiencia que realmente obtiene el usuario. Los estándares compartidos, las bibliotecas de componentes, los presupuestos de rendimiento y los patrones arquitectónicos son lo que impide que muchos equipos independientes produzcan un conjunto lento, inconsistente y frágil.

La relevancia en entornos corporativos y gubernamentales es acuciante. Las grandes empresas mantienen aplicaciones de vida prolongada donde la longevidad del framework y el mantenibilidad pesan más que la novedad, y donde muchos equipos deben interoperar. Los gobiernos prestan servicio a toda la ciudadanía, incluyendo personas con dispositivos antiguos, conexiones lentas o limitadas y tecnologías de apoyo. Todo ello convierte el rendimiento, el [enriquecimiento progresivo](https://en.wikipedia.org/wiki/Progressive_enhancement) y la resiliencia en algo que no es un detalle opcional sino la diferencia entre un servicio que funciona para todos y uno que excluye a los más desfavorecidos. Un servicio gubernamental que solo funciona en el último móvil con una conexión rápida incumple su mandato.

## Principios fundamentales

- El frontend se ejecuta en un entorno que no se controla; hay que diseñar para la variabilidad y la falla.
- Elegir tecnología madura y duradera para sistemas de vida prolongada; optimizar para el mantenimiento y la contratación.
- El rendimiento es una característica y, para muchos usuarios, un requisito previo para el acceso.
- Enriquecimiento progresivo: ofrecer primero una experiencia central funcional y, después, capas de mejoras.
- Enviar menos código: el código más rápido y fiable es el que no se envía.
- Ajustar la estrategia de renderizado al tipo de contenido y la necesidad del usuario, no a las modas.
- Resiliencia: la interfaz debe degradarse con elegancia ante un fallo, no romperse.
- Los estándares y las capacidades de la plataforma superan en vida útil a los frameworks; apoyarse en la plataforma.

## Recomendaciones

### Elegir frameworks por su durabilidad y adecuación, no por la moda

Seleccionar la tecnología de frontend en función del problema, el equipo, el horizonte de mantenimiento y el mercado laboral, no por lo que esté de moda. Para sistemas corporativos y gubernamentales de vida prolongada, preferir tecnologías maduras, bien apoyadas, con grandes pools de talento, prácticas de publicación estables y caminos claros de actualización. Poner en la balanza el coste total de la rotación de frameworks: las reescrituras son caras y arriesgadas. Preferir enfoques que se apoyen en [estándares web](https://en.wikipedia.org/wiki/Web_standards) para que la inversión sobreviva al cambio de framework, e aislar el código específico de un framework tras límites claros para que la aplicación no quede rehén del ciclo de vida de una sola biblioteca.

### Ajustar la estrategia de renderizado a la necesidad

Las principales estrategias de renderizado encajan con tipos de contenido distintos. El renderizado del lado del servidor (SSR) produce un primer pintado rápido, favorece el [posicionamiento en buscadores](https://en.wikipedia.org/wiki/Search_engine_optimization) y funciona sin JavaScript en el cliente, resultando adecuado para páginas ricas en contenido y de cara pública. La [generación de sitios estáticos](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) pre-renderiza en tiempo de compilación para lograr una máxima velocidad y capacidad de caché, ideal para contenidos que cambian con poca frecuencia. El renderizado del lado del cliente (CSR) conviene para experiencias de aplicación muy interactivas tras un punto de autenticación. El streaming y la hidratación progresiva envían y activan la página de forma incremental, de modo que el usuario ve y usa el contenido antes. Muchos sistemas grandes combinan estas estrategias por ruta en lugar de imponer una sola globalmente. Gestionar el estado con deliberación: mantener separados el estado del servidor, el estado de la URL y el estado local de la interfaz, y evitar centralizar todo en un almacén global pesado.

### Tratar el rendimiento como una disciplina presupuestada y medida

Adoptar presupuestos de rendimiento (límites explícitos en el tamaño del bundle, el número de peticiones y las métricas clave) y ejecutarlos en el pipeline de integración continua para que cualquier regresión haga fallar la compilación. Seguirlas métricas Core Web Vitals (carga, interactividad y estabilidad visual) mediante la monitorización con usuarios reales desde dispositivos y redes reales, no solo con pruebas de laboratorio en máquinas veloces. Reducir el JavaScript de forma agresiva: dividir el código y usar [carga diferida](https://en.wikipedia.org/wiki/Lazy_loading) para que cada vista descargue únicamente lo que necesita, posponer el trabajo no crítico y preferir las capacidades de la plataforma antes que bibliotecas pesadas. Optimizar imágenes y fuentes, aprovechar la caché con eficacia y medir en dispositivos de gama baja y conexiones lentas representativos.

### Construir con enriquecimiento progresivo y resiliencia

Partir de una base que funcione con HTML semántico y con un mínimo o ninguna dependencia de JavaScript, y mejorar la experiencia para los clientes que lo permitan. Así se garantiza que la tarea central siga siendo posible cuando un script no se carga, el dispositivo es antiguo o la red es inestable: una realidad habitual, no un caso marginal. Manejar los errores con elegancia: mostrar estados útiles para carga, vacío, error y desconexión en lugar de pantallas en blanco o animaciones de espera interminables. Para servicios de los que la gente depende, considerar técnicas de primer plano offline para que la aplicación siga siendo usable con conectividad intermitente, sincronizando cuando la conexión se restablece.

### Garantizar compatibilidad multidevico, multinavegador y con tecnologías de apoyo

Probar en los navegadores, dispositivos y tecnologías de apoyo que los usuarios realmente tienen, guiándose por datos analíticos reales y no por las máquinas del equipo. Utilizar enriquecimiento progresivo y detección de características en lugar de suponer que las funciones más recientes de la plataforma están disponibles en todas partes. Construir de forma [responsiva](https://en.wikipedia.org/wiki/Responsive_web_design) (véase el capítulo de sistemas de diseño) para que un mismo código sirva desde el móvil hasta el escritorio. Integrar la accesibilidad y la internacionalización en la arquitectura del frontend desde el inicio, no como pases posteriores.

### Gobernar el frontend como infraestructura compartida

Ofrecer bibliotecas de componentes compartidas, herramientas de análisis estático, formateo y construcción para que los equipos sean consistentes y productivos. Establecer pautas arquitectónicas (cómo estructurar aplicaciones, gestionar el estado y dividir bundles) y presupuestos de rendimiento ejecutados en la integración continua. Para frontends muy extensos, considerar arquitecturas modulares o de micro-frontends que permitan a los equipos desplegar de forma independiente, pero sopesar la complejidad añadida y el coste de rendimiento con cuidado, pues no son gratuitos.

## Compromisos: ventajas e inconvenientes

| Decisión | Ventajas | Inconvenientes |
|---|---|---|
| Framework maduro y popular | Gran reserva de talento, estabilidad, soporte | Puede arrastrar lastres heredados; adopción más lenta de las funciones más recientes |
| Framework más nuevo | Funciones modernas, ganancias de rendimiento | Riesgo de rotación, reserva de talento reducida, longevidad incierta |
| SSR / SSG | Primer pintado rápido, buen posicionamiento, funciona sin JS | Complejidad en el servidor o la compilación, desafíos de caché |
| CSR (SPA) | Interactividad rica, sensación de aplicación | Carga inicial lenta, dependencia de JS, coste en posicionamiento y resiliencia |
| JavaScript extenso en el cliente | Funcionalidad avanzada | Mal rendimiento en dispositivos de gama baja, fragilidad |
| Enriquecimiento progresivo | Resiliente, inclusivo, funciona en cualquier entorno | Mayor esfuerzo de diseño para definir una base funcional |
| Micro-frontends | Despliegues independientes por equipo, escalabilidad | Complejidad, dependencias duplicadas, sobrecarga de rendimiento |

El compromiso recurrente es entre la riqueza y la comodidad del desarrollador, por un lado, y el alcance, el rendimiento y la resiliencia, por otro. Los enfoques pesados en el lado del cliente son agradables de construir y demostralos en máquinas rápidas, pero excluyen a los usuarios con dispositivos débiles y redes limitadas. Para audiencias corporativas y, sobre todo, gubernamentales, conviene inclinar la balanza hacia el rendimiento, el enriquecimiento progresivo y la durabilidad, porque el coste de excluir usuarios es alto y, a menudo, ineludible.

## Preguntas para debatir con el equipo

1. **¿Cómo aislamos el código específico del framework para que la aplicación no quede rehén del ciclo de vida de una sola biblioteca?** En sistemas corporativos y gubernamentales de vida prolongada, la rotación de frameworks es el mayor gasto evitable: una reescritura es costosa y arriesgada, y la biblioteca en boga de hoy condiciona la contratación y el mantenimiento durante años. Apoyarse en los estándares web y colocar el código específico del framework tras límites claros significa que la lógica de negocio y los contenidos sobreviven al próximo cambio de framework. Decidir dónde están esas juntas y si un ingeniero nuevo podría distinguir el código de plataforma del de framework. Presentar una estimación de lo que costó la última migración de framework, o de lo que costará la inminente. Si la lógica central está soldada a las APIs de una sola biblioteca, cuantificar ese acoplamiento antes de defender la elección del framework.

2. **¿Ajustamos la estrategia de renderizado por ruta o imponemos una única estrategia a todo el producto?** El renderizado del lado del servidor ofrece un primer pintado rápido y funciona sin JavaScript en el cliente para el contenido público; la generación estática maximiza la velocidad para páginas que cambian con poca frecuencia, y el renderizado del lado del cliente conviene para superficies interactivas tras un inicio de sesión. Imponer una sola estrategia global o bien frena las páginas públicas con JavaScript innecesario o sobredimensiona una página de contenido sencilla. Para el sector gubernamental, es una cuestión de alcance: un servicio que solo funciona tras cargar un bundle voluminoso excluye a los usuarios con dispositivos antiguos y conexiones lentas. Presentar las rutas clave y etiquetar cada una con la estrategia que usa realmente en la actualidad. Si una página de cara pública necesita JavaScript para mostrar su contenido, decidir si esa dependencia es una elección deliberada o un accidente.

3. **¿Qué tan disciplinada es la gestión del estado y estamos centralizando todo en un almacén global excesivamente pesado?** Mantener separados el estado del servidor, el de la URL y el local de la interfaz impide el acoplamiento y las tormentas de re-renderizado que hacen lentos y frágiles a los frontends extensos, y sin embargo el camino de menor resistencia es volcar todo en un almacén global. A gran escala, esto se multiplica: muchos equipos que tocan un almacén compartido generan dependencias ocultas y un rendimiento impredecible. Acordar dónde reside cada tipo de estado y qué no debe estar en el almacén global. Presentar un componente que se re-renderiza más de lo necesario y trazar por qué. Si la respuesta es un almacén central inflado, fijar los límites antes de que el acoplamiento se consolide.

4. **¿Cuáles son nuestros presupuestos de rendimiento, se ejecutan en la integración continua como criterio de aceptación y se miden en los dispositivos que nuestros usuarios realmente tienen?** Un presupuesto que nadie ejecuta es un deseo, y uno medido solo en los portátiles veloces del equipo describe a un usuario que no existe. Para una gran organización, los presupuestos son el único mecanismo que mantiene el tamaño del bundle y los Core Web Vitals bajo control cuando decenas de equipos añaden funcionalidades a una superficie compartida, porque ningún revisor puede detectar cada regresión a simple vista. La presión contraria es la velocidad de entrega: un fallo de compilación por unos pocos kilobytes resulta obstructivo hasta que se cuantifica la abandonabilidad que impide. Presentar los presupuestos actuales, los datos de monitorización con usuarios reales desde dispositivos de gama baja y conexiones lentas, y la lista de liberaciones en las que una regresión pasó desapercibida. En el sector gubernamental, donde el mandato es servir a toda la ciudadanía, incluidas las personas con teléfonos antiguos y datos por cuota, vincular el presupuesto al decil más lento de los usuarios, no a la mediana, y hacer que la barrera en la integración continua sea innegociable.

5. **¿Qué servicios deben seguir funcionando sin JavaScript en el cliente y hemos probado realmente esa vía?** El enriquecimiento progresivo es fácil de proclamar y fácil de romper en silencio, porque el camino mejorado es el que los desarrolladores usan a diario mientras la base funcional se degrada sin control. Decidir esto de forma deliberada importa a gran escala, pues muchos equipos que publican en una misma plataforma asumirán que los scripts siempre se cargan a menos que un estándar compartido diga lo contrario, y una sola dependencia rígida puede inutilizar la tarea central para quien sufra un fallo en la carga del bundle. El compromiso es real: una base funcional sin JavaScript exige esfuerzo de diseño y limita cómo se construye la interactividad. Presentar los recorridos de usuario críticos, una prueba que cargue cada uno con los scripts desactivados o fallando, y datos sobre la frecuencia real de fallos de carga en producción. Para un servicio público, un formulario de prestaciones o fiscal que se colapsa ante un tiempo de espera de un script no es una experiencia degradada, es un ciudadano incapaz de cumplir una obligación legal; tratar la base como un requisito de cumplimiento, no como una concesión.

6. **¿Cuándo se justifican los micro-frontends frente a su complejidad y quién decide antes de que un equipo se lanzue a adoptarlos?** Los despliegues independientes por equipo son atractivos, pero los micro-frontends arrastran complejidad de sistemas distribuidos, dependencias duplicadas y un impuesto de rendimiento que el usuario paga en cargas más lentas. Sin un punto de decisión compartido, los equipos ambiciosos los adoptan por conveniencia organizativa mucho antes de que la escala lo justifique, y todo el producto hereda la sobrecarga. La consideración contraria es la autonomía: los equipos que publican en un mismo código base pueden bloquearse mutuamente, y a una escala genuina ese acoplamiento es, en sí mismo, un problema costoso. Presentar el número de equipos que tocan la superficie, la contención de despliegue que se experimenta realmente hoy y una estimación medida de la duplicación de carga que una división introduciría. En plataformas corporativas y gubernamentales, donde las decisiones arquitectónicas comprometen a muchos equipos durante años y deben sobrevivir a la auditoría y la sucesión, exigir un umbral explícito y documentado y un responsable que autorice el paso, en lugar de dejar que cada equipo decida por su cuenta.

## Perspectiva sectorial

**Startup.** Tanto la velocidad como el alcance importan cuando cada registro cuenta, por lo que hay que resistir la tentación de la aplicación de página única pesada para páginas públicas. Renderizar el sitio de marketing y el flujo de registro del lado del servidor para que carguen rápido en los móviles de gama media y la data inestable que usan los primeros clientes, y reservar la interactividad del lado del cliente para la aplicación tras el inicio de sesión. Fijar un presupuesto de tamaño de bundle sencillo en la integración continua para que una dependencia descuidada no hinche la página en silencio, y apoyarse en los estándares web para mantener un código base reducido y mantenible a medida que se contrata.

**Pequeña empresa.** Sin un especialista en frontend dedicado y con un presupuesto ajustado, preferir un framework mainstream bien soportado o un constructor de sitios alojado por encima de cualquier solución a medida, de modo que se contrate de un amplio mercado laboral y se compre mantenimiento en lugar de dotarlo. Enmarcar la elección como durabilidad: la opción más barata es la que no obliga a reescribir en dos años. Exigir páginas rápidas, aptas para móvil y con marcado accesible de serie, porque un checkout lento o roto cuesta clientes que no se puede permitir perder.

**Empresa grande.** El problema es la consistencia entre muchos equipos: una biblioteca de componentes compartida, patrones arquitectónicos acordados, herramientas de análisis estático y construcción, y presupuestos de rendimiento ejecutados en la integración continua para que ningún equipo regrese en silencio el rendimiento global. Elegir frameworks por su longevidad y disponibilidad de talento en lugar de por novedad, aislar el código específico del framework tras límites para sobrevivir a la próxima migración y ajustar la estrategia de renderizado a cada superficie. Gestionar el frontend como infraestructura compartida, con monitorización con usuarios reales, gobernanza y un registro auditable de por qué se tomó cada decisión arquitectónica.

**Gobierno.** Se sirve a toda la ciudadanía, incluidas personas con dispositivos antiguos, conexiones lentas o por cuota y tecnologías de apoyo, por lo que el enriquecimiento progresivo y el rendimiento son obligaciones, no acabados. Convertir una base funcional sin JavaScript en una norma rígida para los servicios de cara al ciudadano, presupuestar las páginas a los usuarios más lentos y no a la mediana, y mantener la tarea central completible ante la falla de un script. Aplicar criterios de contratación y transparencia: preferir tecnología duradera y orientada a estándares que evite la dependencia de un único proveedor, documentar los requisitos de accesibilidad y rendimiento en los contratos y poder demostrar que el servicio funciona para el usuario más desfavorecido, no solo en el dispositivo de demostración.

## Ejemplos

**Startup.** Una startup en fase semilla se tentó a construir su sitio de marketing y su flujo de registro como una aplicación de página única pesada, pero sus clientes objetivo eran compradores que a menudo usaban móviles de gama media sobre data móvil inestable. Los dos fundadores optaron por renderizar las páginas públicas del lado del servidor para que cargaran rápido y funcionaran antes de que se ejecutara cualquier JavaScript, y reservaron la interactividad del lado del cliente para la aplicación tras el inicio de sesión. Establecieron un presupuesto de tamaño de bundle sencillo en la integración continua para que una dependencia descuidada no hinchara la página en silencio. La carga inicial ligera y veloz mejoró mediblemente los registros, y el apoyo en los estándares web mantuvo su reducido código base fácil de mantener a medida que crecía el equipo.

**Empresa grande.** Una firma de servicios financieros modernizó un conjunto extenso de aplicaciones internas y de clientes estandarizando un framework maduro, una biblioteca de componentes compartida y presupuestos de rendimiento ejecutados en la integración continua. La estrategia de renderizado se eligió por superficie: páginas cacheables renderizadas del lado del servidor para marketing y contenido públicos, y una aplicación renderizada del lado del cliente tras el inicio de sesión para paneles de control interactivos. Los presupuestos de bundle y la monitorización con usuarios reales detectaron regresiones antes del despliegue, manteniendo los tiempos de carga veloces a lo largo de los muchos equipos de la firma y reduciendo el riesgo de rotación de framework que antes había obligado a reescrituras costosas.

**Gobierno.** Un equipo de servicio digital nacional construyó servicios de cara al ciudadano con el enriquecimiento progresivo como norma rígida: cada servicio funciona primero con HTML semántico y renderizado del lado del servidor, y el JavaScript solo lo enriquece. Esto garantiza que el servicio funcione en móviles antiguos, conexiones rurales lentas y tecnologías de apoyo, poblaciones que un gobierno no puede excluir. Los presupuestos de rendimiento mantienen las páginas ligeras y veloces en dispositivos de gama baja, y la degradación progresiva asegura que la falla de un script nunca impida a nadie completar una solicitud de prestaciones. El resultado es un servicio veloz, resiliente, accesible y usable por toda la ciudadanía.

## Argumento de negocio: motivaciones, retorno y coste total de propiedad

Las decisiones de ingeniería de frontend determinan ingresos, alcance y coste. El rendimiento está directamente ligado a la conversión, la participación y la finalización de tareas. Las experiencias más rápidas superan mediblemente a las más lentas, y para los usuarios con dispositivos débiles, el rendimiento es la línea entre usar el servicio y abandonarlo. El enriquecimiento progresivo y el soporte multiplataforma amplían la audiencia alcanzable, lo cual para el gobierno es un mandato y para la empresa, cuota de mercado. Elecciones fundamentadas de framework y arquitectura reducen la frecuencia y el coste de las reescrituras, el mayor gasto evitable en la ingeniería de frontend.

En cuanto al coste total de propiedad, los costes de adopción son la disciplina de los presupuestos de rendimiento y las pruebas, el esfuerzo del enriquecimiento progresivo y la inversión en herramientas y bibliotecas de componentes compartidas. El coste de no adoptar se paga en experiencias lentas que generan pérdida de usuarios e ingresos, en la exclusión de usuarios con dispositivos de gama baja y tecnologías de apoyo (con responsabilidad legal en el ámbito gubernamental), en aplicaciones frágiles que fallan en producción y en la rotación de framework y reescrituras provocadas por perseguir modas. Los problemas de frontend se manifiestan como una abandonabilidad difusa y una carga de soporte repartida, no como un rubro contable único, por lo que es fácil infradotarlos.

Para presentar el caso a la dirección, vincular los Core Web Vitals y los tiempos de carga a los embudos de conversión y finalización, cuantificar los usuarios excluidos por los enfoques pesados del lado del cliente y poner en precio el coste de reescrituras pasadas o inminentes frente a la estabilidad de una arquitectura duradera y orientada a estándares. Enmarcar los presupuestos de rendimiento y el enriquecimiento progresivo como reducción de riesgo y ampliación de alcance.

## Antipatrones y trampas

- **Carrera de frameworks**: reescribir con cada nueva biblioteca, incurriendo en rotación sin beneficio para el usuario.
- **Experiencias exclusivas de JavaScript**: nada funciona hasta que se carga y ejecuta un bundle voluminoso, lo que excluye a muchos usuarios.
- **Pruebas solo en dispositivos rápidos**: los portátiles de última generación del equipo ocultan la experiencia real del usuario.
- **Ignorar el tamaño del bundle**: crecimiento incontrolado de dependencias hasta que todas las páginas son lentas.
- **Sin presupuesto de rendimiento**: las regresiones se acumulan en silencio liberación tras liberación.
- **Fallos de pantalla en blanco**: no hay estados de carga, vacío, error ni desconexión; una petición fallida rompe la página.
- **Estado global sobrecentralizado**: todo en un almacén, generando acoplamiento y tormentas de re-renderizado.
- **Micro-frontends prematuros**: complejidad de sistemas distribuidos y carga duplicada sin la escala que los justifique.
- **Descuidar la accesibilidad y la internacionalización en la arquitectura**: añadirlas después con un coste elevado.

## Modelo de madurez

**Nivel 1: Iniciar.** Frontend ad hoc, construido por equipo sin estándares compartidos. Código denso del lado del cliente, sin presupuestos de rendimiento, probado solo en los dispositivos del equipo. Las decisiones de framework se toman por preferencia o moda, y la falla de un script puede dejar al usuario ante una pantalla en blanco.

**Nivel 2: Desarrollar.** Algunos equipos adoptan herramientas y una biblioteca de componentes compartidas, pero la práctica es inconsistente en la organización. El rendimiento se mide de vez en cuando, no se presupuesta ni se ejecuta. La estrategia de renderizado suele ser uniforme sin importar el tipo de contenido, y las pruebas en distintos dispositivos son limitadas y manuales.

**Nivel 3: Estandarizar.** Framework y arquitectura se eligen deliberadamente por su longevidad, y las decisiones están documentadas y ejecutadas en toda la organización. La estrategia de renderizado se ajusta por superficie, el enriquecimiento progresivo y la degradación elegante son la norma, y las bibliotecas de componentes compartidas, el análisis estático y las herramientas de construcción aplican a cada equipo. La accesibilidad multidevico y la internacionalización se construyen desde el diseño, no se añaden después.

**Nivel 4: Gestionar.** El frontend se mide y controla con datos. Los presupuestos de rendimiento se ejecutan en la integración continua de modo que cualquier regresión hace fallar la compilación, y los Core Web Vitals se siguen mediante monitorización con usuarios reales desde dispositivos de gama baja y conexiones lentas, con baselines explícitas. El tamaño del bundle, la cobertura de estados de error y desconexión y la proporción de usuarios servidos en las conexiones más lentas se reportan y se revisan, de modo que las decisiones se sustenten en evidencia y no en opinión.

**Nivel 5: Orquestar.** El rendimiento, la resiliencia y el alcance se mejoran de forma continua y se vinculan a resultados de negocio en toda la organización. El frontend se apoya en los estándares web para la durabilidad, aísla las dependencias del framework para que las migraciones sean baratas y evoluciona la arquitectura de forma adaptativa a medida que cambian los dispositivos, la plataforma y los datos de usuarios reales. Toda la ciudadanía y todos los dispositivos son ciudadanos de primera clase, y la práctica del frontend se integra con el diseño, la accesibilidad y la planificación de producto en lugar de tratarse como una preocupación aparte.

## Ideas para el debate

- ¿Cómo se decide cuándo una migración de framework justifica su coste y su riesgo?
- ¿Qué Core Web Vitals y presupuestos de bundle deberían ser umbrales que hagan fallar la compilación?
- Dónde es esencial el enriquecimiento progresivo y dónde una aplicación del lado del cliente es aceptable?
- ¿Cómo se mantiene la consistencia de la arquitectura de frontend entre muchos equipos autónomos?
- ¿Cuándo se justifican los micro-frontends frente a su complejidad?
- ¿Cómo incorporar la prueba en dispositivos reales y redes lentas al pipeline?

## Conclusiones clave

- El frontend se ejecuta en un entorno que no se controla: diseñar para la variabilidad y la falla.
- Elegir tecnología madura y bien soportada para sistemas de vida prolongada; apoyarse en los estándares web.
- Ajustar la estrategia de renderizado (SSR, SSG, CSR, streaming) al contenido y a la necesidad, a menudo combinada por ruta.
- Tratar el rendimiento como una disciplina presupuestada y medida, ejecutada en la integración continua con datos de usuarios reales.
- Construir con enriquecimiento progresivo para que la experiencia central funcione en cualquier entorno.
- Enviar menos JavaScript: dividir el código, cargar de forma diferida y preferir las capacidades de la plataforma.
- En el ámbito gubernamental, sobre todo, el rendimiento y la resiliencia son requisitos previos para un acceso equitativo.

## Referencias y lecturas complementarias

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (enriquecimiento progresivo)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, escritos sobre rendimiento, división de código y el coste del JavaScript
- Google, *Web Vitals* y la guía de rendimiento de web.dev
- MDN Web Docs, referencias de la plataforma web y el enriquecimiento progresivo
- Alex Russell, ensayos sobre el coste del JavaScript y la diversidad de dispositivos
- UK Government Digital Service, guía de frontend y enriquecimiento progresivo
- WHATWG HTML Living Standard y especificaciones de la plataforma web de la W3C

