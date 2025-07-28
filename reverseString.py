def strReverse(s):
    num = len(s)
    res = []
    for i in range(0,num):
        res.append(s[(num-1) - i])
        
    return res

st = ['o','l','a','r','i','a']
stt = ['h','e','l','l','o']
result = strReverse(stt)
print(result)