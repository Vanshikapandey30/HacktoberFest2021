print("enter list elements")
Ylist= input("separated by space")
my_list = Ylist.split()
print("enter target element")
target = int(input())
flag=0
for i in my_list:
    if my_list[int(i)] == target:
        flag=1
        break

if flag==1:
    print("element found in list")
else:
    print("No element found in list")
