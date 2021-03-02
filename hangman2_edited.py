

#secretWord =input('Hey bud whats the word: ').upper()

#def convert_letter(secretWord):
#    new_word = secretWord
#   for i in range(0, len(secretWord)):
 #       if ord(secretWord[i]) != 32:
  #          new_word = new_word.replace(secretWord[i], '_ ')
   # print(new_word)
#displayWord = convert_letter(secretWord)   
#print(displayWord)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Player = 1

#InvalidInput = True
def GamePlay(secretWord):
    global alphabet
    GameOver = False
    
    guess = ""
    count = 0
    displayWord = getdisplayWord(secretWord)



    while GameOver == False:
        InvalidInput = True
        while InvalidInput:
            print('Player', Player)
            guess = input('What is your guess? ').upper()
            if len(guess) > 1 or guess not in alphabet:
                print('Bad guess, try again')
            else:
                InvalidInput = False
#why is the if below continue when I just changed InvalidInput to False? Doesnt make sense to me


        if guess in secretWord:
            for i in range(len(secretWord)):
                if secretWord[i] == guess:
                    displayWord[i] = guess
            printWord(displayWord)

            if '_' not in displayWord:
                print('Good Game')
                GameOver = True
                #Player == 3
                #main()
           # printWord(displayWord)

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
            elif count ==6:
                print('Game Over')
            printWord(displayWord)
def printWord(displayWord):
    word = ""
    for i in range(len(displayWord)):
        word = word + displayWord[i]   
        print()
        print('OK', word)
        
def getdisplayWord(secretWord):
    displayWord = []
    for i in range(len(secretWord)):
        if secretWord[i] in alphabet:
            displayWord.append('_')
        else:
            displayWord.append(secretWord[i])
           
    return displayWord
def main():
    global alphabet
    global Player
    
    #alphabet:"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Continue = True
    secretWord = ""
    
    while Continue:
        if Player == 1:
            secretWord =input('Player One hey bud whats the word: ').upper()

            Player = 2
            for i in range(40):
                print()

            GamePlay(secretWord)
        elif Player == 2:
            secretWord =input('Player Two hey bud whats the word: ').upper()
            Player = 1
            for i in range(40):
                print()


            GamePlay(secretWord)
        #elif Player == 3:
        quit = input('Do you want to quit? (Y/N): ')
        if quit == 'y' or quit == 'yes' or quit == 'Y':
            Continue = False


main()

#Remaining Errors:
#1. The displayWord is displayed multiple times every guess
#2. Game keeps going when hangman is there


#else:
 #   print('Try again')

        

#while InvalidInput == True:
 #   if guess in secretWord:
  #      new_word = secretWord
   #     for i in range(0, len(secretWord)):
    #        if ord(secretWord[i]) != 32:
     #           new_word = new_word.replace(secretWord[i], guess)
   # print(new_word)
#displayWord = convert_letter(secretWord) 

        





