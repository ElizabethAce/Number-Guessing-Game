############################################################
'''
Author: Elizabeth Acevedo
Date: 04/16/2026

Project: Number Guessing Game

Description: This is a game where the user attempts to guess 
the correct number that the programmer pre-defined as the 
correct number. The user gets as many attempts until they guess
the correct number.

Utilization:
On terminal, type the command:
    python3 main.py

'''
#############################################################

# GLOBAL VARIABLES
correct_num = 4

def main():
    '''Welcome User'''
    print("Welcome to the Number Guessing Game.\nGuess a number from 0-10")

    '''Ask user for input'''
    guess = int(input("What's your guess?: \n"))
    
    '''Check if guess matches correct guess'''
        #Let user know if their number is too high or too low
    tries = 1
    while (guess!=correct_num):
        if (guess > correct_num):
            print("You're guess is too high.")
            guess = int(input("What's your guess?: \n"))

        elif (guess < correct_num):
            print("You're guess is too low.")
            guess = int(input("What's your guess?: \n"))
        tries+=1

    '''Success/Winner Message'''
    print("CONGRATULATIONS YOU GUESSED CORRECTLY!\nIt took you", tries, "guess(es).\n")


if __name__ == "__main__":
    main()
