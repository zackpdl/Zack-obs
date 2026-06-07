# Puran Paodensakul
# 6611140
# 541
import sys

sys.setrecursionlimit(10000)

values = []
n = 0
total_sum = 0
min_diff = float('inf')

def split_balance(index, current_sum_group0):
    global min_diff

    if index == n:
        sum_group1 = total_sum - current_sum_group0
        diff = abs(current_sum_group0 - sum_group1)
        min_diff = min(min_diff, diff)
        return

    split_balance(index + 1, current_sum_group0 + values[index])

    split_balance(index + 1, current_sum_group0)

if __name__ == "__main__":
    input_line = input("Enter values : ")
    values = list(map(int, input_line.split()))
    n = len(values)
    total_sum = sum(values)

    split_balance(0, 0)
    print(min_diff)
