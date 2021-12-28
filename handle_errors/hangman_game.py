"""
Script to play hangman game
"""

import random
import os
from unidecode import unidecode


# class Hangman:
#     def __init__(self, name):
#         self.name = name

def get_word():
    # Read a file by lines and create a list
    list_words = open('./data/data.txt', 'r', encoding='utf-8').read().splitlines()
    # Remove accents, upper case and choose a random word from list
    word = unidecode(random.choice(list_words)).lower()
    return word

def hide_word(word):
    hidden_word = '_' * len(word)
    hidden_word = [u for u in hidden_word]
    return print(f'Tu palabra secreta tiene {len(hidden_word)} letras \n\n {hidden_word}\n')

def guess_word(word):
    guess = input('Escoge una letra: ')
    assert guess.isalpha(), 'Sólo puedes ingresar letras'
    # Command to clear terminal
    os.system('clear')
    # Create a list with word letters
    letters = [l for l in word]
    # Cover letters that doesn't match the input
    for i in range(len(letters)):
        if guess != letters[i]:
            letters[i] = '_'
    # Create a list with matches from input
    count = list(filter(lambda l: l == guess, letters))
     
    if guess in letters:
        if len(count) > 1:
            print(f"Hay {len(count)} coincidencias de '{guess}'\n")
        else:
            print(f"Hay {len(count)} coincidencia de '{guess}'\n")
    else:
        print(f"Ups, '{guess}' no se encuentra en la palabra secreta :(\n")

    return print(letters)

def run():
    word = get_word()
    print(word)
    hide_word(word)

    guess_word(word)

if __name__ == "__main__":
    run()
