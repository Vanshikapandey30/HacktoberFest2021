# from random import randint
#
# player1_choice = [("Rock", "Scissors"),("Scissors", "Paper"),("Paper","Rock")]
#
# player1 = input("Player1 enter your choice")
# player2 = input("Player2 enter your choice")
#
# if  player1 in player1_choice:
#     print("Player 1 is the winner")
# elif player1 == player2:
#     print("DRAW")
# else:
#     print("Lose player1")

import random
import getpass
import sys
player_wins=["scissorspaper","paperstone","stonescissors"]
choice=["scissors","paper","stone"]
player1=random.choice(choice)
player2 = input("Enter Player 2 choice ")#getpass.getpass(stream=sys.stderr, prompt="Enter")
player2=player2.lower()
if player1+player2 in player_wins:
    print("Player 1 wins")
    print("Player 1 enters ",player1)
elif player2+player1 in player_wins:
    print("Player 2 wins")
    print("Player 1 enters ",player1)
else :
    print("It's a tie")
    print("player 1 enters ",player1)
    print("player 2 enters ",player2)
