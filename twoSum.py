


def twoSum(numarr,target):
    res = []
    for i in range(0, len(numarr)):
        for k in range(i+1,len(numarr)):
            if numarr[i] + numarr[k] == target:
                res.append(i)
                res.append(k)
                
    return res


nums = [2,7,11,15]
trgt = 9
result = twoSum(nums,trgt)
print(result)    
        