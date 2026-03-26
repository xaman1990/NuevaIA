# Arquitectura — AI Native Programming Language

## Objetivo técnico
Crear un lenguaje con compilación, runtime y debugging para sistemas IA nativos.

## Componentes
1. Especificación del lenguaje
2. Parser / AST
3. Type system orientado a objetivos y efectos
4. Runtime de ejecución
5. Tool interface layer
6. Memory bindings
7. Debugger y trace visualizer

## Primitivas propuestas
- goal
- observe
- plan
- act
- reflect
- constraint
- memory
- policy

## Stack de implementación inicial
- Compiler front-end: Rust o TypeScript
- Runtime: Rust / Python hybrid
- VS Code extension
- Playground web

## MVP 90 días
- DSL mínima
- Parser y ejecutor simple
- Ejemplos de agentes
- Extension básica para editor

## Riesgos
- Adopción baja sin killer app
- Sobrecarga conceptual
- Necesidad de integrarse con ecosistemas existentes

## Resultado esperado
Una base diferenciada para toda la línea de productos de agentes.
