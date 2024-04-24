# 6 8 1
# 3 2 6 3 1 2 9 7
# 9 7 8 2 1 4 5 3
# 5 9 2 1 9 6 1 8
# 2 1 3 8 6 3 9 2
# 1 3 2 8 7 9 2 1
# 4 5 1 9 8 2 1 3
# 1

import copy

height, width, try_count = map(int, input().split())

matrix = [[0] * width for _ in range(height)]
cp_matrix = [[0] * width for _ in range(height)]
for i in range(height):
    matrix[i] = list(map(int, input().split()))
    cp_matrix[i] = matrix[i][:]




def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def command_1(matrix):
    top_line = 0
    bottom_line = height - 1
    while top_line <= bottom_line:
        matrix[top_line], matrix[bottom_line] = matrix[bottom_line], matrix[top_line]
        top_line += 1
        bottom_line -= 1

def command_2(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()

def command_3(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][len(matrix) - i - 1] = matrix[i][j]
    matrix.clear()
    matrix.extend(new_matrix)

def command_4(matrix):
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[len(matrix[0]) - 1 - j][i] = matrix[i][j]
    matrix.clear()
    matrix.extend(new_matrix)

def command_5(matrix):
    temp_quarter = [[0] * (len(matrix[0]) // 2) for _ in range(len(matrix) // 2)]
    half_height = len(matrix) // 2
    half_width  = len(matrix[0]) // 2
    for i in range(len(matrix)//2):
        temp_quarter[i] = matrix[i][:half_width]
    
    for i in range(half_height):
        for j in range(half_width):
            matrix[i][j] = matrix[i + half_height][j]
    
    for i in range(half_height):
        for j in range(half_width):
            matrix[i + half_height][j] = matrix[i + half_height][j + half_width]
    
    for i in range(half_width):
        for j in range(half_height):
            matrix[j + half_height][i + half_width] = matrix[j][i + half_width]
        
    for i in range(half_width):
        for j in range(half_height):
            matrix[j][i + half_width] = temp_quarter[j][i]

def command_6(matrix):
    temp_quarter = [[0] * (len(matrix[0]) // 2) for _ in range(len(matrix) // 2)]
    half_height = len(matrix) // 2
    half_width  = len(matrix[0]) // 2
    for i in range(len(matrix)//2):
        temp_quarter[i] = matrix[i][:half_width]
    
    for i in range(half_height):
        for j in range(half_width):
            matrix[i][j] = matrix[i][j + half_width]
    
    for i in range(half_height):
        for j in range(half_width):
            matrix[i][j + half_width] = matrix[i + half_height][j + half_width]

    for i in range(half_width):
        for j in range(half_height):
            matrix[j + half_height][i + half_width] = matrix[j + half_height][i]
    
    for i in range(half_width):
        for j in range(half_height):
            matrix[j + half_height][i] = temp_quarter[j][i]



command_list = list(map(int, input().split()))
# version 1 : 상하 반전
# version 2 : 좌우 반전
# version 3 : 오른쪽 90도 회전
# version 4 : 왼쪽 90도 회전
# version 5 : 4등분 후 시계방향 회전
# version 6 : 4등분 후 반시계방향 회전

for i in range(try_count):
    command = command_list[i] 
    if command == 1:
        command_1(matrix)
    elif command == 2:
        command_2(matrix)
    elif command == 3:
        command_3(matrix)
    elif command == 4:
        command_4(matrix)
    elif command == 5:
        command_5(matrix)
    elif command == 6:
        command_6(matrix)


print_matrix(matrix)

