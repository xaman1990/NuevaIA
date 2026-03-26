# Arquitectura — Robot Cloud

## Objetivo técnico
Unificar control, observabilidad y coordinación de dispositivos autónomos físicos.

## Stack sugerido
- Edge agents en cada dispositivo
- Backend cloud con FastAPI / Go
- Mensajería MQTT / NATS
- Time-series DB
- Motor de reglas y misiones
- Frontend geoespacial

## Módulos
1. Device Registry
2. Telemetry Ingestion
3. Mission Control
4. Fleet Orchestrator
5. Edge Update Manager
6. Computer Vision Services
7. Incident Center

## MVP 90 días
- Registro de dispositivos
- Streaming de telemetría
- Comandos remotos básicos
- Consola de flota en mapa

## Riesgos
- Conectividad intermitente
- Seguridad física y lógica
- Diversidad de hardware

## Resultado esperado
Base SaaS para operaciones robotizadas a escala.
