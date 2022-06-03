N = int(input())
answer = 1000000000

# 各数字が何秒の時に出現したか
time = [[] for i in range(10)]

# 各数の出現回数を数える
# count[a][b]=cならa秒目にbがc回表示された
count = [[0]*10 for i in range(10)]

# 入力
for i in range(N):
    S = input()
    for x in range(10):
        Sint = int(S[x])
        # 出現回数をプラス
        count[Sint][x] += 1

        # 表示された秒数を記録
        time[Sint].append(x+(count[Sint][x]-1)*10)

# iをそろえるための秒数
for i in range(10):
    answer = min(answer,max(time[i]))
print(answer)