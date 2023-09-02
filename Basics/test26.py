import random

dict = {}

for i in range(0, 3):
    name = input('Enter Student Name: ')
    lst = []

    j = 0
    for j in range(0, 3):
        mrk = random.randint(1, 100)
        lst.append(mrk)

    dict[name] = lst

for k, l in dict.items():
    i = 0
    sum = 0
    for i in range(0, len(l)):
        sum = sum + l[i]

    avg = sum / 3
    lst = [sum, avg]

    dict[k] = lst

print(dict)

portfolio = {
    'accounts': ['sbi', 'iob'],
    'shares': ['hdfc', 'icici', 'tm', 'tcs'],
    'ornaments': ['10gm gold', '1 kg silver']
}

portfolio['mf'] = ['relaince', 'absl']

print(portfolio)

portfolio['accounts'] = ['axis', 'bob']

print(portfolio)
