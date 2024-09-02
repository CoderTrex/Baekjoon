# from collections import deque

# vertex, edge, start = map(int, input().split())
# matrix = [[False] * (vertex + 1) for _ in range(vertex + 1)]

# for _ in range(edge):
#     a, b = map(int, input().split())
#     matrix[a][b] = True
#     matrix[b][a] = True

# dfs_visited = [False] * (vertex + 1)
# bfs_visited = [False] * (vertex + 1)

# def dfs(loc):
#     dfs_visited[loc] = True
#     print(loc, end=" ")
#     for i in range(1, vertex + 1):
#         if not dfs_visited[i] and matrix[loc][i]:
#             dfs(i)

# def bfs():
#     dq = deque([start])
#     bfs_visited[start] = True
#     while dq:
#         value = dq.popleft()
#         print(value, end=" ")
#         for i in range(1, vertex + 1):
#             if not bfs_visited[i] and matrix[value][i]:
#                 dq.append(i)
#                 bfs_visited[i] = True

# dfs(start)
# print()
# bfs()

from collections import deque

vertex, edge, start = map(int, input().split())
matrix = [[False] * (vertex + 1) for _ in range(vertex + 1)]

for i in range(edge):
    a, b = map(int, input().split())
    matrix[a][b] = True
    matrix[b][a] = True

dfs_visited = [False] * (vertex + 1)
bfs_visited = [False] * (vertex + 1)

# def print_matrix():
#     for i in range(vertex + 1):
#         for j in range(vertex + 1):
#             print(matrix[i][j], end=" ")
#         print()
# print_matrix()

def dfs(loc):
    dfs_visited[loc] = True
    print(loc, end=" ")
    for i in range(vertex + 1):
        if not dfs_visited[i] and matrix[loc][i]:
            dfs(i)

def bfs():
    dq = deque([start])
    bfs_visited[start] = True
    while dq:
        value = dq.popleft()
        print(value, end=" ")
        for i in range(vertex + 1):
            if not bfs_visited[i] and matrix[value][i]:
                dq.append(i)
                bfs_visited[i] = True

dfs(start)
print()
bfs()