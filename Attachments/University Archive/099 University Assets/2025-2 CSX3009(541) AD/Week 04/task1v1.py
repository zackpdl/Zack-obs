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

def comb(i):
    global rc
    rc += 1

    if i == N:
        sw, sv = 0, 0
        for j in range(N):
            if x[j] == 1:
                sw += w[j]
                sv += v[j]
        if sw > M: return -1 # after sum weight, check if exceed capacity. If sum of weights exceed M then make it invalid
        else: return sv

    else:
        x[i] = 0
        a = comb(i + 1)
        x[i] = 1
        b = comb(i + 1)
        return max(a, b)

print("Maximum value in Knapsack = ", comb(0))
print("Recursive calls =", rc)

end_time = time.process_time()
print(f"Execution time: {end_time - start_time:.6f}")