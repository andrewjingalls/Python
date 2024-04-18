import random
import csv
import math
def open_file(name,count):
    f=open('quiz.csv', 'w')
    x = csv.writer(f)
    x.writerow([name,count])
    f.close()
count=0
for i in range(3):
    num = random.randint(1,10)
    answer = float(input('What is the square root of'+str(num)+'?'))
    if answer ==math.sqrt(num):
        count+=1
name = input('What is your name? ')
open_file(name,count)
