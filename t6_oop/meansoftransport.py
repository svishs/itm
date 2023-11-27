class MeansOfTransport:
    def __init__(self, color: str, brand: str) -> None:
        self._color = color
        self._brand = brand

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self._brand)

    @property  # определяем геттер в первую очередь
    def color(self):
        return self._color

    @color.setter
    def color(self, color:str):
        self._color = color

    @property  # определяем геттер для брэнда и только затем сеттер
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand:str):
        self._brand = brand
