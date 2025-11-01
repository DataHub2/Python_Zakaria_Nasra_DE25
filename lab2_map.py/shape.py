
class Shape:
    """ This is the base class (parent class) 
    
    it gives the other classes that i have med functionallity. """
    

    def __init__ (self, x = 0, y = 0):
        #this part will check if the x and y values are numbers
        #if not it will show somthing is wrong withh Error message
        if not isinstance(x, (int, float)): 
            raise TypeError(f"x has to be a number") 
        if not isinstance(y, (int, float)):
            raise TypeError(f"y has to be a number")
        
    # this is going to store the values of x and y as float values, beacuse the positions have decimal in them 
    # this is privat beacause i would like to control how the values are set in the code.    
        self._x = float(x) 
        self._y = float(y)


    # this lines bellow will create property thst is a read only property 
    #### note that i got help with this part of the code from a website called pynative.com ####  
                
     # the area method has to ba used in the underclass 
    @property
    def area(self):     
        raise NotImplementedError("the underclass has to be implemented for area") 
        
    # the perimeter method has to ba used in the underclass 
    @property
    def perimeter(self):
        raise NotImplementedError("the underclass has to be implemented for perimeter") 

     # this property gives read only access to the x coordinate
    @property 
    def x(self):   
        return self._x
        
    # this property gives read only access to the y coordinate    
    @property
    def y(self):   
        return self._y

    # moves the shape position by adding the value for x and y 
    def translate(self, move_in_x_coordinate, move_in_y_coordinate): 
        
        
        # Note!! i got stuch here beacuse i did not write the if not isinstance part, a classmate helped me with this part
        if not isinstance(move_in_x_coordinate, (int, float)):
            raise TypeError(f"move_in_x_coordinate has to be a number or decimal value")
        if not isinstance(move_in_y_coordinate, (int, float)):
            raise TypeError(f"move_in_y_coordinate has to be a number or decimal value")
        
        # this part is going to move the shape depending on the value that giis inputed   
        self._x += move_in_x_coordinate
        self._y += move_in_y_coordinate   


      
    def __eq__(self, other):
        if not isinstance(other, Shape):
            return False 
        return self.area == other.area
         
     # this looks to see if one shape has a smaller area then the other shape 
    def __lt__(self, other):
        if not isinstance(other, Shape):
            return False 
        return self.area < other.area 

    # checks to see if one shape has a greater area then the other shape
    def __gt__(self, other):  
        if not isinstance(other, Shape):
            return False
        return self.area > other.area

    # this checks if one shape has smaller or equal area then other shape
    def __le__(self, other):
        if not isinstance (other, Shape):
            return False 
        return self.area <= other.area 
    # this is meant to check if area greater then or equal to other shape
    def __ge__(self, other): 
        if not isinstance (other, Shape):
            return False 
        return self.area >= other.area 
    # this repr is for other developers
    def __repr__(self): 
        return f"shape(x = {self._x}, y = {self._y})"
    
    # this code is for a more readable string showing the position.
    def __str__(self):
        return f" shape placement is : ({self._x}, {self._y})" 
    
    
         
          
    
    

        
                







           
    
        

            
