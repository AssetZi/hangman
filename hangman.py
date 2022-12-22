import random 

def hangman(word):
	wrong = 0
	stages = [
	"",
	"----------  ",
	"|     |     ",
	"|     |     ",
	"|     O     ",
	"|    /|\    ",
	"|    / \    ",
	"|           ",
	]

	right_letters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman.")

	while wrong < len(stages) - 1:
		print("\n")
		msg = "Guess a letter: "
		char = input(msg)
		if char in right_letters:
			cind = right_letters \
			    .index(char)
			board[cind] = char
			right_letters[cind] = '$'
		else:
			print("WRONG! Try again.")
			wrong += 1

		print((" ".join(board)))
		e = wrong + 1
		print("\n"
			.join(stages[0:e]))
		if "__" not in board:
			print("You Win!")
			print("".join(board))
			win = True
			break

	if not win:
		print("\n"
			.join(stages[0: \
				wrong]))
		print(f"You lose! it was {word}.")





list_of_words = ["brock", "stephanie", "mia", "gavazzi",
"pie", "coffee", "steak"]
x = len(list_of_words) - 1

random_num = random.randint(0, x)
random_word = list_of_words[random_num]


hangman(random_word)



