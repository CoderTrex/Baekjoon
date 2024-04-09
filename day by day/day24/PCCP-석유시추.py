import sys
sys.setrecursionlimit(10**6)

cnt = 0
land_value = {}

def dfs_land(land, start, land_visited, height, width, land_number):
    if start[0] < 0 or start[0] >= height or start[1] < 0 or start[1] >= width:
        return
    if land_visited[start[0]][start[1]] != 0 or land[start[0]][start[1]] == 0:
        return
    global cnt
    cnt += 1
    land_visited[start[0]][start[1]] = land_number
    dfs_land(land, (start[0] + 1, start[1]), land_visited, height, width, land_number)
    dfs_land(land, (start[0] - 1, start[1]), land_visited, height, width, land_number)
    dfs_land(land, (start[0], start[1] + 1), land_visited, height, width, land_number)
    dfs_land(land, (start[0], start[1] - 1), land_visited, height, width, land_number)
    return cnt

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

def solution(land):
    # print_matrix(land)
    land_number, height, width = 0, len(land), len(land[0])
    land_visited = [[0] * width for _ in range(height)]
    global cnt
    for j in range(width):
        for i in range(height):
            if land[i][j] != 0 and land_visited[i][j] == 0:
                cnt = 0
                land_number += 1
                cnt += dfs_land(land, (i, j), land_visited, height, width, land_number)
                land_value[land_number] = cnt

    line_value_dict = {}
    highest_value_line = 0
    for j in range(width):
        list = []
        line_value = 0
        for i in range(height):
            if land_visited[i][j] != 0 and land_visited[i][j] not in list:
                list.append(land_visited[i][j])
                line_value += land_value[land_visited[i][j]]
        line_value_dict[j] = line_value
        if highest_value_line < line_value:
            highest_value_line = line_value
    
        
    # print("\nland value\n")
    # print(land_value)
    # print("\nland visited\n")
    # print_matrix(land_visited)
    # print("\nline value\n")
    # print(line_value_dict)
    # print("\nhighest value line\n")
    # print(highest_value_line)
    return highest_value_line

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) # 6
