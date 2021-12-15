#import person_2
class Boss:
    'пробуем подвязать к person_2'





    def __init__(self, name, age = 'Не указан'):
        self.name = name
        self.age =age

    def display_boss(self):
        print('Начальник: {}. Возраст: {} ' .format(self.name, self.age))


k = Boss('Макс', 9)

k.display_boss()

#person_2