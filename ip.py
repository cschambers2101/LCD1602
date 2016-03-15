
from subprocess import *
from lcd1602 import LCD1602
from time import sleep
import socket
import fcntl
import struct
import sys


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


ver = sys.version_info[0]
print('DEBUG: Running under Python V' + str(ver))

if ver == 2:
    ip = get_ip_address('wlan0')  # '192.168.0.110'
elif ver == 3:
    ip = 'Use Python V2'
print('DEBUG: IP Address is ' + str(ip))

lcd = LCD1602()

lcd.lcd_string("IP address", lcd.LCD_LINE_1)
lcd.lcd_string(ip, lcd.LCD_LINE_2)
