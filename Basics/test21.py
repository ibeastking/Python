from turtle import end_fill


n = (int)(input('Enter Number of rows and columns: '))
m = (2 * n) - 2

i = 0
for i in range(0, n, 1):
    for j in range(0, m, 1):
        print(end=' ')

    m = m - 1

    j = 0
    for j in range(0, i+1, 1):
        print(i+1, end=' ')
    print(' ')

i = 0
for i in range(n, -1, -1):
    for j in range(m, 0, -1):
        print(end=' ')

    m = m + 1

    j = 0
    for j in range(0, i+1, 1):
        print('*', end=' ')

    print(' ')
