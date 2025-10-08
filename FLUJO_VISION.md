# 🔄 Flujo de Visión con Dos Modelos

## 📊 Sistema Implementado

Tu asistente ahora usa **dos modelos trabajando en conjunto**:

```
┌─────────────┐
│   Usuario   │
│  (habla +   │
│   cámara)   │
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────┐
│  1️⃣ LLAVA (Visión)                   │
│  - Recibe: Imagen de la cámara       │
│  - Analiza: Objetos o persona        │
│  - Retorna: Descripción breve        │
│  Ejemplo: "Un mouse inalámbrico     │
│  blanco sobre un escritorio"         │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│  2️⃣ QWEN 3 (Texto)                   │
│  - Recibe: Pregunta + Descripción    │
│  - Procesa: Contexto visual          │
│  - Retorna: Respuesta conversacional │
│  Ejemplo: "Es un mouse inalámbrico, │
│  útil para trabajar sin cables"      │
└──────────┬───────────────────────────┘
           │
           ▼
    ┌──────────────┐
    │   Respuesta  │
    │   en voz     │
    └──────────────┘
```

---

## 🎯 Cómo Funciona

### Con Imagen 📷/🖥️:

1. **Activas la cámara** o **compartes pantalla**
2. **Hablas tu pregunta**: "¿Qué es esto?"
3. **LLaVA interpreta la imagen**:
   - Si ve objetos → describe solo los objetos
   - Si solo ve persona → describe brevemente a la persona
   - Respuesta concisa (2-3 frases máximo)
4. **Qwen3 recibe**:
   ```
   [Contexto visual: Un mouse inalámbrico blanco sobre un escritorio]
   Pregunta del usuario: ¿Qué es esto?
   ```
5. **Qwen3 responde** de forma natural y conversacional

### Sin Imagen ⌨️:

1. **Hablas tu pregunta** (sin cámara/pantalla activa)
2. **Qwen3 responde directamente** como asistente normal

---

## 🔍 Ejemplos de Uso

### Ejemplo 1: Objeto en la mano

```
👤 Usuario: [Muestra un libro a la cámara]
         "¿Qué es esto?"

🤖 LLaVA: "Un libro de tapa dura con texto en la portada"

🧠 Qwen3: "Es un libro. Por la tapa dura, parece ser una 
          edición de calidad. ¿Necesitas información sobre 
          algún tema específico del libro?"
```

### Ejemplo 2: Pantalla con código

```
👤 Usuario: [Comparte pantalla con código Python]
         "¿Qué hace este código?"

🤖 LLaVA: "Código en Python con una función que usa un 
          bucle for"

🧠 Qwen3: "Este código define una función que itera sobre 
          elementos usando un bucle for. Parece estar 
          procesando una lista de datos..."
```

### Ejemplo 3: Solo persona (sin objetos)

```
👤 Usuario: [Solo aparece la persona frente a la cámara]
         "¿Qué ves?"

🤖 LLaVA: "Una persona sentada frente a la cámara"

🧠 Qwen3: "Veo a una persona sentada. ¿En qué puedo ayudarte?"
```

---

## ⚙️ Configuración Actual

| Componente | Modelo | Función |
|------------|--------|---------|
| **Visión** | `llava:7b` | Interpreta imágenes |
| **Texto** | `qwen3:8b` | Responde conversacionalmente |
| **Puerto** | `5002` | Servidor web |

---

## 💡 Prompts del Sistema

### Para LLaVA (Visión):
```
Describe brevemente y de forma puntual lo que ves en esta imagen.
Reglas:
- Si hay objetos, enfócate solo en ellos (ignora personas en ese caso)
- Si solo hay una persona y ningún objeto relevante, descríbela brevemente
- Sé conciso (máximo 2-3 frases)
- No des explicaciones largas, solo describe lo esencial
```

### Para Qwen3 (Texto):
```
[Contexto visual: {interpretación de LLaVA}]

Pregunta del usuario: {pregunta real}

Responde a la pregunta del usuario basándote en lo que se ve en la imagen.
Sé natural y conversacional.
```

---

## 🎮 Casos de Uso

### 1. Identificar Objetos
- "¿Qué es esto?"
- "¿Para qué sirve?"
- "¿Cómo se usa?"

### 2. Ayuda con Código
- "¿Qué hace este código?"
- "¿Hay algún error aquí?"
- "¿Cómo puedo mejorarlo?"

### 3. Explicar Diagramas
- "Explica este diagrama"
- "¿Qué significa esto?"
- "¿Cómo funciona?"

### 4. Asistencia General
- "Describe lo que ves"
- "¿Qué puedes decirme de esto?"
- "Ayúdame a entender esto"

---

## 🔧 Cambiar Modelos

### Modelo de Visión:
```bash
# Opciones disponibles
export VISION_MODELO="llava:7b"      # Por defecto
export VISION_MODELO="llava:13b"     # Mejor calidad
export VISION_MODELO="bakllava"      # Alternativa
```

### Modelo de Texto:
```bash
export QWEN_MODELO="qwen3:8b"        # Por defecto
export QWEN_MODELO="qwen3:14b"       # Más potente
```

Luego reinicia:
```bash
pkill -f "python app_web.py"
./iniciar_web.sh
```

---

## 📊 Rendimiento

| Operación | Tiempo Aproximado |
|-----------|-------------------|
| LLaVA interpreta imagen | ~5-10 segundos |
| Qwen3 genera respuesta | ~3-5 segundos |
| **Total** | **~8-15 segundos** |

*Tiempos pueden variar según hardware*

---

## 🐛 Depuración

Los mensajes en la terminal muestran el flujo:

```
🔍 Consultando a llava:7b para interpretar la imagen...
👁️ LLaVA vio: Un mouse inalámbrico blanco sobre un escritorio
💬 Consultando a qwen3:8b para la respuesta...
```

---

## ✨ Ventajas de Este Flujo

1. **Especialización**: Cada modelo hace lo que mejor sabe
   - LLaVA → Visión precisa
   - Qwen3 → Conversación natural

2. **Flexibilidad**: Puedes usar diferentes modelos sin cambiar código

3. **Contexto**: El historial se mantiene limpio (solo pregunta y respuesta)

4. **Eficiencia**: Solo se usa visión cuando hay imagen

---

## 🚀 Uso Rápido

```bash
# 1. Abre la interfaz
http://localhost:5002

# 2. Activa cámara
Clic en "📷 Cámara"

# 3. Haz clic en micrófono y habla
"¿Qué es esto?"

# 4. Escucha la respuesta
El sistema usa LLaVA + Qwen3 automáticamente
```

---

**¡Disfruta tu asistente de visión mejorado!** 👁️🤖

