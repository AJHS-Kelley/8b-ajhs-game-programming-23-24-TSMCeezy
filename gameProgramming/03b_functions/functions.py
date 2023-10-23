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
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        print(f"Roll: {roll}\n")
        numRolled += 1

rollDice(3, 6)
rollDice(1, 20)


