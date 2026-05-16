# Puran Paodensakul
# 6611140
# 541


from functools import lru_cache
import time 
import sys
start_time = time.process_time()
sys.setrecursionlimit(100000000)

N, M = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

x = [0] * N # track items taken
rc = 0
# 2D Memoization table
mem = [[None] * (M + 1) for _ in range(N + 1)]
def maxValByMem(i, C): # i: current item index, C: current capacity
    global mem
    global rc
    rc += 1

    if mem[i][C] != None: return mem[i][C]

    if i == N: return 0
    else:
        skip = maxValByMem(i + 1, C)
        if w[i] <= C: 
            take = v[i] + maxValByMem(i + 1, C - w[i])
            result = max(skip, take)
        else: result = skip

        mem[i][C] = result
        return result

print("Maximum value in Knapsack = ", maxValByMem(0, M))
print("Recursive calls =", rc)

end_time = time.process_time()
print(f"Execution time: {end_time - start_time:.6f}")