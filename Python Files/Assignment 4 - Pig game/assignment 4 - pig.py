import random
game_total_comp=0
game_total_human=0
turn_total_comp=0           #setting turn values and total game values to zero
turn_total_human=0          
input('PRESS ENTER TO START GAME')
while (game_total_comp<100) and (game_total_human<100):     #game loop, the game continues to  loop until one person gets to 100
    while game_total_comp <100:                             #start of the computers turn
        die = 6                                             #setting die value to 6 to establish the variable
        while (turn_total_comp<20 and die!= 1):             #computer continues to roll the die until they either hit 20 points or they roll a 1
            die = random.randint(1,6)                       #die roll
            print('Roll:',die)
            if die==1:                                      #if they hit a 1, sets the turn total to 0 and loop exits
                turn_total_comp = 0
                break
            else:                                           # if they don't hit a 1 the die value is added to the turn total
                turn_total_comp += die
        print('Computer Turn total =', turn_total_comp)     #prints the turn total
        game_total_comp += turn_total_comp                  #at end of turn, turn total is added to game total and prints it
        print('COMPUTER GAME TOTAL: ',game_total_comp)
        
        if game_total_comp>=100:                            
            print('GAME OVER! Computer wins!')              #if computer gets 100 points the game is over and the game loop exits displaying 'Game over'
            break
        else:
            input('YOUR TURN, Press ENTER to continue')     #Otherwise the game continues and its the humans turn
            turn_total_comp=0                               #As the turn changes, set turn total to zero for next round after adding it to the game total
        
        while game_total_human<100:                         #start of human turn loop
            die = 6
            print('Type "R" for roll or "H" for Hold?')     
            while die!=1:
                decision = input('R or H?')                 #asking if human wants to roll the die or hold
                if decision.lower() == 'r':                 #if you say roll, die is rolled and the number is displayed
                    die = random.randint(1,6)
                    print('Roll: ', die)
                    if die==1:                              #if you roll a 1, turn total is zero and the loop exits
                        turn_total_human = 0
                        print('Your Turn Total =',turn_total_human)
                        break
                    else:
                        turn_total_human += die                     #if you don't roll a 1, die value is added to turn total
                    print('Your Turn Total = ', turn_total_human)
                else:                                               #once you decide to hold, turn total is added to game total, is displayed and loop exits
                    print('Your Turn Total = ',turn_total_human)
                    break
            game_total_human +=turn_total_human
            print('YOUR GAME TOTAL: ',game_total_human)

            if game_total_human>=100:                               #if you get to 100 points turn loop exits displaying game over
                print('GAME OVER! YOU WIN!!')
                break
            else:
                input('COMPUTERS TURN, Press ENTER to continue')    #if your game total is less than 100, the turn switches, setting your turn total to zero
                turn_total_human=0
                break
        if game_total_human>=100:                                   #if you reach 100 points, the game loop exits and the game is over
            break
    else:                                                           #continue function starts the computers turn loop again and the game continues
        continue
