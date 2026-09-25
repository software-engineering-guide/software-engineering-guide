# 2.7 Documentación

## Visión general y motivación

La [documentación](https://en.wikipedia.org/wiki/Software_documentation) es el conocimiento escrito que permite a las personas usar, operar y modificar software sin tener que reconstruir su comprensión a partir del código por sí solo. Se presenta en múltiples géneros: cómo empezar, cómo llevar a cabo una tarea, cómo está estructurado un sistema, cómo responder a un incidente, qué acepta y devuelve una [API](https://en.wikipedia.org/wiki/API). Cada uno atiende a un lector distinto con una necesidad distinta. Una buena documentación no es opcional: es la diferencia entre un conocimiento que escala en toda una organización y uno que vive en la cabeza de pocas personas.

En equipos grandes, la documentación es su mejor defensa contra el riesgo de dependencia de personas clave (el peligro que surge cuando el conocimiento crítico reside en una o dos personas) y su vía más rápida para incorporar a nuevos miembros. Cuando cientos de ingenieros dependen de sistemas que no construyeron, y la gente entra, se mueve y sale continuamente, la organización solo puede funcionar si el conocimiento está escrito y es fácil de encontrar. Los sistemas sin documentación se vuelven frágiles: solo sus autores pueden modificarlos con seguridad, y cuando esos autores se van, la organización pierde la capacidad de mantener su propio software. Esa es una de las fallas más frecuentes y costosas a gran escala.

En entornos empresariales y gubernamentales, la jugada sube de nivel. Los sistemas tienen una vida larga, así que la documentación debe servir a los mantenedores años, incluso décadas, después de que el equipo original haya desaparecido. Los regímenes regulatorios y de auditoría suelen exigir documentos concretos como evidencia de control: registros de arquitectura, [manuales de operaciones](https://en.wikipedia.org/wiki/Runbook) (procedimientos paso a paso para la operación y la respuesta a incidentes) y registros de decisiones. Los sistemas del sector público que se transfieren entre proveedores dependen por completo de la documentación para transmitir el conocimiento a través de los límites contractuales. Y, sin embargo, la documentación es notoriamente propensa a la obsolescencia, de modo que el verdadero reto es mantenerla precisa a medida que el software evoluciona.

## Principios clave

- Escriba para un lector concreto con una necesidad concreta; cada tipo de documentación cumple un propósito diferente.
- Mantenga la documentación cerca del código y trátela como código (*docs-as-code*).
- La exactitud prima sobre la completitud; una cantidad reducida de documentación fiable vale más que una abundante que resulta errónea.
- Genere lo que pueda generarse; no mantenga a mano lo que una herramienta puede producir a partir de la fuente de verdad.
- Combatir la obsolescencia documental de forma activa: la documentación desactualizada es peor que ninguna, porque engaña.
- Haga que la documentación sea descubreble; el conocimiento inalcanzable es, en la práctica, inexistente.
- Registre las decisiones y su justificación, no solo el estado actual.

## Recomendaciones

### Adopte documentación como código

Guarde la documentación en [control de versiones](https://en.wikipedia.org/wiki/Version_control) junto al código que describe, redíjala en marcado de texto plano y revísela a través del mismo proceso de solicitud de fusión. Así queda versionada, revisable y próxima al código, de modo que puede actualizar ambos de forma conjunta. Púbelela mediante una pipeline automatizada para que la última versión esté siempre disponible. Tratar la documentación como código introduce la misma disciplina que mantiene el código fiable: revisión, historial y automatización.

### Estructure el contenido con el marco Diátaxis

Organice la documentación en cuatro tipos bien diferenciados, porque mezclarlos no sirve bien a ningún lector: tutoriales (orientados al aprendizaje, para principiantes), guías de uso (orientadas a la tarea, para un objetivo concreto), referencia (orientada a la información, precisa y completa) y explicación (orientada a la comprensión, el porqué y el contexto). Manténgalos separados y todo se vuelve más fácil de escribir, navegar y mantener, porque cada página tiene una labor clara y un público claro.

### Mantenga los documentos operativos esenciales

Proporcione a cada repositorio un [README](https://en.wikipedia.org/wiki/README) claro como su puerta de entrada: qué es, cómo compilarlo y ejecutarlo, y a dónde ir a continuación. Redacte manuales de operaciones para tareas operativas y respuesta a incidentes, de modo que cualquier persona de guardia pueda actuar, no solo los expertos. Mantenga documentación de arquitectura que explique la estructura del sistema y sus componentes clave. Ofrezca también documentación de incorporación que permita a un nuevo ingeniero ser productivo con rapidez. Esos son los documentos que más se extrañan cuando faltan.

### Genere la documentación de API y los registros de cambios a partir de la fuente de verdad

Genere la documentación de referencia de la API a partir del contrato legible por máquina o de las anotaciones del código, para que no pueda desviarse de la interfaz real. Mantenga un [registro de cambios](https://en.wikipedia.org/wiki/Changelog), idealmente generado a partir de compromisos estructurados o notas de publicación, para que los consumidores puedan ver qué cambió entre versiones. Automatizar estos procesos quita de encima la documentación generativa más propensa a la obsolescencia y la mantiene fiable.

### Registre las decisiones de arquitectura

Capture las decisiones arquitectónicas y de diseño significativas en registros ligeros y datados que declaren el contexto, la decisión y sus consecuencias. Esos registros preservan la justificación que de otro modo se perdería, de modo que los mantenedores futuros puedan ver por qué el sistema es como es, en lugar de poner en duda decisiones acertadas o repetir errores ya superados. Su rendimiento se manifiesta con especial fuerza en los largos ciclos de vida de los sistemas empresariales y gubernamentales.

### Combatir la obsolescencia documental con determinación

Trate la documentación obsoleta como un defecto. Actualice la documentación en el mismo cambio que altera el comportamiento, y conviértalo en un requisito de revisión. Asigne propiedad: cada documento importante debe tener alguien responsable de él. Revise la documentación de alto valor en cuanto a su exactitud periódicamente, elimine lo obsoleto y retire o señale claramente lo que ya no inspira confianza. La documentación que menos envejece es la documentación viva: la que se genera o se prueba contra el sistema en sí.

### Invierta en la gestión del conocimiento y la descubrebilidad

Haga que la documentación sea hallable mediante una buena búsqueda, una navegación clara y un hogar conocido, para que la gente pueda localizar lo que necesita sin tener que preguntar a nadie. No permita que se fragmente en demasiados wikis y herramientas desconectadas. Y capture el [conocimiento tácito](https://en.wikipedia.org/wiki/Tacit_knowledge) (la comprensión informal que vive en los hilos de chat y en las mentes de las personas) en forma duradera y descubreble antes de que se pierda.

## Costos y beneficios

| Enfoque | Ventajas | Desventajas |
|---|---|---|
| Documentación como código | Versionada, revisable, próxima al código; baja obsolescencia | Exige disciplina del ingeniero; menos amable para autores no técnicos |
| Wiki / base de conocimiento | Fácil de editar; accesible para todos | Se desvía del código; se fragmenta; envejece en silencio |
| Documentación generada (API, registro de cambios) | Siempre exacta; bajo mantenimiento | Limitada a lo que la fuente expresa; requiere herramienta |
| Explicación escrita a mano | Rico en contexto y justificación que las máquinas no producen | Laboriosa; propensa a quedar obsoleta |
| Estructura Diátaxis | Propósito claro por página; más fácil de navegar y mantener | Esfuerzo inicial de estructuración; exige disciplina de autoría |

El equilibrio central es entre el esfuerzo y la exactitud y durabilidad. La documentación más barata de escribir, una rápida página en un wiki, es también la más propensa a la obsolescencia y la fragmentación. La más durable, generada a partir de la fuente o revisada como código, cuesta más disciplina al principio, pero se mantiene fiable. Una buena regla práctica: genere lo que pueda, mantenga lo demás cerca del código y revíselo como código, y reserve el esfuerzo de la explicación escrita a mano para la justificación que solo las personas pueden ofrecer.

## Preguntas para debatir con el equipo

1. **¿Están los documentos separados por necesidad del lector, o tutoriales, referencia y explicación se amontonan en una misma página?** Este capítulo recomienda la separación Diátaxis en tutoriales, guías de uso, referencia y explicación, y señala la mezcla de tipos como un antipatrón que no sirve bien a ningún lector. A gran escala, un principiante que aprende el sistema y un ingeniero de guardia que busca un dato preciso necesitan páginas distintas, y una página mixta frena a ambos. Aporte la señal: elija sus documentos más visitados y verifique si cada uno tiene una labor clara y un público claro. Reestructure los peores ejemplos en tipos distintos, para que cada página sea más fácil de escribir, navegar y mantener. Esa estructura es lo que hace que la documentación sea mantenible a medida que la organización crece.

2. **¿Capturan las decisiones de arquitectura significativas con su justificación, o solo el estado actual?** El capítulo recomienda registros ligeros y datados que declaren contexto, decisión y consecuencias, y señala que su rendimiento se manifiesta con especial fuerza en los largos ciclos de vida de los sistemas empresariales y gubernamentales. Sin ellos, un mantenedor años después no puede ver por qué el sistema es como es, y termina poniendo en duda decisiones acertadas o repitiendo errores antiguos. Aporte como señal concreta una decisión difícil reciente cuya justificación ahora vive solo en un hilo de chat o en la memoria de alguien. Adote un formato breve de registro de decisión e incorpore la redacción de uno a cualquier cambio de diseño significativo. La justificación es exactamente ese conocimiento que solo las personas pueden ofrecer y que envejece más rápido cuando no se escribe.

3. **¿Cualquier ingeniero de guardia puede responder a un incidente a partir de sus manuales de operaciones, sin tener que buscar a la persona que construyó el sistema?** El capítulo nombra los manuales de operaciones como documento operativo esencial para que cualquier persona de guardia pueda actuar, no solo los expertos, y describe un equipo gubernamental que solo pudo heredar un sistema porque los manuales de operaciones transportaron el conocimiento a través de un límite contractual. El riesgo de dependencia de personas clave es la falla que esto previene: cuando el único experto no está disponible o ya no está, un procedimiento de recuperación sin documentación convierte un incidente rutinario en una caída del servicio. Aporte la evidencia: tome un incidente reciente y verifique si el manual de operaciones, por sí solo, lo habría resuelto. Escriba y pruebe manuales para los procedimientos que la gente teme, y trate un manual que no pueda sostenerse por sí mismo como un defecto. Esa es la diferencia entre una recuperación a las dos de la madrugada y una escalada a las dos de la madrugada.

4. **¿Cuáles de sus referencias de API y registros de cambios se generan a partir de la fuente de verdad y cuáles se mantienen a mano y se están desviando en silencio?** El capítulo indica generar la documentación de referencia a partir del contrato legible por máquina o de las anotaciones del código para que no pueda divergir de la interfaz real, y señala como antipatrón el mantenimiento manual de contenido generable. En un equipo grande, un documento de API escrito a mano que va a la zaga de la interfaz real es peor que ninguno: cada consumidor que confía en él construye una integración rota, y la falla se manifiesta lejos de la página obsoleta que la causó. Aporte la señal concreta: muestree un puñado de sus interfaces más usadas y compare la referencia publicada contra el contrato real para ver cuánto se ha desviado cada una. Donde encuentre desviación, conecte la referencia a la compilación para que se regenere en cada cambio, y retire la copia mantenida a mano. En entornos empresariales y gubernamentales, donde las interfaces se consumen entre equipos, proveedores y límites contractuales que nunca se ven, una referencia generada y autorizada suele ser lo único que impide que los integradores construyan contra una ficción.

5. **¿Quién es el propietario de cada documento de alto valor y cómo se enterarían hoy si uno se hubiera vuelto obsoleto?** El capítulo trata la documentación obsoleta como un defecto y advierte que los documentos sin propietario envejecen porque actualizarlos es tarea de nadie, mientras que la documentación obsoleta presentada como actual destruye la confianza en toda la colección. A gran escala, el peligro no es una página incorrecta aislada, sino la erosión lenta de la confianza: una vez que los lectores caen en instrucciones desactualizadas, dejan de confiar en el corpus entero y vuelven a interrumpir a la gente. Aporte un mapa de propietarios de sus documentos más críticos y una respuesta honesta a cómo se detecta la obsolescencia, ya sea por cadencia de revisión, por generación, por pruebas contra el sistema o por puro azar. Asigne un propietario con nombre a cada documento que importe, y prefiera la documentación viva, generada o probada, para que la obsolescencia se manifieste de forma mecánica en lugar de a través de un lector avergonzado. En sistemas empresariales y gubernamentales que sobreviven a sus equipos originales, la documentación sin propietario es una carga que un auditor o un proveedor heredero terminará cobrándole.

6. **¿Qué tan descubreble es su documentación y cuánta información crítica sigue viviendo solo en hilos de chat y en la cabeza de las personas?** El capítulo dice que el conocimiento inalcanzable es, en la práctica, inexistente, advierte contra fragmentar la documentación en demasiados wikis y herramientas desconectadas, y urge a capturar el conocimiento tácito en forma duradera y descubreble antes de que se pierda. En una organización grande, el mismo hecho suele redescubrirse, reconsultarse y recontestarse cien veces porque nadie encuentra donde ya estaba escrito, y cada partida se lleva un contexto irremplazable por la puerta. Aporte la evidencia: cuente cuántos hogares de documentación mantienen, intente hallar tres hechos importantes solo por búsqueda y anote dónde las respuestas reales resultaron vivir en la memoria de alguien o en un mensaje enterrado. Conviértase hacia un hogar conocido con búsqueda real y navegación clara, y haga de la captura de conocimiento tácito una rutina del trabajo en lugar de un rescate heroico. En contextos del sector público y fuertemente externalizados, donde los sistemas pasan entre proveedores y equipos por contrato, el conocimiento escrito y descubreble es lo único que sobrevive a la transición.

## Perspectiva sectorial

**Startup.** Con un puñado de ingenieros y sin margen que sobrar, documente solo lo que una caída a las dos de la madrugada o una nueva incorporación realmente necesitaría: un README real por servicio, un manual de operaciones probado para el procedimiento de despliegue y recuperación que todos temen, y unas notas datadas sobre las decisiones que de otro modo olvidarían. Genere la documentación de API a partir del contrato para no tener que mantenerla a mano. Resista la tentación de construir una plataforma de documentación; una carpeta versionada de marcado junto al código es suficiente hasta que sientan un dolor real.

**Pyme.** Sin redactor técnico y con un presupuesto ajustado, apóyese en la documentación que sus herramientas ya generan y en una documentación como código ligera, en lugar de un programa con personal dedicado. Enfrante la decisión como comprar o construir: prefiere plataformas que produzcan su propia referencia actual y una base de conocimiento buscable antes que un wiki que deba cuidar a mano. Gaste su esfuerzo escaso en los dos o tres documentos cuya ausencia paralizaría el negocio, y que una página errónea o faltante sea el disparador para corregir la propiedad.

**Empresa.** En muchos equipos, el problema es la consistencia y la descubrebilidad: una pipeline de documentación como código compartida, una estructura común como Diátaxis, referencias de API y registros de cambios generados, y registros de decisiones aplicados del mismo modo en todas partes, para que el conocimiento no se fragmente en decenas de wikis. Asigne propiedad a cada documento de alto valor y mida la exactitud, no solo la presencia. Trate los registros de arquitectura, manuales de operaciones y registros de decisiones como evidencia de auditoría, y estandarice cómo se producen para que una revisión de controles encuentre una trazabilidad documentada y defendible en lugar de una carrera desordenada.

**Gobierno.** Las reglas de contratación y la rendición de cuentas pública convierten la documentación en un entregable, no en una cortesía. Incluya la documentación de arquitectura, los manuales de operaciones y los registros de decisiones en los contratos como artefactos obligatorios, revisados en cuanto a su exactitud, para que el conocimiento sobreviva a la transición de proveedores y el sistema pueda ser operado por quien lo herede. Exija que cualquier operador autorizado pueda responder a un incidente a partir del manual de operaciones solo, y mantenga los registros de decisiones como un registro público transparente del porqué de cada elección. Una documentación escueta aquí no es una molestia privada; se convierte en una costosa ingeniería inversa financiada por el contribuyente.

## Ejemplos

**Startup.** Una startup de cinco personas escribe un README real para cada servicio y un manual de operaciones breve para el único procedimiento de despliegue y recuperación que todos temen, para que una caída a las dos de la madrugada no dependa de desvelar al único fundador que conoce el sistema. Generan la documentación de API a partir del contrato en lugar de escribirla a mano, y apuntan unas notas datadas que explican por qué eligieron su base de datos y su enfoque de autenticación. Se mantiene ligero, pero significa que la sexta y séptima incorporación se incorporan a partir de documentos, no interrumpiendo a todos.

**Empresa.** Una gran compañía de software mantiene toda su documentación en los mismos repositorios que su código, escrita en marcado y revisada en solicitudes de fusión junto a los cambios que describe. Las referencias de API se generan a partir de los contratos de servicio, de modo que nunca se desvían. Los registros de cambios se generan a partir de compromisos estructurados, y los registros de decisiones de arquitectura preservan la justificación de las grandes opciones. Un sitio de documentación se compila automáticamente en cada fusión. Los nuevos ingenieros alcanzan la productividad con rapidez porque las guías de incorporación y los manuales de operaciones están al día y son descubrebles, y los ingenieros de guardia se apoyan en los manuales en lugar de desvelar a los autores originales.

**Gobierno.** Una agencia nacional hereda un sistema de un contratista saliente, dependiendo por completo de la documentación para transportar el conocimiento a través del límite contractual. Porque el proveedor anterior mantuvo la documentación de arquitectura, los manuales de operaciones y los registros de decisiones como entregables obligatorios, el equipo nuevo puede operar y modificar el sistema sin los autores originales. Donde la documentación era escueta, la agencia se enfrenta a una costosa ingeniería inversa. Esa experiencia impulsa una nueva política: la documentación es un entregable contractual, revisado en cuanto a su exactitud y no tratado como un asunto posterior, y los manuales de operaciones deben permitir que cualquier operador autorizado responda a los incidentes.

## Caso de negocio: motivaciones, retorno de inversión y costo total de propiedad

La documentación le devuelve en menor tiempo de incorporación, menos riesgo de dependencia de personas clave, respuesta a incidentes más rápida y menor costo de cambio a lo largo de la vida del sistema. Ingenieros nuevos que alcanzan la productividad en días en lugar de semanas, personal de guardia que resuelve incidentes a partir de un manual en lugar de escalar, mantenedores que modifican un sistema con confianza años después de su construcción: son grandes ahorros recurrentes que se acumulan a lo largo de una gran organización y un ciclo de vida largo del sistema.

¿Qué cuesta la documentación? El esfuerzo de autoría y mantenimiento. ¿Qué cuesta *no* documentar? Se paga continuamente: en incorporaciones lentas, preguntas repetidas, cuellos de botella por dependencia de personas clave, recuperación de incidentes más lenta y, en el extremo, sistemas que nadie puede modificar con seguridad, lo que obliga a reescrituras o ingeniería inversa costosas. En escenarios de transición de proveedores y auditoría, la falta de documentación puede acarrear costos contractuales y de cumplimiento directos. Para hacer el caso ante la dirección, ponga números en el tiempo de incorporación, el tiempo de respuesta a incidentes y cuánta información crítica vive en cabezas individuales. Luego, presente la documentación como código y la generación como formas de obtener documentación durable sin una carga de mantenimiento equivalente. Y enfatice que la documentación inexacta es un pasivo, de modo que la inversión debe incluir mantenerla actualizada.

## Antipatrones y trampas

- **Documentación obsoleta presentada como actual:** engaña a los lectores y destruye la confianza en toda la documentación.
- **El wiki de un solo uso:** páginas creadas y nunca actualizadas, que se desvían de la realidad en silencio.
- **Fragmentación de la documentación:** conocimiento repartido en muchas herramientas y wikis de modo que nada se encuentra.
- **Mezcla de tipos de documentación:** tutoriales, referencia y explicación amontonados en una página, que no sirven bien a nadie.
- **Mantenimiento manual de contenido generable:** documentación de API escrita a mano que inevitablemente diverge de la interfaz real.
- **Conocimiento tribal:** comprensión crítica guardada solo en las cabezas de las personas y en el historial de chat, perdida cuando se van.
- **La documentación como asunto posterior:** escrita al final, si es que se escribe, en lugar de junto al cambio.
- **Ausencia de propiedad:** documentos sin propietario responsable que envejecen porque actualizarlos es tarea de nadie.

## Modelo de madurez

- **Nivel 1, Iniciar.** La documentación es escasa, dispersa y obsoleta, y el conocimiento vive en las cabezas de las personas. Lo que existe se escribió una vez y nunca se tocó de nuevo, de modo que una caída o una partida obliga a hacer ingeniería inversa del sistema.
- **Nivel 2, Desarrollar.** Los documentos clave existen (README, algunos manuales de operaciones) , pero se mantienen de forma inconsistente y son difíciles de encontrar. Algunos equipos documentan bien y otros apenas, y no hay una expectativa compartida sobre qué debe llevar un repositorio ni dónde debe estar.
- **Nivel 3, Estandarizar.** La documentación como código es la norma en toda la organización: una estructura común como Diátaxis, referencias de API y registros de cambios generados, registros de decisiones y la expectativa en la revisión de que la documentación cambia junto al código que describe. Cada documento de alto valor tiene un propietario con nombre, y hay un hogar conocido con búsqueda real.
- **Nivel 4, Gestionar.** La documentación se mide, no solo se presencia. Se rastrean la cobertura de los documentos esenciales, la tasa de cambio documental frente a la tasa de cambio de código, el tiempo de incorporación, la resolución de incidentes a partir de manuales solos y la frescura frente a un umbral de obsolescencia definido, y se revisan esas métricas contra líneas base. La obsolescencia se detecta de forma mecánica mediante generación, pruebas contra el sistema y comprobaciones de enlaces y exactitud, y las páginas obsoletas se señalan o prueban con evidencia, no por azar.
- **Nivel 5, Orquestar.** La documentación se mejora de forma continua e integrada en toda la organización: viva, en su mayor parte generada o probada contra el sistema, con propietario, descubreble y adaptable. Las métricas alimentan la decisión de dónde invertir, el conocimiento tácito se captura como parte rutinaria del trabajo, y el corpus se reequilibra y poda activamente a medida que cambian los sistemas, los equipos y los lectores.

## Ideas para el debate

- ¿Qué documentación, si desapareciera mañana, lastimaría más a su organización, y existe actualmente y se mantiene actualizada?
- ¿Cómo hace de la actualización de documentación una parte natural de cambiar el código, en lugar de una tarea aparte?
- ¿Dónde puede reemplazar documentación escrita a mano por documentación generada vinculada a la fuente de verdad?
- ¿Cómo mide si su documentación es exacta y se usa, y no solo está presente?
- ¿Cómo deben cambiar los asistentes de IA la forma en que escribe, mantiene y busca documentación, y dónde podrían introducir contenido plausible pero incorrecto?
- ¿Cómo captura el conocimiento tácito antes de que se vayan las personas que lo poseen?

## Ideas clave

- Trate la documentación como código: versionada, revisada, próxima a la fuente y publicada automáticamente.
- Estructure el contenido por necesidad del lector: tutoriales, guías de uso, referencia y explicación.
- Mantenga los esenciales de alto valor: README, manuales de operaciones, documentación de arquitectura, guías de incorporación y registros de decisiones.
- Genere la documentación de API y los registros de cambios para que no puedan desviarse de la fuente de verdad.
- Luche contra la obsolescencia con propiedad, expectativas de revisión y poda; la documentación inexacta es peor que ninguna.

## Referencias y lecturas adicionales

- Daniele Procida, *Diátaxis* (marco de documentación)
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* y guía Season of Docs (como ejemplos de referencia)
- Michael Nygard, *Documenting Architecture Decisions* (registros de decisiones de arquitectura)
- Andrew Hunt y David Thomas, *The Pragmatic Programmer* (sobre conocimiento y documentación)
- *Keep a Changelog* (como convención de referencia)

