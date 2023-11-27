from meansoftransport import MeansOfTransport
from carelements import CarPart, Motor, Lights, Wheel
import copy
class Car(MeansOfTransport):
    # В классе Car добавьте переменную класса car_drive = 4
    # и реализуйте classmethod, который выводит на экран
    # переменную car_drive
    CAR_DRIVE = 4
    __max_number_of_passengers = 4
    __wheels_count = 4
    _req_elements_list = ['motor', 'lights','wheels']

    @classmethod
    def show_car_drive(cls):
        print(cls.CAR_DRIVE)

    def __init__(self, color: str, brand: str, wheels_count:int =4, **kwargs):
        """
        необязательные аргументы: wheels_count:int = 4,
        max_number_of_passengers: int, passengers:list[str]
        req_elements = {}
        """
        super().__init__(color, brand)
        self._wheels_count = kwargs.pop("wheels_count", self.__wheels_count)
        self._max_number_of_passengers = kwargs.pop(
            "max_number_of_passengers", self.__max_number_of_passengers
        )
        self._passengers = kwargs.pop("passengers", [])
        self._req_elements = kwargs.pop('req_elements', {})

    def _get_state(self): # используется при копировании свойств объекта в функциях
        """ Возвращает словарь свойств объекта.
            Используется в операциях __add__, __sub__ и им подобных для создания нового объекта.
        """

        # обязательно делаем копию списка пассажиров, иначе список будет
        # единым для всех объектов скопированных с этого экземпляра
        _passengers_list_copy = self._passengers[:]
        # обязательно делаем копию словаря элементов машины, иначе словарь будет
        # единым для всех объектов скопированных с этого экземпляра
        _req_elements_dic_copy = copy.deepcopy(self._req_elements)
        return {
            "wheels_count": self._wheels_count,
            "max_number_of_passengers": self._max_number_of_passengers,
            "passengers": _passengers_list_copy,
            "req_elements": _req_elements_dic_copy
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

    def __iadd__(self, other):# создавать новый объект не нужно, только меняем
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
        return (
            f"Объект класса {self.__class__.__name__}, цвет {self._color},"
            f" марка {self._brand}. Машина {'исправна' if self.__bool__() else 'неисправна'} "
        )

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self._passengers):
            current_pas = self._passengers[self.__index]
            self.__index += 1
            return current_pas
        else:
            raise StopIteration

    def __bool__(self):
        for key in self._req_elements_list: # _req_elements_list = ['motor', 'lights','wheels']
            car_element: CarPart = self._req_elements.get(key, False)
            if not car_element: # общий случай когда такого ключа-значения нет в словаре
                # print('машина недоукомплектована')
                return False
            if key =='wheels': # значения для этого ключа -  список элементов CarPart!
                if len(car_element) < self.__wheels_count:
                    # print('машина недоукомплектована колёсами!')
                    return False
                for i in range(self.__wheels_count):
                    if not car_element[i]._unbroken:
                        return False
                continue
            if not car_element._unbroken:
                return False
        return True

    def add_car_req_el(self, el:CarPart):
        if isinstance(el, CarPart):
            match el._name:
                case 'wheel':
                    if not self._req_elements.get('wheels', False):
                        self._req_elements['wheels'] = []
                        self._req_elements['wheels'].append(el)
                    else:
                        if len(self._req_elements['wheels']) < self.__wheels_count:
                            self._req_elements['wheels'].append(el)
                        else:
                            raise ValueError('Колёс уже достаточно. Куда больше?')
                case 'motor':
                    self._req_elements.update({'motor': el})
                case 'lights':
                    self._req_elements.update({'lights': el})
        else:
            raise ValueError('Недопустимый тип элемента!')
                
    def get_passengers_str(self):
        return f"Пассажиры: {', '.join(self._passengers)}"



if __name__ == "__main__":
    car = Car("green", "ford")
    motor = Motor('12312')
    lights = Lights('234324')
    wheel1 = Wheel('a')
    wheel2 = Wheel('b')
    wheel3 = Wheel('c')
    wheel4 = Wheel('d')

    car.add_car_req_el(wheel4)
    car.add_car_req_el(wheel2)
    car.add_car_req_el(wheel3)
    car.add_car_req_el(wheel1)
    car.add_car_req_el(motor)
    car.add_car_req_el(lights)

    print(f" машина car {'исправна' if car else 'неисправна'}")
    wheel4._unbroken = False
    print(f" машина car после того, как пробили колесо: {'исправна' if car else 'неисправна'}")


    car2 = Car("Red", "Зил")
    motor2 = Motor('12312')

    car2.add_car_req_el(motor2)
    print(f"недоукомплектованая машина car2: {'исправна' if car2 else 'неисправна'}")

    print(car) # проверка __str__ / __repr__
    print()
    print(car2)
    print()
    car = car + "Иван"
    car = car + "Ольга"
    car = car + "Вася"
    car = car + "Валя"
    print('список пассажиров объекта car ', car.get_passengers_str())

    car2 = car - "Иван"
    print('car2 копия car без одного пассажира ', car2.get_passengers_str())
    car = car - "Иван"
    car -= "Валя"
    print('car после удаления двух пассажиров ', car.get_passengers_str())
    # print(car.__dict__)

    print('проверка итерируемости объекта класса car (проход по внутреннему атрибуту _passengers)')
    for pas in car:
        print(pas)