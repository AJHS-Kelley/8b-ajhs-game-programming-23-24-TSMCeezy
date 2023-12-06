#Example Game Functions by Ceon Gordon v0.1
import random 

def functionOne ():
    pass

def functionTwo (param1):
    pass

def functionThree(param1= "Defualt Value"):
    pass

def functionFour(param1, param2, param3):
    pass

#def catchBall(throwQuality, passCatchScore, wheater):
    #if throwQuality > 5.0 and passCatchScore >= 99 and wheater == 'Sunny':
  #      ballCaught=True
   # elif throwQuality > 4.0 and passCatchScore >= 75 and wheater == 'Windy':
   #     ballCaught = False
   # else:
    #    print('Oh, no, interception!\n')
    #    ballIntercepted = True
    #    return ballIntercepted
   # return ballCaught

#catchBall(4.25, 107, 'Rainy')

#PlatformGame
moveForwardAmount = 0
moveBackAmount = 0 
turnLeftAmount = 0
gameScore= 0


print("""
     *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
      |                                                             |
      |                   platformer stat generater                 |
      |                         ceon gordon                         |
      |                            2023                             |
      *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~* 
      
      """)
print ("Make your stats.")


def rollDice(numDice, sizeDIce,):
    numRolled=0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Strength: {sum}\n")
        numRolled += 1
        return sum 
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











  
    

