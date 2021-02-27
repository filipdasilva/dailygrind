

secretWord =input('Hey bud whats the word: ').upper()

#def convert_letter(secretWord):
#    new_word = secretWord
#   for i in range(0, len(secretWord)):
 #       if ord(secretWord[i]) != 32:
  #          new_word = new_word.replace(secretWord[i], '_ ')
   # print(new_word)
#displayWord = convert_letter(secretWord)   
#print(displayWord)


InvalidInput = True

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
GameOver = False
Player = 1
guess = ""
count = 0

def getdisplayWord(secretWord):
    displayWord = []
    for i in range(len(secretWord)):
        if secretWord[i] in alphabet:
            displayWord.append('_')
        else:
            displayWord.append(secretWord[i])

displayWord = getdisplayWord(secretWord)

def PrintWord(displayWord):
    word = ""
    for i in range(len(displayWord)):
        word = word + displayWord[i]
       
        
        print('OK', word)


    while Gameover == False:
        InvalidInput == True
        while InvalidInput:
            guess = input('What is your guess? ').upper()
            if len(guess) > 1 or guess not in alphabet:
                print('Bad guess, try again')
            else:
                InvalidInput == False

    
    
        if guess in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i] == guess:
                    displayWord[i] = guess

            if '_' not in displayWord:
                print('Good Game')
            printWord(displayWord)

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
        

#while InvalidInput == True:
 #   if guess in secretWord:
  #      new_word = secretWord
   #     for i in range(0, len(secretWord)):
    #        if ord(secretWord[i]) != 32:
     #           new_word = new_word.replace(secretWord[i], guess)
   # print(new_word)
#displayWord = convert_letter(secretWord) 

        





