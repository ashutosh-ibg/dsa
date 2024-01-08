abc = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n= len(abc)-1
for i in range(len(abc)//2):
    for j in range(len(abc)):
        a = abc[i][j]
        abc[i][j] = abc[n][j]
        abc[n][j] = a
    n -= 1

for i in range(len(abc)):
    for j in range(i, len(abc)):
        a = abc[j][i]
        abc[j][i] = abc[i][j]
        abc[i][j] = a
    #     print(abc[j][i], end=" ")
    # print("--------------------------------")
    # print("")
j = 0
i = 0
# while (j < len(abc)):
#     for 
# j = 0
# for i in range(len(abc)):
#     for j in range(i, len(abc)):
#         a = abc[j][i]
#         abc[j][i] = abc[i][j]
#         abc[i][j] = a
#     j += 1
for i in abc:
    print(i)