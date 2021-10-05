import random
import time
import sys
from typing import Optional

#global variables
rock = ["rock","r", "1"]
paper = ["paper","p", "2"]
scissors = ["scissors", "s", "3"]
r = "rock"
p = "paper"
s = "scissors"
user_choice = ""
choices = ["rock", "paper", "scissors"]

#some shit
print("Welcome to the Rock Paper Scissors game made by Birb#2018\n")
time.sleep(1)
name = input("Enter your name here: \n")
print(f"\nHello {name}! If you don't know the rules of Rock Paper Scissors then you have no childhood.\n")
time.sleep(2)
print("Let's play!")
time.sleep(1)

#replay
def loop():
    play_game = ""
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? Y or N \n")
        time.sleep(1)

    if play_game.lower() == "y":
        main()

    else:
        print("\nThanks For Playing! Come back another time!")
        sys.exit()

def logic(one: str, two: str):
    if one == two:
        return None
    elif one == "scissors" and two == "rock":
        return "rock_uno"
    elif one == "paper" and two == "rock":
        return "rock_dos"

    elif one == "rock" and two == "paper":
        return "paper_uno"
    elif one == "scissors" and two == "paper":
        return "paper_dos"

    elif one == "paper" and two == "scissors":
        return "scissors_uno"
    elif one == "rock" and two == "scissors":
        return "scissors_dos"
    else:
        return False

#actual game
def main():
    bot = random.choice(choices)
    user_choice = input("\n1. Rock\n2. Paper\n3. Scissors\n")
    print(bot)
    time.sleep(1)

    if user_choice.lower() in rock:
        user = "rock"
    elif user_choice.lower() in paper:
        user = "paper"
    elif user_choice.lower() in scissors:
        user = "scissors"
    else:
        print("\nThat's not in any of the choices! Try again.")
        time.sleep(1)
        print("Loading...")
        time.sleep(2)
        main()

    result = logic(bot, user)

#same choice
    if result is None:
        print("\nTie!")
        time.sleep(1)
        print("Again\n")
        main()

#game logic
    if result == "rock_uno":
        print("\nCongrats! You 'rocked' the world!\n")
        time.sleep(2)
        loop()
    elif result == "rock_dos":
        print("\nSorry, the paper wrapped around you and made you feel like you're in your moms womb again.\n")
        time.sleep(2)
        loop()

    elif result == "paper_uno":
        print("\nCongrats! You've sent the rock to santa to give him a gift!\n")
        time.sleep(2)
        loop()
    elif result == "paper_dos":
        print("FINISH HIM!!!")
        time.sleep(1)
        print("FATALITY!!!")
        time.sleep(1)
        print("\nSorry, you've been cut in half.\n")
        time.sleep(2)
        loop()

    elif result == "scissors_uno":
        print("\nCongrats! You scissored the paper!\n")
        time.sleep(2)
        loop()
    elif result == "scissors_dos":
        print("\nSorry, you've been Super Smashed Bro.\n")
        time.sleep(2)
        loop()
    else:
        print("An error has occured")
        print("Forgive me and play again")
        main()

main()
