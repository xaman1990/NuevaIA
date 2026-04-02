# Secret Binding Spec

## Objetivo
Definir cómo una tool se conecta con secretos sin almacenar valores sensibles en tablas de negocio.

## Principio
La tool nunca guarda el secreto crudo. Solo guarda referencia declarativa.

## Modelo recomendado
### workspace_secrets
- secret_key
- provider_type
- reference_value
- status

### tool secret binding
Agregar una estructura en metadata o tabla futura con:
- tool_id
- required_secret_keys[]

## Regla de resolución
1. la tool declara qué claves necesita
2. en tiempo de ejecución el orchestrator resuelve las referencias del workspace
3. el valor real se obtiene del proveedor configurado o entorno seguro
4. el secreto nunca entra a respuesta API, traza ni logs

## MVP pragmatico
### Opción elegida
- almacenar en `workspace_secrets.reference_value` una referencia segura, no el valor real
- resolver inicialmente desde variables protegidas o un provider simple

## Validaciones
- no se puede activar una tool si requiere secretos no configurados
- no se puede ejecutar un run si la tool asignada carece de binding válido

## Error recomendado
`business_rule_violation` o `tool_denied` cuando falte binding válido
