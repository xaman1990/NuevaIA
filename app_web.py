#!/usr/bin/env python3
"""
Interfaz Web para el Asistente de Voz con Qwen 3
Permite conversar con el modelo desde el navegador
"""

from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Configuración
MODELO_TEXTO = os.environ.get('QWEN_MODELO', 'qwen3:8b')  # Modelo para respuestas de texto
MODELO_VISION = os.environ.get('VISION_MODELO', 'llava:7b')  # Modelo para interpretar imágenes
OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:11434')

# Almacenar historial de conversaciones (en memoria)
conversaciones = {}

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint para enviar mensajes al modelo
    
    Flujo:
    1. Si hay imagen: LLaVA interpreta → Qwen3 responde
    2. Si no hay imagen: Qwen3 responde directamente
    
    Espera JSON con:
        - mensaje: texto del mensaje
        - session_id: ID de sesión (opcional)
        - imagen: imagen en base64 (opcional)
    """
    try:
        data = request.json
        mensaje = data.get('mensaje', '')
        session_id = data.get('session_id', 'default')
        imagen_base64 = data.get('imagen', None)
        
        if not mensaje:
            return jsonify({'error': 'No se proporcionó mensaje'}), 400
        
        # Obtener o crear historial para esta sesión
        if session_id not in conversaciones:
            conversaciones[session_id] = []
        
        historial = conversaciones[session_id]
        
        # PASO 1: Si hay imagen, usar LLaVA para interpretarla
        interpretacion_vision = None
        if imagen_base64:
            # Limpiar el prefijo de data URL si existe
            if ',' in imagen_base64:
                imagen_base64 = imagen_base64.split(',')[1]
            
            # Prompt específico para LLaVA: conciso y enfocado en objetos
            prompt_vision = """Describe brevemente y de forma puntual lo que ves en esta imagen. 
Reglas:
- Si hay objetos, enfócate solo en ellos (ignora personas en ese caso)
- Si solo hay una persona y ningún objeto relevante, descríbela brevemente
- Sé conciso (máximo 2-3 frases)
- No des explicaciones largas, solo describe lo esencial"""
            
            # Consultar a LLaVA con la imagen
            url_vision = f"{OLLAMA_URL}/api/chat"
            payload_vision = {
                "model": MODELO_VISION,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_vision,
                        "images": [imagen_base64]
                    }
                ],
                "stream": False
            }
            
            print(f"🔍 Consultando a {MODELO_VISION} para interpretar la imagen...")
            response_vision = requests.post(url_vision, json=payload_vision, timeout=120)
            
            if response_vision.status_code == 200:
                resultado_vision = response_vision.json()
                interpretacion_vision = resultado_vision['message']['content']
                print(f"👁️ LLaVA vio: {interpretacion_vision}")
            else:
                return jsonify({
                    'error': f'Error al interpretar imagen: {response_vision.status_code}'
                }), 500
        
        # PASO 2: Construir mensaje para Qwen3
        if interpretacion_vision:
            # Si hubo interpretación de imagen, agregar contexto de forma natural
            mensaje_completo = f"""Estoy viendo que estás mostrando: {interpretacion_vision}

Tu pregunta es: {mensaje}

Responde como si estuvieras viendo directamente lo que muestras. Usa lenguaje natural y en primera persona, como "veo que estás mostrando...", "estás mostrando...", "puedo ver...". NO digas "en la imagen" o "la imagen muestra". Habla como si estuvieras presente mirando directamente."""
            
            # Agregar al historial el mensaje original del usuario (sin el contexto visual)
            historial.append({
                "role": "user",
                "content": mensaje
            })
        else:
            # Sin imagen, usar el mensaje tal cual
            mensaje_completo = mensaje
            historial.append({
                "role": "user",
                "content": mensaje
            })
        
        # PASO 3: Consultar a Qwen3 para la respuesta final
        url = f"{OLLAMA_URL}/api/chat"
        
        # Si hay interpretación visual, crear un mensaje temporal para Qwen3
        if interpretacion_vision:
            mensajes_para_qwen = historial[:-1] + [{
                "role": "user",
                "content": mensaje_completo
            }]
        else:
            mensajes_para_qwen = historial
        
        payload = {
            "model": MODELO_TEXTO,
            "messages": mensajes_para_qwen,
            "stream": False
        }
        
        print(f"💬 Consultando a {MODELO_TEXTO} para la respuesta...")
        response = requests.post(url, json=payload, timeout=120)
        
        if response.status_code == 200:
            resultado = response.json()
            respuesta = resultado['message']['content']
            
            # Agregar respuesta al historial
            historial.append({
                "role": "assistant",
                "content": respuesta
            })
            
            return jsonify({
                'respuesta': respuesta,
                'session_id': session_id,
                'interpretacion_vision': interpretacion_vision if interpretacion_vision else None
            })
        else:
            return jsonify({
                'error': f'Error de Ollama: {response.status_code}'
            }), 500
            
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout al consultar el modelo'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'No se pudo conectar con Ollama. ¿Está ejecutándose?'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/limpiar', methods=['POST'])
def limpiar():
    """Limpia el historial de una sesión"""
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        if session_id in conversaciones:
            conversaciones[session_id] = []
        
        return jsonify({'mensaje': 'Historial limpiado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/modelos', methods=['GET'])
def listar_modelos():
    """Lista los modelos disponibles en Ollama"""
    try:
        url = f"{OLLAMA_URL}/api/tags"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            modelos = response.json().get('models', [])
            return jsonify({'modelos': modelos})
        else:
            return jsonify({'error': 'No se pudieron obtener los modelos'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/estado', methods=['GET'])
def estado():
    """Verifica el estado de Ollama"""
    try:
        url = f"{OLLAMA_URL}/api/tags"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return jsonify({
                'estado': 'conectado',
                'modelo_texto': MODELO_TEXTO,
                'modelo_vision': MODELO_VISION
            })
        else:
            return jsonify({
                'estado': 'error',
                'mensaje': f'Código de estado: {response.status_code}'
            }), 500
    except requests.exceptions.ConnectionError:
        return jsonify({
            'estado': 'desconectado',
            'mensaje': 'No se pudo conectar con Ollama'
        }), 503
    except Exception as e:
        return jsonify({
            'estado': 'error',
            'mensaje': str(e)
        }), 500

if __name__ == '__main__':
    print("="*60)
    print("🌐 Iniciando servidor web del asistente de voz")
    print(f"💬 Modelo de texto: {MODELO_TEXTO}")
    print(f"👁️ Modelo de visión: {MODELO_VISION}")
    print(f"🔌 Ollama URL: {OLLAMA_URL}")
    print("="*60)
    print("\nFlujo de trabajo:")
    print("  1. Imagen → LLaVA interpreta")
    print("  2. Interpretación → Qwen3 responde")
    print("="*60)
    print("\n🚀 Abre tu navegador en: http://localhost:5002")
    print("\n")
    
    app.run(debug=True, host='0.0.0.0', port=5002)

