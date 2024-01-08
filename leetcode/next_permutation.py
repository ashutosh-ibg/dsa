import copy
nums = [2,3,1]

# total_combinations = 1
# for i in range(1, len(arr)+1):
#     total_combinations *= i
# print(total_combinations)

# # n = 0
# last_list = arr[:]
# min_num = arr[:]
# for i in range(total_combinations-1):
#     arr[n], arr[n+1] = arr[n+1], arr[n]
#     print(min_num != last_list, min_num, last_list, arr)
#     if min_num != last_list:
#         for j in arr:
#             if j < min_num:
#                 min_num = arr[:]
#                 break
# x = arr[:]
# n = len(arr)-1
# for i in range(total_combinations):
    
#     if arr[n] != arr[n-1] and arr[n]< arr[n-1]:
#         arr[n], arr[n-1] = arr[n-1], arr[n]
#         print(arr)
#         break
#     n -= 1
#     if n <= 0:
#         n = len(arr)-1
#         print(arr, x)
#         if x == arr:
#             arr[n], arr[n-1] = arr[n-1], arr[n]
#         print(arr)
#         break
l = len(nums)-2
r = len(nums)-1
x_l = len(nums)-1
x_r = len(nums)-1

count = 1

for j in range(len(nums)):
    if nums[x_r] < nums[x_l]:
        count += 1
    x_l -= 1

if count == len(nums):
    x_last_index = 0
    for j in range(x_l, len(nums)//2 ):
        nums[-x_last_index], nums[j] = nums[j], nums[-x_last_index]
        x = 0
        l = 0
if l > 0 or count != len(nums):
    for i in range(len(nums)):
        if l < 0 or count == len(nums):
            break
        if nums[r] > nums[l]:
            print(nums[r] > nums[l])
            break
        l -= 1 
        r -= 1

    for j in range(len(nums)-1,0, -1):
        if nums[j] > nums[l]:
            nums[j] , nums[l] = nums[l], nums[j]
            break

    last_index = 1
    for j in range(l, (len(nums[l+1:])//2)):
        print(l+1, nums[j], nums[-last_index])
        nums[-last_index], nums[j+1] = nums[j+1], nums[-last_index]
        last_index += 1
print(nums)
# print(min_num, "sssss")
# [2,3,1]
#[1,3,2]--> [1,3,2] ---> []
# 12345