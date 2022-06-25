"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    lowerbound = input(f"Enter an lower bound: ")
    lowerbound = check_int(lowerbound)
    upperbound = input(f"Enter an upper bound: ")
    upperbound = check_big(lowerbound, upperbound)
    print(f"OK then, a number between {lowerbound} and {upperbound} ?")
    actualNumber = random.randint(lowerbound, upperbound)
    guessed = False
  
    while not guessed:
        guessedNumber = input("Guess a number: ")
        guessedNumber = check_int(guessedNumber) 
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber > upperbound:
            print("You're the genius in your family aren't you? LOL try again.")
        elif guessedNumber < lowerbound:
            print(f"Don't get the point of this game? The number needs to be within {lowerbound} and {upperbound}. Try again.")
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

def check_int(user_input):
  user_input = make_int(user_input)
  numeric = isinstance(user_input, (int))
  while numeric == False:
      message = "That isn't a number smart ass. Input a number:"
      user_input = input(message)
      user_input = make_int(user_input)
      numeric = isinstance(user_input, (int))
  return user_input

def check_big(lowerbound, upperbound):
  user_input = check_int(upperbound)
  while lowerbound >= user_input:
    message = f"UPPER means BIGGER you dolt... pick a number greater than {lowerbound}:"
    user_input = input(message)  
    user_input = check_int(user_input)
  return user_input

def make_int(user_input): 
  try:
    return int(user_input)
  except ValueError:
    print ("umm..")
    return user_input

if __name__ == "__main__":
    print(advancedGuessingGame())
