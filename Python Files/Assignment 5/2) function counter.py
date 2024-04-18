def counter(x):
    count_upper=0
    count_lower=0
    for i in x:
        if i.isupper():
            count_upper+=1
    for i in x:
        if i.islower():
            count_lower+=1
    print('Total capital letters:', count_upper)
    print('Total lowercase letters:', count_lower)

sent= input('Write a sentence: ')
print(counter(sent))
