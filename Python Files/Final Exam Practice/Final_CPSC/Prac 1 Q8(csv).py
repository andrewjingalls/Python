import csv
import random

#num = random.randint(1,10)
    
    
q1 = int(input('What is 5 * 3? '))
q2 = int(input('What is 6 * 5? '))
q3 = int(input('What is 9 * 9? '))

score=0

if q1 == 15:
    score += 1
if q2 == 30:
    score += 1
if q3 == 81:
    score += 1

print('Score is:', score)
name=input("What is your name?")

with open('quiz_score.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Score"])
    writer.writerow([name, score])
