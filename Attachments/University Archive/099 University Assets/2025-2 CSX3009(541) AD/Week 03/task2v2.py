import time

# Puran Paodensakul
# 6611140
# 541

def CutRod(n, p, mem=None):
    if mem is None:
        mem = {}
    if n == 0:
        return 0
    if n in mem:
        return mem[n]
    q = 0
    for i in range(1, n + 1):
        q = max(p[i] + CutRod(n - i, p, mem), q)
    mem[n] = q
    return q

prices_input = input().strip().split()
p = [0] + [int(price) for price in prices_input]

n = len(p) - 1

start_time = time.time()
result = CutRod(n, p)
end_time = time.time()

print(f"Result: {result}")
print(f"Time: {end_time - start_time:.4f}s")
