# 🎙️ Asistente de Voz con Qwen 3

Este proyecto te permite conversar con tu modelo Qwen 3 local usando voz, tanto por línea de comandos como a través de una interfaz web moderna.

## 🌟 Características

- ✅ **Conversación por voz**: Habla con tu modelo y escucha sus respuestas
- ✅ **Reconocimiento de voz**: Convierte tu voz a texto automáticamente
- ✅ **Síntesis de voz**: El asistente responde con voz natural
- ✅ **Interfaz web moderna**: Diseño limpio y responsivo
- ✅ **Línea de comandos**: Opción para usar desde la terminal
- ✅ **Historial de conversación**: Mantiene el contexto de la charla
- ✅ **Compatible con cualquier modelo de Ollama**

## 📋 Requisitos Previos

1. **Ollama instalado y corriendo** en tu máquina
2. **Python 3.8 o superior**
3. **Modelo Qwen 3** descargado en Ollama

### Verificar que Ollama está funcionando:

```bash
# Verificar si Ollama está corriendo
curl http://localhost:11434/api/tags

# Ver tus modelos instalados
ollama list
```

Si no tienes Qwen 3 instalado:

```bash
# Descargar Qwen 3 (ejemplo con versión 8B)
ollama pull qwen3:8b

# O la versión 14B si tienes más memoria
ollama pull qwen3:14b
```

## 🚀 Instalación

### 1. Instalar dependencias

```bash
# Instalar las dependencias de Python
pip install -r requirements.txt

# En macOS, también necesitas instalar portaudio:
brew install portaudio
```

**Nota para macOS**: Si tienes problemas con PyAudio, instálalo así:

```bash
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/opt/homebrew/include' --global-option='-L/opt/homebrew/lib' pyaudio
```

### 2. Dar permisos de micrófono

En macOS, ve a:
**Preferencias del Sistema → Seguridad y Privacidad → Privacidad → Micrófono**

Asegúrate de dar permiso a Terminal o tu aplicación de Python.

## 💻 Uso

### Opción 1: Línea de Comandos

La forma más sencilla de empezar:

```bash
# Ejecutar con el modelo por defecto
python asistente_voz.py

# Especificar un modelo diferente
python asistente_voz.py --modelo qwen2.5:7b
```

**Comandos de voz disponibles:**
- "Salir", "Adiós", "Chao" → Termina la conversación
- "Limpiar historial" → Reinicia la conversación
- Ctrl+C → Salir en cualquier momento

### Opción 2: Interfaz Web

Para una experiencia más visual:

```bash
# Iniciar el servidor web
python app_web.py
```

Luego abre tu navegador en: **http://localhost:5000**

**Características de la interfaz web:**
- 💬 Chat visual con historial
- 🎤 Botón de micrófono para grabar audio
- ⌨️ También puedes escribir mensajes
- 🗑️ Botón para limpiar la conversación
- 🔊 Reproducción automática de respuestas por voz

### Configurar variables de entorno (opcional)

```bash
# Cambiar el modelo (si tienes otra versión)
export QWEN_MODELO="qwen3:14b"

# Cambiar la URL de Ollama (si no está en localhost)
export OLLAMA_URL="http://192.168.1.100:11434"

# Ejecutar la app web
python app_web.py
```

## 🎯 Ejemplos de Uso

### Conversación de ejemplo:

```
🎤 Tú: "Hola, ¿quién eres?"
🤖 Qwen: "Soy Qwen, un modelo de lenguaje desarrollado por Alibaba Cloud..."

🎤 Tú: "¿Puedes explicarme qué es Python?"
🤖 Qwen: "Python es un lenguaje de programación de alto nivel..."

🎤 Tú: "Salir"
🤖 Qwen: "Hasta luego, que tengas un buen día"
```

## 🛠️ Solución de Problemas

### El micrófono no funciona

1. Verifica los permisos del micrófono en tu sistema
2. Prueba grabando algo con otra app para confirmar que funciona
3. En macOS, reinicia Terminal después de dar permisos

### Error: "No se pudo conectar con Ollama"

1. Verifica que Ollama está corriendo:
   ```bash
   ollama list
   ```
2. Si no está corriendo, inícialo:
   ```bash
   ollama serve
   ```

### PyAudio no se instala

En macOS:
```bash
brew install portaudio
pip install pyaudio
```

En Linux:
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

### No hay voz en español

El sistema intentará encontrar una voz en español automáticamente. Si no funciona:

1. En macOS: Ve a Preferencias del Sistema → Accesibilidad → Contenido Hablado
2. Descarga voces en español (como "Mónica" o "Paulina")

### La voz web no funciona en el navegador

- La síntesis de voz web funciona mejor en Chrome/Edge
- Safari también la soporta pero con menos voces
- Firefox tiene soporte limitado

## 📱 Compatibilidad

### Navegadores (para interfaz web):
- ✅ Chrome/Chromium (Recomendado)
- ✅ Edge
- ✅ Safari (funcionalidad limitada)
- ⚠️ Firefox (sin reconocimiento de voz)

### Sistemas Operativos:
- ✅ macOS (Probado)
- ✅ Linux
- ✅ Windows (requiere configuración adicional)

## 🎨 Personalización

### Cambiar la velocidad de la voz (línea de comandos)

Edita `asistente_voz.py` línea 40:

```python
# Más rápido: 200, Más lento: 100
self.motor_voz.setProperty('rate', 150)
```

### Cambiar el modelo

```bash
# Por línea de comandos (si tienes otra versión)
python asistente_voz.py --modelo qwen3:14b

# Para la web, edita app_web.py o usa variable de entorno
export QWEN_MODELO="qwen3:14b"
```

### Ajustar el tiempo de escucha

Edita `asistente_voz.py` línea 53:

```python
# timeout: tiempo máximo esperando que hables
# phrase_time_limit: tiempo máximo de grabación
audio = self.reconocedor.listen(source, timeout=5, phrase_time_limit=10)
```

## 📚 Estructura del Proyecto

```
NuevaIA/
├── asistente_voz.py      # Script de línea de comandos
├── app_web.py            # Servidor Flask para interfaz web
├── requirements.txt      # Dependencias
├── README.md            # Este archivo
├── templates/
│   └── index.html       # Interfaz web
└── static/              # (vacío por ahora)
```

## 🤝 Contribuir

Si encuentras algún bug o tienes sugerencias, ¡son bienvenidas!

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## ⭐ Consejos Útiles

1. **Habla claramente** cerca del micrófono
2. **Evita ruidos de fondo** para mejor reconocimiento
3. **Frases cortas** funcionan mejor que párrafos largos
4. El modelo **mantiene contexto**, así que puedes hacer preguntas de seguimiento
5. Usa "limpiar historial" si quieres empezar una conversación nueva

## 📞 Soporte

Si tienes problemas:

1. Revisa la sección de "Solución de Problemas"
2. Verifica que Ollama está corriendo: `ollama list`
3. Comprueba los logs en la terminal
4. Asegúrate de tener todos los permisos necesarios

---

¡Disfruta conversando con tu asistente de voz! 🎉

