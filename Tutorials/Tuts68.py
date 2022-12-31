
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    # def printarea(self):
    #     return 0
    def printdetail(self):
        # self.kaka=578
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
        self.kaka = 999

    def printarea(self):
        return self.length * self.breadth

    def printdetail(self):
        return self.kaka

rect1 = Rectangle()
print(rect1.printdetail())

