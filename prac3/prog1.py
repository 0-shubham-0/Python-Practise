# define shape class with appropriate members to calculate and display area, perimeter of different shapes
class Shape:
    def circle(self, radius):
        area = 3.14 * radius ** 2
        perimeter = 2 * 3.14 * radius
        print("{0} is the area".format(area))
        print("{0} is the perimeter".format(perimeter))

    def rectangle(self, side1, side2):
        area = side1 * side2
        perimeter = (side1 * 2) + (side2 * 2)
        print("{0} is the area".format(area))
        print("{0} is the perimeter".format(perimeter))


shp1 = Shape()
sides = int(input('Number of sides : '))
if sides == 0:
    rad = int(input("Enter Radius"))
    shp1.circle(rad)
elif sides == 4:
    n = int(input("Enter 1 for Square and 2 for rectangle : "))
    if n == 1:
        length = int(input("Enter length of Square : "))
        shp1.rectangle(length, length)
    elif n == 2:
        length = int(input("Enter length of Side 1 : "))
        length1 = int(input("Enter length of Side 2 : "))
        shp1.rectangle(length, length1)

else:
    print("Enter value from 0 or 4")
