class ThreadData:
    # словарь с общими локальными свойствами экземпляров класса:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        # при создании нового экземпляра класса, то каждый экземпляр будет ссылаться на словарь __shared_attrs,
        # и у них будут общие свойства
        self.__dict__ = self.__shared_attrs
