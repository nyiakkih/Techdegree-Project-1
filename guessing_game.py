"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import random
from statistics import mean, median, mode

scoreboard = []

def stats():
    score_mean = mean(scoreboard)
    score_median = median(scoreboard)
    score_mode = mode(scoreboard)
    print(f"Mean of your attempts: {score_mean}")
    print(f"Median of your attempts: {score_median}")
    print(f"Mode of your attempts: {score_mode}")

def highscore():
    score_min = min(scoreboard)
    print(f"Highscore: {score_min}")

def intro():
    print("Welcome to \"Can You Guess the Number?\"")

def start_game():
    print("Instructions: Guess a number between 1 and 100!")
    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess > 100 or guess < 1:
                raise ValueError("Try entering a number between 1 and 100.")
            
        except ValueError as err:
            if "invalid literal for int()" in str(err):
                print("That is not a valid number. Please enter a number between 1 and 100.")
            else:
                print(err)
            continue   
            
        else:
            if guess == answer:
                print("You got it!")
                break
            elif guess > answer:
                print("It's lower.")
                continue
            elif guess < answer:
                print("It's higher.")
                continue

    print(f"It took you {attempts} attempts.")
    scoreboard.append(attempts)

    new_game = input("Would you like to play again? (Y/N)  ").upper()
    if new_game == "Y":
        highscore()    
        start_game()
    elif new_game == "N":
        print("Thank you for playing!")
        stats()   

intro()
start_game()