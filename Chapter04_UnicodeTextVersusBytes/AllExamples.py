import array


if __name__ == '__main__':
    s = 'café'
    print(s)
    print(len(s))

    b = s.encode('utf8')
    print(b)

    c = b.decode('utf8')
    print(c)

    cafe = bytes('café', encoding='utf_8')
    print(cafe)
    print(cafe[0])
    print(cafe[:1])

    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[-1:])

    numbers = array.array('h', [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)

    city = 'São Paulo'
    print(city.encode('utf_8'))
    print(city.encode('utf_16'))

    # print(city.encode('cp437')) raises encoding error
    city.encode('cp437', errors='ignore')  # to ignore error characters silently and this is usually a bad idea
    city.encode('cp437', errors='replace')  # to replace error characters with ?
    city.encode('cp437', errors='xmlcharrefreplace')  # to replace error characters with XML entity

    octets = b'Montr\xe9al'
    octets.decode('cp1252')  # to decode using Windows 1252
    octets.decode('iso8859_7')  # to decode for Greek
    octets.decode('koi8_r')   # to decode for Russian
    # octets.decode('utf_8')  throws error
    octets.decode('utf_8', errors='replace')  # to replace error characters with ?
