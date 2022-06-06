import collections


if __name__ == '__main__':
    d1 = dict(a=1, b=2, d=6)
    d2 = dict(a=3, b=4, c=5)
    print(d1 | d2)
    chain = collections.ChainMap(d1, d2)
    print(chain)
    print(chain['a'])
    ct = collections.Counter('abracadabra')
    print(ct)
    ct.update('aaaaazzz')
    print(ct)
    print(ct.most_common(3))
