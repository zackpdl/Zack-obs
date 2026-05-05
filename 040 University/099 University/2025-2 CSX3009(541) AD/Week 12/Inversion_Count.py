# Puran Paodensakul
# 542
# 6611140

import sys
sys.setrecursionlimit(10**7)

def merge_count(arr, temp, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_count(arr, temp, left, mid)
    inv_count += merge_count(arr, temp, mid + 1, right)

    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    arr[left:right + 1] = temp[left:right + 1]
    return inv_count


def inversion_count(arr):
    temp = [0] * len(arr)
    return merge_count(arr, temp, 0, len(arr) - 1)


input = sys.stdin.read
data = input().split()

t = int(data[0])
idx = 1

results = []

for _ in range(t):
    n = int(data[idx])
    idx += 1

    arr = list(map(int, data[idx:idx + n]))
    idx += n

    results.append(str(inversion_count(arr)))

print("\n".join(results))
