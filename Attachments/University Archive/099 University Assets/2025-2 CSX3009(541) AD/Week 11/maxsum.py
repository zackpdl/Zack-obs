# Puran Paodensakul
# 542
# 6611140

import sys

def max_crossing_sum(arr, left, mid, right):
    left_sum = -float('inf')
    total = 0
    for i in range(mid, left - 1, -1):
        total += arr[i]
        left_sum = max(left_sum, total)

    right_sum = -float('inf')
    total = 0
    for i in range(mid + 1, right + 1):
        total += arr[i]
        right_sum = max(right_sum, total)

    return left_sum + right_sum


def max_sub_sum(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    left_max = max_sub_sum(arr, left, mid)
    right_max = max_sub_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


n = int(input())
arr = list(map(int, input().split()))

print(max_sub_sum(arr, 0, n - 1))
