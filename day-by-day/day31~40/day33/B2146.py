from collections import deque
import sys
sys.setrecursionlimit(10**9)

Size = int(input())
island_map = [list(map(int, input().split())) for _ in range(Size)]
island_vistied = [[0] * Size for _ in range(Size)]
island_distance = [[0] * Size for _ in range(Size)]

def print_map(map):
    print("Print Map Function")
    for i in range(Size):
        for j in range(Size):
            print(map[i][j], end = " ")
        print()
    print()

color = 1
def dfs_color_island(x, y):
    global color
    # print("x: ", x, "y: ", y, "color: ", color)
    # print_map(island_vistied)
    if x - 1 >= 0 and island_map[x - 1][y] == 1 and island_vistied[x - 1][y] == 0:
        island_vistied[x - 1][y] = 1
        island_map[x - 1][y] = color
        dfs_color_island(x - 1, y)
    if x + 1 < Size and island_map[x + 1][y] == 1 and island_vistied[x + 1][y] == 0:
        island_vistied[x + 1][y] = 1
        island_map[x + 1][y] = color
        dfs_color_island(x + 1, y)
    if y - 1 >= 0 and island_map[x][y - 1] == 1 and island_vistied[x][y - 1] == 0:
        island_vistied[x][y - 1] = 1
        island_map[x][y - 1] = color
        dfs_color_island(x, y - 1)
    if y + 1 < Size and island_map[x][y + 1] == 1 and island_vistied[x][y + 1] == 0:
        island_vistied[x][y + 1] = 1
        island_map[x][y + 1] = color
        dfs_color_island(x, y + 1)

for i in range(Size):
    for j in range(Size):
        if island_map[i][j] == 1 and island_vistied[i][j] == 0:        
            island_vistied[i][j] = 1
            island_map[i][j] = color
            dfs_color_island(i, j)
            color += 1

# print_map(island_map)
shortest_distance_list = [9999999 for _ in range(color - 1)]

def cal_distance(dq, color, island_vistied):
    step = 0
    temp_dq = deque()
    flag = False
    while (dq):
        while (dq):
            # print("x: ", x, "y: ", y, "color: ", color, "step: ", step)
            # print_map(island_vistied)
            x, y = dq.popleft()
            island_vistied[x][y] = 1
            if x + 1 < Size and island_vistied[x + 1][y] == 0 and island_map[x + 1][y] != color:
                if island_map[x + 1][y] != 0 and island_map[x + 1][y] != color:
                    # print("x: ", x, "y: ", y, "color: ", color, "step: ", step, "shortest_distance_list: ", shortest_distance_list)
                    shortest_distance_list[color - 1] = min(shortest_distance_list[color - 1], step)
                    flag = True
                    break
                else:
                    temp_dq.append((x + 1, y))
                    island_vistied[x + 1][y] = 1
            if y + 1 < Size and island_vistied[x][y + 1] == 0 and island_map[x][y + 1] != color:
                if island_map[x][y + 1] != 0 and island_map[x][y + 1] != color:
                    # print("x: ", x, "y: ", y, "color: ", color, "step: ", step, "shortest_distance_list: ", shortest_distance_list)
                    shortest_distance_list[color - 1] = min(shortest_distance_list[color - 1], step)
                    flag = True
                    break
                else:
                    temp_dq.append((x, y + 1))
                    island_vistied[x][y + 1] = 1
            if x - 1 >= 0 and island_vistied[x - 1][y] == 0 and island_map[x - 1][y] != color:
                if island_map[x - 1][y] != 0 and island_map[x - 1][y] != color:
                    # print("x: ", x, "y: ", y, "color: ", color, "step: ", step, "shortest_distance_list: ", shortest_distance_list)
                    shortest_distance_list[color - 1] = min(shortest_distance_list[color - 1], step)
                    flag = True
                    break
                else:
                    temp_dq.append((x - 1, y))
                    island_vistied[x - 1][y] = 1
            if y - 1 >= 0 and island_vistied[x][y - 1] == 0 and island_map[x][y - 1] != color:
                if island_map[x][y - 1] != 0 and island_map[x][y - 1] != color:
                    # print("x: ", x, "y: ", y, "color: ", color, "step: ", step, "shortest_distance_list: ", shortest_distance_list)
                    shortest_distance_list[color - 1] = min(shortest_distance_list[color - 1], step)
                    flag = True
                    break
                else:
                    temp_dq.append((x, y - 1))
                    island_vistied[x][y - 1] = 1
        if flag or shortest_distance_list[color - 1] <= step:
            shortest_distance_list[color - 1] = min(shortest_distance_list[color - 1], step)
            break

        if len(dq) == 0:
            dq = temp_dq
            temp_dq = deque()
            step += 1


dq = deque()
for i in range(Size):
    for j in range(Size):
        if island_map[i][j]:
            dq.append((i, j))
            island_vistied = [[0] * Size for _ in range(Size)]
            island_vistied[i][j] = 1
            cal_distance(dq, island_map[i][j], island_vistied)

# print("shortest_distance_list: ", shortest_distance_list)

print(min(shortest_distance_list))