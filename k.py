
MOD = 10**9 + 7

def ways(nvalues):
    results = []
    max_n = max(nvalues)
    dp = [0] * (max_n+1)
    dp[0] = 1  
    if max_n > 0:
        dp[1] = 0  
    if max_n > 1:
        dp[2] = 2  
    if max_n > 2:
        dp[3] = 3  

    for i in range(4, max_n+1):
        dp[i] = (dp[i-1] + 2 * dp[i-2] + 3 * dp[i-3]) % MOD

    for n in nvalues:
        results.append(dp[n])

    return results


