# 5.7 Desarrollo de aplicaciones móviles

## Panorama y motivación

El [desarrollo de aplicaciones móviles](https://en.wikipedia.org/wiki/Mobile_app_development) es la disciplina de crear software para teléfonos y tabletas. Para muchas personas, un teléfono es ya el ordenador principal o el único que poseen. Eso convierte a la aplicación móvil en la puerta de entrada a su servicio y, con frecuencia, en la superficie donde los usuarios juzgan a toda la organización.

El entorno móvil es un espacio de ingeniería distinto, no una versión reducida de la web o del escritorio. El dispositivo funciona en un bolsillo, alimentado por batería y sobre conexiones que aparecen y desaparecen. Las pantallas son pequeñas. El sistema operativo decide qué puede hacer la aplicación. Existen dos plataformas dominantes ([iOS](https://en.wikipedia.org/wiki/IOS), de Apple, y [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29), de Google), cada una con sus propios lenguajes, sus propias normas de diseño y su propia tienda. No se puede publicar una actualización a voluntad, porque la tienda la revisa antes y los usuarios deciden cuándo la instalan. Este capítulo se apoya en la ingeniería frontend (capítulo 5.6), los fundamentos de experiencia de usuario (capítulo 5.1) y la accesibilidad (capítulo 5.3), y recurre a la seguridad de aplicaciones (capítulo 4.2) y a la integración y entrega continuas (capítulo 8.1).

La relevancia para el sector empresarial y el ámbito gubernamental es elevada. Las empresas publican aplicaciones para sus clientes y aplicaciones internas para su propia plantilla, a menudo gestionadas mediante [gestión de dispositivos móviles](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM, por sus siglas en inglés: software centralizado que configura y protege los dispositivos de la empresa). Los gobiernos crean aplicaciones para ciudadanos en materia de prestaciones, salud, identidad y pagos, y deben atender a todos, incluidas las personas con dispositivos antiguos y conexiones lentas, cumpliendo las leyes de accesibilidad. En ambos contextos, la plataforma móvil es un compromiso serio y de larga duración, así que hay que abordarla con el mismo rigor que cualquier otro sistema en producción.

## Principios fundamentales

- Diseñar para el dispositivo: pantalla pequeña, batería limitada y una red que va y viene.
- Asumir la conectividad intermitente; trabajar sin conexión primero y sincronizar cuando sea posible.
- Respetar las convenciones de diseño e interacción de cada plataforma.
- No se controla el momento del lanzamiento: la tienda y el usuario lo deciden.
- La fragmentación es la norma; hay que soportar un abanico real de dispositivos y versiones del sistema operativo.
- Almacenar los datos en el dispositivo de forma segura, porque los teléfonos se pierden y se roban.
- La accesibilidad es un requisito, no un adorno final.
- Elegir la estrategia de construcción para la vida completa de la aplicación, no solo para el día del lanzamiento.

## Recomendaciones

### Elegir la estrategia de construcción con criterio

Existen tres enfoques amplios, y cada uno responde a necesidades diferentes.

El [desarrollo nativo](https://en.wikipedia.org/wiki/Mobile_app_development) consiste en programar por separado para cada plataforma con sus propias herramientas: Swift para iOS, Kotlin para Android. Se obtiene el mejor rendimiento, el acceso más completo a las funciones del dispositivo y la sensación más fiel a la plataforma, a cambio de construir y mantener dos bases de código.

Los [marcos de trabajo multiplataforma](https://en.wikipedia.org/wiki/Cross-platform_software) permiten que una sola base de código apunte a ambas plataformas. [React Native](https://en.wikipedia.org/wiki/React_Native) usa JavaScript y renderiza componentes nativos reales. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) emplea el lenguaje Dart y dibuja sus propios widgets. Estos enfoques reducen la duplicación de esfuerzo y pueden acelerar la entrega, pero añaden una dependencia de la salud del marco de trabajo y pueden rezagarse respecto a las últimas funciones de la plataforma.

Una [aplicación web progresiva](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA, por sus siglas en inglés: un sitio web que puede instalarse y funcionar sin conexión) no necesita tienda y se actualiza al instante, pero tiene acceso limitado a algunas funciones del dispositivo y una presencia más débil en la pantalla de inicio.

La elección debe basarse en las funciones del dispositivo que se requieren, el perfil de rendimiento, el horizonte de mantenimiento, las competencias que se pueden contratar y el alcance necesario. Una aplicación de consumo con exigencias de rendimiento alto puede justificar el enfoque nativo. Una aplicación de contenido y formularios con un equipo reducido puede encajar bien con un enfoque multiplataforma o una PWA.

### Seguir las pautas de diseño de cada plataforma

Cada plataforma dispone de convenciones publicadas y detalladas. Apple ofrece las [Pautas de interfaz humana](https://en.wikipedia.org/wiki/Human_interface_guidelines) y Google ofrece [Material Design](https://en.wikipedia.org/wiki/Material_Design). Estas pautas abarcan la navegación, los gestos, la tipografía, los espaciados y los comportamientos del sistema. Seguirlas hace que la aplicación se sienta familiar, lo que reduce el esfuerzo que el usuario dedica a aprenderla. Enfrentarse a ellas hace que la aplicación se perciba extraña y torpe. Una base de código compartida entre plataformas debe respetar las convenciones propias de cada una donde difieren, en lugar de imponer el aspecto de una plataforma a la otra.

### Diseñar para las restricciones del móvil

Diseñar con un enfoque *offline-first*: permitir que las tareas esenciales funcionen sin conexión, guardar los cambios localmente y sincronizar cuando la red regrese. Manejar los conflictos con cuidado cuando los mismos datos cambian en dos sitios a la vez. Ser frugal con la batería y los datos: agrupar las llamadas de red, evitar el rastreo constante de ubicación o el trabajo en segundo plano, comprimir los paquetes de datos y respetar los ajustes de ahorro de datos del usuario. Prever la fragmentación, la gran dispersión de tamaños de pantalla, potencia de dispositivo y versiones del sistema operativo. Elegir un rango de compatibilidad basado en datos de uso reales y probar en hardware modesto, no solo en equipos de gama alta. Diseñar para pantallas pequeñas con jerarquía clara, áreas táctiles amplias y contenido que se adapte a distintos tamaños y orientaciones.

### Planificar la distribución, la versión y las actualizaciones

La publicación pasa por la [App Store de Apple](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) y [Google Play](https://en.wikipedia.org/wiki/Google_Play), cada una con procesos y políticas de revisión que pueden retrasar o rechazar un lanzamiento. Incluir el tiempo de revisión en el calendario y leer las políticas con anticipación. Como los usuarios deciden cuándo actualizarse, siempre habrá muchas versiones en circulación. Mantener la aplicación compatible hacia atrás con los clientes antiguos y versionar las APIs (capítulo 2.3) para que una app vieja siga funcionando. Prever un mecanismo para exigir una actualización cuando sea necesario, por ejemplo, un aviso de actualización forzada cuando una versión sea insegura o incompatible, y usarlo con moderación. Las empresas también pueden distribuir aplicaciones internas a través del MDM o canales privados en lugar de las tiendas públicas.

### Usar las notificaciones push y los enlaces profundos con prudencia

Las [notificaciones push](https://en.wikipedia.org/wiki/Push_technology) permiten llegar al usuario cuando la aplicación está cerrada. Utilizarlas para un valor genuino, respetar el consentimiento del usuario y los permisos de la plataforma, y evitar el exceso, porque la gente desactiva las notificaciones de las aplicaciones que van demasiado lejos. Los [enlaces profundos](https://en.wikipedia.org/wiki/Deep_linking) llevan al usuario directamente a una pantalla concreta desde un enlace o una notificación. Configurarlos para que el enlace abra el lugar correcto en la aplicación y, cuando esta no esté instalada, redirija de forma elegante a la web.

### Proteger la aplicación y sus datos

Tratar el dispositivo como un recurso no confiable y posiblemente extraviado. Guardar los datos sensibles en el almacenamiento seguro de la plataforma (el [Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29) de iOS o el Android Keystore), nunca en archivos en texto plano. Ofrecer [autenticación biométrica](https://en.wikipedia.org/wiki/Biometrics) (huella dactilar o reconocimiento facial) para desbloquear acciones sensibles, respaldada por un código de acceso. Considerar la [fijación de certificados](https://en.wikipedia.org/wiki/Public_key_pinning) (verificar que el servidor presente el certificado esperado) para conexiones de alto valor, y prever la rotación de esos certificados. Minimizar lo que se almacena en el dispositivo, proteger los secretos y seguir la orientación más amplia del capítulo sobre seguridad de aplicaciones (capítulo 4.2).

### Construir una cadena de pruebas y entrega real

Probar en dispositivos reales, no solo en [emuladores](https://en.wikipedia.org/wiki/Emulator) y simuladores, porque el hardware, los sensores y el rendimiento difieren. Usar un laboratorio de dispositivos o una granja en la nube para cubrir un abanico representativo de modelos y versiones del sistema operativo. Automatizar la compilación, las pruebas, la firma y el envío a la tienda a través de la [integración y entrega continuas](https://en.wikipedia.org/wiki/CI/CD) (capítulo 8.1), incluida la distribución beta a los probadores antes del lanzamiento público. Gestionar las claves de firma y las credenciales de la tienda de forma segura es parte de esta cadena.

### Hacer de la accesibilidad un requisito

Apoyar las funciones de accesibilidad de cada plataforma: lectores de pantalla ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) en iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) en Android), ajuste dinámico del tamaño del texto, contraste de color suficiente y áreas táctiles amplias. Etiquetar los controles para que la tecnología de apoyo pueda describirlos. Probar con las herramientas de apoyo reales, no solo con comprobaciones automáticas. En el ámbito gubernamental, la accesibilidad es una obligación legal, y los detalles están en el capítulo de accesibilidad (capítulo 5.3).

## Compromisos: ventajas e inconvenientes

| Enfoque | Ventajas | Inconvenientes |
|---|---|---|
| Nativo (Swift, Kotlin) | Mejor rendimiento, acceso completo al dispositivo, sensación auténtica de plataforma | Dos bases de código, mayor coste, más personal |
| React Native | Una base de código en JavaScript, componentes nativos reales, iteración rápida | Dependencia del marco de trabajo, complejidad del puente, rezago funcional |
| Flutter | Una sola base de código, interfaz coherente, buen rendimiento | Competencias en Dart menos habituales, mayor tamaño de la app, modelo de widgets propio |
| Aplicación web progresiva | Sin tienda, actualizaciones instantáneas, una base de código web | Funciones de dispositivo limitadas, presencia más débil, restricciones de plataforma |
| Actualización forzada | Elimina versiones antiguas inseguras con rapidez | Molesta si se abusa; puede bloquear el acceso |
| Fijación de certificados | Protección sólida contra la interceptación | Se rompe si los certificados rotan sin actualizar la app |

El compromiso que se repite es el alcance y la velocidad de entrega frente a la profundidad y la fidelidad. El enfoque nativo ofrece la experiencia más rica y fiel, pero a mayor coste de construcción y mantenimiento. Los enfoques multiplataforma y las PWAs ahorran esfuerzo y amplían el alcance, a cambio de algo de fidelidad a la plataforma o acceso al dispositivo. Para un equipo pequeño que publica formularios y contenido, compartir la base de código suele ser lo más sensato. Para una app de consumo exigente, la profundidad nativa puede merecer la pena. Decidir con la vida completa de la app en perspectiva, no solo con la vista puesta en el lanzamiento.

## Preguntas para debatir con el equipo

1. **¿Durante cuánto tiempo se soportarán los clientes antiguos en circulación y están versionadas las APIs para que sigan funcionando?** Como los usuarios eligen cuándo actualizarse, siempre habrá muchas versiones de la app instaladas a la vez, y un cambio en el backend que suponga que todos están al día romperá la cola larga de clientes antiguos. Definir la ventana de compatibilidad hacia atrás, versionar las APIs para que la app antigua continúe funcionando y mantener un camino de actualización forzada, poco usado, para versiones que sean genuinamente inseguras. Esto importa tanto para aplicaciones de ciudadanía del sector público como para aplicaciones de plantilla en empresas, donde personas con dispositivos antiguos no pueden ni querrán actualizar en el plazo que se les imponga. Traer los datos actuales de distribución de versiones y preguntar qué se rompe en el cliente más antiguo que aún se usa en la práctica. Si no se conoce esa distribución, instrumentarla antes de publicar el próximo cambio incompatible.

2. **¿Cuál es el umbral para enviar una notificación push y quién decide qué merece interrumpir al usuario?** Las notificaciones push alcanzan a las personas cuando la app está cerrada, lo que las hace poderosas y fáciles de abusar, y los usuarios desactivan las notificaciones (o borran la app) de los productos que van demasiado lejos. Acordar qué cuenta como valor genuino, cómo los usuarios controlan la frecuencia y el canal y cómo se honra el consentimiento de la plataforma en lugar de insistir en pedir permiso. Sin un umbral compartido, cada equipo con una métrica que cumplir buscará el push y el canal entero se degradará en ruido. Traer las notificaciones enviadas el mes pasado y preguntar cuáles le habrían agradado al usuario. Si la mayoría eran promocionales, endurecer la política antes de que la tasa de baja la haga a la fuerza.

3. **¿La cadena de entrega móvil es real, cubriendo la firma, una granja de dispositivos y la distribución beta, o cada lanzamiento es un forcejeo manual estresante?** El móvil añade peligros que la web no tiene: la revisión de la tienda puede retrasar o rechazar un lanzamiento, las claves de firma y las credenciales de la tienda deben manejarse con cuidado, y el hardware y los sensores difieren lo suficiente como para que los emuladores oculten problemas reales. Automatizar la compilación, las pruebas, la firma y el envío a la tienda a través de la integración y entrega continuas, con distribución beta a los probadores y una granja de dispositivos en la nube que cubra los modelos que los usuarios llevan de verdad, es lo que convierte los lanzamientos de hazañas en rutina. Decidir quién es responsable de la cadena y de las claves de firma, y cómo el tiempo de revisión de la tienda se integra en cada plan de lanzamiento. Contar los pasos manuales del último lanzamiento. Cada uno es un punto donde un lanzamiento puede salir mal bajo presión.

4. **¿Se ha elegido el enfoque nativo, multiplataforma o PWA para la vida completa de este producto, o solo para el día del lanzamiento?** La estrategia de construcción es la palanca más grande sobre el coste y las capacidades de una app durante años, y una decisión tomada para ir rápido puede dejar atrapado: el enfoque nativo compra el acceso más rico al dispositivo y la sensación de plataforma al precio de dos bases de código y dos perfiles de competencia, mientras que el multiplataforma y la PWA comparten código pero añaden una dependencia del marco de trabajo o pierden acceso a algunas funciones. Para un equipo grande, esta decisión define las contrataciones, el presupuesto de mantenimiento y la rapidez con la que se puede adoptar cada actualización anual del sistema operativo, por lo que merece un responsable explícito en lugar de una opción por defecto elegida por quien escribió el primer prototipo. Traer las funciones de dispositivo necesarias, el perfil de rendimiento, el horizonte de mantenimiento y las competencias que de verdad se pueden contratar, y ser honesto sobre qué funciones de plataforma se renunciaría bajo cada opción. En entornos empresariales y del sector público, valorar si la app es un compromiso de larga duración que debe sobrevivir a la rotación de personal y a una década de cambios de plataforma, y registrar la decisión y su justificación para que un equipo futuro no tenga que adivinar por qué la base de código es como es.

5. **¿Qué rango de dispositivos y versiones del sistema operativo necesitan los usuarios reales y se está probando en el hardware que de verdad llevan, y no en los teléfonos que hay en los escritorios?** La fragmentación es la condición normal del móvil: los usuarios abarcan una gran dispersión de tamaños de pantalla, potencia de dispositivo y versiones del sistema operativo, y una app ajustada en los equipos de gama alta del equipo saldrá pesada o rota en el hardware modesto que posee gran parte del público. Definir un rango de compatibilidad es un compromiso entre alcance y esfuerzo, porque cada modelo antiguo y cada versión del sistema operativo que se promete soportar ensancha la matriz de pruebas y la carga de mantenimiento, así que el rango debe provenir de datos de uso reales y no de suposiciones. Traer la distribución de dispositivos y versiones del sistema operativo, los modelos que una granja de dispositivos en la nube o un laboratorio cubre actualmente, y el rendimiento medido en hardware de gama baja, no solo en simuladores. Para aplicaciones de ciudadanía del sector público esto es casi innegociable, porque hay que atender a todos, incluidas las personas con dispositivos antiguos y conexiones lentas, bajo obligaciones de accesibilidad; y para flotas empresariales conviene probar en los terminales robustos que el personal lleva realmente, no en una muestra genérica.

6. **¿Qué datos sensibles se guardan en el dispositivo y cada pieza está protegida frente a un teléfono perdido, robado o en manos ajenas?** Un dispositivo móvil viaja en un bolsillo y se pierde o se roba, así que cualquier dato o secreto guardado en un archivo en texto plano está a un teléfono extraviado de distancia de una exposición, y el radio de impacto crece con cada usuario. Los intereses se tensionan: cachear datos en el dispositivo es lo que hace posible el enfoque *offline-first* y mantiene la app rápida, pero cada elemento caché es un pasivo que debe estar en el almacenamiento seguro de la plataforma (el Keychain de iOS o el Android Keystore), ser mínimo e idealmente estar protegido por biometría o código de acceso. Traer un inventario exacto de lo que la app persiste localmente, dónde se guarda cada elemento, qué lo desbloquea y si las conexiones de alto valor usan fijación de certificados con un plan de rotación viable. En entornos empresariales, vincularlo a la política de gestión de dispositivos móviles y la borrado a distancia; y en el sector público, tratar los datos personales en el dispositivo como una exposición de privacidad y legalidad que debe justificarse, documentarse y ser defendible ante una auditoría.

## Perspectiva por sector

**Startup.** Con un equipo minúsculo y poca financiación, rara vez se pueden permitir dos bases de código nativas ni dos perfiles de competencia, así que un marco de trabajo multiplataforma o incluso una PWA que alcance ambas tiendas desde una sola base de código suele ganar. Lanzar con enfoque *offline-first* para la tarea central que importa, guardar cualquier token en el almacenamiento seguro de la plataforma en lugar de un archivo en texto plano, e incluir el tiempo de revisión de la tienda en cada lanzamiento para que un rechazo no comprometa la fecha. Dejar para cuando el uso real lo justifique las actualizaciones forzadas, la fijación de certificados y una granja de dispositivos.

**Pequeña empresa.** Sin un especialista en móvil y con un presupuesto ajustado, conviene apoyar con fuerza en comprar en lugar de construir: un generador de apps sin código, una app con marca blanca del proveedor del punto de venta o de reservas, o una PWA bien hecha a partir del sitio web existente suelen superar a una app a medida que no se puede mantener. Si se encarga una app, ser dueño de las claves de firma y las cuentas de tienda para que un contratista no tome el control de la presencia de la empresa, e imponer la accesibilidad y el almacenamiento seguro en el dispositivo en el contrato. Limitar el alcance a la o las dos tareas que los clientes realmente hacen en el teléfono.

**Empresa.** A gran escala, la app es un compromiso de larga duración que atraviesa muchos equipos, así que conviene estandarizar la estrategia de construcción, el patrón de almacenamiento seguro, la cadena de integración y entrega y la política de versión de APIs, en lugar de dejar que cada producto lo reinvente. Las aplicaciones internas para la plantilla suelen circular a través del MDM para la instalación, configuración, borrado a distancia y política, mientras que las aplicaciones para los clientes necesitan una granja de dispositivos que cubra el uso real, y una accesibilidad y seguridad auditadas. Gobernar de forma central las claves de firma, las credenciales de tienda y el momento de los lanzamientos para que un cambio incompatible en el backend nunca deje a la cola larga de clientes antiguos sin servicio.

**Sector público.** Las reglas de contratación, la transparencia y la rendición de cuentas pública condicionan cada decisión. Hay que atender a todos, incluidas las personas con dispositivos antiguos y conexiones lentas, así que la accesibilidad es una obligación legal verificada con herramientas de apoyo reales, y un rango amplio de compatibilidad de dispositivos es casi innegociable. Prefierense enfoques y contratos que eviten el acoplamiento a un proveedor, mantengan los datos portables y permitan que el público inspeccione qué hace la app con sus datos, y tratar los datos personales en el dispositivo como una exposición que debe justificarse y documentarse para una auditoría.

## Ejemplos

**Startup.** Una startup de tres personas que construía una app para seguir hábitos tenía que llegar a iOS y a Android, pero no podía permitirse dos bases de código nativas ni dos perfiles de competencia. Elegió un marco de trabajo multiplataforma para que un equipo pequeño pudiera publicar en ambas tiendas, y diseñó con enfoque *offline-first* desde el principio para que un usuario pudiera registrar un hábito en el metro sin señal y sincronizarlo después. Guardó el token de sesión en el almacenamiento seguro de la plataforma en lugar de un archivo en texto plano, incluyó el tiempo de revisión de la tienda en cada plan de lanzamiento y probó en un par de teléfonos viejos y económicos junto a los suyos, lo que les detectó una lentitud que de otro modo habrían publicado.

**Empresa.** Una compañía logística construyó una app interna para sus repartidores y personal de almacén. Como los almacenes y las rutas de reparto tienen señal irregular, el equipo optó por un diseño *offline-first*: las escaneos y las actualizaciones de estado se guardan localmente y se sincronizan cuando la conexión regresa. Usaron un marco de trabajo multiplataforma para servir una sola base de código a ambas plataformas con un equipo reducido. La app se distribuye a través del MDM en lugar de las tiendas públicas, de modo que el equipo de TI controla la instalación, la configuración y la política de seguridad en los dispositivos de la empresa. Las credenciales sensibles están en el almacenamiento seguro de la plataforma y la biometría desbloquea la app. Una granja de dispositivos en la nube prueba un abanico representativo de los terminales robustos que el personal lleva realmente.

**Sector público.** Un organismo nacional lanzó una app de ciudadanía para la identidad y las prestaciones. La accesibilidad fue un requisito hard desde el primer día: soporte completo del lector de pantalla, ajuste dinámico del tamaño del texto y fuerte contraste, probados con herramientas de apoyo reales para cumplir la ley. Como los ciudadanos usan una enorme variedad de dispositivos, el equipo soportó un rango amplio de modelos antiguos y conexiones lentas, y mantuvo las tareas esenciales funcionando sin conexión. Los datos sensibles permanecen en el almacenamiento seguro del dispositivo, la biometría protege el acceso, y las conexiones de alto valor usan fijación de certificados con un proceso de rotación previsto. La versión de las APIs mantiene funcionando a las apps antiguas ya instaladas, y existe un camino de actualización forzada, de uso excepcional, para correcciones de seguridad. Los plazos de revisión de la tienda se incorporan a cada plan de lanzamiento.

## Caso de negocio: motivaciones, retorno y coste total de propiedad

El móvil es donde muchos usuarios conocen su servicio, por lo que la app afecta a la adopción, la satisfacción y la finalización de las tareas que importan a la organización. Una app rápida, fiable y bien diseñada aumenta el uso y reduce la carga de soporte. Para las empresas, una app móvil interna puede hacer que una plantilla en movilidad sea mediblemente más productiva y reducir el papel. Para el sector público, una app de ciudadanía usable amplía el acceso y reduce la demanda de centros de atención y de atención presencial.

En el coste total de propiedad (TCO, por sus siglas en inglés), la elección del enfoque es la palanca más grande. Lo nativo implica pagar por dos bases de código y dos perfiles de competencia durante toda la vida de la app. El multiplataforma intercambia parte de eso por una dependencia que hay que mantener actualizada. Más allá del código, presupuestar las tarifas de tienda y los ciclos de revisión, un laboratorio de pruebas de dispositivos o una granja en la nube, el soporte continuo de versiones del sistema operativo a medida que las plataformas publican cada año, y el trabajo de seguridad que el móvil exige. El coste de no invertir se manifiesta en bloqueos en dispositivos no soportados, incidentes de seguridad por datos sin proteger en el dispositivo, lanzamientos rechazados o retrasados y usuarios que abandonan una app lenta o torpe.

Para hacer el caso ante la dirección, conectar la app con resultados concretos: finalización de tareas, retención, productividad de la plantilla o reducción del coste de soporte. Preciar la decisión de enfoque a lo largo de toda la vida de la app, no solo del primer lanzamiento, y nombrar los riesgos (seguridad, ley de accesibilidad, rechazo en la tienda) que una práctica móvil seria reduce.

## Antipatrones y trampas

- **Tratar el móvil como un sitio web en miniatura**: ignorar el tacto, los gestos y las convenciones de plataforma.
- **Asumir una red perfecta**: no hay manejo sin conexión, y la app se rompe en cuanto se pierde la señal.
- **Probar solo en la última gama alta**: ocultar un rendimiento deficiente en los dispositivos que los usuarios reales llevan.
- **Guardar secretos en archivos en texto plano**: datos sensibles expuestos ante la pérdida o robo del dispositivo.
- **Exceso de notificaciones**: demasiados pushes, y los usuarios silencian o borran la app.
- **Ignorar el tiempo de revisión de la tienda**: planes de lanzamiento que suponen una publicación instantánea y luego se retrasan.
- **Sin camino de actualización forzada**: versiones antiguas inseguras perviven sin forma de retirarlas.
- **Drenar batería y datos**: trabajo constante en segundo plano y comunicaciones verbosas que el usuario percibe.
- **La accesibilidad como adición tardía**: excluir usuarios y, en el sector público, incumplir la ley.
- **Una sola base de código forzada a parecer idéntica en todas partes**: una app que se siente extraña en ambas plataformas.

## Modelo de madurez

**Nivel 1: Iniciar.** Lo móvil es ad hoc y reactivo. La app se construye como un sitio web, se prueba en los teléfonos del equipo y con frecuencia se rompe sin conexión. Se piensa poco en el almacenamiento seguro, la accesibilidad o los plazos de revisión de la tienda. Los lanzamientos son un forcejeo manual estresante y nadie es responsable de la estrategia de construcción ni de las claves de firma.

**Nivel 2: Desarrollar.** Aparecen prácticas básicas, pero de forma inconsistente entre equipos y productos. Se elige un enfoque de construcción para una app dada, se siguen los fundamentos de la plataforma y se prueba en algunos dispositivos reales, y existe cierto manejo sin conexión y almacenamiento seguro. Las compilaciones están parcialmente automatizadas y alguien es responsable del envío a la tienda, pero otra app de otro equipo puede hacer todo esto de forma distinta o no hacerlo en absoluto.

**Nivel 3: Estandarizar.** La buena práctica está documentada y se aplica en toda la organización. El enfoque *offline-first* es la norma, un rango de compatibilidad de dispositivos documentado se prueba en un laboratorio de dispositivos o una granja en la nube, y se siguen y verifican con herramientas de apoyo reales las pautas de diseño y la accesibilidad de la plataforma. El almacenamiento seguro, la biometría y la versión de APIs son estándar, la integración y entrega continuas automatizan la compilación, las pruebas, la firma y la distribución beta, y el tiempo de revisión de la tienda se planifica en cada lanzamiento.

**Nivel 4: Gestionar.** La calidad móvil se mide y controla frente a líneas base. Los bloqueos, el arranque en frío, el renderizado de pantallas, el consumo de batería y datos, y las tasas de finalización de tareas se recogen de forma continua desde dispositivos reales y se siguen contra objetivos, con desgloses por modelo y versión del sistema operativo para que una regresión en hardware de gama baja se detecte, no se publique. La accesibilidad y la seguridad se auditan en lugar de darlas por sentadas, se monitorizan las tasas de baja de notificaciones y de adopción de actualizaciones, y el rango de soporte y la estrategia de construcción se revisan a la luz de esa evidencia. Las decisiones de matar o corregir un lanzamiento se toman en función de las métricas, no de cómo se sentía la app en el teléfono del responsable.

**Nivel 5: Orquestar.** Lo móvil se mejora de forma continua y se integra en toda la organización, y se adapta a medida que el panorama de dispositivos cambia. La rotación de certificados, los caminos de actualización forzada y la reversión son rutinarios, el rango de soporte y la estrategia de construcción se redefinen con evidencia a medida que las plataformas publican cada año, y todo el abanico de usuarios y dispositivos se trata como un ciudadano de primera clase. La planificación móvil se articula con la seguridad, la accesibilidad, las APIs y la práctica de entrega, de modo que un cambio de sistema operativo, una nueva categoría de dispositivo o un giro de política se absorbe como trabajo rutinario y no como una emergencia.

## Ideas para la reflexión

- ¿Cómo se decide entre el enfoque nativo, el multiplataforma y la PWA para un producto dado?
- ¿Qué rango de dispositivos y versiones del sistema operativo encaja con los datos de uso reales y cómo se mantiene actualizado?
- Dónde es esencial el enfoque *offline-first* en la app y cómo se gestionarán los conflictos de sincronización?
- ¿Cuándo está justificada una actualización forzada y cómo se evita bloquear injustamente a los usuarios?
- ¿Cómo se probará en dispositivos reales a una escala que refleje a los usuarios?
- ¿Qué datos sensibles hay en el dispositivo y cómo se protege cada uno?
- ¿Cómo se honran las convenciones de cada plataforma desde una base de código compartida?

## Puntos clave

- Elegir la estrategia de construcción (nativa, multiplataforma o PWA) para la vida completa de la app.
- Seguir las pautas de diseño de cada plataforma para que la app se sienta familiar y reduzca el esfuerzo del usuario.
- Diseñar para las restricciones del móvil: *offline-first*, frugalidad en batería y datos, fragmentación, pantallas pequeñas.
- No se controla el momento del lanzamiento; planificar la revisión de la tienda, la versión y las actualizaciones forzadas.
- Usar las notificaciones push y los enlaces profundos con mesura y consentimiento.
- Proteger los datos en el dispositivo con almacenamiento seguro, biometría y, donde proceda, fijación de certificados.
- Probar en dispositivos reales y automatizar la cadena de entregas móviles a través de la integración y entrega continuas.
- Hacer de la accesibilidad un requisito, que en el sector público es una obligación legal.

## Referencias y lectura complementaria

- Apple, *Human Interface Guidelines*
- Google, *Pautas de Material Design*
- Apple, *Pautas de revisión de la App Store*
- Google, *Políticas de Google Play y documentación del desarrollador de Android*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* y *Mobile Security Testing Guide*
- Documentación del proyecto React Native
- Documentación del proyecto Flutter
- Google, *web.dev*, orientación sobre aplicaciones web progresivas
- Sección 508 de EE. UU. y WCAG (Directrices de accesibilidad del contenido web) como referencias de accesibilidad móvil
- NIST, *Directrices de seguridad y gestión de dispositivos móviles*

