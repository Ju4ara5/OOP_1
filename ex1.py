# Переменная в классах - атрибуты
# методы - действия
# свойства - данные
# a = Point()  -  создание экземпляра класса
#     (внутри него можно создать свое отдельное пространство имен (атрибутов))
# setattr(Point, 'prop', 1) - создание нового атрибута (Класс, 'имя атрибута', значение)
# getattr(Point, 'a', False) - метод обращения к атрибуту класса (Класс , 'имя', что вернуть)
#      (в случае отсуствия нужного 'имя' , вернет *что вернуть*)
# del Класс.имя_атрибута (или delattr ...) - удаление атрибута из Класса
#      (при удалении несуществующего атрибута, вернет ошибку!)
#  hasattr(Класс, 'имя_атрибута') - проверка наличия атрибута в классе (вернет True или False)
# Point.__doc__ - вернет текст описания Класса ('''...''')
# __dict__ - содержит набор атрибутов экземнляра класса
# __init__ - инициализатор обьекта класса
# __del__ - финализатор класса
# __new__ - вызываеся перед созданием обьекта класса
# cls - ссылается на текущий экземпляр класса
# self - ссылается на создаваемый экземпляр класса
# super() - ссылка на базовый класс




class Point:

    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ ', str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('вызов __init__ ', str(self))
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)




