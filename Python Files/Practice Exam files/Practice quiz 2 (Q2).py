hourly_salary = float(input('What is your hourly salary? '))
hours_week = float(input('How many hours did you work a week? '))
yearly_salary = hourly_salary*hours_week*52
if yearly_salary>100000:
    print('YOU''RE RICH!')
else:
    print('KEEP SHOOTING FOR THE STARS!')
