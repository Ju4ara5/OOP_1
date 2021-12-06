class Employee:
    'try class'
    print('hao')
    emp_count = 0

    def __init__(self, name, salary, age, born):
        self.name = name
        self.salary = salary
        self.age = age
        self.born = born
        Employee.emp_count += 1


    def display_count(self):
        print('Всего сотрудников: %d' % Employee.emp_count)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}. Возраст: {}. {}' .format(self.name, self.salary, self.age, self.born))

# пробуем внестти новый обект
#try:
#    i = str(input('Внесите имя:'))
#    z = int(input('Зарплата:'))
#    v = int(input('Внесите возраст:'))
#    a = int(input('Год рождения:'))
#    emp3 = Employee(i, z, v, a)
#     emp3.display_employee()
#except:
#    print('Не верно внесены данные')



# Это создаст первый обект класса Emploee
emp1 = Employee('Андрей', 'Бомж :)', 34, 1988)
# Это создаст второй обект класса Emploee
emp2 = Employee('Мария', 5000, 43, 'f')



#setattr(emp1, 'salary', 3)
#print(Employee.__dict__)


emp1.display_employee()
emp2.display_employee()



print('Всего сотрудников: ', Employee.emp_count)


print(Employee.__doc__)