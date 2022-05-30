S = []
que = []
Q = int(input())
for i in range(Q):
    tmp = input().split()
    que.append(tmp)
for i in range(len(que)):
    if int(que[i][0]) == 1:
        S.append(int(que[i][1]))
    elif int(que[i][0]) == 2:
        num = min(int(que[i][2]),S.count(int(que[i][1])))
        for j in range(num):
            S.remove(int(que[i][1]))
    elif int(que[i][0]) == 3:
        tmp = max(S)-min(S)
        print(tmp)