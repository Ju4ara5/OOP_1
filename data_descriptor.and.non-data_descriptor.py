#  non-data descriptor:
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


#  data descriptor:
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        #  return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)
        #  print(f'__set__ : {self.name} = {value}')
        #  instance.__dict__[self.name] = value


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть целым числом')


p = Point3D(1, 2, 3)
p.__dict__['xr'] = 5
#  p.xr = 5
print(p.xr, p.__dict__, p.y)
