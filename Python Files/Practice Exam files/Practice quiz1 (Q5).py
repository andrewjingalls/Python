count= input('Do you want to count up or down? ')
if count.lower() == 'up':
    x = 0
    while x <=10:
        print(x)
        x=x+2
elif count.lower() == 'down':
    x = 10
    while x >=0:
        print(x)
        x=x-2
    
