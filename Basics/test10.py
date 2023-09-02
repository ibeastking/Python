# for loop

i = 1

while i <= 3:
    j = 1
    while j <= 3:
        k = 1
        while k <= 3:
            if(i == j or j == k or i == k):
                k = k + 1
                continue
            else:
                print(i, j, k)
            k = k+1
        j = j+1
    i = i + 1
