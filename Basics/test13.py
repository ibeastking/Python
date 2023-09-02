from re import I


m = 1

for m in range(1, 1000, 1):
    n = 0
    n = m

    rev = 0
    while (n > 0):
        rev = rev + (pow((n % 10), 3))
        n = n // 10

    if rev == m:
        print(m, end=" ")

print('\n')
n = (int)(input('Enter Number: '))

i = 1
for i in range(1, 11, 1):
    m = 0
    m = n * i

    print(n, '*', i, '=', m)
