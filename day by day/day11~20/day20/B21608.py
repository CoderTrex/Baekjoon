# 3
# 4 2 5 1 7
# 3 1 9 4 5
# 9 8 1 2 3
# 8 1 9 3 4
# 7 2 3 4 8
# 1 9 2 5 7
# 6 5 2 3 4
# 5 1 9 2 8
# 2 9 3 1 4

# 1.    비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2.    1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3.    2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
#       그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

size = int(input())
command = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

matrix = [[0 for i in range(size)] for j in range(size)]

for i in range(size*size):
    command.append(list(map(int, input().split())))

# command 전부다 돌면서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
for index in range(size*size):
    student = command[index][0]     # 학생 번호
    like    = command[index][1:]    # 좋아하는 학생들
    find_x, find_y = 0, 0
    max_count, like_count = 0, 0
    max_empty, empty_count = 0, 0
    for i in range(size):
        for j in range(size):
            like_count = 0
            empty_count = 0
            if matrix[i][j] != 0:
                continue
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < size and 0 <= y < size:
                    if matrix[x][y] in like:
                        like_count += 1
                    if matrix[x][y] == 0:
                        empty_count += 1
            if max_count < like_count:
                max_count = like_count
                max_empty = empty_count
                find_x = i
                find_y = j
            elif max_count == like_count:
                if max_empty < empty_count:
                    max_empty = empty_count
                    find_x = i
                    find_y = j
            if (find_x == 0 and find_y == 0) and (matrix[0][0] != 0):
                find_x = i
                find_y = j
    #         print("{0}: ({1}, {2}) like: {3} / empty: {4}".format(student, i, j, like_count, empty_count))
    # print("max: ({0}, {1}) like: {2} / empty: {3}".format(find_x, find_y, max_count, max_empty))
    matrix[find_x][find_y] = student

# print()
# for i in range(size):
#     for j in range(size):
#         print(matrix[i][j], end=' ')
#     print()

total_happy = 0
for i in range(size):
    for j in range(size):
        stu = matrix[i][j]
        like_list = []

        for k in range(size*size):
            if command[k][0] == stu:
                like_list = command[k][1:]
                break
        
        like_count = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < size and 0 <= y < size:
                if matrix[x][y] in like_list:
                    like_count += 1
        
        if like_count == 1:
            total_happy += 1
        elif like_count == 2:
            total_happy += 10
        elif like_count == 3:
            total_happy += 100
        elif like_count == 4:
            total_happy += 1000

print(total_happy)