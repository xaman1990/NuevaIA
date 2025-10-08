# 🌐 Compartir tu Asistente por Internet

## 🎯 Opciones Disponibles

Tienes varias formas de hacer accesible tu asistente desde internet.

---

## ⭐ Opción 1: Ngrok (Recomendado)

### ¿Qué es Ngrok?
Crea un túnel seguro HTTPS que expone tu servidor local a internet.

### Instalación:

```bash
# En macOS con Homebrew
brew install ngrok
```

### Uso Básico:

```bash
# 1. Inicia tu asistente normalmente
./iniciar_web.sh

# 2. En otra terminal, crea el túnel
ngrok http 5002
```

### Resultado:
```
Session Status                online
Account                       tu_cuenta
Version                       3.x.x
Region                        United States (us)
Forwarding                    https://abc123.ngrok.io -> http://localhost:5002
```

**URL pública**: `https://abc123.ngrok.io`

### Ventajas:
- ✅ HTTPS automático
- ✅ Muy fácil de usar
- ✅ Sin configurar router
- ✅ URL temporal (perfecto para demos)
- ✅ Gratis para uso básico

### Desventajas:
- ⚠️ URL cambia cada vez (gratis)
- ⚠️ Límite de conexiones (gratis)
- ⚠️ Se cierra al detener ngrok

### Versión Avanzada:

```bash
# Con dominio personalizado (requiere cuenta de pago)
ngrok http 5002 --domain=mi-asistente.ngrok.io

# Con autenticación básica
ngrok http 5002 --basic-auth="usuario:password"
```

---

## 🔷 Opción 2: Cloudflare Tunnel

### ¿Qué es?
Túnel gratuito de Cloudflare, similar a ngrok pero con más opciones.

### Instalación:

```bash
# macOS
brew install cloudflare/cloudflare/cloudflared
```

### Uso:

```bash
# 1. Inicia tu asistente
./iniciar_web.sh

# 2. Crea el túnel
cloudflared tunnel --url http://localhost:5002
```

### Ventajas:
- ✅ Completamente gratis
- ✅ Sin límites de conexiones
- ✅ Más rápido que ngrok
- ✅ HTTPS automático

### Desventajas:
- ⚠️ URL larga y difícil de recordar
- ⚠️ Configuración más compleja para dominios personalizados

---

## 🔸 Opción 3: LocalTunnel

### Instalación:

```bash
npm install -g localtunnel
```

### Uso:

```bash
# 1. Inicia tu asistente
./iniciar_web.sh

# 2. Crea el túnel
lt --port 5002
```

### Ventajas:
- ✅ Muy simple
- ✅ Gratis
- ✅ Código abierto

### Desventajas:
- ⚠️ Menos estable que ngrok
- ⚠️ A veces tiene problemas de conectividad

---

## 🏠 Opción 4: Port Forwarding en Router

### Para acceso permanente desde tu red:

**Pasos:**
1. Configura IP estática en tu Mac
2. Accede a tu router (usualmente 192.168.1.1)
3. Busca "Port Forwarding" o "NAT"
4. Crea regla:
   - Puerto externo: 5002
   - Puerto interno: 5002
   - IP: Tu Mac
   - Protocolo: TCP

**Acceso:**
- Necesitas tu IP pública: https://www.whatismyip.com
- URL: `http://TU_IP_PUBLICA:5002`

### Ventajas:
- ✅ Sin servicios externos
- ✅ Control total
- ✅ Gratis

### Desventajas:
- ❌ Sin HTTPS (a menos que configures certificado)
- ❌ Tu IP puede cambiar
- ❌ Expones tu red
- ❌ Requiere configuración del router

---

## 🚀 Opción 5: Desplegar en la Nube

### Servicios compatibles:

#### **Railway.app**
- ✅ Fácil de usar
- ✅ Plan gratuito
- ✅ HTTPS automático
- ⚠️ Requiere subir código

#### **Render.com**
- ✅ Plan gratuito
- ✅ HTTPS automático
- ⚠️ Se duerme después de inactividad

#### **DigitalOcean / AWS / Google Cloud**
- ✅ Control total
- ✅ Mejor rendimiento
- ❌ Requiere configuración
- ❌ Costos mensuales

---

## 📋 Guía Paso a Paso: Ngrok (Recomendado)

### 1. Instalar Ngrok

```bash
# Opción A: Con Homebrew
brew install ngrok

# Opción B: Descarga manual
# Ve a https://ngrok.com/download
```

### 2. Crear Cuenta (Opcional pero recomendado)

```bash
# Ve a https://dashboard.ngrok.com/signup
# Copia tu authtoken

# Autentica (una sola vez)
ngrok authtoken TU_TOKEN_AQUI
```

### 3. Iniciar tu Asistente

```bash
cd /Users/xmn/Documents/Trabajo/NuevaIA
./iniciar_web.sh
```

### 4. Crear Túnel

```bash
# En otra terminal
ngrok http 5002
```

### 5. Compartir

Verás algo así:
```
Forwarding    https://abc123.ngrok.io -> http://localhost:5002
```

**Comparte la URL**: `https://abc123.ngrok.io`

---

## ⚠️ Consideraciones de Seguridad

### 🔒 Importante:

1. **Ollama Local**: Tu modelo corre en TU computadora
   - Consume TU CPU/GPU
   - Consume TU ancho de banda
   - Necesitas dejar la computadora encendida

2. **Límites Recomendados**:
   ```bash
   # Limitar conexiones simultáneas
   ngrok http 5002 --max-conns=3
   
   # Agregar autenticación
   ngrok http 5002 --basic-auth="usuario:password123"
   ```

3. **Privacidad**:
   - El historial se guarda en memoria local
   - Las imágenes de cámara se procesan localmente
   - Usa túneles solo para demos o pruebas

4. **Rendimiento**:
   - Cada usuario extra consume recursos
   - Límite recomendado: 2-3 usuarios simultáneos
   - Respuestas más lentas con múltiples usuarios

---

## 🎯 Comparación Rápida

| Característica | Ngrok | Cloudflare | LocalTunnel | Port Forward |
|----------------|-------|------------|-------------|--------------|
| **Facilidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Gratis** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **HTTPS** | ✅ | ✅ | ✅ | ❌ |
| **Estabilidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Velocidad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Seguridad** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

---

## 💡 Recomendación por Caso de Uso

### 🎯 Para Demos/Pruebas Rápidas:
```bash
# Ngrok (más fácil)
brew install ngrok
ngrok http 5002
```

### 🎯 Para Compartir con Equipo:
```bash
# Ngrok con autenticación
ngrok http 5002 --basic-auth="equipo:password123"
```

### 🎯 Para Uso Personal Externo:
```bash
# Cloudflare Tunnel (gratis, sin límites)
brew install cloudflared
cloudflared tunnel --url http://localhost:5002
```

### 🎯 Para Producción:
- Despliega en Railway, Render, o servidor cloud
- Configura dominio propio
- Implementa autenticación robusta

---

## 🔧 Script de Inicio Automático

Crea un script para iniciar todo junto:

```bash
#!/bin/bash
# compartir_asistente.sh

echo "🚀 Iniciando asistente y túnel ngrok..."
echo ""

# Inicia el asistente en segundo plano
cd /Users/xmn/Documents/Trabajo/NuevaIA
source venv/bin/activate
python app_web.py &
SERVER_PID=$!

# Espera a que el servidor inicie
sleep 3

# Inicia ngrok
echo ""
echo "🌐 Creando túnel público..."
ngrok http 5002

# Al cerrar ngrok, cierra el servidor
kill $SERVER_PID
```

Uso:
```bash
chmod +x compartir_asistente.sh
./compartir_asistente.sh
```

---

## 📱 Ejemplo de Uso Real

### Escenario: Mostrar a un amigo

```bash
# 1. Inicia el asistente
./iniciar_web.sh

# 2. En otra terminal, crea el túnel
ngrok http 5002

# 3. Verás:
Forwarding: https://abc123.ngrok.io -> localhost:5002

# 4. Comparte la URL con tu amigo
# Le envías: "Ve a https://abc123.ngrok.io"

# 5. Tu amigo accede desde su navegador
# Puede usar el asistente de voz desde cualquier lugar
```

---

## ⚡ Tips y Trucos

### 1. **URL Personalizada** (Ngrok Pro):
```bash
ngrok http 5002 --domain=mi-asistente.ngrok.io
# URL fija: https://mi-asistente.ngrok.io
```

### 2. **Ver Tráfico**:
```bash
# Ngrok incluye inspector web
# Abre: http://localhost:4040
# Verás todas las peticiones HTTP
```

### 3. **Múltiples Túneles**:
```bash
# ngrok.yml
tunnels:
  asistente:
    proto: http
    addr: 5002
  api:
    proto: http
    addr: 8000
```

### 4. **Con Contraseña**:
```bash
ngrok http 5002 --basic-auth="admin:mipassword123"
# Los usuarios necesitan user/password
```

---

## 🐛 Solución de Problemas

### Ngrok dice "Tunnel not found":
```bash
# Asegúrate de estar autenticado
ngrok authtoken TU_TOKEN
```

### "Connection refused":
```bash
# Verifica que tu servidor esté corriendo
curl http://localhost:5002
```

### Túnel muy lento:
```bash
# Usa región más cercana
ngrok http 5002 --region=us
# Opciones: us, eu, ap, au, sa, jp, in
```

### Límite de conexiones alcanzado:
```bash
# Upgrade a cuenta de pago o usa Cloudflare Tunnel
cloudflared tunnel --url http://localhost:5002
```

---

## 📊 Costos Aproximados

| Servicio | Gratis | Básico | Pro |
|----------|--------|--------|-----|
| **Ngrok** | ✅ (con límites) | $8/mes | $20/mes |
| **Cloudflare Tunnel** | ✅ Ilimitado | ✅ Ilimitado | - |
| **LocalTunnel** | ✅ Todo gratis | - | - |
| **Railway** | ✅ $5 crédito | Pay-as-you-go | - |
| **Render** | ✅ (se duerme) | $7/mes | - |

---

## 🎉 Resumen

**Para empezar YA**:
```bash
# 1. Instala ngrok
brew install ngrok

# 2. Inicia tu asistente
./iniciar_web.sh

# 3. En otra terminal
ngrok http 5002

# 4. Comparte la URL que te da
```

**¡Listo! Tu asistente está en internet** 🌐

---

**Nota**: Recuerda que mientras el túnel esté activo, tu computadora debe estar encendida y ejecutando el servidor.

