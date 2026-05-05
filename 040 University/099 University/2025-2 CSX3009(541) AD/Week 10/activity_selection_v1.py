# Puran Paodensakul
# 542
# 6611140

n = int(input())

activities = []
for _ in range(n):
    s, t = map(int, input().split())
    activities.append((s, t))

activities.sort(key=lambda x: x[1])

count = 1
last_finish = activities[0][1]

for i in range(1, n):
    if activities[i][0] >= last_finish:
        count += 1
        last_finish = activities[i][1]

print(count)
