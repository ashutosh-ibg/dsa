startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

n = len(startTime)

def getnextIndex (vector, l, target):
    r=n-1
    result= n+1
    while l<=r:
        mid = l + (r-l)//2
        if vector[mid][0] >= target:
            result = mid
            r = mid - 1
        else:
            l = mid+1
    return result


def recur(vector, i, dp):
    if i>=n:
        return 0
    if dp[i] != -1:
        return dp[i]
    
    next = getnextIndex(vector, i+1, vector[i][1])
    taken = vector[i][2] + recur(vector, next, dp)
    not_taken = recur(vector, i+1, dp)
    dp[i] = max(taken,not_taken)
    return dp[i]


vector = []

for i in range(len(startTime)):
    vector.append([startTime[i], endTime[i], profit[i]])
vector.sort()
print(vector)
dp= [-1]*n
abc = recur(vector, 0, dp)
print(abc)