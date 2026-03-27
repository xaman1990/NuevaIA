# Tech Stack

## Backend
- Python 3.12
- FastAPI
- Pydantic v2
- SQLAlchemy 2.x
- Alembic
- Celery
- Redis
- PostgreSQL 16

## Frontend
- React
- TypeScript
- Vite
- TanStack Query
- React Router
- Tailwind CSS
- shadcn/ui style component approach

## Security and identity
- OIDC
- Keycloak for self-hosted enterprise friendly option
- JWT validation in API
- secret storage through environment and external secret manager later

## Observability
- OpenTelemetry SDK
- Prometheus
- Grafana
- structured JSON logs

## Infra
- Docker
- Docker Compose for local dev
- Kubernetes later when product maturity justifies it
- Nginx as reverse proxy

## Testing
- pytest
- httpx test client
- pytest-asyncio
- Playwright for admin UI later

## Documentation
- Markdown docs in repo
- OpenAPI generated from FastAPI
- architecture diagrams later from Mermaid or C4 tooling

## Why this stack
- fast iteration
- strong ecosystem for APIs and automation
- simple enough for an MVP
- can evolve without deep rewrites if boundaries are respected
