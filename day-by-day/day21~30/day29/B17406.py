from copy import deepcopy
N, M, K = map(int, input().split())

o_matrix = [list(map(int, input().split())) for _ in range(N)]
min = 1000000

def rotate_matrix(matrix, start_y, start_x, end_y, end_x):
    temp = matrix[start_y][start_x]
    for i in range(start_y, end_y):
        matrix[i][start_x]  = matrix[i + 1][start_x]
    for i in range(start_x, end_x):
        matrix[end_y][i]    = matrix[end_y][i + 1]
    for i in range(end_y, start_y, -1):
        matrix[i][end_x]    = matrix[i - 1][end_x]
    for i in range(end_x, start_x, -1):
        matrix[start_y][i]  = matrix[start_y][i - 1]
    matrix[start_y][start_x + 1] = temp

def check_min(matrix):
    global min
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += matrix[i][j]
        if sum < min:
            min = sum

list = []
for _ in range(K):
    r, c, s = map(int, input().split())
    list.append([r, c, s])

visited = [False] * K

def dfs(matrix, list, visited, depth):
    if depth != K:
        for i in range(K):
            if visited[i] == False:
                c_matrix = deepcopy(matrix)
                c_visited = deepcopy(visited)
                r, c, s = list[i]
                start_y = r - s - 1
                start_x = c - s - 1
                end_y   = r + s - 1
                end_x   = c + s - 1
                while True:
                    rotate_matrix(c_matrix, start_y, start_x, end_y, end_x)
                    start_x += 1
                    start_y += 1
                    end_x -= 1
                    end_y -= 1
                    if start_y == end_y and start_x == end_x:
                        break
                c_visited[i] = True
                dfs(c_matrix, list, c_visited, depth + 1)
                c_visited[i] = False
    else:
        check_min(matrix)

dfs(o_matrix, list, visited, 0)
print(min)

