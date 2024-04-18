import random
from words import words         #imported a list of words from a file of hundreds of random words

def valid_word(words):          #defining a function that picks a word without any hiphens or spaces in it

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

input('Welcome to hangman, press return to display the word you must guess')

game_word = valid_word(words)       #assigning the word used in the game with a random word from the function


hidden_word = []            #defining an empty list as the word you must guess
wrong_guesses = []          #defining an empty list as the wrong letters already guessed


for i in game_word:             #displaying underscores for every letter is in the word to visualize the word
    hidden_word.append('_')
print()
print(hidden_word)
print('The word has', hidden_word.count('_'), 'letters')    #displaying the number of letters in the word

strikes = 6                     #defining how many wrong guesses you have until you lose
while '_' in hidden_word:                   #While loop is main game loop, continues until there are no more underscores in the word meaning you have successfully guessed the word
    guess = input('Guess a letter: ')
    print()

    if guess in game_word:              #if statement runs if you guess  letter correctly
        index = 0
        while index < len(game_word):       #while loop locates the position of the correct letter in the word, must be loop for repeating letters
            index = game_word.find(guess, index)

            if index == -1:
                break
            hidden_word[index] = guess      #Changes underscores with correctly guessed letters in correct position
            index += 1
        print(hidden_word)
        print(guess, 'is in the word!')
        print('Incorrect guess bank:', wrong_guesses)       #displays wrong guesses in list


    else:                       #else statement runs if guess is not in the word
        strikes-=1
        print(guess, 'is not in the word, you have', strikes, 'tries remaining')
        print(hidden_word)
        wrong_guesses.append(guess)             #displays wrong guesses in list
        print('Incorrect guess bank:', wrong_guesses)


    if strikes==0:
        print('GAME OVER, YOU LOSE! The word was:', game_word)      #if user runs out of guesses, user loses and the word is displayed
        break

if '_' not in hidden_word:
    print('CONGRATS YOU WIN!! The word was:', game_word)    #if there are no more underscores in the word, the user has guessed all the letters and game ends, user wins
