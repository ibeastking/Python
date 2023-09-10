
#! weight converter

weight = float(input('Enter Weight: '))
category = input('L(pounds) or K(Kilograms)')

if (category == 'L' or category == 'l'):
    weight = weight * 0.45359237
    print(f"Your weight in Pounds is {weight}")
elif (category == 'K' or category == 'k'):
    weight = weight * 2.2046226218
    print(f"Your weight in Kilograms is {weight}")
else:
    print('Invalid Input')
