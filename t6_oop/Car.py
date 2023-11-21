from MeansOfTransport import MeansOfTransport


class Car(MeansOfTransport):
    # В классе Car добавьте переменную класса car_drive = 4
    # и реализуйте classmethod, который выводит на экран
    # переменную car_drive
    CAR_DRIVE = 4
    __anti_block_system = False
    __gearbox_type = "m"  # m - mechanical, a - automatic
    __current_gear = 0
    __current_speed = 0
    __engine_capacity = 1.8
    __max_number_of_passengers = 4
    __wheels_count = 4

    @classmethod
    def show_car_drive(cls):
        print(cls.CAR_DRIVE)

    def __init__(self, color: str, brand: str, **kwargs):
        """
        необязательные аргументы: wheels_count:int = 4, gearbox_type:str ("m"|"a"),
        engine_capacity: float, max_number_of_passengers: int, passengers:list[str]
        """
        super().__init__(color, brand)
        self._wheels_count = kwargs.pop("wheels_count", self.__wheels_count)
        self._gearbox_type = kwargs.pop("gearbox_type", self.__gearbox_type)
        self._engine_capacity = kwargs.pop("engine_capacity", self.__engine_capacity)
        self._max_number_of_passengers = kwargs.pop(
            "max_number_of_passengers", self.__max_number_of_passengers
        )
        self._passengers = kwargs.pop("passengers", None)

        if not self._passengers:
            self._passengers = []

    def _get_state(self):
        return {
            "wheels_count": self._wheels_count,
            "gearbox_type": self._gearbox_type,
            "engine_capacity": self._engine_capacity,
            "max_number_of_passengers": self._max_number_of_passengers,
            "passengers": self._passengers,
        }

    @classmethod
    def __valid_operand(cls, other):
        if not isinstance(other, str):
            raise ArithmeticError("Вторым аргументом должна быть строка!")

    def __add__(self, other):
        self.__valid_operand(other)  # если недопустимый операнд, то получим исключение
        if len(self._passengers) < self._max_number_of_passengers:
            self._passengers.append(other)
        else:
            raise ValueError("Невозможно добавить ещё одного пассажира")
        return Car(self._color, self._brand, **self._get_state())

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.__valid_operand(other)
        if len(self._passengers) < self._max_number_of_passengers:
            self._passengers.append(other)
        else:
            raise ValueError("Невозможно добавить ещё одного пассажира")
        return self

    def __sub__(self, other):
        self.__valid_operand(other)
        if other not in self._passengers:
            raise ValueError("Пассажира с таким именем не найдено")
        else:
            # создадим экземпляр класса, после чего удалим пассажира и вернём
            #  этот экземпляр (т.е. исходный объект изменять нельзя)
            # исходный объект изменится если он стоит слева операции вычитания.
            temp_car = Car(self._color, self._brand, **self._get_state())
            temp_car._passengers.pop(temp_car._passengers.index(other))
            return temp_car

    def __isub__(self, other):
        self.__valid_operand(other)
        if other not in self._passengers:
            raise ValueError("Пассажира с таким именем не найдено")
        else:
            self._passengers.pop(self._passengers.index(other))
            return self

    def __repr__(self) -> str:
        return f'Объект класса {self.__class__}, цвет {self._color}, марка {self._brand} '
    
    def __str__(self) -> str:
        return f'Объект класса {self.__class__}, цвет {self._color}, марка {self._brand} '

if __name__ == '__main__':
    c = Car("green", "lada")
    # print(c.__current_gear)  #попытка обращения к приват свойству приводит к ошибке
    # print(c._gearbox_type)

    c = c + "Иван"
    c = c + "Ольга"
    c = c + "Вася"
    c = c + "Валя"
    print(c.__dict__)
    c = c - "Иван"
    c -= "Валя"
    print(c.__dict__)
    print(c)
