import time
import board
import busio
import adafruit_as7341

# Init I2C and sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_as7341.AS7341(i2c)

def get_percent(value, total):
    if total == 0:
        return 0
    return round((value / total) * 100, 2)

while True:
    clear = sensor.channel_clear
    nir = sensor.channel_nir  # optional

    print("–––––––––– Normalized % Spectral Values ––––––––––")
    print(f"415 nm : {get_percent(sensor.channel_415nm, clear)}%")
    print(f"445 nm : {get_percent(sensor.channel_445nm, clear)}%")
    print(f"480 nm : {get_percent(sensor.channel_480nm, clear)}%")
    print(f"515 nm : {get_percent(sensor.channel_515nm, clear)}%")
    print(f"555 nm : {get_percent(sensor.channel_555nm, clear)}%")
    print(f"590 nm : {get_percent(sensor.channel_590nm, clear)}%")
    print(f"630 nm : {get_percent(sensor.channel_630nm, clear)}%")
    print(f"680 nm : {get_percent(sensor.channel_680nm, clear)}%")
    print(f"Clear  : {clear} (reference)")
    print(f"NearIR : {get_percent(nir, clear)}% (IR component)")
    print("––––––––––––––––––––––––––––––––––––––––––––––––––\n")

    time.sleep(2)
