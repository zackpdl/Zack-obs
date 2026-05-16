# Puran Paodensakul
# 541
# 6611140
import sys

sys.setrecursionlimit(30000)

d = 3
n = d * d
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class State:
    def __init__(self, p, g=0):
        self.p = p
        self.g = g

def is_goal(s):
    for i in range(n):
        if s.p[i] != i:
            return False
    return True

def find_hole(p):
    return p.index(0)

def is_valid(r, c):
    return 0 <= r < d and 0 <= c < d

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
            succ.append(State(new_p, s.g + 1))
    return succ

count = 0

def DLS(s, maxDepth, visited):
    global count

    if s.g > maxDepth:
        return -1

    if is_goal(s):
        return s.g

    board = tuple(s.p)
    if board in visited and visited[board] <= s.g:
        return -1

    visited[board] = s.g
    count += 1

    for u in successor(s):
        res = DLS(u, maxDepth, visited)
        if res != -1:
            return res
    return -1

def IDS(start):
    depth = 0
    while True:
        visited = {}
        res = DLS(start, depth, visited)
        if res != -1:
            return res
        depth += 1

def main():
    nums = []
    for _ in range(d):
        nums.extend(map(int, sys.stdin.readline().split()))
    start = State(nums)

    if is_goal(start):
        print(0)
    else:
        print(IDS(start))

if __name__ == "__main__":
    main()
