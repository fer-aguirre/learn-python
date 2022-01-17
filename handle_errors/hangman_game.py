"""
Script to play hangman game
"""

import random
import os
from xml.dom import WrongDocumentErr
from unidecode import unidecode

# Constant with a file path
DATA = "./data/hangman_data.txt"

"""
Function to read a txt file
"""
def get_word():
    """
    return: a random word from file
    """
    # Read a file by lines and create a list
    list_words = open(DATA, 'r', encoding='utf-8').read().splitlines()
    # Remove accents, upper case and choose a random word from list
    word = unidecode(random.choice(list_words)).lower()
    return word

"""
Function to cover the
word with underscores
"""
def hide_word(word):
    """
    word: random word generated from get_word() function
    return: string with underscores
    """
    hidden_word = '_ ' * len(word)
    return hidden_word


"""
Function to check if a 
letter is into the word
"""
def is_letter_in_word(letter, word):
    """
    letter: character from input
    word: random word generated from get_word() function
    return: boolean, True if letter is in word and False if it isn't
    """
    if letter in word:
        return True
    else:
        return False

"""
Function to uncover the word
with matches from input
"""
def uncover_word(letter, word, hidden_word):
    for char in word, hidden_word:
        if char == letter:
           hidden_word += char
        else:
            hidden_word += '_ '
    return hidden_word

"""
Function to clear the terminal
"""
def clean_terminal():
    # Command to clear terminal
    os.system('clear')



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
    word = get_word()
    print(word)
    hidden_word = hide_word(word)
    print(f'Tu palabra secreta tiene {len(word)} letras \n\n {hidden_word}\n')
    guess = input("Escoge una letra: ")
    is_match = is_letter_in_word(guess, word)
    if is_match == True:
        uncovered = uncover_word(guess, word, hidden_word)
        print(uncovered)
    else:
        pass

def run():
    hangman_game()


if __name__ == "__main__":
    run()

     
