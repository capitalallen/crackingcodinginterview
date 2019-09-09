def SieveOfEratosthenes(n):
    """
    a list with length of n and all equal to True
    p: 2
    while p *p <=n if prime[p] == True it's a prime
    """
    prime = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*2,n+1,p):
                prime[i] = False
        p +=1
    prime[0] = False
    prime[1] = False
    for p in range(n+1):
        if prime[p]:
            print(p)
SieveOfEratosthenes(1000)