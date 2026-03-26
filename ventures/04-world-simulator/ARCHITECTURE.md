# Arquitectura — World Simulator

## Objetivo técnico
Simular sistemas complejos del mundo físico y económico con capacidad de escenarios, optimización y predicción.

## Stack sugerido
- Backend: Python
- Motor de simulación: AnyLogic-like custom engine o Mesa + servicios propios
- Geo stack: PostGIS + deck.gl
- Series temporales: TimescaleDB
- Data lake: object storage
- ML: pipelines para forecasting y clasificación
- Frontend: React + mapas + dashboards

## Módulos
1. Data Ingestion Layer
2. World Model Builder
3. Simulation Engine
4. Scenario Designer
5. Optimization Engine
6. Risk Monitor
7. Visualization Console

## Modelo de datos
- Region
- Asset
- Flow
- Constraint
- Event
- Scenario
- SimulationRun
- KPISet

## Flujo principal
1. Se cargan datos reales.
2. Se arma el modelo del dominio.
3. Se definen escenarios.
4. El motor simula.
5. Se comparan KPIs y riesgos.

## MVP 90 días
- Simulación de una ciudad o corredor logístico
- KPIs de demanda, congestión y costes
- Dashboard geoespacial
- Comparador de escenarios

## Riesgos
- Calidad de datos
- Exceso de complejidad en la primera versión
- Dependencia de expertos del dominio

## Resultado esperado
Una plataforma de simulación vendible a clientes de ticket alto.
