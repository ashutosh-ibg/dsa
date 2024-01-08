nums = [-2,1,-3,4,-1,2,1,-5,4]

# Brute Force Method
# max_n = -100000
# for i in range(len(nums)):
#     s = nums[i]
#     for j in range(i+1, len(nums)):
#         s = s+nums[j]
#         max_n = max(max_n, s)
# print(max_n)

# Optimization
max_values = -100000
max_ending =0
for i in range(len(nums)):
    max_ending = max_ending + nums[i]
    if max_ending > max_values:
        max_values = max_ending
    if max_ending < 0:
        max_ending = 0
print(max_values)
