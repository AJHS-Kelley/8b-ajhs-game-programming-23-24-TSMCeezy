# Data Types and Operaters, Ceon Gordon, v0.3

# Variable Rules. 
# Can not start with a number.
# Can not use built in keywords as variables. 
# VAriable name should discribe data being stored.
# snake_case variable use _ to seperate words, all lowercase 
# camelCase variable do not usespaces, 1st word lower, rest upper

# String Literal Examples
playerName = "Bossone"
emptyString = " "
spaceString = "  "
monsterName = "hot girl summer"

# Integer Data Types
health = 500
Extralives = 3
Tempature = 75

# Floating Point Data Types
pi= 3.14167
lapTime = 1.7
velocity = -2.21

#Boolean Data Typess
isFireType = True
WeaponEquipped = True 
pvpEnabled = True 

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH

print[3+-1] # Addition
print[0-17] # Subtraction
print[2*-5] # Multiplication 
print[3/-2] # Division
print[3 ** 9] # Exoponent
print[19%6] # Modules -- Divides, then returns remander 

# Comparison Operators 
# Evalute The Expresion Then Return True Or False
print (5 > 3) # Greater than
print ( 7 >= 2) # Greater then or equal too
print (7 < 10) # Less then
print (5 <= 5) # Less then or equal too
print (4 == 4) # Equal to
print (56 != 78) # Not equal to

# Assingment Operators 
myVariable = "myValue" # Assign varible on the left the value on the right, throw out any current value.

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignnment 
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # AND requires ALL Expressions to be True
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 and favColor == "Blue" and temp == -5)
# When writting and expressions, put the most likely to be False 

# Logical OR -- Reuires only one expression to be true
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined
print(3 > 2 and 4 < 3 or 5 != 7)
print(True and False or True)


# NOT Logical Operator
print(not(3 > 2))
print(not(not(not(5 != 3))))

