from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("This is creating method")
    
    def area(self):
        print("This is creating method")
    
obj = Circle(7)