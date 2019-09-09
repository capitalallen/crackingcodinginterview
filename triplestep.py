def countWays(n):
    memo = [-1 for i in range(n+1)]
    return triplestep(n,memo)
def triplestep(n,memo):
    if n <0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] >-1:
        return memo[n]
    else:
        memo[n] = triplestep(n-1,memo) + triplestep(n-2,memo) + triplestep(n-3,memo)
        return memo[n]
a = countWays(100)
print(a)