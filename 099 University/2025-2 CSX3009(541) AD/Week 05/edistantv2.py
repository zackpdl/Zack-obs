# Puran Paodensakul
# 6611140
# 541

def edistantv2(a, b):

    len_a, len_b = len(a), len(b)
    
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for i in range(len_a + 1):
        dp[i][0] = i
    for j in range(len_b + 1):
        dp[0][j] = j
        
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1,        
                           dp[i][j-1] + 1,        
                           dp[i-1][j-1] + cost)   
                           
    return dp[len_a][len_b]

if __name__ == '__main__':
    string_a = input()
    string_b = input()
    print(edistantv2(string_a, string_b))
