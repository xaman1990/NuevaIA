# 🚀 Empieza Aquí - Tu Asistente de Voz con Qwen 3 (8B)

## ✅ Tu Modelo Detectado

Has detectado que tienes **Qwen 3 versión 8B** instalado.  
Todos los archivos ya están configurados para usar: `qwen3:8b`

---

## 📋 Pasos Rápidos (3 minutos)

### 1️⃣ Instalar Dependencias

```bash
./instalar.sh
```

Este script:
- ✅ Verifica Python 3
- ✅ Detecta tu Qwen 3 (8B)
- ✅ Instala todas las dependencias
- ✅ Crea un entorno virtual
- ⏱️ Toma ~2 minutos

### 2️⃣ Verificar Sistema

```bash
source venv/bin/activate
python verificar_sistema.py
```

Esto comprobará:
- 📦 Librerías de Python
- 🎤 Micrófono
- 🔊 Síntesis de voz
- 🤖 Conexión con Ollama y tu modelo Qwen 3 (8B)

### 3️⃣ ¡Usar el Asistente!

**Opción A - Interfaz Web** (🌟 Recomendado)

```bash
./iniciar_web.sh
```

Luego abre: **http://localhost:5000**

- 💬 Chat visual bonito
- 🎤 Micrófono integrado
- ⌨️ También puedes escribir
- 📜 Historial de conversación

**Opción B - Línea de Comandos**

```bash
./iniciar_voz.sh
```

- 🎤 Conversación por terminal
- Comandos: "salir", "limpiar historial"

---

## 🎯 Ejemplo de Uso

```
🎤 Tú: "Hola Qwen, ¿cómo funciona Python?"

🤖 Qwen 3: "Python es un lenguaje de programación de alto nivel..."

🎤 Tú: "Dame un ejemplo de función"

🤖 Qwen 3: "Claro, aquí tienes un ejemplo..."

🎤 Tú: "Gracias, salir"

🤖 Qwen 3: "Hasta luego, que tengas un buen día"
```

---

## ⚠️ Solución Rápida de Problemas

### Error: "No se pudo conectar con Ollama"

```bash
# En otra terminal, ejecuta:
ollama serve
```

### Error: "No se detectó voz"

1. Verifica permisos del micrófono en Preferencias del Sistema
2. Habla más cerca del micrófono
3. Reduce el ruido de fondo

### Error instalando PyAudio

```bash
brew install portaudio
pip install pyaudio
```

---

## 📊 Tu Configuración Actual

| Componente | Configuración |
|-----------|---------------|
| **Modelo** | `qwen3:8b` |
| **Ubicación** | `/Users/xmn/.ollama/models/` |
| **URL Ollama** | `http://localhost:11434` |
| **Idioma** | Español (es-ES) |

---

## 🎨 Características

✅ **Reconocimiento de voz** en español  
✅ **Síntesis de voz** natural  
✅ **Interfaz web moderna** con diseño bonito  
✅ **Historial contextual** - recuerda la conversación  
✅ **Dos modos**: Terminal o Web  
✅ **Fácil de usar** - scripts listos para ejecutar  

---

## 📁 Estructura del Proyecto

```
NuevaIA/
├── 🚀 EMPIEZA_AQUI.md       ← Estás aquí
├── 📄 LEEME_PRIMERO.txt     ← Guía visual
├── 📄 INICIO_RAPIDO.md      ← Guía detallada
├── 📄 README.md             ← Documentación completa
│
├── 🔧 instalar.sh           ← Instalador automático
├── 🔍 verificar_sistema.py  ← Verificador del sistema
│
├── 🚀 iniciar_voz.sh        ← Inicia modo terminal
├── 🚀 iniciar_web.sh        ← Inicia modo web
│
├── 🐍 asistente_voz.py      ← Asistente de voz (terminal)
├── 🐍 app_web.py            ← Servidor web Flask
│
└── 📁 templates/
    └── index.html           ← Interfaz web bonita
```

---

## 💡 Consejos Pro

1. **Primera vez**: Usa la interfaz web, es más fácil
2. **Habla claro**: Di frases completas cerca del micrófono
3. **Sin ruido**: Reduce el ruido de fondo para mejor reconocimiento
4. **Contexto**: El modelo recuerda la conversación, aprovéchalo
5. **Reiniciar**: Di "limpiar historial" para empezar de nuevo

---

## 🎓 Comandos Útiles

```bash
# Ver qué modelos tienes
ollama list

# Verificar que Ollama está corriendo
curl http://localhost:11434/api/tags

# Activar entorno virtual
source venv/bin/activate

# Desactivar entorno virtual
deactivate
```

---

## 🆘 Necesitas Ayuda?

1. 📖 Lee `README.md` para documentación completa
2. 📖 Consulta `INICIO_RAPIDO.md` para guía paso a paso
3. 🔍 Ejecuta `verificar_sistema.py` para diagnosticar problemas

---

## 🎉 ¡Listo!

Tu asistente está configurado para usar **Qwen 3 (8B)**.

**Para empezar ahora:**

```bash
./iniciar_web.sh
```

Luego abre: http://localhost:5000 y empieza a conversar! 🎤

---

**Creado con ❤️ para conversar con tu Qwen 3 local**

