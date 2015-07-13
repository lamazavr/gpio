from gpio import Gpio, GpioDirection
from time import sleep

class Wh1602:
    def __init__(self):
        self.reserve_gpios()

    def __del__(self):
        pass

    def reserve_gpios(self):
        self.rs = Gpio(37, GpioDirection.output)
        self.e = Gpio(38, GpioDirection.output)
        self.d = [Gpio(39, GpioDirection.output), Gpio(39, GpioDirection.output),
                  Gpio(41, GpioDirection.output), Gpio(42, GpioDirection.output)]

    def lcd_write_nibble(self, val):
        for i, p in enumerate(self.d):
            p.set_value(0 if (val & 1 << i) == 0 else 1)

        self.e.set_value(1)
        sleep(0.02)
        self.e.set_value(0)

    def lcd_write_data(self, data):
        self.lcd_write_nibble(data & 0xF)
        self.lcd_write_nibble(data >> 4)

    def init_lcd(self):
        self.rs.set_value(0)
        sleep(0.2)

        self.lcd_write_nibble(0x30)
        sleep(0.05)

        self.lcd_write_nibble(0x30)
        sleep(0.05)

        self.lcd_write_nibble(0x28)
        sleep(0.02)

        self.lcd_write_nibble(0x08)
        sleep(0.02)

        self.lcd_write_nibble(0x01)
        sleep(0.02)

        self.lcd_write_nibble(0x06)
        sleep(0.02)

        self.lcd_write_nibble(0x0D)
        sleep(0.02)

        self.rs.set_value(1)

    def lcd_write_string(self, str):
        for s in str:
            self.lcd_write_data(s)