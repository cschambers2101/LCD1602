from subprocess import *
from lcd1602 import LCD1602
from time import sleep

import socket
import fcntl
import struct

def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

ip= getHwAddr('wlan0')
#ip = Popen("ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d -f1", shell=True, stdout=PIPE).communicate()[0]
print('DEBUG: ', ip)

lcd = LCD1602()

lcd.lcd_string("IP address", lcd.LCD_LINE_1)
#lcd.lcd_string(ip, lcd.LCD_LINE_1)
