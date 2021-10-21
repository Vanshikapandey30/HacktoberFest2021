"""
Author : sanamkandar
project: game snake water gun
"""
import random

print("\t\t\t\t\t\t\t\t-: GAME SNAKE WATER GUN :-")
print("\t\t\t\t\t\t\t\t   YOU HAVE 10 CHANCES")

usr_point = 0
comp_point = 0
chance = 0

while chance<10:

    user = input(f"Enter s for Snake, w for Water, g for Gun:- {10-chance} chance left: \n").lower()

    if user == "s" or user == "w" or user == "g":   # IF statement for to pass only s,w,g otherwise print invalid.
        pass
    else:
        print("INVALID INPUT. \n")
        continue

    element = ["snake", "water", "gun"]
    computer = random.choice(element)


    if user == "s" and computer == "snake":     # game tie block
        print("draw!\n")
        continue
    if user == "w" and computer == "water":
        print("draw!\n")
        continue
    if user == "g" and computer == "gun":
        print("draw!\n")
        continue


    chance = chance + 1

    if user == "s" and computer == "water":
        print("user win! - snake drink all water! \n")
        usr_point = usr_point+1                             # incrementing points
    elif user == "s" and computer == "gun":
        print("computer win! - snake shooted by gun! \n")
        comp_point = comp_point+1

    elif user == "w" and computer == "snake":
        print("computer win! - snake drink all water! \n")
        comp_point = comp_point+1
    elif user == "w" and computer == "gun":
        print("user win! - water slow down gun's bullet! \n")
        usr_point = usr_point+1

    elif user == "g" and computer == "snake":
        print("user win! - snake shooted by gun! \n")
        usr_point = usr_point+1
    elif user == "g" and computer == "water":
        print("computer win! - water slow down gun's bullet! \n")
        comp_point = comp_point+1

print("\t\t\t\t\----------SCOREBOARD------------")   # checking winner

if usr_point<comp_point:
    print(f"COMPUTER WIN THE GAME! WITH {comp_point} POINTS, YOU LOOSE WITH {usr_point} POINTS. ")
elif usr_point==comp_point:
    print(f"THE GAME IS TIE BOTH HAVE SAME POINTS {usr_point}. ")
else:
    print(f"CONGRATULATIONS! YOU WIN THE GAME WITH {usr_point} POINTS, COMPUTER LOOSE WITH {comp_point} POINTS. ")