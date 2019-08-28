def checkUnique(s):
    tmp = set(s)
    if len(tmp) == len(s):
        print(True)
    else:
        print(False)

checkUnique('hb 627jh=j ()')
checkUnique('23ds2')

