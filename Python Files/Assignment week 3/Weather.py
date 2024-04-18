weather = str(input('Is it raining? '))
if weather.lower() == 'yes':
    wind = str(input('Is it windy? '.lower()))
    if wind == 'yes':
        print('It is too windy for an umbrella.')
    else:
        print('Take an umbrella.')
else:
    print('Enjoy your day')
