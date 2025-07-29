def strReverse(s):
    """num = len(s)       solução 1 antes do valid palindrome
    res = []
    for i in range(0,num):
        res.append(s[(num-1) - i])
        
    return res"""
    s[:] = s[::-1]
    return s #in place

st = ['o','l','a','r','i','a']
stt = ['h','e','l','l','o']
result = strReverse(stt)
print(result)