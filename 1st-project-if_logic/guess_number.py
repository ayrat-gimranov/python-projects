#!/usr/bin/python3
"""Alta3 Python project: Number guessing game
   Author: Ayrat Gimranov"""

# import our classes
import random

# entry point
def main():
    
    round = 1 # we wil lhabe three rounds, incrementing with each incorrect guess
    
    # set the range
    start = 1
    end = 10

    # pick a random integer wihtin that range
    num = random.randint(start, end)
    
    # we will update this if user guesses correctly
    won_game = False

    # loop for three rounds
    while round <= 3:

        print(f"\nRound {round}\n")
        
        # initialize an empty string
        user_input = ""

        #keep asking until the input is a number and is within the range
        while not user_input.isdigit() or not (start <= int(user_input) <= end): 
           user_input = input(f"Guess a number between {start} and {end}\n>")

        # check to see if the user guessed it correctly
        if int(user_input) == num:
            print(f"\nCONGRATUALTIONS! You guessed the number.\nAnswer:{num}")
            
            #update the win status
            won_game = True
            #break ou tof the loop if user wins
            break
        else:
            print(f"\nWrong guess!\n")
        
        # increment the round
        round = round + 1

    # if guessed correctly, print a corresponding message    
    if won_game:
        print("\nThanks for playing!\n")
    # otherwise, tell what the number in my mine was
    else:
        print(f"\nYou lost! The answer was: {num}\n")

if __name__ == "__main__":
    main()
