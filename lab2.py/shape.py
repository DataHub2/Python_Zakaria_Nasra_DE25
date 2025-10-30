# this will be the base class for the diffrent geometric shapes
 
class Shape:
    """ this is the base class (parent class) """
    
    


    def __init__ (self, x = 0, y = 0):

        if not isinstance(x, (int, float)): #this part will check if the x and y values are numbers
            raise TypeError(f"x has to be a number") #if not it will show somthing is wrong withh Error message
        if not isinstance(y, (int, float)):
            raise TypeError(f"y has to be a number")
        
        # this is going to store the values of x and y as float values, beacuse the positions have decimal in them 
        self._x = float(x) # this is privat beacause i would like to control how the values are set in the code. 
        self._y = float(y)


        # this lines bellow will create property thst is a read only property 
                #### note that i got help with this part of the code from a website called pynative.com ####  
    @property
    def area(self):     
        raise NotImplementedError("the underclass has to be implemented for area") # the area method has to ba used in the underclass 
        
        
    @property
    def perimeter(self):
            raise NotImplementedError("the underclass has to be implemented for perimeter") # the perimeter method has to ba used in the underclass


    @property 
    def x(self):   #  this property gives read only access to the x coordinate
            return self._x
        
        
    @property
    def y(self):   #  this property gives read only access to the y coordinate
            return self._y

        

    def translate(self, move_in_x_coordinate, move_in_y_coordinate): # this method will move the shape in the x and y coordinate
            #the property bill move the shapes posiotion when a number is added
            
            
            # Note!! i got stuch here beacuse i did not write the if not isinstance part, a classmate helped me with this part
            if not isinstance(move_in_x_coordinate, (int, float)):
                raise TypeError(f"move_in_x_coordinate has to be a number or decimal value")
            if not isinstance(move_in_y_coordinate, (int, float)):
                raise TypeError(f"move_in_y_coordinate has to be a number or decimal value")
            
            
            # this part is going to move the shape depending on the value that is inputed 
            
            self._x += move_in_x_coordinate
            self._y += move_in_y_coordinate   


     # the property looks if two shapes have the same area 
    def __eq__(self, other):
         if not isinstance(other, Shape):
              return False 
         return self.area == other.area
         

     # this looks to see if one shape has a smaller perimiter then the other shape 
    def __lt__ (self, other):
         if not isinstance(other, Shape):
              return False 
         return self.perimeter < other.perimeter 

    
    def __gt__ (self, other): # checks to see if one shape has a greater area then the other shape 
         if not isinstance(other, Shape):
              return False
         return self.area > other.area

    # this checks if one shape has smaller or equal perimeter then other shape
    def __le__(self, other):
         if not isinstance (self, other):
              return False 
         return self.perimeter <= other.perimeter 
              
          
    
    

        
                







           
    
        

            
