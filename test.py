#import


class LCD1602:

    import RPi.GPIO as GPIO
    import time

    # Define GPIO to LCD mapping
    LCD_RS = 7
    LCD_E  = 8
    LCD_D4 = 25
    LCD_D5 = 24
    LCD_D6 = 23
    LCD_D7 = 18

    # Define some device constants
    LCD_WIDTH = 16    # Maximum characters per line
    LCD_CHR = True
    LCD_CMD = False

    LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

    # Timing constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005

    def __init__(self):
        try:
            self.setup()
        except:
            print('ERROR!')
        finally:
            pass


    def cleanup(self):
        self.lcd_byte(0x01, LCD_CMD)
        self.lcd_string("Goodbye!",LCD_LINE_1)
        time.sleep(3)
        self.lcd_string("",LCD_LINE_1)
        self.lcd_string("",LCD_LINE_2)
        GPIO.cleanup()

    def lcd_init(self):
      # Initialise display
      self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
      self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
      self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
      self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
      self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
      # lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      self.lcd_clear() # Clear display
      time.sleep(E_DELAY)

    def lcd_clear(self):
      self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      time.sleep(E_DELAY)

    def lcd_byte(self, bits, mode):
      # Send byte to data pins
      # bits = data
      # mode = True  for character
      #        False for command

      GPIO.output(LCD_RS, mode) # RS

      # High bits
      GPIO.output(LCD_D4, False)
      GPIO.output(LCD_D5, False)
      GPIO.output(LCD_D6, False)
      GPIO.output(LCD_D7, False)
      if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
      if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
      if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
      if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)

      # Toggle 'Enable' pin
      self.lcd_toggle_enable()

      # Low bits
      GPIO.output(LCD_D4, False)
      GPIO.output(LCD_D5, False)
      GPIO.output(LCD_D6, False)
      GPIO.output(LCD_D7, False)
      if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
      if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
      if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
      if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)

      # Toggle 'Enable' pin
      self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
      # Toggle enable
      time.sleep(E_DELAY)
      GPIO.output(LCD_E, True)
      time.sleep(E_PULSE)
      GPIO.output(LCD_E, False)
      time.sleep(E_DELAY)

    def lcd_string(self, message,line):
      # Send string to display

      message = message.ljust(LCD_WIDTH," ")

      self.lcd_byte(line, LCD_CMD)

      for i in range(LCD_WIDTH):
        self.lcd_byte(ord(message[i]),LCD_CHR)

    def setup(self):
      # Main program block
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
      GPIO.setup(LCD_E, GPIO.OUT)  # E
      GPIO.setup(LCD_RS, GPIO.OUT) # RS
      GPIO.setup(LCD_D4, GPIO.OUT) # DB4
      GPIO.setup(LCD_D5, GPIO.OUT) # DB5
      GPIO.setup(LCD_D6, GPIO.OUT) # DB6
      GPIO.setup(LCD_D7, GPIO.OUT) # DB7

      # Initialise display
      self.lcd_init()

if __name__ == '__main__':
    print('You are running from the class, create an instance to use!')


