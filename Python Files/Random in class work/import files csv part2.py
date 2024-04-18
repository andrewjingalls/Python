import csv
f=open('groceries.csv')
myData=[['Apple', 'Pear', 'Orange'], [3, 2.99, 4]]
writer=csv.writer(f)
writer.writerows(myData)
