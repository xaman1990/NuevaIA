# Technical Architecture

## Architecture decision
Start as a modular monolith with strict module boundaries. Do not split into microservices early.

## Core runtime flow
1. request enters API
2. identity and workspace context resolved
3. authorization checks applied
4. agent definition loaded
5. tool policy validated
6. execution created
7. steps recorded during run
8. result stored and exposed
9. audit export available

## Main modules
- Identity and Access
- Workspace and Tenant Management
- Agent Registry
- Agent Versioning
- Tool Catalog
- Tool Permission Engine
- Run Orchestrator
- Step Trace Store
- Audit Export
- Notification hooks
- Admin UI API

## Main logical layers
### Presentation layer
- REST API
- admin web UI

### Application layer
- use cases
- command handlers
- orchestration services

### Domain layer
- entities
- policies
- invariants
- domain services

### Infrastructure layer
- ORM repositories
- queue integration
- auth provider integration
- observability adapters
- export adapters

## Multi-tenant approach
Single database, shared schema, tenant isolation at application and query level in version 1.

## Security posture
- RBAC at workspace level
- tool access allowlist
- execution records immutable after completion
- secrets never stored in plain text in business tables
- approval hook for risky actions reserved for later phase

## Event design
Use internal domain events even inside the modular monolith.
Examples:
- agent.created
- agent.version.published
- run.started
- run.step.recorded
- run.completed
- tool.denied

## Persistence areas
- transactional relational data in PostgreSQL
- queue tasks in Redis
- future semantic memory in pgvector
- object export storage later if needed

## Technical constraints
- avoid custom workflow engine in v1
- avoid plugin marketplace in v1
- avoid advanced multi-agent coordination in v1
- avoid kubernetes dependency in local build

## Engineering principle
Every feature must improve one of these: control, traceability, safety, operability.
