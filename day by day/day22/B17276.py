# 2 3 4
# 1   5
# 8 7 6

def up_element(original_matrix, matrix, size, version):
    if (version == 1):
        # 1 -> 2
        mid = size//2
        for i in range(size//2):
            matrix[i][i] = original_matrix[mid][i]
    if (version == 2):
        # 5 -> 4
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid-i][mid+i] = original_matrix[mid][mid+i]
    if (version == 3):
        # 8 -> 1 
        mid = size//2
        for i in range(size//2):
            matrix[mid][i] = original_matrix[mid+mid-i][i]
    if (version == 4):
        # 6 -> 5 
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid][mid+i] = original_matrix[mid+i][mid+i]
    return matrix

def down_element(original_matrix, matrix, size, version):
    if (version == 1):
        # 1 -> 8
        mid = size//2
        for i in range(size//2):
            matrix[mid+mid-i][i] = original_matrix[mid][i]
    if (version == 2):
        # 5 -> 6
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid+i][mid+i] = original_matrix[mid][mid+i]
    if (version == 3):
        # 2 -> 1 
        mid = size//2
        for i in range(size//2):
            matrix[mid][i] = original_matrix[i][i]
    if (version == 4):
        # 4 -> 5
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid][mid+i] = original_matrix[mid-i][mid+i]
    return matrix


def left_element(original_matrix, matrix, size, version):
    if version == 1:
        # 3 -> 2
        mid = size//2
        for i in range(size//2):
            matrix[i][i] = original_matrix[i][mid]
    if version == 2:
        # 7 -> 8 
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid+i][mid-i] = original_matrix[mid+i][mid]
    if version == 3:
        # 4 -> 3
        mid = size//2
        for i in range(size//2):
            matrix[i][mid] = original_matrix[i][mid+mid-i]
    if version == 4:
        # 6 -> 7
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid+i][mid] = original_matrix[mid+i][mid+i]
    return matrix


def right_element(original_matrix, matrix, size, version):
    if version == 1:
        # 3 -> 4
        mid = size//2
        for i in range(size//2):
            matrix[i][mid+mid-i] = original_matrix[i][mid]
    if version == 2:
        # 7 -> 6
        mid = size//2
        for i in range(1, size//2 + 1):
            matrix[mid+i][mid+i] = original_matrix[mid+i][mid]
    if version == 3:
        # 2 -> 3
        mid = size//2
        for i in range(size//2):
            matrix[i][mid] = original_matrix[i][i]
    if version == 4:
        # 8 -> 7
        mid = size//2
        for i in range(0, size//2):
            print(matrix[mid+mid-i][mid], original_matrix[mid+mid-i][i])
            matrix[mid+mid-i][mid] = original_matrix[mid+mid-i][i]
    return matrix

def right_rotate(original_matrix, matrix, size, time):
    for _ in range(time):
        up_element(original_matrix, matrix, size, 1) # 1 -> 2
        up_element(original_matrix, matrix, size, 3) # 8 -> 1
        left_element(original_matrix, matrix, size, 2) # 7 -> 8
        left_element(original_matrix, matrix, size, 4) # 6 -> 7
        down_element(original_matrix, matrix, size, 2) # 5 -> 6
        down_element(original_matrix, matrix, size, 4) # 4 -> 5
        right_element(original_matrix, matrix, size, 1) # 3 -> 4
        right_element(original_matrix, matrix, size, 3) # 2 -> 3
        for i in range(size):
            original_matrix[i] = matrix[i].copy()
    return matrix

TK = int(input())

for _ in range(TK):
    size, angle = map(int, input().split())
    
    matrix = [[0 for i in range(size)] for j in range(size)]
    original_matrix = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        matrix[i] = list(map(int, input().split()))
        original_matrix[i] = matrix[i].copy()

    if (angle == 45 or angle == -315):
        matrix = right_rotate(original_matrix, matrix, size, 1)
    elif (angle == 90 or angle == -270):
        matrix = right_rotate(original_matrix, matrix, size, 2)
    elif (angle == 135 or angle == -225):
        matrix = right_rotate(original_matrix, matrix, size, 3)
    elif (angle == 180 or angle == -180):
        matrix = right_rotate(original_matrix, matrix, size, 4)
    elif (angle == 225 or angle == -135):
        matrix = right_rotate(original_matrix, matrix, size, 5)
    elif (angle == 270 or angle == -90):
        matrix = right_rotate(original_matrix, matrix, size, 6)
    elif (angle == 315 or angle == -45):
        matrix = right_rotate(original_matrix, matrix, size, 7)
    elif (angle == 360 or angle == 0):
        matrix = matrix
    for i in range(size):
        for j in range(size):
            print("{}".format(matrix[i][j]), end=" ")
        print()


# 1
# 7 45
# 1 2 3 4 5 6 7
# 8 9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35
# 36 37 38 39 40 41 42
# 43 44 45 46 47 48 49