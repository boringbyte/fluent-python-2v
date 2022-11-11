import re
import collections

WORD_RE = re.compile(r'\w+')
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


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case _:
            raise ValueError(f'Invalid record: {record!r}')


def standard_api_mapping_types():
    my_dict = {}
    print(isinstance(my_dict, collections.abc.Mapping))
    print(isinstance(my_dict, collections.abc.MutableMapping))


"""
    Inserting or Updating Mutable Values
    1. d[key] raises error if key is not present in the dictionary d.
    2. So, we can use d.get(key, default) 
"""


def get_index0(file):
    index = dict()
    with open(file, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                occurrences = index.get(word, [])  # This is not the best way to code.
                occurrences.append(location)
                index[word] = occurrences

    for word in sorted(index, key=str.upper):
        print(word, index[word])


def get_index1(file):
    index = dict()
    with open(file, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)  # somewhat better than previous one
                # Reduces two searches to single search

    for word in sorted(index, key=str.upper):
        print(word, index[word])


def get_index2(file):
    index = collections.defaultdict(list)  # take list as the default factory
    with open(file, encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)  # somewhat better than original one
                # Reduces two searches to single search

    for word in sorted(index, key=str.upper):
        print(word, index[word])


class StrKeyDict0(dict):
    """
        The __missing__ method
        1. Underlying the way mappings deal with missing keys is __missing__ method.
        2. This method is not defined in the base dict class, but dict is aware of it.
        3. If you subclass dict and provide a __missing__ method, the standard dict.__getitem__ will call it
           whenever a key is not found, instead of raising KeyError.
    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):  # For overwriting general 'in' functionality
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict1(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):  # For overwriting general 'in' functionality
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str[key]] = value


if __name__ == '__main__':
    """Different dictionary creation methods
       Dictionary by default are ordered from python version 3.6 and above"""
    food1 = dict()
    food2 = dict(category='ice cream', flavor='vanilla', cost=199)
    food3 = {'category': 'ice cream', 'flavor': 'vanilla', 'cost': 199}

    """dictionary comprehensions can be created as below"""
    country_dial1 = {country: code for code, country in DIAL_CODES}
    country_dial2 = {code: country.upper()
                     for country, code in sorted(country_dial1.items())
                     if code < 70}
    print(country_dial2)

    """Unpacking mappings
    In cases of duplicate keys, later occurrences overwrite previous ones"""
    print(dump(**{'x': 1}, y=2, **{'z': 3}))
    # >> {'x': 1, 'y': 2, 'z': 3}
    print(dump(**{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}))
    # >> {'a': 0, 'x': 4, 'y': 2, 'z': 3}

    """Merging Mappings with |"""
    d1 = {'a': 1, 'b': 3}
    d2 = {'a': 2, 'b': 4, 'c': 4}
    d = d1 | d2  # new dictionary
    # >> {'a': 2, 'b': 4, 'c': 4}
    d1 |= d2  # in place of d1
    # >> {'a': 2, 'b': 4, 'c': 4}

    """Pattern Matching with Mappings
        1. Mapping pattern succeed on partial matches.
        2. There is no need to use **extra to match extra key-value pairs, but if you wan to capture them as dict, 
        you can prefix one variable with **.
    """
    b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')
    print(get_creators(b1))
    # >> ['Douglas Hofstadter']
    b2 = collections.OrderedDict(api=2, type='book', title='Python in a Nutshell',
                                 authors='Martelli Ravenscroft Holden'.split())
    print(get_creators(b2))
    # >> ['Martelli', 'Ravenscroft', 'Holden']
    # get_creators({'type': 'book', 'pages': 770})
    # Returns errors

    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
        case {'category': 'ice cream', **details}:
            print(f'Ice cream details: {details}')
    # >> Ice cream details: {'flavor': 'vanilla', 'cost': 199}

    standard_api_mapping_types()
    # >> True
    # >> True

    """What is hashable:
        1. An object is hashable if it has a hash code which never changes during its lifetime (it needs a __hash__()
           method.
        2. The object should be compared to other objects
        3. Numeric types and flat immutable types str and bytes are all hashable.
        4. Container types are hashable fi they are immutable and all contained objects are also hashable.
        5. User-defined types are hashable by default because their hash code is their id(), and the __eq__() method.
        6. If an object implements a custom __eq__() that takes into account its internal state, it will be 
           hashable only if its __hash__() always returns the same hash code.
    """
    tt = (1, 2, (30, 40))
    print(hash(tt))
    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))

    get_index0('../zen.txt')
    get_index1('../zen.txt')
    get_index2('../zen.txt')

