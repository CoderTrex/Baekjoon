N, M, R = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)]
OriginalMatrix = []
for i in range(N):
    OriginalMatrix.append(Matrix[i].copy())
command = list(map(int, input().split()))

def do_reverse_up_down(Matrix):
    for i in range(len(Matrix) // 2):
        Matrix[i], Matrix[len(Matrix) - 1 - i] = Matrix[len(Matrix) - 1 - i], Matrix[i]
    return Matrix

def do_reverse_left_right(Matrix):
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i]) // 2):
            Matrix[i][j], Matrix[i][len(Matrix[i]) - 1 - j] = Matrix[i][len(Matrix[i]) - 1 - j], Matrix[i][j]
    return Matrix

def do_rotate_90_degree_clockwise(Matrix):
    new_matrix = [[0 for i in range(len(Matrix))] for j in range(len(Matrix[0]))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            new_matrix[j][len(Matrix) - 1 - i] = Matrix[i][j]
    return new_matrix

def do_rotate_90_degree_counter_clockwise(Matrix):
    new_matrix = [[0 for i in range(len(Matrix))] for j in range(len(Matrix[0]))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            new_matrix[len(Matrix[i]) - 1 - j][i] = Matrix[i][j]
    return new_matrix

def do_rotate_90_degree_inner_clockwise(Matrix):
    height_half = len(Matrix) // 2
    width_half = len(Matrix[0]) // 2

    for i in range(len(Matrix) // 2):
        for j in range(len(Matrix[i]) // 2):
            tmp = Matrix[i][j]
            Matrix[i][j] = Matrix[i][width_half + j]
            Matrix[i][width_half + j] = Matrix[height_half + i][width_half + j]
            Matrix[height_half + i][width_half + j] = Matrix[height_half + i][j]
            Matrix[height_half + i][j] = tmp
    return Matrix

def do_rotate_90_degree_inner_counter_clockwise(Matrix):
    height_half = len(Matrix) // 2
    width_half = len(Matrix[0]) // 2

    for i in range(len(Matrix) // 2):
        for j in range(len(Matrix[i]) // 2):
            tmp = Matrix[i][j]
            Matrix[i][j] = Matrix[height_half + i][j]
            Matrix[height_half + i][j] = Matrix[height_half + i][width_half + j]
            Matrix[height_half + i][width_half + j] = Matrix[i][width_half + j]
            Matrix[i][width_half + j] = tmp
    return Matrix


from collections import deque
deque = deque()
deque.append(OriginalMatrix)

for i in range(R):
    cmd = command[i]
    if cmd == 1:
        deque.append(do_reverse_up_down(deque.popleft()))
    elif cmd == 2:
        deque.append(do_reverse_left_right(deque.popleft()))
    elif cmd == 3:
        deque.append(do_rotate_90_degree_clockwise(deque.popleft()))
    elif cmd == 4:
        deque.append(do_rotate_90_degree_counter_clockwise(deque.popleft()))
    elif cmd == 5:
        deque.append(do_rotate_90_degree_inner_counter_clockwise(deque.popleft()))
    elif cmd == 6:
        deque.append(do_rotate_90_degree_inner_clockwise(deque.popleft()))

print_matrix = deque.popleft()
for i in range(len(print_matrix)):
    for j in range(len(print_matrix[i])):
        print(print_matrix[i][j], end=' ')
    print()
