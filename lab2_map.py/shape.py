
class Shape:
    """ 
    This is the base of the geomatric shapes.

    This class is going to represent a general shape in a coordinate system and it gives
    functionality to the subclasses (Rectangle, Circle).
    In this class i have defined coordinate handling, translation and comaprison of area.


    Attributes of this class: 
        _x (float) : this is the x coordinate of the shape
        _y (float) : this is the y coordinate of the shape

    Methods:
        translate: moves the shape depending on the inputed value.
        area(): this has to be implemented in the subclass
        perimeter(): this has to be implemented in the subclass
        __eq__, __lt__, __gt__, __le__, __ge__ : Comparison method that compares area.
         __repr__(): this represents strings better for develepers.
        __str__(): this method gives the user a more readble placement description.
    
    """
    

    def __init__ (self, x = 0, y = 0):
        """
        Initializing a shape object with the coordinates thats given. 

        Args: 
            x (float): x coordinates. 
            y (float): y coordinates.

        Error raise:
        TypeErorr: this Error gets raised if x or y is not a number.
        """
        
        if not isinstance(x, (int, float)): 
            raise TypeError(f"x has to be a number") 
        if not isinstance(y, (int, float)):
            raise TypeError(f"y has to be a number")
        
    # this is going to store the values of x and y as float values.     
        self._x = float(x) 
        self._y = float(y)


    
    #### note that i got help with this part of the code from a website called https://pynative.com/python-area-perimeter-diagonal-of-square/ ####         
    @property
    def area(self) -> float :     
        """This property has to be implemented in the subclass"""
        raise NotImplementedError("the underclass has to be implemented for area") 
        
    @property
    def perimeter(self) -> float:
        """This property has to be implemented in the subclass"""
        raise NotImplementedError("the underclass has to be implemented for perimeter") 

    
    @property 
    def x(self) -> float :   
        """This property gives read only accsess to the x coordinate"""
        return self._x
            
    @property
    def y(self) -> float :   
        """This property gives read only accsess to the y coordinate"""
        return self._y

     
    def translate(self, move_in_x_coordinate, move_in_y_coordinate): 
        """ 
        Moves the shape by adding a value to x and y

        arguments:
        move_in_x_coordinate (float): added value to x.
        move_in_y_coordinate (flaot): added value to y

        """
        
        # Note!! i got stuck here beacuse i did not write the if not isinstance part, 
        # a classmate helped me with this part.
        if not isinstance(move_in_x_coordinate, (int, float)):
            raise TypeError(f"move_in_x_coordinate has to be a number or decimal value")
        if not isinstance(move_in_y_coordinate, (int, float)):
            raise TypeError(f"move_in_y_coordinate has to be a number or decimal value")
          
        self._x += move_in_x_coordinate
        self._y += move_in_y_coordinate   


      # this part of the code bellow is  equality and comparison operators.
    def __eq__(self, other) -> bool :
        if not isinstance(other, Shape):
            return False 
        return self.area == other.area
         
      
    def __lt__(self, other) -> bool :
        if not isinstance(other, Shape):
            return False 
        return self.area < other.area 

   
    def __gt__(self, other) -> bool :  
        if not isinstance(other, Shape):
            return False
        return self.area > other.area

    
    def __le__(self, other) -> bool :
        if not isinstance (other, Shape):
            return False 
        return self.area <= other.area 
    
    def __ge__(self, other) -> bool : 
        if not isinstance (other, Shape):
            return False 
        return self.area >= other.area 
    # this repr is for other developers
    
    def __repr__(self) -> str: 
        return f"shape(x = {self._x}, y = {self._y})"
    
    # this code is for a more readable string showing the position.
    def __str__(self) -> str:
        return f" shape placement is : ({self._x}, {self._y})" 
    
    
         
          
    
    

        
                







           
    
        

            
