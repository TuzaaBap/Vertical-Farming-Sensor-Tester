import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor

# Initialize DHT11 on GPIO20
dht_sensor = adafruit_dht.DHT11(board.D20)  # or board.GP20 depending on board lib version

# Initialize DS18B20 (1-Wire on GPIO21)
ds18b20_sensor = W1ThermSensor()

while True:
    try:
        # DS18B20 Temperature
        ds18b20_temp = ds18b20_sensor.get_temperature()

        # DHT11 Temp + Humidity
        dht_temp = dht_sensor.temperature
        dht_humidity = dht_sensor.humidity

        print("–––––– Digital Sensor Readings ––––––")
        print(f"DS18B20 Temp  : {ds18b20_temp:.2f} °C")
        print(f"DHT11 Temp    : {dht_temp} °C")
        print(f"DHT11 Humidity: {dht_humidity} %")
        print("–––––––––––––––––––––––––––––––––––––\n")

    except RuntimeError as e:
        print("Sensor read error:", e)

    time.sleep(2)
