# Puran Paodensakul
# 6611140
# 541

def max_contiguous_subsequence(arr):

    max_so_far = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += arr[k]
            if current_sum > max_so_far:
                max_so_far = current_sum
    return max_so_far

if __name__ == '__main__':
    import sys
    import time

    if len(sys.argv) != 2:
        print("Usage: python maxsum_v1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        arr = [int(x) for x in f.read().split()]

    start_time = time.perf_counter()
    max_sum = max_contiguous_subsequence(arr)
    end_time = time.perf_counter()

    print(f"Maximum contiguous subsequence sum: {max_sum}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")