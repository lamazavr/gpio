from gpio import Gpio
from time import sleep

if __name__ == "__main__":
    g = Gpio(2, "out")
    while True:
        g.set_value(1)
        sleep(0.001)
        g.set_value(0)
        sleep(0.005)
