letters = [["i", "q", "m", "S"], ["a", "!", "t", "y"], 
["p", "-", "a", "q"], ["o", ".", "R", "l"], ["s", "V", 
"t", "-"], ["!", "r", "k", "E"], ["a", "r", "!", "P"]]
for i in range(len(letters)):
    for j in range(4):
        if i%2 == 0 and j%2 == 0:
            char = letters[i][j]
            print(char.upper())



