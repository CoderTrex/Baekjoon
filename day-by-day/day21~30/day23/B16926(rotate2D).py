N, M, rotate = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
original_matrix = [[0 for i in range(M)] for j in range(N)]
visited = [[False for i in range(M)] for j in range(N)]

for i in range(N):
    original_matrix[i] = matrix[i].copy()

def move_down(original_matrix, matrix, y, x):
    matrix[y+1][x] = original_matrix[y][x]

def move_right(original_matrix, matrix, y, x):
    matrix[y][x+1] = original_matrix[y][x]

def move_left(original_matrix, matrix, y, x):
    matrix[y][x-1] = original_matrix[y][x]

def move_up(original_matrix, matrix, y, x):
    matrix[y-1][x] = original_matrix[y][x]



def printer(matrix):
    for i in range(N):
        print(" ".join(map(str, matrix[i])))

start = (0, 0)

while rotate > 0:
    while True:
        # 아래로 이동
        while True:
            if (start[0] + 1 < N) and not visited[start[0] + 1][start[1]]:
                move_down(original_matrix, matrix, start[0], start[1])
                visited[start[0]][start[1]] = True
                start = (start[0] + 1, start[1])
            else:
                break
        # 오른쪽으로 이동
        while True:
            if (start[1] + 1 < M) and not visited[start[0]][start[1] + 1]:
                move_right(original_matrix, matrix, start[0], start[1])
                visited[start[0]][start[1]] = True
                start = (start[0], start[1] + 1)
            else:
                break
        # 위로 이동
        while True:
            if (start[0] - 1 >= 0) and not visited[start[0] - 1][start[1]]:
                move_up(original_matrix, matrix, start[0], start[1])
                visited[start[0]][start[1]] = True
                start = (start[0] - 1, start[1])
            else:
                break
        # 왼쪽으로 이동
        while True:
            if (start[0] == start[1] -1):
                move_left(original_matrix, matrix, start[0], start[1])
                visited[start[0]][start[1]] = True
                start = (start[0], start[1] - 1)

            if (start[1] - 1 >= 0) and not visited[start[0]][start[1] - 1]:
                move_left(original_matrix, matrix, start[0], start[1])
                visited[start[0]][start[1]] = True
                start = (start[0], start[1] - 1)
            else:
                break
        start = (start[0] + 1, start[1] + 1)
        if (visited[start[0]][start[1]]):
            break
    rotate -= 1
    start = (0, 0)
    visited = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        original_matrix[i] = matrix[i].copy()
printer(matrix)
