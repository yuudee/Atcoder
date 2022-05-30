H,W = map(int,input().split())

HW = []

for i in range(H):
    location = input()
    for j in range(W):
        if location[j] == 'o':
            HW.append([i,j])


y_dis = abs(HW[0][0] - HW[1][0])
x_dis = abs(HW[0][1]- HW[1][1])

answer = y_dis + x_dis

print(answer)