# Puran Paodensakul
# 6611140
# 541

import time 
import sys
start_time = time.process_time()

N, M = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

rc = 0
memo = {} # Memoization table

def maxVal(i, C): # C: current capacity
    global rc
    rc += 1

    if (i, C) in memo:
        return memo[(i, C)]

    if i == N:
        return 0
    else:
        skip = maxVal(i + 1, C)
        take = -1 # Initialize take as invalid
        if w[i] <= C:
            take = v[i] + maxVal(i + 1, C - w[i])
        
        result = max(skip, take)
        memo[(i, C)] = result
        return result

print("Maximum value in Knapsack = ", maxVal(0, M))
print("Recursive calls =", rc)

end_time = time.process_time()
print(f"Execution time: {end_time - start_time:.6f}")
