import heapq

INF = int(1e9)
student_count, road_count, target_village = map(int, input().split())

# village는 시작점을 인덱스로 가지며, 각 인덱스에는 해당 인덱스에서 갈 수 있는 마을과 비용이 저장되어 있음
village = [[] for _ in range(student_count)]

for _ in range(road_count):
    start, end, cost = map(int, input().split())
    village[start-1].append((end-1, cost))

def dijkstra(s):
    distance = [INF] * student_count # 시작점에서 각 마을로 가는 최단거리
    distance[s] = 0 # 시작점은 0으로 초기화
    q = [] # 우선순위 큐
    heapq.heappush(q, (0, s)) # 시작점을 우선순위 큐에 넣음

    while q:
        dist, now = heapq.heappop(q) # 최소 힙이기 때문에 가장 작은 값이 나옴
        if distance[now] < dist: # 이미 처리된 노드라면 무시-
            continue
        for v, value in village[now]: # v: 도착지, value: 비용 / 현재 노드에서 갈 수 있는 모든 노드에 대해 반복
            if dist + value < distance[v]:
                distance[v] = dist + value
                heapq.heappush(q, (dist + value, v))
    
    return distance

answer = dijkstra(target_village-1) # 목적지에서 각 마을로 가는 최단거리
for i in range(student_count):
    if i == target_village - 1:
        continue
    answer[i] += dijkstra(i)[target_village-1] # 각 마을에서 목적지로 가는 최단거리0

print(max(answer))


# def print_matrix(matrix):
#     print("    ", end="")
#     for i in range(len(matrix)):
#         print("{:1}도".format(i+1), end=" ")
#     print()
#     for i in range(len(matrix)):
#         print("{:1}출".format(i+1), end=" ")
#         for j in range(len(matrix[i])):
#             if (matrix[i][j] == INF):
#                 print("INF", end=" ")
#             else:
#                 print("{:3}".format(matrix[i][j]), end=" ")
#         print()

# ----------------------------------------------- #
# 다익스트라 알고리즘
# visited = [False] * student_count
# visited[target_village] = True
# while False in visited:
#     min_distance = INF
#     next_village = 0
#     for i in range(student_count):
#         if i == target_village:
#             continue
#         if matrix[target_village][i] < min_distance and visited[i] == False:
#             min_distance = matrix[target_village][i]
#             next_village = i
#     visited[next_village] = True
#     for i in range(student_count):
#         if i == target_village:
#             continue
#         if matrix[target_village][i] > matrix[target_village][next_village] + matrix[next_village][i]:
#             matrix[target_village][i] = matrix[target_village][next_village] + matrix[next_village][i]

# # print_matrix(matrix)

# visited = [False] * student_count
# visited[target_village] = True
# while False in visited:
#     min_distance = INF
#     next_village = 0
#     for i in range(student_count):
#         if i == target_village:
#             continue
#         if matrix[i][target_village] < min_distance and visited[i] == False:
#             min_distance = matrix[i][target_village]
#             next_village = i
#     visited[next_village] = True
#     for i in range(student_count):
#         if i == target_village:
#             continue
#         if matrix[i][target_village] > matrix[i][next_village] + matrix[next_village][target_village]:
#             matrix[i][target_village] = matrix[i][next_village] + matrix[next_village][target_village]
# print_matrix(matrix)


# ----------------------------------------------- #
# 플로이드 워셜 알고리즘
# for k in range(student_count):
#     for a in range(student_count):
#         for b in range(student_count):
#             if a == b:
#                 continue
#             else:
#                 matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

# print_matrix(matrix)
# ----------------------------------------------- #
# 목적지에서 각 마을로 가는 최단거리
# for i in range(student_count):
#     for j in range(student_count):
#         if i == j and i == target_village-1:
#             continue
#         matrix[target_village-1][i] = min(matrix[target_village-1][i], matrix[target_village-1][j] + matrix[j][i])

# 각 마을에서 목적지로 가는 최단거리
# for i in range(student_count):
#     for j in range(student_count):
#         if i == j and i == target_village-1:
#             continue
#         matrix[i][target_village-1] = min(matrix[i][target_village-1], matrix[i][j] + matrix[j][target_village-1])
# ----------------------------------------------- #


# answer = []
# for i in range(student_count):
#     if i == target_village - 1:
#         continue
#     print("i:", i+1, "target_village:", target_village+1)
#     print(matrix[i][target_village-1], matrix[target_village-1][i])
#     answer.append(matrix[i][target_village-1] + matrix[target_village-1][i])

# print(max(answer))
# print(answer)
# print_matrix(matrix)
