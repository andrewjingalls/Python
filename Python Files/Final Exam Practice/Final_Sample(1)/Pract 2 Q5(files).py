def is_even(x):
    if x%2==0:
        return True
    else:
        return False


f = open('numbers.txt', 'w')
f.write('1\n2\n3\n4\n5')
f.close()
f=open('numbers.txt', 'r')
file=open('evenNumbers.txt', 'w')


for line in f:
    num = int(line)
    if is_even(num)==True:
        file.write(str(num))
        file.write('\n')






f.close()
file.close()
