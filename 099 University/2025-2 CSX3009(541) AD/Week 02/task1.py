# Puran Paodensakul
# 6611140
# 541

import sys

sys.setrecursionlimit(10000)

x = []
n = 0

def comb(i):
    if i == n:
        print("".join(map(str, x)))
        return

    x[i] = 0
    comb(i + 1)

    x[i] = 1
    comb(i + 1)

if __name__ == "__main__":
    n = int(input())
    x = [0] * n
    comb(0)