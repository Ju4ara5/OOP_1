class Vector():
    # атрибуты класса:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod  # работает только с атрибутами класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD  # вернет True если arg попадает в диапазон, иначе False


    def __init__(self, x, y):
        self.x = self.y = 0 # значения по умолчанию (если if...ниже вернет False)
        if self.validate(x) and self.validate(y):  # если значения xy True ->
            self.x = x  # присваиваем значения
            self.y = y  # присваиваем значения
        # вызов независимого метода внутри метода класса:
        print('Внутри __init__: ', self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # независимый от класса метод
    def norm2(x, y):
        return x*x + y*y


print(Vector.validate(5))  # вызов метода со значением arg

print(Vector.norm2(5, 6))  # вызов статического метода

v = Vector(1, 2)
res = v.get_coord()   # простой вызов метода
print(res)

# self - ссылка на текущий экземпляр класса, он так же содержит в себе инфу о классе

