# Project Structure

```text
01-agent-os/
├── README.md
├── README_TECHNICAL.md
├── PRD.md
├── C4.md
├── ROADMAP.md
├── PITCH.md
├── GTM.md
├── MODULES.md
├── TECH_STACK.md
├── ARCHITECTURE_TECHNICAL.md
├── BACKLOG_INITIAL.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── domain/
│   │   ├── application/
│   │   ├── infrastructure/
│   │   ├── workers/
│   │   └── main.py
│   ├── tests/
│   ├── alembic/
│   ├── requirements/
│   ├── Dockerfile
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── pages/
│   │   ├── features/
│   │   ├── shared/
│   │   └── main.tsx
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
├── infra/
│   ├── docker/
│   ├── compose/
│   ├── nginx/
│   └── observability/
└── scripts/
```

## Implementation note
This is the starter structure to create next. Keep the backend modular and avoid service splitting early.
