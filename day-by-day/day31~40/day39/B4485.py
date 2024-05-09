from collections import deque

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 9999999:
                print("INF", end=" ")
            else:
                print("{:3}".format(matrix[i][j]), end=" ")
        print()

answer = []
while True:
    size = int(input())
    if (size == 0):
        break

    value_matrix = [[9999999] * size for _ in range(size)]
    visted_matrix = [[False] * size for _ in range(size)]
    matrix = []
    for i in range(size):
        matrix.append(list(map(int, input().split())))

    value_matrix[0][0] = matrix[0][0]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = 0
    deq = deque()
    deq.append((0, 0, matrix[0][0]))

    while True:
        while deq:
            t_deq = deque()
            while deq:
                x, y, value = deq.popleft()
                mx = -1
                my = -1
                m_value = 9999999
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= size or ny >= size:
                        continue
                    elif nx == size - 1 and ny == size - 1:
                        value_matrix[nx][ny] = min(value_matrix[nx][ny], matrix[nx][ny] + value)
                        continue
                    elif matrix[nx][ny] < m_value and not visted_matrix[nx][ny]:
                        m_value = matrix[nx][ny]
                        mx = nx
                        my = ny
                if (mx != -1 and my != -1) and (mx != size and my != size):
                    min_target = min(value_matrix[mx][my], value + matrix[mx][my])
                    value_matrix[mx][my] = min_target
                    visted_matrix[mx][my] = True
                    t_deq.append((mx, my, min_target))
            deq = t_deq
        
        
        
        for i in range(size):
            for j in range(size):
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= size or ny >= size:
                        continue
                    elif not visted_matrix[nx][ny] and (nx != size - 1 and ny != size - 1):
                        deq.append((i, j, value_matrix[i][j] + matrix[nx][ny]))
                    elif value_matrix[nx][ny] > value_matrix[i][j] + matrix[nx][ny]:
                        value_matrix[nx][ny] = value_matrix[i][j] + matrix[nx][ny]
                        deq.append((nx, ny, value_matrix[nx][ny]))
        if not deq:
            break

    answer.append(value_matrix[size - 1][size - 1])

for i in range(len(answer)):
    print("Problem {}: {}".format(i + 1, answer[i]))
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 5
# 3 3 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0

