def permutation(str1,str2):
   # Get lenghts of both strings 
    n1 = len(str1) 
    n2 = len(str2) 
  
    # If length of both strings is not same, 
    # then they cannot be Permutation 
    if (n1 != n2): 
        return False
  
    # Sort both strings 
    a = sorted(str1) 
    str1 = " ".join(a) 
    b = sorted(str2) 
    str2 = " ".join(b) 
  
    # Compare sorted strings 
    for i in range(0, n1, 1): 
        if (str1[i] != str2[i]): 
            return False
  
    return True

def test(data):
    for i in data:
        result = permutation(i[0],i[1])
        print(result)
dataT = (
    ('abcd', 'bacd'),
    ('3563476', '7334566'),
    ('wef34f', 'wffe34'),
    ("a","a")
)
test(dataT)
# permutation("abc","def")
# print(permutation("abc","def"))