import array
symbols = '$¢£¥€¤'

if __name__ == '__main__':
    print(tuple(ord(symbol) for symbol in symbols))
    a = array.array('I', (ord(symbol) for symbol in symbols))
    print(a)
