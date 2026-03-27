# Agent OS — Technical README

## Purpose
Agent OS is the operational layer for business agents that need controlled execution, step traceability, role-based access and safe tool usage.

## Initial product scope
Version 1 focuses on four capabilities:
- agent registration and versioning
- controlled execution runs
- tool access governance
- audit and trace export

## Primary architecture style
- modular monolith first
- event-ready internal boundaries
- multi-tenant from day one
- API-first

## Initial stack
- Backend API: Python 3.12 + FastAPI
- Background jobs: Celery
- Broker: Redis
- Database: PostgreSQL
- Vector support later: pgvector
- Admin UI: React + TypeScript + Vite
- Auth: Keycloak or external OIDC provider
- Containerization: Docker
- Local orchestration: docker compose
- Observability: OpenTelemetry + Prometheus + Grafana
- Reverse proxy: Nginx

## Execution model
A user or service triggers an agent run. The system resolves workspace context, validates access, loads the agent definition, checks tool permissions, executes the run, records steps and exposes an audit trail.

## Repository intention
This folder contains the technical documents and starter structure required to begin implementation.

## Near-term build order
1. core backend
2. auth and tenancy
3. agent registry
4. run execution and trace logging
5. tool governance
6. admin console
7. observability and export
