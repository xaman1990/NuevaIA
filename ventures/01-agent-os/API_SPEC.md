# API Spec

## Base path
`/api/v1`

## Auth
All endpoints require Bearer JWT except health checks.

## Health
### GET /health
Returns service health.

## Workspaces
### GET /workspaces/current
Returns current workspace context.

### GET /workspaces/{workspaceId}/members
List members for workspace admins.

## Agents
### POST /workspaces/{workspaceId}/agents
Create agent.

### GET /workspaces/{workspaceId}/agents
List agents.

### GET /workspaces/{workspaceId}/agents/{agentId}
Get agent detail.

### PATCH /workspaces/{workspaceId}/agents/{agentId}
Update agent metadata.

## Agent Versions
### POST /workspaces/{workspaceId}/agents/{agentId}/versions
Create draft version.

### POST /workspaces/{workspaceId}/agents/{agentId}/versions/{versionId}/publish
Publish version.

### GET /workspaces/{workspaceId}/agents/{agentId}/versions
List versions.

## Tools
### POST /workspaces/{workspaceId}/tools
Create tool.

### GET /workspaces/{workspaceId}/tools
List tools.

### PATCH /workspaces/{workspaceId}/tools/{toolId}
Update tool metadata.

### POST /workspaces/{workspaceId}/agent-versions/{versionId}/tools/{toolId}
Assign tool to version.

### DELETE /workspaces/{workspaceId}/agent-versions/{versionId}/tools/{toolId}
Remove tool assignment.

## Runs
### POST /workspaces/{workspaceId}/runs
Create run.

Request:
- agentId
- agentVersionId
- triggerType
- inputPayload

Response:
- runId
- status
- correlationId

### GET /workspaces/{workspaceId}/runs
List runs with filters.

Filters:
- status
- agentId
- createdFrom
- createdTo

### GET /workspaces/{workspaceId}/runs/{runId}
Get run summary.

### GET /workspaces/{workspaceId}/runs/{runId}/steps
Get ordered run steps.

## Audit
### GET /workspaces/{workspaceId}/audit-events
List audit events with filters.

### GET /workspaces/{workspaceId}/runs/{runId}/export
Export one run as JSON.

## Error handling
- 400 validation_error
- 401 unauthorized
- 403 forbidden
- 404 not_found
- 409 conflict
- 422 business_rule_violation
- 500 internal_error

## Versioning rule
Breaking changes require new API version path.
