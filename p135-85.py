def recmul(a,b):
    if b ==0:
        return 0
    else:
        return a+recmul(a,b-1)

a,b = 5,100
a = recmul(a,b)
print(a)