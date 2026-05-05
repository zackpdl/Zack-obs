# Puran Paodensakul
# 542
# 6611140

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

ds = DisjointSet(V)
mst_weight = 0
edges_used = 0

for w, u, v in edges:
    if ds.union(u, v):
        mst_weight += w
        edges_used += 1
        if edges_used == V - 1:
            break

print(mst_weight)
