def get_cycle(arr, start, visited, s_visited):
    # print(start + 1, visited)
    s_visited[start] = 1
    visited[start] = 1
    next = arr[start] - 1
    if s_visited[next] == 0 and visited[next] == 0:
        get_cycle(arr, next, visited, s_visited)
        return 1
    else:
        # print(start + 1, visited)
        return 1

N = int(input())

for i in range(N):
    len = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * len
    total = 0
    for j in range(len):
        if visited[j] == 0:
            small_visited = [0] * len
            total += get_cycle(arr, j, visited, small_visited)
    print(total)