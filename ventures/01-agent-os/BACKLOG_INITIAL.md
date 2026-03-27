# Initial Backlog

## Epic 1 — foundation
### Story 1
Set up backend project with FastAPI, settings, health endpoint and base dependency injection.

### Story 2
Set up PostgreSQL, SQLAlchemy, Alembic and first migration.

### Story 3
Set up Celery and Redis with one sample background task.

## Epic 2 — identity and workspaces
### Story 4
Implement token validation and current user resolution.

### Story 5
Create workspace model and membership model.

### Story 6
Implement role checks for workspace actions.

## Epic 3 — agents
### Story 7
Create agent entity and CRUD endpoints.

### Story 8
Create agent version entity and publish flow.

### Story 9
List agents and versions by workspace.

## Epic 4 — tools
### Story 10
Create tool entity and catalog endpoints.

### Story 11
Assign tools to agent versions.

### Story 12
Add allow/deny validation before run execution.

## Epic 5 — runs and traces
### Story 13
Create run request endpoint.

### Story 14
Run background execution stub.

### Story 15
Persist run status changes.

### Story 16
Persist step trace records.

### Story 17
Expose run detail with ordered trace.

## Epic 6 — audit and export
### Story 18
Create audit query endpoint.

### Story 19
Export run trace as JSON.

## Epic 7 — admin console
### Story 20
Create frontend shell with auth-aware routing.

### Story 21
Create agents screen.

### Story 22
Create runs and trace detail screens.

## Epic 8 — dev quality
### Story 23
Add test scaffolding for backend.

### Story 24
Add lint and format rules.

### Story 25
Add docker compose local environment.
