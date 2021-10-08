def bubblesort(a, number):
    for i in range(number -1):
        for j in range(number - i - 1):
            if(a[j] > a[j + 1]):
                temp = a[j] # a[j],a[j+1]=a[j+1],a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
a = []
number = int(input("Enter the total number of Elements : "))
for i in range(number):
    value = int(input("Enter the %d Element of List : " %i))
    a.append(value)
bubblesort(a, number)
print("The Sorted List in Ascending Order : ", a)
