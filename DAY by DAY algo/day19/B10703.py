height, width = map(int, input().split())
arr = [['.' for _ in range(width)] for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

for i in range(height):
    arr[i] = list(input())

start = 0
short_height = height
for i in range(width):
    comet_flag = False
    for j in range(height):
        if arr[j][i] == 'X':
            comet_flag = True
            start = j
        if arr[j][i] == '#' and comet_flag:
            short_height = min(short_height, j - start)
            break

for j in range(height - 1, -1, -1):
    for i in range(width):
        if arr[j][i] == 'X' and not visited[j][i]:
            arr[j + short_height - 1][i] = 'X'
            arr[j][i] = '.'
            visited[j][i] = True

for i in range(height):
    print(''.join(arr[i]))

