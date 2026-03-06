import time

# Puran Paodensakul
# 6611140
# 541

def MinChange(n, C, memo=None):
    if memo is None:
        memo = {}
    
    if n == 0:
        return 0
    
    if n in memo:
        return memo[n]
    
    v = float('inf')
    for c in C:
        if c <= n:
            v = min(MinChange(n - c, C, memo) + 1, v)
    
    memo[n] = v
    return v

coins_input = input().strip().split()
C = [int(coin) for coin in coins_input]

n = int(input().strip())

start_time = time.time()
result = MinChange(n, C)
end_time = time.time()

print(f"Result: {result}")
print(f"Time: {end_time - start_time:.4f}s")