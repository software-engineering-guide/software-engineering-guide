# 1.6 Registros de decisiones

## Visión general y motivación

Un **registro de decisión** es un documento que capta una decisión importante junto con su contexto y sus consecuencias. Su forma más conocida es el **[registro de decisión arquitectónica](https://en.wikipedia.org/wiki/Architectural_decision) (RDA)**: una nota breve, inmutable por preferencia, que registra una elección arquitectónicamente significativa, las razones de su adopción y lo que se deriva de ella. El conjunto completo de registros de un proyecto constituye su **bitácora de decisiones (BDA)**, y la disciplina de mantenerla forma parte de la **gestión del conocimiento arquitectónico (GKA)**. Este capítulo se apoya en las prácticas de toma de decisiones y gobernanza del capítulo 1.5 y se centra en cómo redactar, almacenar y sostener registros de decisiones a escala.

La motivación es sencilla y dolorosa si se aprende a expensas de un error. En cualquier sistema de vida larga, la pregunta más costosa es «¿por qué demonios se construyó de esta manera?», formulada meses o años después por personas que no estuvieron en la reunión. El código muestra *qué* hace el sistema. Las pruebas demuestran que *funciona*. Pero ninguno de los dos captura *por qué* se eligió este camino en lugar de las alternativas que se barajaron y descartaron. Sin registros de decisiones, ese razonamiento se evapora con la rotación de personal. Los equipos reviven debates ya resueltos, revierten buenas decisiones por razones infundadas o mantienen malas decisiones por miedo. Un registro de decisiones es una carta económica al futuro que preserva el razonamiento.

En equipos grandes, esta práctica es tanto una herramienta de coordinación como una ayuda de memoria. Las empresas ejecutan decenas de equipos que toman decisiones solapadas. Una bitácora compartida convierte el razonamiento costoso de un equipo en un activo reutilizable y evita decisiones divergentes e incompatibles. En ámbitos regulados y del sector público, los registros de decisiones son casi obligatorios. Los auditores, los organismos de supervisión y los contratistas sucesores necesitan una justificación rastreable que conecte los requisitos arquitectónicamente significativos con las decisiones tomadas al respecto. Una bitácora bien mantenida suele marcar la diferencia entre un sistema que puede certificarse y auditar y otro que no.

## Principios clave

- **Registrar el *por qué*, no solo el *qué*.** El contexto y las alternativas descartadas son el punto.
- **Una decisión por registro.** Cada registro debe ser específico y autosuficiente.
- **Lo pequeño y ligero vence a lo exhaustivo y no usado.** Un registro de una página que existe supera a un informe que nunca se redacta.
- **Fecha todo.** Los costes, las restricciones y los proveedores cambian; ponga fecha a cada afirmación.
- **Preferir una bitácora viva, de forma pragmática.** La inmutabilidad es el ideal; en la práctica, se añaden modificaciones con notas datadas.
- **Palabras en lugar de abreviaturas.** «Decisiones» invita a más participación que «RDAs».
- **Hacer que las decisiones sean localizables y, en lo posible, verificables.** Presentar el registro adecuado en el momento adecuado; respaldarlo con funciones de aptitud.

## Recomendaciones

### Capturar la estructura esencial

Un buen registro de decisiones incluye unas pocas secciones esenciales. Adapte una plantilla conocida en lugar de inventar una propia:

- **Título:** una frase breve en imperativo de presente («Utilizar [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) para el libro mayor»).
- **Estado:** propuesto, aceptado, suplantado, en desuso.
- **Contexto:** la situación, las fuerzas, las prioridades de negocio y las restricciones que hacen necesaria la decisión; incluye el requisito arquitectónicamente significativo que aborda.
- **Decisión:** la elección adoptada, expuesta con claridad.
- **Consecuencias:** qué se facilita y qué se complica, decisiones secundarias que se desencadenan y riesgos aceptados.

Entre las plantillas más populares se encuentran la de Michael Nygard (sencilla y muy adoptada), la de Tyree y Akerman (más elaborada, con alternativas ponderadas), MADR (Markdown Any Decision Records, orientada a las opciones y sus pros y contras), y las afirmaciones tipo Y (una forma estructurada en una sola frase). Establezca una plantilla por organización para que los registros sean comparables. Consulte el capítulo 12.3 para una plantilla lista para copiar y pegar.

### Redactar registros específicos, datados e inmutables en la práctica

Cada registro debe tratar exactamente una decisión. Asigne fecha a las afirmaciones individuales, sobre todo a las que fluctúan: precios, cifras de escalado, capacidades de proveedores, condiciones de licencia. En teoría, un registro debe ser inmutable. Cuando una decisión cambia, se redacta un *nuevo* registro que suplanta al anterior, conservando la historia. En la práctica, muchos equipos encuentran que el enfoque de **documento vivo** funciona mejor: se inserta nueva información en el registro existente con una fecha y una nota que indica que llegó después de la decisión. Ambas approaches son legítimas. El estilo inmutable es más sólido para las trazas de auditoría; el estilo vivo es mejor para el conocimiento cotidiano del equipo. Elija con deliberación y sea coherente.

### Almacenar los registros donde se hace el trabajo

Coloque los registros de decisiones en el [control de versiones](https://en.wikipedia.org/wiki/Version_control) junto al código: un directorio `decisions/` (o `adr/`) con archivos en [Markdown](https://en.wikipedia.org/wiki/Markdown), uno por decisión, nombrados con una frase en imperativo, en minúsculas y con guiones (`choose-database.md`, `format-timestamps.md`). Así se obtiene histórico, revisión y comparación de diferencias de forma gratuita, y se mantiene la justificación al lado de lo que explica. Si el equipo prefiere [wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs o un sistema de seguimiento tipo Jira, úselos. La herramienta importa mucho menos que el hábito. Una herramienta de línea de comandos ligera (como `adr-tools`) puede generar plantillas e indexar los registros.

### Llamarlos «decisiones» y ampliar más allá de la arquitectura

Una observación práctica de muchos equipos: la etiqueta importa. Algunos desarrolladores y gerentes se resisten a la palabra «arquitectura», y «registro» puede evocar burocracia ex post. Renombrar el directorio simplemente «decisiones» suele cambiar la dinámica. Los equipos empiezan a registrar decisiones de proveedores, de planificación, de programación, de datos y de cumplimiento, todas con la misma plantilla. La gente aprende más rápido a partir de las palabras que de las abreviaturas, y participa más cuando el enfoque es «ayuda a tus futuros compañeros a pensar» en lugar de «cumple el trámite obligatorio».

### Definir el ciclo de vida y la gobernanza

Para que los registros de decisiones escalen, conviene acordar el proceso que los rodea (aquí es donde la gobernanza del capítulo 1.5 se materializa en la práctica):

- **Quién puede proponer uno y qué lo justifica:** habitualmente, cualquier contribuidor informado; se propone un registro cuando los futuros desarrolladores necesiten el *por qué*, y se omite para decisiones de bajo riesgo, autocontenidas o ya documentadas.
- **Ciclo de vida:** un flujo sencillo como *Inicio → Investigación → Evaluación → Implementación → Mantenimiento → Retiro*, con criterios de aceptación para transitar entre etapas (problema articulado, alternativas consideradas, compensaciones documentadas, partes interesadas consultadas).
- **Roles:** proponente, investigador, revisor, aprobador y un responsable de mantenimiento que revise el registro periódicamente (al menos una vez al año) y promueva su eventual retiro.
- **Gobernanza:** cómo operan el consenso, el conflicto, la escalación y el veto, y las restricciones de cumplimiento. Apóyese en principios como el *sesgo a la acción* y el *[discrepar y comprometerse](https://en.wikipedia.org/wiki/Disagree_and_commit)*, y reserve un proceso más riguroso para las decisiones irreversibles y de gran radio de impacto («puertas de un solo sentido»).

### Hacer las decisiones verificables y localizables

Un registro de decisión *documenta* una decisión; una **función de aptitud** la *asegura*: es una comprobación automatizada, ejecutada en [integración continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), que verifica que la decisión sigue vigente («todos los cambios de estado deben emitir eventos», «ningún módulo puede importar entre estos límites», mediante herramientas como ArchUnit). Esto convierte la gobernanza de una revisión manual periódica en una ejecución continua y escalable, especialmente valiosa para objetivos regulatorios y de auditoría (capítulos 3.1, 4.6, 8.5). Después, presente el registro *adecuado* en el *momento* adecuado. Una herramienta que adjunte los registros relevantes a una *pull request*, cuando un desarrollador modifica el código que ellos rigen, supera a la esperanza de que alguien lea una carpeta de documentación.

## Compensaciones: ventajas y desventajas

| Opción | Ventajas | Desventajas |
|---|---|---|
| **RDAs ligeros (Nygard/MADR)** | Rápidos de redactar; efectivamente se redactan; bajo ceremonial | Menor rigor en decisiones de alto impacto y controvertidas |
| **Plantillas exhaustivas (Tyree-Akerman)** | Alternativas ponderadas; idóneas para decisiones grandes y costosas | Más lentas; pueden disuadir el registro rutinario |
| **Inmutable + suplantación** | Trazabilidad de auditoría limpia; se conserva el histórico | Más registros; el lector debe seguir cadenas |
| **Documento vivo (modificaciones datadas)** | Una única fuente de verdad actual; fácil de mantener | Historia de auditoría más débil; riesgo de modificaciones silenciosas |
| **Markdown en el repositorio** | Versionado, revisable, junto al código | Menos accesible para no desarrolladores |
| **Wiki / herramienta de documentación** | Accesible para todos los perfiles | Histórico y revisión más débiles; se distancia del código |

La tensión central es entre **rigor y adopción**. El sistema más riguroso que nadie usa no registra nada. El más ligero que todos usan acumula valor. Parta de lo ligero y reserve un proceso más riguroso para las pocas decisiones que son costosas y difíciles de revertir.

## Preguntas para debatir con su equipo

1. **¿Cómo llegará el registro de decisión adecuado al desarrollador en el momento en que modifica el código que lo rige, en lugar de quedarse en una carpeta que nadie abre?** Una bitácora de solo escritura registra razonamientos que nunca cambian el comportamiento, y ese es el modo de fallo más frecuente: los registros existen y nadie los lee cuando importan. La consideración contraria es el esfuerzo, porque surfear automáticamente los registros (adjuntarlos a una *pull request* cuando alguien edita el código regido) requiere una inversión en herramientas que una wiki o una carpeta de documentación no exige. Aporte evidencias al debate: cuando recientemente se revirtió o revivió un debate resuelto, ¿el registro pertinente era localizable en ese momento o estaba enterrado? Para una gran organización con decenas de equipos, la localización es lo que convierte el razonamiento costoso de un equipo en un activo reutilizable en lugar de un archivo privado. Decida si los registros deben almacenarse en el control de versiones junto al código y conectarse al flujo de *pull requests*, para que el registro aparezca donde ocurre el trabajo.

2. **¿Quién es el responsable de mantenimiento de cada registro y qué impide que la bitácora se degrade en desinformación confiable?** El modo de fallo más peligroso de una bitácora de decisiones no es una carpeta vacía, sino una carpeta llena de registros cuyos costes, capacidades de proveedores y restricciones envejecieron silenciosamente hace años. Cada registro necesita un responsable que lo revise con periodicidad (al menos anual) y que promueva su suplantación o retiro, o la bitácora se pudrirá en folklore que la gente cita selectivamente y confía poco. Aporte evidencias: cuántos de sus registros carecen de fecha, cuántos describen un proveedor o un precio que ha cambiado desde entonces y cuándo se revisó cada uno. En el sector público y en entornos regulados, el asunto es más urgente, porque una cadena inmutable y suplantada es exactamente lo que los auditores y los contratistas sucesores necesitan para una justificación rastreable. Defina el ciclo de vida de forma explícita, asigne fechas a las afirmaciones que fluctúan y designe responsables, para que la bitácora siga siendo un activo vivo y no un cementerio.

3. **¿Debe estandarizarse una única plantilla para todos los equipos y cuánto rigor necesitan realmente sus decisiones de mayor enjute?** La comparabilidad es una ventaja real: cuando todos los equipos usan la misma estructura (Nygard, MADR o similar), un equipo nuevo puede encontrar tres registros previos y adoptar el razonamiento en una tarde en lugar de un mes de debate. La tensión central es entre rigor y adopción, porque la plantilla más exhaustiva que nadie usa no registra nada, mientras que la más ligera que todos usan acumula valor. Aporte evidencias: ¿se están redactando registros de hecho y, por separado, alguna decisión grande, controvertida y costosa se ha analizado insuficientemente porque la forma ligera omitió ponderar alternativas? Para una empresa que coordina decisiones solapadas entre equipos, una plantilla compartida y un índice buscable previenen decisiones divergentes e incompatibles. Parta de lo ligero para el caso habitual y acuerde de antemano qué decisiones de puerta de un solo sentido merecen una forma más rigurosa con alternativas ponderadas.

4. **¿Qué justifica de hecho proponer un registro de decisiones y quién tiene autoridad para decidir que una elección no lo necesita?** Si la barrera es demasiado alta, el razonamiento detrás de decisiones trascendentes se evapora; si es demasiado baja, la bitácora se llena de trivialidades que enterran los registros que de verdad se necesitan. En una gran organización, un umbral poco claro hace que cada equipo improvisa el suyo, la cobertura se vuelve desigual y nadie puede confiar en que la ausencia de un registro señale una decisión irrelevante. Aporte al debate un puñado de decisiones recientes que se registraron pero no necesitaban serlo, y decisiones dolorosas que no se registraron y luego costaron un redescubrimiento. Acuerde un criterio sencillo, como registrar siempre que un futuro desarrollador necesite el *por qué* y omitir decisiones de bajo riesgo, autocontenidas o ya documentadas. En contextos regulados y del sector público, el cálculo cambia, porque un mandato de auditoría puede exigir un registro para cada requisito arquitectónicamente significativo, con independencia de si el equipo lo considera digno de redactar, por lo que hay que señalar de antemano qué decisiones son innegociables.

5. **¿Sus registros son razonamiento auténtico capturado en el momento de la decisión o burocracia redactada a posteriori para cumplir un mandato?** Un registro redactado después de los hechos para cerrar un trámite tiende a lavar la opción elegida y a omitir silenciosamente las alternativas que realmente se ponderaron, que son precisamente la información que más necesita el lector del futuro. La presión contraria es real: escribir el *por qué* antes o durante la decisión se siente más lento que desplegar, y reconocer por escrito los caminos descartados exige seguridad psicológica que algunos equipos no tienen. Traiga una muestra de registros recientes a la mesa y pregunte con honestidad si el contexto y las alternativas descartadas se leen como deliberación real o como justificación retroactiva. En un equipo grande, los registros huecos son peores que ninguno, porque enseñan a la gente que la bitácora no es de fiar. En la auditoría empresarial y gubernamental, la distinción es aguda: los organismos de supervisión y los contratistas sucesores dependen de una justificación que refleje lo que realmente se consideró, y un registro que se lee como teatro socava la certeza que la bitácora existe para proporcionar.

6. **¿Cuántas de sus decisiones de mayor enjute pueden asegurarse con una función de aptitud automatizada en lugar de confiar en que la revisión manual periódica detecte una violación?** Un registro de decisión documenta una elección, pero solo una comprobación automatizada ejecutada en la integración continua impide que esa elección se erosione silenciosamente mientras decenas de desarrolladores tocan el código a lo largo de años. El contrapunto es la inversión, porque escribir y mantener funciones de aptitud (con herramientas como ArchUnit) cuesta tiempo de ingeniería, y muchas decisiones, especialmente de proceso o de proveedor, no son mecánicamente verificables. Aporte evidencias: ¿qué decisiones de límite (dependencias entre módulos, emisión de eventos, reglas de acceso a datos) se han violado silenciosamente y solo se detectaron en la revisión o en producción? Para una empresa con muchos equipos, las funciones de aptitud convierten la gobernanza de un cuello de botella central en una ejecución continua que escala sin frenar a todos. En contextos regulados y del sector público, una comprobación automatizada y permanente es una evidencia de auditoría mucho más sólida que una firma en una revisión, porque demuestra que la decisión sigue vigente hoy en lugar de que alguien la aprobó alguna vez.

## Enfoque por sector

**Start-up.** Límitese al hábito y nada más: una carpeta `decisions/` en el repositorio principal y una nota de dos secciones (contexto y elección) cada vez que se tome una decisión que el propio equipo se cuestionará en el futuro. Olvide el ciclo de vida, los roles y los aprobadores, porque el proceso que no se puede sostener se abandona. El único registro que ahorrará a su primer contratado preguntar por qué el sistema está construido de esa manera ya justifica toda la práctica.

**Pequeña empresa.** Sin arquitecto dedicado y con poco tiempo, coloque los registros donde el equipo ya trabaja: en una wiki, un documento compartido o el repositorio, en lugar de adquirir una herramienta dedicada. El hábito importa mucho más que la herramienta, así que baje la barrera: llame a la carpeta `decisions` en lugar de `adr` y capture las decisiones de proveedores y de comprar-versus-construir con la misma naturalidad que las técnicas. Cuando se recurra a contratistas externos, un registro breve y fechado de por qué se eligió un proveedor o una plataforma es un seguro económico contra quedar bloqueado en una elección que nadie podrá explicar después.

**Gran empresa.** El reto es la coordinación entre muchos equipos: estandarice una plantilla, publique un índice buscable entre equipos y respalde las decisiones clave de límite con funciones de aptitud para que las violaciones fallen la compilación en lugar de esperar a la revisión. Asigne un responsable de mantenimiento a cada registro con una cadencia de revisión, para que la bitácora siga siendo un activo vivo en lugar de degradarse en folklore. Bien hecho, el razonamiento de un equipo sobre una decisión difícil se convierte en un activo que el siguiente equipo adopta en una tarde en lugar de revivirlo.

**Sector público.** Las normas de contratación, la transparencia y la rendición de cuentas hacen que los registros de decisiones sean casi obligatorios. Exija un registro inmutable y suplantado para cada requisito arquitectónicamente significativo, cada uno vinculado al mandato o control de cumplimiento que satisface, para que los organismos de supervisión hallen una justificación rastreable y no una reconstrucción. Dado que los sistemas públicos abarcan vidas multipluri y multiproveedor, una bitácora bien mantenida es a menudo lo que permite a un contratista sucesor entender *por qué* el sistema está configurado de esa manera y continuar el trabajo sin revivir terreno ya resuelto (capítulos 4.6, 10.4).

## Ejemplos

**Start-up.** Una start-up de cinco personas añade una carpeta `decisions/` a su repositorio principal, con una nota de dos secciones (contexto y elección) cada vez que alguien toma una decisión que sus futuros yo se cuestionarán. No hay ciclo de vida, ni roles, ni aprobadores: solo el hábito de escribir el *por qué* junto al código. Cuando su primer contratado se incorpora seis meses después, lee la carpeta entera en una hora y deja de preguntar «¿por qué está construido así?». La bitácora ligera cuesta minutos por entrada y les ahorra el impuesto del redescubrimiento que muerde mucho antes de que el equipo crezca.

**Gran empresa.** Un minorista con 30 equipos de ingeniería estandariza registros en formato MADR en cada repositorio, además de un índice central buscable. Cuando un equipo nuevo enfrenta «[monorepo](https://en.wikipedia.org/wiki/Monorepo) vs. multirepo», encuentra tres registros previos con contexto y consecuencias, y adopta el razonamiento en una tarde en lugar de un mes de debate. Las decisiones clave de límite (propiedad de servicios, reglas de acceso a datos) están respaldadas por funciones de aptitud en ArchUnit, de modo que las violaciones fallan la compilación en lugar de detectarse en la revisión. Esa es gobernanza que escala sin un cuello de botella central.

**Sector público.** Un organismo que moderniza un sistema de prestaciones exige un RDA para cada requisito arquitectónicamente significativo, cada uno vinculado al mandato o control de cumplimiento que satisface (accesibilidad, residencia de datos, auditabilidad). Los registros son inmutables y suplantados, produciendo una bitácora rastreable que satisface la revisión de supervisión. Lo crucial es que también permite a un contratista sucesor comprender *por qué* el sistema está configurado de esa manera, preservando la continuidad en los ciclos multipluri y multiproveedor típicos de los programas públicos (capítulos 4.6, 10.4).

## Justificación de negocio: motivación, ROI y TCO

Un registro de decisiones cuesta minutos de redacción y unos más de revisión. El retorno es el coste evitado de la *redecisión* y el coste evitado de la *reversión errónea*, ambos elevados y recurrentes en sistemas de vida larga. Cada vez que un equipo revive un debate ya resuelto o revierte una decisión acertada porque nadie recuerda la restricción que la sustenta, paga en horas de ingeniería senior y, a menudo, en un incidente. Una bitácora de decisiones convierte ese impuesto recurrente en una única escritura.

En cuanto al **coste total de propiedad**, los registros de decisiones están entre la documentación de mayor palanca que se puede mantener, porque apuntan al activo más sensible a la rotación: la justificación. La incorporación es más rápida (los nuevos leen el *por qué*, no solo el código). La modernización es más segura (capítulo 3.6: se distingue entre decisiones esenciales e incidentales). Las auditorías son más económicas (la evidencia ya existe). El coste de *no* mantenerlos es invisible en cualquier panel de control y se acumula en silencio con cada salida. Para presentar el caso a la dirección, señale un redescubrimiento reciente costoso o una decisión revertida que causó un incidente, y señale que el coste de instituir la práctica es prácticamente nulo.

## Antipatrones y trampas

- **Registrar el *qué* sin el *por qué*:** omitir el contexto y las alternativas descartadas, que es todo el punto.
- **Burocracia a posteriori:** registros redactados para cumplir un mandato, no para pensar; se leen huecos y nadie confía en ellos.
- **Megadocumentos multidisciplinario:** una página gigante que nadie puede navegar ni suplantar con limpieza.
- **Afirmaciones sin fecha:** costes y restricciones que fueron ciertos una vez, presentados como atemporales.
- **Modificaciones silenciosas:** cambiar la historia de una decisión sin nota datada, destruyendo la traza de auditoría.
- **Bitácoras de solo escritura:** registros creados y nunca presentados en el momento en que son relevantes, por lo que no influyen en el comportamiento.
- **Control de acceso por abreviatura:** exigir «RDA» y «arquitectura» y disuadir así la participación.
- **Sin ciclo de vida:** registros que nunca se revisan, suplan ni retiran, degradándose en desinformación.

## Modelo de madurez

- **Nivel 1 (Iniciar):** Las decisiones viven en la cabeza de las personas, en hilos de chat y en mensajes de comisión; la captura es reactiva y esporádica, y la justificación se pierde con la rotación de personal.
- **Nivel 2 (Desarrollar):** Algunos equipos mantienen registros, en formatos y plantillas variados, cuando alguien se acuerda; la práctica es irregular entre equipos, sin bitácora, nomenclatura ni proceso compartidos.
- **Nivel 3 (Estandarizar):** Una plantilla única, almacenamiento en el repositorio y un ciclo de vida y gobernanza definidos (criterios de propuesta/omisión, roles, cadencia de revisión) se documentan y aplican de forma consistente en toda la organización; los registros se revisan y suplan en lugar de editarse en silencio.
- **Nivel 4 (Gestionar):** La bitácora de decisiones se mide contra líneas base: cobertura (la proporción de decisiones arquitectónicamente significativas que tienen registro), frescura (la proporción de registros revisados dentro de su cadencia, más el número de afirmaciones sin fecha o caducas) y localización (con qué frecuencia un registro relevante llegó efectivamente al desarrollador que modificó el código regido). Los responsables de mantenimiento actúan sobre esas métricas, suplantando registros caducos y cerrando brechas de cobertura con evidencia en lugar de anécdota.
- **Nivel 5 (Orquestar):** Una bitácora de decisiones buscable y transversal está integrada en el trabajo diario: los registros relevantes se presentan automáticamente en los cambios que rigen, las decisiones clave se aseguran con funciones de aptitud en la integración continua, y la bitácora alimenta la incorporación, la modernización y la auditoría como un activo vivo. La organización mejora continuamente la propia práctica, retirando, suplantando y redefiniendo el alcance de los registros a medida que el sistema y sus restricciones evolucionan, y reequilibrando dónde invierte rigor a medida que la cartera de decisiones crece.

## Ideas para la reflexión

1. ¿Cuál fue la última decisión que su equipo revirtió o revivió porque nadie recordaba el razonamiento original?
2. ¿Cambiaría algo que un `adr/` se llame `decisions/` en cuanto a quién participa y qué se registra?
3. ¿Cuáles de sus decisiones críticas podrían asegurarse hoy con una función de aptitud automatizada?
4. Inmutable con suplantación o documento vivo: ¿cuál se ajusta mejor a sus obligaciones de auditoría y a su cultura, y por qué?
5. ¿Cómo descubriría hoy un nuevo contratado (o un contratista sucesor) *por qué* su sistema está configurado de esa manera?
6. ¿Qué justifica proponer un registro de decisiones en su equipo y qué justifica *no* hacerlo?

## Puntos clave

- Un registro de decisiones capta una decisión importante con su **contexto y consecuencias**: el *por qué*, no solo el *qué*.
- Mantenga los registros **específicos, datados y ligeros**; estandarice una plantilla (Nygard, MADR o similar).
- Almacénelos **en el control de versiones junto al código**; considere llamarlos «decisiones» para ampliar la participación.
- Defina un **ciclo de vida y una gobernanza** (criterios de propuesta/omisión, roles, cadencia de revisión); reserve un proceso riguroso para las decisiones de puerta de un solo sentido.
- Haga que las decisiones sean **localizables** en el momento del cambio y, en lo posible, **verificables** mediante funciones de aptitud.
- El ROI es el coste evitado de redescubrimiento y reversión errónea; la justificación del TCO es más fuerte donde la rotación, la modernización y la auditoría pesan más. Consulte el capítulo 1.5 (toma de decisiones y gobernanza) y el capítulo 3.1 (fundamentos de la arquitectura).

## Referencias y lecturas complementarias

- Michael Nygard, «Documenting Architecture Decisions» (2011): el RDA ligero fundacional.
- MADR: proyecto Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree y Art Akerman, «Architecture Decisions: Demystifying Architecture» (*IEEE Software*, 2005).
- Olaf Zimmermann, «Y-Statements» y «Architectural Decision Making» (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: plantillas, ejemplos y guías de trabajo en equipo (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: «Lightweight Architecture Decision Records».
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (funciones de aptitud).
- AWS Prescriptive Guidance, «ADR process»; Red Hat, «Why you should use ADRs».
- Wikipedia, «Architectural decision» y «Architecturally significant requirements».

