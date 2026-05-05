# Puran Paodensakul
# 6611140
# 541   

N = int(input())

colors = []
for _ in range(N):
    V, D = map(int, input().split())
    colors.append((V, D))

min_diff = float('inf')

for mask in range(1, 1 << N):
    vividness = 1
    dullness = 0

    for i in range(N):
        if mask & (1 << i):
            vividness *= colors[i][0]
            dullness += colors[i][1]

    diff = abs(vividness - dullness)
    min_diff = min(min_diff, diff)

print(min_diff)
