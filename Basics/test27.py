import random

dict1 = {}
dict2 = {}

# tp stands for total price
# tq stands for total quantity

tp, tq = 0, 0

for i in range(0, 5):
    grocery = input('Enter Grocery Item: ')

    # p stands for price
    p = random.randint(1, 100)
    tp = tp + p

    # q stands for quantity
    q = random.randint(1, 10)
    tq = tq + q

    dict1[grocery] = p
    dict2[grocery] = q

print('Total Bill: Rs {}'.format(tq * tp))
