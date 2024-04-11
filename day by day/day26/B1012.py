import sys
sys.setrecursionlimit(100000)

TK = int(input())

def dfs(y, x, arr, visited, width, height):
    if (x < 0 or x >= width or y < 0 or y >= height):
        return
    if visited[y][x] == 1:
        return
    visited[y][x] = 1
    if x > 0 and arr[y][x - 1] == 1 and visited[y][x - 1] == 0:
        dfs(y, x-1, arr, visited, width, height)
    if x < width - 1 and arr[y][x + 1] == 1 and visited[y][x + 1] == 0:
        dfs(y, x+1, arr, visited, width, height)
    if y > 0 and arr[y - 1][x] == 1 and visited[y - 1][x] == 0:
        dfs(y - 1, x, arr, visited, width, height)
    if y < height - 1 and arr[y + 1][x] == 1 and visited[y + 1][x] == 0:
        dfs(y + 1, x, arr, visited, width, height)

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])

for i in range(TK):
    width, height, cabbage = map(int, input().split())
    arr = [[0] * width for i in range(height)]
    visited = [[0] * width for i in range(height)]
    count = 0
    for j in range(cabbage):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # print("\n\n")
    for i in range(height):
        for j in range(width):
            if arr[i][j] == 1 and visited[i][j] == 0:
                # print("i: ", i, "j: ", j)
                # print_arr(visited)
                # print("\n\n")
                dfs(i, j, arr, visited, width, height)
                count += 1
    print(count)