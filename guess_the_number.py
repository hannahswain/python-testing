

# Write a programme where the computer randomly generates a number between 0 and 20. 
# The user needs to guess what the number is. If the user guesses wrong, tell them their 
# guess is either too high, or too low. This will get you started with the 
# random library if you haven't already used it.

import random

def help():
	print()
	print("The game will chose a random number between 1 and 20. Guess until you figure it out.")
	print()
	
	
help()

random_number = random.randint(1,20)
guessed_right = False

# Print these for testing purposes
print(random_number)
# print(guessed_right)

while guessed_right == False:
	current_guess = int(input("Choose a number between 1 and 20: "))
	
	if current_guess >  20 or current_guess < 1:
		print("That number isn't between 1 and 20. Try again.")
	elif current_guess == random_number:
		# print("You guessed {} and that's right! You win!".format(current_guess))
		print(f"You guessed {current_guess} and that's right! You win!")
		guessed_right = True
	else:
		# print("You guessed {} and that's not it. Try again!".format(current_guess))
		print(f"You guessed {current_guess} and that's not it. Try again!")
	
print("Thanks for playing. :)")
