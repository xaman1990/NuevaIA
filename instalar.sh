#!/bin/bash

echo "================================"
echo "🎙️  Instalador del Asistente de Voz"
echo "================================"
echo ""

# Verificar Python
echo "📦 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    echo "   Instálalo con: brew install python3"
    exit 1
fi
echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Verificar Ollama
echo "🔍 Verificando Ollama..."
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama no está instalado"
    echo "   Descárgalo desde: https://ollama.ai"
    exit 1
fi
echo "✅ Ollama encontrado"
echo ""

# Verificar que Ollama está corriendo
echo "🔌 Verificando conexión con Ollama..."
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✅ Ollama está corriendo"
else
    echo "⚠️  Ollama no está corriendo"
    echo "   Ejecútalo con: ollama serve"
    echo "   (en otra terminal)"
fi
echo ""

# Verificar modelos Qwen
echo "📋 Buscando modelos Qwen..."
MODELOS=$(ollama list | grep -i qwen | awk '{print $1}')
if [ -z "$MODELOS" ]; then
    echo "⚠️  No se encontraron modelos Qwen"
    echo "   Descarga uno con:"
    echo "   ollama pull qwen3:8b"
    echo ""
    read -p "¿Quieres descargar qwen3:8b ahora? (s/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        ollama pull qwen3:8b
    fi
else
    echo "✅ Modelos Qwen encontrados:"
    echo "$MODELOS" | while read modelo; do
        echo "   - $modelo"
    done
fi
echo ""

# Instalar PortAudio (necesario para PyAudio)
echo "🔧 Instalando dependencias del sistema..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    if command -v brew &> /dev/null; then
        echo "   Instalando portaudio..."
        brew install portaudio 2>/dev/null || echo "   (portaudio ya instalado)"
    else
        echo "⚠️  Homebrew no encontrado. Instálalo desde: https://brew.sh"
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "   Instalando portaudio..."
    sudo apt-get update
    sudo apt-get install -y portaudio19-dev python3-pyaudio
else
    echo "⚠️  Sistema operativo no reconocido"
fi
echo ""

# Crear entorno virtual
echo "🐍 Creando entorno virtual..."
if [ -d "venv" ]; then
    echo "   (entorno virtual ya existe)"
else
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
fi
echo ""

# Activar entorno virtual e instalar dependencias
echo "📦 Instalando dependencias de Python..."
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip > /dev/null 2>&1

# Instalar dependencias
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencias instaladas correctamente"
else
    echo "❌ Hubo un error al instalar las dependencias"
    echo "   Intenta manualmente: source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi
echo ""

echo "================================"
echo "✨ ¡Instalación completada!"
echo "================================"
echo ""
echo "Para usar el asistente:"
echo ""
echo "1️⃣  Línea de comandos:"
echo "   source venv/bin/activate"
echo "   python asistente_voz.py"
echo ""
echo "2️⃣  Interfaz web:"
echo "   source venv/bin/activate"
echo "   python app_web.py"
echo "   Luego abre: http://localhost:5000"
echo ""
echo "📖 Lee el README.md para más información"
echo ""

