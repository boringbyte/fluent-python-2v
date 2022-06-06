def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

if __name__ == '__main__':
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))
    print(fact)
    print(fact(5))
    print(map(factorial, range(11)))
    print(list(map(factorial, range(11))))
