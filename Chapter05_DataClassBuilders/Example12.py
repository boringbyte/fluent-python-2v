from dataclasses import dataclass


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'


if __name__ == '__main__':
    print(DemoDataClass.__annotations__)
    print(DemoDataClass.b)
    print(DemoDataClass.c)
    print(DemoDataClass.__doc__)
    nt = DemoDataClass(8)
    print(nt.a)
    print(nt.b)
    print(nt.c)
    print(DemoDataClass.a)
