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
exampleFunctionA()
exampleFunctionB(5,0)

