#!/bin/bash

# Script para iniciar la interfaz web

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ No se encontró el entorno virtual"
    echo "   Ejecuta primero: ./instalar.sh"
    exit 1
fi

echo "🚀 Iniciando interfaz web..."
echo "📱 Abre tu navegador en: http://localhost:5000"
echo ""

source venv/bin/activate
python app_web.py

