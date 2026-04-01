# Quality Gates

## Workspace
User outside workspace cannot read workspace data.

## Agents
Duplicate key in same workspace is rejected.

## Versions
Only published version can run.

## Tools
Tool must be assigned before run can use it.

## Runs
Run returns id and state.
Completed run stays readable.

## Trace
Run steps are ordered and visible.
Failed run still has trace.

## Audit
Business actions create audit records.
One run can be exported.
