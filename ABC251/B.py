N,W = map(int,input().split())

weight = list(map(int,input().split()))
ans_set = set()
# おもりが１つの時
for i in range(N):
    if weight[i] <= W:
        ans_set.add(weight[i])

# おもりが２つの時
for i in range(N):
    for j in range(i+1,N):
        if weight[i] + weight[j] <= W:
            ans_set.add(weight[i] + weight[j])

# おもりが３つの時
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if weight[i] + weight[j] + weight[k] <= W:
                ans_set.add(weight[i] + weight[j] + weight[k])

print(len(ans_set))