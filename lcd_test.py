from RPLCD.i2c import CharLCD
import time

# Adjust based on your display size
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, charmap='A00', auto_linebreaks=True)

lcd.clear()

while True:
    lcd.home()
    lcd.write_string("AVFFM Sensor Hub")
    lcd.crlf()
    lcd.write_string("CO2, pH, TDS, Light")
    lcd.crlf()
    lcd.write_string("Temp+Hum: Live")
    lcd.crlf()
    lcd.write_string(" Let's Glrow ")
    time.sleep(5)

    lcd.clear()
    lcd.write_string("...Updating...")
    time.sleep(1)
