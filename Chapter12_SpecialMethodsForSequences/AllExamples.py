import functools
import math
import operator
import reprlib
from array import array


# This is version 1 of multidimensional vector implementation. In chapter 11, we can find the 2d vector implementation.
class Vector1v:

    typecode = 'd'  # typecode is a class attribute we'll use when converting instance to from bytes

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return f'Vector({components}'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod  # The class method modifies the method so that it can be called directly on a class.
    def frombytes(cls, octets):  # No self argument as class itself is passed as the first argument.
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


# This is version 1 of multidimensional vector implementation with sequence protocol.
class Vector2v:

    typecode = 'd'  # typecode is a class attribute we'll use when converting instance to from bytes

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return f'Vector({components}'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):  # If the key argument is a slice
            cls = type(self)  # Then get the type of the object
            return cls(self._components[key])  # invoke the class to return another vector instance from a slice.
        index = operator.index(key)
        return self._components[index]

    @classmethod  # The class method modifies the method so that it can be called directly on a class.
    def frombytes(cls, octets):  # No self argument as class itself is passed as the first argument.
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


# This is version 1 of multidimensional vector implementation with sequence protocol.
class Vector3v:

    typecode = 'd'  # typecode is a class attribute we'll use when converting instance to from bytes
    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return f'Vector({components}'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):  # zip is a generator
            if a != b:
                return False
        return True

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)  # 0 is the initializer

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):  # If the key argument is a slice
            cls = type(self)  # Then get the type of the object
            return cls(self._components[key])  # invoke the class to return another vector instance from a slice.
        index = operator.index(key)
        return self._components[index]

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:  # Special handling for single-character attribute names.
            if name in cls.__match_args__:  # If name is one of __match_args__, set specific error message.
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():  # If name is lowercase, set error message about all single-letter names.
                error = "can't set attributes 'a' to 'z; in {cls_name!r}"
            else:
                error = ''  # Otherwise, set blank error message.
            if error:  # If there is a nonblank error message, raise error
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # Default case: call __setattr__ on superclass for standard behavior.

    @classmethod  # The class method modifies the method so that it can be called directly on a class.
    def frombytes(cls, octets):  # No self argument as class itself is passed as the first argument.
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
