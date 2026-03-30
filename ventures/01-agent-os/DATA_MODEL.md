# Data Model

## Scope
Version 1 uses a single PostgreSQL database with shared schema and tenant scoping at query level.

## Core tables

### workspaces
- id (uuid, pk)
- name
- slug
- status
- created_at
- updated_at

### users
- id (uuid, pk)
- external_subject
- email
- display_name
- created_at
- updated_at

### workspace_memberships
- id (uuid, pk)
- workspace_id (fk)
- user_id (fk)
- role
- status
- created_at
- updated_at

### agents
- id (uuid, pk)
- workspace_id (fk)
- name
- key
- description
- status
- created_by
- created_at
- updated_at

### agent_versions
- id (uuid, pk)
- agent_id (fk)
- version_label
- status
- runtime_config_json
- published_at
- created_by
- created_at
- updated_at

### tools
- id (uuid, pk)
- workspace_id (fk)
- name
- key
- description
- owner_name
- risk_level
- status
- config_schema_json
- created_at
- updated_at

### agent_version_tools
- id (uuid, pk)
- agent_version_id (fk)
- tool_id (fk)
- access_mode
- created_at

### runs
- id (uuid, pk)
- workspace_id (fk)
- agent_id (fk)
- agent_version_id (fk)
- triggered_by_user_id (nullable fk)
- trigger_type
- input_payload_json
- status
- started_at
- completed_at
- correlation_id
- created_at

### run_steps
- id (uuid, pk)
- run_id (fk)
- step_order
- step_type
- step_name
- status
- tool_id (nullable fk)
- input_payload_json
- output_payload_json
- error_code (nullable)
- started_at
- completed_at
- created_at

### audit_events
- id (uuid, pk)
- workspace_id (fk)
- actor_user_id (nullable fk)
- entity_type
- entity_id
- action
- payload_json
- created_at

### workspace_secrets
- id (uuid, pk)
- workspace_id (fk)
- secret_key
- provider_type
- reference_value
- status
- created_at
- updated_at

## Recommended enums
- workspace.status: active, suspended
- membership.role: workspace_admin, engineer, auditor, operator
- membership.status: invited, active, disabled
- agent.status: draft, active, archived
- agent_version.status: draft, published, retired
- tool.risk_level: low, medium, high
- tool.status: active, inactive
- run.status: queued, running, succeeded, failed, cancelled
- run_step.status: pending, running, succeeded, failed, skipped

## Constraints
- unique workspaces.slug
- unique users.external_subject
- unique agents(workspace_id, key)
- unique tools(workspace_id, key)
- unique agent_versions(agent_id, version_label)
- unique workspace_memberships(workspace_id, user_id)
- unique agent_version_tools(agent_version_id, tool_id)

## Indexes
- runs(workspace_id, created_at desc)
- runs(agent_id, created_at desc)
- run_steps(run_id, step_order)
- audit_events(workspace_id, created_at desc)
- workspace_memberships(user_id, workspace_id)
- agents(workspace_id, status)
- tools(workspace_id, status)

## Tenant rule
Every query touching business data must include workspace scope explicitly.
