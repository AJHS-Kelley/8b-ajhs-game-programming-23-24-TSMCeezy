import random
# Function named piece of code that can be reused easily
# Function Signature -- Syntax for creating a new function
def exampleFunctionA(): #No Parameters
    count = 0
    num = int(input("How many times do you want to wish a happy birthday?\n"))
    while count<num:
        print("Happy Birthday!\n")
        count += 1
def exampleFunctionB(num,count): #PARAMETERS
    while count<num:
        print ("Happy Birthday!\n")
        count += 1
# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT

# RUNNING A FUNCTION IS KNOW AS CALL IT
#exampleFunctionA()
#exampleFunctionB(5,0)

def rollDice(numDice, sizeDIce,):
    numRolled=0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"SUm: {sum}\n")
        numRolled += 1
        return sum # RETURN will exit a loop, function, if/elif/else block.

rollDice(3, 6)

strengthPlayer= rollDice(3, 6)
dexterityPlayer= rollDice(3, 6)
wisdomplayer= rollDice(3, 6)

def genStats():
    playerStats = [0,0,0,0,0,0]
    i = 0
    while i < 6:
     playerStats[i] = rollDice (3,6) # Strenth
     while i < len(playerStats):
      i+=1
     
    print(playerStats)

genStats()

