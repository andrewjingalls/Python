def secret_function(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    if w1[::-1] == w2:
        return True
    else:
        return False


#a) change = to ==

#b) The function changes the letters to lowercase, if the last element in w1 
