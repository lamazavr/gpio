from gpio import Gpio, GpioDirection

if __name__ == "__main__":
    g = Gpio(37, GpioDirection.output)
    g.set_value(1)