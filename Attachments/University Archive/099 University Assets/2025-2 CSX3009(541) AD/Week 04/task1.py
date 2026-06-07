import sys
sys.setrecursionlimit(10000)

p = input().split()
L = len(p)
for i in range(L):
    p[i] = int(p[i])
p.insert(0, 0)

calls = [0] * (L + 1)

def maxRev(l):
    global p, L, calls
    calls[l] += 1
    if l == 0:
        return 0
    mx = 0
    for j in range(1, l + 1):
        mx = max(mx, p[j] + maxRev(l - j))
    return mx

print(maxRev(L))
print(calls)
# Example usage:
# Input: "1 5 8 9 10 17 17 20 24 30"
# Output: 30