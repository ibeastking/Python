import random
import math

x1 = (int)(((random.random())*10)/1)
y1 = (int)(((random.random())*10)/1)

x2 = (int)(((random.random())*10)/1)
y2 = (int)(((random.random())*10)/1)

x3 = (int)(((random.random())*10)/1)
y3 = (int)(((random.random())*10)/1)

print(x1, y1, x2, y2, x3, y3)

l12 = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
l31 = math.sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2))
l23 = math.sqrt(pow((x2 - x3), 2) + pow((y2 - y3), 2))

if((l12 + l23 == l31) or (l12 + l31 == l23) or (l23 + l31 == l12)):
    print('The three points lie on the same line.')
else:
    print('The three points do not lie on the same line')

# r stands for radius
r = 5
x, y = 3, 4

# l stands for length

l = math.sqrt(pow((x1 - x), 2) + pow((y1 - y), 2))

if(l == 5):
    print('The point lies on the circle')
elif(l > 5):
    print('The point lies outside the circle')
else:
    print('The point lies inside the circle')
