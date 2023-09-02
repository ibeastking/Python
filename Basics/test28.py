dict = {}

for i in range(0, 10):
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    dict[username] = password

u = input('Enter Username: ')
p = input('Enter Password: ')

for key, value in dict.items():
    if(key == u):
        if(value == p):
            print('Valid Username and Password')
