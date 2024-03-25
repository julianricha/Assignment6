#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Shape:
    def area(self):
        raise NotImplementedError("Not Implemented Error")
        
    def perimeter(self):
        raise NotImplementedError("Not Implemented Error")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
        
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
        
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        
    def area(self):
        return 0.5 * self.base * self.height
        
    def perimeter(self):
        return self.base + self.side1 + self.side2


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5, 5)]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")


# In[ ]:




