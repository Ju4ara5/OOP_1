# attribute - (без подчеркивания) публичное свойство (public)
# _attribute - (с 1 подчеркиванием) режим доступа (protected),
                # сужит для обращения внутри класса и во всех его дочерних классах
# __attribute - (с 2 подчеркиваниями) режим доступа (private), служит для обращения только внутри класса



#class Point:
#    def __init__(self, x=0, y=0):
#        self._x = x
#        self._y = y
#
#pt = Point(1, 2)
#print(pt._x, pt._y)

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

#  метод setter:
    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

#  метод getter:
    def get_coord(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
#print(pt.__x, pt.__y)  #  так вызвать неполучится

# 7video  6 min