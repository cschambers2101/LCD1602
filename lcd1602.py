import time

class LCD1602:

    def __init__(self, board):

        self.pi = board
        # Define GPIO to LCD mapping
        self.LCD_RS = 7
        self.LCD_E  = 8
        self.LCD_D4 = 25
        self.LCD_D5 = 24
        self.LCD_D6 = 23
        self.LCD_D7 = 18

        # Define some device constants
        self.LCD_WIDTH = 16    # Maximum characters per line
        self.LCD_CHR = True
        self.LCD_CMD = False

        self.LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
        self.LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

        # Timing constants
        self.E_PULSE = 0.0005
        self.E_DELAY = 0.0005

        try:
            self.setup()
        except:
            print('ERROR!')
        finally:
            pass


    def cleanup(self):
        self.lcd_byte(0x01, self.LCD_CMD)
        self.lcd_string("Goodbye!",self.LCD_LINE_1)
        time.sleep(3)
        self.lcd_string("",self.LCD_LINE_1)
        self.lcd_string("",self.LCD_LINE_2)
        self.pi.GPIO.cleanup()

    def lcd_init(self):
      # Initialise display
      self.lcd_byte(0x33,self.LCD_CMD) # 110011 Initialise
      self.lcd_byte(0x32,self.LCD_CMD) # 110010 Initialise
      self.lcd_byte(0x06,self.LCD_CMD) # 000110 Cursor move direction
      self.lcd_byte(0x0C,self.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
      self.lcd_byte(0x28,self.LCD_CMD) # 101000 Data length, number of lines, font size
      # lcd_byte(0x01,LCD_CMD) # 000001 Clear display
      self.lcd_clear() # Clear display
      time.sleep(self.E_DELAY)

    def lcd_clear(self):
      self.lcd_byte(0x01,self.LCD_CMD) # 000001 Clear display
      time.sleep(self.E_DELAY)

    def lcd_byte(self, bits, mode):
      # Send byte to data pins
      # bits = data
      # mode = True  for character
      #        False for command

      self.pi.GPIO.output(self.LCD_RS, mode) # RS

      # High bits
      self.pi.GPIO.output(self.LCD_D4, False)
      self.pi.GPIO.output(self.LCD_D5, False)
      self.pi.GPIO.output(self.LCD_D6, False)
      self.pi.GPIO.output(self.LCD_D7, False)
      if bits&0x10==0x10:
        self.pi.GPIO.output(self.LCD_D4, True)
      if bits&0x20==0x20:
        self.pi.GPIO.output(self.LCD_D5, True)
      if bits&0x40==0x40:
        self.pi.GPIO.output(self.LCD_D6, True)
      if bits&0x80==0x80:
        self.pi.GPIO.output(self.LCD_D7, True)

      # Toggle 'Enable' pin
      self.lcd_toggle_enable()

      # Low bits
      self.pi.GPIO.output(self.LCD_D4, False)
      self.pi.GPIO.output(self.LCD_D5, False)
      self.pi.GPIO.output(self.LCD_D6, False)
      self.pi.GPIO.output(self.LCD_D7, False)
      if bits&0x01==0x01:
        self.pi.GPIO.output(self.LCD_D4, True)
      if bits&0x02==0x02:
        self.pi.GPIO.output(self.LCD_D5, True)
      if bits&0x04==0x04:
        self.pi.GPIO.output(self.LCD_D6, True)
      if bits&0x08==0x08:
        self.pi.GPIO.output(self.LCD_D7, True)

      # Toggle 'Enable' pin
      self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
      # Toggle enable
      time.sleep(self.E_DELAY)
      self.pi.GPIO.output(self.LCD_E, True)
      time.sleep(self.E_PULSE)
      self.pi.GPIO.output(self.LCD_E, False)
      time.sleep(self.E_DELAY)

    def lcd_string(self, message,line):
      # Send string to display

      message = message.ljust(self.LCD_WIDTH," ")

      self.lcd_byte(line, self.LCD_CMD)

      for i in range(self.LCD_WIDTH):
        self.lcd_byte(ord(message[i]),self.LCD_CHR)

    def setup(self):
      # Main program block
      self.pi.GPIO.setwarnings(False)
      self.pi.GPIO.setmode(self.pi.GPIO.BCM)       # Use BCM GPIO numbers
      self.pi.GPIO.setup(self.LCD_E, self.pi.GPIO.OUT)  # E
      self.pi.GPIO.setup(self.LCD_RS, self.pi.GPIO.OUT) # RS
      self.pi.GPIO.setup(self.LCD_D4, self.pi.GPIO.OUT) # DB4
      self.pi.GPIO.setup(self.LCD_D5, self.pi.GPIO.OUT) # DB5
      self.pi.GPIO.setup(self.LCD_D6, self.pi.GPIO.OUT) # DB6
      self.pi.GPIO.setup(self.LCD_D7, self.pi.GPIO.OUT) # DB7

      # Initialise display
      self.lcd_init()

if __name__ == '__main__':
    print('You are running from the class, create an instance to use!')
