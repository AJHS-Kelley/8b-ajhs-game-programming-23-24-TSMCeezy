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
    sum= 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDIce)
        sum += roll
        #print(f"Wisdom: {roll}\n")
        #print(f"Strength: {roll}\n")
        #print(f"dexterity:{roll}\n")
        numRolled += 1
        return sum 
rollDice(1, 6)

strengthPlayer= rollDice(1, 6)
dexterityPlayer= rollDice(1, 6)
wisdomplayer= rollDice(1, 6)
#print(strengthPlayer)
#print(dexterityPlayer)
#print(wisdomplayer)
def genStats():
    playerStats = [0,0,0]
    i = 0
    while i < 3:
     playerStats[i] = rollDice (1,6) # Strenth
     while i < len(playerStats):
      i+=1
     
    print(playerStats)

genStats()
print("First number is your strength, second wisdom, last dexterity")




#edited by jermya jitt.








  
    

