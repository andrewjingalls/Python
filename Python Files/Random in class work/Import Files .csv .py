import csv
f=open('project.csv')
a=csv.reader(f)
count=0
for i in a:
    for j in i:
        if j=="Hangman":
            count+=1
print('Found',count, 'Hangman')

f=open('project.csv')
a=csv.reader(f)
for row in a:
    print(row)
