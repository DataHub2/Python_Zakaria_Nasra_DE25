class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.age = age

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"age must be of type int, not {type(value)}")

        if value < 0 or value > 124:
            raise ValueError(f"age must be between 0 and 123, not {value}")
        
        self._age = value
    
    def say_hi(self) -> None:
        print(f"{self.name} says hi")


p1 = Person("Örjan", 25)

try:
    # setter not defined
    p1.name = "Börje"
except AttributeError as err:
    print(err)

# used getter
print(p1.name)

p1.say_hi()

try: 
    p2 = Person("Ceda", age = -5)
except ValueError as err:
    print(err)

try:
    p3 = Person("Doddo", age = "femtio")
except TypeError as err:
    print(err)



# implementr student 

class Student(Person):
    def __init__ (self, name: str, age: int, language: str):
        # this goes to the parent and uses its __init__
        super().__init__(name, age) # super means we get something from the parent class
        self.language = language

    def say_hi(self):
        print(f"student says hi in language {self.language}")


try:
    s1 = Student("Björn", 124, language = "Norska")
except ValueError as err:
    print(err)

s2 = Student("Dan", 37, language = "Pyhon")  
s2.say_hi()  


from Old_coins import OldCoinsStash
class viking(Person):
    def __init__ (self, name: str, age: int, weapon: str):
        super().__init__(name, age)
        
        # composition - has a relationship
        self.stash = OldCoinsStash(name)

viking_ubbe = viking("Ubbe", 35, "axe") 
viking_ubbe.say_hi()
print(viking_ubbe.stash)       

viking_ivar = viking("Ivar", -4, "sword")



    
        
       

