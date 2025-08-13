import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_as7341
from RPLCD.i2c import CharLCD

# --- LCD Setup ---
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, charmap='A00', auto_linebreaks=False)
lcd.clear()
lcd.backlight_enabled = True

# --- I2C Setup ---
i2c = busio.I2C(board.SCL, board.SDA)

# --- TDS & pH Setup ---
ads = ADS.ADS1115(i2c)
tds_channel = AnalogIn(ads, ADS.P0)
ph_channel = AnalogIn(ads, ADS.P1)

TDS_CALIBRATION_FACTOR = 7.26
PH_NEUTRAL_VOLTAGE = 1.5
PH_SLOPE = 0.6867
PH_OFFSET = -3.67

def read_tds(voltage):
    return round((voltage / 5.0) * 1000 * TDS_CALIBRATION_FACTOR, 2)

def read_ph(voltage):
    return round(7.0 + ((voltage - PH_NEUTRAL_VOLTAGE) / PH_SLOPE) + PH_OFFSET, 2)

# --- Wavelength (AS7341) ---
as7341 = adafruit_as7341.AS7341(i2c)

def get_percent(value, total):
    return round((value / total) * 100, 2) if total != 0 else 0

def read_680nm():
    clear = as7341.channel_clear
    return get_percent(as7341.channel_680nm, clear)

# --- Main Loop ---
while True:
    try:
        # Read sensors
        tds_voltage = tds_channel.voltage
        ph_voltage = ph_channel.voltage
        tds = read_tds(tds_voltage)
        ph = read_ph(ph_voltage)
        nm_680 = read_680nm()

        # Clear screen and write manually per line
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f"TDS  = {tds:.2f} ppm")

        lcd.cursor_pos = (1, 0)
        lcd.write_string(f"pH   = {ph:.2f}")

        lcd.cursor_pos = (2, 0)
        lcd.write_string(f"680nm = {nm_680:.2f}%")

        time.sleep(5)

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(5)