# Domain Model

## Aggregates

### Workspace
Represents a tenant boundary.

#### Invariants
- slug must be unique
- only active workspaces can create runs
- membership changes must stay within workspace scope

### Agent
Represents a logical business agent.

#### Invariants
- name and key belong to one workspace
- archived agents cannot accept new versions
- active agent must have at least one published version before execution

### AgentVersion
Represents an executable version of an agent.

#### Invariants
- version label unique within agent
- only published versions can execute runs
- a retired version cannot receive new tool assignments

### Tool
Represents an approved callable capability.

#### Invariants
- tool key unique within workspace
- inactive tools cannot be invoked
- every tool has risk level and owner

### Run
Represents one execution instance.

#### Invariants
- run belongs to one workspace and one agent version
- run status transitions must follow allowed state machine
- completed runs are immutable except for read/export operations

### AuditEvent
Represents compliance-friendly history.

#### Invariants
- audit event is append-only
- actor, action and entity reference are mandatory for business actions

## Value Objects
- WorkspaceRole
- AgentStatus
- AgentVersionStatus
- ToolRiskLevel
- RunStatus
- StepStatus
- CorrelationId

## Domain services
- ToolPermissionEvaluator
- RunStateTransitionService
- WorkspaceScopeGuard
- AuditEventFactory

## Important rules
- deny by default for tool usage
- workspace scope mandatory for every business operation
- every tool call inside a run must produce a trace step
- every business write must emit at least one audit event
