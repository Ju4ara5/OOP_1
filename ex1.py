# Переменная в классах - атрибуты
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



class Point:
    '''Класс для представления координат точек на плоскости'''
    color = 'red'
    circle = 2

