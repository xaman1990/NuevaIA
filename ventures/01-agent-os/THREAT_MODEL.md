# Threat Model v1 — Agent OS (STRIDE resumido)

## Superficie 1: API pública
- **Spoofing:** JWT inválido o robado.
- **Mitigación:** validación OIDC, expiración corta, rotación de claves.

- **Tampering:** alteración de payload run.
- **Mitigación:** validación estricta, idempotency key, auditoría inmutable.

## Superficie 2: Tool execution
- **Elevation of privilege:** agente invoca tool no autorizada.
- **Mitigación:** allowlist por versión + deny by default + risk gate.

- **DoS:** tool externa lenta bloquea workers.
- **Mitigación:** timeout, circuit breaker, colas separadas por prioridad.

## Superficie 3: Multi-tenant
- **Information disclosure:** fuga entre workspaces.
- **Mitigación:** tenant scope obligatorio en query layer + pruebas de aislamiento.

## Superficie 4: Secrets
- **Information disclosure:** secretos en logs/trazas.
- **Mitigación:** redacción de campos sensibles + almacenamiento fuera de tablas de negocio.

## Superficie 5: Auditoría
- **Repudiation:** actor niega acción.
- **Mitigación:** actor_id + timestamps + hash de integridad por evento.
