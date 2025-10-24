import time
import board
import adafruit_dht

# Use GPIO20 (physical pin 38)
dht_sensor = adafruit_dht.DHT11(board.D20) # if using anyother pin change it to as per requirement 

while True:
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        print(f"DHT11 Temp: {temperature}°C | Humidity: {humidity}%")

    except RuntimeError as e:
        print("Sensor read error:", e)

    time.sleep(2)
