a = [-4, -2, 1, -3,2]
k = 2
prefix_max = []
prefix_max.append(a[0])
for i in range(1, len(a)):
    s = a[i] + prefix_max[-1]
    prefix_max.append(s)
print(prefix_max)
for i in range(k, len(prefix_max)):
    