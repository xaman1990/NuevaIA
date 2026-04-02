# Request Response Schemas

## POST /workspaces/{workspaceId}/agents
### Request
```json
{
  "name": "ERP Sync Bot",
  "key": "erp-sync-bot",
  "description": "Sincroniza datos ERP a CRM"
}
```

### Response
```json
{
  "id": "uuid",
  "workspaceId": "uuid",
  "name": "ERP Sync Bot",
  "key": "erp-sync-bot",
  "status": "draft"
}
```

## POST /workspaces/{workspaceId}/agents/{agentId}/versions
### Request
```json
{
  "versionLabel": "1.0.0",
  "runtimeConfig": {
    "entrypoint": "default",
    "maxRunSeconds": 300
  }
}
```

### Response
```json
{
  "id": "uuid",
  "agentId": "uuid",
  "versionLabel": "1.0.0",
  "status": "draft"
}
```

## POST /workspaces/{workspaceId}/tools
### Request
```json
{
  "name": "CRM API",
  "key": "crm-api",
  "description": "Acceso CRM",
  "ownerName": "Integration Team",
  "riskLevel": "medium",
  "timeoutSeconds": 30,
  "configSchema": {}
}
```

### Response
```json
{
  "id": "uuid",
  "workspaceId": "uuid",
  "name": "CRM API",
  "key": "crm-api",
  "status": "active"
}
```

## POST /workspaces/{workspaceId}/runs
### Request
```json
{
  "agentId": "uuid",
  "agentVersionId": "uuid",
  "triggerType": "manual_user",
  "idempotencyKey": "string-optional",
  "inputPayload": {
    "documentId": "123"
  }
}
```

### Response
```json
{
  "runId": "uuid",
  "status": "queued",
  "correlationId": "uuid"
}
```

## GET /workspaces/{workspaceId}/runs/{runId}
### Response
```json
{
  "id": "uuid",
  "workspaceId": "uuid",
  "agentId": "uuid",
  "agentVersionId": "uuid",
  "status": "running",
  "triggerType": "manual_user",
  "startedAt": "iso-datetime",
  "completedAt": null,
  "correlationId": "uuid"
}
```

## GET /workspaces/{workspaceId}/runs/{runId}/steps
### Response
```json
[
  {
    "id": "uuid",
    "stepOrder": 1,
    "stepType": "tool_call",
    "stepName": "fetch_erp_data",
    "status": "succeeded",
    "toolId": "uuid",
    "errorCode": null
  }
]
```

## Pagination convention
List endpoints should accept:
- page
- pageSize
- sortBy
- sortDirection

## Patch convention
PATCH endpoints accept partial fields only. Unknown fields are rejected with `400 validation_error`.
