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
tries = 0

def main():
    '''Welcome User'''
    print("Welcome to the Number Guessing Game")

    '''Ask user for input'''
    guess = int(input("What's your guess?: \n"))
    
    '''Check if guess matches correct guess'''
        #Let user know if their number is too high or too low
    if (guess > correct_num):
        print("You're guess is too high.")
        input("What's your guess?: \n")
        ''' Conditions would have to be checked under the same if block again and again until met. 
        So if the user guesses the same high number or any high number, the program can 
        eventually end because there was no condition to meet the user's choice. 
        It ends up becoming repetitive and inefficient'''
        print(correct_num)
        if (guess > correct_num):
            print("You're guess is too high.")
            input("What's your guess?: \n")

        elif (guess < correct_num):
            print("You're guess is too low.")
            input("What's your guess?: \n")
        elif (guess == correct_num):
            '''Success/Winner Message'''
            print("CONGRATULATIONS YOU GUESSED CORRECTLY!\nIt took you", tries, "guesses.\n")

    elif (guess < correct_num):
        print("You're guess is too low.")
        input("What's your guess?: \n")

    elif (guess == correct_num):
        '''Success/Winner Message'''
        print("CONGRATULATIONS YOU GUESSED CORRECTLY!\nIt took you", tries, "guesses.\n")

    else:
        pass

if __name__ == "__main__":
    main()
