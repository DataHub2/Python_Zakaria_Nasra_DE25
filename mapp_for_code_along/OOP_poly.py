from numbers import Number

class Vector:
    """A class representing a Euclidean vector"""
    def __init__(self, *numbers):
        print(type(numbers))
        print(numbers)

        for number in numbers:
            if not isinstance(number, Number):
                raise TypeError(f"elements must be numbers not {type(number)}")

v1 = Vector(1,2)

try:
    v2 = Vector("1",2)
except TypeError as err:
    print(err)


              