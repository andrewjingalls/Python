import csv
my_grocery_items=open('grocery.csv', 'w')
x = csv.writer(my_grocery_items)
x.writerows([['Kiwi', 'Apple', 'Lemon'],[2.99,3.15,1.99]])
my_grocery_items.close()


