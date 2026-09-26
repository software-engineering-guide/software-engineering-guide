# 12.3 Plantillas

Estas plantillas son puntos de partida listos para copiar y pegar. Toma cualquier plantilla y llévala a tu wiki, repositorio, o sistema de tickets, y llena los marcadores entre corchetes. Las notas en cursiva y los comentarios en línea explican qué corresponde en cada sección; elimínalos una vez que la sección esté llena. Mantén las plantillas ligeras: una plantilla que es más rápida de saltar que de completar no se usará. Adapta los encabezados y secciones a tu organización, pero preserva la intención de cada parte.

Algunas convenciones usadas abajo:

- El texto entre `[corchetes]` es un marcador de posición para reemplazar.
- El texto en _cursiva_ o `<!-- comentarios -->` es guía para eliminar.
- Mantén el documento terminado lo más corto posible mientras siga respondiendo sus preguntas.

## Registro de Decisión de Arquitectura (ADR)

```markdown
# ADR [NNNN]: [Título corto de la decisión]

- Estado: [Propuesto | Aceptado | Obsoleto | Reemplazado por ADR-XXXX]
- Fecha: [AAAA-MM-DD]
- Quiénes deciden: [nombres o roles]
- Consultados: [nombres o roles]

## Contexto

<!-- ¿Cuál es el problema, fuerza, o restricción que impulsa esta decisión?
     Declara los hechos y requisitos neutralmente. Incluye solo lo que un
     lector futuro necesita para entender por qué fue necesaria una decisión. -->

## Decisión

<!-- Declara la elección en una o dos frases claras: "Haremos ..." -->

## Alternativas consideradas

<!-- Lista las opciones realistas que sopesaste y por qué cada una fue o no
     elegida. Al menos dos alternativas deberían aparecer aquí. -->

- Opción A: [resumen]; rechazada porque [razón].
- Opción B: [resumen]; rechazada porque [razón].
- Opción elegida: [resumen]; elegida porque [razón].

## Consecuencias

<!-- Resultados honestos de la decisión, tanto buenos como malos. -->

- Positivas: [beneficios obtenidos]
- Negativas: [costos, riesgos, o limitaciones aceptados]
- Seguimiento: [migraciones, trabajo nuevo, o decisiones que esto activa]

## Relacionados

<!-- Enlaces a ADR previos, RFC, tickets, o documentos relacionados. -->
```

## RFC / documento de diseño

```markdown
# RFC: [Título]

- Autor(es): [nombres]
- Estado: [Borrador | En revisión | Aprobado | Rechazado | Implementado]
- Revisores: [nombres o roles]
- Creado: [AAAA-MM-DD]
- Última actualización: [AAAA-MM-DD]
- Ticket / rastreo: [enlace]

## Resumen

<!-- Un párrafo: qué propone esto y por qué importa. Un lector
     debería captar la esencia solo de esta sección. -->

## Problema y motivación

<!-- ¿Qué problema estamos resolviendo? ¿A quién afecta? ¿Qué sucede si
     no hacemos nada? Incluye antecedentes y restricciones relevantes. -->

## Objetivos y no objetivos

- Objetivos: [cómo se ve el éxito, medible donde sea posible]
- No objetivos: [explícitamente fuera de alcance, para prevenir la expansión de alcance]

## Diseño propuesto

<!-- El núcleo del documento. Describe el enfoque, la arquitectura,
     el modelo de datos, las interfaces, y los flujos clave. Usa diagramas donde
     clarifiquen. Explica cómo funciona, no solo qué es. -->

## Alternativas consideradas

<!-- Otros enfoques y por qué no se eligieron. Muestra al lector
     que se exploró el espacio de diseño. -->

## Impacto y riesgos

- Seguridad y privacidad: [implicaciones y mitigaciones]
- Rendimiento y escala: [carga y comportamiento esperados]
- Operabilidad: [monitoreo, modos de fallo, despliegue, retroceso]
- Costo: [impacto de infraestructura o licenciamiento]
- Compatibilidad hacia atrás: [migración y obsolescencia]

## Plan de pruebas y despliegue

<!-- Cómo se validará el cambio y se liberará de forma segura. -->

## Preguntas abiertas

<!-- Asuntos sin resolver sobre los que quieres que opinen los revisores. -->
```

## Autopsia / revisión de incidente (sin culpa)

```markdown
# Autopsia: [Título del incidente]

- ID del incidente: [ID]
- Fecha del incidente: [AAAA-MM-DD]
- Autores: [nombres]
- Estado: [Borrador | Final]
- Severidad: [SEV1 | SEV2 | SEV3]

> Esta revisión es sin culpa. Nos enfocamos en los sistemas y factores
> contribuyentes, no en individuos. El objetivo es aprender y prevenir
> la recurrencia.

## Resumen

<!-- Dos o tres frases: qué sucedió, el impacto, y la
     resolución, legible para un no experto. -->

## Impacto

- Duración: [hora de inicio a hora de recuperación, con zona horaria]
- Usuarios afectados: [alcance y número]
- Impacto de negocio: [ingreso, SLA, reputación, u otro]

## Línea de tiempo

<!-- Secuencia factual y con marca de tiempo de eventos. Incluye la
     detección, la escalación, las acciones clave, y la recuperación. -->

- [HH:MM] [evento]
- [HH:MM] [evento]

## Factores contribuyentes

<!-- La cadena de condiciones que llevaron al incidente. Prefiere
     "factores contribuyentes" sobre una única causa raíz. -->

## Detección y respuesta

- ¿Cómo se detectó? [alerta, reporte de cliente, etc.]
- ¿Qué ayudó a la respuesta?
- ¿Qué ralentizó la respuesta?

## Qué salió bien

<!-- Reconoce las acciones y salvaguardas efectivas que funcionaron. -->

## Elementos de acción

<!-- Específicos, con dueño, y fechados. Aborda la prevención, la detección, y
     la mitigación. Rastrea estos en el backlog normal. -->

| Acción | Dueño | Fecha límite | Tipo (prevenir/detectar/mitigar) | Ticket |
|--------|-------|----------|--------------------------------|--------|
| [acción] | [nombre] | [fecha] | [tipo] | [enlace] |

## Lecciones aprendidas

<!-- Qué debería llevarse la organización más amplia. -->
```

## Modelo de amenazas (basado en STRIDE)

```markdown
# Modelo de amenazas: [Nombre del sistema o característica]

- Autor(es): [nombres]
- Fecha: [AAAA-MM-DD]
- Revisores: [contacto de seguridad, dueños]
- Alcance: [qué se cubre y qué no]

## Panorama del sistema

<!-- Descripción breve del sistema, su propósito, y sus usuarios. -->

## Activos

<!-- Qué vale la pena proteger: datos, credenciales, funcionalidad,
     reputación. Anota la sensibilidad de cada uno. -->

## Límites de confianza y flujo de datos

<!-- Describe o diagrama los componentes, almacenes de datos, entidades
     externas, y los límites donde cambia la confianza. -->

## Amenazas (STRIDE)

<!-- Para cada elemento, considera las categorías STRIDE. Registra cada
     amenaza creíble, su riesgo, y la mitigación o riesgo aceptado. -->

| Amenaza | Categoría STRIDE | Elemento afectado | Riesgo (B/M/A) | Mitigación | Estado |
|--------|-----------------|------------------|--------------|------------|--------|
| [amenaza] | Suplantación | [elemento] | [riesgo] | [control] | [abierto/mitigado/aceptado] |
| [amenaza] | Manipulación | [elemento] | [riesgo] | [control] | [estado] |
| [amenaza] | Repudio | [elemento] | [riesgo] | [control] | [estado] |
| [amenaza] | Divulgación de información | [elemento] | [riesgo] | [control] | [estado] |
| [amenaza] | Denegación de servicio | [elemento] | [riesgo] | [control] | [estado] |
| [amenaza] | Elevación de privilegio | [elemento] | [riesgo] | [control] | [estado] |

## Supuestos y dependencias

<!-- Supuestos de seguridad en los que se confía y controles externos en los que se confía. -->

## Asuntos abiertos y seguimiento

<!-- Amenazas que necesitan más trabajo, rastreadas como tickets. -->
```

## Manual de operación

```markdown
# Manual de operación: [Nombre de la tarea o escenario]

- Servicio: [nombre del servicio]
- Dueño: [equipo]
- Última revisión: [AAAA-MM-DD]
- Alertas relacionadas: [nombres de alertas]

## Propósito

<!-- Cuándo usar este manual y qué logra. -->

## Prerrequisitos

<!-- Acceso, herramientas, y permisos necesarios antes de empezar. -->

## Detección / síntomas

<!-- Qué observa el operador: alertas, firmas de error, tableros. -->

## Diagnóstico

<!-- Verificaciones paso a paso para confirmar el problema y acotar la causa.
     Incluye los comandos exactos, consultas, o enlaces de tableros. -->

1. [paso y resultado esperado]
2. [paso y resultado esperado]

## Resolución

<!-- Pasos concretos y ordenados para corregir o mitigar. Anota cualquier paso que sea
     riesgoso o irreversible, y cómo verificar el éxito. -->

1. [paso]
2. [verificar la recuperación]

## Retroceso

<!-- Cómo deshacer las acciones si la resolución empeora las cosas. -->

## Escalación

<!-- A quién contactar y cuándo escalar. Guardia secundaria, equipo
     dueño, y contactos de proveedores. -->

## Referencias

<!-- Tableros, manuales de operación relacionados, documentos de arquitectura. -->
```

## README de servicio / entrada de catálogo de servicio

```markdown
# [Nombre del servicio]

- Equipo dueño: [equipo]
- Guardia: [enlace de rotación]
- Nivel / criticidad: [Nivel 1 | 2 | 3]
- Repositorio: [enlace]
- Estado: [Activo | Obsoleto]

## Qué hace

<!-- Un párrafo sobre la responsabilidad del servicio y sus consumidores. -->

## Arquitectura

<!-- Componentes clave, dependencias (río arriba y río abajo), y un
     enlace al documento de diseño o diagrama. -->

## Interfaces

- API / puntos finales: [enlace a la especificación]
- Eventos publicados / consumidos: [temas]
- Almacenes de datos: [bases de datos, cachés, buckets]

## Tiempo de ejecución y despliegue

- Entornos: [dev, staging, prod]
- Cómo desplegar: [enlace del pipeline y proceso]
- Configuración y banderas de características: [dónde y cómo]

## Observabilidad

- Tableros: [enlaces]
- Alertas: [enlaces]
- Registros: [dónde encontrarlos]
- SLO: [enlace]

## Operaciones

- Manuales de operación: [enlaces]
- Tareas comunes: [escalado, reinicio, relleno]
- Problemas y limitaciones conocidos: [notas]

## Empezando (para nuevos colaboradores)

<!-- Cómo construir, probar, y ejecutar localmente. -->

## Contactos

- Canal de Slack / chat: [enlace]
- Escalación: [ruta]
```

## Política de SLO / presupuesto de error

```markdown
# Política de SLO y presupuesto de error: [Nombre del servicio o recorrido]

- Dueño: [equipo]
- Fecha efectiva: [AAAA-MM-DD]
- Cadencia de revisión: [por ejemplo, trimestral]

## Indicadores de nivel de servicio (SLI)

<!-- Define cada SLI precisamente: la cantidad medida, cómo se
     mide, y de dónde (idealmente la perspectiva del usuario). -->

| SLI | Definición | Fuente de datos |
|-----|-----------|-------------|
| Disponibilidad | [por ejemplo, solicitudes exitosas / solicitudes totales] | [fuente] |
| Latencia | [por ejemplo, proporción de solicitudes bajo Xms] | [fuente] |

## Objetivos (SLO)

| SLI | Objetivo | Ventana de medición |
|-----|--------|--------------------|
| Disponibilidad | [por ejemplo, 99.9%] | [por ejemplo, 28 días móviles] |
| Latencia | [por ejemplo, 95% bajo 300ms] | [28 días móviles] |

## Presupuesto de error

<!-- La falta de fiabilidad permitida: 100% menos el objetivo, sobre la
     ventana. Declara el presupuesto en términos concretos (por ejemplo, minutos/mes). -->

- Presupuesto: [asignación derivada]

## Política cuando se agota el presupuesto

<!-- Las consecuencias acordadas. Hazlas concretas y exigibles. -->

- [por ejemplo, congelar las liberaciones de características no críticas hasta que el presupuesto se recupere.]
- [por ejemplo, priorizar el trabajo de fiabilidad en el próximo ciclo de planificación.]
- [por ejemplo, escalar al liderazgo de ingeniería si se viola dos ventanas seguidas.]

## Política cuando el presupuesto está sano

<!-- Qué riesgo extra puede tomar el equipo, por ejemplo despliegues más rápidos. -->

## Alertas

<!-- Alertas de tasa de consumo y umbrales atados a este SLO. -->
```

## Entrada de registro de riesgo

```markdown
## Riesgo: [Título corto del riesgo]

- ID del riesgo: [ID]
- Fecha de planteamiento: [AAAA-MM-DD]
- Dueño: [nombre o rol responsable de gestionar este riesgo]
- Categoría: [seguridad | operativo | cumplimiento | financiero | entrega | proveedor]
- Estado: [Abierto | Mitigando | Aceptado | Cerrado]

### Descripción

<!-- Declara el riesgo como: causa -> evento -> consecuencia. Qué podría
     suceder, y por qué importa. -->

### Evaluación

- Probabilidad: [Baja | Media | Alta]
- Impacto: [Bajo | Medio | Alto]
- Calificación general: [derivada de probabilidad x impacto]

### Controles actuales

<!-- Qué ya reduce este riesgo hoy. -->

### Plan de mitigación

<!-- Acciones planificadas para reducir la probabilidad o el impacto, con dueños y
     fechas. Si se acepta el riesgo, registra quién lo aceptó y por qué. -->

| Acción | Dueño | Fecha límite | Estado |
|--------|-------|----------|--------|
| [acción] | [nombre] | [fecha] | [estado] |

### Revisión

- Próxima fecha de revisión: [AAAA-MM-DD]
- Decisión / notas: [cualquier aprobación de aceptación o cambio]
```

## Hoja única de proyecto / resumen de producto

```markdown
# [Nombre del proyecto o producto]: hoja única

- Patrocinador: [nombre]
- Líder: [nombre]
- Fecha: [AAAA-MM-DD]
- Estado: [Idea | Aprobado | En progreso | Entregado]

## Problema

<!-- Un párrafo: el problema del cliente o de negocio, y evidencia de que
     es real y vale la pena resolver. -->

## Audiencia

<!-- Quién tiene este problema y quién se beneficia de resolverlo. -->

## Solución propuesta

<!-- Una descripción corta de qué construiremos o cambiaremos. Mantenla al
     nivel de intención, no de detalle de implementación. -->

## Por qué ahora

<!-- La razón para hacer esto ahora en lugar de después. -->

## Métricas de éxito

<!-- Cómo sabremos que funcionó. Prefiere resultados medibles. -->

- [métrica y objetivo]

## Alcance

- En alcance: [qué haremos]
- Fuera de alcance: [qué no haremos]

## Riesgos y preguntas abiertas

<!-- Principales incertidumbres y dependencias. -->

## Plan aproximado e hitos

<!-- Fases de alto nivel y calendario aproximado. -->

## Costo y recursos

<!-- Personas, tiempo, y presupuesto requeridos. -->
```

## Notas de transferencia de guardia

```markdown
# Transferencia de guardia: [AAAA-MM-DD]

- Saliente: [nombre]
- Entrante: [nombre]
- Servicio(s): [nombres]

## Estado general

<!-- Una línea: tranquilo, ruidoso, o problema en curso. -->

## Incidentes abiertos

<!-- Cualquier incidente activo o recientemente resuelto que el
     siguiente respondiente debe conocer, con enlaces. -->

- [incidente, estado, y qué queda pendiente]

## Cambios en curso o planificados

<!-- Despliegues, migraciones, ventanas de mantenimiento, o experimentos en
     vuelo que podrían causar alertas. -->

## Alertas ruidosas o inestables

<!-- Alertas que se dispararon y su significado real, para que la
     siguiente persona no se confunda. Anota cualquier silencio temporal y su expiración. -->

## Elementos a vigilar

<!-- Métricas o sistemas con tendencia en una dirección preocupante. -->

## Seguimientos pendientes

<!-- Tareas entregadas al siguiente turno, con enlaces a tickets. -->

## Notas

<!-- Cualquier otra cosa útil: peculiaridades de acceso, problemas con proveedores, contexto. -->
```

## Solicitud de cambio (para control de cambios regulado)

```markdown
# Solicitud de cambio: [Título del cambio]

- ID del cambio: [ID]
- Solicitante: [nombre]
- Fecha de envío: [AAAA-MM-DD]
- Tipo: [Estándar | Normal | Emergencia]
- Prioridad: [Baja | Media | Alta]
- Estado: [Enviado | Aprobado | Rechazado | Implementado | Cerrado]

## Descripción del cambio

<!-- Qué está cambiando y por qué. Referencia el ticket o requisito. -->

## Sistemas y componentes afectados

<!-- Servicios, datos, entornos, y usuarios impactados. -->

## Justificación e impacto de negocio

<!-- La razón del cambio y el impacto de no hacerlo. -->

## Evaluación de riesgo

- Nivel de riesgo: [Bajo | Medio | Alto]
- Impacto potencial si el cambio falla: [descripción]
- Impacto en la seguridad, privacidad, o cumplimiento: [descripción]

## Plan de implementación

<!-- Pasos ordenados, partes responsables, y calendario. -->

## Plan de prueba y validación

<!-- Cómo se verificará el éxito antes y después del cambio. -->

## Plan de reversión / retroceso

<!-- Cómo revertir el cambio si falla, y el tiempo de recuperación. -->

## Calendario

- Ventana propuesta: [inicio y fin, con zona horaria]
- Tiempo de inactividad esperado: [duración o ninguno]

## Aprobaciones

| Rol | Nombre | Decisión | Fecha |
|------|------|----------|------|
| Dueño del cambio | [nombre] | [aprobar/rechazar] | [fecha] |
| Revisor técnico | [nombre] | [aprobar/rechazar] | [fecha] |
| Comité asesor de cambios | [nombre] | [aprobar/rechazar] | [fecha] |

## Revisión posterior a la implementación

<!-- Resultado, problemas encontrados, y si se necesitó la reversión. -->
```

## Esquema de Evaluación de Impacto de Protección de Datos (DPIA)

```markdown
# Evaluación de Impacto de Protección de Datos: [Nombre de la actividad de procesamiento]

- Evaluador: [nombre]
- Fecha: [AAAA-MM-DD]
- Revisores: [DPO / contacto de privacidad]
- Estado: [Borrador | Revisado | Aprobado]

## 1. Descripción del procesamiento

<!-- Qué datos personales se procesan, cómo, por quién, y para qué
     propósito. Incluye los flujos de datos desde la recolección hasta la eliminación. -->

- Titulares de datos: [de quién son los datos]
- Categorías de datos: [tipos de datos personales, anota cualquier categoría especial]
- Propósitos: [por qué se procesan los datos]
- Receptores y procesadores: [quién recibe o maneja los datos]
- Período de retención: [cuánto tiempo se guardan los datos y método de eliminación]
- Transferencias internacionales: [destinos y mecanismo de transferencia]

## 2. Necesidad y proporcionalidad

<!-- ¿Es el procesamiento necesario para el propósito? ¿Es la opción menos
     intrusiva? ¿Cuál es la base legal o autoridad? -->

- Base legal / autoridad: [base para cada propósito]
- Minimización de datos: [por qué cada campo es necesario]
- Justificación de exactitud y retención: [notas]
- Cómo se respaldan los derechos del titular de datos: [acceso, eliminación, etc.]

## 3. Consulta

<!-- Interesados, y donde sea relevante titulares de datos, consultados. -->

## 4. Riesgos para los individuos

<!-- Identifica los riesgos de privacidad y califica cada uno. -->

| Riesgo para los individuos | Probabilidad | Severidad | General |
|---------------------|-----------|----------|---------|
| [por ejemplo, acceso no autorizado a datos sensibles] | [B/M/A] | [B/M/A] | [calificación] |

## 5. Medidas para reducir el riesgo

<!-- Para cada riesgo, la mitigación y el riesgo residual después de ella. -->

| Riesgo | Medida | Riesgo residual | Aceptado por |
|------|---------|---------------|-------------|
| [riesgo] | [control] | [B/M/A] | [nombre] |

## 6. Resultado y aprobación

- Riesgo residual aceptable: [Sí | No]
- Medidas aprobadas por: [nombre, rol]
- Se requiere consulta con la autoridad de supervisión: [Sí | No]
- Fecha de revisión: [AAAA-MM-DD]
```
