class CarPart:
    def __init__(self, serial: str, unbroken: bool = True):
        self._serial = serial
        self._unbroken = unbroken

    def get_state(self):
        return self._unbroken


# 'ligths', 'abs','wheels'
class Motor(CarPart):
    def __init__(self, serial: str, unbroken: bool = True):
        super().__init__(serial, unbroken)
        self._name = 'motor'


class Lights(CarPart):
    def __init__(self, serial: str, unbroken: bool = True):
        super().__init__(serial,  unbroken)
        self._name = 'lights'

class Wheel(CarPart):
    def __init__(self, serial: str,  unbroken: bool = True):
        super().__init__(serial, unbroken)
        self._name = "wheel"
