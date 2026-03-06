# Puran Paodensakul
# 541
# 6611140

import sys

sys.setrecursionlimit(30000)

d = 3
n = d * d
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(r, c):
    return 0 <= r < d and 0 <= c < d

class State:
    def __init__(self, p, g=0, h=0):
        self.p = p
        self.g = g
        self.h = h

def manhattan(p):
    h = 0
    for i in range(n):
        if p[i] != 0:
            tr, tc = i // d, i % d
            gr, gc = p[i] // d, p[i] % d
            h += abs(tr - gr) + abs(tc - gc)
    return h

def find_hole(p):
    return p.index(0)

def successor(s):
    succ = []
    hole = find_hole(s.p)
    r, c = hole // d, hole % d

    for dr, dc in adj:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc):
            new_p = list(s.p)
            new_idx = nr * d + nc
            new_p[hole], new_p[new_idx] = new_p[new_idx], new_p[hole]
            new_p = tuple(new_p)
            succ.append(State(new_p, s.g + 1, manhattan(new_p)))
    return succ

found = False
min_exceed = float('inf')

def DLS(s, threshold, path):
    global found, min_exceed
    f = s.g + s.h

    if f > threshold:
        min_exceed = min(min_exceed, f)
        return None

    if s.h == 0:
        found = True
        return s.g

    path.add(s.p)

    for u in successor(s):
        if u.p not in path:
            res = DLS(u, threshold, path)
            if found:
                return res

    path.remove(s.p)
    return None

def IDAstar(start):
    global found, min_exceed
    start.h = manhattan(start.p)

    threshold = start.h
    while True:
        path = set()
        min_exceed = float('inf')
        result = DLS(start, threshold, path)
        if found:
            return result
        if min_exceed == float('inf'):
            return -1
        threshold = min_exceed

def main():
    nums = []
    for _ in range(d):
        nums.extend(map(int, sys.stdin.readline().split()))
    start = State(tuple(nums))
    print(IDAstar(start))

if __name__ == "__main__":
    main()
