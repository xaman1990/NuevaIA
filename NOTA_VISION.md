# ⚠️ Nota Importante sobre Visión Multimodal

## 🎯 Funcionalidad Agregada

He agregado las siguientes características al asistente:

✅ **Filtro de emoticonos** - Ya no se leen los emoticonos en la síntesis de voz  
✅ **Captura de cámara web** - Botón 📷 Cámara  
✅ **Captura de pantalla** - Botón 🖥️ Pantalla  
✅ **Envío automático de imágenes** - Cuando hablas, se captura y envía la imagen actual

---

## ⚠️ Modelo con Visión Requerido

**Tu modelo actual: `qwen3:8b`**

Este modelo **NO tiene capacidades de visión**. Para que pueda "ver" y analizar imágenes de la cámara o pantalla, necesitas un modelo con capacidades multimodales (visión + texto).

### Opciones de modelos con visión:

1. **LLaVA** (recomendado para comenzar)
   ```bash
   ollama pull llava:7b
   # o la versión más reciente
   ollama pull llava:latest
   ```

2. **Qwen2-VL** (si existe en Ollama)
   ```bash
   ollama pull qwen2-vl:7b
   ```

3. **BakLLaVA**
   ```bash
   ollama pull bakllava
   ```

4. **LLaVA 13B** (mejor calidad, más recursos)
   ```bash
   ollama pull llava:13b
   ```

---

## 📝 Cambiar el Modelo

### Opción 1: Variable de entorno

```bash
export QWEN_MODELO="llava:7b"
./iniciar_web.sh
```

### Opción 2: Editar app_web.py

Abre `app_web.py` y cambia la línea 15:

```python
MODELO = os.environ.get('QWEN_MODELO', 'llava:7b')  # Cambiado de qwen3:8b
```

---

## 🧪 Probar la Funcionalidad

1. **Abre:** http://localhost:5002

2. **Activa la cámara:**
   - Haz clic en el botón "📷 Cámara"
   - Verás una vista previa del video

3. **Haz tu pregunta:**
   - Haz clic en el micrófono 🎤
   - Di: "¿Qué ves en la imagen?"
   - El sistema capturará un frame y lo enviará al modelo

4. **Compartir pantalla:**
   - Haz clic en "🖥️ Pantalla"
   - Selecciona qué ventana/pantalla compartir
   - Pregunta: "Describe lo que ves en la pantalla"

---

## 🔄 Qué Pasa Si Usas `qwen3:8b` (sin visión)

- ✅ El sistema funcionará normalmente para texto
- ✅ Capturará y enviará las imágenes
- ❌ El modelo ignorará las imágenes
- ❌ Solo responderá al texto de tu pregunta

**No habrá error, pero no verá las imágenes.**

---

## 📊 Comparación de Modelos

| Modelo | Visión | Tamaño | Velocidad | Calidad |
|--------|--------|--------|-----------|---------|
| qwen3:8b | ❌ | 8B | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| llava:7b | ✅ | 7B | ⚡⚡ | ⭐⭐⭐ |
| llava:13b | ✅ | 13B | ⚡ | ⭐⭐⭐⭐ |
| bakllava | ✅ | 7B | ⚡⚡ | ⭐⭐⭐ |

---

## 🚀 Guía Rápida de Instalación

```bash
# 1. Descargar modelo con visión
ollama pull llava:7b

# 2. Cambiar modelo
export QWEN_MODELO="llava:7b"

# 3. Reiniciar servidor (si está corriendo, detenerlo primero)
pkill -f "python app_web.py"
./iniciar_web.sh

# 4. Abrir navegador
# http://localhost:5002
```

---

## 💡 Casos de Uso

### Con Cámara 📷:
- "¿Qué objeto tengo en la mano?"
- "¿De qué color es mi camisa?"
- "Describe lo que ves"
- "¿Cuántos dedos estoy mostrando?"

### Con Pantalla 🖥️:
- "¿Qué código ves en pantalla?"
- "Explica este diagrama"
- "¿Qué error hay en este código?"
- "Describe esta imagen"

---

## ⚙️ Configuración Actual

Tu asistente está configurado con:
- ✅ Filtrado de emoticonos activado
- ✅ Captura de cámara disponible
- ✅ Captura de pantalla disponible
- ✅ Síntesis de voz mejorada
- ✅ Micrófono continuo
- ⚠️ Modelo sin visión (qwen3:8b)

**Para activar la visión completa, cambia a un modelo multimodal.**

---

**Creado:** $(date)  
**Puerto:** 5002  
**URL:** http://localhost:5002

