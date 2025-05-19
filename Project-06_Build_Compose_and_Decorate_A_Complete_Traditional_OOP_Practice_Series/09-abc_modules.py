# 9. **Abstract Classes and Methods**
# **Assignment:**  
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self , lenght , width):
        self.length = lenght
        self.width = width

    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return f"Rectangle Area: {self.area()}"
    

result = Rectangle(7 , 2)
print(result)
print(f"Tha area of Rectangle is {result.area()}")





            

