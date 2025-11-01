from shape import Shape 
import math 

class Rectangle(Shape):

    #width and height had to be set to a defult = 1 so thst i got be able to work with it.
    def __init__ (self, x = 0, y = 0, width = 1, height = 1 ):
        # this will connect with the parent class
        super().__init__(x, y)  


        
        
