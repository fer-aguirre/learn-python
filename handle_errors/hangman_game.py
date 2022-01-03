"""
Script to play hangman game
"""

import random
import os
from unidecode import unidecode

# Constant with a file path
DATA = "./data/data.txt"

def get_word():
    # Read a file by lines and create a list
    list_words = open(DATA, 'r', encoding='utf-8').read().splitlines()
    # Remove accents, upper case and choose a random word from list
    word = unidecode(random.choice(list_words)).lower()
    return word

def hide_word(word):
    hidden_word = '_ ' * len(word)
    return hidden_word

def is_word_guessed():
    pass

def letters_chosen():
    pass

def count_attempts():
    pass

def uncover_word(word, letters_guessed):
    uncovered = ''
    for letter in word:
        if letter in letters_guessed:
           uncovered += letter
        else:
            uncovered += '_'
    return uncovered

#     # Command to clear terminal
#     os.system('clear')

#     # Create a list with matches from input
#     count = list(filter(lambda l: l == guess, letters))

def guess_letter(word):
    while True:
        letters = [l for l in word]
        guess = input("Escoge una letra: ")
        assert guess.isalpha(), "Sólo puedes escoger letras"
        if guess not in word:
           print(f"No hay coincidencias de '{guess}'")
        else:
            # Cover letters that doesn't match the input
            for i in range(len(word)):
                if guess != letters[i]:
                    letters[i] = '_'
            print(f"  {' '.join(letters)} ")
            

            if '_' not in letters:
                break
            else:
                continue

def hangman_game():
    pass

def run():
    word = get_word()
    print(word)
    hidden_word = hide_word(word)
    print(f'Tu palabra secreta tiene {len(word)} letras \n\n {hidden_word}\n')
    guess = guess_letter(word)

if __name__ == "__main__":
    run()

     
