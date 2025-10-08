#!/bin/bash

# Script para compartir el asistente usando Cloudflare Tunnel
# No requiere registro ni configuración

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║  🌐 COMPARTIR CON CLOUDFLARE TUNNEL (SIN REGISTRO)      ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Verificar si cloudflared está instalado
if ! command -v cloudflared &> /dev/null; then
    echo "❌ Cloudflared no está instalado"
    echo ""
    echo "Para instalarlo:"
    echo "  brew install cloudflared"
    exit 1
fi

echo "✅ Cloudflared encontrado"
echo ""

# Verificar si el servidor ya está corriendo
if lsof -Pi :5002 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  El servidor ya está corriendo en el puerto 5002"
    echo ""
    read -p "¿Quieres reiniciarlo? (s/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        echo "🔄 Deteniendo servidor anterior..."
        pkill -f "python app_web.py"
        sleep 2
    else
        echo "📝 Usando el servidor existente..."
    fi
fi

# Si el servidor no está corriendo, iniciarlo
if ! lsof -Pi :5002 -sTCP:LISTEN -t >/dev/null ; then
    echo "🚀 Iniciando servidor del asistente..."
    cd "$(dirname "$0")"
    source venv/bin/activate
    nohup python app_web.py > /dev/null 2>&1 &
    
    # Esperar a que el servidor inicie
    echo "⏳ Esperando a que el servidor inicie..."
    sleep 5
    
    # Verificar que inició correctamente
    if ! lsof -Pi :5002 -sTCP:LISTEN -t >/dev/null ; then
        echo "❌ Error: El servidor no pudo iniciarse"
        exit 1
    fi
    
    echo "✅ Servidor iniciado correctamente"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "🌐 Creando túnel público con Cloudflare..."
echo ""
echo "✨ VENTAJAS de Cloudflare Tunnel:"
echo "  ✅ Sin registro necesario"
echo "  ✅ Sin límites de conexiones"
echo "  ✅ Completamente gratis"
echo "  ✅ HTTPS automático"
echo ""
echo "⚠️  NOTA:"
echo "  - La URL será larga (tipo: abc-123-def.trycloudflare.com)"
echo "  - Tu computadora debe permanecer encendida"
echo "  - Presiona Ctrl+C para detener el túnel"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "🚀 Iniciando túnel..."
echo ""

# Ejecutar cloudflared en modo quick tunnel (sin autenticación)
cloudflared tunnel --url http://localhost:5002 --no-autoupdate

# Cuando se cierre cloudflared (Ctrl+C), preguntar si detener el servidor
echo ""
echo ""
read -p "¿Quieres detener el servidor del asistente? (s/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "🛑 Deteniendo servidor..."
    pkill -f "python app_web.py"
    echo "✅ Servidor detenido"
else
    echo "📝 El servidor sigue corriendo en http://localhost:5002"
fi

echo ""
echo "👋 ¡Hasta luego!"

