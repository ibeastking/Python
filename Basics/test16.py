import math

start, end, step = (input('Enter Numbers: ')).split()

s = (int)(start)
e = (int)(end)
i = (int)(step)

print(f'Number Square Cube Square root Cube root')
n = 1
for n in range(s, e, i):
    print(f'{n:>4}{n**2:>6}{n**3:>6}{(math.sqrt(n)):{10}.{3}}{(pow(n,1/3)):{10}.{4}}')
