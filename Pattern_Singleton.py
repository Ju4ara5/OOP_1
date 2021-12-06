# для работы с базой данных. надо создавать только 1 экземпляр этого класса
class DataBase:
    __instance = None # Ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # если ... принимает значание None
            cls.__instance = super().__new__(cls) # тогда создается новый экземпляр класса

        return cls.__instance  # вернет адрес ранее созданного обьекта

    def __del__(self):  # после удаления обьекта __ins... , он вернет значание NONE
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД {data}')

db = DataBase('root', '1234', 80) # создаем экземпляр класса
db2 = DataBase('root2', '5678', 40) # будет ссылаться на ранее созданый обьект (db)

print(id(db), id(db2))
