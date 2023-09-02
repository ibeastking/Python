import random


def create_array(a, b, c):
    lst = []
    for i in range(0, a):
        lstb = []
        for j in range(0, b):
            lstc = []
            for k in range(0, c):
                lstc.append(random.randint(1, 9))
            lstb.append(lstc)
        lst.append(lstb)

    return lst


lst = []
a = (int)(input('Enter Number of Rows:'))
b = (int)(input('Enter Number of Columns: '))
c = (int)(input('Enter Number of Heights: '))

lst = create_array(a, b, c)
print(lst)
