nums = [1,3,4,1,2,3,1]


abc = []
# a_dict = {}
# for i in nums:
#     if i not in a_dict:
#         a_dict[i] = 1
#     else:
#         a_dict[i] = a_dict[i] + 1

# for j in range(len(nums)):
#     new_list = []
#     for k in a_dict:
#         if a_dict[k] >= 1:
#             new_list.append(k)
#             a_dict[k] -= 1
#     if new_list:
#         abc.append(new_list)
# print(abc)


i = 0
x = set()
while len(nums)>0:
    if nums[i] not in x:
        x.add(nums[i])
        del nums[i]
        i -= 1

    i += 1
    if (i == len(nums)):
        abc.append(list(x))
        x = set()
        i = 0
print(abc)