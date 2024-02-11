"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
from statistics import mean, median, mode

scoreboard = []
# Create the start_game function.
# Write your code inside this function.
def intro():
  print("Welcome to \"Can You Guess the Number?\"")

def start_game():
  print("Instructions: Guess a number between 1 and 100!")
  answer = random.randint(1, 100)
  attempts = 0

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
while True:
    try:
      guess = int(input("Enter your guess: "))
      attempts += 1
      if guess > 100:
        raise ValueError("Guess has to be a number between 1 and 100")
      elif guess < 1:
        raise ValueError("Guess has to be a number between 1 and 100")
        
    except ValueError as err:
      print("That is not a valid value, try again.")
      
    else:
      if guess == answer:
        print("You got it!")
        break
      elif guess > answer:
        print("It's lower.")
      elif guess < answer:
        print("It's higher.")

print(f"It took you {attempts} attempts.")
scoreboard.append(attempts)
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
