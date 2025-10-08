#!/bin/bash

# Script para compartir el asistente por internet usando ngrok

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║     🌐 COMPARTIR ASISTENTE POR INTERNET                 ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Verificar si ngrok está instalado
if ! command -v ngrok &> /dev/null; then
    echo "❌ Ngrok no está instalado"
    echo ""
    echo "Para instalarlo:"
    echo "  brew install ngrok"
    echo ""
    echo "O descarga desde: https://ngrok.com/download"
    exit 1
fi

echo "✅ Ngrok encontrado"
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
else
    # Iniciar el servidor
    echo "🚀 Iniciando servidor del asistente..."
    cd "$(dirname "$0")"
    source venv/bin/activate
    nohup python app_web.py > /dev/null 2>&1 &
    SERVER_PID=$!
    
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

# Preguntar por opciones de ngrok
echo "Opciones de compartir:"
echo ""
echo "  1) Básico (sin contraseña)"
echo "  2) Con contraseña (más seguro)"
echo "  3) Limitar conexiones (máx 3 usuarios)"
echo "  4) Contraseña + Límite de conexiones"
echo ""
read -p "Selecciona una opción (1-4): " opcion

# Construir comando de ngrok
NGROK_CMD="ngrok http 5002"

case $opcion in
    2)
        read -p "Usuario: " usuario
        read -sp "Contraseña: " password
        echo ""
        NGROK_CMD="ngrok http 5002 --basic-auth='$usuario:$password'"
        ;;
    3)
        NGROK_CMD="ngrok http 5002 --max-conns=3"
        ;;
    4)
        read -p "Usuario: " usuario
        read -sp "Contraseña: " password
        echo ""
        NGROK_CMD="ngrok http 5002 --basic-auth='$usuario:$password' --max-conns=3"
        ;;
esac

echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "🌐 Creando túnel público con ngrok..."
echo ""
echo "La URL pública aparecerá a continuación."
echo "Compártela con quien quieras que acceda al asistente."
echo ""
echo "⚠️  IMPORTANTE:"
echo "  - Tu computadora debe permanecer encendida"
echo "  - El servidor consumirá recursos por cada usuario"
echo "  - Presiona Ctrl+C para detener el túnel"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""

# Ejecutar ngrok
eval $NGROK_CMD

# Cuando se cierre ngrok (Ctrl+C), preguntar si detener el servidor
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

