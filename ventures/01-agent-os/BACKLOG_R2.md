# Backlog R2 — Agent OS

## Fase 0 — discovery obligatorio
### Tarea 1
Preparar lista de 20 cuentas objetivo.

### Tarea 2
Realizar 10 entrevistas con buyers o usuarios técnicos.

### Tarea 3
Documentar top 5 incidentes o miedos alrededor de agentes en producción.

## Fase 1 — foundation técnica
### Tarea 4
Inicializar backend con FastAPI y settings.

### Tarea 5
Inicializar PostgreSQL, SQLAlchemy y migraciones.

### Tarea 6
Inicializar Redis y Celery.

### Tarea 7
Configurar logging estructurado.

## Fase 2 — identidad y tenancy
### Tarea 8
Validar JWT y resolver current user.

### Tarea 9
Crear workspace y membresías.

### Tarea 10
Forzar tenant scope en capa de acceso a datos.

## Fase 3 — agentes y tools
### Tarea 11
Crear agente.

### Tarea 12
Crear versión de agente.

### Tarea 13
Crear catálogo de tools con riesgo y owner.

### Tarea 14
Asignar tools por versión de agente.

## Fase 4 — runs y trazas
### Tarea 15
Crear endpoint de run.

### Tarea 16
Ejecutar stub asíncrono.

### Tarea 17
Persistir estado de run.

### Tarea 18
Persistir pasos de traza.

### Tarea 19
Listar y consultar detalle de run.

## Fase 5 — seguridad mínima y auditoría
### Tarea 20
Aplicar deny by default a tools no autorizadas.

### Tarea 21
Guardar actor, agente, versión, workspace y timestamps por run.

### Tarea 22
Exportar auditoría en JSON.

### Tarea 23
Evitar secretos en logs y trazas.

## Fase 6 — UI mínima
### Tarea 24
Pantalla de agentes.

### Tarea 25
Pantalla de runs.

### Tarea 26
Detalle de traza.

## Fase 7 — validación de piloto
### Tarea 27
Correr piloto sobre un workflow real.

### Tarea 28
Medir onboarding, trazabilidad y valor percibido.

### Tarea 29
Decidir expansión o recorte.
