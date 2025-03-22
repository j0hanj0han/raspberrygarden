#!/usr/bin/env python3

import bme680
import time
import json
import sys

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
    except (RuntimeError, IOError) as e:
        print(json.dumps({"error": "Impossible de se connecter au capteur BME680: " + str(e)}))
        sys.exit(1)

# Configuration du capteur
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

try:
    if sensor.get_sensor_data():
        data = {
            "temperature": round(sensor.data.temperature, 2),
            "humidity": round(sensor.data.humidity, 2),
            "pressure": round(sensor.data.pressure, 2)
        }
        print(json.dumps(data))
    else:
        print(json.dumps({"error": "Impossible de lire les données du capteur"}))
        sys.exit(1)
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
