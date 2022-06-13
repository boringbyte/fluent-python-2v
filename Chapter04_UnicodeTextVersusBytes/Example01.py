s = 'café'


if __name__ == '__main__':
    print(len(s))
    b = s.encode('utf8')
    print(b)
    print(b.decode('utf8'))
