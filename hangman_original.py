#this part defines multiple variables we are going to work with
def gamePlay(secretWord):
	failedGuesses = 0
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	guess = ""
	displayWord = getDisplayWord(secretWord)
	gameOver = False

#first we define what is happening when the round is on 
	while not gameOver:
		invalidInput = True
		while invalidInput:
			print("Player", Player, end = "")
            #when the game is on we are asking the player to input a guess for a letter and then the first if says your guess is invalid, if not then this round is over
			guess = input(", please guess a letter: ").upper()
            #the guess has to be one character and in the alphabet - aka if its more than 1 or not in the alphabet then we say invalid
			if len(guess) > 1 or guess not in alphabet:
				print("You did enter a valid guess. Please try again.")
			else:
                #this is what changes the round to be over
				invalidInput = False
                #now that we have a guess, we now know the guess is valid and we are looking for if it is in the secret word
		if guess in secretWord:
			for i in range(len(secretWord)):
				if secretWord[i] == guess:
					displayWord[i] = guess
                    #displayword and secret word are different, so if the guess is in the secret word then we will add to the display word
                    
                    #the game is over when there are no more ___ in the display word
                    
                    #QQ how does it know the displayword has any blanks at all? is it what the getdisplayword(secretword) does?
			printWord(displayWord)
			if "_" not in displayWord:
				print("Player", Player, " wins!")
				gameOver = True
		else:
            #this is failed guesses counter
			failedGuesses += 1
			print("Your guess is incorrect! Please try again.")
			print("Hangman Status: ", end = "")
#based on how many failed guesses you have is how the game knows what the face should look like
			if failedGuesses == 1:
				print("O")
			elif failedGuesses == 2:
				print("O-")
			elif failedGuesses == 3:
				print("O_O")
			elif failedGuesses == 4:
				print("O-<")
			elif failedGuesses == 5:
				print("O+<")
			elif failedGuesses == 6:
				print("You died!")
				gameOver = True
                #printing how many chances you have
			print("Number of chances left:", 6-failedGuesses)

			printWord(displayWord)
#unsure							
def printWord(displayWord):
	word = ""
	for i in range(len(displayWord)):
		word += displayWord[i]
	print()
	print("Current Progress: ", word)
#so this is what takes a secret word and turns it into a bunch of blanks
def getDisplayWord(secretWord):
	displayWord = []
	for i in range(len(secretWord)):
		if secretWord[i] in alphabet:
			displayWord.append("_")
		else:
			displayWord.append(secretWord[i])
	return displayWord

#defines whats going on right now - this is the gameplay
def main():
	global Player
	global alphabet
	Player = 1
	secretWord = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"		
	Continue = True
#when the round is going

#word must be under 50 letters
	while Continue:		
		if Player == 1:
			print()
			secretWord = input("Player one, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 2
			print("Player 2 must guess Player's One's word")
            
            #here we initiate gameplay and the entire first section becomes applicable
			gamePlay(secretWord)
		
        #this is already a new game so this one line ^ is the entire rturn
        elif Player == 2:
			print()
			secretWord = input("Player two, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 1
			print("Player 1 must guess Player's Two's word")
			gamePlay(secretWord)
            
            #dip then
		quit = input("Do you want to quit? (Yes/No): ").upper()
		if quit == "YES" or quit == "Y" or quit=='y':
            
            #if you say quit then continue stops
			Continue = False
	print()
	print("Thank you for playing Hangman!")

main()