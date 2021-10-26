# Fibonacci series

first=0
second =1

print(first,second,sep = '\n')

for i in range(0,6):
    nextvar = first+second
    print(nextvar)
    first,second = second,nextvar
