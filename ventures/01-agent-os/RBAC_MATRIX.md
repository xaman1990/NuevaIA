# RBAC Matrix

## Roles
- workspace_admin
- engineer
- auditor
- operator

## Permissions

### workspace_admin
- manage workspace members
- create and update agents
- create and publish versions
- create and update tools
- assign tools to versions
- create runs
- view runs and traces
- export audit

### engineer
- create and update agents
- create draft versions
- publish versions
- create and update tools
- assign tools to versions
- create runs
- view runs and traces
- cannot manage memberships

### auditor
- read agents
- read tools
- read runs and steps
- export audit
- cannot create runs
- cannot change tools or versions

### operator
- create runs
- read run summaries
- read run traces for allowed workspace
- cannot change agents
- cannot change tools
- cannot export full workspace audit unless explicitly enabled

## Enforcement notes
- role checks happen at application layer
- data access always scoped by workspace
- deny by default for undefined actions
