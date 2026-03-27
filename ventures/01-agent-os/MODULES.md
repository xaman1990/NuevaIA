# Modules

## 1. identity_access
Purpose: authenticate users and resolve permissions.

### Responsibilities
- validate tokens
- resolve user profile
- resolve workspace roles
- expose permission checks

## 2. workspaces
Purpose: tenant and workspace management.

### Responsibilities
- create workspace
- manage membership
- tenant scoping rules
- plan limits later

## 3. agents
Purpose: define agents and versions.

### Responsibilities
- create agent metadata
- publish versions
- bind runtime configuration
- maintain status

## 4. tools
Purpose: register tools and safe access rules.

### Responsibilities
- define tool metadata
- define risk level
- assign tool permissions to agents
- expose invocation policies

## 5. runs
Purpose: execute and track runs.

### Responsibilities
- create run request
- dispatch background execution
- update run state
- expose summaries and status

## 6. traces
Purpose: store execution steps and diagnostics.

### Responsibilities
- record step data
- store timestamps and outputs
- expose step-by-step trace
- support audit export

## 7. audits
Purpose: provide compliance-friendly history.

### Responsibilities
- immutable event history
- export filtered records
- support incident review

## 8. notifications
Purpose: emit operational signals.

### Responsibilities
- webhooks later
- alert hooks later
- run status notifications

## 9. admin_api
Purpose: application-facing orchestration for UI.

### Responsibilities
- aggregate module outputs for console
- dashboard endpoints
- filters and search
