# Tool Interface Spec

## Goal
Define the minimum contract every callable tool must satisfy in version 1.

## Required metadata
- id
- workspace scope
- key
- name
- description
- owner_name
- risk_level
- status
- timeout_seconds
- config_schema_json

## Invocation contract
Input:
- runId
- stepName
- correlationId
- actorContext
- toolInput

Output:
- success boolean
- outputPayload
- errorCode nullable
- errorMessage nullable
- durationMs

## Rules
- tool must be registered before use
- tool must be assigned to agent version before invocation
- inactive tool cannot run
- high risk tools may exist in catalog but remain denied for MVP if not assigned
- input and output must be serializable to JSON

## Timeout rule
Every tool invocation must have an explicit timeout.

## Trace rule
Every invocation must produce one run step record.

## Failure rule
Tool failure must not erase prior run trace.
