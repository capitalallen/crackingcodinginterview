"""
input: two string
output: bool
c: optimize
e: two s == 0
"""
def oneAway(s1,s2):
    # l: find the longest string 
    # loop through the shorter string
    # delete duplicate char
    # if one char left and length of s1 != s2 return true
    # if no char left and lenght of s1 == s2 return false
    l1 = len(s1)
    l2 = len(s2)
    table = ""
    tmp = ""
    if l1 < l2:
        table = list(s2)
        tmp = list(s1)
    elif l1 > l2:
        table = list(s1)
        tmp = list(s2)
    else:
        table = list(s1)
        tmp = list(s2)
    for i in range(len(tmp)):
        if tmp[i] in table:
            t = table.index(tmp[i])
            del table[t]
    if len(table) == 0 and l1 == l2:
        return True
    elif len(table) == 1 and abs(l1-l2) == 1:
        return True
    else: 
        return False
def test(data):
    for i in range(len(data)):
        result = oneAway(data[i][0],data[i][1])
        if result == data[i][2]:
            print(True)
data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]
test(data)
            