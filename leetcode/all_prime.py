n = 50
n_dp = [True]*(n+1)
n_dp[0] = False
n_dp[1] = False
sum = 0
for i in range(2,n+1):
    if i*i <= n:
        if n_dp[i] == True:
            for j in range(i*2, n+1, i):
                n_dp[j] = False

count = 0
for k in n_dp:
    if k == True:
        count += 1
print(count)