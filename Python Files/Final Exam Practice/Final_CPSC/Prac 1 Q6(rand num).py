import random
def ran_num():
    x = int(input('Enter a low number: '))
    y = int(input('Enter a high number: '))
    comp_num = random.randint(x, y)
    return comp_num

print(ran_num())
