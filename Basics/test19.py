import random

lst = []

i = 0
for i in range(0, 20, 1):
    lst.append(random.randint(1, 10))

n = (int)(input('Enter Number: '))

print(lst.count(n))
print(lst)

m = (int)(input('Enter Number: '))

i = 0
for i in range(0, 20, 1):
    if(lst[i] == n):
        lst[i] = m

print(lst)

lsto = []
lste = []

i = 0
for i in range(0, 20, 1):
    if(lst[i] % 2 == 0):
        lste.append(lst[i])
    else:
        lsto.append(lst[i])

print(lsto)
print(lste)
