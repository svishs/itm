from contextlib import contextmanager

class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f'ресурс открыт с аргументами{args}')
        self.opened = True

    def close(self):
        print('Ресурс был закрыт')
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Обнаружена утечка памяти. Ресурс не был закрыт')

    def action(self):
        print('Какие-то действия с ресурсом')

@contextmanager
def open_resource(*args):
    ''' контекстный менеджер для экзепляров класса Resource'''
    # функция генератор
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource
    except Exception:
        raise
    finally:
        if resource:
            resource.close()

class DefendedVector:
    def __init__(self, v: list):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: # если исключения не было, то
            self.__v = self.__temp # вернуть изменнеый список
        return False


class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()
        # return True # в этом случае ислючения не буду брошены дальше из блока
        return False


if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [3, 4, 8]

    try:
        with DefendedVector(v1) as dv:
            for i, el in enumerate(dv):
                dv[i] += v2[i]
    except:
        print('Ошибка')
    print(v1)

    with open_resource(1,2,3) as res:
        res.action()
        # raise ValueError('stop')

    with ResourceWorker(1,2,3) as res:
        res.action()
        raise ValueError('stop')