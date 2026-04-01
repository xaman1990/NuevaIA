# Error Model

## Error shape
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {},
    "correlationId": "string"
  }
}
```

## Categories
- validation_error
- unauthorized
- forbidden
- not_found
- conflict
- business_rule_violation
- tool_denied
- tool_timeout
- internal_error

## Examples
- trying to execute unpublished agent version -> business_rule_violation
- trying to use unassigned tool -> tool_denied
- workspace mismatch -> forbidden
- duplicated agent key -> conflict

## Logging rule
Internal exceptions may be richer in logs, but public API must return controlled error shape.

## Trace rule
Run-related failures must still generate trace and audit records when applicable.
