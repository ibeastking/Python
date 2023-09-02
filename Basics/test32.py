import random

dict = {}

for i in range(1, 10):
    lst = []
    for j in range(0, 5):
        lst.append(random.randint(1, 100))

    name = input('Enter Student Name: ')
    dict[name] = lst

print(dict)
