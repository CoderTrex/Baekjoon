N, K = map(int, input().split())

matrix = [[0] * (N) for _ in range(N)]
active_virus = [[0] * (N) for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().split()))
    active_virus[i] = [0 if x == 0 else 1 for x in matrix[i]]

time, x, y = map(int, input().split())



for t in range(time):
    change_list = []
    
    for i in range(N):
        for j in range(N):
            if active_virus[i][j] == t + 1:

                # 1. 이동 가능한 칸이어야 함 
                # 2. 이동한 칸이 아직 바이러스가 퍼지지 않은 곳 
                # 3. 이동한 칸이 현재 바이러스보다 작은 값이며, 이번 차례에 바이러스가 퍼진 곳

                
                # 위로 이동: 
                if i > 0 and (matrix[i-1][j] == 0 or (matrix[i-1][j] > matrix[i][j] and [i-1, j] in change_list)):
                    change_list.append([i-1, j])
                    matrix[i-1][j] = matrix[i][j]
                    active_virus[i-1][j] = t + 2
                    # print("up")
                    # print("i: ", i, "j: ", j, "matrix[i-1][j]: ", matrix[i-1][j], "matrix[i][j]: ", matrix[i][j])
                # 아래로 이동
                if i < N-1 and (matrix[i+1][j] == 0 or (matrix[i+1][j] > matrix[i][j] and [i+1, j] in change_list)):
                    change_list.append([i+1, j])
                    matrix[i+1][j] = matrix[i][j]
                    active_virus[i+1][j] = t + 2
                    # print("down")
                    # print("i: ", i, "j: ", j, "matrix[i-1][j]: ", matrix[i-1][j], "matrix[i][j]: ", matrix[i][j])
                # 왼쪽으로 이동
                if j > 0 and (matrix[i][j-1] == 0 or (matrix[i][j-1] > matrix[i][j] and [i, j-1] in change_list)):
                    change_list.append([i, j-1])
                    matrix[i][j-1] = matrix[i][j]
                    active_virus[i][j-1] = t + 2
                    # print("left")
                    # print("i: ", i, "j: ", j, "matrix[i-1][j]: ", matrix[i-1][j], "matrix[i][j]: ", matrix[i][j])
                # 오른쪽으로 이동
                if j < N-1 and (matrix[i][j+1] == 0 or (matrix[i][j+1] > matrix[i][j] and [i, j+1] in change_list)):
                    change_list.append([i, j+1])
                    matrix[i][j+1] = matrix[i][j]
                    active_virus[i][j+1] = t + 2
                    # print("right")
                    # print("i: ", i, "j: ", j, "matrix[i-1][j]: ", matrix[i-1][j], "matrix[i][j]: ", matrix[i][j])
                active_virus[i][j] = 0
    # print("t: ", t)   
print(matrix[x-1][y-1])