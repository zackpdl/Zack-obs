import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

def nWays(d, s):
    if d == L:
        
    else:
        counter = 0
        if s == FLAT:
            
        else:  # s is either UPPER2 or LOWER2
            
        return counter

print(nWays(0, FLAT))


