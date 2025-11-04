from shape import Shape 
import math 
# this is ht e child class of Shape, this class is a circle.
class Circle(Shape):
    #this class is for creating a circle position on a coordinate system.
    def __init__(self, x = 0, y = 0, radius = 1):

        super().__init__(x, y) # this is to connect with the parent class

        # this is going to make sure that the radius is a number or else it will raise TypeError
        if not isinstance(radius, (int, float)):
            raise TypeError("radius has to be a number")
        
        # stores value as float
        self._radius = float(radius)

    # this property is for calculating the area of the circle
    # Note that i got with this part from a website called: https://docs.kanaries.net/topics/Python/python-pi
    @property
    def area(self):
        return math.pi * (self._radius ** 2)  
    # this calculates the perimeter in this case (circumference)
    @property
    def perimeter(self):
        return 2 * math.pi * self._radius 
    # this gives read only accses to radius
    @property
    def radius(self):
        return self._radius 
    
    # checks to see if circle is a circle
    def is_unit_circle(self):
        return self._radius == 1
    
    # this a repr for the developers
    def __repr__(self):
        return f"circle(x = {self._x}, y = {self._y} radius = {self._radius})"
    
    # this code is for more readble string text showing the position and radius
    def __str__(self):
        return f"circle placement is : ({self._x}, {self._y}) with radius {self._radius}"
    

    
      





    

    

