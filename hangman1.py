#parts to this

def LetsPlay(secretWord):
    failedguesses = 0
    displayWord = getdisplayWord(secretWord)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guess = ""
    gameover = False

#here you can guess a letter


    while not gameover:
        invalidinput = True
        while invalidinput:
            print('Player' , Player, '')
            the = input('Enter your guess here: ').upper()
            print(the)
            if len(the) > 1 or the not in alphabet:
                print('Try Again')
            else:
                invalidinput = False

        if the in secretWord:
            for i in range(len(secretWord)):
                 if secretWord[i] == the:
                    displayWord[i] = the
            printWord(displayWord)
            if "_" not in displayWord:
                print('Player', Player, 'Wins')
                gameover = True
        else: 
            failedguesses += 1
            print('Losa Aint right')
            if failedguesses == 1:
                print('0')
            elif failedguesses == 2:
                print('0_')
            elif failedguesses == 3:
                print('0_0')
            elif failedguesses == 4:
                print('X_0')
            elif failedguesses == 5:
                print('X_X')
            else: 
                print('remaining tries' , 6 - failedguesses)
                printWord(displayWord)
#= is assignment, == is equals to                      
                       
#one part needs to loop to continue the game if this is right or wrong

#one part needs to hold the secret word

def printWord(secretWord):
    huh = ""
    for i in range(len(secretWord)):
        huh += displayWord[i]
    print("Currently", huh)

def getdisplayWord(secretWord):
    displayWord = []
    for i in range(len(secretWord)):
        if secretWord[i] in alphabet:
            displayWord.append("_")
        else: 
            displayWord.append(secretWord[i])
    return displayWord

def maingame():
    #why global?
    global Player
    global alphabet
    Player = 1
    secretWord = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Continue = True
   

    
    while Continue:
        if Player == 1:
            print()
            secretWord = input('Whats the word bird? ').upper()
            for i in range(40):
                print()
            Player = 2
            print('Player', Player, 'Guess the word homie')
            LetsPlay(secretWord)
        elif Player == 2:
            print('Game over')
            for i in range(40):
                print()
            Player = 1
            print('Player')

quit = input('Done?(Y/N): ')       
if quit == 'Y' or quit == 'y':
    Continue = False
    
    
maingame()


