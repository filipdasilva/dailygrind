#First need to define gameplay
#need to define whats going on and then what is the basis of the game

#variables are
#player, alphabet, secret word, displayword, guess

#def LetsPlay(secretWord):


#Then define what the turn is
#Turn 1
#import re

secretWord =input('Hey bud whats the word: ').upper()

#displayWord = re.sub('\w', '_', secretWord)

#def displayWord(secretWord):
 #   for i in range(0, len(secretWord)):
  #      secretWord.replace(secretWord[i],'_')
  #  print(secretWord)

#i = i in range(0, len(secretWord))

def convert_letter(secretWord):
    new_word = secretWord
    for i in range(0, len(secretWord)):
        if ord(secretWord[i]) != 32:
            new_word = new_word.replace(secretWord[i], '_ ')
    print(new_word)
displayWord = convert_letter(secretWord)   
print(displayWord)

#def convert_letter(word):
  #  ''.join('_' if c in secretWord.ascii_letters else c for c in word)
    
#print(convert_letter(secretWord))

InvalidInput = False

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#displayWord = secretWord
Player = 1
guess = ""
count = 0

#LetsPlay(secretWord)

while InvalidInput == False:
    guess = input('What is your guess? ').upper()
    if guess in secretWord:
        print('Correct')
        InvalidInput = True
    elif len(guess) > 1:
        print('Incorrect')
    elif guess not in alphabet:
        print('Try Again')
       
    elif guess not in secretWord:
        print('Wrong')
        count = count + 1
        if count == 1:
            print('0')
            print('Tries Remaining:', 6-count)
        elif count == 2:
            print('0_')
            print('Tries Remaining:', 6-count)
        elif count == 3:
            print('0_0')
            print('Tries Remaining:', 6-count)
        elif count == 4:
            print('X_0')
            print('Tries Remaining:', 6-count)
        elif count == 5:
            print('X_X')
            print('Tries Remaining:', 6-count)
        else:
            print('Game Over')
        
    else:
        print('Try again')
        InvalidInput = True
    continue

while InvalidInput == True:
    if guess in secretWord:
        new_word = secretWord
        for i in range(0, len(secretWord)):
            if ord(secretWord[i]) != 32:
                new_word = new_word.replace(secretWord[i], guess)
    print(new_word)
displayWord = convert_letter(secretWord) 

InvalidInput = False
        





#Then define who's turn it is

