def remove_duplicate(nums):
    k = len(nums)
    index = 0
    for j in range(1, k):
        if(nums[index]!=nums[j]):
            index += 1   
            nums[index] = nums[j]
        
    return index+1


lst = [1,2,2,3,4,4,4,5]
lst1 = [1,1,2]
res = remove_duplicate(lst)
res1 = remove_duplicate(lst1)
print(res)
print(res1)