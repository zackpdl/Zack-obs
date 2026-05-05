# Puran Paodensakul
# 6611140
# 541

def mincoinchange(coins, amount):

    dp = [float('inf')] * (amount + 1)
    
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins_input = list(map(int, input().split()))
    amount_input = int(input())
    
    result = mincoinchange(coins_input, amount_input)
    print(result)
