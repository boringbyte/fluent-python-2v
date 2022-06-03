from typing import NamedTuple


class DemoNTClass(NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


if __name__ == '__main__':
    print(DemoNTClass.__annotations__)
    print(DemoNTClass.b)
    print(DemoNTClass.c)
    print(DemoNTClass.a)
    print(DemoNTClass.__doc__)
    nt = DemoNTClass(8)
    print(nt.a)
    print(nt.b)
    print(nt.c)
