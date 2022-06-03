class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'


if __name__ == '__main__':
    print(DemoPlainClass.__annotations__)
    print(DemoPlainClass.b)
    print(DemoPlainClass.c)
    print(DemoPlainClass.a)
