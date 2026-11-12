# Conditions

# if 1 == 2: # 1 == 2 > False
#     print('hello')

# elif 2 >= 10:
#     print('alsalam 3lekm')

# else:
#     print('anta u ar6mk kld')

database = {'lw_w7':'12341234',
            'lw__w6':'mohammed'}
username = input('Enter Your Username: ')
password = input('Enter Your Password: ')
if username not in database.keys():
    print('Username or password is incorrect')
elif password == database[username]:
    print('Welcome Mster', username)
else:
    print('Username or password is incorrect')