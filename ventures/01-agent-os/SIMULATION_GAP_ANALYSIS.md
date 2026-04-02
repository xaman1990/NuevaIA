# Simulation Gap Analysis — Agent OS

## Purpose
This document simulates how Agent OS would behave with the current specifications and identifies gaps that must be closed before implementation can be considered execution-ready.

## Simulated flow 1 — register agent and publish version
### Expected flow
1. engineer creates agent
2. engineer creates draft version
3. engineer publishes version
4. engineer assigns tools

### Works with current specs
- core entities exist
- API endpoints exist for agent creation and version publishing
- RBAC allows engineer and admin

### Gaps found
- no endpoint defined to get one version detail directly
- no endpoint defined to retire a version
- no endpoint defined to archive an agent
- no validation format defined for agent key or version label
- runtime_config_json exists but its schema is not specified

## Simulated flow 2 — assign tools to a version
### Expected flow
1. admin or engineer creates tool
2. tool is assigned to one agent version
3. run execution checks allowlist

### Works with current specs
- tool catalog exists
- assignment endpoint exists
- tool contract exists

### Gaps found
- no endpoint defined to view assigned tools for one version in a single call
- access_mode exists in data model but allowed values are not specified
- no relationship defined between tools and workspace secret references
- no process defined for testing a tool safely before production use

## Simulated flow 3 — create run and execute
### Expected flow
1. operator creates run
2. system validates workspace, version and tool permissions
3. run enters queue
4. worker executes steps
5. trace is stored
6. run completes or fails

### Works with current specs
- run endpoint exists
- run states are defined
- trace table exists
- tool deny model exists

### Gaps found
- no cancellation endpoint exists although cancelled state exists
- no retry policy is defined for worker failures
- no idempotency rule is defined for repeated run requests
- no payload size limits are defined for input_payload_json
- no execution timeout is defined at run level, only tool timeout exists
- no service account model exists for system-triggered runs

## Simulated flow 4 — audit and review incident
### Expected flow
1. auditor filters runs or audit events
2. auditor opens run detail
3. auditor exports JSON evidence

### Works with current specs
- audit export endpoint exists
- auditor role can read and export
- audit_events table exists

### Gaps found
- audit payload shape is not standardized
- no retention policy is defined for audit records
- no rule defines exactly which business actions must emit audit events
- no rule defines whether audit export is full snapshot or filtered projection

## Simulated flow 5 — multi-workspace operation
### Expected flow
1. same user belongs to multiple workspaces
2. user chooses active workspace
3. every query stays isolated

### Works with current specs
- workspace membership exists
- tenant scoping rule exists

### Gaps found
- no active workspace selection flow is defined
- no endpoint exists to switch active workspace context
- application-level tenant scope is documented, but no stronger enforcement strategy is defined

## Cross-cutting gaps
### API level
- request and response schemas are not detailed enough
- pagination and sorting rules are missing
- partial update rules for PATCH endpoints are missing
- no endpoint exists for run step replay or download other than JSON export

### Data level
- missing soft delete policy
- missing created_by and updated_by consistency across all business tables
- missing concurrency strategy for publishes and updates

### Security level
- secret references exist but secret lifecycle is under-specified
- no approval boundary for high-risk tools in later phases is outlined clearly
- no session or token expiry behavior is documented for UI workflows

### Operational level
- no worker queue naming strategy
- no retry/dead-letter behavior
- no deployment environment matrix
- no backup and restore policy for PostgreSQL

## Must-fix before implementation sprint
1. define request/response schemas for all v1 endpoints
2. define agent key and version label validation rules
3. define allowed values for tool access_mode
4. define run retry and timeout policy
5. define cancellation endpoint and semantics
6. define service account or system actor model
7. define audit payload contract
8. define active workspace selection flow
9. define secret binding model for tools
10. define pagination, sorting and filtering conventions

## Conclusion
The project is strong at product direction and architectural intent, but it is not yet fully execution-complete. The missing pieces are now narrow and actionable, which means the project is close to implementation readiness if these gaps are closed next.
