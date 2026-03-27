# Internal Alignment R2 — Agent OS

Este documento resuelve los puntos críticos detectados por el personal interno en la primera revisión. No reemplaza la crítica anterior; la convierte en decisiones obligatorias.

## 1. Problema: propuesta demasiado horizontal
### Observación del CEO y CRO
El producto seguía describiéndose como plataforma amplia y eso abría demasiados frentes.

### Resolución acordada
Agent OS no se posicionará en la fase inicial como plataforma universal. Se posicionará como:

**capa de control, trazabilidad y restricción para agentes que interactúan con sistemas reales de negocio**.

### Estado
Resuelto.

### Implicación
El caso de entrada queda limitado a workflows internos sensibles y agentes de integración.

---

## 2. Problema: MVP inflado
### Observación del CTO
El MVP seguía demasiado grande para 90 días si se quería construir bien.

### Resolución acordada
El MVP queda congelado en cinco capacidades:
1. registro de agentes
2. versionado de agentes
3. ejecución de runs
4. trazabilidad paso a paso
5. control básico de acceso a tools

### Lo que se excluye explícitamente
- marketplace
- billing complejo
- memoria semántica avanzada
- coordinación multiagente avanzada
- kubernetes obligatorio
- plugin system abierto

### Estado
Resuelto.

---

## 3. Problema: narrativa comercial débil
### Observación del CPO y CRO
El valor seguía expresado como features y no como dolor comprador.

### Resolución acordada
Narrativa oficial de valor:

**Antes de poner agentes en producción, necesitas saber qué hacen, qué pueden tocar y cómo detenerlos cuando algo sale mal.**

### Oferta inicial acordada
Pilot control package para 1 workflow crítico.

### Estado
Resuelto.

---

## 4. Problema: seguridad insuficientemente detallada
### Observación del CISO
Los controles seguían demasiado generales.

### Resolución acordada
Se aprueba baseline obligatoria:
- secretos segregados por workspace
- tools por allowlist
- deny by default para herramientas no autorizadas
- auditoría inmutable al finalizar run
- sandbox lógico por ejecución
- no almacenar secretos en tablas de negocio
- trazabilidad completa de quién ejecutó y qué tool invocó

### Estado
Parcialmente resuelto en arquitectura. Se crea documento específico de baseline.

---

## 5. Problema: riesgo de construir demasiada infraestructura propia
### Observación del VP Engineering
El diseño podía derivar en exceso de plataforma antes de validar demanda.

### Resolución acordada
Regla de ingeniería:

**comprar o adoptar componentes probados antes de construir infraestructura no diferencial**.

### Aplicación concreta
- Celery en lugar de workflow engine propio
- Redis en lugar de broker custom
- PostgreSQL en lugar de storage inventado
- OIDC/Keycloak en lugar de auth propia
- OpenTelemetry estándar en lugar de observabilidad casera

### Estado
Resuelto.

---

## 6. Problema: falta de disciplina comercial real
### Observación Founder-Market Fit
Existe riesgo de enamoramiento de arquitectura.

### Resolución acordada
Antes de ampliar el MVP, deben ejecutarse entrevistas con buyers y usuarios reales.

### Criterio obligatorio
No se aprueba expansión de alcance sin evidencia de al menos:
- 10 entrevistas relevantes
- 3 pilotos potenciales
- 1 caso con urgencia clara

### Estado
Resuelto como regla de producto.

---

## 7. Cierre del comité interno
### Decisión final
El comité acepta continuar con Agent OS solo bajo estas condiciones:
- wedge comercial estrecho
- MVP congelado
- baseline de seguridad explícita
- discovery real antes de expansión
- nada de plataforma universal en la fase inicial

### Veredicto
**Aprobado para ejecución controlada.**
