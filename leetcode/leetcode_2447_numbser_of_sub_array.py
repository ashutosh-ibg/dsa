def subarrayGCD(nums, k):
    def gcd(remainder, devidend):
        if remainder == 0 :
            return devidend
        return gcd(devidend % remainder, remainder)
    count = 0
    for i in range(len(nums)):
        ans = 0
        for j in range(i, len(nums)):
            ans = gcd(ans, nums[j])
            if ans < k:
                break
            if ans == k:
                count += 1
    return count
nums = [9,3,1,2,6,3]
k =3
xyz = subarrayGCD(nums, k)
print(xyz)
