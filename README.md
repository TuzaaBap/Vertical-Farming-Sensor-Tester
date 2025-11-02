# Vertical Farming Sensor Tester

Collection of individual **sensor test scripts** for Raspberry Pi–based vertical-farming rigs.
Each script runs standalone, prints live readings to the terminal/CLI, and helps you validate wiring, drivers, and calibration before integrating into bigger systems.

## What’s inside

- Quick, one-file tests for common hydroponics sensors and modules
- Clean terminal output for fast bring-up and debugging
- Optional MQTT publish hooks and a simple Flask demo for dashboards

## Supported modules (by script)

- `ads1115_test.py` — ADS1115 test
- `as7341_test.py` — AS7341 test
- `dht11_test.py` — DHT11 test
- `digital_temp_humidity.py` — DIGITAL TEMP HUMIDITY test
- `display.py` — DISPLAY test
- `lcd_test.py` — LCD test
- `relay.py` — RELAY test
- `scd4x_test.py` — SCD4X test

## Hardware target
- Raspberry Pi 3/4/5 (tested on Pi 3 for LCD/MQTT demo; Pi 5 for dashboard)
- I²C-enabled sensors and basic GPIO (relays, LED, etc.)

## Quick start

```bash
# 1) Clone
git clone https://github.com/TuzaaBap/Vertical-Farming-Sensor-Tester.git
cd Vertical-Farming-Sensor-Tester

# 2) (Recommended) Create venv
python3 -m venv .venv && source .venv/bin/activate

# 3) Install deps (pick only what you need)
pip install adafruit-circuitpython-ads1x15 adafruit-circuitpython-as7341 adafruit-circuitpython-dht \
            adafruit-circuitpython-busdevice smbus2 RPi.GPIO board paho-mqtt flask \
            scd4x

# 4) Enable I2C on Raspberry Pi (raspi-config)
sudo raspi-config  # Interfacing Options → I2C → Enable

# 5) Run a sensor test (examples)
python ads1115_test.py      # TDS/pH via ADS1115 (ADC)
python as7341_test.py       # Spectral sensor
python dht11_test.py        # Temp/Humidity (1-wire like timing)
python scd4x_test.py        # CO₂/Temp/Humidity
python lcd_test.py          # I²C 16x2/20x4 LCD rotation
python relay.py             # Toggle relay(s) change the relay pins 'nano relay.py'
python display.py           # CLI display helper/demo
```

> Tip: If a library import fails, install the exact library for that script and retry.

### Optional: MQTT

Set environment variables and run any script with MQTT publishing enabled (see inline flags if present).

```bash
export MQTT_HOST=localhost
export MQTT_PORT=1883
export MQTT_TOPIC=avffm/sensors
```
Integrate with your existing broker (e.g., Mosquitto) or forward to a Pi 5 dashboard.



## Wiring notes (quick)
- **AS7341**: I²C (SDA/SCL, 3V3, GND)
- **ADS1115**: I²C; connect analog signal from **TDS/pH** sensor interface to A0–A3
- **DHT11**: 3V3, GND, Data (with 10k pull-up to 3V3 recommended)
- **SCD4x**: I²C
- **LCD (PCF8574 backpack)**: I²C
- **Relay**: VCC, GND, IN → Pi GPIO (mind active-low modules)

## Calibrations
- **pH/TDS**: Use buffer solutions / known TDS standards; adjust scaling factors in `ads1115_test.py`.
- **Spectral (AS7341)**: Normalize counts and record dark current; consider integration time and gain.
- **CO₂ (SCD4x)**: Perform forced recalibration per vendor docs if available.



## License
MIT — see `LICENSE`.
- Free for personal and educational use. Attribution appreciated.
