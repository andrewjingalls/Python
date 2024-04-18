def my_func():
    L1 = []
    L2 = []
    L3 = []
    L1 = input('Enter a list of numbers: ').split(',')
    L2 = input('Enter another list of numbers: ').split(',')
    for i in L1:
        if i in L2:
            L3.append(i)
    
    return L3
print(my_func())
