import heapq
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

v1, v2 = map(int, input().split())

     # (edge1) (edge2)  (edge3)
# 1. start ->  v1  ->   v2  -> N
# 2. start ->  v2  ->   v1  -> N 
# 두 경우 중 최소값을 찾게 되면 된다.

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # 간선 + 현재까지의 거리 = cost
            if cost < distance[i[0]]: # cost가 더 작다면 갱신
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))
    return distance

start = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

answer = min(start[v1] + v1_distance[v2] + v2_distance[N], start[v2] + v2_distance[v1] + v1_distance[N])
if answer >= INF:
    print(-1)
else:
    print(answer)