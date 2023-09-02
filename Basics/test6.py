import math
import random

w = (int)((random.random()*10) % 2)
x = (int)((random.random()*10) % 2)
y = (int)((random.random()*10) % 2)
z = (int)((random.random()*10) % 2)

print(w, x, y, z)

a = w and x and y and z
b = w or x or y or z

print(a, b)
