class Parent:
    def __init__(self) -> None:
        self.parent_attribute = "I am a parent"

    def parent_method(self):
        print("Back in my day")


# создаём дочерний класс который наследуется от Parent
class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        self.child_attribute = "I am a child"


class Parent1:
    def __init__(self) -> None:
        self.parent_attribute = "I am a parent"

    def parent_method(self):
        print("Back in my day")


# создаём дочерний класс который наследуется от Parent
class Child1(Parent1):
    def __init__(self) -> None:
        super().__init__()
        self.child_attribute = "I am a child"


class B:
    def b(self):
        print("b")


class C:
    def c(self):
        print("c")


class D(B, C):
    def d(self):
        print("d")


class B1:
    def x(self):
        print("x: B1")


class C1:
    def x(self):
        print("x: C1")


class D1(B1, C1):
    pass


if __name__ == "__main__":
    child = Child()
    print(child.child_attribute)
    print(child.parent_attribute)
    child.parent_method()

    d = D()
    d.b()
    d.c()
    d.d()

    d1 = D1()
    d1.x()
    print(D1.mro())
