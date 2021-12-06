class Person:
# Параметры возраста и пола имеют значение по умолчанию.
    def __init__(self, name, age=1, gender="Male"):
        self.name = name
        self.age = age
        self.gender= gender
    def showInfo(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print('------------')

pers1 = Person('Андрей')
pers2 = Person('Жорик', 36, 'male')

pers1.showInfo()
pers2.showInfo()
