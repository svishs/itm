def mean():
    count = 0
    try:
        x = int(
            input("Введите число отличное от нуля, либо ноль для завершения работы: ")
        )
        sum = x
    except ValueError:
        raise SystemExit("Некорректные входные данные! Ошибка типа. Выход")
    if x == 0:
        print("Завершение. Нечего считать.")
        return

    while x != 0:
        try:
            x = int(
                input(
                    "Введите число отличное от нуля, либо ноль для завершения работы: "
                )
            )
        except ValueError:
            raise SystemExit("Некорректные входные данные! Ошибка типа. Выход")
        count += 1
        sum += x

    print(f"Среднее арифметическое введённых чисел = {sum/count:10.4f} ")


if __name__ == "__main__":
    mean()
