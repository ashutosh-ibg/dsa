n= 30
k = 30
target=500
k_faces = []
for i in range(1, k+1):
    k_faces.append(i)
res= 0

for i in range(k):
    res = []
    for j in range(n):
        a = k_faces[j:]+k_faces[:j]

for i in range(n):
    res_l = []
    for j in range(k):
        for l in range(j, k+1):
            res_l.append(l)
        res_l += k_faces[:j]

# print(30**30)
# result = 1
# for  i in range(1, 30):
#     result = result * i
# print(result)
