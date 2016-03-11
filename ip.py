from subprocess import *
from lcd1602 import LCD1602
from time import sleep

ip = Popen("ip addr show wlan0 | grep inet | awk '{print $2}' |cut -d -f1", shell=True, stdout=PIPE).communicate()[0]
print('DEBUG: ', ip)

lcd = LCD1602()

#lcd.lcd_string("IP address", lcd.LCD_LINE_1)
#lcd.lcd_string(ip, lcd.LCD_LINE_1)
