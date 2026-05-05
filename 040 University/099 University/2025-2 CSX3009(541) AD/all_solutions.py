# This file is a compilation of all Python solutions from Week 1 to Week 7.

# ====================================================================================================
# Week 01: Maximum Contiguous Subsequence Sum
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: maxsum_v1.py
#
# Explanation:
# This solution finds the maximum contiguous subsequence sum using a brute-force approach with three
# nested loops. It iterates through all possible start and end points of a subarray, calculates the
# sum of each subarray, and keeps track of the maximum sum found. This approach has a time
# complexity of O(n^3).
# ----------------------------------------------------------------------------------------------------

def max_contiguous_subsequence_v1(arr):
    """
    Finds the maximum contiguous subsequence sum using a brute-force approach (O(n^3)).
    """
    max_so_far = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            if current_sum > max_so_far:
                max_so_far = current_sum
    return max_so_far

# ----------------------------------------------------------------------------------------------------
# Original Filename: maxsum_v2.py
#
# Explanation:
# This is an improved version of the brute-force approach with two nested loops. It iterates through
# all possible start points of a subarray and then iterates from that start point to the end of the
# array, calculating the sum as it goes. This reduces the time complexity to O(n^2).
# ----------------------------------------------------------------------------------------------------

def max_contiguous_subsequence_v2(arr):
    """
    Finds the maximum contiguous subsequence sum using an improved brute-force approach (O(n^2)).
    """
    max_so_far = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum > max_so_far:
                max_so_far = current_sum
    return max_so_far

# ----------------------------------------------------------------------------------------------------
# Original Filename: maxsum_v3.py
#
# Explanation:
# This solution uses Kadane's algorithm to find the maximum contiguous subsequence sum in linear time.
# It iterates through the array, keeping track of the maximum sum ending at the current position and
# the overall maximum sum found so far. This is the most efficient approach with a time complexity
# of O(n).
# ----------------------------------------------------------------------------------------------------

def max_contiguous_subsequence_v3(arr):
    """
    Finds the maximum contiguous subsequence sum using Kadane's algorithm (O(n)).
    """
    max_so_far = 0
    current_max = 0
    for x in arr:
        current_max += x
        if current_max < 0:
            current_max = 0
        if current_max > max_so_far:
            max_so_far = current_max
    return max_so_far

# ====================================================================================================
# Week 02: Recursion and Combinatorics
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: balance_split.py
#
# Explanation:
# This script solves the partition problem, which is to divide a set of numbers into two subsets
# such that the absolute difference between their sums is minimized. It uses a recursive approach
# to explore all possible combinations of including each number in one of the two groups.
# ----------------------------------------------------------------------------------------------------

def balance_split(values):
    """
    Solves the partition problem to find the minimum difference between the sums of two subsets.
    """
    total_sum = sum(values)
    min_diff = float('inf')
    n = len(values)

    def split_balance_recursive(index, current_sum_group0):
        nonlocal min_diff
        if index == n:
            sum_group1 = total_sum - current_sum_group0
            diff = abs(current_sum_group0 - sum_group1)
            min_diff = min(min_diff, diff)
            return

        # Include the current element in the first group
        split_balance_recursive(index + 1, current_sum_group0 + values[index])
        # Exclude the current element from the first group (it goes to the second group)
        split_balance_recursive(index + 1, current_sum_group0)

    split_balance_recursive(0, 0)
    return min_diff

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1.py
#
# Explanation:
# This script generates all possible binary combinations of a given length 'n'. It uses a recursive
# function that explores both possibilities (0 and 1) for each position in the binary string.
# ----------------------------------------------------------------------------------------------------

def generate_binary_combinations(n):
    """
    Generates all binary combinations of length n.
    """
    x = [0] * n
    result = []
    def comb(i):
        if i == n:
            result.append("".join(map(str, x)))
            return
        x[i] = 0
        comb(i + 1)
        x[i] = 1
        comb(i + 1)
    comb(0)
    return result

# ----------------------------------------------------------------------------------------------------
# Original Filename: task2.py
#
# Explanation:
# This script calculates the number of binary combinations of length 'n' that have exactly 'k' ones.
# It uses a recursive approach to count the valid combinations.
# ----------------------------------------------------------------------------------------------------

def count_k_ones_combinations(n, k):
    """
    Counts the number of binary combinations of length n with exactly k ones.
    """
    x = [0] * n
    def comb(i):
        if i == n:
            return 1 if sum(x) == k else 0
        x[i] = 0
        count_from_zero = comb(i + 1)
        x[i] = 1
        count_from_one = comb(i + 1)
        return count_from_zero + count_from_one
    return comb(0)

# ====================================================================================================
# Week 03: Dynamic Programming - Minimum Coin Change and Cut Rod
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1v1.py (MinChange - Recursive)
#
# Explanation:
# This script solves the minimum coin change problem using a pure recursive approach. It finds the
# minimum number of coins required to make a certain amount 'n' given a set of coin denominations 'C'.
# This version is inefficient due to re-computation of the same subproblems.
# ----------------------------------------------------------------------------------------------------

def min_change_recursive(n, C):
    """
    Solves the minimum coin change problem using recursion.
    """
    if n == 0:
        return 0
    v = float('inf')
    for c in C:
        if c <= n:
            v = min(min_change_recursive(n - c, C) + 1, v)
    return v

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1v2.py (MinChange - Memoization)
#
# Explanation:
# This is an optimized version of the minimum coin change problem that uses memoization (top-down
# dynamic programming) to store the results of subproblems and avoid re-computation. This
# significantly improves performance.
# ----------------------------------------------------------------------------------------------------

def min_change_memoization(n, C, memo=None):
    """
    Solves the minimum coin change problem using memoization.
    """
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    v = float('inf')
    for c in C:
        if c <= n:
            v = min(min_change_memoization(n - c, C, memo) + 1, v)
    memo[n] = v
    return v

# ----------------------------------------------------------------------------------------------------
# Original Filename: task2v1.py (CutRod - Recursive)
#
# Explanation:
# This script solves the cut rod problem using a pure recursive approach. Given a rod of length 'n'
# and a list of prices for different lengths, it finds the maximum revenue that can be obtained by
# cutting the rod and selling the pieces. This version is inefficient.
# ----------------------------------------------------------------------------------------------------

def cut_rod_recursive(n, p):
    """
    Solves the cut rod problem using recursion.
    """
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        q = max(p[i] + cut_rod_recursive(n - i, p), q)
    return q

# ----------------------------------------------------------------------------------------------------
# Original Filename: task2v2.py (CutRod - Memoization)
#
# Explanation:
# This is an optimized version of the cut rod problem that uses memoization to store the results of
# subproblems. This avoids redundant calculations and improves the efficiency of the solution.
# ----------------------------------------------------------------------------------------------------

def cut_rod_memoization(n, p, mem=None):
    """
    Solves the cut rod problem using memoization.
    """
    if mem is None:
        mem = {}
    if n == 0:
        return 0
    if n in mem:
        return mem[n]
    q = 0
    for i in range(1, n + 1):
        q = max(p[i] + cut_rod_memoization(n - i, p, mem), q)
    mem[n] = q
    return q

# ====================================================================================================
# Week 04: Knapsack Problem
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1v1.py (Knapsack - Brute Force 1-State)
#
# Explanation:
# This script solves the 0/1 knapsack problem using a brute-force recursive approach. It generates
# all possible combinations of items and finds the combination with the maximum value that fits
# within the knapsack's capacity. This version has a single state in the recursion (the current item index).
# ----------------------------------------------------------------------------------------------------

def knapsack_brute_force_1_state(N, M, w, v):
    """
    Solves the 0/1 knapsack problem using a 1-state brute-force recursion.
    """
    x = [0] * N
    def comb(i):
        if i == N:
            sw, sv = 0, 0
            for j in range(N):
                if x[j] == 1:
                    sw += w[j]
                    sv += v[j]
            return sv if sw <= M else -1
        else:
            x[i] = 0
            a = comb(i + 1)
            x[i] = 1
            b = comb(i + 1)
            return max(a, b)
    return comb(0)

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1v2.py (Knapsack - Brute Force 2-State)
#
# Explanation:
# This is another brute-force recursive solution to the 0/1 knapsack problem. It uses a two-state
# recursion (current item index and remaining capacity), which is a more common way to formulate
# the recursive solution.
# ----------------------------------------------------------------------------------------------------

def knapsack_brute_force_2_state(N, M, w, v):
    """
    Solves the 0/1 knapsack problem using a 2-state brute-force recursion.
    """
    def maxVal(i, C):
        if i == N:
            return 0
        else:
            skip = maxVal(i + 1, C)
            take = -1
            if w[i] <= C:
                take = v[i] + maxVal(i + 1, C - w[i])
            return max(skip, take)
    return maxVal(0, M)

# ----------------------------------------------------------------------------------------------------
# Original Filename: task1v3.py (Knapsack - Memoization)
#
# Explanation:
# This script solves the 0/1 knapsack problem using memoization (top-down dynamic programming).
# It stores the results of subproblems in a dictionary to avoid re-computation, which significantly
# improves performance compared to the brute-force approaches.
# ----------------------------------------------------------------------------------------------------

def knapsack_memoization(N, M, w, v):
    """
    Solves the 0/1 knapsack problem using memoization.
    """
    memo = {}
    def maxVal(i, C):
        if (i, C) in memo:
            return memo[(i, C)]
        if i == N:
            return 0
        else:
            skip = maxVal(i + 1, C)
            take = -1
            if w[i] <= C:
                take = v[i] + maxVal(i + 1, C - w[i])
            result = max(skip, take)
            memo[(i, C)] = result
            return result
    return maxVal(0, M)

# ----------------------------------------------------------------------------------------------------
# Original Filename: task2.py (Knapsack - 2D DP Table)
#
# Explanation:
# This script also solves the 0/1 knapsack problem using a 2D memoization table (a list of lists).
# It's another way to implement top-down dynamic programming for this problem.
# ----------------------------------------------------------------------------------------------------

def knapsack_2d_dp(N, M, w, v):
    """
    Solves the 0/1 knapsack problem using a 2D DP table for memoization.
    """
    mem = [[None] * (M + 1) for _ in range(N + 1)]
    def maxValByMem(i, C):
        if mem[i][C] is not None:
            return mem[i][C]
        if i == N:
            return 0
        else:
            skip = maxValByMem(i + 1, C)
            if w[i] <= C:
                take = v[i] + maxValByMem(i + 1, C - w[i])
                result = max(skip, take)
            else:
                result = skip
            mem[i][C] = result
            return result
    return maxValByMem(0, M)

# ====================================================================================================
# Week 05: Edit Distance and CPU Scheduling
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: edistantv1.py (Edit Distance - Recursive)
#
# Explanation:
# This script calculates the edit distance (Levenshtein distance) between two strings using a pure
# recursive approach. The edit distance is the minimum number of single-character edits (insertions,
# deletions, or substitutions) required to change one string into the other. This version is
# inefficient due to overlapping subproblems.
# ----------------------------------------------------------------------------------------------------

def edit_distance_recursive(a, b):
    """
    Calculates the edit distance between two strings using recursion.
    """
    if not a:
        return len(b)
    if not b:
        return len(a)
    if a[0] == b[0]:
        return edit_distance_recursive(a[1:], b[1:])
    insert_cost = 1 + edit_distance_recursive(a, b[1:])
    delete_cost = 1 + edit_distance_recursive(a[1:], b)
    substitute_cost = 1 + edit_distance_recursive(a[1:], b[1:])
    return min(insert_cost, delete_cost, substitute_cost)

# ----------------------------------------------------------------------------------------------------
# Original Filename: edistantv2.py (Edit Distance - DP)
#
# Explanation:
# This script calculates the edit distance between two strings using dynamic programming (bottom-up
# approach). It builds a 2D table to store the edit distances between all prefixes of the two
# strings, which is much more efficient than the recursive approach.
# ----------------------------------------------------------------------------------------------------

def edit_distance_dp(a, b):
    """
    Calculates the edit distance between two strings using dynamic programming.
    """
    len_a, len_b = len(a), len(b)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for i in range(len_a + 1):
        dp[i][0] = i
    for j in range(len_b + 1):
        dp[0][j] = j
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
    return dp[len_a][len_b]

# ----------------------------------------------------------------------------------------------------
# Original Filename: mincoinchange.py (DP)
#
# Explanation:
# This script solves the minimum coin change problem using a bottom-up dynamic programming approach.
# It builds a 1D DP table to store the minimum number of coins for each amount from 0 to the target
# amount.
# ----------------------------------------------------------------------------------------------------

def min_coin_change_dp(coins, amount):
    """
    Solves the minimum coin change problem using bottom-up dynamic programming.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# ----------------------------------------------------------------------------------------------------
# Original Filename: code.py (CPU Scheduling)
#
# Explanation:
# This script simulates two CPU scheduling algorithms: First-Come, First-Served (FCFS) and Round
# Robin. It takes the number of processes, their burst times, and priorities as input and calculates
# the average waiting time for each algorithm.
# ----------------------------------------------------------------------------------------------------

from collections import deque

def fcfs_scheduling(processes):
    """
    Simulates First-Come, First-Served (FCFS) CPU scheduling.
    """
    time = 0
    total_waiting = 0
    print("\n===== FCFS Scheduling =====")
    print("Process | Burst | Priority | Waiting (ms)")
    print("-" * 50)
    for pid, burst, priority in processes:
        waiting = time
        total_waiting += waiting
        time += burst
        print(f"{pid:^7} | {burst:^5} | {priority:^8} | {waiting:^12}")
    avg_waiting = total_waiting / len(processes)
    print("\nAverage Waiting Time =", avg_waiting, "ms")

def round_robin_scheduling(processes, quantum):
    """
    Simulates Round Robin CPU scheduling.
    """
    remaining = {p[0]: p[1] for p in processes}
    queue = deque([p[0] for p in processes])
    completed = {}
    time = 0
    while queue:
        pid = queue.popleft()
        exec_time = min(quantum, remaining[pid])
        time += exec_time
        remaining[pid] -= exec_time
        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completed[pid] = time
    print("\n===== Round Robin Scheduling =====")
    print("Process | Waiting Time (ms)")
    print("-" * 30)
    total_waiting = 0
    for pid, b, _ in processes:
        waiting = completed[pid] - b
        total_waiting += waiting
        print(f"{pid:^7} | {waiting:^15}")
    avg_waiting = total_waiting / len(processes)
    print("\nAverage Waiting Time =", avg_waiting, "ms")

# ====================================================================================================
# Week 06: Longest Common Subsequence and Other DP Problems
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: LCS.py
#
# Explanation:
# This script finds the length of the Longest Common Subsequence (LCS) between two sequences of
# numbers. It uses a bottom-up dynamic programming approach with a 2D table to store the lengths
# of the LCS for all prefixes of the two sequences.
# ----------------------------------------------------------------------------------------------------

def longest_common_subsequence(A, B):
    """
    Finds the length of the Longest Common Subsequence (LCS) of two sequences.
    """
    N, M = len(A), len(B)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[N][M]

# ----------------------------------------------------------------------------------------------------
# Original Filename: assignment1.py
#
# Explanation:
# This script solves a problem where you are given N colors, each with a vividness and dullness value.
# You need to select a subset of these colors to mix, where the total vividness is the product of
# the vividness of the selected colors, and the total dullness is the sum of their dullness. The goal
# is to find the minimum absolute difference between the total vividness and total dullness. This
# solution uses a brute-force approach, checking all possible subsets of colors.
# ----------------------------------------------------------------------------------------------------

def color_mixing_brute_force(colors):
    """
    Solves the color mixing problem using a brute-force approach.
    """
    N = len(colors)
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
    return min_diff

# ----------------------------------------------------------------------------------------------------
# Original Filename: v2_mm.py (0/1 Knapsack - 1D DP)
#
# Explanation:
# This script solves the 0/1 knapsack problem using a space-optimized, bottom-up dynamic programming
# approach. It uses a 1D DP array to store the maximum value for each capacity, which reduces the
# space complexity from O(N*W) to O(W).
# ----------------------------------------------------------------------------------------------------

def knapsack_1d_dp(N, W, v, w):
    """
    Solves the 0/1 knapsack problem using a space-optimized 1D DP array.
    """
    dp = [0] * (W + 1)
    for i in range(N):
        for c in range(W, w[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - w[i]] + v[i])
    return dp[W]

# ====================================================================================================
# Week 07: Tiling Problem
# ====================================================================================================

# ----------------------------------------------------------------------------------------------------
# Original Filename: m3tileBF_skeleton.py
#
# Explanation:
# This is a skeleton for a brute-force solution to a tiling problem. The goal is to find the number
# of ways to tile a 3xL rectangle with 2x1 dominoes. The state 's' represents the shape of the
# frontier: FLAT (no protruding dominoes), UPPER2 (a domino protrudes from the top two rows), or
# LOWER2 (a domino protrudes from the bottom two rows). The function 'nWays(d, s)' calculates the
# number of ways to tile the rest of the board from column 'd' with a frontier of shape 's'.
#
# Note: The provided code is a skeleton and is not a complete, working solution.
# ----------------------------------------------------------------------------------------------------

def tiling_3xL_skeleton(L):
    """
    A skeleton for a brute-force solution to the 3xL tiling problem.
    This is not a complete solution.
    """
    FLAT = 0
    UPPER2 = 1
    LOWER2 = 2

    def nWays(d, s):
        if d == L:
            # Base case: if we've reached the end and the frontier is flat, we've found one valid tiling.
            return 1 if s == FLAT else 0
        else:
            counter = 0
            if s == FLAT:
                # From a flat frontier, we can place three vertical dominoes or one horizontal one.
                # This part of the logic is incomplete in the original skeleton.
                pass
            else:  # s is either UPPER2 or LOWER2
                # From a non-flat frontier, the choices are more restricted.
                # This part of the logic is also incomplete.
                pass
            return counter

    # The initial call would be nWays(0, FLAT), but the function is incomplete.
    return "Incomplete skeleton"

# You can add main execution blocks here to test the functions, for example:
if __name__ == '__main__':
    print("This file contains a compilation of solutions from Week 1 to 7.")
    # Example usage of one of the functions:
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"\nTesting Kadane's Algorithm (maxsum_v3) on {arr}:")
    print(f"Maximum contiguous subsequence sum: {max_contiguous_subsequence_v3(arr)}")
