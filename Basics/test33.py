import random


def func(n):
    return n**2


lst = []
K = random.randint(1, 10)
M = random.randint(1, 10)
S = 0

for i in range(1, K+1):
    lstt = []
    for j in range(0, i):
        n = random.randint(1, 10)
        lstt.append(n)

    S = S + func(max(lstt))
    lst.append(lstt)

S = S % M

print(lst)
print('Max number will be {}'.format(S))
