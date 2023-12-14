# Control Flow, Ceon Gordon Kelley, v0.0
# DECLARATIONS

favColor = "orange"
luckyNumber = 30
myGPA = 3.8
myAge = 16
chickenSaladForDinner = True

# if statements - Check for a condition to be true or false and do somthing if true
if favColor == "orange":
    print("Correct.")

if myGPA  >= 3.8:
    print("BigBrain.")

# if-else Statemenet -- Check for a condition, do somthing for True and false
if myGPA >= 3.8:
    print("Good job.")
else:
    print("Be better. Try harder.")






# if - elif - Else statements -- Checks for multiple conditions
if myAge > 50:
    print("Your old.")
if myAge > 16:
    print("No way.")
    # 1 if, 1 else, any number of elif allowed.

# Nested if - elif - else Statements
if myAge >= 15:
    print("You can get a license.")
elif myGPA >= 4.0:
    print("You qualify for a new can.")
else:
    print("You are not yet old enough to drive")

# When doing if - elif - else satements, Check for highest number value first
if myGPA > 1.5:
    print("You are in anger of failing this year.")
elif myGPA > 2.0:
    print("Your on track to graduate")
elif myGPA > 3.0:
    print("You qualify for scholarship money.")
elif myGPA > 3.99:
    print("You qualify for Bright future 100 percent")
else:
    print("GPA was not calculated. Please try agian.")
# () Parentheses
# [] square brackets
# <> angle brackets
# {} Braces
# while Loop -- Think "Musical chairs" -- Used when you do NOT know how many iterations you need.
# Iteration is one complete trip through a loop
x=0
while x < 100: 
    print(f"X is currently equal to {x}")
    x += 1

