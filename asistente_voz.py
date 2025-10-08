#!/usr/bin/env python3
"""
Asistente de Voz con Qwen 3 usando Ollama
Este script permite conversar con el modelo mediante voz
"""

import speech_recognition as sr
import pyttsx3
import requests
import json
import sys
import time

class AsistenteVoz:
    def __init__(self, modelo="qwen3:8b"):
        """
        Inicializa el asistente de voz
        
        Args:
            modelo: Nombre del modelo en Ollama (por defecto: qwen3:8b)
        """
        self.modelo = modelo
        self.reconocedor = sr.Recognizer()
        self.motor_voz = pyttsx3.init()
        self.historial = []
        
        # Configurar voz en español
        voces = self.motor_voz.getProperty('voices')
        for voz in voces:
            if 'spanish' in voz.name.lower() or 'es' in voz.languages:
                self.motor_voz.setProperty('voice', voz.id)
                break
        
        # Ajustar velocidad de habla
        self.motor_voz.setProperty('rate', 150)
        
        print(f"✓ Asistente de voz inicializado con modelo: {self.modelo}")
    
    def escuchar(self):
        """
        Captura audio del micrófono y lo convierte a texto
        
        Returns:
            str: Texto reconocido o None si hay error
        """
        with sr.Microphone() as source:
            print("\n🎤 Escuchando... (habla ahora)")
            
            # Ajustar para ruido ambiente
            self.reconocedor.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = self.reconocedor.listen(source, timeout=5, phrase_time_limit=10)
                print("🔄 Procesando audio...")
                
                # Intentar reconocimiento en español
                texto = self.reconocedor.recognize_google(audio, language="es-ES")
                print(f"📝 Tú dijiste: {texto}")
                return texto
                
            except sr.WaitTimeoutError:
                print("⏱️  No se detectó voz. Intenta de nuevo.")
                return None
            except sr.UnknownValueError:
                print("❌ No se pudo entender el audio. Intenta hablar más claro.")
                return None
            except sr.RequestError as e:
                print(f"❌ Error en el servicio de reconocimiento: {e}")
                return None
    
    def hablar(self, texto):
        """
        Convierte texto a voz y lo reproduce
        
        Args:
            texto: Texto a convertir en voz
        """
        print(f"🤖 Qwen: {texto}")
        self.motor_voz.say(texto)
        self.motor_voz.runAndWait()
    
    def consultar_ollama(self, mensaje):
        """
        Envía un mensaje al modelo en Ollama y obtiene la respuesta
        
        Args:
            mensaje: Texto del mensaje
            
        Returns:
            str: Respuesta del modelo
        """
        try:
            url = "http://localhost:11434/api/chat"
            
            # Agregar mensaje al historial
            self.historial.append({
                "role": "user",
                "content": mensaje
            })
            
            payload = {
                "model": self.modelo,
                "messages": self.historial,
                "stream": False
            }
            
            print("⏳ Consultando a Qwen 3...")
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                resultado = response.json()
                respuesta = resultado['message']['content']
                
                # Agregar respuesta al historial
                self.historial.append({
                    "role": "assistant",
                    "content": respuesta
                })
                
                return respuesta
            else:
                return f"Error al comunicarse con Ollama: {response.status_code}"
                
        except requests.exceptions.ConnectionError:
            return "Error: No se pudo conectar con Ollama. ¿Está ejecutándose?"
        except Exception as e:
            return f"Error inesperado: {str(e)}"
    
    def limpiar_historial(self):
        """Limpia el historial de conversación"""
        self.historial = []
        print("🗑️  Historial limpiado")
    
    def conversacion(self):
        """
        Inicia una conversación continua por voz
        """
        print("\n" + "="*60)
        print("🎙️  ASISTENTE DE VOZ CON QWEN 3")
        print("="*60)
        print("\nComandos disponibles:")
        print("  - Di 'salir' o 'adiós' para terminar")
        print("  - Di 'limpiar historial' para resetear la conversación")
        print("  - Presiona Ctrl+C para salir en cualquier momento")
        print("\n" + "="*60)
        
        self.hablar("Hola, soy tu asistente de voz. ¿En qué puedo ayudarte?")
        
        while True:
            try:
                # Escuchar entrada del usuario
                texto = self.escuchar()
                
                if texto is None:
                    continue
                
                # Procesar comandos especiales
                texto_lower = texto.lower()
                
                if any(palabra in texto_lower for palabra in ['salir', 'adiós', 'chao', 'hasta luego']):
                    self.hablar("Hasta luego, que tengas un buen día")
                    break
                
                if 'limpiar historial' in texto_lower or 'borrar historial' in texto_lower:
                    self.limpiar_historial()
                    self.hablar("He limpiado el historial de nuestra conversación")
                    continue
                
                # Consultar al modelo
                respuesta = self.consultar_ollama(texto)
                
                # Hablar la respuesta
                self.hablar(respuesta)
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrumpido por el usuario")
                self.hablar("Hasta luego")
                break
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                continue

def main():
    """Función principal"""
    # Puedes cambiar el modelo aquí si usas otro
    # Por ejemplo: "qwen3:1.5b", "qwen3:14b", etc.
    
    import argparse
    parser = argparse.ArgumentParser(description='Asistente de voz con Qwen 3')
    parser.add_argument('--modelo', type=str, default='qwen3:8b',
                        help='Nombre del modelo en Ollama')
    args = parser.parse_args()
    
    try:
        asistente = AsistenteVoz(modelo=args.modelo)
        asistente.conversacion()
    except Exception as e:
        print(f"\n❌ Error al inicializar el asistente: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

