def revupper(x):
    
    word = ''.join(reversed(x.upper()))
    return(word)
    
sent= input('Write something: ')
print(revupper(sent))
