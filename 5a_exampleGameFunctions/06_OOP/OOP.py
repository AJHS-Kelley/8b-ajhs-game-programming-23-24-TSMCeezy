# Object Oriented progaming. ceon gordon
class Person: # Use PascalCase for classNames aka all 
    def __init__(self, Name, age, weight) :
        self.name= Name
        self.age = age
        self.weight = weight 
        self.weakness = None
        self.nemesis= None
    
    def __str__(self):
        return f"Name:{self.name}\nThis person is {self.age} years old.\n They weigh {self.weight} pounds.\n "


Person1 = Person("Ash Kash", 21, 120)
print (Person1)

class Person: # Use PascalCase for classNames aka all 
    def __init__(self, Name, Age, weight) :
        self.name= Name
        self.age = Age
        self.weight =weight 
    
    def __str__(self):
        return f"Name:{self.name}\n This person is {self.age}years old\n He is {self.weight}\n and proud"


Person2 = Person("Ceon Gordon", 16, 160)
print (Person2)

#if Person1.age > Person2.age:
#print(f"{Person1} is older then {Person2}.")
#elif Person1.age < Person2.age:
       # print(f"{Person1} is younger then {Person2}")

#Person1.classFunction()

#Changing Item
print(Person1)
Person1.name = "Gon black"
print(Person1)

#Deleting property
#print(Person1.name)
#del Person1.name
#print(Person1)

#Delete Object
del Person1

#Adding properties
Person2. weakness = "Water"
print(Person2)
print(Person2.weakness)