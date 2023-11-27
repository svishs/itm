# Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите
# метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.

class Calculator:
    @staticmethod
    def add(a: int, b: int):
        return a + b

class StrCalc(Calculator):
    @staticmethod
    def add(a: str, b: str):
        return a + b

if __name__ == '__main__':
    print(Calculator.add(3, 4))
    print(StrCalc.add('abc', 'qwe'))
