# 3 7
# 32 62
# 42 68
# 12 98
# 95 13
# 97 25
# 93 37
# 79 27
# 75 19
# 49 47
# 67 17

ladder, snake = map(int, input().split())
ladder_dict = {}
snake_dict = {}

for _ in range(ladder):
    a, b = map(int, input().split())
    ladder_dict[a] = b

for _ in range(snake):
    a, b = map(int, input().split())
    snake_dict[a] = b

import queue

def bfs():
    qu = queue.Queue()
    qu.put(1)
    visited = [0] * 101
    visited[1] = 1

    while not qu.empty():
        x = qu.get()
        for i in range(1, 7):
            y = x + i
            if y > 100:
                continue
            
            if y in ladder_dict:
                y = ladder_dict[y]
            elif y in snake_dict:
                y = snake_dict[y]
            
            if visited[y] == 0:
                visited[y] = visited[x] + 1
                qu.put(y)
    return visited[100] - 1

print(bfs())