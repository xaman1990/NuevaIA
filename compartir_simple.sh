#!/bin/bash

# Script simple para compartir con Cloudflare Tunnel

echo ""
echo "🌐 COMPARTIR ORG-IA POR INTERNET"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Verificar si cloudflared está instalado
if ! command -v cloudflared &> /dev/null; then
    echo "❌ Cloudflared no está instalado"
    echo ""
    echo "Instala con: brew install cloudflared"
    exit 1
fi

echo "✅ Cloudflared instalado"
echo ""

# Verificar si el servidor está corriendo
if ! lsof -Pi :5002 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  El servidor no está corriendo"
    echo "🚀 Iniciando Org-IA..."
    echo ""
    
    cd "$(dirname "$0")"
    source venv/bin/activate
    nohup python app_web.py > /dev/null 2>&1 &
    
    sleep 5
    
    if ! lsof -Pi :5002 -sTCP:LISTEN -t >/dev/null ; then
        echo "❌ Error al iniciar el servidor"
        exit 1
    fi
    
    echo "✅ Servidor iniciado"
fi

echo "✅ Org-IA corriendo en http://localhost:5002"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🌐 Creando túnel público (puede tardar 10-15 segundos)..."
echo ""
echo "⚠️  NOTA: Verás un error 'Cannot determine default origin"
echo "    certificate path' - IGNÓRALO, es normal y no afecta."
echo ""
echo "📋 Busca la línea que dice:"
echo "    'Your quick Tunnel has been created!'"
echo "    Debajo estará tu URL pública (https://...)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⏳ Iniciando túnel..."
echo ""

# Ejecutar cloudflared
cloudflared tunnel --url http://localhost:5002 --no-autoupdate 2>&1 | grep -A1 "quick Tunnel has been created" --line-buffered &

# Guardar PID del proceso
TUNNEL_PID=$!

# Esperar y mostrar la URL
sleep 15

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ TÚNEL ACTIVO"
echo ""
echo "La URL pública aparece arriba (línea que empieza con https://)"
echo ""
echo "📋 COMPARTE ESA URL con quien quieras"
echo ""
echo "💡 MIENTRAS ESTO ESTÉ CORRIENDO:"
echo "   - Tu Org-IA es accesible desde internet"
echo "   - Tu computadora procesa todas las peticiones"
echo "   - Mantén esta ventana abierta"
echo ""
echo "🛑 Para DETENER: Presiona Ctrl+C"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Ejecutar cloudflared completo ahora (para que continúe corriendo)
kill $TUNNEL_PID 2>/dev/null
cloudflared tunnel --url http://localhost:5002 --no-autoupdate

# Al terminar (Ctrl+C)
echo ""
echo ""
read -p "¿Detener el servidor de Org-IA? (s/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Ss]$ ]]; then
    echo "🛑 Deteniendo servidor..."
    pkill -f "python app_web.py"
    echo "✅ Servidor detenido"
else
    echo "📝 Servidor sigue corriendo en http://localhost:5002"
fi

echo ""
echo "👋 ¡Hasta luego!"

