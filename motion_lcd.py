from gpiozero import MotionSensor
import I2C_LCD_driver
import socket
import fcntl
import struct
import time

pir = MotionSensor(4)
mylcd = I2C_LCD_driver.lcd()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

mylcd.backlight(0)

while True:
    mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    mylcd.lcd_display_string(get_ip_address('eth0'), 2)
    pir.wait_for_motion()
    mylcd.backlight(1)
    time.sleep(5)
    mylcd.backlight(0)