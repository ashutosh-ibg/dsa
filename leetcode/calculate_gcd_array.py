
def gcd(remainder, dividend):
    if remainder ==0 :
        return dividend
    return gcd((dividend%remainder), remainder)
def array_gcd(abc):
    if len(abc) == 0:
        return 0
    ans = abs(abc[0])
    for i in range(1,len(abc)):
        ans = gcd(ans, abs(abc[i]))
    return ans

abc = [10,20,40,50]
xyz= array_gcd(abc)
print(xyz)