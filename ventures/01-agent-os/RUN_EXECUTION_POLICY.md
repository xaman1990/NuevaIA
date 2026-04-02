# Run Execution Policy

## Objetivo
Definir cómo se ejecuta un run en versión 1 para evitar ambigüedad en workers, reintentos, cancelación e idempotencia.

## Ciclo de vida
1. API crea run en estado `queued`
2. Se encola tarea en Celery
3. Worker toma el run y cambia a `running`
4. Worker registra pasos en `run_steps`
5. Worker cierra run en `succeeded`, `failed` o `cancelled`

## Política de reintentos
### Regla general
- No reintentar automáticamente un run completo en v1
- Sí permitir reintento manual desde una acción posterior del sistema

### Justificación
Los runs pueden tocar sistemas externos y un reintento automático podría duplicar efectos.

## Política de idempotencia
### Regla
Toda creación de run debe aceptar `idempotencyKey` opcional.

### Comportamiento
- si llega la misma key para el mismo workspace y el mismo payload dentro de una ventana corta, se devuelve el run existente
- si cambia el payload, se rechaza con `409 conflict`

## Política de timeout
### Run timeout
- todo run debe tener `maxRunSeconds`
- valor por defecto v1: 300 segundos

### Tool timeout
- cada tool define `timeout_seconds`
- una tool que excede timeout genera step `failed`

## Política de cancelación
### Endpoint requerido
`POST /workspaces/{workspaceId}/runs/{runId}/cancel`

### Regla
- solo runs en `queued` o `running` pueden cancelarse
- la cancelación debe generar audit event
- si el worker ya completó el run, cancelar devuelve `409 conflict`

## Política de actor
### Tipos de trigger
- `manual_user`
- `system`
- `api`

### Regla
Si no hay usuario humano, debe existir `triggered_by_system_key` o equivalente en auditoría.

## Política de failure
- un fallo no borra pasos previos
- todo fallo terminal debe registrar `error_code` y mensaje controlado
- runs terminales son inmutables
