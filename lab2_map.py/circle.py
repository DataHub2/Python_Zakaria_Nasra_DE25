from shape import Shape 
import math 
"""
'This class is the circle class that represents a circle in a coordinate system.
It inherits from the shape class and here it defines its own area and perimeter.

Atttributes:
    _ radius (float): radius of the circle

Methods:
    area(): returns area of the circle

    perimeter(): returns the perimeter of the circle.

    radius(): read only property for the radius
    is_unit_circle: checks too see if the circle has a radius of 1.

    """
class Circle(Shape):
    def __init__(self, x = 0, y = 0, radius = 1):
        """ Initialize the circle object
        Args:
            x (float): x coordinate of the center.
            y (float): y coordinate of the center.
            radius (float): radius of the circle.
        
        
        Raises:
            TypeError: if the radius is not a number


        """
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius has to be a number")
        
        # stores value as float
        self._radius = float(radius)

    # these properies is for calculating the area of the circle
    # Note that i learned how to use pi in python from this website: https://docs.kanaries.net/topics/Python/python-pi
    @property
    def area(self) -> float:
        """Caluculate and return the area of the circle"""
        return math.pi * (self._radius ** 2)  

    @property
    def perimeter(self) -> float:
        """Calculate and return the circumference of the circle"""
        return 2 * math.pi * self._radius 
    
    @property
    def radius(self) -> float:
        """Read only accsess to radius"""
        return self._radius 
    
    def is_unit_circle(self) -> bool:
        """return True if radius equal to 1"""
        return self._radius == 1
    
   
    def __repr__(self):
        """This gives better readble text to the developers"""
        return f"circle(x = {self._x}, y = {self._y} radius = {self._radius})"
    
    def __str__(self):
        """This gives better readble text of the placement and size"""
        return f"circle placement is : ({self._x}, {self._y}) with radius {self._radius}"
    

    
      





    

    

