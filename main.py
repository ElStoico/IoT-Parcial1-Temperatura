import network
import urequests
import machine
import utime

# 🚀 Configurar Wi-Fi
SSID = "tu red" # Escribir el nombre de la red entre las comillas
PASSWORD = "tu contraseña" # Lo mismo pero con la contraseña de la red

# 🌍 Configuración de ThingSpeak
API_KEY = "tu clave de escritura api de thingspeak"
URL = "https://api.thingspeak.com/update?api_key=" + API_KEY #Url, no cambiar, solo cambiar API_KEY

# 🎛️ Configuración del ADC
lm35 = machine.ADC(26)  # GP26 = ADC0
conversion_factor = 3.3 / 65535 

# 📡 Conectar a Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

# Esperar conexión
print("Conectando a Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    utime.sleep(1)
print("\nConectado! IP:", wlan.ifconfig()[0])

def leer_temperatura():
    lectura = lm35.read_u16() * conversion_factor  # Convertimos la lectura a voltaje
    temperatura = lectura * 100  # Convertimos voltaje a °C (10mV por grado)
    return round(temperatura, 2)

while True:
    temperatura = leer_temperatura()
    print(f"📡 Enviando temperatura: {temperatura}°C")

    # 📡 Enviar datos a ThingSpeak
    response = urequests.get(URL + f"&field1={temperatura}")
    print("✅ Respuesta:", response.text)
    response.close()

    # ⏳ Esperar 160 segundos antes de la siguiente medición
    utime.sleep(160)