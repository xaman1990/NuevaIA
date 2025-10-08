# 🔧 Configurar Ngrok (Solución al Error de Autenticación)

## ❌ Error que Recibes

```
ERROR: authentication failed: Usage of ngrok requires a verified account and authtoken.
ERROR: Sign up for an account: https://dashboard.ngrok.com/signup
```

## ✅ Solución (5 minutos)

---

## 📝 Paso 1: Crear Cuenta en Ngrok (GRATIS)

1. **Abre tu navegador** y ve a:
   ```
   https://dashboard.ngrok.com/signup
   ```

2. **Regístrate** con:
   - Email
   - Google
   - GitHub

3. **Verifica tu email** (revisa tu bandeja de entrada)

---

## 🔑 Paso 2: Obtener tu Authtoken

1. **Inicia sesión** en: https://dashboard.ngrok.com/login

2. **Ve a la sección de authtoken**:
   ```
   https://dashboard.ngrok.com/get-started/your-authtoken
   ```

3. **Copia tu token** (se verá así):
   ```
   2abc123def456ghi789jkl_1MnOpQrStUvWxYz2AbCdEfG
   ```

---

## ⚙️ Paso 3: Configurar el Token

Abre tu terminal y ejecuta:

```bash
ngrok config add-authtoken TU_TOKEN_AQUI
```

**Ejemplo real:**
```bash
ngrok config add-authtoken 2abc123def456ghi789jkl_1MnOpQrStUvWxYz2AbCdEfG
```

**Deberías ver:**
```
Authtoken saved to configuration file: /Users/xmn/.ngrok2/ngrok.yml
```

---

## ✅ Paso 4: Probar que Funciona

```bash
./compartir_asistente.sh
```

O manualmente:
```bash
ngrok http 5002
```

**Si funciona, verás:**
```
Session Status    online
Account           tu_email@ejemplo.com
Forwarding        https://abc123.ngrok.io -> http://localhost:5002
```

---

## 🎉 ¡Listo!

Ahora puedes usar ngrok sin límites (en la versión gratuita).

---

## 📊 Límites de la Cuenta Gratuita

| Característica | Gratis | Pago |
|----------------|--------|------|
| Túneles simultáneos | 1 | Ilimitados |
| Conexiones/min | 40 | Ilimitadas |
| Dominios personalizados | ❌ | ✅ |
| URL fija | ❌ | ✅ |
| Túneles TCP | ❌ | ✅ |

**Para la mayoría de casos, gratis es suficiente.**

---

## 🐛 Solución de Problemas

### "Authtoken saved" pero sigue sin funcionar
```bash
# Verifica que el token esté configurado
cat ~/.ngrok2/ngrok.yml

# Debería mostrar:
authtoken: TU_TOKEN_AQUI
```

### "Invalid authtoken"
- Verifica que copiaste el token completo
- No debe tener espacios al inicio o final
- Cópialo de nuevo del dashboard

### "Account limit exceeded"
- Ya tienes un túnel corriendo
- Cierra ngrok y vuelve a intentar
- O upgrade a plan de pago

---

## 💡 Comandos Útiles

```bash
# Ver configuración actual
ngrok config check

# Ver dónde está el archivo de configuración
ngrok config show

# Eliminar configuración (si necesitas resetear)
rm ~/.ngrok2/ngrok.yml

# Volver a configurar
ngrok config add-authtoken TU_NUEVO_TOKEN
```

---

## 🔄 Alternativas (Si no Quieres Registrarte)

Si prefieres no registrarte en ngrok, puedes usar:

### Opción A: Cloudflare Tunnel (Sin Registro)
```bash
# Instalar
brew install cloudflared

# Usar
cloudflared tunnel --url http://localhost:5002
```

### Opción B: LocalTunnel (Sin Registro)
```bash
# Instalar
npm install -g localtunnel

# Usar
lt --port 5002
```

Ambas opciones son **completamente gratis** y **sin registro**.

---

## 📝 Resumen Rápido

```bash
# 1. Regístrate (gratis)
https://dashboard.ngrok.com/signup

# 2. Obtén tu token
https://dashboard.ngrok.com/get-started/your-authtoken

# 3. Configura
ngrok config add-authtoken TU_TOKEN_AQUI

# 4. Usa
./compartir_asistente.sh
```

---

**Tiempo total:** ~5 minutos

**Costo:** GRATIS

**Válido:** Para siempre

