class Gpio:
    def __init__(self):
        self.num = None

    def __init__(self, num, dir):
        self.export(num)
        self.set_direction(dir)

    #def __init__(self, num, dir, value):
    #    self.export(num)
    #    self.set_direction(dir)
    #    self.set_value(value)

    def __del__(self):
        with open("/sys/class/gpio/unexport", 'w') as f_export:
            f_export.write("{}".format(self.num))

    def export(self, num):
        self.num = num
        with open("/sys/class/gpio/export", 'w') as f_export:
            f_export.write("{}".format(num))

    def set_direction(self, dir):
        with open("/sys/class/gpio/gpio{}/direction".format(self.num), 'w') as f_direction:
            if dir == "in":
                f_direction.write("in")
            elif dir == "out":
                f_direction.write("out")

    def set_value(self,value):
        with open("/sys/class/gpio/gpio{}/value".format(self.num), 'w') as f_value:
            f_value.write("{}".format(value))

    def get_value(self):
        with open("/sys/class/gpio/gpio{}/value".format(self.num), 'r') as f_value:
            return f_value.read()
