import math

radius, length, breadth = input('Enter radius, length, breadth: ').split()

r = (int)(radius)
l = (int)(length)
b = (int)(breadth)


print('Circumference: {0} \nPerimeter: {1}'.format(
    (2 * (math.pi) * r), (2 * (l + b))))
