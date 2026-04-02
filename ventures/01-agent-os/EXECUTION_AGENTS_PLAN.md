# Execution Agents Plan — Cierre de brechas críticas

## Objetivo
Activar "agentes" especializados (roles) para cerrar las fallas detectadas en el diagnóstico crítico con entregables concretos y secuencia de ejecución.

## Agente 1 — Product Strategist
**Foco:** wedge, narrativa de valor, delimitación de alcance.

**Entregables:**
- `PILOT_OFFER.md`
- actualización de criterios de éxito/fracaso por piloto

## Agente 2 — UX Lead
**Foco:** experiencia operativa para control y auditoría.

**Entregables:**
- `UX_GUIDELINES.md`
- `USER_FLOWS.md`
- `DESIGN_SYSTEM_MIN.md`
- imágenes de propuesta UX en `assets/ux/`

## Agente 3 — API Architect
**Foco:** contratos funcionales v1.

**Entregables:**
- `API_CONTRACT_V1.md`

## Agente 4 — Data Architect
**Foco:** modelo de datos transaccional y trazabilidad.

**Entregables:**
- `DATA_MODEL_V1.md`

## Agente 5 — Security & Compliance
**Foco:** threat model y controles verificables.

**Entregables:**
- `THREAT_MODEL.md`

## Agente 6 — SRE / Reliability
**Foco:** NFRs, SLI/SLO y operación de incidentes.

**Entregables:**
- `NFRS.md`

## Agente 7 — QA Lead
**Foco:** estrategia de pruebas y quality gates.

**Entregables:**
- `TEST_STRATEGY.md`

## Orden recomendado
1. Product Strategist
2. UX Lead
3. API Architect + Data Architect (paralelo)
4. Security & Compliance + SRE (paralelo)
5. QA Lead

## Definición de cierre
Se considera cerrada la iteración cuando:
- existe trazabilidad entre riesgos detectados y entregables;
- cada documento define criterios verificables;
- UX cubre al menos 3 flujos críticos con artefactos visuales.
