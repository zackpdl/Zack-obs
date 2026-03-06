# Puran Paodensakul
# 542
# 6611140

MOD = 2147483647

def power(a, x):
    if x == 0:
        return 1

    half = power(a, x // 2)
    half = (half * half) % MOD

    if x % 2 == 0:
        return half
    else:
        return (a * half) % MOD

a, x = map(int, input().split())
print(power(a, x))
