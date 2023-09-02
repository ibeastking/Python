from operator import truediv
import random

# a is the input
a = (int)(random.random()*100)

if(a < 10):
    b = 20
else:
    b = 30

print('The value of b is', (str)(b))

# time
time = (int)((random.random()*10) % 2) * 12

if(time < 12):
    print('Morning')
if(time >= 12):
    print('Afternoon')

# marks
marks = (int)((random.random())*100)
print(marks)

if(marks >= 70):
    flag = True
else:
    flag = False

print(flag)
