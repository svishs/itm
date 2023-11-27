from abc import ABC, abstractmethod


# Реализуйте абстрактный класс Animals, создайте класс Cat, котрый будет наследоваться
# от класса Animals и реализуйте метод voice.
class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass


class Cat(Animals):
    def __init__(self, name: str):
        self.name = name

    def voice(self):
        print('мяу')

# Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс и
# какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton
class Dog(Animals):
    __instance = None
    __first_instance = True
    # обязательно указываем *args, **kwargs иначе __init__ не отработает корректно и будет ошибка
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Dog.__instance = None
        Dog.__first_instance = True

    def __init__(self, name, age = 1):
        if self.__first_instance:
            self.__first_instance = False
            print(f'Вызов __init__ для {str(self)}')
            self.name = name
            self.age = age
        else:
            pass

    def voice(self):
        print('gav')

if __name__ == '__main__':
    dog = Dog('бобик', 3)
    print(dog)
    dog2 = Dog('шарик', 5) # не изменяет свойства первого созданного экземпляра
    print(dog2.name)
    print(dog.name)
    print(dog.age)
    print(dog is dog2)
