from collections import defaultdict


nums = [2,4,6,8,10]
# nums.sort()

# def recursion(nums, i, count):
#     if len(nums[i:]) < 3:
#         return 0
#     first_number = nums[i]
#     second_number = nums[i+1]
#     third_number = nums[i+2]
#     print(first_number , second_number , third_number)
#     if second_number - first_number  == third_number - second_number:
#         count += 1

#     sequence = count + recursion(nums, i+1, count)
#     return result

# count = 0
# result = recursion(nums, 0, count)
# print(result)

total_count = 0
n = len(nums)
dp = [defaultdict(int) for _ in range(n)]
print(dp)
print(dp[0][2],"================================")

# for i in range(1, n):
#     for j in range(i):
#         diff = nums[i] - nums[j]
#         print(diff, i, j)
#         dp[i][diff] += 1
#         if diff in dp[j]:
#             dp[i][diff] += dp[j][diff]
#             total_count += dp[j][diff]
# print(total_count)
