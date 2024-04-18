subjects = ['Math', 'Science', 'History', 'PE', 'English', 'Spanish']
print(subjects)
least_fav = input('Which subject is your least favorite: ')
subjects.remove(least_fav)
print(subjects)


invite= input('Who are 3 people you want to invite? ').split()
add = input('Do you want to add any more people? ')
while add.lower() == 'yes':
    people_added = input('Who do you want to add? ')
    invite.append(people_added)
    print(invite)
    add = input('Do you want to add any more people? ')
else:
    print('You have invited', len(invite), 'people to the party')
