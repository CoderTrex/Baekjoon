height, width, try_count = map(int, input().split())
half_height = height // 2
half_width = width // 2

matrix = [[0] * width for _ in range(height)]
matrix_small = [[0, 1], [2, 3]]
rotate_count = 0
reverse_h = False
reverse_w = False
command_list = []

for i in range(height):
    matrix[i] = list(map(int, input().split()))

matrix_list = [[[0] * half_width for _ in range(half_height)] for _ in range(4)]

for i in range(half_height):
    for j in range(half_width):
        matrix_list[0][i][j] = matrix[i][j]
        matrix_list[1][i][j] = matrix[i][j + half_width]
        matrix_list[2][i][j] = matrix[i + half_height][j]
        matrix_list[3][i][j] = matrix[i + half_height][j + half_width]

def command_1():
    global matrix_small, rotate_count, reverse_h
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[1][0], matrix_small[1][1], matrix_small[0][0], matrix_small[0][1]
    reverse_h = not reverse_h
    command_list.append(1)

def command_2():
    global matrix_small, rotate_count, reverse_w
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[0][1], matrix_small[0][0], matrix_small[1][1], matrix_small[1][0]
    reverse_w = not reverse_w
    command_list.append(2)

def command_3():
    global matrix_small, rotate_count
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[1][0], matrix_small[0][0], matrix_small[1][1], matrix_small[0][1]
    rotate_count += 1
    command_list.append(3)

def command_4():
    global matrix_small, rotate_count
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[0][1], matrix_small[1][1], matrix_small[0][0], matrix_small[1][0]
    rotate_count += 3
    command_list.append(4)
    
def command_5():
    global matrix_small, rotate_count
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[1][0], matrix_small[0][0], matrix_small[1][1], matrix_small[0][1]

def command_6():
    global matrix_small, rotate_count
    matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]\
        = matrix_small[0][1], matrix_small[1][1], matrix_small[0][0], matrix_small[1][0]

command_list = list(map(int, input().split()))
for i in range(try_count):
    command = command_list[i] 
    if command == 1:
        command_1()
    elif command == 2:
        command_2()
    elif command == 3:
        command_3()
    elif command == 4:
        command_4()
    elif command == 5:
        command_5()
    elif command == 6:
        command_6()

def print_matrix(one_count, two_count, three_count, four_count, _matrix_list):
    one, two = _matrix_list[one_count], _matrix_list[two_count]
    for i in range(half_height):
        for j in range(half_width):
            print(one[i][j], end=' ')
        for j in range(half_width):
            print(two[i][j], end=' ')
        print()
    three, four = _matrix_list[three_count], _matrix_list[four_count]
    for i in range(half_height):
        for j in range(half_width):
            print(three[i][j], end=' ')
        for j in range(half_width):
            print(four[i][j], end=' ')
        print()


def rotate_matrix():
    global matrix_list, rotate_count, half_height, half_width
    if (rotate_count == 0):
        for i in range(half_height):
            for j in range(half_width):
                new_matrix_list[0][i][j] = matrix_list[0][i][j]
                new_matrix_list[1][i][j] = matrix_list[1][i][j]
                new_matrix_list[2][i][j] = matrix_list[2][i][j]
                new_matrix_list[3][i][j] = matrix_list[3][i][j]

    if (rotate_count == 1):
        for i in range(half_height): 
            for j in range(half_width): 
                new_matrix_list[0][i][j] = matrix_list[0][half_width - 1 - j][i]
                new_matrix_list[1][i][j] = matrix_list[1][half_width - 1 - j][i]
                new_matrix_list[2][i][j] = matrix_list[2][half_width - 1 - j][i]
                new_matrix_list[3][i][j] = matrix_list[3][half_width - 1 - j][i]

    elif (rotate_count == 2):
        for i in range(half_height):
            for j in range(half_width):
                new_matrix_list[0][i][j] = matrix_list[0][half_height - 1 - i][half_width - 1 - j]
                new_matrix_list[1][i][j] = matrix_list[1][half_height - 1 - i][half_width - 1 - j]
                new_matrix_list[2][i][j] = matrix_list[2][half_height - 1 - i][half_width - 1 - j]
                new_matrix_list[3][i][j] = matrix_list[3][half_height - 1 - i][half_width - 1 - j]

    elif (rotate_count == 3):
        for i in range(half_height):
            for j in range(half_width):
                new_matrix_list[0][i][j] = matrix_list[0][j][half_height - 1 - i]
                new_matrix_list[1][i][j] = matrix_list[1][j][half_height - 1 - i]
                new_matrix_list[2][i][j] = matrix_list[2][j][half_height - 1 - i]
                new_matrix_list[3][i][j] = matrix_list[3][j][half_height - 1 - i]

def reverse_matrix():
    if reverse_h:
        for i in range(half_height // 2):
            for j in range(half_width):
                new_matrix_list[0][i][j], new_matrix_list[0][half_height - 1 - i][j] = new_matrix_list[0][half_height - 1 - i][j], new_matrix_list[0][i][j]
                new_matrix_list[1][i][j], new_matrix_list[1][half_height - 1 - i][j] = new_matrix_list[1][half_height - 1 - i][j], new_matrix_list[1][i][j]
                new_matrix_list[2][i][j], new_matrix_list[2][half_height - 1 - i][j] = new_matrix_list[2][half_height - 1 - i][j], new_matrix_list[2][i][j]
                new_matrix_list[3][i][j], new_matrix_list[3][half_height - 1 - i][j] = new_matrix_list[3][half_height - 1 - i][j], new_matrix_list[3][i][j]
    if reverse_w:
        for i in range(half_height):
            for j in range(half_width // 2):
                new_matrix_list[0][i][j], new_matrix_list[0][i][half_width - 1 - j] = new_matrix_list[0][i][half_width - 1 - j], new_matrix_list[0][i][j]
                new_matrix_list[1][i][j], new_matrix_list[1][i][half_width - 1 - j] = new_matrix_list[1][i][half_width - 1 - j], new_matrix_list[1][i][j]
                new_matrix_list[2][i][j], new_matrix_list[2][i][half_width - 1 - j] = new_matrix_list[2][i][half_width - 1 - j], new_matrix_list[2][i][j]
                new_matrix_list[3][i][j], new_matrix_list[3][i][half_width - 1 - j] = new_matrix_list[3][i][half_width - 1 - j], new_matrix_list[3][i][j]


def execute_matrix():
    global matrix_list, rotate_count, half_height, half_width, reverse_h, reverse_w
    if (rotate_count % 2) != 0:
        half_height, half_width = half_width, half_height
    new_matrix_list = [[[0] * half_width for _ in range(half_height)] for _ in range(4)]
    rotate_count = rotate_count % 4




    one, two, three, four = matrix_small[0][0], matrix_small[0][1], matrix_small[1][0], matrix_small[1][1]
    print_matrix(one, two, three, four, new_matrix_list)

execute_matrix()