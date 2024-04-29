height, width = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(height)]

Williamsons_Sap_sucking_Woodpecker = (0, 0)
Cheonggukjang = (0, 0)
Sushi = (0, 0)
MacAndCheese = (0, 0)

for i in range(height):
    for j in range(width):
        if matrix[i][j] == 2:
            Williamson_Sap_sucking_Woodpecker = (i, j)
        if matrix[i][j] == 3:
            Cheonggukjang = (i, j)
        if matrix[i][j] == 4:
            Sushi = (i, j)
        if matrix[i][j] == 5:
            MacAndCheese = (i, j)

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def bfs():
    dq = deque()
    temp = deque()
    step = 0
    dq.append((Williamson_Sap_sucking_Woodpecker, step))
    while dq:
        loc, step = dq.popleft()
        x, y = loc
        # print("=====")
        # print(x, y, step, dq)
        # print_matrix(matrix)
        # print("=====")
        if (x, y) == Cheonggukjang or (x, y) == Sushi or (x, y) == MacAndCheese:
            return step
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and matrix[nx][ny] != 1:
                temp.append(((nx, ny), step + 1))
                matrix[nx][ny] = 1
        if not dq:
            dq = temp
            temp = deque()
    return -1

num = bfs()
if num == -1:
    print("NIE")
else:
    print("TAK")
    print(num)