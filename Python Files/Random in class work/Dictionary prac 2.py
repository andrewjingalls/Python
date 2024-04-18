dict= {'France':'Paris', 'Spain':'Madrid', 'Italy':'Rome'}
for key,value in dict.items():
    print('What is the capital of',key)
    x=input()
    if x == dict[key]:
        print('Good job')
    else:
        print('Correct answer is ',value)

