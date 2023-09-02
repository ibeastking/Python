import math

p = math.pi / 180

for t in range(0, 190, 10):
    y = 0.5 + (0.6366*math.cos(p*t)) - \
        (0.2122*math.cos(3*p*t)) + (0.1273*math.cos(5*p*t))
    print(t, ':', y, ':', 20*math.log(math.fabs(y), 10))
