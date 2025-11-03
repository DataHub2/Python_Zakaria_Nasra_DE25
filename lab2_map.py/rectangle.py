from shape import Shape 
import math 
# Note: i did not know how to create this under class so i went in to : https://www.w3schools.com/python/python_inheritance.asp
class Rectangle(Shape):

    #width and height had to be set to a defult = 1 so thst i got be able to work with it.
    def __init__ (self, x = 0, y = 0, width = 1, height = 1 ):
        # this will connect with the parent class
        super().__init__(x, y) 

        # this code will check too see if the value is a number, otherwise it will raise TypeError
        if not isinstance(width, (int, float)):
            raise TypeError("width has to be a number")
        if not isinstance(height,(int, float)):
            raise TypeError("height has to be a number")
        

        # i kept the values private, this is so i can have control of how they are set
        self._width = float(width)
        self._height = float(height)


    @property
    def area(self):
        # this checks the area by multipling the width and the height 
        return self._width * self._height
    
    @property
    def perimeter(self):
        # this will check the perimeter by additing the height and the width, and the multipling it by 2
        return 2 * (self._width + self._height)
    
    #this method below will check # Note that i got help from a class mate adding the @property, i got stuck
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    

        
        




    


     


        
        
