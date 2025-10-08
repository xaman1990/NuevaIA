# 🤖 Org-IA - Guía Completa

## ✨ Bienvenido a Org-IA

Tu asistente personal con visión, voz y lenguaje natural.

---

## 🎨 Nuevo Diseño

### Azul Marino Oscuro Premium
- 🌑 Fondo azul marino oscuro elegante
- 💎 Efectos de luz sutiles
- ✨ Gradientes modernos
- 🎯 Interfaz profesional

---

## 🚀 Inicio Rápido

### 1️⃣ Abrir la Interfaz

```bash
# El servidor ya está corriendo en:
http://localhost:5002
```

**Recarga la página** (Cmd + Shift + R) para ver el nuevo diseño

### 2️⃣ Usar Org-IA

1. **Haz clic en 🎤** para activar el micrófono
2. **Habla** tu pregunta
3. **Escucha** la respuesta
4. **Continúa** hablando (micrófono se reactiva solo)

### 3️⃣ Compartir por Internet

```bash
./compartir_cloudflare.sh
```

**Sin registro, sin límites, gratis**

---

## 🎯 Funciones Principales

### 💬 Conversación por Voz
- Habla en español
- Respuestas naturales
- Micrófono continuo
- Sin emoticonos en voz

### 👁️ Visión Multimodal
- **📷 Cámara**: Muestra objetos
- **🖥️ Pantalla**: Comparte código/imágenes
- **LLaVA** ve e interpreta
- **Qwen 3** responde naturalmente

### 🔄 Sistema de Doble Modelo

```
Tú muestras algo → LLaVA ve → Qwen 3 responde
```

**Lenguaje natural**: "Veo que estás mostrando..." (no "en la imagen...")

---

## 🎨 Paleta de Colores

| Elemento | Color |
|----------|-------|
| **Fondo** | Azul marino oscuro (#0a1628) |
| **Mensajes Usuario** | Azul brillante (#3b82f6) |
| **Mensajes Org-IA** | Azul oscuro (#1e3a5f) |
| **Acentos** | Azul claro (#60a5fa) |
| **Texto** | Blanco suave (#e0e7ff) |
| **Botón Activo** | Verde (#34d399) / Azul (#3b82f6) |

---

## 💡 Ejemplos de Uso

### Con Cámara 📷

```
1. Activa la cámara (botón 📷 se pone verde)
2. Muestra un objeto
3. Habla: "¿Qué es esto?"
4. Org-IA responde: "Veo que estás mostrando un libro..."
```

### Con Pantalla 🖥️

```
1. Comparte pantalla (botón 🖥️ se pone azul)
2. Muestra código
3. Habla: "¿Qué hace este código?"
4. Org-IA responde: "Veo que estás mostrando código Python..."
```

### Sin Imagen 💬

```
1. No actives cámara ni pantalla
2. Habla: "¿Qué es Python?"
3. Org-IA responde conversacionalmente
```

---

## 🌐 Compartir por Internet

### Método Rápido (Cloudflare - Sin Registro)

```bash
./compartir_cloudflare.sh
```

**Resultado:**
```
https://abc-123-def.trycloudflare.com
```

**Comparte esa URL** - Funciona desde cualquier dispositivo

### Ventajas:
- ✅ Sin registro
- ✅ Sin límites
- ✅ Gratis
- ✅ HTTPS automático

---

## 📊 Especificaciones Técnicas

| Componente | Especificación |
|------------|----------------|
| **Nombre** | Org-IA |
| **Modelo Visión** | LLaVA 7B |
| **Modelo Texto** | Qwen 3 8B |
| **Puerto** | 5002 |
| **Idioma** | Español |
| **Framework** | Flask + JavaScript |

---

## 🎮 Controles

| Botón | Función | Color Activo |
|-------|---------|--------------|
| 🎤 | Micrófono | Rojo |
| 📷 | Cámara | Verde |
| 🖥️ | Pantalla | Azul |
| 🗑️ | Limpiar | Gris |
| Enviar | Enviar mensaje | Azul |

---

## 🔧 Personalización

### Cambiar Nombre
Edita `templates/index.html` línea 393:
```html
<h1>🤖 Tu Nombre Aquí</h1>
```

### Cambiar Colores
Edita `templates/index.html` líneas 16-50 (sección de estilos)

### Cambiar Modelos
```bash
export VISION_MODELO="llava:13b"
export QWEN_MODELO="qwen3:14b"
```

---

## 📱 Compatibilidad

### Escritorio:
- ✅ Chrome (Recomendado)
- ✅ Edge
- ✅ Safari
- ⚠️ Firefox (sin reconocimiento de voz)

### Móvil:
- ✅ Voz funciona
- ⚠️ Cámara no disponible en móvil
- ✅ Chat de texto funciona

---

## 🐛 Solución de Problemas

### Diseño no se actualiza
```bash
# Recarga forzada en el navegador
Cmd + Shift + R (Mac)
Ctrl + Shift + R (Windows/Linux)
```

### Colores no se ven bien
```bash
# Limpia caché del navegador
# O abre en modo incógnito
```

### Servidor no inicia
```bash
# Verifica que no haya otro corriendo
pkill -f "python app_web.py"

# Reinicia
./iniciar_web.sh
```

---

## 📚 Archivos de Documentación

1. **ORG-IA_GUIA.md** ← Este archivo
2. **RESUMEN_FINAL.md** - Resumen completo del sistema
3. **FLUJO_VISION.md** - Explicación del flujo de visión
4. **LENGUAJE_NATURAL.md** - Cómo responde naturalmente
5. **CLOUDFLARE_TUNNEL.md** - Compartir por internet
6. **EMPIEZA_AQUI.md** - Guía de inicio

---

## 🎯 Características de Org-IA

### 🧠 Inteligencia
- Doble modelo (Visión + Texto)
- Contexto conversacional
- Respuestas naturales

### 👁️ Visión
- Ve objetos en tiempo real
- Interpreta pantallas
- Enfoque inteligente (objetos > personas)

### 🗣️ Voz
- Reconocimiento en español
- Síntesis natural
- Sin emoticonos en audio
- Micrófono continuo

### 🎨 Diseño
- Azul marino oscuro premium
- Interfaz moderna
- Responsive
- Efectos visuales sutiles

---

## ⚡ Comandos Rápidos

```bash
# Iniciar Org-IA
./iniciar_web.sh

# Compartir por internet
./compartir_cloudflare.sh

# Verificar sistema
source venv/bin/activate
python verificar_sistema.py

# Ver modelos instalados
ollama list
```

---

## 🌟 Tips Pro

1. **Mejor Calidad de Voz**:
   - Descarga voces premium de macOS
   - Preferencias → Accesibilidad → Contenido Hablado

2. **Mejor Visión**:
   - Usa buena iluminación para la cámara
   - Acerca objetos para mejor detalle

3. **Mejor Velocidad**:
   - Cierra aplicaciones pesadas
   - Conecta vía Ethernet si es posible

4. **Mejor Experiencia**:
   - Usa audífonos para evitar eco
   - Habla claro y a ritmo normal
   - Deja que termine de hablar antes de responder

---

## 🎊 ¡Disfruta Org-IA!

Tu asistente personal con:
- 👁️ Visión
- 🗣️ Voz
- 🧠 Inteligencia
- 🎨 Diseño premium

**URL:** http://localhost:5002

**Compartir:** `./compartir_cloudflare.sh`

---

**Versión:** 2.0 - Org-IA  
**Última actualización:** $(date)  
**Estado:** ✅ Completamente funcional

