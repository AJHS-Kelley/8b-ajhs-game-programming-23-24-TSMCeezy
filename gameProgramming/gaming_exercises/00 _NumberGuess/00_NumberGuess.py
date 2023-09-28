# Select a secret nuber from a given range.
# Have palyer guess a number.
# compare player guess to secret number.
# WHat happens if the guess is wrong?
    # Tell them the guess is wrong.
    # State the number of guesses left
    # Tell if the number guessed was high or low
# WHat happens if guessed right?
    # Tell them its right.
    # Award a point.
# WHat happens after players runs out of guesses
    #Tell the player they lost the round
    #Give the cpu a point
# Check to see who got three points first if so they win

import random # Import the random module to our code.

# Declerations 
secretNumber = -1
playerGuesses = -1 
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = ""
rangeMin = -1
rangeMax = -1
numAttempts = -1
print("""
     *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
      |                                                             |
      |                       Guess a number                        |
      |                         ceon gordon                         |
      |                            2023                             |
      *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~* 
      
      """)

# CPU SECRET NUMBER GRERATION


# GANG LOOP
# Change difficulty code
# Make a explination for each difficulty 
print("Easy difficulty keeps your number range small and attempts big. Normal keeps the attempts normal and range normal. Hard makes the range larger and attempts low.")
difficulty = input("Choose a difficulty\n")

 
# Let the player choose dificulty
# use input() to store dificulty
# Assign values to numAttempts, rangMax, and rangMin
while playerScore != 3 and cpuScore != 3: # Game starts
    # pass -- TELLS Python to skip this block of code
    # whenever you assign  specific value to somthing, it's called "hard coded".
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    #print secrete numneber
    # Add code here to change difficulty in each round.
    if difficulty == "Easy":
        rangeMin = 1
        rangeMax = 20
        numAttempts = 4
    elif difficulty == "Normal":
        rangeMin = 20
        rangeMax = 40
        numAttempts = 2
    elif difficulty == "Hard":
        rangeMin = 40
        rangeMax = 100
        numAttempts = 1
    else: 
        difficulty == "Normal"
        rangeMin = 20
        rangeMax = 40
        numAttempts = 2
        
        # You need to add the default values from one of the other difficulty levels. 
        pass 
    secretNumber = random.randint(rangeMin, rangeMax)
    print(secretNumber)
    numGuesses = 0 
    print(f"You need to guess a number from {rangeMin} to {rangeMax}.\nYou have {numAttempts} guesses.\nIf you guess right you get a point.\n if you dont get it right in 4 guesses CPU gets a point.")
    for guesses in range(4): # round starts
            print(f"You have {4-numGuesses} guesses remaining.\n")
            playerGuess = int(input("type a number from 0 to 20 and push enter.\n"))
            # input() save whatever you type in as a string.
            # int() will convert it to an integer
            # float() will convert to a float
            if playerGuess == secretNumber:
                print("Whoa dude, what a guess, you got it.\n")
                playerScore += 1
                break #IMMEDIATELY EXIT ANY LOOP
            else:
                print("You did not guess correctley.\n")
                if playerGuess > secretNumber:
                    print("Your guess is too high.\n")
                else:
                    print("Your guess is too low.\n")
            numGuesses -= 1       
            if playerGuess != secretNumber:
                cpuScore += 1
            print("The CPU wins a point.\n")     
    if playerScore >=3:
        print("Good dubs.\n")
    else:
        print("You lost to a computer.\n")


                    