vax = str(input('Did you get the first dose of the Vaccine?'))
if vax.lower()=='yes':
    vax2 = str(input('Did you get your second dose?'))
    if vax2.lower() =='yes':
        vaxboost = str(input('Did you get the booster?'))
        if vaxboost.lower() == 'yes':
            print('Complete!')
        else:
            print('Get your booster!')
    else:
        print('Get your second dose!')
else:
    print('Get your first dose!')
