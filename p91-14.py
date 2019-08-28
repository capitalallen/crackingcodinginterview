"""
Input: string
Output: bool
C: optimize
E: len = 0
"""


def palPerm(s):
    #if even: there must be two of every char
    #if odd: there must be only one unique char
    #use hash table to store letters
    #if we see the same letter again, delete from hash
    #check hash at the end: odd - 1 key left, even no key
    table = {}
    charCount = 0
    for i in range(len(s)):
        tmp = s[i].lower()
        if tmp != " ":
            if tmp in table:
                del table[tmp]
            else:
                table[tmp] = True
            charCount +=1
    if charCount%2 == 0:
        return len(table)%2 == 0
    else:
        return len(table) ==  1
print(palPerm('Tact Coa'))