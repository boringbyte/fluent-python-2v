DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]


def dump(**kwargs):
    return kwargs


if __name__ == '__main__':
    country_dial = {country: code for code, country in DIAL_CODES}
    print(country_dial)
    upper_country_dial = {code: country.upper() for code, country in DIAL_CODES if code < 70}
    print(upper_country_dial)
    print(dump(**{'x': 1}, y=2, **{'z': 3}))
    print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 4}
    print(d1 | d2)
    d1 |= d2
    print(d1)
    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
        case {'category': 'ice cream', **details}:
            print(f'Ice cream details: {details}')
