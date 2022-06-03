from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])


if __name__ == '__main__':
    print(Coordinate(0, 0))
    print(Coordinate._field_defaults)
