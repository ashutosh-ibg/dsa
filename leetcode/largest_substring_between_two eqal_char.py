def maxLengthBetweenEqualCharacters(s):
    if s[0] == s[-1]:
        return len(s)-2

    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            # s_dict[s[i]][0] += 1
            s_dict[s[i]].append(i)
        else:
            s_dict[s[i]] = [i]
    print(s_dict)
    max_len = 0
    for i in s_dict:
        sub = s_dict[i][-1] - s_dict[i][0]
        max_len = max(max_len,sub)
    return max_len-1

s = "mgntdygtxrvxjnwksqhxuxtrv"
ans = maxLengthBetweenEqualCharacters(s)
print(ans)







{'m': [0], 'g': [1, 6], 'n': [2, 13], 't': [3, 7, 22], 'd': [4], 'y': [5], 'x': [8, 11, 19, 21], 'r': [9, 23], 'v': [10, 24], 'j': [12], 'w': [14], 'k': [15], 's': [16], 'q': [17], 'h': [18], 'u': [20]}











