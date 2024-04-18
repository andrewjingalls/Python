def capitalize_and_reverse(string):                                          
    def _process_word(index, word):                                        
        if index % 2 == 0:                                                   
            return upcase(word)                                              
        else:                                                                
            return reverse(word)                                             

    return ' '.join(map(_process_word, enumerate(words(string))))            


string = "Michelle ma belle these are words that go together well"           
print (capitalize_and_reverse(string)   )  
