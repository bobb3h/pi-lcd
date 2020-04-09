from gpiozero import MotionSensor
import I2C_LCD_driver

pir = MotionSensor(4)
mylcd = I2C_LCD_driver.lcd()

while True:
    pir.wait_for_motion()
    mylcd.backlight(1)
    pir.wait_for_no_motion()
    mylcd.backlight(0)