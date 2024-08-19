height, width = map(int, input().split())
maze_trapped_zihoon = [list(input()) for _ in range(height)]
maze_zihoon_visited = [[0]*width for _ in range(height)]
maze_fire_visited = [[0]*width for _ in range(height)]

def print_maze():
    for row in maze_trapped_zihoon:
        print(row)
    print()

def bfs_maze():
    global width, height
    fire_queue = []
    zihoon_queue = []
    for hei in range(height):
        for wid in range(width):
            if maze_trapped_zihoon[hei][wid] == 'J':
                zihoon_queue.append((hei, wid))
                maze_zihoon_visited[hei][wid] = 1
            if maze_trapped_zihoon[hei][wid] == 'F':
                fire_queue.append((hei, wid))
                maze_fire_visited[hei][wid] = 1
    count = 0
    
    while True:
        temp_fire_queue = []
        temp_zihoon_queue = []
        
        while fire_queue:
            pos_y, pos_x = fire_queue.pop(0)
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y, new_x = pos_y + dy, pos_x + dx
                if new_y < 0 or new_y >= height or new_x < 0 or new_x >= width:
                    continue
                if maze_trapped_zihoon[new_y][new_x] == '.' and not maze_fire_visited[new_y][new_x]:
                    maze_trapped_zihoon[new_y][new_x] = 'F'
                    maze_fire_visited[new_y][new_x] = 1
                    temp_fire_queue.append((new_y, new_x))
        
        while zihoon_queue:
            pos_y, pos_x = zihoon_queue.pop(0)
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y, new_x = pos_y + dy, pos_x + dx
                if new_y < 0 or new_y >= height or new_x < 0 or new_x >= width:
                    print(count+1)
                    return
                if maze_trapped_zihoon[new_y][new_x] == '.' and not maze_zihoon_visited[new_y][new_x]:
                    maze_trapped_zihoon[new_y][new_x] = 'J'
                    maze_zihoon_visited[new_y][new_x] = 1
                    temp_zihoon_queue.append((new_y, new_x))
        
        if not temp_fire_queue and not temp_zihoon_queue:
            print("IMPOSSIBLE")
            return
        
        fire_queue = temp_fire_queue
        zihoon_queue = temp_zihoon_queue
        count += 1
        # print_maze()
bfs_maze()
