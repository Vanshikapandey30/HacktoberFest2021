import random
import time


class Tries(Exception):
    pass


class RangeError(Exception):
    pass


print("Welcome to Number Guessing Game\n\n")
time.sleep(0.8)
choice = int(input("Press 1 to Guess a number\n"
                   "Press 2 to make computer guess a number:"))

if choice == 1:
    num = random.randint(1, 30)
    tries = 10
    while True:
        try:
            if tries == 0:
                raise Tries
            print(f"\n{tries} tries remaining")
            userInput = int(input("Entering a number other than given range will result in penalty\n"
                                  "Enter a number between 1 to 30:"))
            print()
            
            if userInput > 30 or userInput < 1:
                tries -= 2
                raise RangeError
            
            if userInput == num and tries != 0:
                time.sleep(0.5)
                print("Congratulations you guessed the correct number")
                break
            
            elif userInput > num and tries != 0:
                time.sleep(0.8)
                tries -= 1
                print(f"You guessed wrong number, try something lower \n")
                time.sleep(0.8)
            
            elif userInput < num and tries != 0:
                tries -= 1
                time.sleep(0.8)
                print(f"You guessed wrong number, try something higher \n")
                time.sleep(0.8)
        
        except Tries:
            time.sleep(0.5)
            print("No more tries left")
            break
        
        except RangeError:
            time.sleep(0.8)
            print()
            print("Enter a number between 1 to 50 only")
            time.sleep(0.7)
            print("As a penalty your 2 tries are deducted")
            time.sleep(0.8)
        
        except ValueError:
            time.sleep(0.6)
            print("Enter a valid input")

if choice == 2:
    
    print("Enter a range for computer to guess the number\n")
    time.sleep(0.4)
    s = int(input("Enter the starting number for range:"))
    time.sleep(0.4)
    e = int(input("Enter the ending number for range:"))
    time.sleep(0.4)
    guess = random.randint(s, e)
    count = 1
    while True:
        try:
            x = int(input("Enter the secret number:"))
            if x < s or x > e:
                raise RangeError
            
            print(f"Guessed number is: {guess}")
            if guess == x:
                print(f"Computer guessed your number in {count} tries")
                break
            elif guess > x:
                time.sleep(0.4)
                e = guess - 1
                guess = random.randint(s, e)
                count += 1
            else:
                time.sleep(0.4)
                s = guess + 1
                guess = random.randint(s, e)
                count += 1
        
        except RangeError:
            time.sleep(0.5)
            print("Enter a number between specified range only.")
