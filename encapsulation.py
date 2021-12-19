# attribute - (без подчеркивания) публичное свойство (public)
# _attribute - (с 1 подчеркиванием) режим доступа (protected),
# сужит для обращения внутри класса и во всех его дочерних классах
# __attribute - (с 2 подчеркиваниями) режим доступа (private), служит для обращения только внутри класса


# class Point:
#    def __init__(self, x=0, y=0):
#        self._x = x
#        self._y = y
#
# pt = Point(1, 2)
# print(pt._x, pt._y)

from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    #  приватный метод:
    #  @private  #  защита обращения к методу. при этом можно убрать __ из имени метода
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    #  метод setter:
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    #  метод getter:
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())

# print(pt._Point__x)  # обращение к значению не рекомендуется использовать
# print(dir(pt)) #  проверка возможных свойств класса pt
# print(pt.__x, pt.__y)  #  так вызвать неполучится
