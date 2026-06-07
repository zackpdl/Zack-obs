# Puran Paodensakul
# 6611140
# 541
import sys

sys.setrecursionlimit(10000)

x = []
n = 0
k = 0 

def comb(i):
    if i == n:
        count_ones = sum(x)
        if count_ones == k:
          
            return 1
        else:
            return 0

    x[i] = 0
    count_from_zero = comb(i + 1)

    x[i] = 1
    count_from_one = comb(i + 1)

    return count_from_zero + count_from_one

if __name__ == "__main__":
    n = int(input("Enter n: "))
    k = int(input("Enter k: ")) 
    x = [0] * n
    
    total_combinations = comb(0)
    print(f"Total combinations with {k} ones: {total_combinations}")