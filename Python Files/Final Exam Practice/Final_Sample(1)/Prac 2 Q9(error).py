try:
    f=open(result, 'r')
    print (f.read())
except (AttributeError, IOError):
    print('Error, try again.')
except:
    print('Try again')
