right= 1000000
left= 1
list_nums = [True]*(right+1)
list_nums[0] = False
list_nums[1] = False
for i in range(2, len(list_nums)):
    if list_nums[i] == True:
        for j in range(i*i, len(list_nums), i):
            list_nums[j] = False
count = 0
res =[]
for j in range(left, len(list_nums)):
    if list_nums[j] == True:
        res.append(j)
print(res)
if len(res)>=2:
    num1 = res[0]
    num2 = res[1]
    min_len = num2-num1
    for i in range(len(res)-1):
        diff = res[i+1] -  res[i]
        if diff < min_len:
            print(res[i+1], res[i], diff, min_len)
            num1 = res[i]
            num2 = res[i+1]
            min_len = diff
    print([num1, num2])
else:
    print([-1,-1])