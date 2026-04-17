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
    print("Welcome to the Number Guessing Game")

    '''Ask user for input'''
    guess = input("What's your guess?: \n")
    
    '''Check if guess matches correct guess'''
        #Let user know if their number is too high or too low
    if (guess > correct_num):
        pass
    elif (guess < correct_num):
        pass
    elif (guess == correct_num):
        '''Success/Winner Message'''
        # Code here
    else:
        pass

if __name__ == "__main__":
    main()
