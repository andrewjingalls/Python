vowels=['a', 'e', 'i', 'o', 'u']
def wordToPig(x):
    if x[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
        print("".join([x[1::],x[0], "ay"]))
    else:
        print(x+'yay')



def nameToPig(firstName,lastName):
    wordToPig(firstName)
    wordToPig(lastName)



firstName= input('What is your first name: ')
lastName = input('What is your last name: ')
nameToPig(firstName, lastName)

file=open('Name.txt', 'w')
file.writelines(['John\n', 'Doe'])
file.close()
file=open('Name.txt.', 'r')
x = file.read()
y=x.split()
print(y)
nameToPig(y[0],y[1])
