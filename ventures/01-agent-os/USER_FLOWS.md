# User Flows v1 — Agent OS

## Flujo 1: Crear agente seguro
1. Crear metadatos del agente (owner, workspace, propósito).
2. Seleccionar allowlist de tools.
3. Definir límites de ejecución (timeout, cuota, riesgo).
4. Ejecutar validación pre-publicación.
5. Publicar versión.

**Criterios de aceptación**
- No permite publicar si hay tool high-risk sin control explícito.
- Muestra lista de validaciones aprobadas/fallidas.

## Flujo 2: Ejecutar run y monitorear estado
1. Usuario dispara run desde consola o API.
2. Sistema registra actor, agente, versión, correlation_id.
3. UI muestra estado en tiempo real.
4. Si hay fallo, UI destaca paso exacto y causa.

**Criterios de aceptación**
- Todo run debe enlazar a detalle de traza.
- Debe existir acceso directo a exportación de auditoría.

## Flujo 3: Investigar incidente
1. Filtrar runs por riesgo alto + estado failed.
2. Abrir traza de run.
3. Revisar step timeline + policy decisions.
4. Exportar evidencia.
5. Abrir incidente con contexto adjunto.

**Criterios de aceptación**
- Tiempo objetivo para llegar a causa probable < 10 min.
- Se puede reconstruir secuencia de pasos sin acceder a logs crudos.

## Flujo 4: Auditoría
1. Selección por periodo + workspace + agente.
2. Export JSON firmado lógicamente.
3. Registro de quién exportó y cuándo.

**Criterios de aceptación**
- Export incluye metadatos de integridad.
- No incluye secretos ni payload sensible en claro.
