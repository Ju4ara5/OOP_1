from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

#    '''другой метод прописать инициализатор (более практичный)
#    т.к. проверка соответствия заданных значений прописана в сеттерах ниже
#    (кроме fio, для него не прописан сеттер с проверкой коректности значений)'''
#
#    def __init__(self, fio, old, ps, weight):
#        self.verify_fio(fio)
#
#        self.__fio = fio.split()
#        self.old = old
#        self.passport = ps
#        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой!')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи ФИО!')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ!')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефиc!')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом от 14 до 120 !')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть больше 20 !')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой!')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами!')

    #  интерфейсы для взаимодействия с данными:

    @property  # создаем геттер для работы с ФИО (неизменяемое т.к. не будем прописывать сеттер)
    def fio(self):
        return self.__fio

    @property
    def old(self):  # геттер для возраста
        return self.__old

    @old.setter
    def old(self, old):  # сеттер для возраста (для записи изменения значения old)
        self.verify_old(old)  # проверка на соответствие заданым параметрам (проверка коректности записи)
        self.__old = old

    #  то же самое но только для веса:

    @property
    def weight(self):  # геттер для веса
        return self.__old

    @weight.setter
    def weight(self, weight):  # сеттер для веса (для записи изменения значения weight)
        self.verify_weight(weight)  # проверка на соответствие заданым параметрам (проверка коректности записи)
        self.__weight = weight

    #  для работы с паспортом:

    @property
    def passport(self):  # геттер для паспорта
        return self.__passport

    @passport.setter
    def passport(self, ps):  # сеттер для паспорта (для записи изменения значения passport)
        self.verify_ps(ps)  # проверка на соответствие заданым параметрам (проверка коректности записи)
        self.__passport = ps


p = Person('Балакирев Сергей Михайлович', 30, '1234 567890', 80.0)

#  меняем параметры (сеттер):
p.old = 100
p.passport = '1234 098765'
p.weight = 70.0
print(p.__dict__)  # результат измененных значений
print(p.old)  # вызов отдельного значения
