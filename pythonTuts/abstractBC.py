# from abc import ABCMeta , abstractmethod

from  abc import ABC ,abstractmethod
# class Shape(metaclass=ABCMeta):
class Shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Ractangle"
    sides = 4
    def __init__(self):
        self.langth = 6
        self.breadth = 7

    def printarea(self):
        return self.langth * self.breadth


rec1 = Rectangle()
print(rec1.printarea())

# trys = Shape()  // We cant create abstract base class object


