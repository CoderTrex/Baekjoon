height, width = map(int, input().split())
matrix = [[] for _ in range(height)]
visited = [[False] * (width * height)]

for hei in range(height):
    matrix[hei] = list(input())

max_size = 0
def dfs(dy, dx, visited):
    global max_size
    if (len(visited) > max_size):
        max_size = len(visited)
    
    if dx+1 < width:
        if not matrix[dy][dx+1] in visited:
            # print("x+1", visited)
            dfs(dy, dx+1, visited + matrix[dy][dx+1])
    if dx-1 > -1:
        if not matrix[dy][dx-1] in visited:
            # print("x-1", visited)
            dfs(dy, dx-1, visited + matrix[dy][dx-1])
    if dy+1 < height:
        if not matrix[dy+1][dx] in visited:
            # print("y+1", visited)
            dfs(dy+1, dx, visited + matrix[dy+1][dx])
    if dy-1 > -1:
        if not matrix[dy-1][dx] in visited:
            # print("y-1", visited)
            dfs(dy-1, dx, visited + matrix[dy-1][dx])
dfs(0, 0, matrix[0][0])

print(max_size)