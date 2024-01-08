intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
prev_x = intervals[0][0]
prev_y = intervals[0][1]
new_interval = []
for i in range(1, len(intervals)):
    
    if intervals[i][0] <= prev_y:
        if intervals[i][1] >= prev_y:
            prev_y = intervals[i][1]
    else:
        new_interval.append([prev_x, prev_y])
        prev_x = intervals[i][0]
        prev_y = intervals[i][1]

new_interval.append([prev_x, prev_y])
print(new_interval)