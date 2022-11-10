from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(f'Sum of {v1} and {v2} is: {v1 + v2}', end='\n\n')
    v = Vector(3, 4)
    print(f'Absolute value of {v} Vector is: {abs(v)}', end='\n\n')
    print(f'Scalar multiplication of vector {v} and value 3 is : {v * 3}', end='\n\n')

