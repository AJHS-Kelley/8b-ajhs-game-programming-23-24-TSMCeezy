#DNAGame ceon gordon
# Import entire tool box 
import time, datetime
#import specific tools
from random import choice
dnaBases = ["A","T","G","C"]

#Game Fuctions
def gameIntro() -> None: 
    pass
def genDNA() -> str:
    bassGenerated = 0
    bassRequested = int(input("Please inter positive integer number of bases to generate.\n"))
    dnaSequence = ""

    while bassGenerated < bassRequested:
        dnaSequence += choice(dnaBases)
        bassGenerated += 1
    return dnaSequence

dna = genDNA()
print (dna)
