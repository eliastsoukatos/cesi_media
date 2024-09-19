# Generador de Comunicados de Prensa con IA

Este proyecto utiliza OpenAI ChatGPT y Whisper para transcribir notas de voz o archivos de audio, y luego generar un comunicado de prensa basado en el contenido transcrito.

## Requisitos

- Mac con macOS Sonoma (14.0 o superior)
- Conexión a Internet

## Instrucciones Paso a Paso

### 1. Instalar Homebrew (si no lo tienes)

Homebrew es un gestor de paquetes que facilita la instalación de software en macOS.

1. **Abrir Terminal:**
   - Haz clic en el icono de **Spotlight Search** (la lupa en la esquina superior derecha) o presiona **Command (⌘) + Espacio**.
   - Escribe `Terminal` y presiona **Enter**.

2. **Instalar Homebrew:**
   - Copia y pega el siguiente comando en la Terminal y presiona **Enter**:

     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

3. **Seguir las Instrucciones:**
   - Es posible que se te solicite ingresar tu contraseña. Mientras escribes, no verás caracteres en la pantalla; esto es normal.
   - Presiona **Enter** después de ingresar la contraseña.
   - Espera a que la instalación se complete.

### 2. Instalar Python 3

1. **Instalar Python 3:**

   ```bash
   brew install python@3.11
   ```

2. **Verificar la Instalación:**

   ```bash
   python --version
   ```

   Debería mostrar algo como `Python 3.11.x`.

   **Nota:** Después de instalar Python con Homebrew, el comando `python` apunta a Python 3.

### 3. Instalar Git (si no lo tienes)

1. **Instalar Git:**

   ```bash
   brew install git
   ```

2. **Verificar la Instalación:**

   ```bash
   git --version
   ```

   Debería mostrar algo como `git version 2.x.x`.

### 4. Clonar el Repositorio

1. **Elegir la Carpeta de Trabajo:**

   ```bash
   cd ~
   ```

2. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/eliastsoukatos/cesi_media.git
   ```

3. **Entrar en la Carpeta del Proyecto:**

   ```bash
   cd cesi_media
   ```

### 5. Crear un Entorno Virtual

1. **Crear el Entorno Virtual:**

   ```bash
   python -m venv venv
   ```

2. **Activar el Entorno Virtual:**

   ```bash
   source venv/bin/activate
   ```

   Deberías ver `(venv)` al principio de la línea en tu Terminal.

### 6. Instalar las Dependencias

1. **Actualizar `pip`:**

   ```bash
   pip install --upgrade pip
   ```

2. **Instalar las Dependencias del Proyecto:**

   ```bash
   pip install -r requirements.txt
   ```

   **Notas Importantes:**

   - **Si aparece un error relacionado con `portaudio` o `sounddevice`:**

     ```bash
     brew install portaudio
     ```

     Luego, vuelve a ejecutar:

     ```bash
     pip install -r requirements.txt
     ```

   - **Si aparece un error relacionado con `weasyprint` o `cairo`:**

     ```bash
     brew install cairo pango gdk-pixbuf libffi
     ```

     Luego, vuelve a ejecutar:

     ```bash
     pip install -r requirements.txt
     ```

### 7. Crear una Cuenta en OpenAI y Obtener una API Key

1. **Abrir el Navegador Web** y visitar [OpenAI](https://platform.openai.com/signup).

2. **Registrarse:**
   - Haz clic en **"Sign up"**.
   - Sigue las instrucciones para crear una cuenta.

3. **Obtener la API Key:**
   - Una vez registrado, ve a [API Keys](https://platform.openai.com/account/api-keys).
   - Haz clic en **"Create new secret key"**.
   - **Copia** la clave generada.

### 8. Crear el Archivo `.env`

1. **Asegurarte de Estar en la Carpeta del Proyecto:**

   ```bash
   cd ~/cesi_media
   ```

2. **Crear el Archivo `.env`:**

   ```bash
   nano .env
   ```

3. **Agregar la Clave API al Archivo:**
   - En el editor `nano`, escribe:

     ```
     OPENAI_API_KEY="tu-api-key-aquí"
     ```

     Reemplaza `"tu-api-key-aquí"` con la clave que copiaste.

4. **Guardar el Archivo:**
   - Presiona **Control + O** (letra O).
   - Presiona **Enter** para confirmar.

5. **Salir del Editor:**
   - Presiona **Control + X**.

### 9. Añadir el Logo (Opcional)

1. **Copiar la Imagen del Logo:**
   - Asegúrate de que la imagen esté en formato `.jpeg` y se llame `logo.jpeg`.

2. **Pegar la Imagen en la Carpeta del Proyecto:**

   ```bash
   cp /ruta/de/tu/logo.jpeg ~/cesi_media/logo.jpeg
   ```

   Reemplaza `/ruta/de/tu/logo.jpeg` con la ruta donde se encuentra tu imagen.

### 10. Ejecutar el Programa

1. **Activar el Entorno Virtual (si no está activo):**

   ```bash
   source venv/bin/activate
   ```

2. **Ejecutar el Script:**

   ```bash
   python main.py
   ```

3. **Seguir las Instrucciones en Pantalla:**
   - Elige **1** para grabar audio o **2** para usar un archivo existente.
   - Si grabas audio:
     - Presiona **Enter** para comenzar a grabar.
     - Habla claramente cerca del micrófono.
     - Presiona **Enter** nuevamente para detener la grabación.
   - Si usas un archivo existente:
     - Ingresa la ruta completa del archivo de audio cuando se te solicite.

4. **Esperar a que el Programa Termine:**
   - La transcripción y generación del comunicado pueden tardar varios minutos.

5. **Verificar el Comunicado Generado:**
   - El archivo `comunicado_de_prensa.pdf` se guardará en la carpeta `Comunicados` dentro del proyecto.

### 11. Abrir el Comunicado de Prensa

1. **Navegar hasta la Carpeta del Proyecto:**
   - Abre el **Finder**.
   - Ve a **Usuarios** > **tu_usuario** > **cesi_media** > **Comunicados**.

2. **Abrir el Archivo PDF:**
   - Haz doble clic en `comunicado_de_prensa.pdf` para abrirlo.

## Notas Adicionales

- **Permisos de Micrófono:**
  - Es posible que necesites otorgar permiso a la Terminal para acceder al micrófono.
  - Ve a **Preferencias del Sistema** > **Seguridad y Privacidad** > **Privacidad** > **Micrófono**.
  - Asegúrate de que **Terminal** esté seleccionada.

- **Créditos de OpenAI:**
  - Asegúrate de tener suficientes créditos en tu cuenta de OpenAI para utilizar los modelos GPT-4 y Whisper.

- **Ayuda Adicional:**
  - Si encuentras problemas, no dudes en contactarme para asistencia.

## Contacto

Si tienes preguntas o necesitas ayuda, puedes contactarme en [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com).

---

¡Disfruta creando comunicados de prensa con inteligencia artificial!

---

### `example.env`

Crea un archivo llamado `.env` y agrega lo siguiente:

```
OPENAI_API_KEY="tu-api-key-aquí"
```

Reemplaza `"tu-api-key-aquí"` con la clave API que obtuviste de OpenAI.

---