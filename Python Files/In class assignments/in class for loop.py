invited = int(input('How many people do you want to invite to the party? '))
if invited <10:
    for i in range(invited):
        name = input('What is their name? ')
        print(name, 'has been invited')
if invited >=10:
    print('Too many people.')
