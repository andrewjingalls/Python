answer = 'start'
while answer.lower() != 'exit':
    num = int(input('Enter a number between 10 and 20: '))
    if 10<=num<=20:
        print('Thank you!')
    else:
        print('Incorrect Answer')
    answer = input('Continue or Exit?')
