# Puran Paodensakul
# 6611140
# 541


N, W = map(int, input().split())

v = []
w = []

for i in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

dp = [0] * (W + 1)

for i in range(N):
    for c in range(W, w[i] - 1, -1):
        dp[c] = max(dp[c], dp[c - w[i]] + v[i])

print(dp[W])
