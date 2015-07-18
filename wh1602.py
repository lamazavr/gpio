from gpio import Gpio
from time import sleep

class Wh1602:
    def __init__(self):
        self.reserve_gpios()
        self.rw.set_value(0)
        sleep(0.05)

    def __del__(self):
        pass

    def reserve_gpios(self):
        self.rs = Gpio(2, "out")
        self.rw = Gpio(3, "out")
        self.e = Gpio(4, "out")
        self.d = [Gpio(17, "out"), Gpio(27, "out"),
                  Gpio(22, "out"), Gpio(23, "out")]

    def lcd_write_nibble(self, val):
        for i, p in enumerate(self.d):
            p.set_value(0 if (val & 1 << i) == 0 else 1)

        self.e.set_value(1)
        sleep(0.02)
        self.e.set_value(0)

    def lcd_write_data(self, data):
        self.lcd_write_nibble(data >> 4)
        self.lcd_write_nibble(data & 0xF)

    def init_lcd(self):
        self.rs.set_value(0)
        sleep(0.2)

        self.lcd_write_nibble(0x03)
        sleep(0.05)

        self.lcd_write_nibble(0x03)
        sleep(0.05)

        self.lcd_write_nibble(0x02)
        sleep(0.02)

        self.lcd_write_data(0x08)
        sleep(0.02)

        self.lcd_write_data(0x01)
        sleep(0.02)

        self.lcd_write_data(0x06)
        sleep(0.02)

        self.lcd_write_data(0x0D)
        sleep(0.02)

        self.rs.set_value(1)

    def lcd_write_string(self, str):
        for s in str:
            self.lcd_write_data(s)
