name = 'mohammed'
user = input('Enter your name: ')

num = 2

while name != user:
    if num != 0:
        print('Username not found error try again...')
        num -= 1
        user = input('Enter your name: ')
    else:
        print('Try again later')
        break
else:
    print('welcome')