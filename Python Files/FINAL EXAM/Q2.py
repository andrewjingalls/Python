pal = 0
def palindrome ():
    x = input('Enter a word: ')
    if x == x[::-1]:
        return True
        pal = 1
    else:
        return False
        

while pal != 1: 
    print(palindrome())
    
