from collections import deque
N, K = map(int, input().split())

matrix = [[0] * (N) for _ in range(N)]
data = []

for i in range(N):
    matrix[i] = list(map(int, input().split()))
    for j in range(N):
        if matrix[i][j] != 0:
            data.append([matrix[i][j], i, j])
time, x, y = map(int, input().split())

data.sort()
dq = deque()
for value, i, j in data:
    dq.append([value, i, j])

for t in range(time):
    tmp_dq = deque()
    while dq:
        value, i, j = dq.popleft()
        if i > 0 and (matrix[i-1][j] == 0):
            matrix[i-1][j] = value
            tmp_dq.append([value, i-1, j])
        if i < N-1 and (matrix[i+1][j] == 0):
            matrix[i+1][j] = value
            tmp_dq.append([value, i+1, j])
        if j > 0 and (matrix[i][j-1] == 0):
            matrix[i][j-1] = value
            tmp_dq.append([value, i, j-1])
        if j < N-1 and (matrix[i][j+1] == 0):
            matrix[i][j+1] = value
            tmp_dq.append([value, i, j+1])
    dq = tmp_dq

print(matrix[x-1][y-1])