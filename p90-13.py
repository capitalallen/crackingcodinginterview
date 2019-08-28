def urlify(s):
    if len(s) == 0:
        return ""
    s = s.rstrip()
    result = ""
    for i in range(len(s)):
        if s[i] == " ":
            result += "%20"
        else:
            result += s[i]
    return result
def test(data):
    for i in data:
        result = urlify(i)
        print(result)
data=['much ado about nothing      ','Mr John Smith    ']
test(data)
