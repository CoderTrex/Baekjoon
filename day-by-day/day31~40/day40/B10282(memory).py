from collections import deque
import heapq
INF = 1e9

def dijkstra(matrix, hacked):
    time = [INF] * count_com
    time[hacked] = 0

    hack_count, total_time = 0, 0
    pq = []
    heapq.heappush(pq, (0, hacked))

    while pq:
        current_time, current_com = heapq.heappop(pq)

        if time[current_com] < current_time:
            continue

        for next_com, next_time in matrix[current_com]:
            next_time += current_time
            if next_time < time[next_com]:
                time[next_com] = next_time
                heapq.heappush(pq, (next_time, next_com))
    
    for t in time:
        if t != INF:
            hack_count += 1
            total_time = max(total_time, t)

    return hack_count, total_time

test_case = int(input())

for _ in range(test_case):
    
    count_com, dependency, hacked = map(int, input().split())
    hacked -= 1

    # [감염되는 컴퓨터][감염시키는 컴퓨터] 
    # value: 감염시키는데 걸리는 시간
    matrix = [[] for _ in range(count_com)]

    for _ in range(dependency):
        a_com, b_com, time = map(int, input().split())
        matrix[b_com-1].append((a_com-1, time))
    
    count, time = dijkstra(matrix, hacked)
    print(count, time)



# 1
# 3 2 1
# 2 1 5
# 3 2 5


# 1
# 3 2 2
# 2 1 5
# 3 2 5

# 1
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4

# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4


# 1
# 5 6 1
# 4 1 1
# 3 1 5
# 2 1 9
# 3 2 1
# 2 4 5
# 3 4 2

# 1
# 5 7 1
# 4 1 1
# 3 1 5
# 2 1 9
# 3 2 1
# 2 4 5
# 3 4 2
# 5 4 5
