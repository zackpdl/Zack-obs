# Puran Paodensakul
# 542
# 6611140

MOD = 2147483647

a, x = map(int, input().split())

result = 1

for _ in range(x):
    result = (result * a) % MOD

print(result)
