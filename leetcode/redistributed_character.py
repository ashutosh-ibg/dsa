def makeEqual(words) -> bool:
    if len(words) <= 1:
        return True
    x = {}
    for i in words:
        for j in i:
            if j not in x:
                x[j] = 1
            else:
                x[j] = x[j] + 1
    s = -1
    for i in x:
        if x[i]%len(words) != 0:
            return False
        
words = ["a","b"]
ans = makeEqual(words=words)
print(ans)



        
        
    

    
    
    