b = '1111'

n = len(b)
i, x = 0, 0

for i in range(i, n, 1):
    x = x + (int)(b[i]) * pow(2, i)

print(x)

i = 65

for i in range(i, 123, 1):
    if((i >= 65 and i < 91) or (i >= 97 and i <= 122)):
        x = (chr)(i)
        print(x, end=" ")
        if(i == 90):
            print('\n')
    else:
        continue

print('\n')

i = 1
for i in range(i, 50, 2):
    print(i, end=" ")

s = 'Nagpur-440010'

# na stands for number of alphabets and nd stands for number of digits

i, na, nd = 0, 0, 0
for i in range(i, len(s), 1):
    if((s[i] >= 'A' and s[i] < 'Z') or (s[i] >= 'a' and s[i] <= 'z')):
        na = na + 1
    if((s[i] >= '0') and (s[i] <= '9')):
        nd = nd + 1

print('\n')
print(na, nd)

n = (int)(input('Enter Number: '))
rev = 0

while n > 0:
    rev = rev * 10 + (n % 10)
    n = n // 10

print(rev)

n = (int)(input('Enter Number: '))
i = 1
fact = 1

for i in range(i, n+1, 1):
    fact = fact * i

print(fact)
