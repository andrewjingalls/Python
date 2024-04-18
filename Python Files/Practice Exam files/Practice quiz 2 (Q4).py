answer = 'start'
while answer != 'quit':
    number = int(input('Enter a number: '))
    if number%2 == 0:
        print('Even number!')
    else:
        print('Odd number!')
    answer= input('continue or quit?')
