bank = ["011001","000000","010100","001000"]
res = []
# for i in range(len(bank)):
#     count = 0
#     for j in bank[i]:
#         if j == "1":
#             count += 1
#     if count > 0:
#         res.append(count)
# print(res)
# if len(res) > 1:
#     tota_beams = 0
#     for j in range(len(res)-1):
#         tota_beams += (res[j] * res[j+1])
#     print( tota_beams)
# else:
#     print(0)


# Optimize
for i in range(len(bank)):
    bank[i] = int(bank[i])