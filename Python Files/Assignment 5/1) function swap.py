def swap(x):
    x[0], x[-1] = x[-1], x[0]
    return(x)

my_list = ['all','good','things','must','end','here']
print(swap(my_list))
