from collections import namedtuple
import typing


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


Coordinate2 = namedtuple('Coordinate2', 'lat lon')
Coordinate3 = typing.NamedTuple('Coordinate3', [('lat', 'float'), ('lon', 'float')])

if __name__ == '__main__':
    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    location = Coordinate(55.76, 37.62)
    print(location == moscow)
    print((location.lat, location.lon) == (moscow.lat, moscow.lon))
    print('----------------------')
    moscow = Coordinate2(55.76, 37.62)
    print(moscow)
    location = Coordinate2(55.76, 37.62)
    print(location == moscow)
    print((location.lat, location.lon) == (moscow.lat, moscow.lon))
    print('----------------------')
    moscow = Coordinate3(55.76, 37.62)
    print(moscow)
    location = Coordinate3(55.76, 37.62)
    print(location == moscow)
    print((location.lat, location.lon) == (moscow.lat, moscow.lon))
