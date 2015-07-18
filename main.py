from gpio import Gpio
from time import sleep
from wh1602 import Wh1602

if __name__ == "__main__":
	wh = Wh1602()
	wh.init_lcd()
	#r = input()
	wh.lcd_write_string(b'hello')
