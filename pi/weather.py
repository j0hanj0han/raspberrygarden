# Exemple de code Python pour lire les données du capteur BME680
import time
import board
import adafruit_bme680

# Configuration du capteur BME680 via I2C
i2c = board.I2C()  # Utilise les broches SCL et SDA par défaut
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

# Calibration de la température (optionnel)
bme680.sea_level_pressure = 1013.25

# Fonction pour lire les données du capteur
def read_sensor_data():
    return {
        "temperature": bme680.temperature,
        "humidity": bme680.relative_humidity,
        "pressure": bme680.pressure,
        "gas": bme680.gas,
        "altitude": bme680.altitude
    }

# Exemple d'utilisation
while True:
    data = read_sensor_data()
    print(f"Température: {data['temperature']}°C")
    print(f"Humidité: {data['humidity']}%")
    print(f"Pression: {data['pressure']} hPa")
    print(f"Qualité de l'air: {data['gas']} ohms")
    print(f"Altitude estimée: {data['altitude']} mètres")
    time.sleep(10)  # Lecture toutes les 10 secondes