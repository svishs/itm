if __name__ == "__main__":
    try:
        number_list = list(
            map(int, input("Введите минимум 3 целых числа через пробел: ").split())
        )
    except BaseException:
        raise SystemExit("Произошла ошибка при вводе данных. Выход")
    # if not number_list:
    # raise SystemExit("Список чисел пуст. Выход.")
    # 1. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
    if len(number_list) < 3:
        raise SystemExit("Введено мало чисел. Выход. ")
    print(
        f"Количество положительных чисел в исходном наборе = {len([el for el in number_list if el>0])}"
    )
    # Даны два числа. Вывести большее из них
    print(
        f" Большее из двух чисел {number_list[0]} {number_list[1]} является {max(number_list[0], number_list[1])}"
    )
    if number_list[0] > number_list[1]:
        print(f"реализация через if... Большее число = {number_list[0]}")
    else:
        print(f"реализация через if... Большее число ={number_list[1]}")
    # Даны два числа. Вывести вначале большее, а затем меньшее из них.
    temp_l = number_list[:2]
    temp_l.sort()
    # print(temp_l)
    print(f"{temp_l[1]} {temp_l[0]}")
    # Даны три числа. Найти наименьшее из них.
    # number_list.sort()
    # print(number_list[0])
    # print(min(number_list))
    min = number_list[0]
    for i in range(1, 3):
        if min > number_list[i]:
            min = number_list[i]
    print(f"минимальное число из первых трёх введённых {min=}")
    # Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка. Координаты задаются пользователем, например (10, 15).
    print("")

    x, y = number_list[0], number_list[1]
    print(f" {x=} {y=}")

    if x == 0 or y == 0:
        print("Одна из координат лежит на оси X или Y...")
    else:
        if x > 0:
            if y > 0:
                print("Точка находится в первой четверти")
            else:
                print("Точка находится в четвёртой четверти")
        else:
            if y > 0:
                print("Точка находится в четвёртой четверти")
            else:
                print("Точка находится в третьей четверти")
