import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Define input channels
tds_channel = AnalogIn(ads, ADS.P0)  # TDS sensor on A0
ph_channel = AnalogIn(ads, ADS.P1)   # pH sensor on A1

# Calibration values (Adjust these based on real measurements)
TDS_CALIBRATION_FACTOR = 0.5  # Adjust based on testing
PH_NEUTRAL_VOLTAGE = 1.5      # Voltage at pH 7 (calibrate with buffer solution)
PH_SLOPE = -0.18              # pH sensitivity (volts per pH unit)

def read_tds(voltage):
    """Convert TDS voltage to ppm (Total Dissolved Solids)"""
    tds_value = (voltage / 5.0) * 1000 * TDS_CALIBRATION_FACTOR  # Scale to ppm
    return round(tds_value, 2)

def read_ph(voltage):
    """Convert pH sensor voltage to pH value"""
    ph_value = 7.0 + ((voltage - PH_NEUTRAL_VOLTAGE) / PH_SLOPE)
    return round(ph_value, 2)

while True:
    # Read voltages from ADS1115
    tds_voltage = tds_channel.voltage
    ph_voltage = ph_channel.voltage

    # Convert to meaningful values
    tds_value = read_tds(tds_voltage)
    ph_value = read_ph(ph_voltage)

    # Display results
    print(f"TDS: {tds_value} ppm | pH: {ph_value}")

    time.sleep(2)
