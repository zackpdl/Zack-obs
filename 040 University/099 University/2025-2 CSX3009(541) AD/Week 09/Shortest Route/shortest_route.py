# Puran Paodensakul
# 541
# 6611140

import sys
import heapq

class Node:
    def __init__(self, city, dist):
        self.city = city
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist


def ucs(adj, V, start, goal):
    pq = []
    dist = [float('inf')] * V

    dist[start] = 0
    heapq.heappush(pq, Node(start, 0))

    while pq:
        cur = heapq.heappop(pq)
        u = cur.city

        if u == goal:
            return cur.dist

        if cur.dist > dist[u]:
            continue

        for v, w in adj[u]:
            new_d = dist[u] + w
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(pq, Node(v, new_d))

    return -1


def main():
    V = int(sys.stdin.readline())
    adj = [[] for _ in range(V)]

    for line in sys.stdin:
        u, v, w = map(int, line.split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    print(ucs(adj, V, 0, V - 1))


if __name__ == "__main__":
    main()
