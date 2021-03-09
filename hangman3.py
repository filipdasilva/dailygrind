alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
player = 1

def Game():
    global alphabet
    global player
    global secretWord
    global Continue
    count = 0
    Invalid = True
    
    while Invalid:
        print('Player', player)
        guess = input('What is your guess? ').upper()
        if len(guess) < 1 or guess not in alphabet:
            print('try again brudda')
        elif guess in secretWord:
            print(secretWord)
            Continue = False
            
        elif guess not in secretWord:
            if count == 0:
                print('Incorrect thats strike 1 nerd')
                print('0')
                count = count + 1
            elif count == 1:
                print('Incorrect thats strike 2 buddy')
                print('0_')
                count = count + 1
            elif count == 2:
                print('Incorrect thats strike 3 broski')
                print('0_0')
                count = count + 1
            elif count == 3:
                print('Incorrect thats strike 4 come on last try')
                print('X_0')
                count = count + 1
            elif count == 4:
                print('Incorrect thats the game bud')
                print('X_X')
                count = count + 1
                Invalid = False
        
        
def getdisplayWord(secretWord):
    for i in secretWord:
        letter = secretWord[i]
        letter.append('_')
        
def printWord(secretWord):
    secretWord
        
#secretWord = 'jimmy'.upper()
#Game()


def main():
    global alphabet
    global player
    global secretWord
    Continue = True
    
    while Continue == True:
        if player == 1:
            print('Player 1 what is your secret word? ')
            secretWord = input('Enter here: ').upper()
            for i in range(40):
                print()

            player = 2
            Game()
        elif player == 2:
            print('Player 2 what is your secret word? ')
            secretWord = input('Enter here: ').upper()
            for i in range(40):
                print()

            player = 1
            Game()
        quit = input('Do you want to quit? (Y/N): ').upper()
        if quit == 'YES' or quit == 'Y':
                Continue = False
        
        
main()
        