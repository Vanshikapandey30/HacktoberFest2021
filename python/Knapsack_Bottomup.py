#knapsack bottomUp approach to get the maximum profit and profit table using Dynamic Programming
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
w_k = 7
n = len(wt)

t = [[0 for i in range(w_k + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, w_k + 1):

        if wt[i - 1] <= j:
            t[i][j] = max((val[i - 1] + t[i - 1][j - wt[i - 1]]), t[i - 1][j])

        else:
            t[i][j] = t[i - 1][j]

print("max profit: ", t[-1][-1])
print()
print("profit table")
for i in range(n + 1):
    print(t[i])
