# Generador de Comunicados de Prensa con IA

Este proyecto utiliza OpenAI ChatGPT y Whisper para transcribir notas de voz o archivos de audio, y luego generar un comunicado de prensa basado en el contenido transcrito.

## Requisitos

- Python 3.8+
- pip
- virtualenv

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/generador-comunicados-prensa-ia.git
   cd generador-comunicados-prensa-ia
   ```

2. Crea un entorno virtual y actívalo:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` en la raíz del proyecto y añade tu API key de OpenAI:
   ```
   OPENAI_API_KEY="tu-api-key-aquí"
   ```

## Uso

Ejecuta el script principal:

```
python generate_press_release.py
```

Sigue las instrucciones en pantalla para grabar una nota de voz o subir un archivo de audio. El programa transcribirá el audio, generará un comunicado de prensa y lo guardará en un archivo PDF.

## Nota

Asegúrate de tener suficientes créditos en tu cuenta de OpenAI para usar los modelos GPT-4 y Whisper.