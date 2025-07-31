
def mergeTwoLists(list1, list2):
    final_list = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            final_list.append(list1[0])
            list1.pop(0)
        elif list2[0] <= list1[0]:
            final_list.append(list2[0])
            list2.pop(0)
    if list1 != []:
        for i in range(0,len(list1)):
            final_list.append(list1[i])
    else:
        for j in range(0,len(list2)):
            final_list.append(list2[j])
            
    return final_list


lst1 = [1,2,4] 
lst2 = [1,3,4]

res = mergeTwoLists(lst1,lst2)
print(res)