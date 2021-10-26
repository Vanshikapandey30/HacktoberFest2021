#Password Generator Project
#Chandrajit Satapathy
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# chandrajit satapathy

password=[]

for r in range(1,nr_letters+1):
  y= random.randint(0,len(letters)-1)
  z= letters[y]
  #print(z)
  password+=z

for q in range(1,nr_symbols+1):
  s= random.randint(0,len(symbols)-1)
  t= symbols[s]
  #print(t) 
  password+=t
for p in range(1,nr_numbers+1):
  a= random.randint(0,len(numbers)-1)
  b= numbers[a]
  #print(b)
  password+=b

#print(password)

random.shuffle(password)

final_password=""
for char in password:
  final_password+=char

print(f"Your password is '{final_password}' ")