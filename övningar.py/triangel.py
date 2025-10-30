import numbers

class Triangle:
    # x and y optional
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")

        if isinstance(value, bool):
            raise TypeError("must not be boolean")

        if value <= 0:
            raise ValueError("base must be larger than zero")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")

        if isinstance(value, bool):
            raise TypeError("must not be boolean")

        if value <= 0:
            raise ValueError("height must be larger than zero")
        self._height = value

    @property
    def area(self):
        pass

    # @property
    # def perimeter(self):
    #     pass

    def eq(self, other):
        pass

    def lt(self, other):
        pass

    def gt(self, other):
        pass

    def repr(self):
        pass