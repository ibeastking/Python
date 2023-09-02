import math

# q stands for quantity
q = (int)(input("Enter Quantity: "))

# p stands for price
p = (float)(input("Enter Price: "))

total = q * p

if(total > 1000):
    print('Previous Total: Rs.' + (str)(total))
    total = total * 0.1
    print('Discounted Total: Rs.', total)
else:
    print('Total: Rs.', total)
