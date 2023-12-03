
MOD = 10**9 + 7

def ways(nvalues):
    if not isinstance(nvalues, list):
        raise ValueError("nvalues must be a list")
    if not all(isinstance(n, int) for n in nvalues):
        raise ValueError("nvalues must contain only integers")

    results = []
    max_n = max(nvalues)
    dp = [0] * (max_n+1)
    dp[0] = 1  # Base case: 1 way to fill 0-length space
    dp[1] = 0  # Base case: No way to fill 2x2x1 space with 2x1x1 dominoes
    
    for i in range(2, max_n+1):
        dp[i] = (dp[i-1] + 2*dp[i-2]) % MOD
        if i > 2:
            dp[i] = (dp[i] + 4*dp[i-3]) % MOD

    for n in nvalues:
        results.append(dp[n])
    
    return results 


