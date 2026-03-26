# Arquitectura — Autonomous Software Factory

## Objetivo técnico
Automatizar el ciclo completo de construcción de software con agentes cooperativos.

## Stack sugerido
- Orquestación: Agent OS
- Backend: Python + FastAPI
- Frontend: React
- Repos y CI/CD: GitHub + Actions
- Base de conocimiento: PostgreSQL + vector DB
- Sandboxes: contenedores efímeros

## Agentes núcleo
1. Product Analyst Agent
2. Architect Agent
3. Backend Agent
4. Frontend Agent
5. QA Agent
6. DevOps Agent
7. Documentation Agent
8. Reviewer Agent

## Flujo principal
1. Ingesta de requerimiento.
2. Descomposición de trabajo.
3. Diseño de arquitectura.
4. Generación de código.
5. Pruebas y revisión.
6. Generación de PR y documentación.
7. Despliegue supervisado.

## MVP 90 días
- Generación de documentos y código scaffold
- PR automáticos
- Pruebas unitarias básicas
- Reporte de trazabilidad por requerimiento

## Riesgos
- Calidad inconsistente del código
- Deriva arquitectónica
- Riesgo de seguridad en código generado

## Resultado esperado
Acelerar brutalmente la producción de software con control razonable.
