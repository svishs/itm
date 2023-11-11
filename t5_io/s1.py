import pandas as pd

if __name__ == "__main__":
    file = open("lorum.txt", encoding="utf8")
    text = file.read()
    print(text)
    file.close()

    # file = open("lorum.txt", "rb")
    # data = file.read()
    # print(data)
    # file.close()
    print("---" * 3)
    with open("lorum.txt") as file:
        text = file.read()
    print(text)

#
