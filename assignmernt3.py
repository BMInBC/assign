def egg_drop(eggs, floors):
    """
    DP-based egg drop for worst-case min drops.
    Returns min number of trials.
    """
    dp = [[0]*(floors+1) for _ in range(eggs+1)]
    
    for i in range(1, eggs+1):
        for j in range(1, floors+1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = float('inf')
                for x in range(1, j+1):
                    res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                    if res < dp[i][j]:
                        dp[i][j] = res
    return dp[eggs][floors]

drops_needed = egg_drop(7, 102)
print("Minimum drops needed with 7 eggs and 102 floors:", drops_needed)
