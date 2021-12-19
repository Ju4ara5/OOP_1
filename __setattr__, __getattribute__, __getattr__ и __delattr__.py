class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_coord(self, x, y):
        self.x = x
        self.y = y

#  метод которы изменяет зачение атрибута MIN_COORD:
#    @classmethod
#    def change(cls, left):
#        cls.MIN_COORD = left


    def __getattribute__(self, item):  # автоматически запускается при обращении к какому либо атрибуту класса
        print('__getattribute__: ', item)
        if item == 'x':  # запрещаем доступ к атрибуту x.
            raise ValueError('Доступ к "x" запрещен')  # сгенерировать ошибку
        else:
            return object.__getattribute__(self, item)


# автом вызывается когда идет присвоение какому либо атрибуту какого-то значания:
# key - имя атрибута, value - значение которое ему присваивается:
# можем запретить создавать какой либо атрибут в экземпляр класса:
    def __setattr__(self, key, value):
        #print('__setattr__: ', key, ':', value)
        if key == 'z':
            raise AttributeError('Запрещенное имя атрибута')
        else:
            object.__setattr__(self, key, value)


pt1 = Point(1, 2)
pt2 = Point(10, 20)

#  a = pt1.x  #  Доступ к "x" запрещен. т.к. это прописано в методе __getattribute__
#pt1.z = 5  # AttributeError: Запрещенное имя атрибута. прописано в __setattr__

