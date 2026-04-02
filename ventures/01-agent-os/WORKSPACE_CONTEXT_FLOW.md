# Workspace Context Flow

## Objetivo
Definir cómo el sistema resuelve el workspace activo cuando un usuario pertenece a uno o varios workspaces.

## Reglas
### Usuario con un solo workspace activo
- el sistema selecciona ese workspace automáticamente

### Usuario con múltiples workspaces activos
- el sistema exige selección explícita en UI
- la UI persiste `currentWorkspaceId` en sesión local
- la API siempre valida que el usuario pertenezca al workspace solicitado

## Endpoints requeridos
### GET /workspaces/current
Devuelve contexto actual cuando la UI ya envía el workspace elegido.

### GET /workspaces
Lista workspaces disponibles para el usuario autenticado.

### POST /workspaces/select
Body:
- workspaceId

Respuesta:
- workspaceId
- role
- status

## Regla de backend
El backend no confía en la selección local del frontend sin validar membresía activa.

## Regla de scoping
Todo endpoint de negocio debe:
1. leer workspaceId del path o contexto
2. validar membresía activa
3. aplicar filtro de tenant en acceso a datos

## Caso system actor
Los system actors no usan selector UI. Deben llevar `workspaceId` explícito en el trigger.
