# Puran Paodensakul
# 6611140
# 541



import time 
import sys
start_time = time.process_time()

N, M = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

x = [0] * N
rc = 0

def maxVal(i, C): # C: current capacity
    global rc
    rc += 1
    if i == N: return 0
    else:
        skip = maxVal(i + 1, C)
        if w[i] <= C: take = v[i] + maxVal(i + 1, C - w[i])
        else: take = -1 # cannot take item i, Make it invalid
        return max(skip, take)

print("Maximum value in Knapsack = ", maxVal(0, M))
print("Recursive calls =", rc)

end_time = time.process_time()
print(f"Execution time: {end_time - start_time:.6f}")