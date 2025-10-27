# this will be the parent class for the diffrent geometric shapes
class Shape:
    # this is the parent class
    def __init__ (self, x = 0, y = 0):

        if not isinstance(x, (int, float)): #this part will check if the x and y values are numbers
            raise TypeError(f"x has to be a number") #if not it will show somthing is wrong withh Error message
        if not isinstance(y, (int, float)):
            raise TypeError(f"y has to be a number")
        
        # this is going to store the values of x and y as float values, beacuse the positions have decimal in them 
        self._x = float # this is privat beacause i would like to control how the values are set in the code. 
        self._y = float 

        
      
