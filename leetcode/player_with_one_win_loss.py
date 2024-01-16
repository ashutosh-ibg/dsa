def findWinners(matches):
    win = []
    loss = {}
    final_win= []
    final_loss =[]
    for i in range(len(matches)):
        win_i = matches[i][0]
        win.append(win_i)
        loss_i = matches[i][1]
        if loss_i in loss:
            loss[loss_i] = loss[loss_i] + 1
        else:
            loss[loss_i] = 1

    for j in set(win):
        if j not in loss.keys():
            final_win.append(j)
    print(win, loss.keys())
    print(final_win)
    for k in loss:
        if loss[k] == 1:
            final_loss.append(k)
    final_win.sort()
    final_loss.sort()
    return [final_win, final_loss]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
res = findWinners(matches)
print(res)