import math


def perimeter_reg_tetragon(a: float):
    return 4 * a


def square_regular_tetragon(a: float):
    return a * a


def squre_rect(a: float, b: float):
    return a * b


def perimeter_rect(a: float, b: float):
    return 2 * (a + b)


def lenght_circle_by_diam(d: float):
    return d * math.pi


def cube_size(a: float):
    return a**3


def cube_square_of_surface(a: float):
    return 6 * (a**2)


def parallelepiped_size(a: float, b: float, c: float):
    return 2 * (a * b + a * c + b * c)


def lenght_circle_by_raduis(r: float):
    return 2 * r * math.pi


def square_of_circle_by_radius(r: float):
    return math.pi * r * r


def arith_average(a: float, b: float):
    return (a + b) / 2


if __name__ == "__main__":
    a = 0.333
    a = float(input("Введите длину стороны квадрата: "))
    print(f" Периметр квадрата = {perimeter_reg_tetragon(a):10.4f}")
    print(f" Площадь квадрата = {square_regular_tetragon(a):10.4f}")

    input_str = input("Введите через пробел стороны прямоугольника: ")
    # a, b = list(map(float, input_str.split()))
    a, b = [float(x) for x in input_str.split()]
    print(
        f" Площадь прямоугольника = {squre_rect(a, b):10.4f} , периметр прямоугольника = {perimeter_rect(a,b):10.4f}  "
    )

    d = float(input("Введите диаметр окружности: "))
    print(f" Длина окружности = {lenght_circle_by_diam(d):10.4f}")

    a = float(input("Введите длину ребра куба: "))
    print(f" Объём куба = {cube_size(a):10.4f}")
    print(f" Площадь поверхности куба = {cube_square_of_surface(a):10.4f}")

    input_str = input("Введите стороны параллелепипеда через пробел: ")
    a, b, c = [float(x) for x in input_str.split()]
    print(f" Объём параллелепипеда = {parallelepiped_size(a,b,c):10.4f} ")

    a = float(input("Введите радиус круга: "))
    print(
        f" Длина окружности = {lenght_circle_by_raduis(a):10.4f} , площадь круга ={square_of_circle_by_radius(a):10.4f} "
    )

    input_str = input("Введите 2 числа: ")
    a, b = [float(x) for x in input_str.split()]
    print(
        f"Среднее арифметическое = {arith_average(a,b):10.4f}, среднее геометрическое = {math.sqrt(a*b):10.4f} "
    )
    print(f"сумма квадратов = {a*a + b*b: 10.4f}")
    print(f"разность квадратов = {a*a - b*b: 10.4f}")
    print(f"произведение квадратов ={a*a*b*b:10.4f} ")
    print(f"частное квадратов = {(a*a)/(b*b):10.4f}")

    print(f" завершение")
