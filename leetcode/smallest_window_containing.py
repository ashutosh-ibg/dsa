s = "012"
a = ""
min_length = 100000
for i in s:
    if len(a) >=3:
        if "0" in s and "1" in s and "2" in s:
            min_length = min(min_length, len(a))
        else:
            a = ""
    else:
        print(i)
        a += i
if min_length >=3 and min_length != 1000000:
    print( min_length)
else:
    print(-1)
