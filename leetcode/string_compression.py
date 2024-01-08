# s = "bababbaba"
# k = 1
# abc = {}

# for i in s:
#     if i not in abc:
#         abc[i] = 1
#     else:
#         abc[i] = abc[i] + 1

# abc_keys = []

# for i in abc.keys():
#     abc_keys.append(i)

# k_list = []

# for j in abc_keys:
#     k_list.append([abc[j], j])
# k_list.sort()
# d = 0
# for i in k_list: 
#     if i[0] <= 9:
#         d += 1
# k_2_list = k_list[d:]
# k_list = k_list[:d]

# l = 1
# m_2 = 0
# print(k_2_list)
# while (l <= len(k_2_list) and len(k_2_list)>0):
#     if k_2_list[m_2][0] > 9:
#         k_2_list[m_2][0] = k_2_list[m_2][0] - 1
#         l = l + 1
#         m_2 = m_2 + 1

# m = 0
# while (l <= k):
#     if k_list[m][0] > 0:
#         k_list[m][0] = k_list[m][0] - 1
#         l = l + 1
#     if k_list[m][0] == 0:
#         m += 1
#     # if l == k:
        
# # for i in k_list[m:]:
# #     if i[0] > 1:
# #         new_s += str(i[0])
# # new_s = new_s + i[1]

# new_s = ""
# print(k_list+k_2_list)

# for i in k_list+k_2_list:
#     if i[0] > 1:
#         new_s += str(i[0])
#         new_s = new_s + str(i[1])
#     elif i[0] == 1:
#         new_s = new_s + str(i[1])

# print(len(new_s))
# for i in range(k):
    
# for i in abc:
#     for j in range(k):
#         if abc[k_list[j]] > abc[i]:
#             # abc[k_list[j]] = abc[i]
#             k_list[j] = i
#             break
# print(abc)
# print(k_list)


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[101] * (k + 1) for _ in range(n)]

        def dfs(i, k):
            nonlocal s, n, dp
            if i + k >= n:
                return 0
            if k < 0:
                return 101
            if dp[i][k] != 101:
                return dp[i][k]

            res = dfs(i + 1, k - 1) # Skip this character
            diff, same, length = 0, 0, 0

            # For all continuous s[i] characters (can skip k characters)
            for j in range(i, n):
                if k - diff < 0:
                    break
                if s[i] == s[j]:
                    same += 1
                    if same <= 2 or same == 10 or same == 100:
                        length += 1
                else:
                    diff += 1
                res = min(res, length + dfs(j + 1, k - diff))

            dp[i][k] = res
            return res

        return dfs(0, k)