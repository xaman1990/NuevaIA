# NFRs v1 — Agent OS

## Objetivos de confiabilidad
- API availability mensual: **99.5%**
- Éxito de creación de run: **>= 99%**
- Integridad de trazas por run: **>= 99.9%**

## Latencia
- `POST /runs` p95 < 400 ms (aceptación de request)
- `GET /runs/{id}` p95 < 250 ms
- `GET /runs/{id}/steps` p95 < 500 ms con paginación

## Observabilidad
- 100% de runs con `correlation_id`
- 100% de eventos de tool invocation trazados
- Trazas distribuidas activas en API + workers

## Operación
- MTTD objetivo: < 10 min
- MTTR objetivo: < 60 min para incidentes severidad alta
- Backup DB diario + restore test mensual

## Escalabilidad inicial
- 200 runs/min sostenidos por workspace sin degradar SLO de API
