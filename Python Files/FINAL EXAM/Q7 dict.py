my_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
my_dict[6]='six'

def dict():
    x = int(input('Enter a num 1-6: '))
    return my_dict[x]

print(dict())
