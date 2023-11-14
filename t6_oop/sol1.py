class MeansOfTransport:
    def __init__(self, color, brand) -> None:
        self.__color = color
        self.__brand = brand

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self.__brand)

    @property  # определяем геттер в первую очередь
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property  # определяем геттер для брэнда и только затем сеттер
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand
