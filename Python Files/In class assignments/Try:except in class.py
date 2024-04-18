try:
    x=open('that_file.txt')
    print(x.read())
except FileNotFoundError:
    print('File not accessible')
