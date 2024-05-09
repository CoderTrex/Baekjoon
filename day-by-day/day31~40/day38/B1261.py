from collections import deque

width, height = map(int, input().split())
matrix = []
for _ in range(height):
    matrix.append(list(map(int, input())))
matrix_visted = [[-1] * width for _ in range(height)]
start = (0, 0)
target = (width-1, height-1)

if width == 1 and height == 1:
    if matrix[0][0] == 1:
        print(1)
        exit()
    else:
        print(0)
        exit()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start):
    dq = deque()
    dq.append((start, 0))
    matrix_visted[0][0] = 0
    while dq:
        loc, cnt = dq.popleft()
        y, x = loc
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < width and 0 <= ny < height:
                if matrix[ny][nx] == 1:
                    if matrix_visted[ny][nx] > cnt + 1 or matrix_visted[ny][nx] == -1:
                        matrix_visted[ny][nx] = cnt + 1
                        dq.append(((ny, nx), cnt + 1))
                else:
                    if matrix_visted[ny][nx] > cnt or matrix_visted[ny][nx] == -1:
                        matrix_visted[ny][nx] = cnt
                        dq.append(((ny, nx), cnt))

bfs(start)
print(matrix_visted[height-1][width-1])