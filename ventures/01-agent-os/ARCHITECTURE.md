# Arquitectura — Agent OS

## Objetivo técnico
Proveer una base universal para ejecutar agentes con seguridad, memoria, comunicación, auditoría y observabilidad.

## Stack sugerido
- Backend: Python + FastAPI
- Orquestación: Temporal o Celery + Redis
- Runtime de agentes: Python SDK
- Bus de eventos: NATS o Kafka
- Estado transaccional: PostgreSQL
- Memoria semántica: pgvector o Qdrant
- Observabilidad: OpenTelemetry + Prometheus + Grafana
- Auth: Keycloak / Auth0 / OIDC
- UI Admin: React + TypeScript
- Infra: Docker + Kubernetes

## Módulos
1. Agent Runtime Engine
2. Registry de agentes y skills
3. Task Scheduler
4. Memory Service
5. Policy & Permission Engine
6. Event Bus
7. Audit & Replay Service
8. API Gateway
9. Admin Console
10. Billing & Quotas

## Modelo de datos inicial
- Agent
- AgentVersion
- Skill
- Execution
- Task
- MemoryRecord
- ToolBinding
- Policy
- User / Team / Workspace
- AuditEvent

## Flujo principal
1. Se registra un agente con sus capacidades.
2. Se define una tarea o trigger.
3. El scheduler crea una ejecución.
4. El runtime consulta políticas y memoria.
5. El agente usa tools internas o externas.
6. Se emiten eventos al bus.
7. Todo queda auditado y observable.

## MVP 90 días
### Fase 1
- Registro de agentes
- Runtime básico
- Ejecución de tareas manuales
- Logs por ejecución

### Fase 2
- Memoria compartida
- Scheduler
- RBAC
- Dashboard mínimo

### Fase 3
- Policy engine simple
- Tool calling
- Métricas y trazas
- API pública

## Riesgos
- Sobrediseño temprano
- Coste de inferencia
- Seguridad en tools externas
- Complejidad de debugging de agentes autónomos

## Entregable de salida
Un producto usable para desplegar agentes internos con gobierno empresarial.
