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


def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart= time.time() #time.time() return the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching rna sequence.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop-rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are Ordered-- you can refrence items with the index.
    # Tuples are unchangeable -- you cannot add, modify, or delete
    # tuples can have duplicate values

rna = genRNA(dna)
print(rna)
