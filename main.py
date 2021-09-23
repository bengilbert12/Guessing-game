import math
import random


def gen_num(start, end):
	return random.randint(start, end)

def check_ans(x, y):
	if x == y:
		return True
	else:
		return False



def hint(x):
	if x % 2 == 0:
		print("The number is even")
	else:
		print("The number is odd")

def play():
	print("Welcome to the guessing game!")
	

	still_playing = True
	still_guessing = True

	while still_playing:
		guess_count = 0
		max_guess_count = 5

		print("Generating number...")
		still_guessing = True
		answer = gen_num(1, 20)

		while still_guessing:

			guess = int(input("\nEnter your guess:"))
			guess_count += 1

			if guess_count == max_guess_count:
				print("You're out of guesses.\n-- Game over --")
				still_guessing = False
				break

			if check_ans(guess, answer):
				print("You did it!")
				break

			elif not check_ans(guess, answer):
				print("Sorry, you're wrong.")

		play_again = input("Would you like to play again? (y or n)\n")

		if play_again == "y":
			continue
		else:
			print("Thanks for playing!")
			break


play()
