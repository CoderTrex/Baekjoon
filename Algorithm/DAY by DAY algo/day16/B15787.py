# 0 1 1 0 0
# 0 1 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

N, M = map(int, input().split())
train = [[0] * 20 for _ in range(N)]

for _ in range(M):
    st = list(map(int, input().split()))
    if (st[0] == 1):
        train[st[1]-1][st[2]-1] = 1
    elif (st[0] == 2):
        train[st[1]-1][st[2]-1] = 0
    elif (st[0] == 3):
        for i in range(19, 0, -1):
            train[st[1]-1][i] = train[st[1]-1][i-1]
        train[st[1]-1][0] = 0
    elif (st[0] == 4):
        for i in range(19):
            train[st[1]-1][i] = train[st[1]-1][i+1]
        train[st[1]-1][19] = 0

# print(train)

list = []
cnt = 0
for i in range(N):
    if (train[i] not in list):
        cnt+=1
        list.append(train[i])

print(cnt)