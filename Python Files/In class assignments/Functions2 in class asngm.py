
def find_A(x):
    count1 = x.count('A')
    count2 = x.count('a')
    return count1+count2      
name = input('What is your name? ')
print(find_A(name))





def num_woofs(x):
    return('woof woof  '*x)
         
num = int(input('Enter a number: '))
print(num_woofs(num))




def average(x1,x2):
    y = (x1+x2)/2
    return(y)

num1 =int(input('Enter a number: '))
num2 = int(input('Enter second number: '))
print(average(num1,num2))
