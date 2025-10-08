# 🚀 Guía Rápida: Compartir por Internet

## ⚡ Inicio Rápido (3 pasos)

### 1️⃣ Instalar Ngrok (solo primera vez)

```bash
brew install ngrok
```

### 2️⃣ Ejecutar el script

```bash
./compartir_asistente.sh
```

### 3️⃣ Compartir la URL

Verás algo como:
```
Forwarding: https://abc123.ngrok.io -> localhost:5002
```

**¡Esa es tu URL pública!** Compártela con quien quieras.

---

## 🎯 Opciones del Script

Cuando ejecutes `./compartir_asistente.sh`, verás:

```
1) Básico (sin contraseña)
2) Con contraseña (más seguro)
3) Limitar conexiones (máx 3 usuarios)
4) Contraseña + Límite de conexiones
```

### Opción 1: Básico
- Cualquiera con la URL puede acceder
- Perfecto para demos rápidas
- Sin restricciones

### Opción 2: Con Contraseña
- Pide usuario y contraseña
- Más seguro
- Controlas quién accede

**Ejemplo:**
```
Usuario: demo
Contraseña: password123

Comparte:
URL: https://abc123.ngrok.io
Usuario: demo
Contraseña: password123
```

### Opción 3: Limitar Conexiones
- Máximo 3 usuarios simultáneos
- Protege tus recursos
- Sin contraseña

### Opción 4: Contraseña + Límite
- Lo más seguro
- Máximo 3 usuarios
- Con autenticación

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Demo Rápida
```bash
./compartir_asistente.sh
# Selecciona: 1 (Básico)
# Comparte la URL que te da
```

### Ejemplo 2: Compartir con Equipo
```bash
./compartir_asistente.sh
# Selecciona: 2 (Con contraseña)
# Usuario: equipo
# Contraseña: mipassword123
# Comparte URL + credenciales
```

### Ejemplo 3: Demostración Pública
```bash
./compartir_asistente.sh
# Selecciona: 3 (Limitar conexiones)
# Comparte URL
# Solo 3 personas podrán usar a la vez
```

---

## 🔍 Verificar que Funciona

### Localmente:
```bash
# Abre en tu navegador
http://localhost:5002
```

### Por Internet:
```bash
# Abre la URL de ngrok en tu navegador
https://abc123.ngrok.io
```

---

## 🛑 Detener el Túnel

1. Presiona `Ctrl+C` en la terminal donde corre ngrok
2. El script preguntará si quieres detener el servidor
3. Responde `s` para detener o `n` para dejar corriendo

---

## ⚠️ Importante

### ✅ Debes tener:
- Computadora encendida
- Servidor corriendo
- Conexión a internet

### ⚠️ Consideraciones:
- **Recursos**: Cada usuario consume CPU/GPU
- **Límite**: Máximo 2-3 usuarios simultáneos recomendado
- **Velocidad**: Puede ser más lento que local
- **Privacidad**: Solo comparte con gente de confianza

---

## 🔒 Seguridad

### Si compartes con desconocidos:
```bash
# SIEMPRE usa opción 4 (con contraseña + límite)
./compartir_asistente.sh
# Opción: 4
```

### Si es solo para amigos/familia:
```bash
# Opción 2 o 3 está bien
./compartir_asistente.sh
# Opción: 2 o 3
```

### Si es demo rápida de 5 minutos:
```bash
# Opción 1 es suficiente
./compartir_asistente.sh
# Opción: 1
```

---

## 📱 Acceso desde Móvil

**¡SÍ funciona desde el móvil!**

1. Comparte la URL de ngrok
2. Abre en el navegador del móvil
3. Permite permisos de micrófono
4. **Nota**: La cámara no funciona en móvil (solo escritorio)

---

## 🐛 Problemas Comunes

### "ngrok: command not found"
```bash
# Instala ngrok
brew install ngrok
```

### "Port 5002 already in use"
```bash
# Detén el servidor anterior
pkill -f "python app_web.py"
# Vuelve a ejecutar
./compartir_asistente.sh
```

### "Connection refused"
```bash
# Verifica que el servidor esté corriendo
curl http://localhost:5002
```

### URL muy lenta
```bash
# Normal, depende de:
# - Tu conexión a internet
# - Distancia del usuario
# - Carga del servidor
```

---

## 💰 Versión Gratis vs Pago

### Ngrok Gratis:
- ✅ HTTPS automático
- ✅ Ilimitadas sesiones
- ⚠️ URL cambia cada vez
- ⚠️ Límite de conexiones: ~40/min

### Ngrok Pago ($8/mes):
- ✅ URL fija (personalizada)
- ✅ Sin límites de conexión
- ✅ Múltiples túneles
- ✅ Soporte técnico

**Recomendación**: Empieza con gratis, si usas mucho, upgrade.

---

## 🎓 Tips Profesionales

### 1. Monitorear Conexiones

Ngrok incluye un inspector web:
```
# Mientras ngrok corre, abre:
http://localhost:4040

# Verás:
# - Quién se conecta
# - Cuándo
# - Qué peticiones hace
```

### 2. Guardar la URL Temporalmente

```bash
# Copia la URL de ngrok
# Pégala en un archivo .txt
# O en un mensaje de WhatsApp/Telegram
```

### 3. Configuración Permanente

Si vas a compartir seguido, crea cuenta en ngrok:
```bash
# 1. Regístrate en https://dashboard.ngrok.com/signup
# 2. Copia tu authtoken
# 3. Autentica (una sola vez):
ngrok authtoken TU_TOKEN_AQUI
```

---

## 📊 Rendimiento Esperado

| Usuarios | Velocidad Local | Velocidad Remota |
|----------|----------------|------------------|
| 1 | ⚡⚡⚡⚡⚡ | ⚡⚡⚡⚡ |
| 2 | ⚡⚡⚡⚡ | ⚡⚡⚡ |
| 3 | ⚡⚡⚡ | ⚡⚡ |
| 4+ | ⚡⚡ | ⚡ |

---

## 🌟 Casos de Uso Reales

### Demo para Cliente
```bash
./compartir_asistente.sh
# Opción: 1 (Básico)
# Duración: 30 minutos
# Usuarios: 1-2
```

### Presentación en Clase
```bash
./compartir_asistente.sh
# Opción: 3 (Límite de conexiones)
# Duración: 1 hora
# Usuarios: 3
```

### Compartir con Amigos
```bash
./compartir_asistente.sh
# Opción: 2 (Con contraseña)
# Duración: Todo el día
# Usuarios: Conocidos
```

---

## ✅ Checklist Antes de Compartir

- [ ] Servidor funcionando localmente
- [ ] Ngrok instalado
- [ ] Script ejecutable (`chmod +x`)
- [ ] Computadora enchufada (no en batería)
- [ ] Buena conexión a internet
- [ ] Decidiste qué opción de seguridad usar

---

## 🎉 ¡Listo!

Tu asistente ahora puede ser usado desde **cualquier parte del mundo** 🌍

**Recuerda:** La URL de ngrok gratis cambia cada vez que reinicias el túnel.

---

**Documentación completa:** `COMPARTIR_INTERNET.md`

