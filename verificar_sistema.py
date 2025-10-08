#!/usr/bin/env python3
"""
Script para verificar que todos los componentes necesarios estén funcionando
"""

import sys

def verificar_imports():
    """Verifica que todas las librerías necesarias estén instaladas"""
    print("📦 Verificando librerías de Python...")
    
    modulos = {
        'speech_recognition': 'SpeechRecognition',
        'pyttsx3': 'pyttsx3',
        'requests': 'requests',
        'flask': 'Flask'
    }
    
    errores = []
    
    for modulo, nombre in modulos.items():
        try:
            __import__(modulo)
            print(f"  ✅ {nombre}")
        except ImportError:
            print(f"  ❌ {nombre} - NO INSTALADO")
            errores.append(nombre)
    
    return len(errores) == 0

def verificar_microfono():
    """Verifica que el micrófono esté disponible"""
    print("\n🎤 Verificando micrófono...")
    
    try:
        import speech_recognition as sr
        reconocedor = sr.Recognizer()
        
        # Intentar acceder al micrófono
        with sr.Microphone() as source:
            print("  ✅ Micrófono accesible")
            return True
    except Exception as e:
        print(f"  ❌ Error con el micrófono: {e}")
        print("\n  Posibles soluciones:")
        print("  - En macOS: Verifica permisos en Preferencias del Sistema")
        print("  - Instala PyAudio: brew install portaudio && pip install pyaudio")
        return False

def verificar_sintesis_voz():
    """Verifica que la síntesis de voz funcione"""
    print("\n🔊 Verificando síntesis de voz...")
    
    try:
        import pyttsx3
        motor = pyttsx3.init()
        print("  ✅ Motor de voz inicializado")
        
        voces = motor.getProperty('voices')
        print(f"  ✅ {len(voces)} voces disponibles")
        
        voces_espanol = [v for v in voces if 'spanish' in v.name.lower() or 'es' in v.languages]
        if voces_espanol:
            print(f"  ✅ {len(voces_espanol)} voz(ces) en español disponible(s)")
        else:
            print("  ⚠️  No se encontraron voces en español")
            print("     (Se usará la voz por defecto)")
        
        return True
    except Exception as e:
        print(f"  ❌ Error con síntesis de voz: {e}")
        return False

def verificar_ollama():
    """Verifica que Ollama esté corriendo y accesible"""
    print("\n🤖 Verificando Ollama...")
    
    try:
        import requests
        
        # Verificar conexión
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        
        if response.status_code == 200:
            print("  ✅ Ollama está corriendo")
            
            # Listar modelos
            modelos = response.json().get('models', [])
            if modelos:
                print(f"  ✅ {len(modelos)} modelo(s) disponible(s):")
                
                modelos_qwen = [m for m in modelos if 'qwen' in m['name'].lower()]
                if modelos_qwen:
                    for modelo in modelos_qwen:
                        nombre = modelo['name']
                        if 'qwen3:8b' in nombre:
                            print(f"     🎯 {nombre} ← Tu modelo configurado")
                        else:
                            print(f"     📦 {nombre}")
                else:
                    print("  ⚠️  No se encontraron modelos Qwen")
                    print("     Descarga uno con: ollama pull qwen3:8b")
            else:
                print("  ⚠️  No hay modelos instalados")
                print("     Descarga Qwen 3 con: ollama pull qwen3:8b")
            
            return True
        else:
            print(f"  ❌ Error al conectar con Ollama (código: {response.status_code})")
            return False
            
    except requests.exceptions.ConnectionError:
        print("  ❌ No se pudo conectar con Ollama")
        print("\n  Posibles soluciones:")
        print("  - Inicia Ollama: ollama serve")
        print("  - Verifica que esté instalado: ollama --version")
        return False
    except Exception as e:
        print(f"  ❌ Error inesperado: {e}")
        return False

def prueba_rapida():
    """Prueba rápida de reconocimiento de voz"""
    print("\n🧪 Prueba rápida (opcional)")
    
    respuesta = input("  ¿Quieres probar el micrófono? (s/n): ").lower()
    
    if respuesta == 's':
        try:
            import speech_recognition as sr
            reconocedor = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("\n  🎤 Di algo en 3 segundos...")
                reconocedor.adjust_for_ambient_noise(source, duration=0.5)
                
                try:
                    audio = reconocedor.listen(source, timeout=3, phrase_time_limit=5)
                    print("  🔄 Procesando...")
                    
                    texto = reconocedor.recognize_google(audio, language="es-ES")
                    print(f"  ✅ Escuché: '{texto}'")
                    
                except sr.WaitTimeoutError:
                    print("  ⏱️  No se detectó voz en 3 segundos")
                except sr.UnknownValueError:
                    print("  ❌ No se pudo entender el audio")
                    
        except Exception as e:
            print(f"  ❌ Error: {e}")

def main():
    """Función principal"""
    print("\n" + "="*60)
    print("🔍 VERIFICACIÓN DEL SISTEMA - QWEN 3 (8B)")
    print("="*60 + "\n")
    
    resultados = []
    
    # Ejecutar verificaciones
    resultados.append(("Librerías Python", verificar_imports()))
    resultados.append(("Micrófono", verificar_microfono()))
    resultados.append(("Síntesis de voz", verificar_sintesis_voz()))
    resultados.append(("Ollama", verificar_ollama()))
    
    # Prueba opcional
    prueba_rapida()
    
    # Resumen
    print("\n" + "="*60)
    print("📊 RESUMEN")
    print("="*60 + "\n")
    
    for componente, estado in resultados:
        icono = "✅" if estado else "❌"
        print(f"  {icono} {componente}")
    
    total_ok = sum(1 for _, estado in resultados if estado)
    total = len(resultados)
    
    print(f"\n  {total_ok}/{total} componentes funcionando correctamente")
    
    if total_ok == total:
        print("\n🎉 ¡Todo listo! Puedes usar el asistente de voz con Qwen 3 (8B).")
        print("\nPara comenzar:")
        print("  • Línea de comandos: ./iniciar_voz.sh")
        print("  • Interfaz web: ./iniciar_web.sh")
    else:
        print("\n⚠️  Algunos componentes necesitan atención.")
        print("   Revisa los errores arriba para solucionarlos.")
        print("\n📖 Consulta README.md para más ayuda")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()

