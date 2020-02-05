#  0-1 Knapsack problem. Dynamic Programming
# Returns the number of optimal values and the maximum value that can be put in a knapsack of capacity W
import datetime

# n - number of items
# W - capacity of knapsack
# v - value
# wt - weight
def knapsack(W, wt, val, n):
    T = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build a table T[][] (bottom-up)
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                T[i][w] = 0
            elif wt[i-1] <= w:
                T[i][w] = max(val[i-1] + T[i-1][w-wt[i-1]],  T[i-1][w])
            else:
                T[i][w] = T[i-1][w]

    #find optimal solution

    max_el = T[i][w]
    mass = []
    while i >0 and w > 0:
        if T[i][w]!= T[i-1][w]:
            mass.append(i)
            w=w-wt[i-1]
            i = i - 1
        else:
            i = i - 1
    return mass,max_el

# Test function

#input data

val = [60, 100, 120, 100, 80, 75]
wt = [10, 20, 30, 55, 25, 30]
W = 50
n = len(val)

a = datetime.datetime.now()
print(knapsack(W, wt, val, n))
b = datetime.datetime.now()
print(b-a)
#time calculation
