"""
Script to play hangman game
"""

import random
import os

# Clean screen
# os.system('clear')

# class Hangman:
#     def __init__(self, name):
#         self.name = name

def get_word():
    list_words = open('./data/data.txt', 'r', encoding='utf-8').read().splitlines()
    word = random.choice(list_words)
    return word

def hide_word(word):
    hidden_word = '_' * len(word)
    return print(hidden_word)

def run():
    word = get_word()
    print(word)
    hide_word(word)

if __name__ == "__main__":
    run()