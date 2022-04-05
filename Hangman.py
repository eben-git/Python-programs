import random
from Words import words
import string



def get_validWord(words):
    word = random.choice(words)   #random word is selected

    while '-' in word or ' ' in word:
        word = random.choice(words)


    return word.upper()


def hangman():
    word = get_validWord(words)
    wletters = set(word)      # letter in the the actual word
    alphabets = set(string.ascii_uppercase)
    used_letters = set()     # letter already guessed by the user
    lives = 7

    # current user state
    while len(wletters) > 0 and lives > 0:
        # the no of letters in the word
        # ' '.join will do this ' '.join(['a', 'bc', 'd']) --> 'a, bc, d'
        print('You have', lives, 'left and you have guessed these letters: ', ' '.join(used_letters))

        # what is the curent state of the word ie w - - d
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #user input
        user_guess = input("Guess a letter: ").upper()
        if user_guess in alphabets - used_letters:
            used_letters.add(user_guess)
            if user_guess in wletters:
                wletters.remove(user_guess)
                print('')

            else:
                lives -= 1 # wrong guess takes away 1 life
                print('\n Your letter', user_guess,'is not in the word.')

        elif user_guess in used_letters:
            print('\nyou have already guessed that letter')

        else:
            print('Invalid input!!')

    # the loop breaks if wletter == 0 and lives == 0
    if lives == 0:
        print(lives)
        print('You lost! The word was ', word)
    else:
        print('You win! You guess the word ', word)

hangman()