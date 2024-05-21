# write a python class named Rectangle to represent a rectangle shape. The class should have the following functionalities:
# A method named set_dimensions that takes two parameters width and height and set the attributes of the rectangle object accordingly.
# A method named area that calculates and returns the area of the reactangle 
# A  method named perimeter that calculated and returns the perimeter of the rectangle 
# Use this to create objects of the class and print the width, height, area and perimeter. 

class Rectangle:

    def __init__(self, height, width):
        print(f"A rectange is created with height: {height} and widht: {width}")
        self.height = height
        self.width = width

    def set_dimensions(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
    

# objects of this class 
rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(5, 7)
rectangle3 = Rectangle(2, 8)
# rectangle1.set_dimensions(4, 3)
# print("The height and width are: ",rectangle1.height,"and",rectangle1.width)
# print("The area is: ", rectangle1.area())
# print("The perimeter is: ", rectangle1.perimeter())
