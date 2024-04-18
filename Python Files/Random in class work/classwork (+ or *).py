x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
answer=input('Add or Multiply? ')
if answer.lower() =='add':  #first way to make sure any type of 'add' works
    print('Answer is:',x+y)
elif answer =='Multiply' or answer =='MULTIPLY' or answer =='multiply': #another way to make sure all versions of multiply work
    print('Answer is:',x*y)
else:
    print('Invalid word')
