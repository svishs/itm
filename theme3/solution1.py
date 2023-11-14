def mean_ver2():
    count = 0
    sum = 0
    print("Введите серию чисел для подсчёта среднего арифметического")
    while True:
        try:
            x = int(
                input(
                    "Введите очередное число отличное от нуля (или 0 для выхода из цикла): "
                )
            )
        except ValueError:
            raise SystemExit("Некорректные входные данные. Выход.")
        if x == 0:
            break
        count += 1
        sum += x

    if count:
        print(f"Среднее арифметическое введённых чисел = {sum/count:10.4f} ")
    else:
        print("Завершение. Нечего считать.")


if __name__ == "__main__":
    mean_ver2()
