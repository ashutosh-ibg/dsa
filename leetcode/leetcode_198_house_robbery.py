def rob(nums):
    # addition = 0
    # for i in range(0, len(nums),2):
    #     addition += nums[i]
    # addition2 = 0
    # for i in range(1, len(nums),2):
    #     addition2 += nums[i]
    # print(addition, addition2)
    
    
    p = [0]*(len(nums)+1)
    p[1]= nums[0]
    for i in range(1, len(nums)):
        p[i+1] = max((p[i-1]+nums[i]), p[i])
    return p[len(nums)]


nums = [2,1,1,2]
[1,2,2,1]
# [1,2,3,4,5,6,7,8,9,10,11,12,13,14]



abc =  rob(nums)
print(abc)