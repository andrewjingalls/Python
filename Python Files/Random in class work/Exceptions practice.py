user_input=input('Enter # ')
while user_input != 'end':
    try:
        divisor= int(user_input)
        print(60//divisor)
    except ValueError:
        print('That wasn\'t a number. \nEnter a number.')
    except ZeroDivisionError:
        print('Oops, try non-zero numbers')

    user_input = input('Enter #')
print('OK')
