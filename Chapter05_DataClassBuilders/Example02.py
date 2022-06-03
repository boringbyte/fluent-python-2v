from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


if __name__ == '__main__':
    moscow = Coordinate(55.76, 37.62)
    print(moscow)
    location = Coordinate(55.76, 37.62)
    print(location)
    print(location == moscow)
    print((location.lat, location.lon) == (moscow.lat, moscow.lon))
