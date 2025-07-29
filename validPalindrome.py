import string
def isPalindrome(s):
    s=s.lower()
    table = str.maketrans('','',string.punctuation + ' ')
    newS = s.translate(table)
    invertedS = newS[::-1]
    print(invertedS)
    print(newS)
    if newS == invertedS:
        res = True
    else:
        res = False
    
    return res

s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)