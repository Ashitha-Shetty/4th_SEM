class Rectangle:
   def __init__(self, length, width):
    self.length = length
    self.width = width
   def area(self):
     return self.length * self.width
   def perimeter(self):
      return 2 * (self.length + self.width)
# Creating an object of the Rectangle class
rectangle = Rectangle(4, 6)
# Displaying the area and perimeter of the rectangle
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())