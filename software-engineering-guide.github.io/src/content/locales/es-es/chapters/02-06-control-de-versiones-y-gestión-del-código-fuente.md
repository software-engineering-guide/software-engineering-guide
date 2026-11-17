# 2.6 Control de versiones y gestión del código fuente

## Presentación y motivación

Pensemos en el [control de versiones](https://en.wikipedia.org/wiki/Version_control) como el sistema de registro oficial de la base de código. Captura cada cambio, indica quién lo hizo, cuándo y por qué, y permite que muchas personas trabajen sobre el mismo software sin pisarse los unos a los otros. En una organización de gran envergadura, va mucho más allá de una copia de seguridad: es el cimiento sobre el que se sostienen la colaboración, la [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), la auditoría y la gestión de lanzamientos. Las decisiones que se tomen sobre la ramificación, la estructura del repositorio y la disciplina de los *commits* determinan la velocidad a la que el equipo puede moverse y el grado de seguridad con el que lo hace.

Para equipos numerosos, la gestión del código fuente es, en esencia, un problema de coordinación a escala. Cuando cientos de ingenieros publican cambios en un código compartido, necesitan una estrategia que mantenga las fusiones pequeñas, la rama principal siempre lista para un lanzamiento y el historial legible. Un equipo que integra de forma continua avanza con fluidez; un equipo que deja que las ramas diverjan durante semanas se tambalea de una crisis de integración a otra. La estructura del repositorio, un solo gran repositorio o muchos, también condiciona cómo los equipos comparten código y se coordinan.

Los entornos corporativos y gubernamentales suman exigencias adicionales: trazabilidad, control de acceso y retención. Un cambio puede necesitar enlazarse con un elemento de trabajo aprobado a efectos de auditoría. Los secretos deben mantenerse siempre fuera del historial. El acceso a los repositorios ha de respetar las fronteras de seguridad. En estos contextos, las prácticas de control de versiones pasan a formar parte del marco de control de la organización, y un despiste, como un secreto filtrado o un historial inauditable, puede tener consecuencias graves.

## Principios clave

- Integrar cambios pequeños con frecuencia; la divergencia prolongada es la raíz de todo dolor asociado a las fusiones.
- Mantener la rama principal siempre lista para su lanzamiento.
- El historial es documentación: escribimos los *commits* pensando en quien, en el futuro, deba comprender el porqué de cada cambio.
- Jamás *commitear* secretos; cualquier secreto que llegue al historial debe considerarse comprometido.
- Automatizar la aplicación de las normas de higiene (ganchos, controles de CI) en lugar de depender únicamente de la disciplina individual.
- Elegir la estructura del repositorio (*monorepo* frente a *polirepo*) en función de cómo los equipos comparten código realmente y se coordinan, no de modas ni tendencias.
- Vincular cada cambio a su justificación (elementos de trabajo, tickets o decisiones) para garantizar la trazabilidad.

## Recomendaciones

### Prefirir el desarrollo centrado en el tronco con ramas de vida breve

Apóyese en el [desarrollo centrado en el tronco](https://en.wikipedia.org/wiki/Trunk-based_development): integrar con frecuencia a una rama principal compartida, usando ramas de funcionalidad de vida corta, medidas en horas o días, no en semanas. Las ramas breves mantienen las fusiones pequeñas y la integración continua, un hábito fuertemente asociado a un alto rendimiento de entrega. Cuando un trabajo no está terminado, no lo aparque en una rama de vida larga. Use *feature flags* (conmutadores de funcionalidad), interruptores en tiempo de ejecución que ocultan el trabajo incompleto, para poder fusionarlo con seguridad. Reserve las ramas de lanzamiento de vida larga para el soporte genuino de múltiples versiones y acepte, desde el momento en que las cree, el coste de mantenimiento que conllevan.

### Elegir un modelo de ramificación que se ajuste al ritmo de lanzamientos

Adecúe su [modelo de ramificación](https://en.wikipedia.org/wiki/Branching_(version_control)) a cómo lanza en realidad. Si despliega de forma continua, el desarrollo centrado en el tronco con una ramificación mínima le servirá perfectamente. Si entrega versiones concretas a sus clientes o debe soportar varias versiones en producción simultáneamente, puede necesitar ramas de lanzamiento y aplicación retroactiva (*backport*). Evite los modelos pesados con múltiples ramas de vida larga a menos que su modelo de lanzamiento lo exija realmente, pues multiplican el sobrecostes de fusión y mantenimiento.

### Decidir entre *monorepo* y *polirepo* con deliberación

Recurre al [monorepo](https://en.wikipedia.org/wiki/Monorepo), un único repositorio que alberga muchos proyectos, cuando los equipos comparten código intensamente, necesitan cambios atómicos que cruzan proyectos y desean una herramienta unificada y una visibilidad global. A cambio, acepta la necesidad de herramientas de compilación a gran escala y controles de acceso más finos. Recurre al *polirepo*, repositorios separados por proyecto o servicio, cuando los equipos y servicios son genuinamente independientes, desean ciclos de acceso y lanzamiento aislados y no necesitan cambios atómicos entre repositorios. A cambio, acepta el coste de coordinar los cambios que abarcan varios repositorios. Ambos funcionan a escala. Lo que genera fricción constante es la elección equivocada para su patrón de acoplamiento.

### Exigir la higiene de los *commits* y adoptar el formato convencional

Pida que los mensajes de *commit* expliquen por qué se hizo un cambio, no solo qué se hizo. Adapte una convención como *conventional commits* para que los mensajes sean estructurados y procesables por máquina, lo que permite automatizar los changelogs y la numeración de versiones. Mantenga los *commits* atómicos, un cambio lógico por cada uno, para que el historial siga siendo biseccionable y fácil de revertir. Deje que los ganchos y los controles de CI impongan el formato del mensaje y la higiene básica, en lugar de fiarse de la memoria.

### Mantener los binarios grandes y el código generado fuera del historial ordinario

No *commitee* activos binarios de gran tamaño directamente en el historial principal, porque inflan cada clonado para siempre. Use un mecanismo de almacenamiento de archivos grandes o un repositorio de artefactos en su lugar. Como regla general, evite también *commitear* código generado; genérelo en la compilación. Cuando en algún caso concreto deba *commitear* un artefacto generado, aíslelo y márquelo con claridad para que no contamine las revisiones ni las diferencias.

### Impedir que los secretos entren nunca en el repositorio

Instale un escaneo automático de secretos en los ganchos de pre-*commit* y en la CI para que las credenciales se bloqueen antes de llegar al repositorio. Proporcione a los ingenieros un sistema adecuado de gestión de secretos, de modo que nunca necesiten codificar en duras una credencial. Y trate cualquier secreto que haya llegado al historial como comprometido: rótele de inmediato. Una vez que un secreto se ha publicado y se ha clonado, eliminarlo del historial es difícil e impreciso.

### Establecer control de acceso y trazabilidad

Configure el acceso a los repositorios de modo que respete las fronteras de seguridad y el [principio de mínimo privilegio](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Vincule los *commits* o las peticiones de fusión a elementos de trabajo, para que cada cambio pueda rastrearse hasta su justificación, lo que ayuda tanto al contexto del trabajo diario como a la auditoría. Proteja las ramas clave con comprobaciones y revisiones obligatorias, de modo que nada se fusione sin pasar los controles acordados.

## Compromisos: ventajas y desventajas

| Decisión | Ventajas | Desventajas |
|---|---|---|
| Desarrollo centrado en el tronco | Integración continua; fusiones pequeñas; alto flujo | Exige *feature flags* y disciplina; menor aislamiento |
| Ramas de funcionalidad de vida larga | Aislamiento sólido del trabajo en curso | Fusiones dolorosas; integración tardía; desviación |
| *Monorepo* | Cambios atómicos entre proyectos; herramientas compartidas; visibilidad | Necesita herramientas de compilación a escala; control de acceso grueso por defecto |
| *Polirepo* | Lanzamientos independientes; acceso aislado; herramientas simples por repositorio | Cambios entre repositorios difíciles; sobrecarga de coordinación de versiones |
| *Commits* convencionales | Changelogs y versionamiento automatizados; historial coherente | Convención inicial; requiere aplicación |

El gran compromiso entre estos enfoques es la frecuencia de integración frente al aislamiento. Las ramas de vida larga dan una sensación de seguridad porque el trabajo está apartado, pero es precisamente ese aislamiento el que provoca las fusiones costosas y las sorpresas de integración posteriores. El desarrollo centrado en el tronco renuncia a esa sensación de aislamiento a cambio de una integración continua y económica, y a cambio pide que se aporten *feature flags* y disciplina. La decisión entre *monorepo* y *polirepo* intercambia la facilidad entre proyectos por la independencia de los equipos. Elija la que se ajuste a cuán estrechamente acoplado está su código en realidad.

## Preguntas para discutir con el equipo

1. **¿Qué controles deben superarse antes de que nada se fusione en la rama principal protegida, y es esa rama principal realmente siempre lista para su lanzamiento?** Este capítulo trata la rama principal siempre lanzable como un principio fundamental y considera un antipatrón una rama principal sin protección, en la que código roto o no revisado llega a la rama de la que todos dependen. En un equipo grande, una rama principal en rojo bloquea a todos a la vez, de modo que la puerta que se exige es una propiedad de seguridad compartida, no una decisión individual. Traiga la evidencia: qué es lo que su protección de ramas impone de hecho hoy y con qué frecuencia la rama principal está actualmente rota. Defina el conjunto requerido (pruebas superadas, escaneos de seguridad y revisión) y haga que la rama principal sea lanzable por política, no por esperanza. Esa puerta es lo que permite que muchas personas integren de forma continua sin temor.

2. **¿Vale la pena para su equipo la adopción de los *commits* convencionales, a pesar de la sobrecarga de convención, dado lo que automatizan?** El capítulo recomienda mensajes de *commit* estructurados y procesables por máquina precisamente porque permiten automatizar los changelogs y la numeración de versiones, y pide *commits* atómicos para que el historial siga siendo biseccionable y revertible. El compromiso es real: se paga una convención inicial y se necesita aplicación, a cambio de notas de lanzamiento generadas y un historial fiable. Traiga el indicador de lo que se hace manualmente hoy: escribir changelogs a mano o buscar qué *commit* introdujo una regresión. Si se lanza con frecuencia o se mantienen varias versiones, la automatización suele amortizar el coste; si rara vez se hace un lanzamiento, una convención más ligera puede ser suficiente. Dejen que los ganchos y la CI impongan el formato para que no dependa de la memoria.

3. **¿Se ha aceptado el coste operativo que su estructura de repositorios demanda, ya sea herramientas para *monorepo* o coordinación entre repositorios?** Este capítulo sostiene que tanto el *monorepo* como el *polirepo* funcionan a escala, y que la elección incorrecta para el patrón de acoplamiento es lo que genera fricción constante. Un *monorepo* exige herramientas de compilación a escala y un control de acceso más granular, mientras que los *polirepos* convierten cualquier cambio que abarque varios repositorios en un proyecto de coordinación con riesgo de desalineación de versiones. Traiga la señal concreta: con qué frecuencia los cambios cruzan fronteras de proyecto y si las herramientas de compilación y acceso pueden sostener la estructura que ya se tiene. Si los cambios atómicos entre proyectos son habituales, invierta en herramientas de *monorepo*; si los equipos y servicios son genuinamente independientes, acepte el coste de coordinación entre repositorios con plena conciencia. La idea es alinear la estructura con el acoplamiento real del código y financiar las herramientas que esa estructura requiere.

4. **¿Si una credencial activa se *commiteara* ahora mismo en un repositorio con mucho tráfico, con qué rapidez se detectaría, y la rotación es realmente automática o es solo una esperanza?** El capítulo trata cualquier secreto que llega al historial como comprometido y advierte que eliminarlo después es difícil e impreciso, por lo que la prevención y la rotación rápida son las únicas defensas reales. Para un equipo grande, la exposición se multiplica: un secreto publicado en un repositorio compartido se clona en decenas de máquinas y se refleja en los cachés de CI en cuestión de minutos, de modo que una respuesta humana lenta garantiza una brecha. El aspecto que se contrapone es la fricción: un escaneo agresivo de secretos en pre-*commit* y una rotación obligatoria ralentizan al equipo y generan falsos positivos, por lo que hay que calibrar los controles en lugar de desactivarlos. Traiga la evidencia: si el escaneo de secretos se ejecuta tanto en los ganchos de pre-*commit* como en la CI, el tiempo medio para detectar y rotar una fuga conocida, y si los ingenieros disponen siquiera de un sistema de gestión de secretos que elimine la tentación de codificar en duras. En entornos corporativos y gubernamentales, vincule esto al proceso de incidentes y a las normas de retención, porque una credencial filtrada en un historial auditable es a la vez un evento de seguridad y uno de cumplimiento, y el regulador preguntará quién lo supo y con qué rapidez actuó.

5. **¿Las ramas son realmente de vida breve, y donde no lo son, por qué el trabajo incompleto se aparca en una rama en lugar de ocultarse detrás de un *feature flag*?** El capítulo se inclina decididamente hacia el desarrollo centrado en el tronco porque la divergencia prolongada es la raíz del dolor asociado a las fusiones, y ofrece los *feature flags* como el mecanismo que permite fusionar trabajo incompleto con seguridad en lugar de aislarlo durante semanas. En un equipo grande, esto es una propiedad de coordinación, no una preferencia personal: cada rama que vive durante semanas se convierte en un *fork* privado de la realidad que alguien debe reconciliar eventualmente, y el coste de esa reconciliación crece con el número de personas. El aspecto que se contrapone es que los *feature flags* tienen su propio coste: complejidad en tiempo de ejecución, combinaciones de pruebas y *flags* obsoletos que deben retirarse. Traiga los datos: la distribución real de la vida de las ramas, con qué frecuencia la integración produce conflictos o sorpresas y cuántas ramas de vida larga existen ahora mismo y por qué. Para una organización grande o regulada, añada el panorama de lanzamientos, ya que el soporte genuino de múltiples versiones puede justificar ramas de lanzamiento de vida larga con un *backport* disciplinado, y eso es una decisión distinta de apartar el trabajo diario de funcionalidad de la rama principal.

6. **¿Cada cambio del historial puede rastrearse hasta su autor y su justificación dentro de los límites de seguridad adecuados, y resistiría una auditoría?** Este capítulo trata el control de acceso, el mínimo privilegio y el vínculo de los cambios a los elementos de trabajo como parte del marco de control de la organización, no como un adorno opcional. Para un equipo grande, la trazabilidad es lo que convierte un flujo opaco de *commits* en algo que se puede razonar durante un incidente o una revisión de cumplimiento, y los límites de acceso son lo que impide que una cuenta comprometida alcance código al que nunca debería llegar. El aspecto que se contrapone es la velocidad del desarrollador: el vínculo obligatorio a elementos de trabajo, los permisos finos y las revisiones requeridas añaden ceremonias que un equipo pequeño y ágil podría razonablemente omitir. Traiga la evidencia: si las ramas protegidas exigen las comprobaciones y revisiones que se declaran, si los *commits* hacen referencia efectivamente a elementos de trabajo aprobados y cómo se mapea el acceso a las fronteras de seguridad reales de hoy. En contextos corporativos y gubernamentales, conecte esto con la clasificación, la retención y las obligaciones de auditoría, porque un historial inauditable o un permiso de acceso demasiado amplio se convierte en una observación que puede detener un programa o hacer fracasar una acreditación.

## Perspectiva por sector

**Startup.** La velocidad y la supervivencia lo son todo. Use un solo repositorio, trabaje centrado en el tronco, fusione ramas de vida corta varias veces al día y oculte el trabajo inacabado detrás de *feature flags* simples en lugar de ramas largas. Active el escaneo de secretos desde el primer *commit*, porque una clave filtrada en un repositorio público puede hundir a una empresa que no tiene un equipo de seguridad para contener el desastre. Olvídese de modelos de ramificación elaborados y procesos pesados; una rama principal protegida y mensajes de *commit* con sentido son la disciplina suficiente para avanzar rápido.

**Pequeña empresa.** Sin especialista de plataforma ni DevOps dedicado y con un presupuesto ajustado, compre los valores predeterminados gestionados en lugar de construirlos. Un proveedor de Git gestionado ofrece protección de ramas, revisiones obligatorias y escaneo de secretos desde el inicio, así que apóyese en esas funciones en lugar de autoalojar un servidor que no puede mantener. Enmarque la decisión como higiene de datos: sepa qué repositorios contienen configuración sensible, guarde las credenciales en el gestor de secretos del proveedor y deje que la plataforma imponga las pocas reglas que de verdad se necesitan.

**Gran empresa.** El problema difícil es la coherencia entre muchos equipos. Estandarice la protección de ramas, las convenciones de *commit* y el escaneo de secretos como política a nivel de organización, para que los equipos dejen de reinventarlos, y tome la decisión entre *monorepo* y *polirepo* deliberadamente según el patrón de acoplamiento, financiando las herramientas de compilación a escala o la coordinación entre repositorios que eso demanda. Encamine los cambios a los revisores adecuados con reglas de propiedad del código, vincule los *commits* a elementos de trabajo para la trazabilidad, y trate la higiene del control de versiones como un control gobernado, con responsables y métricas, no como una cuestión de hábito individual.

**Sector público y administración.** Las reglas de contratación pública, la transparencia y la rendición de cuentas pública configuran todo el conjunto. Exija que cada *commit* haga referencia a un elemento de trabajo aprobado, controle el acceso por frontera de clasificación y haga obligatorios el escaneo de secretos y la rotación inmediata bajo un proceso de incidentes documentado. Soporte múltiples versiones en despliegue con ramas de lanzamiento de vida larga y un *backport* disciplinado donde los sitios no puedan actualizarse todos a la vez, y mantenga el historial auditable y retenido para que las solicitudes de acreditación, acceso a la información y supervisión puedan responderse sin apuros.

## Ejemplos

**Startup.** Una startup de tres personas trabaja centrada en el tronco por hábito y por necesidad, fusionando ramas de vida corta en *main* varias veces al día y ocultando funciones a medio terminar detrás de *flags* simples. Activan el escaneo de secretos en la CI desde el primer *commit*, porque una clave de API filtrada en un repositorio público podría hundir a una empresa sin equipo de seguridad para contener la situación. Un solo repositorio, una rama *main* protegida y mensajes de *commit* con sentido les dan la disciplina suficiente para avanzar rápido sin tropezar con su propio historial.

**Gran empresa.** Una gran empresa tecnológica gestiona un *monorepo* con cientos de servicios y librerías compartidas. Las herramientas de compilación a escala y las reglas de propiedad del código encaminan cada cambio a los revisores correspondientes. Un único *commit* puede actualizar de forma atómica una librería compartida y todos sus consumidores a la vez, eludiendo los problemas de desalineación de versiones que azotan a los repositorios distribuidos. El desarrollo centrado en el tronco con *feature flags* mantiene la rama principal lista para su lanzamiento, y el escaneo de secretos bloquea las credenciales en el momento del *commit* en todo el repositorio.

**Sector público y administración.** Un contratista nacional de defensa se mantiene firme en la trazabilidad estricta. Cada *commit* debe hacer referencia a un elemento de trabajo aprobado. La protección de ramas exige que se superen los escaneos de seguridad y una revisión independiente, y el acceso está estrechamente controlado por frontera de clasificación. El escaneo de secretos es obligatorio y cualquier credencial expuesta dispara la rotación inmediata bajo un proceso de incidentes. Las ramas de lanzamiento de vida larga soportan múltiples versiones en despliegue en sitios que no pueden actualizarse todos a la vez, con un *backport* disciplinado de las correcciones de seguridad.

## Justificación económica: motivaciones, retorno de inversión y coste total de propiedad

Una buena gestión del código fuente cuesta casi nada adoptarla y mucho no tenerla. El desarrollo centrado en el tronco y la integración continua son de las prácticas más fuertemente asociadas a un alto rendimiento en la entrega de software, que a su vez se correlaciona con mejores resultados organizacionales. Un historial limpio y trazable reduce el tiempo que se tarda en diagnosticar incidentes y cumplir auditorías, y una ramificación disciplinada ahorra el coste recurrente y no presupuestado de las crisis de integración y las maratones de fusión.

El riesgo más desproporcionado es la presencia de secretos en el control de versiones. Una sola credencial filtrada puede causar una brecha cuyo coste anula cualquier inversión en herramientas, y el historial hace que esas fugas perduren. Prevenirlas es barato; limpiar después no. Las decisiones erróneas de estructura se manifiestan como fricción crónica: cada cambio entre repositorios se convierte en un proyecto de coordinación, o cada compilación del *monorepo* se vuelve un cuello de botella. Para presentar el caso a la dirección, vincule la estrategia de ramificación a las métricas de entrega y al tiempo de diagnóstico de incidentes, y presente el escaneo de secretos y el control de acceso como controles de bajo coste frente a un riesgo de brecha y auditoría de alto coste.

## Antipatrónes y trampas

- **Ramas divergentes de vida larga:** semanas de trabajo aislado que desembocan en eventos de fusión dolorosos y arriesgados.
- **Secretos en el historial:** credenciales codificadas en duras que persisten en cada clonado para siempre y requieren rotación una vez expuestas.
- **Binarios grandes *commiteados* en el historial principal:** inflan cada clonado de forma permanente y ralentizan todas las operaciones.
- **Mensajes de *commit* vacíos:** «*fix*», «*wip*», «*changes*» que destruyen el valor del historial como documentación.
- **Commitear código generado como si estuviera escrito a mano:** diferencias ruidosas, conflictos de fusión y confusión sobre la fuente de verdad.
- **Estructura de repositorio equivocada para el acoplamiento:** *polirepos* para código fuertemente acoplado o *monorepos* sin herramientas a escala.
- **Rama principal sin protección:** sin comprobaciones obligatorias, de modo que código roto o no revisado llega a la rama de la que todos dependen.

## Modelo de madurez

- **Nivel 1, Iniciar:** Ad hoc y reactivo. La ramificación es improvisada, las ramas viven durante semanas, los mensajes de *commit* dicen «*fix*» o «*wip*», no hay escaneo de secretos y la integración va de una crisis de fusión a otra.
- **Nivel 2, Desarrollar:** Aparecen prácticas básicas pero varían entre equipos. Existe en algunos sitios un modelo de ramificación y convenciones de mensaje, pero las ramas siguen viviendo demasiado tiempo, la aplicación es parcial, el escaneo de secretos es irregular y la estructura de repositorios se heredó en lugar de elegirse.
- **Nivel 3, Estandarizar:** Las prácticas están documentadas y se aplican a nivel de organización: desarrollo centrado en el tronco con ramas breves, una rama principal protegida y siempre lanzable, convenciones de *commit* impuestas, escaneo de secretos tanto en ganchos como en CI, acceso con mínimo privilegio y una elección deliberada entre *monorepo* o *polirepo*.
- **Nivel 4, Gestionar:** Las prácticas de código fuente se miden y controlan con datos. Se registra la vida de las ramas, la frecuencia de integración, la tasa de rotura de la rama principal, el tiempo medio para detectar y rotar un secreto filtrado y la trazabilidad de cambios a elementos de trabajo, todo comparado con baselines acordados, y se actúa cuando los números se desvían, en lugar de esperar al siguiente incidente.
- **Nivel 5, Orquestar:** Las prácticas se mejoran continuamente y se integran a lo largo de toda la organización. La ramificación, la estructura de repositorios y las herramientas se adaptan a medida que los equipos y el acoplamiento del código cambian, la automatización impone la higiene de extremo a extremo, y los datos del control de versiones alimentan las decisiones de entrega, seguridad y riesgo a escala organizacional.

## Ideas para la discusión

- ¿La vida de las ramas del equipo es realmente breve, y si no lo es, qué impide la integración continua?
- ¿La elección entre *monorepo* o *polirepo* se ajusta al acoplamiento real del código?
- ¿Cómo se manejan hoy los binarios grandes y los artefactos generados, y qué coste supone?
- ¿Qué pasaría si una credencial activa se *commiteara* ahora mismo, y con qué rapidez se detectaría y rotaría?
- ¿Cuánta disciplina en los mensajes de *commit* y en la trazabilidad vale la pena imponer en su contexto?
- ¿Cómo cambian los *feature flags* la estrategia de ramificación, y qué nuevos riesgos introducen?

## Puntos clave

- Integre con frecuencia y con ramas de vida corta; la divergencia prolongada provoca el dolor que parece evitar.
- Mantenga la rama principal siempre lista para su lanzamiento y protegida por comprobaciones obligatorias.
- Jamás permita que los secretos entren en el historial; escanee automáticamente y rote de inmediato si llegan.
- Elija entre *monorepo* y *polirepo* según el acoplamiento real y las necesidades de coordinación.
- Trate el historial de *commits* como documentación, con *commits* significativos, convencionales y atómicos.

## Referencias y lecturas complementarias

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble y David Farley, *Continuous Delivery*
- Scott Chacon y Ben Straub, *Pro Git*
- Paul Hammant y otros, escritos sobre el desarrollo centrado en el tronco
- Especificación *Conventional Commits* (como referencia estándar)
- Martin Fowler, artículos sobre patrones de ramificación e integración continua

