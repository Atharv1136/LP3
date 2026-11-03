# 0/1 knapsack problem using dynamic programming
#Practical: 04
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    profit.append(int(input("Enter profit: ")))
    weight.append(int(input("Enter weight: ")))

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weight[i - 1] <= w:
            dp[i][w] = max(profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                           dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum Profit =", dp[n][capacity])