import os
import tempfile
from pathlib import Path
from dotenv import load_dotenv
import openai
import sounddevice as sd
import soundfile as sf
import numpy as np
import markdown
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import base64

# Cargar variables de entorno
load_dotenv()

# Configurar la clave API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Carpeta de salida
OUTPUT_FOLDER = "Comunicados"  # Puedes cambiar el nombre de la carpeta aquí
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def record_audio():
    print("Presiona Enter para comenzar a grabar...")
    input()
    print("Grabando... Presiona Enter para detener.")
    
    fs = 44100  # Frecuencia de muestreo
    duration = 600  # Duración máxima en segundos (10 minutos)
    
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    input()
    sd.stop()
    
    return recording, fs

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcription = openai.Audio.transcribe(
            model="whisper-1", 
            file=audio_file
        )
    return transcription["text"]

def generate_press_release(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": """Eres un periodista experto en escribir comunicados de prensa. 
            Escribe un comunicado de prensa en formato Markdown basado en la información proporcionada. 
            Usa la siguiente estructura:
             
            Escribe el comunicado de prensa primero en español y luego en inglés.
             
            Palabras clave (así es como se escriben estas palabras, en la transcripción están mal): Erick Rozo, Veneyorker, Fundavenyc

            # COMUNICADO DE PRENSA
            ## PARA PUBLICACIÓN INMEDIATA
            ### [Título del comunicado]

            **[Ciudad], [Fecha]** - [Primer párrafo con la información principal]

            [Cuerpo del comunicado en varios párrafos]

            [Párrafo de cierre]
             
           
            Para más información, visite [sitio web] o síganos en [redes sociales].

            **Contacto de prensa:** Carlos Egaña +1-917-499-9589 thecesifoundation@gmail.com

            Asegúrate de usar negritas, cursivas y otros elementos de Markdown para mejorar la estructura y legibilidad.
            Usa acentos y caracteres especiales del español correctamente."""},
            {"role": "user", "content": f"Escribe un comunicado de prensa en formato Markdown basado en la siguiente transcripción: {transcription}"}
        ]
    )
    return response.choices[0].message.content

def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_as_pdf(content, filename):
    # Convertir Markdown a HTML
    html_content = markdown.markdown(content, extensions=['extra'])
    
    # Obtener la imagen en base64
    logo_base64 = get_image_base64("logo.jpeg")
    
    # Añadir el logo al HTML
    html_with_logo = f"""
    <html>
        <body>
            <div class="logo">
                <img src="data:image/jpeg;base64,{logo_base64}" alt="Logo">
                </div>
                {html_content}
        </body>
    </html>
    """
    
    # Configurar fuentes
    font_config = FontConfiguration()
    
    # Crear CSS para el PDF
    css = CSS(string='''
        @page { size: letter; margin: 2cm }
        body { font-family: Arial, sans-serif; }
        h1 { color: #000000; font-size: 24px; }
        h2 { color: #000000; font-size: 20px; }
        h3 { color: #000000; font-size: 18px; }
        p { font-size: 12px; line-height: 1.5; }
        strong { font-weight: bold; }
        em { font-style: italic; }
        .logo {
            position: absolute;
            top: 0;
            right: 0;
            width: 100px;
            height: 100px;
        }
        .logo img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }
    ''', font_config=font_config)
    
    # Crear el PDF
    HTML(string=html_with_logo).write_pdf(filename, stylesheets=[css], font_config=font_config)

def main():
    print("Bienvenido al Generador de Comunicados de Prensa con IA")
    
    # Opción para grabar audio o subir archivo
    print("Selecciona una opción:")
    print("1. Grabar audio")
    print("2. Usar un archivo de audio existente")
    choice = input("Ingresa 1 o 2 y presiona Enter: ")
    
    if choice == "1":
        print("Preparando para grabar audio...")
        audio, fs = record_audio()
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            sf.write(temp_audio.name, audio, fs)
            audio_file_path = temp_audio.name
    elif choice == "2":
        audio_file_path = input("Ingresa la ruta completa del archivo de audio (por ejemplo, /Users/tu_usuario/archivo.wav): ")
    else:
        print("Opción no válida. Saliendo...")
        return
    
    print("Transcribiendo audio... Esto puede tomar unos minutos.")
    transcription = transcribe_audio(audio_file_path)
    
    print("Generando comunicado de prensa... Esto puede tomar unos minutos.")
    press_release = generate_press_release(transcription)
    
    output_filename = "comunicado_de_prensa"
    output_path = os.path.join(OUTPUT_FOLDER, f"{output_filename}.pdf")
    
    print(f"Guardando comunicado de prensa en {output_path}...")
    save_as_pdf(press_release, output_path)
    
    print(f"¡Listo! El comunicado de prensa se ha guardado en {output_path}")

if __name__ == "__main__":
    main()
