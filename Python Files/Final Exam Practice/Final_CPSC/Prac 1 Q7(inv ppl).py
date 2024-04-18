num_people = int(input('How many people do you want to invite to party? '))
if num_people <10:
    for i in range(num_people):
        name=input('Enter the name of a guest: ')
        print(name, 'has been invited')

elif num_people >=10:
    print('Too many people')
