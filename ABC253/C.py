#defalutdictでそれぞれの数がSに入っている数を管理する
#heapで最大値、最小値を高速で取り出す

from collections import defaultdict
import heapq

#　クエリ数の受け取り
Q = int(input())

count = defaultdict(int)
maxque = []
minque = []

for i in range(Q):
    # 入力の受け取り
    query = list(map(int,input().split()))

    if query[0] == 1:
        x = query[1]
        count[x] += 1

        heapq.heappush(minque,x)
        heapq.heappush(maxque,-x)
    elif query[0] == 2:
        count[query[1]] -= min(query[2],count[query[1]])
    else:
        # 最小値取り出し
        smin = heapq.heappop(minque)
        # 最小値がクエリ2によってすでに全部削除されて0個になっているかもしれない
        while count[smin] == 0:
            smin = heapq.heappop(minque)

        # 最大値取り出し
        smax = heapq.heappop(maxque)
        smax *= -1
        # 最大値がクエリ2によってすでに全部削除されて0個になっているかもしれない
        while count[smax] == 0:
            smax = heapq.heappop(maxque)
            smax *= -1
        
        print(smax - smin)

        # 次のクエリのために最小値、最大値を戻す
        heapq.heappush(minque,smin)
        heapq.heappush(maxque,-smax)