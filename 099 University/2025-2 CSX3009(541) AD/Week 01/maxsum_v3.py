# Puran Paodensakul
# 6611140
# 541

def max_contiguous_subsequence(arr):
  
    max_so_far = 0
    current_max = 0
    for x in arr:
        current_max += x
        if current_max < 0:
            current_max = 0
        if current_max > max_so_far:
            max_so_far = current_max
    return max_so_far

if __name__ == '__main__':
    import sys
    import time

    if len(sys.argv) != 2:
        print("Usage: python maxsum_v3.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        arr = [int(x) for x in f.read().split()]

    start_time = time.perf_counter()
    max_sum = max_contiguous_subsequence(arr)
    end_time = time.perf_counter()

    print(f"Maximum contiguous subsequence sum: {max_sum}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
