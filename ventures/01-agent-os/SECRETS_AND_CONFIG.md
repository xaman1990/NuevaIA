# Secrets and Config

## Config layers
- application settings
- infrastructure settings
- workspace secret references

## Version 1 rule
Do not store raw secrets in business tables.

## Accepted approach for MVP
- application config from environment variables
- workspace secrets stored as references
- secret values resolved from external provider later

## Minimum config items
- database url
- redis url
- oidc issuer url
- oidc audience
- app environment
- log level

## Minimum secret items
- provider client secret
- internal signing secret if needed
- external tool credentials by workspace

## Safety rule
Secrets must never appear in API responses, traces or logs.
