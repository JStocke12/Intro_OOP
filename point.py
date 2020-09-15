from math import sqrt

from math import pi

class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


    def abs(self):
        return sqrt(self.x**2 + self.y**2)

class Rectangle:

    p1 = Point(0,0)
    p2 = Point(0,0)

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return (self.p2.x - self.p1.x)*(self.p2.y - self.p1.y)

    def perimeter(self):
        return 2*(self.p2.x - self.p1.x)+2*(self.p2.y - self.p1.y)

class Circle:

    c = Point(0,0)
    r = 0.0

    def __init__(self, c, r):
        self.c = c
        self.r = r

    def area(self):
        return pi*self.r**2

    def perimeter(self):
        return 2*pi*self.r

    def inside(self, p):
        return self.c.dist_to(p) <= r


def main():
    p1 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

    rect = Rectangle(Point(1,1), Point(4,5))
    print("The rectangle defined by the corners ({}, {}) and ({}, {}) has an area of {} and a perimeter of {}.".format(rect.p1.x, rect.p1.y, rect.p2.x, rect.p2.y, rect.area(), rect.perimeter()))

    circ = Circle(Point(-2,3), 2)
    p3 = Point(0, 1)
    print("The circle with radius {} centered at the point ({}, {}) {} ({}, {}) and has an area of {} and a perimeter of {}.")


if __name__ == "__main__":
    main()
