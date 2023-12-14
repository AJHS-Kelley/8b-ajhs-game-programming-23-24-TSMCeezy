#Dice rolling Modules by Ceon
import random
def roll(numDice, sizeDIce,): #Working
    numRolled=0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        sum += roll
        numRolled += 1
    return sum # RETURN will exit a loop, function, if/elif/else block.

roll(3, 6)

def display(numDice, sizeDIce,): #Working 
    numRolled=0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"SUm: {sum}\n")
        numRolled += 1
        return sum # RETURN will exit a loop, function, if/elif/else block.

display(1, 100)

def isDoubles(roll1,roll2):
    if roll1 == roll2:
        isDoubles = True
    else:
        isDoubles = False
    return isDoubles

def isExploding(roll, sizeDice):
    if roll == sizeDice:
        isExploding = True
    else:
        isExploding = False
    return isExploding

