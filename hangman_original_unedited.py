def gamePlay(secretWord):
	failedGuesses = 0
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	guess = ""
	displayWord = getDisplayWord(secretWord)
	gameOver = False

	while not gameOver:
		invalidInput = True
		while invalidInput:
			print("Player", Player, end = "")
			guess = input(", please guess a letter: ").upper()
			if len(guess) > 1 or guess not in alphabet:
				print("You did enter a valid guess. Please try again.")
			else:
				invalidInput = False
		if guess in secretWord:
			for i in range(len(secretWord)):
				if secretWord[i] == guess:
					displayWord[i] = guess
			printWord(displayWord)
			if "_" not in displayWord:
				print("Player", Player, " wins!")
				gameOver = True
		else:
			failedGuesses += 1
			print("Your guess is incorrect! Please try again.")
			print("Hangman Status: ", end = "")

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
			print("Number of chances left:", 6-failedGuesses)

			printWord(displayWord)
							
def printWord(displayWord):
	word = ""
	for i in range(len(displayWord)):
		word += displayWord[i]
	print()
	print("Current Progress: ", word)

def getDisplayWord(secretWord):
	displayWord = []
	for i in range(len(secretWord)):
		if secretWord[i] in alphabet:
			displayWord.append("_")
		else:
			displayWord.append(secretWord[i])
	return displayWord

def main():
	global Player
	global alphabet
	Player = 1
	secretWord = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"		
	Continue = True

	while Continue:		
		if Player == 1:
			print()
			secretWord = input("Player one, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 2
			print("Player 2 must guess Player's One's word")
			gamePlay(secretWord)
		elif Player == 2:
			print()
			secretWord = input("Player two, please enter your secret word: ").upper()
			for i in range(50):
				print()
			Player = 1
			print("Player 1 must guess Player's Two's word")
			gamePlay(secretWord)
		quit = input("Do you want to quit? (Yes/No): ").upper()
		if quit == "YES" or quit == "Y" or quit=='y':
			Continue = False
	print()
	print("Thank you for playing Hangman!")

main()