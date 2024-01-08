nums = [2,3,3,2,2,4,2,3,4]

nums_dict = {}
for i in nums:
    if i not in nums_dict:
        nums_dict[i] = 1
    else:
        nums_dict[i] = nums_dict[i] + 1


delete_num= 0
print(nums_dict)
for i in nums_dict:
    if nums_dict[i] == 1:
        print(-1)
    if nums_dict[i]%3 == 0:
        delete_num += nums_dict[i]//3
    elif nums_dict[i]%3 == 1:
        delete_num += nums_dict[i]//3 -1
        delete_num += 2
    else:
        delete_num += 1
        delete_num += nums_dict[i]//3
print(delete_num)

