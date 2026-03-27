# Security Baseline — Agent OS

## Objetivo
Definir los controles mínimos de seguridad que deben existir desde la primera versión usable.

## 1. Identidad y acceso
- autenticación vía OIDC
- validación de JWT en API
- RBAC por workspace
- deny by default para acciones no autorizadas

## 2. Tools
- toda tool debe estar registrada
- toda tool debe tener owner, nivel de riesgo y descripción
- ninguna tool puede ser usada por un agente sin asignación explícita
- allowlist por versión de agente

## 3. Secretos
- secretos separados por workspace
- secretos fuera de tablas de negocio
- no exponer secretos en trazas ni logs
- rotación manual inicial documentada

## 4. Runs
- cada run debe registrar actor, workspace, agente, versión y hora
- toda invocación de tool debe quedar trazada
- el resultado final no debe poder reescribirse silenciosamente

## 5. Auditoría
- exportación de auditoría en JSON
- historial consultable por filtros
- integridad lógica del historial luego de cierre de run

## 6. Aislamiento
- aislamiento lógico por workspace
- validación obligatoria de tenant scope en consultas
- evitar ejecución cruzada entre workspaces

## 7. Logs
- logs estructurados
- no incluir secretos
- incluir correlation id y run id

## 8. Postura para MVP
No se promete seguridad perfecta. Se promete una base seria y verificable para operar agentes con menos riesgo que un conjunto caótico de scripts o frameworks sueltos.
