# Diagnóstico crítico — Documentación de `01-agent-os`

Fecha: 2026-03-27

## Veredicto ejecutivo (sin filtro)
La documentación tiene una **base estratégica fuerte** y, comparada con muchos repos early-stage, está por encima del promedio en claridad de problema y enfoque en control/auditoría.

Pero también muestra una fragilidad típica de proyectos de plataforma: **mucha narrativa de visión y arquitectura, poca especificación operativa para ejecutar producto real con calidad consistente**.

En corto:
- **Bien**: tesis, foco en riesgo operativo, límites de MVP, baseline de seguridad inicial.
- **Débil**: UX, diseño de interacción, modelo de datos detallado, contratos API, NFRs medibles, operación SRE, compliance formal, testing strategy aterrizada y criterios de aceptación verificables por feature.

## Lo mejor que sí está bien resuelto
1. **Problema y propuesta están claros**: pasar de pilotos caóticos a operación gobernada.
2. **Corrección de rumbo explícita**: ya reconocen riesgo de horizontalidad y lo acotan a wedge inicial.
3. **MVP lock razonable**: hay lista de incluidos/excluidos y regla de cambio.
4. **Postura de seguridad base**: deny-by-default, trazabilidad, separación de secretos, aislamiento por workspace.
5. **Disciplina comercial mejorada**: discovery y pilotos como condición para expandir alcance.

## Diagnóstico crítico por dimensión

### 1) Producto y estrategia
**Problema:** persiste ambigüedad entre “control plane narrow” vs “plataforma total”.

- Hay múltiples documentos con el mismo mensaje en diferentes grados de ambición. Eso ayuda al storytelling, pero en ejecución genera ambigüedad de prioridades.
- Falta un **single source of truth** para “qué NO se construye en los próximos 2 trimestres” con criterio de kill-switch.

**Impacto:** riesgo de backlog inflado, desalineación entre ventas y producto, y pérdida de foco de ingeniería.

---

### 2) UX / Product Design (vacío importante)
**Problema:** no hay lineamientos de UX de nivel producto.

Falta explícitamente:
- principios UX (claridad, prevención de error, explicabilidad, confianza);
- arquitectura de información (navegación, jerarquía de pantallas, objetos principales);
- flujos críticos end-to-end (crear agente, lanzar run, investigar incidente, exportar auditoría);
- estados vacíos, carga, error, degradación;
- diseño para roles distintos (AI Engineer, Security Admin, Auditor);
- criterios de accesibilidad (WCAG), i18n y consistencia visual;
- patrones de visualización de trazas (timeline, diff, step failure root cause).

**Impacto:** pueden construir backend sólido y aun así fallar en adopción interna por mala usabilidad.

---

### 3) Especificación funcional
**Problema:** hay backlog y módulos, pero faltan specs ejecutables por feature.

Falta:
- user stories con criterios de aceptación Given/When/Then;
- definición de “done” por módulo;
- límites funcionales por release;
- catálogo de errores y mensajes para API/UI;
- contratos de permisos por acción (matriz rol × recurso × operación).

**Impacto:** alta probabilidad de retrabajo y entregas “técnicamente completas, funcionalmente ambiguas”.

---

### 4) Arquitectura y datos
**Problema:** arquitectura conceptual sólida, pero faltan detalles críticos de implementación.

Falta:
- esquema de datos real (campos, índices, constraints, estrategia de particionado/retención);
- versionado de eventos y semántica de idempotencia;
- estrategia de concurrencia/locking para runs;
- políticas de reintento y compensación;
- límites de consistencia entre run state, trace store y auditoría.

**Impacto:** bugs difíciles de depurar, inconsistencias de auditoría y problemas de performance en producción.

---

### 5) Seguridad y compliance
**Problema:** baseline útil pero todavía “principios”, no “controles auditables”.

Falta:
- threat model (STRIDE o equivalente) por superficie (API, tools, secrets, tenant isolation);
- clasificación de datos y policy de retención/borrado;
- plan de respuesta a incidentes y evidencias forenses;
- mapeo a marcos (SOC2, ISO27001, GDPR/CCPA según mercado);
- hardening de tool execution (sandbox técnico real, egress controls, timeouts, quotas por tool).

**Impacto:** difícil pasar due diligence enterprise serio.

---

### 6) Operación, SRE y confiabilidad
**Problema:** observabilidad está mencionada pero no aterrizada como disciplina operativa.

Falta:
- SLO/SLI por servicio (latencia, tasa de error, disponibilidad, tiempo de diagnóstico);
- error budgets y proceso de priorización de reliability;
- runbooks (caídas de broker, backlog de jobs, fallas de proveedor LLM, degradación parcial);
- estrategia de capacity planning y load testing;
- políticas de backup/restore y pruebas de disaster recovery.

**Impacto:** cuando llegue el primer incidente real, el equipo improvisa.

---

### 7) Calidad e ingeniería
**Problema:** testing aparece en stack, pero no existe estrategia de calidad definida por capas.

Falta:
- pirámide de testing (unit, contract, integration, e2e, chaos) y cobertura objetivo;
- estándares de PR (qué pruebas son obligatorias para merge);
- convenciones de versionado (SemVer/API versioning);
- governance de migraciones DB;
- guía de contribución y convenciones de código/documentación.

**Impacto:** deuda técnica temprana y baja confianza para iterar rápido.

---

### 8) Comercial / GTM
**Problema:** GTM tiene buenas intenciones, pero no está instrumentado.

Falta:
- definición concreta de paquete piloto (alcance, precio, duración, entregables, criterios de éxito/fallo);
- playbook de ventas por segmento (integrador vs enterprise interno);
- objeciones típicas + respuestas;
- sistema de medición de conversiones por etapa de funnel.

**Impacto:** pipeline difícil de predecir y aprendizaje comercial lento.

## Inconsistencias y señales de alerta en la documentación
1. **Duplicidad alta** entre PRD, README técnico, architecture, roadmap, review docs.
2. **Idioma mixto** (español/inglés) sin regla editorial.
3. **Granularidad desigual**: algunos temas hiper estratégicos, otros demasiado esquemáticos.
4. **Código actual placeholder**: no hay todavía artefactos que validen factibilidad técnica real.

## Prioridad recomendada (próximos 30 días)
1. **Definir UX blueprint mínimo** para 3 flujos críticos.
2. **Especificar contratos API v1** (OpenAPI + error model + auth scopes).
3. **Publicar data model v1** con entidades, índices y políticas de retención.
4. **Formalizar NFRs** (SLO/SLI, seguridad mínima verificable, performance budget).
5. **Crear test strategy v1** con “quality gates” obligatorios.
6. **Empaquetar oferta piloto comercial** con pricing, entregables y métricas de conversión.

## Entregables faltantes concretos (lista accionable)
- `UX_GUIDELINES.md`
- `USER_FLOWS.md`
- `DESIGN_SYSTEM_MIN.md`
- `API_CONTRACT_V1.md` (o OpenAPI inicial)
- `DATA_MODEL_V1.md`
- `NFRS.md`
- `SRE_RUNBOOKS.md`
- `THREAT_MODEL.md`
- `COMPLIANCE_MAPPING.md`
- `TEST_STRATEGY.md`
- `CONTRIBUTING.md`
- `PILOT_OFFER.md`

## Conclusión honesta
La iniciativa **no está mal enfocada**: está mejor pensada que la mayoría de ideas “agent platform”.

Pero hoy la documentación está en estado **“visión convincente + arquitectura aspiracional”**, no en estado **“sistema listo para ejecución rigurosa de producto enterprise”**.

Si no llenan los huecos de UX, especificación funcional verificable, operación SRE y compliance, el riesgo no es técnico: es **construir bastante y aun así no lograr adopción ni contratos repetibles**.
