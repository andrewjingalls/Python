import random
turn_total_human = 0
game_total_human = 0
while game_total_human<100:
    die = 6
    print('Type "R" for roll or "H" for Hold?')
    while die!=1:
        decision = input('R or H?')
        if decision.lower() == 'r':
            die = random.randint(1,6)
            print('Roll: ', die)
            if die==1:
                turn_total_human = 0
                print('Turn total = 0')
                break
            else:
                turn_total_human += die
            print('Turn total = ', turn_total_human)
        else:
            print('Turn total = ',turn_total_human)
            break
    game_total_human +=turn_total_human
    print('GAME TOTAL: ',game_total_human)

    if game_total_human>=100:
        print('GAME OVER! YOU WIN!!')
    else:
        input('Press ENTER to continue')
        turn_total_human=0
        continue
