s = "gctcxyuluxjuxnsvmomavutrrfb"
t = "qijrjrhqqjxjtprybrzpyfyqtzf"

s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] = s_dict[i] + 1

t_dict = {}
for i in t:
    if i not in t_dict:
        t_dict[i] = 1
    else:
        t_dict[i] = t_dict[i] + 1
print(s_dict)
print(t_dict)
count = 0
for i in  s_dict:
    if i not in t_dict:
        count += s_dict[i]
    elif i in t_dict and s_dict[i] >= t_dict[i]:
        count = count + (s_dict[i] - t_dict[i])
print(count)

