# Data Model v1 — Agent OS

## Entidades núcleo
- `workspaces(id, name, plan, created_at)`
- `workspace_members(id, workspace_id, user_id, role, created_at)`
- `agents(id, workspace_id, name, owner_id, status, created_at)`
- `agent_versions(id, agent_id, version, config_json, published_at)`
- `tools(id, workspace_id, name, risk_level, owner_id, status)`
- `tool_bindings(id, agent_version_id, tool_id, policy_mode)`
- `runs(id, workspace_id, agent_id, agent_version_id, actor_id, status, started_at, ended_at, correlation_id)`
- `run_steps(id, run_id, step_index, step_name, step_status, latency_ms, input_ref, output_ref, error_code)`
- `audit_events(id, workspace_id, run_id, event_type, event_payload, created_at, immutable_hash)`

## Índices mínimos
- `runs(workspace_id, created_at desc)`
- `runs(agent_id, status)`
- `run_steps(run_id, step_index)`
- `audit_events(workspace_id, created_at desc)`

## Invariantes
- Un `run` pertenece a un único `workspace`.
- No hay `run_step` sin `run`.
- `audit_events` no se reescriben tras cierre de run.
- `tool_bindings` deben apuntar a versión de agente existente.

## Retención inicial
- `run_steps`: 90 días hot, luego archivo.
- `audit_events`: 365 días mínimo.
