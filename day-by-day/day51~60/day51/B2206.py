# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# height, width = map(int, input().split())
# matrix = [list(input()) for _ in range(height)]
# flag = False
# min_move = sys.maxsize

# def check(matrix, break_count, x, y, move):
#     global flag, min_move
#     if break_count > 1:
#         return
#     if min_move < move:
#         return
#     if x == height - 1 and y == width - 1:
#         if min_move > move:
#             min_move = move
#         return
#     # print(x, y, move, break_count)
#     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         if x + dx < 0 or y + dy < 0 or x + dx >= height or y + dy >= width:
#             continue
#         if matrix[x + dx][y + dy] == '0':
#             check(matrix, break_count, x + dx, y + dy, move + 1)
#         elif matrix[x + dx][y + dy] == '1':
#             check(matrix, break_count + 1, x + dx, y + dy, move + 1)
#     return -1

# check(matrix, 0, 0, 0, 1)
# if flag == False:
#     print(-1)
# else:
#     print(min_move)

# 9 9
# 010001000
# 010101010
# 010101010
# 010101010
# 010101010
# 010101010
# 010101010
# 010101011
# 000100010

import sys
from collections import deque
input = sys.stdin.readline
height, width = map(int, input().split())
matrix = [list(input()) for _ in range(height)]


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
        

def bfs():
    dq = deque()
    dq.append((0, 0, 0, 0))
    block1_visited = [[False] * width for _ in range(height)]
    block2_visited = [[False] * width for _ in range(height)]
    block1_visited[0][0] = True
    block2_visited[0][0] = True
    
    while dq:
        temp_dq = deque()
        while dq:
            x, y, block, move = dq.popleft()
            # print(x, y, block, move)
            # print_matrix(block1_visited)
            # print()
            if x == height - 1 and y == width - 1:
                print(move + 1)
                exit()
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if x + dx < 0 or y + dy < 0 or x + dx >= height or y + dy >= width:
                    continue
                if block == 0 and not block1_visited[x + dx][y + dy]:
                    if matrix[x + dx][y + dy] == '0':
                        block1_visited[x + dx][y + dy] = True
                        temp_dq.append((x + dx, y + dy, block, move + 1))
                    elif matrix[x + dx][y + dy] == '1':
                        block1_visited[x + dx][y + dy] = True
                        temp_dq.append((x + dx, y + dy, block + 1, move + 1))
                elif block == 1 and not block2_visited[x + dx][y + dy]:
                    if matrix[x + dx][y + dy] == '0':
                        block2_visited[x + dx][y + dy] = True
                        temp_dq.append((x + dx, y + dy, block, move + 1))
        dq = temp_dq

    return -1

result = bfs()
print(result)