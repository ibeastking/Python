import math

p = math.pi

for t in range(0, 190, 10):
    y = 0.75-(0.45*math.cos(t*p/180)) - (0.318*math.cos(t*p/90)) - \
        (0.15*math.cos(t*p/60)) + (0.09*math.cos(t*p/36))
    print(t, ':', y, ':', 20*math.log(math.fabs(y), 10))
