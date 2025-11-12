
'''
Guessgame.PY:
Gissa tal spel med 7 försök

__author__  = "Didi Sandström"
__version__ = "2.0.0"
__email__   = "diditimaogui.sandstrom@elev.ga.dbgy.se"
'''

import random
import os
from bcolors import bcolors
game = True
while game == True:
    os.system('cls')
    answer = random.randint(1,100)
    tries = 0
    print(f"{bcolors.YELLOW}Hello! Welcome to my number guessing game. You will only have 7 tries to guess a number between 1-100")
    for x in range(7):
        try:
            guess = int(input(f"{bcolors.YELLOW}Guess a number"))
        except:
            print(f"{bcolors.RED}Ogiltigt format, skriv in en siffra!")
            continue
        tries = tries + 1
        if guess == answer:
            print(f"{bcolors.GREEN}CONGRATS YOU WON{bcolors.DEFAULT}")
            break
        elif guess == 0:
            print(f"{bcolors.BLUE}ANSWER IS: {bcolors.DEFAULT}", answer)
        elif guess > answer:
            print(f"{bcolors.YELLOW}The number is lower")
        elif guess < answer:
            print("The number is higher")
    print(f"{bcolors.YELLOW}Game over")
    print(f"{bcolors.YELLOW}:", tries,"/ 7")
    continue_1 = str(input("Do you want to continue? y/n"))
    if continue_1 == "y":
        print("Initiating new game")
        game = True
        continue
    if continue_1 == "n":
        print("Stopping game")
        game = False