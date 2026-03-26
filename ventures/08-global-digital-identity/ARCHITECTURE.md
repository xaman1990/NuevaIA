# Arquitectura — Global Digital Identity

## Objetivo técnico
Ofrecer identidad verificable, consentida y reutilizable entre múltiples servicios.

## Stack sugerido
- Backend: Rust / Go / Python
- Wallet app: mobile + web
- Credential registry
- Verifiable credentials / DID compatible model
- KMS / HSM para claves
- Consent management service

## Módulos
1. Identity Wallet
2. Credential Issuer
3. Verification API
4. Consent Manager
5. Reputation Layer
6. Recovery & Delegation

## MVP 90 días
- Wallet básica
- Emisión y verificación de credenciales simples
- Panel de consentimiento
- SDK de integración

## Riesgos
- Regulación
- Adopción por red
- UX compleja para usuarios finales

## Resultado esperado
Infraestructura reusable para múltiples mercados regulados.
