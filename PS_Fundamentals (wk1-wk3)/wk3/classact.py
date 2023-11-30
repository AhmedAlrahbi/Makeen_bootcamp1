#ICA,shape area using classes 28112023
class Shape:
    def __init__(self, color = None, name= None):
        self.color = color
        self.name = name

    def __str__(self):
        print(f"im a {self.name} from class Shape")
    def area(self):
        print("im Area function from Shape")
class Square(Shape):
    def __init__(self, color, name, length):
        super().__init__(color, name)
        self.length = length


    def area(self):
        squArea = self.length**2
        print(f"The area of the {self.name} is ", squArea)
    def __str__(self):
        print(f"im a {self.name} from class Square and my color is {self.color}")

class Circle(Shape):
    def __init__(self,color, name, rad ):
        super().__init__(color, name)
        self.rad = rad
    def area(self):
        cirArea = 3.14*self.rad**2
        print(f"The area of {self.name} is ",cirArea)
    def __str__(self):
        print(f"im a {self.name} from class Circle and my color is {self.color}")


s1 =Square("Blue","Square", 3)

s1.__str__()
s1.area()
print("\n----------------------\n----------------------\n")
c1 = Circle("red","Circle", 5)
c1.__str__()
c1.area()










