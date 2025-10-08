# 🚀 Inicio Rápido

## Instalación (Solo la primera vez)

```bash
# 1. Dar permisos al instalador
chmod +x instalar.sh

# 2. Ejecutar instalador
./instalar.sh
```

El instalador verificará:
- ✅ Python 3
- ✅ Ollama
- ✅ Modelos Qwen disponibles
- ✅ Instalará todas las dependencias

## Uso Diario

### Opción A: Línea de Comandos 🎤

```bash
./iniciar_voz.sh
```

**Cómo funciona:**
1. El programa te dice "Escuchando..."
2. Habla tu pregunta
3. Espera la respuesta en audio
4. Repite

**Comandos de voz:**
- "Salir" o "Adiós" → Termina el programa
- "Limpiar historial" → Reinicia la conversación

### Opción B: Interfaz Web 🌐

```bash
./iniciar_web.sh
```

Luego abre en tu navegador: **http://localhost:5000**

**Características:**
- 💬 Chat visual
- 🎤 Botón de micrófono
- ⌨️ También puedes escribir
- 🗑️ Botón para limpiar conversación
- 🔊 Respuestas en audio automáticas

## Solución Rápida de Problemas

### ❌ Error: "No se pudo conectar con Ollama"

```bash
# Inicia Ollama en otra terminal
ollama serve
```

### ❌ Error: "No se detectó voz"

1. Verifica permisos del micrófono
2. Habla más cerca del micrófono
3. Reduce el ruido de fondo

### ❌ Error instalando PyAudio

```bash
# En macOS
brew install portaudio
pip install pyaudio

# En Linux
sudo apt-get install portaudio19-dev
pip install pyaudio
```

## Cambiar el Modelo

```bash
# Ver modelos disponibles
ollama list

# Usar un modelo específico (línea de comandos)
./iniciar_voz.sh --modelo qwen3:14b

# Para la web, edita app_web.py o usa:
export QWEN_MODELO="qwen3:14b"
./iniciar_web.sh
```

## Ejemplos de Conversación

```
🎤 "¿Qué tiempo hace hoy en Madrid?"
🤖 [Responde con información sobre el clima]

🎤 "Explícame qué es Python"
🤖 [Explica Python en detalle]

🎤 "Cuéntame un chiste"
🤖 [Cuenta un chiste]

🎤 "Salir"
🤖 "Hasta luego, que tengas un buen día"
```

## Estructura del Proyecto

```
├── asistente_voz.py      → Versión de línea de comandos
├── app_web.py            → Servidor web Flask
├── templates/index.html  → Interfaz web
├── requirements.txt      → Dependencias de Python
├── instalar.sh          → Script de instalación
├── iniciar_voz.sh       → Inicia versión de línea de comandos
├── iniciar_web.sh       → Inicia interfaz web
└── README.md            → Documentación completa
```

## Consejos

💡 **Habla claramente** y cerca del micrófono
💡 **Evita ruido de fondo** para mejor reconocimiento
💡 **Frases cortas** funcionan mejor
💡 El modelo **mantiene contexto** entre preguntas
💡 Usa "limpiar historial" para empezar de cero

---

**¿Necesitas más ayuda?** Lee el README.md completo para información detallada.

