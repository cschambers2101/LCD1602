from subprocess import *
from lcd1602 import LCD1602
from time import sleep

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

ip = run_cmd(cmd)
#ip = Popen("ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d -f1", shell=True, stdout=PIPE).communicate()[0]
print('DEBUG: ', ip)

lcd = LCD1602()

lcd.lcd_string("IP address", lcd.LCD_LINE_1)
#lcd.lcd_string(ip, lcd.LCD_LINE_1)
