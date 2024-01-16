def gcd(remainder, devidend):
    if remainder == 0 :
        return devidend
    return gcd(devidend % remainder, remainder)


xyz = gcd(34, 24)
print(xyz)


########################################################################
# Time Complexity Functions
######. O log2 (N)
# N= max(a, b)
## max(remainder, devidend)