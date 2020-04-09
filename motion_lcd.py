from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver

pir = MotionSensor(4)
switchPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switchPin, GPIO.OUT)

while True:
    pir_wait_for_motion()
    GPIO.output(switchPin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(switchPin, GPIO.LOW)


