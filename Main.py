# Rock, Paper, Scissors Game
import random

choices = ["rock","paper","scissors"]
player = None
computer = random.choice(choices)
yes_no = ["yes","no"]

while True:
    while player not in choices:
        player = input("choose rock,paper or scissors: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("you chose: ",player)
        print("it's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ", computer)
            print("you chose: ", player)
            print("win")
        if computer == "paper":
            print("computer: ", computer)
            print("you chose: ", player)
            print("lose")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("you chose: ", player)
            print("win")
        if computer == "scissors":
            print("computer: ", computer)
            print("you chose: ", player)
            print("lose")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("you chose: ", player)
            print("win")
        if computer == "rock":
            print("computer: ", computer)
            print("you chose: ", player)
            print("lose")

    again = input("Play again?: ")

    if again != "yes":
        break

print("boo hoo")
