numRows = 5
array = [[]]*numRows

for i in range(1, numRows+1):
    array[i-1] = [1]*i

for i in range(1, len(array)-1):
    new_list = []
    for j in range(i):
        # print(array[i][:j+2], i, j,  array[i], sum(array[i][:j+2]))
        # print(array[i][j:j+1])
        add = sum(array[i][j:j+2])
        new_list.append(add)
    array[i+1] = [1]+new_list+[1]
    # print(new_list)

print(array)