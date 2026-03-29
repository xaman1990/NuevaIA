# API Contract v1 (borrador ejecutable)

## Convenciones
- Base path: `/api/v1`
- Auth: `Authorization: Bearer <JWT>`
- Multi-tenant: `X-Workspace-Id` obligatorio
- Idempotencia en creación de run: `Idempotency-Key`

## Endpoints clave
### Agents
- `POST /agents`
- `GET /agents`
- `POST /agents/{agent_id}/versions`
- `POST /agents/{agent_id}/versions/{version_id}/publish`

### Tools
- `POST /tools`
- `GET /tools`
- `POST /agents/{agent_id}/versions/{version_id}/tool-bindings`

### Runs
- `POST /runs`
- `GET /runs`
- `GET /runs/{run_id}`
- `GET /runs/{run_id}/steps`

### Audit
- `GET /audit/events`
- `POST /audit/exports`

## Error model
```json
{
  "error_code": "TOOL_DENIED",
  "message": "Tool is not allowlisted for this agent version",
  "correlation_id": "c_7712",
  "details": {
    "tool": "sap_api.delete_payment",
    "agent_version": "v3"
  }
}
```

## Códigos mínimos
- `400` bad request
- `401` unauthenticated
- `403` forbidden / denied by policy
- `404` not found in workspace scope
- `409` conflict (idempotency/state)
- `422` validation error
- `500` internal
