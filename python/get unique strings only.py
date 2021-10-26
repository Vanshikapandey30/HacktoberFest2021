# Enter your code here. Read input from STDIN. Print output to STDOUT
get = int(input("enter no. of countries you going to enter"))
x= set()
for i in range(0,get):
    x.add(input("enter country name"))

print(x.__len__())
