# Hang man game Ceon v0.1
import random
#words= 'cat dog goat frog cheeta bird fish turtle cow moose one two three four five six seven eight nine ten killer danny phanny telephone jacksonville ceon computer maximum minimum death'.split() #30 words
# VARIABAL_NAMES in all caps are constants meant not to CHAnge!
# Dictionary version
# Stored in Key:Value Pairs.
#Actually Dictionary Word (Key) : Value (Definition)
# Uses {} to specify a dictionary.
words= {'Colors': 'red, blue, orange, green, purple, teal, gold, silver, white, black'.split(),
        'Animals': 'dog cat worm cow chicken human duck gator bird spider'.split(),
        'Shapes': 'square triangle circle rhombus parrallelogram trapezoid diamond dodecahdron'.split(),
        'Foods': 'burger fries shake waffle pancakes potatoes meat carrot salad spinich'.split() }
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
    ========''','''   +---+
   o   |
  /|\- |
  / \  |
    ========''','''   
   o   |
  /|\_ |
  / \_ |
    ========''',]
i=0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i+= 1

def getRandomWord(wordList): # return a random word from the list
    wordIndex = random.randint(0,len(wordList)-1)
    #len(listName)-1 is common for working with list.
    return wordList[wordIndex]
#Pikc random word from dictionary
def getRandomWord(wordDict): # return a random word from the list
    wordKey = random.choice (list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]-1))
    #len(listName)-1 is common for working with list.
    return [wordDict[wordKey][wordIndex], wordKey]

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
        if secretWord[i]  not in correctLetters:
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

# CHoose Dif
difficulty = 'X'
while difficulty not in 'EMH':
    print('Choose easy med and hard by puting the first letter of the dif.\n')
    difficulty= input().upper()
if difficulty == 'M': #med
    del HANGMAN_BOARD [8]
    del HANGMAN_BOARD[7]
if difficulty == 'H': #hard
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[6]
    del HANGMAN_BOARD[5]

missedLetters = ''
correctLetters = ''
secretWord= getRandomWord(words)
gameIsDone = False

#Main game loop
while True:
    displayboard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if they guess the whole word
        foundAllLetters= True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
              foundAllLetters = False
              break
        if foundAllLetters:
            print('Good job you guessed all the letters right')
            print('The secret word was' + secretWord)
            gameIsDone = True 
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len (HANGMAN_BOARD) - 1:
            displayboard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses and lost the game.')
            print('The word was' + secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord (words)
        else: 
            break
            #i = 0
#while i < 50:
    #word=getRandomword(words)
    #print(word)
    #i += 1