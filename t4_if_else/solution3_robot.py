# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток) и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо. Дан символ C — исходное направление робота и целое число N — посланная ему команда. Вывести направление робота после выполнения полученной команды.
class Robot:
    # _directions = {"С": 0, "В": 1, "Ю": 2, "З": 3}
    _directions = "СВЮЗ" 
    _list_direction = ['Север','Восток','Юг','Запад']
    def __init__(self, pos: str):
        self._direction = self._directions.index(pos)
    def moveLeft(self):
        if self._direction == 0:
            self._direction = 3
        else:
            self._direction-=1

    def moveRight(self):
        if self._direction == 3:
            self._direction =0 
        else:
            self._direction+=1

    def getDirection(self):
        return self._list_direction[self._direction]


def move_robot():
    start_direction = input(
        "Введите исходное положение робота одной буквой (С,В,Ю либо З): "
    ).capitalize()
    if len(start_direction) == 1 and start_direction in "СВЮЗ":
        robot = Robot(start_direction)
        print(f'Исходное положение робота {robot.getDirection()}')
        move_queue = input("Введите последовательность команд для робота: ")
        move_queue = move_queue.replace("2", "!") # на всяк случай уберём все мусорные 2ки
        print(move_queue)
        move_queue = move_queue.replace('-1', '2')

        for el in move_queue:
            match el:
                case '1':
                    robot.moveLeft()
                    print(f'Поворот влево. Положение робота - {robot.getDirection()}')
                case '2':
                    robot.moveRight()
                    print(f'Поворот вправо. Положение робота - {robot.getDirection()}')
        print(f'Конечное направление робота после последовательности движений ={robot.getDirection()}')
    else:
        print("Задано неверное положение робота")
        return


if __name__ == "__main__":
    move_robot()

    #

    #
