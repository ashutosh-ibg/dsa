c = [1,2,3]
k = [1,1]

c.sort()
k.sort()
i = 0
for j in range(0, len(k)):
    if i < len(c):
        if c[i] <= k[j]:
            i += 1
print(i)