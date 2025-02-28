# IoT-Parcial1-Temperatura

## Descripción del Proyecto
El proyecto consiste en utilizar un Raspberry Pi Pico W junto con un sensor LM35 para registrar temperaturas a intervalos regulares y enviar las lecturas a un canal en ThingSpeak.

## Instrucciones de Instalación y uso

### Paso 1: Clonar el repositorio
   Clona el repositorio con el siguiente comando:
   ```bash
   git clone https://github.com/ElStoico/IoT-Parcial1-Temperatura.git
   ```
### Paso 2: Crear un canal en ThingSpeak

1. Ve a [ThingSpeak](https://thingspeak.mathworks.com) y crea un canal.
2. Accede a la sección de "API Keys" de tu canal y copia la "Write API Key".

### Paso 3: Modificar el archivo `main.py`

1. Abre el archivo `main.py` con Thonny.
2. Modifica los siguientes campos en el código:
   - **SSID**: Reemplázalo con el nombre de tu red.
   - **PASSWORD**: Coloca la contraseña de tu red.
   - **API_KEY**: Pega la **Write API Key** del canal de ThingSpeak que copiaste en el paso anterior.

### Paso 4: Guardar el archivo en tu Raspberry Pi Pico W

1. Conecta tu **Raspberry Pi Pico W** a tu computadora.
2. Guarda el archivo `main.py` en el almacenamiento de la Raspberry Pi Pico W desde Thonny.

### Paso 5: Conectar el sensor LM35

Realiza las siguientes conexiones entre el sensor LM35 y tu Raspberry Pi Pico W:

- **VCC (LM35)** → **3.3V (Pico W)**
- **GND (LM35)** → **GND (Pico W)**
- **VOUT (LM35)** → **GP26/ADC0 (Pico W)**

### Paso 6: Iniciar la recolección de muestras

Conecta tu Raspberry Pi Pico W a una fuente de energía adecuada para comenzar a recolectar las muestras.

