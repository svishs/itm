from meansoftransport import MeansOfTransport


class Moped(MeansOfTransport):
    # В классе {{Moped}}напишите статическую
    # функцию, которая на вход будет принимать расстояние и
    # максимальную скорость, а на выходе получать время, за которое
    # проедет мопед это расстояние.
    def __init__(self, color: str, brand: str, wheels_count: int = 2):
        super().__init__(color, brand)
        self.wheel_count = wheels_count

    @staticmethod
    def calc_time(length: int, max_speed: int) -> float:
        if not max_speed:
            raise ValueError("Скорость не может равняться нулю!")
        return length / max_speed


m = Moped("red", "bmw")
print(Moped.calc_time(100, 20))
