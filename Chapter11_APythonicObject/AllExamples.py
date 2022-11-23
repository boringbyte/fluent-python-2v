import math
from array import array


class Vector2d:

    typecode = 'd'  # typecode is a class attribute we'll use when converting instance to from bytes
    __match_args__ = ('x', 'y')  # To make positional patterns, we need to add a class attribute named like this

    def __init__(self, x, y):
        self.__x = float(x)   # Use exactly two leading underscores (with zero or one trailing underscore) to make an attribute private
        self.__y = float(y)

    @property  # The @property decorator marks the getter method of a property
    def x(self):  # The getter method is named after th public property if exposes: x.
        return self.__x  # Just return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod  # The classmethod modifies the method so that it can be called directly on a class.
    def frombytes(cls, octets):  # No self argument as class itself is passed as the first argument.
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_format = '<{}, {}>'
        else:
            coords = self
            outer_format = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_format.format(*components)

    def __hash__(self):
        return hash((self.x, self.y))


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'{v!r} is vertical')
        case Vector2d(y=0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if x == y:  # can be replaced with Vector2d(x, y) if x == y: as we added __match_args__
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is null')


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
    print('-------------------------------')

    print(format(Vector2d(1, 1), 'p'))
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '.5fp'))
