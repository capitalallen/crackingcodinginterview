def  getNext(n):
    """
    find rightmost non-trailing 0
    clear bits to the right of p
    add in c1-1 1s
    """
    c = n
    c0,c1 = 0,0
    #while next bit is 0 increment c0
    while c&1 == 0 and c !=0:
        c0 +=1
        c>>=1
    while c&1 == 1 and c!=0:
        c1 +=1
        c>>=1
    p = c1 + c0
    if p ==31 or p ==0:
        return -1
    n |= 1<<p
    n &= ~((1<<p)-1)
    n |= (1<<(c1-1))-1
    return n
def getPrev(n):
    c = n
    c0,c1 = 0,0
    while c&1 == 1:
        c1 +=1
        c>>=1
    while c&1 == 0 and c !=0:
        c0 += 1
        c>>=1
    p = c0 + c1
    n &= ((~0)<<(p+1))
    mask = (1<<(c1+1))-1
    n |= mask << (c0-1)
    return n

getNext(13948)
getPrev(13948)