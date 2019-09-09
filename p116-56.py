def conversion(n1,n2):
    count = 0
    c = n1 ^ n2
    while c !=0:
        c = c& (c-1)
        count +=1
    print(count)


n1 = 29
n2 = 15
conversion(n1,n2)