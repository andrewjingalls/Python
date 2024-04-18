import random
turn_total_comp = 0
game_total_comp = 0

while game_total_comp <100:
    die = 6
    while (turn_total_comp<20 and die!= 1):
        die = random.randint(1,6)
        print('Roll:',die)
        if die==1:
            turn_total_comp = 0
            break
        else:
            turn_total_comp += die
    print('Turn total =', turn_total_comp)
    game_total_comp += turn_total_comp
    print('GAME TOTAL COMPUTER: ',game_total_comp)
        
    if game_total_comp>=100:
        print('GAME OVER! Computer wins!')
    else:
        input('Press ENTER to continue')
        turn_total_comp=0
        continue
