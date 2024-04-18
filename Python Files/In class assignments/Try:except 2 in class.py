try:
    x=input('What file do you want to open? ')
    f=open(x, 'r')
    if x == 'corruptfile.txt':
        raise FileNotFoundError
    print(f.read())
    f.close()
except FileNotFoundError:
    print('Wrong corrupted file')
finally:
    print('Good Job')
