grades = [78, 93, 95, 74, 85]
grades = [i+10 for i in grades]
print(grades)


names = ["Sara", "bob", "jeff", "alex"]
names = [i.capitalize() for i in names]
print(names)



cities = ["Rome", "Paris", "Portland", "NY"]
newlist=[]
for x in cities:
    if "a" in x:
        newlist.append(x)
print(newlist)



squares = []                    #prints all the squares 0-9
for i in range(10):
    squares.append(i**2)
print(squares)

squares = [i**2 for i in range(10)] #same thing just smaller
print(squares)



nums = [65, 78, 98, 100, 77]
for i,j in enumerate(nums):
    print(f'{i}:{j}')
