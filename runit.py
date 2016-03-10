from lcd1602 import LCD1602
from time import sleep

lcd = LCD1602()

lcd.lcd_string("Testing ....",lcd.LCD_LINE_1)
lcd.lcd_string("And it works!",lcd.LCD_LINE_2)

sleep(3)

lcd.cleanup()
