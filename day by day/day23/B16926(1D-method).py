N, M, rotate = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
matrix_list = []

# 2, 2 -> 1개
# 4, 5 -> 2개
# 7, 6 -> 3개
# 이는 결국 N, M 중 작은 값의 절반만큼 회전하는 껍데기가 생긴다는 뜻
rotate_count = int(min(N, M) // 2)

start = (0, 0)
for _ in range(rotate_count):
    list = []
    while True:
        if (start[0] + 1 < N) and not visited[start[0] + 1][start[1]]:
            visited[start[0]][start[1]] = True
            start = (start[0] + 1, start[1])
            list.append(matrix[start[0]][start[1]])
        else:
            break
    while True:
        if (start[1] + 1 < M) and not visited[start[0]][start[1] + 1]:
            visited[start[0]][start[1]] = True
            start = (start[0], start[1] + 1)
            list.append(matrix[start[0]][start[1]])
        else:
            break
    while True:
        if (start[0] - 1 >= 0) and not visited[start[0] - 1][start[1]]:
            visited[start[0]][start[1]] = True
            start = (start[0] - 1, start[1])
            list.append(matrix[start[0]][start[1]])
        else:
            break
    while True:
        if (start[0] == start[1] -1):
            visited[start[0]][start[1]] = True
            start = (start[0], start[1] - 1)
            list.append(matrix[start[0]][start[1]])
        if (start[1] - 1 >= 0) and not visited[start[0]][start[1] - 1]:
            visited[start[0]][start[1]] = True
            start = (start[0], start[1] - 1)
            list.append(matrix[start[0]][start[1]])
        else:
            break
    matrix_list.append(list)
    start = (start[0] + 1, start[1] + 1)



for mt in matrix_list:
    last = mt[-1]
    mt.pop()
    mt.insert(0, last)


def rotate_matrix(matrix_list):
    for mt in matrix_list:
        rotate_count = rotate % len(mt)
        for _ in range(rotate_count):
            last = mt[-1]
            mt.pop()
            mt.insert(0, last)
    return matrix_list

rotate_matrix(matrix_list)

visited = [[False for i in range(M)] for j in range(N)]
def list_to_matrix(matrix_list):
    start = (0, 0)
    for mt in matrix_list:
        while True:
            if (start[0] + 1 < N) and not visited[start[0] + 1][start[1]]:
                visited[start[0]][start[1]] = True
                matrix[start[0]][start[1]] = mt.pop(0)
                start = (start[0] + 1, start[1])
            else:
                break
        while True:
            if (start[1] + 1 < M) and not visited[start[0]][start[1] + 1]:
                visited[start[0]][start[1]] = True
                matrix[start[0]][start[1]] = mt.pop(0)
                start = (start[0], start[1] + 1)
            else:
                break
        while True:
            if (start[0] - 1 >= 0) and not visited[start[0] - 1][start[1]]:
                visited[start[0]][start[1]] = True
                matrix[start[0]][start[1]] = mt.pop(0)
                start = (start[0] - 1, start[1])
            else:
                break
        while True:
            if (start[0] == start[1] -1):
                visited[start[0]][start[1]] = True
                matrix[start[0]][start[1]] = mt.pop(0)
                start = (start[0], start[1] - 1)
            if (start[1] - 1 >= 0) and not visited[start[0]][start[1] - 1]:
                visited[start[0]][start[1]] = True
                matrix[start[0]][start[1]] = mt.pop(0)
                start = (start[0], start[1] - 1)
            else:
                break
        start = (start[0] + 1, start[1] + 1)

    return matrix

list_to_matrix(matrix_list)

for i in range(N):
    print(" ".join(map(str, matrix[i])))