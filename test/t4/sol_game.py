import random

if __name__ == "__main__":
    print('Игра "Отгадай число"')

    try:
        top_bound = int(
            input(
                "Настройка игры. \nЗадайте верхнюю границу генерации случайного числа. "
            )
        )
    except ValueError:
        print(
            "Было введено что-то непонятное, поэтому возьмём в качестве верхней границы 100."
        )
        top_bound = 100
    if top_bound <= 0:
        print(
            "Было введено что-то непонятное, поэтому возьмём в качестве верхней границы 100."
        )
        top_bound = 100

    secret_num = random.randint(0, top_bound)

    while True:
        try:
            attempt = int(
                input(
                    f" Попытайся отгадать число, которое сгенерировал робот в диапазоне [0, {top_bound}]: "
                )
            )
        except ValueError:
            raise SystemExit("Ошибка ввода числа. Выход")
        if attempt == secret_num:
            print(" Поздравляю! Ты отгадал число!")
            break
        if secret_num > attempt:
            print(" Загаданное число больше того, которое ты ввёл. Попробуй ещё раз. ")
        else:
            print(" Загаданное число меньше числа введённого тобой. Попробуй ещё раз. ")
