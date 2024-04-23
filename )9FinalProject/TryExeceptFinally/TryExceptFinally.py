#Try -- except -- else -- finally

try:
 myVariable=1
 print(myVariable)
 myString = "five"
 print(float(myString))
except NameError:#Code will run if there is a error
 print("Somthing has gone wrong in your code")
except:
 print(" Somthing else went wrong")
else:
 print("Code ran succefully no exceptions.\n")
finally:
 print("Ill be back.\n")
