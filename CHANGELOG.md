## Version 0.2.0 - Randomly Generated Number
- Imported library: Random Library
- Modified program to generate random number every time it is run

## Version 0.1.1 - Modified success print statement
- Added if conditions to check how many tries it took to get the correct guess in order to print singular/plural.

## Version 0.1.0 - Working Version of Guessing Game
- Used a while loop to keep prompting until correct number is guessed.
- Had to update guess inside loop

## Version 0.0.6 - Demonstrate How Pure Use of If-Blocks are Inefficient for this Game
- Asks for guess 3 times if your first attempt was high
- Asks for guess 2 times if your first attempt was low
- If you start with a high number, try again and guess the correct number, you are told 
your guess is too high which is incorrect because there's no block for the condition if 
you got it right the next time.
- And so on... So we see the issue right?
- If you guess correctly the first time, you get a success message printed on the terminal screen

## Version 0.0.5 - Updated Header & Added more to conditions block
- Additions to Header & conditions block

## Version 0.0.4 - User Input test
- Run on terminal command: python3 main.py
- Test passed and input was taken

## Version 0.0.3 - Print test
- Run on terminal command: python3 main.py
- Test passed and printed message

## Version 0.0.2 - Planning Stage on File
- Created main.py
- Basic plan layout for program

## Version 0.0.1 - Planning Stage
How it's played and what needs to be taken into account:
- Need to guess a number from 0-10
- The user is asked for a number as their guess
    - Ask user for input and check if number matches
- The program returns feedback if the number was too high or too low
    - Check conditions
    - Print statement
- The user keeps guessing until the answer is correct
    - Can later also save numbers guessed and have user try again without repeating same guesses
    - Loop in the same prompt until number is guessed correctly
- Display a message for when the user wins
- Display the number of attempts
    - Variable will store a number of attempts
