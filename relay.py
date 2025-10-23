import RPi.GPIO as GPIO
import time

# Relay GPIO pins
relay_pins = [16, 12, 28, 23]  # change this relay pins according to your requirement

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configure pins as output and turn OFF all relays initially
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # LOW = OFF for active HIGH

try:
    print("Turning ON all relays (motors start)")
    for pin in relay_pins:
        GPIO.output(pin, GPIO.HIGH)  # HIGH = ON
    time.sleep(40)

    print("Turning OFF all relays (motors stop)")
    for pin in relay_pins:
        GPIO.output(pin, GPIO.LOW)  # LOW = OFF

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Ensure everything is OFF before exiting
    for pin in relay_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
