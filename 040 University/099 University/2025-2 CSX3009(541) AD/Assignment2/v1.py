# Puran Paodensakul
# 6611140
# 541

def solve_brute_force(cost: list[int]) -> int:
    n = len(cost)

    def climb(i: int) -> int:
        if i == 0:
            return cost[0]
        if i == 1:
            return cost[1]
        return cost[i] + min(climb(i - 1), climb(i - 2))

    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    return min(climb(n - 1), climb(n - 2))


