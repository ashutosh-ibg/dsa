nums = [1,3,5,7,9]
count = 0 
for i in range(len(nums)):
    if nums[i]%2  == 0:
        count += 1
    
if count >=2 :
    print( True)
else:
    print( False)
