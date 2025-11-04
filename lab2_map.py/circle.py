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
    
      





    

    

