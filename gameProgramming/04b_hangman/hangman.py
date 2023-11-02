# Hang man game Ceon v0.1
import random
words= 'cat dog goat frog cheeta bird fish turtle cow moose one two three four five six seven eight nine ten killer danny phanny telephone jacksonville ceon computer maximum minimum death'.split() #30 words
print(words)
# VARIABAL_NAMES in all caps are constants meant not to CHAnge!
HANGMAN_BOARD= ['''
   +---+
       |
       |
       |
    ======''','''
   +---+
   o   |
       |
       |
    ======''','''
   +---+
   o   |
   |   |
       |
    =======''','''
  +---+
   o  |
   |\ |
      |
    ========''','''
   +---+
   o   |
  /|\  |
       |
    ========''','''
   +---+
   o   |
  /|\  |
    \  |
    ========''','''
   +---+
   o   |
  /|\  |
  / \  |
    ========''']
i=0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i+= 1

def getRandomWord(wordList): # return a random word from the list
    wordIndex = random.randint(0,len(wordList)-1)
    #len(listName)-1 is common for working with list.
    return wordList[wordIndex]

def displayboard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('missed Letters:', end= ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()

    blanks='_'*len(secretWord)
    
    #Replace blanks with correct letters
    for i in range(len(secretWord)):
        if secretWord[i] ? correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = '')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter from the key board')
        guess = input()
        guess= guess.lower()
        if len(guess) != 1:
            print('enter a single letter.')
        elif guess in alreadyGuessed:
            print('letter has been guessed, try agian.')
        elif guess not in 'abcdefghijklmnopqrstuvwxwz':
            print('Please guess a letter from the English alphabet.')
        else:
            return guess 

def playAgain():
    print('Try one more time?')  
    return input(). lower().startwith('y')


#Start of the game
print('Welcome to hangman by ceon.')
missedLetters = ''
correctLetters = ''
secretWord= getRandomWord(words)
gameIsDone = False

#Main game loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
#i = 0
#while i < 50:
    word=getRandomword(words)
    print(word)
    i += 1