# Hang man game Ceon v0.1

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