# Test Strategy v1 — Agent OS

## Pirámide
1. **Unit tests** (dominio y policies) — objetivo 70% en módulos críticos.
2. **Integration tests** (DB + API + workers) — flujos run/traza/auditoría.
3. **Contract tests** (API schema/error model).
4. **E2E tests UI** (Playwright) para 3 flujos críticos.
5. **Security tests** (tenant isolation, tool deny-by-default).

## Quality gates para merge
- Lint y format en verde.
- Unit + integration en verde.
- Contract checks sin breaking changes no versionadas.
- Si toca auth/tenant/tools: test de seguridad obligatorio.

## Suite mínima obligatoria
- Crear agente + publicar versión.
- Asignar tool y bloquear tool no permitida.
- Crear run + registrar steps.
- Exportar auditoría.
- Verificar que secretos no aparecen en logs/traza.
