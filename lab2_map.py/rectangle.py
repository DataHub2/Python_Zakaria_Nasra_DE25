from shape import Shape 
import math 
""" 
This class is the circle class that represents a Rectangle in a coordinate system.
It inherits from the shape class and here it defines its own area and perimeter.

Atttributes:
    _width (float): The width of the Rectangle.
    _height (float): The height of the Rectaangle.

Methods:
    area(): calculates the area.

    perimeter(): calculates the perimeter.
    
    width(), height(): Read only access.
    
   is_sqaure(): checks if the Rectangle id a square. 
"""


# Note: i got help from W3 schools on how i can create inheritance class : https://www.w3schools.com/python/python_inheritance.asp
class Rectangle(Shape):

    #width and height had to be set to a defult = 1 so thst i got be able to work with it.
    def __init__ (self, x = 0, y = 0, width = 1, height = 1 ):
        """
        Initialize a Rectangle object.


        Args:
            x (float): x coordinate.
            y (float): y coordinate.

            width (float): width of the Rectangle.
            height (float): height of the Rectangle.

            Raises:
                TyperError: if the width or height is not a number.
    
        """
        super().__init__(x, y) 
        if not isinstance(width, (int, float)):
            raise TypeError("width has to be a number")
        if not isinstance(height,(int, float)):
            raise TypeError("height has to be a number")
        

        self._width = float(width)
        self._height = float(height)

    
    @property
    def area(self) -> float :
        """Calculates and returns area of the rectangle"""
        return self._width * self._height

    @property
    def perimeter(self) -> float :
        """Calculates and returns the perimeter of the rectangle"""
        return 2 * (self._width + self._height)
    
    #this method below will check # Note that i got help from a class mate adding the @property, i got stuck.
    @property
    def width(self) -> float:
        """Read only access to width"""
        return self._width
    
    @property
    def height(self) -> float:
        """Read only access to height"""
        return self._height
    
    def is_square(self) -> bool:
        """This will return True if width is equal to height"""
        return self._width == self._height
    
    # Note that i went through this part with LLM and got instructions on how i can do it
    def __repr__(self) -> str:
        """This is for a more readable text for the developers"""
        return f"rectangle(x = {self._x}, y = {self._y}, width = {self._width}, height = {self._height})"
    
    def __str__(self) -> str:
        """This is for a more user friendly showing of the placement and size"""
        return f"rectangle placement is on: ({self._x}, {self._y}, the width {self.width}, the height {self._height})"
    
    
    

        
        




    


     


        
        
