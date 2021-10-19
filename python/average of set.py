def average(array):
    # your code goes here
    #array = set()
    x= len(array)
    y=sum(array)
    return y/x


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
