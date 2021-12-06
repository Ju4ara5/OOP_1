class Boss:
    'пробуем подвязать к person_2'





    def __init__(self, name):
        self.name = name

    def display_boss(self):
        print('Начальник: {}.' .format(self.name))


k = Boss('Макс')

k.display_boss()

