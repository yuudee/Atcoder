N,K = map(int,input().split())

like = list(map(int,input().split()))  #それぞれのおいしさが入っている
dislike_index = list(map(int,input().split())) #嫌いな食べ物のインデックス

max_like = max(like)

flag = 0
for i in dislike_index:
    if like[i-1] == max_like:
        flag = 1
    
if flag == 1:
    print('Yes')
else:
    print('No')