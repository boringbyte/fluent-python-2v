from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'


if __name__ == '__main__':
    trash = Coordinate('Ni!', None)
    print(trash)
