# Run State Machine

## Run states
- queued
- running
- succeeded
- failed
- cancelled

## Allowed transitions
- queued -> running
- queued -> cancelled
- running -> succeeded
- running -> failed
- running -> cancelled

## Forbidden transitions
- succeeded -> any other state
- failed -> any other state
- cancelled -> any other state

## Step states
- pending
- running
- succeeded
- failed
- skipped

## Rules
- run starts in queued
- first worker action changes queued to running
- every step begins as pending and moves forward only once
- terminal run states are immutable
- cancellation must be recorded as explicit action, not silent disappearance

## Audit requirement
Every state change in runs must emit an audit event.
