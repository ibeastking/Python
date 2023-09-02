n = (int)(input('Enter number of rows and columns: '))
i, j = 1, 1

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if (i >= j):
            print(i, end=' ')
    print('\n')

for i in range(1, n+1, 1):
    for j in range(1, n+1, 1):
        if (i <= j):
            print(i, end=' ')
    print('\n')

m = (2 * n) - 2

for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m = m - 1

    for j in range(0, i+1):
        print(i+1, end=' ')
    print(' ')

for i in range(n, -1, -1):
    for j in range(m, 0, -1):
        print(end=' ')
    m = m + 1

    for j in range(0, i+1):
        print(i+1, end=" ")
    print(' ')
