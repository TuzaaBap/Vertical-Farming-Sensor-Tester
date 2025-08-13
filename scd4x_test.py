import smbus2
import time
time.sleep(1.5)  # Wait 1.5s after powering before sending first command

# I2C Config
I2C_CHANNEL = 1
SCD4X_ADDRESS = 0x62
bus = smbus2.SMBus(I2C_CHANNEL)

def send_command(command):
    msb = (command >> 8) & 0xFF
    lsb = command & 0xFF
    bus.write_i2c_block_data(SCD4X_ADDRESS, msb, [lsb])

def read_measurement():
    try:
        bus.write_i2c_block_data(SCD4X_ADDRESS, 0xEC, [0x05])
        time.sleep(0.005)

        data = bus.read_i2c_block_data(SCD4X_ADDRESS, 0x00, 9)

        def parse_val(msb, lsb):
            return (msb << 8) | lsb

        co2 = parse_val(data[0], data[1])
        temp_raw = parse_val(data[3], data[4])
        rh_raw = parse_val(data[6], data[7])

        temp = -45 + (175 * temp_raw / 65536.0)
        humidity = 100 * rh_raw / 65536.0

        print(f"CO₂: {co2} ppm | Temp: {temp:.2f} °C | Humidity: {humidity:.2f} %")

    except Exception as e:
        print("Error reading data:", e)

def main():
    print("Starting SCD4x periodic measurement...")
    send_command(0x21B1)
    time.sleep(1)

    try:
        while True:
            read_measurement()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping...")
        send_command(0x3F86)

if __name__ == "__main__":
    main()
