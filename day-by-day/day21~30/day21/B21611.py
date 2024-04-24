# ↑, ↓, ←, →
# 1, 2, 3, 4

N, M = map(int, input().split())

matrix = [[0 for i in range(N)] for j in range(N)]
magic_command = []

for i in range(N):
    matrix[i] = list(map(int, input().split()))

for i in range(M):
    magic_command.append(list(map(int, input().split())))

magician = [(N)//2, (N)//2]


def matrix_move(matrix):
    move = 1
    move_try = 0
    move_direction = 0
    pos_x, pos_y = magician[0], magician[1]
    while (True):
        if (move_direction == 0):
            


for command in magic_command:
    # ↑, ↓, ←, →
    # 1, 2, 3, 4
    if (command[0] == 1):
        magic_range = command[1]
        for i in range(1, magic_range+1):
            matrix[magician[0]-i][magician[1]] = 0
    elif (command[0] == 2):
        magic_range = command[1]
        for i in range(1, magic_range+1):
            matrix[magician[0]+i][magician[1]] = 0
    elif (command[0] == 3):
        magic_range = command[1]
        for i in range(1, magic_range+1):
            matrix[magician[0]][magician[1]-i] = 0
    elif  (command[0] == 4):
        magic_range = command[1]
        for i in range(1, magic_range+1):
            matrix[magician[0]][magician[1]+i] = 0
















for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=' ')
    print()
