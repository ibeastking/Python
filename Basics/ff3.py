def func(t):
    if(t > 0):
        return func(t-1) * t
    else:
        return 1


n = (int)(input('Enter Number'))
fact = 1
fact = fact * func(n)
print(fact)
