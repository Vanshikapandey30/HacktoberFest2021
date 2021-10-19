from random import randint

z= randint(0,50)


for i in range(0,5):
    guess = int(input("Just guess a number between (0,50)"))
    if z>guess:
        print("Number is higher")
    elif z<guess:
        print("Number is lower")
    else:
        print("Yo you won the match")
        break

print("Number is :",z)
