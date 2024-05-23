import sys
import heapq


INF = 1e9
X, Y = map(float, sys.stdin.readline().rstrip().split())
TX, TY = map(float, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
cannons = []

for i in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    cannons.append([x, y])
cannons.insert(0, [X, Y])
cannons.append([TX, TY])

nodes = [[] for _ in range(n+2)]

def get_distance(x1, y1, x2, y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return dist


for i in range(1, n+2):
    x1, y1 = cannons[i]
    dist = get_distance(X, Y, x1, y1)
    nodes[0].append([i, dist/5.0])

for i in range(1, n+1):
    x1, y1 = cannons[i]
    dist = get_distance(x1, y1, TX, TY)
    nodes[i].append([n+1, dist/5.0])
    nodes[i].append([n+1, 2.0 + (abs(dist-50.0)/5.0)])

for i in range(1, n+1):
    x1, y1 = cannons[i]
    for j in range(i+1, n+1):
        x2, y2 = cannons[j]
        dist = get_distance(x1, y1, x2, y2)
        nodes[i].append([j, dist/5.0])
        nodes[i].append([j, 2.0 + (abs(dist-50.0)/5.0)])
        nodes[j].append([i, dist/5.0])
        nodes[j].append([i, 2.0 + (abs(dist-50.0)/5.0)])

def Dijkstra():
    distances = [INF for _ in range(n+2)]
    distances[0] = 0.0
    pq = []
    heapq.heappush(pq, [0.0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue
        elif cur_node == n+1: continue

        for next_node, next_cost in nodes[cur_node]:
            cost = cur_cost + next_cost
            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(pq, [cost, next_node])

    return distances[n+1]

print(round(Dijkstra(), 6))