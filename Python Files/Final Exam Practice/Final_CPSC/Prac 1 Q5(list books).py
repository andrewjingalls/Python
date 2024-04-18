names = []
x = input('Enter the names of your three favorite books (seperated by a comma): ')
names=x.split(',')
print(names)
answer = ' '
while answer != 'no':
    answer = input('Do you want to add another?')
    if answer == 'no':
        continue
    y = input('Enter another book: ')
    names.append(y)
else:
    print(names)
    print('Thank you for taking the time to complete this servey')
