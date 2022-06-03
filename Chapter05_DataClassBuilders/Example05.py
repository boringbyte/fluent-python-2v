import json
from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', '36.933', (35.689722, 139.691667))
delhi_data = ('Delhi NCR', 'IN', '21.935', Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data)


if __name__ == '__main__':
    print(delhi._asdict())
    print(json.dumps(delhi._asdict()))
