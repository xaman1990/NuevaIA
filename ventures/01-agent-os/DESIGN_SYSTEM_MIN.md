# Design System Min — Agent OS

## Tokens base
- Color primario: `#2563EB`
- Éxito: `#22C55E`
- Warning: `#F59E0B`
- Error: `#EF4444`
- Fondo dark: `#0B1020`
- Texto principal: `#E5E7EB`

## Tipografía
- UI general: Inter/Arial fallback
- Datos técnicos y trazas: monospace

## Componentes mínimos
1. **DataTable** (orden, filtros, paginación, densidad alta)
2. **RiskBadge** (low/medium/high/critical)
3. **StepTimeline** (estado por paso)
4. **AuditExportButton** (con confirmación)
5. **PolicyDecisionCard** (allow/deny + razón)
6. **InlineErrorPanel** (error_code + remediation)

## Reglas
- Toda pantalla crítica debe mostrar `workspace` y `run_id` visibles.
- Toda acción destructiva requiere confirmación de doble paso.
- Controles primarios a la derecha, secundarios a la izquierda.
