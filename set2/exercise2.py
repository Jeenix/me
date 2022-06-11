"""Correct the syntax in this file.

This file doesn't run yet. Go through it and change it until it runs.

Look at the wiggly lines. Pay attention to the colours fix the first error, and 
it might fix errors that come after. We'll often talk about upstream (things 
that happen before) and downstream (things that happen after). Python reads the 
file from top to bottom.
"""

import string

def getLetter(index):
    alphabet = str(string).lower() + " "
    return alphabet[index]


def set2exersise2():
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = [getLetter(x) for x in indices]
    wordArray[0] = wordArray[0]
    wordArray[1] = wordArray[1].upper()
    wordArray[3] = wordArray[3].upper()
    secret_word="".join(wordArray)
    print(secret_word)
    return secret_word


if __name__ == "__main__":
    print (set2exersise2())
