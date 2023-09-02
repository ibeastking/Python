def fun(n):
    lower, upper = 0, 0
    for i in range(0, len(n)):
        if(n[i] >= 'a' and n[i] <= 'z'):
            lower = lower + 1

        if(n[i] >= 'A' and n[i] <= 'Z'):
            upper = upper + 1

    return upper, lower


n = (input('Enter String: '))
x, y = fun(n)

print('Number of Upper Characters: {}\nNumber of Lower Characters: {}'.format(x, y))


def fun1(n):
    return n, n**2, n**3, n**4


n = (int)(input('Enter Number: '))
tpl = fun1(n)

print(tpl)
