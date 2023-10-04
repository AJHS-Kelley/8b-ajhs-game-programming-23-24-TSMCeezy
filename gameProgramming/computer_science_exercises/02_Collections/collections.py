#Collections examples, Ceon gordon V0.3A

#LIST -- ordered, changeable, it allows duplicates
breakfastFoods = ["Bacon", "Waffles", "Bread", "h", "5", "6"] 
#Each item is a element
#THe position in the list for each is the INDEX
#The element "Bacon" is at idex 0
#Python Only: Index -1 it is the last item on the list
testScores = [95,100,25,15,27,35]
classGpa = [3.14,2.25,1.74,1.99,8.99,4.25]

# Printing contents of an list
#print (breakfastFoods)
#print (testScores)
#print(classGpa)

# Acces specific things in list
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGpa[0])

#Accsesing last item in list -- use -1
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGpa[-1])
#Number three on each list
#print(breakfastFoods[2])
#print(testScores[2])
#print(classGpa[2])
#Changeing items in a list

breakfastFoods [0] = "Sausage"
testScores[0]= 97
classGpa[0] = 3.57

#print(breakfastFoods[0])
#print(testScores[0])
#print(classGpa[0])
#print (breakfastFoods)
#print (testScores)
#print(classGpa)

#breakfastFoods[4]="fort"
#testScores[4]=7
#classGpa[4]=3.0

#print(breakfastFoods[4])
#print(testScores[4])
#print(classGpa[4])
#print (breakfastFoods)
#print (testScores)
#print(classGpa)

# Adding and inserting items to a list
# .append() adds an item to the end of the list
#breakfastFoods.append("Orange")
#print (breakfastFoods)
#testScores.append(99)
#print(testScores)
#classGpa.append(7.0)
#print(classGpa)

# .Insert() allows you to place an item at a specific index/spot in the list
#breakfastFoods.insert(2,"Eggs")
#print(breakfastFoods)
#testScores.insert(3, "heloo")
#print(testScores)
#classGpa.insert(3, 4.26)
#print(classGpa)

# Deleting from list
# Use .remove()in list
#breakfastFoods.remove("Bread")
#print(breakfastFoods)
#testScores.remove(100)
#print(testScores)
#classGpa.remove(1.99)
#print(classGpa)

# To delete using the index/spot number use .pop()
#breakfastFoods.pop(1)
#print(breakfastFoods)
#testScores.pop(1)
#print(testScores)
#classGpa.pop(1)
#print(classGpa)

#breakfastFoods.remove("Bread")
#print(breakfastFoods)
#testScores.remove(25)
#print(testScores)
#classGpa.remove(1.99)
#print(classGpa)

# Determining list leghth 
print(f"There are {len(breakfastFoods)} items in breakfeast list.")
print(f"Some of the scores on the test vary but most are in between{len(testScores)} adverages.")
print(f"The average for class GPAS varied from {len(classGpa)} diffrent gpas.")