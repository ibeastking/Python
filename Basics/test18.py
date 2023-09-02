import random

lst = []

n = 0
for n in range(0, 20, 1):
    lst.append(random.randint(10, 100))

n = 0
for n in range(0, 20, 1):
    print(lst[n])

n = 0
for num in lst:
    if((num >= 20) and (num <= 50)):
        lst.remove(num)

lst.sort()
print(lst)
