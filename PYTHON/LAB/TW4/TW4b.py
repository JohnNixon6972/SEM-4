# Create a class Polygon that uses the initializer to initialize the number of sides
# and the default value of zero for each side as instance variables. It also defines
# member functions to read values for each side and displays the values. Derive two
# classes viz., Triangle and Rectangle from Polygon class. The two derived classes
# define member functions to compute area and display area.

import math


class Polygon():  # creating Parent class "Polygon"
    # creating constructor for parent class , to assign values when object is created
    def __init__(self, sides=0):
        self.sides = sides
        self.val_sides = []

    def read(self):  # mehtod to read the values of the sides
        print("Enter the values  of sides :: ")
        for i in range(self.sides):
            self.val_sides.append(int(input()))

    def Display(self):  # method to display the values of the sides
        print("Sides are :: ", *self.val_sides)


class Triangle(Polygon):  # creating class "Triangle" that inherits class "Polygon"
    def __init__(self):  # constructor for class "Triangle"
        # calling the constructor of parent class by passing "3" as the value for "sides"
        Polygon.__init__(self, 3)
        # calling the parent class method to red the values of sides
        Polygon.read(self)
        # calling the parent class method to display the value of sides
        Polygon.Display(self)

    def compute_area(self):  # method to compute area of triangle
        a, b, c = self.val_sides

        perimeter = (a+b+c)/2

        area = math.sqrt(perimeter*((perimeter - a) *
                         (perimeter - b)*(perimeter - c)))

        return area

    def Display(self):  # Method to Display the area of triangle
        print("Area of Triangle is :: ", self.compute_area())


class Rectangle(Polygon):  # creating class "Rectangle" that inherits calss "Polygon"
    def __init__(self):  # constructor for class "Rectangle"
        # calling the constructor of parent class by passing "2" as the value for sides as opposite sides of a rectangle are same
        Polygon.__init__(self, 2)
        # calling the parent class method to read the values of sides
        Polygon.read(self)
        # calling the parent class method to display the value of sides
        Polygon.Display(self)

    def compute_area(self):  # method to compute area of a rectangle
        l, b = self.val_sides

        area = l*b

        return area

    def Display(self):  # method to display the area of rectangle
        print("Area of Rectangle is :: ", self.compute_area())


def main():  # main function
    print("Created Trinagle Object :: ")
    tri_obj = Triangle()  # creating objcet for class "Trinagle"
    tri_obj.compute_area()  # calling their respective methods
    tri_obj.Display()

    print()

    print("Created Trinagle Object ")
    rect_obj = Rectangle()  # creating object for class "Rectangle"
    rect_obj.compute_area()  # calling their respective methods
    rect_obj.Display()


if __name__ == "__main__":  # condition to check if there is a main function in the program
    main()  # calling the main() function to start the execution of the program
