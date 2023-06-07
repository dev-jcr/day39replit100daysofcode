import random, sys

# Color change subroutine
def c(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color=="green":
    return ("\033[32m")
  elif color=="purple":
    return ("\033[35m")
  elif color=="pink":
    return ("\033[38;5;206m")

listOfWords = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(f"""{c("pink")}
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
""")

wordChosen=random.choice(listOfWords)
wordChosenList=[]
guessed=[]
wordChosenLen=len(wordChosen)
errorCounter=0
remaining=7
underscoreCount=0
counter=0
guessedCount=0

for letter in range(wordChosenLen):
  guessed.append("_")

for letter in wordChosen:
  wordChosenList.append(letter)

def check():
  global counter
  global guessedCount
  global errorCounter
  print()
  for i in range(len(guessed)):
    print(f"{c('pink')}{guessed[i]}", sep="", end="")
  print()
  userLetter=input(f"{c('white')}\nType in a letter...\n\n")
  print()
  if userLetter not in wordChosenList:
    print(f"{c('red')}{hangmanpics[errorCounter]}")
    errorCounter+=1
    if errorCounter==7:
      print("Hangman died!")
      sys.exit("Game finished!")
  else:
    for letter in wordChosenList:
      indexLetter=wordChosenList.index(letter)
      if userLetter==wordChosenList[counter]:
        guessed[counter]=userLetter
        counter+=1
        guessedCount+=1
        if guessedCount==wordChosenLen:
          print("You won!")
          print(f"The word is: {wordChosen}")
          sys.exit("Game finished!")
      else:
        counter+=1
    counter=0

while remaining>0:
  remaining-=1
  check()