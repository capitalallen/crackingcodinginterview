"""
input: stirng
output: string
C: optimize
e: len(s) == 0
time: O[n]
space: constant
"""
def strCompr(s):
    #result: store the output
    #i = 0 
    #while loop through the string
    #init curr = s[i] and count = 1
    #while i+1 <= length-1
    #next = s[i+1]
    #check if curr = next value of the string
    #yes: increment; curr = next; 
    #no: return 
    #append curr and count to result
    length = len(s)
    if length == 0:
        return s
    i = 0
    result = ""
    while i < length:
        curr = s[i]
        count = 1
        while i+1 <= length-1:
            next = s[i+1]
            if curr == next:
                count +=1
                i +=1
            else: 
                i+=1
                break
        else:
            i+=1
        result += curr + str(count)
    return min(result, s, key=len)
s = "aabcccccaaa"
print(strCompr(s)=='a2b1c5a3')
print(strCompr('abcdef')=='abcdef')
