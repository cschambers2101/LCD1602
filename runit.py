from test import LCD1602

lcd = LCD1602()

lcd.lcd_string("Testing ....",lcd.LCD_LINE_1)
lcd.lcd_string("And it works!",lcd.LCD_LINE_2)