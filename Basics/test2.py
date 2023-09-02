import math
import random

x = 9
print(math.sqrt(math.pi))

print(math.fabs(math.pi))

print(math.trunc(math.sqrt(math.pi)))

print(math.ceil(math.sqrt(math.pi)))
print(math.floor(math.sqrt(math.pi)))

print(math.modf(math.sqrt(math.pi)))

print(random.randint(5, 15))
print(hex(random.randint(5, 15)))
print(random.random())

a = 30
b = "OM"

print(a, b)
print(type(a), type(b))  # prints the type of inputted variable
print(id(a), id(b))  # prints the unique id of inputted variable
# prints true if inputted variable and variable type are same else prints false
print(isinstance(a, str), isinstance(b, str))

print(int('341', 8))
