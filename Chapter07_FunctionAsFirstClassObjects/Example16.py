from operator import mul
from functools import partial

triple = partial(mul, 3)


if __name__ == '__main__':
    print(triple(7))
    print(list(map(triple, range(1, 10))))
    print([triple(i) for i in range(1, 10)])
