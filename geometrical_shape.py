# find the area and perimeter of circle,square, rectangle,triangle
pi=3.14
def circle_area(radius):
    return pi*radius**2
print(circle_area(2))
def circle_perimeter(radius):
    return 2*pi*radius
print(circle_perimeter(3))
def rectangle_area(length,breadth):
    return length*breadth
def rectangle_perimeter(length,breadth):
    return 2*(length+breadth)
def square_area(side):
    return side*side
def square_perimeter(side):
    return 4*side
def triangle_area(base,height):
    return 1/2*base*height
def triangle_perimeter(a,b,c):
    return a+b+c


