import operator

tpl1 = ('Bananas', 11.94)
tpl2 = ('Mango', 32.11)
tpl3 = ('Oranges', 12.88)
tpl4 = ('Apple', 27.33)

lst = [tpl1, tpl2, tpl3, tpl4]

i = 0
for i in range(0, len(lst)):
    print(lst[i])

print(sorted(lst, key=operator.itemgetter(1)))
