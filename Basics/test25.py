dict = {}

i = 0
for i in range(0, 3):
    word = input('Enter String: ')
    lst = [0] * 26

    for ch in word:
        if(ord(ch) >= 97 and ord(ch) <= 122):
            lst[ord(ch) - 97] = lst[ord(ch) - 97] + 1
        if(ord(ch) >= 65 and ord(ch) <= 90):
            lst[ord(ch) - 65] = lst[ord(ch) - 65] + 1

    dict[word] = lst

print(dict)
