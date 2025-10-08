#!/bin/bash

# Script para iniciar el asistente de voz por línea de comandos

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ No se encontró el entorno virtual"
    echo "   Ejecuta primero: ./instalar.sh"
    exit 1
fi

source venv/bin/activate
python asistente_voz.py "$@"

