def uniqueOccurrences(arr):
    arr_dict = {}
    for i in arr:
        if i not in arr_dict:
            arr_dict[i] = 1
        else:
            arr_dict[i] = arr_dict[i] + 1
    new_arr = []
    for i in arr_dict:
        if arr_dict[i] not in new_arr:
            new_arr.append(arr_dict[i])
        else:
            return False
    return True
        
arr = [1,2,2,1,1,3]
res = uniqueOccurrences(arr)
print(res)