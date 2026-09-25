# 2.5 Revisión de código y colaboración

## Visión general y motivación

La [revisión de código](https://en.wikipedia.org/wiki/Code_review) consiste en que alguien distinto al autor examine un cambio antes de que se integre. Es una de las actividades de mayor impacto en cuanto a calidad y difusión del conocimiento que una organización de software puede realizar, y en equipos grandes, además, constituye el principal mecanismo de coordinación y de cultura. La revisión detecta defectos, extiende el conocimiento del código, impone estándares y forma a los ingenieros, pero solo cuando se hace bien. Hecha mal, se convierte en un cuello de botella, en una fuente de fricción o en una aprobación mecánica que genera una falsa sensación de seguridad.

En equipos grandes, la revisión es el punto donde el trabajo individual se encuentra con la propiedad colectiva. Suele ser el principal contacto entre ingenieros que, de lo contrario, trabajan en solitario, por lo que sus normas moldean la forma en que toda la organización colabora. La revisión difunde el conocimiento para que ninguna parte del sistema dependa del saber de una sola persona, lo que reduce el riesgo del [factor bus](https://en.wikipedia.org/wiki/Bus_factor) (el peligro de que el conocimiento esté concentrado en muy pocas personas) que atormenta a los sistemas grandes y de larga vida. Además, crea un registro de quién cambió qué y quién lo aprobó.

En entornos empresariales y de organismos públicos, la revisión suele tener una dimensión de cumplimiento normativo. La [segregación de funciones](https://en.wikipedia.org/wiki/Separation_of_duties) (que una sola persona no controle un cambio sensible de principio a fin), las aprobaciones obligatorias y la trazabilidad son controles con frecuencia requeridos. Un cambio que afecta a sistemas sensibles puede necesitar la revisión de roles específicos, y el registro de esa revisión se convierte en evidencia de auditoría. El reto es cumplir estos controles manteniendo la revisión ágil y constructiva, en lugar de convertirla en un mero trámite.

## Principios clave

- Revisar para mejorar el cambio y compartir conocimiento, no para lucirse.
- Los cambios pequeños reciben mejores revisiones, así que mantén las *pull requests* (PRs) centradas y de un tamaño razonable.
- La latencia de la revisión es un costo colectivo. Un tiempo de respuesta rápido mantiene en movimiento a todos.
- Automatiza lo mecánico (estilo, pruebas, análisis de seguridad) para que las personas revisen el diseño y la corrección.
- Distingue los problemas bloqueantes de las sugerencias y preferencias, y sé explícito sobre qué es cada uno.
- Critica el código, no a la persona. Las normas de retroalimentación determinan si la revisión construye confianza o la erosiona.
- El autor es responsable de hacer que su cambio sea fácil de revisar.

## Recomendaciones

### Haz que las pull requests sean pequeñas y bien descritas

Cada cambio debe centrarse en una única preocupación lógica y ser lo suficientemente pequeño como para poder revisarse con cuidado. Las PRs extensas reciben revisiones superficiales. Acompaña cada una con una descripción clara de qué cambió, por qué y cómo se verificó, para que el revisor tenga contexto. Separa los refactorizaciones mecánicas de los cambios de comportamiento en PRs distintas, para que cada una sea fácil de razonar. Una buena descripción es la contribución más importante del autor a la calidad de la revisión.

### Establece estándares y listas de verificación para la revisión

Especifica qué deben buscar los revisores: corrección, adecuación de diseño, suficiencia de pruebas, implicaciones de seguridad, legibilidad y cumplimiento de estándares. Una lista de verificación ligera mantiene las revisiones consistentes y evita que dimensiones importantes se escapen, sin convertir la revisión en un ejercicio de casillas. Define qué requiere revisión, quién puede aprobar y cuáles son las aprobaciones basadas en roles necesarias para las áreas sensibles.

### Fija y vigila normas de latencia de revisión

Acuerda un plazo objetivo de respuesta, por ejemplo, responder en un día hábil, y considera la revisión una parte primera de la jornada en lugar de algo que se deja para el final. Las colas de revisión largas frenan la entrega y tentan a los ingenieros a hacer cambios más grandes y agrupados. Monitoriza el tiempo hasta la primera revisión y el tiempo hasta la integración, y trata la latencia sostenida como un problema de proceso a resolver, no como una falla personal.

### Automatiza todo lo mecánico

Ejecuta el formato, el [análisis estático](https://en.wikipedia.org/wiki/Lint_(software)), las pruebas y los escaneos de seguridad y dependencias en la [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), para que los revisores no gasten atención en ello. Reserva la revisión humana para aquello que las máquinas no pueden juzgar: si el diseño es correcto, si el enfoque encaja con el sistema, si las pruebas son significativas y si el código seguirá teniendo sentido en el futuro.

### Utiliza la programación en parejas y en grupo donde correspondan

Reserva la [programación en parejas](https://en.wikipedia.org/wiki/Pair_programming), en la que dos ingenieros escriben código juntos en un mismo puesto, para trabajo complejo o de alto riesgo, para la incorporación de nuevos miembros y para la transferencia de conocimiento. Es una revisión continua que, con frecuencia, elimina la necesidad de un paso de revisión separado. Usa la [programación en grupo](https://en.wikipedia.org/wiki/Mob_programming), donde todo el equipo trabaja en una tarea a la vez, para decisiones de diseño críticas o para extender el conocimiento de un área complicada a todo el equipo. Piensa en estas prácticas como complementos de la revisión asíncrona, elegidos según el contexto, no como sustitutos que deban imponerse en todo momento.

### Adota la revisión automatizada y asistida por IA con prudencia

Utiliza herramientas de revisión automatizada y asistentes de IA para detectar problemas comunes, sugerir mejoras y aliviar la carga del revisor, pero trata su resultado como una entrada, no como una autoridad. La revisión con IA es buena para problemas de superficie y coherencia, pero floja en el juicio profundo sobre diseño y en el contexto del sistema. Mantén a una persona responsable de cada aprobación, especialmente en cambios sensibles a la seguridad y relevantes para el cumplimiento.

### Fija normas de retroalimentación constructiva

Establece normas que mantengan los comentarios específicos, amables y centrados en el código. Anima a los revisores a formular preguntas en lugar de dar órdenes, a explicar el razonamiento detrás de cada solicitud y a reconocer el buen trabajo. Marca claramente las preocupaciones bloqueantes y las sugerencias opcionales (por ejemplo, añadiendo un prefijo a las notas no bloqueantes). Estas normas determinan si la revisión fortalece al equipo o si genera resentimiento.

## Contrapartidas: ventajas y desventajas

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Revisión asíncrona por PR | Flexible; documentada; escalable entre zonas horarias | Latencia; pierde matices; puede parecer adversarial |
| Programación en parejas | Revisión continua; transferencia rápida de conocimiento; alta calidad | Dos personas en una tarea; agotadora; difícil de coordinar |
| Programación en grupo | Alineación del equipo completo; difunde el conocimiento en profundidad | Costosa en conjunto; no apta para trabajo rutinario |
| Aprobación múltiple obligatoria | Alta garantía; apta para cumplimiento normativo | Más lenta; diluye la responsabilidad; presiona la cola |
| Revisión asistida por IA | Rápida, incansable con los problemas comunes; reduce la carga | Ignora el contexto del sistema; genera falsa confianza si se confía en exceso |

La tensión central es entre el rigor y la velocidad. Una revisión más profunda detecta más, pero frena la entrega y puede frustrar a los autores. Una revisión más ágil mantiene el flujo, pero corre el riesgo de ser superficial. La salida consiste en adaptar la profundidad de la revisión al riesgo del cambio, de modo que los cambios triviales reciban una revisión ligera y los riesgosos, una más exhaustiva, y en automatizar el trabajo mecánico para concentrar el esfuerzo humano donde de verdad importa.

## Preguntas para discutir con el equipo

1. **¿Qué se considera demasiado grande para una sola pull request y se separan las refactorizaciones mecánicas de los cambios de comportamiento?** Este capítulo afirma con claridad que las PRs extensas reciben revisiones superficiales y que el autor es el responsable de la revisabilidad, y pide separar las refactorizaciones de los cambios de comportamiento para que cada uno sea fácil de razonar. En un equipo grande, una PR gigante garantiza una aprobación mecánica que da una falsa sensación de seguridad mientras deja pasar defectos reales. Trae la evidencia: la distribución de tamaños de PRs del equipo y cómo cae la profundidad de la revisión a medida que crecen los difus. Acuerda una norma práctica de tamaño y el hábito de integrar las refactorizaciones puras por separado de los cambios de lógica, para que un revisor pueda realmente mantener cada cambio en la cabeza. Esa sola disciplina eleva la calidad de cada revisión que sigue.

2. **¿Cómo se distingue una objeción bloqueante de una sugerencia opcional, y esa convención se aplica de verdad?** El capítulo pide separar los problemas bloqueantes de las preferencias y ser explícito sobre cuál es cuál, y señala que bloquear por una preferencia es un antipatrón corrosivo. Sin una convención compartida, una opinión de estilo de un revisor se lee como un cambio obligatorio, lo que genera resentimiento y frena la entrega de todo el equipo. Trae ejemplos de revisiones recientes donde una preferencia haya retrasado una integración, como señal concreto. Adota un marcador ligero, por ejemplo un prefijo que etiquete las notas no bloqueantes, para que el autor sepa al instante qué debe cambiar y qué es una sugerencia. Así la revisión se centra en la corrección y el diseño en lugar de en los gustos personales.

3. **¿Quién debe aprobar los cambios en código sensible a la seguridad o relevante para el cumplimiento, y cómo se garantiza ese enrutamiento?** Este capítulo describe aprobaciones basadas en roles, reglas de propiedad de código y segregación de funciones en la que una sola persona no controla un cambio sensible de principio a fin, con la aprobación registrada como evidencia de auditoría. En entornos empresariales y de organismos públicos son controles obligatorios, y el riesgo es que se saltan o se convierten en un cuello de botella que paraliza la entrega. Trae la señal: qué módulos son sensibles y si las reglas de propiedad actuales enrutian esos cambios automáticamente a los aprobadores correctos. Codifica el enrutamiento en la configuración de propiedad de código y combínalo con verificaciones automatizadas y cambios pequeños, de modo que el control se cumpla sin una cola de aprobación manual. Decide esto de forma deliberada en lugar de descubrir la carencia durante una auditoría.

4. **¿Cuál es el objetivo de latencia de revisión que realmente habéis acordado, se mide y se aplica, o es solo un deseo?** El capítulo trata la latencia de la revisión como un costo colectivo y pide monitorizar el tiempo hasta la primera revisión y el tiempo hasta la integración, tratando el retraso sostenido como un problema de proceso y no como una falla personal. En un equipo grande, una cola de revisión sin dueño grava en silencio a todos: los autores agrupan cambios más grandes para evitar la espera, esos cambios reciben entonces una revisión más superficial y el tiempo de entrega se alarga sin que haya un único culpable. La consideración contraria es que un plazo estricto puede empujar a los revisores a escanear superficialmente, por lo que velocidad y profundidad deben equilibrarse, no intercambiarse a ciegas. Trae la evidencia: la distribución actual del tiempo hasta la primera revisión, cómo varía por equipo y por tamaño de cambio, y dónde se acumulan las revisiones más tiempo. En entornos empresariales y de organismos públicos, vincula el objetivo a las métricas de flujo que la dirección ya sigue, porque un control de aprobación múltiple obligatorio sin una norma de latencia se convierte en el cuello de botella que paraliza la entrega y tienta a los equipos a esquivar el control por completo.

5. **¿Para qué tipos de cambio se confía en la revisión automatizada y asistida por IA, y dónde debe mantenerse la responsabilidad humana?** El capítulo dice que el resultado de una revisión con IA debe tratarse como una entrada, no como una autoridad: fuerte en problemas de superficie y coherencia, débil en el juicio profundo sobre diseño y en el contexto del sistema, con una persona responsable de cada aprobación. Sin un límite explícito, un equipo grande deriva hacia la confianza excesiva, donde un comentario verde de un bot se lee como una revisión superada y los riesgos reales de diseño y seguridad se filtran bajo una falsa sensación de seguridad. La fuerza contraria es que la revisión con IA alivia genuinamente la carga y detecta defectos comunes de forma incansable, por lo que prohibirla desperdicia una palanca valiosa. Trae la evidencia: dónde las sugerencias automatizadas han detectado problemas reales, dónde han generado ruido y qué tipos de cambio (sensibles a la seguridad, relevantes para el cumplimiento, arquitectónicos) nunca se dejarían al arbitrio de una máquina sola. En el trabajo empresarial y de organismos públicos, señala quién asume la responsabilidad de una aprobación cuando un asistente de IA estuvo en el proceso, porque una auditoría preguntará quién revisó un cambio y «lo hizo la herramienta» no es una respuesta que un regulador acepte.

6. **¿Dónde deben la programación en parejas o en grupo sustituir a la revisión asíncrona, y cómo se usa la revisión para reducir el riesgo del factor bus de forma deliberada?** El capítulo presenta la programación en parejas y en grupo como revisión continua elegida por contexto, y nombra la revisión como el mecanismo que difunde el conocimiento para que ninguna parte del sistema dependa de una sola persona. Si se deja implícito, el conocimiento se concentra: el mismo experto revisa todo cambio en un subsistema, la revisión se convierte en una aprobación mecánica porque nadie más puede contradecirlo y el riesgo del factor bus crece justo donde el sistema es más crítico. La consideración contraria es el costo, ya que la programación en grupo consume el tiempo de todo el equipo y la programación en parejas ata a dos ingenieros, por lo que no puede imponerse en todo momento. Trae la evidencia: qué módulos tienen solo un revisor creíble, dónde se atasca la incorporación y dónde una área complicada beneficiaría de una sesión en vivo frente a hilos de comentarios. En una organización grande o pública, considera la difusión deliberada del conocimiento como gestión de riesgo, porque un sistema de larga vida cuyas partes críticas dependen de una sola persona es una responsabilidad operativa y de continuidad, no una simple incomodidad de plantilla.

## Perspectiva por sector

**Startup.** Con tres o cuatro ingenieros, mantén la revisión ligera: la aprobación de un compañero en una PR pequeña, los checks mecánicos en CI y ningún segundo revisor obligatorio que paralice una integración. El objetivo real es menos el cumplimiento que asegurarse de que más de una persona entienda cada parte del sistema, así que programa en parejas las piezas riesgosas y trátalo como incorporación. No construyas un sistema de enrutamiento por propiedad de código que pronto quedarás grande; una norma compartida de cambios pequeños y bien descritos aporta la mayor parte del beneficio a un coste casi nulo.

**Pequeña empresa.** Es improbable que tengas un especialista en herramientas de revisión, así que aprovecha lo que tu plataforma de alojamiento (por ejemplo, un servicio gestionado de Git) ofrece de serie en lugar de construir automatizaciones a medida. Contrata las integraciones de análisis estático, pruebas y escaneo de seguridad en lugar de mantenerlas tú, para que tus pocos ingenieros dediquen sus escasos minutos de revisión a diseño y corrección. Mantén una sola regla simple: cada cambio recibe los ojos de otra persona, y resiste la tentación de añadir procesos que no tienes a nadie que los mantenga.

**Empresa grande.** El reto es la consistencia entre muchos equipos: estándares compartidos, reglas de propiedad de código que enrutian los cambios sensibles a los aprobadores correctos y aprobaciones basadas en roles registradas como evidencia de auditoría. Automatiza los checks mecánicos a nivel de organización para que la revisión humana se concentre en el diseño, y monitoriza la latencia de la revisión como una métrica de flujo para que los controles de aprobación múltiple obligatoria no se conviertan en cuellos de botella en silencio. Adapta la profundidad de la revisión al riesgo del cambio con una política documentada, de modo que los cambios triviales se mantengan rápidos y los de alto riesgo reciban segregación de funciones y un escrutinio más profundo.

**Organismo público.** El control de cambios suele ser obligatorio: cada cambio en producción revisado y aprobado por alguien distinto del autor, con el registro conservado como evidencia de auditoría para cumplir los requisitos de segregación de funciones. Prioriza una huella transparente y trazable de quién autoró, quién aprobó y qué verificaciones pasaron, e invierte en automatización y en cambios pequeños y frecuentes para que el control no paralice la entrega. Cuando la herramienta de revisión se adquiera, exija registros de auditoría exportables y evita el *vendor lock-in*, porque la evidencia debe sobrevivir a cualquier proveedor individual y resistir el escrutinio público.

## Ejemplos

**Startup.** Una startup de cuatro ingenieros mantiene cada PR pequeña y pide la aprobación de un compañero antes de integrar, no tanto por cumplimiento como para asegurarse de que ninguna persona sea la única que entienda una parte del sistema. La CI ejecuta el formateador y las pruebas, así que las personas dedican sus pocos minutos de revisión a diseño y corrección en lugar de a espacios. Cuando el equipo se topa con una pieza complicada del flujo de pagos, dos de ellos programan en parejas en lugar de intercambiar comentarios asíncronos, lo que duplica como incorporación del miembro más nuevo.

**Empresa grande.** Una gran empresa de software exige al menos una aprobación de revisión en cada cambio, más una segunda aprobación para los cambios en módulos sensibles a la seguridad identificados por las reglas de propiedad de código. La CI gestiona todas las verificaciones de estilo y pruebas, para que los revisores se concentren en diseño y corrección. El equipo monitoriza el tiempo hasta la primera revisión y trata un mediana en ascenso como una señal para reequilibrar la carga de trabajo. Los nuevos ingenieros se incorporan mediante la programación en parejas, lo que acorta su camino hacia la contribución autónoma.

**Organismo público.** Una agencia nacional que opera bajo requisitos estrictos de control de cambios exige que cada cambio en producción sea revisado y aprobado por alguien distinto del autor, con la aprobación registrada para auditoría. Para que este control no se convierta en un cuello de botella, la agencia invierte en verificaciones automatizadas y en cambios pequeños y frecuentes, y establece una norma de respuesta de revisión el mismo día. La huella de la revisión, que abarca quién autoró, quién aprobó y qué verificaciones pasaron, forma parte de la evidencia de cumplimiento de cada lanzamiento, satisfaciendo los requisitos de segregación de funciones sin paralizar la entrega.

## Justificación económica: motivaciones, retorno de inversión y coste total de propiedad

La revisión de código devuelve el esfuerzo en tres divisas: defectos detectados antes de llegar a producción, conocimiento difundido por todo el equipo y estándares aplicados de forma automática con el tiempo. Detectar un defecto en la revisión es mucho más barato que detectarlo en producción, y el beneficio de la difusión del conocimiento reduce el riesgo de dependencia de personas clave que, de lo contrario, puede costarle carísimo a una organización cuando alguien se va. La revisión es también el mecanismo de transmisión cultural que mantiene coherente a un equipo en crecimiento.

El costo de la revisión es tiempo de ingenieros y algo de latencia, ambos manejables con buenas prácticas. El costo de *no* revisar, o de revisar mal, incluye defectos en producción, conocimiento en silos, código inconsistente y, en entornos regulados, auditorías fallidas y hallazgos de incumplimiento. Una revisión excesivamente pesada también tiene un costo real: colas largas, lotes excesivos, ingenieros desmotivados. Para presentar el caso a la dirección, vincula las prácticas de revisión con la tasa de fallo por cambio, el tiempo de entrega y la velocidad de incorporación, y monitoriza la latencia de la revisión como una métrica de flujo explícita.

## Antipatrones y trampas

- **La aprobación mecánica:** aprobaciones sin examen real, que brindan una falsa seguridad y satisfacen solo la letra de un control.
- **La PR gigante:** miles de líneas que solo pueden escanearse, garantizando una revisión superficial.
- **La revisión de detalles triviales:** centrarse en trivialidades mientras se pasan por alto el diseño y la corrección, a menudo porque los checks mecánicos no están automatizados.
- **La revisión como postura restrictiva:** usar la revisión para afirmar dominio o bloquear a otros, envenenando la colaboración.
- **La cola lenta:** revisiones que permanecen días, frenando la entrega y fomentando el agrupamiento de cambios.
- **La confianza excesiva en la IA:** tratar las sugerencias automatizadas como autoritativas y abandonar el juicio humano en cambios riesgosos.
- **Bloquear por preferencia:** presentar opiniones de estilo personal como cambios obligatorios sin distinguirlas de defectos reales.

## Modelo de madurez

- **Nivel 1, Iniciar:** La revisión es ad hoc y reactiva. A menudo se omite o se aplica de forma inconsistente, los comentarios se llenan de problemas mecánicos, las normas de retroalimentación no están fijadas y cualquier rastro de aprobación es incidental, no deliberado.
- **Nivel 2, Desarrollar:** Existen prácticas básicas de revisión, pero varían de un equipo a otro. La revisión es obligatoria en algunos lugares y lenta o opcional en otros, la automatización es parcial y el tamaño y la calidad de las PRs oscilan mucho, sin una expectativa compartida.
- **Nivel 3, Estandarizar:** Los estándares están documentados y se aplican a toda la organización. PRs pequeñas y centradas, formateo, análisis estático, pruebas y escaneos de seguridad en CI, listas de verificación claras, una convención explícita de lo bloqueante frente a lo sugerido y reglas de propiedad de código que enrutian los cambios sensibles a los aprobadores correctos.
- **Nivel 4, Gestionar:** La revisión se mide y controla frente a líneas de base. Se siguen el tiempo hasta la primera revisión, el tiempo hasta la integración, la profundidad de revisión frente al riesgo del cambio, la tasa de fuga de defectos y la tasa de fallo por cambio; el retraso sostenido se trata como un problema de proceso; y los datos guían dónde reequilibrar la carga de revisores y dónde los controles frenan la entrega sin añadir garantías.
- **Nivel 5, Orquestar:** La revisión mejora de forma continua y se integra en toda la organización. La profundidad se adapta al riesgo del cambio; la programación en parejas, en grupo y la asistencia por IA se usan con intención y con una persona responsable; la difusión del conocimiento y el riesgo del factor bus se gestionan de forma deliberada, y la revisión mejora de manera medible la calidad, el flujo de entrega y la velocidad de incorporación.

## Ideas para el debate

- ¿Cuál es el objetivo de latencia de revisión adecuado para vuestro equipo y qué os impide alcanzarlo?
- ¿Cómo se adapta la profundidad de la revisión al riesgo del cambio sin añadir burocracia?
- ¿Dónde superan la programación en parejas o en grupo a la revisión asíncrona en vuestro contexto?
- ¿Cuánta confianza debe depositarse en la revisión asistida por IA y para qué tipos de cambios?
- ¿Cómo se mantiene la retroalimentación de revisión constructiva a medida que el equipo crece y se diversifica?
- ¿Cómo se satisfacen los requisitos de aprobación de cumplimiento sin crear cuellos de botella?

## Puntos clave

- Mantén las pull requests pequeñas y bien descritas; el autor es el responsable de la revisabilidad.
- Automatiza lo mecánico para que las personas revisen diseño, corrección y pruebas.
- Monitoriza y gestiona la latencia de la revisión como un costo de flujo colectivo.
- Adapta la profundidad de la revisión al riesgo del cambio y distingue los problemas bloqueantes de las preferencias.
- Usa la programación en parejas, en grupo y la asistencia por IA como complementos según el contexto, manteniendo siempre la responsabilidad humana.

## Referencias y lectura adicional

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (como referente ejemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (sobre la programación en parejas)
- Woody Zuill, escritos sobre programación en grupo
- Michael Lopp, *Managing Humans* (sobre la colaboración en ingeniería)

