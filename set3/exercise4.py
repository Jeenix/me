# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    dict_guesses = {}
    guessed = False
    guess = low    
    while not guessed:
        tries += 1
        mid_value = (low + high) // 2
        dict_guesses = guess_log(guess, tries, dict_guesses)
        if guess == actual_number:
            guessed = True
        elif actual_number < mid_value:
            guess = low + 1
            low = guess
            high = mid_value
        elif actual_number > mid_value: 
            guess = high - (tries + 1)  
            low = mid_value
    return {"guess": guess, "tries": tries}

def guess_log(number, tries, dict_guesses): #just logs guess to dict
    dict_guesses[number] = tries
    dict_guesses
    return dict_guesses 

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
