from lcd1602 import LCD1602
from time import sleep
from subprocess import *
import socket

print(socket.gethostbyname(socket.getfqdn()))

c = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

ip = run_cmd(c)

print('DEBUG: IP Address is ', ip)

lcd = LCD1602()

lcd.lcd_string("IP address", lcd.LCD_LINE_1)
lcd.lcd_string(ip, lcd.LCD_LINE_2)
