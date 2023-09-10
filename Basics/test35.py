
#! pattern printing

n = int(input("Enter Number: "))

for i in range(0, n):
    for j in range(0, n):
        if i+j >= n-1:
            print('#', end="")
        else:
            print(' ', end='')
        if j == n-1:
            print()
