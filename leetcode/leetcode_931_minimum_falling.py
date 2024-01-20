def minimum_failling(row, col, matrix, i):
    if row <= len(matrix[0][0]):
        return 0
    if col <= len(matrix[0][1]):
        return 0
    
    left = minimum_failling(row[i+1], col[i-1], matrix, i)
    right = minimum_failling(row, col, matrix, i)
    dig = minimum_failling(row, col, matrix, i)






matrix = [[2,1,3], [6,5,4], [7,8,9]]
