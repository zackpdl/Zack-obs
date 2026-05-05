# Puran Paodensakul
# 542
# 6611140

n = int(input())
activities = []

for _ in range(n):
    s, t = map(int, input().split())
    activities.append((s, t))

activities.sort(key=lambda x: x[1])

count = 0
last_finish = -1

for s, t in activities:
    if s >= last_finish:
        count += 1
        last_finish = t

print(count)
