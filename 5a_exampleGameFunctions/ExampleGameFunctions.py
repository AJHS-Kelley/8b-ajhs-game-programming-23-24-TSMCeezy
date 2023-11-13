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

def catchBall(throwQuality, passCatchScore, wheater):
    if throwQuality > 5.0 and passCatchScore >= 99 and wheater == 'Sunny':
        ballCaught=True
    elif throwQuality > 4.0 and passCatchScore >= 75 and wheater == 'Windy':
        ballCaught = False
    else:
        print('Oh, no, interception!\n')
        ballIntercepted = True
        return ballIntercepted
    return ballCaught

catchBall(4.25, 107, 'Rainy')
  
    

