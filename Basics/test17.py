lst = ['Anil', 'Amol', 'Aditya', 'Avil', 'Alka']
print(lst)

lst.insert(2, 'Anuj')
print(lst)

lst.append('Zulu')
print(lst)

del(lst[4])
print(lst)

lst[0] = 'AnilKumar'
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)

print('New Program')

lsto = [1, 3, 5, 7, 9]
lste = [0, 2, 4, 6, 8]

lstc = lsto + lste

lstc.insert(0, 11)
lstc.insert(1, 17)
lstc.insert(2, 29)

print(lstc)
print('Size: ', len(lstc))

lstc[len(lstc) - 3:len(lstc)] = [100, 200, 300]
print(lstc)
