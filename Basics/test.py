num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
first = input("Enter the first name: ")
middle = input("Enter the middle name: ")
last = input("Enter the last name: ")

# * Add two numbers
sum = num1 + num2

# * Display the sum
print('The sum of {} and {} is {}'.format(num1, num2, sum))
print('The full name {0} , {1}, {2} is {3}'.format(
    first, middle, last, first+middle+last))
