import logging

#  получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{__name__}.log", mode="w")
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

py_logger.info(f"тестирование логера {__name__}...")

print("! before main")
if __name__ == "__main__":
    a = 3
    b = 0
    try:
        x = a / b
    except ZeroDivisionError:
        print(" На ноль делить нельзя!")
        py_logger.exception("ZeroDivisionError")
        raise SystemExit("Зафиксирована попытка деления на ноль. Выход. ")
    print("завершение работы")
