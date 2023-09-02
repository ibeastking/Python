
n = 1
for n in range(1, 301, 1):
    i = 2

    for i in range(i, n, 1):
        if(n % i == 0):
            break
        else:
            i = i + 1
            continue

    if(i == n):
        print(i, end=" ")
