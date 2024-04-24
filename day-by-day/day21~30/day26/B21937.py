N, M = map(int, input().split())

dict_node = {}
for i in range(M):
    start, end = map(int, input().split())
    if end not in dict_node:
        dict_node[end] = []
    dict_node[end].append(start)

target = int(input())
count = 0
while True:
    if target in dict_node:
        for i in dict_node[target]:
            count += 1
            target = i
    else:
        break

print(count)


# N, M = map(int, input().split())
# matrix = [[0] * N for _ in range(N)]

# for _ in range(M):
#     start, end = map(int, input().split())
#     matrix[start-1][end-1] = 1

# target = int(input())
# count = 0
# target_list = [target-1]

# def print_matrix(matrix):
#     for i in range(N):
#         print(matrix[i])

# list_node = []
# while True:
#     found = False
#     for t in target_list:
#         target_list.remove(t)
#         for i in range(N):
#             if matrix[i][t] == 1:
#                 # print("t: ", t, "i: ", i, "matrix[t][i]: ", matrix[t][i])
#                 if i not in list_node:
#                     list_node.append(i)
#                     count += 1
#                 target_list.append(i)
#                 found = True
#     if not found:
#         break

# print(count)


N,M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int, input().split())
    graph[y].append(x)

start = int(input())
stack = [start]
cnt = 0
visited = [True for _ in range(N+1)]
visited[start] = False
while stack:
    x = stack.pop()
    for next_node in graph[x]:
        if visited[next_node]:
            visited[next_node] = False
            cnt += 1
            stack.append(next_node)
print(cnt)


from collections import deque
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

N,M = MIIS()
cnt = 0
work = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
	a, b = MIIS()
	work[b].append(a)

start = int(input())
que = deque()
que.append(start)
visited[start] = True

while que:
	x = que.popleft()
	for i in work[x]:
		if not visited[i]:
			visited[i] = True
			cnt += 1
			que.append(i)

print(cnt)