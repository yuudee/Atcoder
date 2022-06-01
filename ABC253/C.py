S = []
que = []
Q = int(input())    #クエリ数取得

#各クエリの内容の入力
que = [input().split() for i in range(Q)]

for q in que:
    if int(q[0]) == 1:
        S.append(int(q[1]))
    elif int(q[0]) == 2:
        num = min(int(q[2]),S.count(int(q[1])))
        for j in range(num):
            S.remove(int(q[1]))
    elif int(q[0]) == 3:
        tmp = max(S)-min(S)
        print(tmp)