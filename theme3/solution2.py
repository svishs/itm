if __name__ == "__main__":
    for i in range(101):
        print(f"{i}", end=" ")
    print(" ")
    
    # input("Нажмите ENTER для продолжения...")

    print('Таблица умножения')    
    s = "mul|"
    for i in range(10):
        s = s + "{:>4d}".format(i)
    print(s)
    print("----" * 11)
    for x in range(10):
        s = "{:^3d}|".format(x)
        for y in range(10):
            s += "{:>4d}".format(x * y)
        print(s)

    l = ["a", 10, 20.0, "!"]
    print(f"Исходный список {l}")
    print("Вывод элементов списка через пробел в цикле")
    for el in l:
        print(f"{el=}", end=" ")

    print("")
    dic = {"str": "string", 2: 2, "bool": False}
    print(f" Исходный словарь {dic}")
    print("Вывод ключей и значений словаря в цикле")
    for key, value in dic.items():
        print(f"{key=} {value=}")
