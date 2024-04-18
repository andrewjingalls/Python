user_input = ''
while user_input != 'q':
    try:
        age = int(input('Enter age: '))
        if age<0:
            raise ValueError('Invalid age')
            age= int(input('Enter your age: '))
        height = int(input('Enter height(in inches): '))
        if height <=0:
            raise ValueError('Invalid Height')
            height = int(input('Enter height(in inches): '))
        user_input= input('Type q if you want to quit or C to continue')
    except ValueError as x:
        print(x)
