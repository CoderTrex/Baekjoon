from collections import deque

test_case = int(input())

for _ in range(test_case):
    
    count_com, dependency, hacked = map(int, input().split())
    hacked -= 1

    # [감염되는 컴퓨터][감염시키는 컴퓨터] 
    # value: 감염시키는데 걸리는 시간
    matrix = [[0] * count_com for _ in range(count_com)]
    visited = [False] * count_com


    for _ in range(dependency):
        a_com, b_com, time = map(int, input().split())
        matrix[a_com-1][b_com-1] = time
    
    for i in range(count_com):
        for j in range(count_com):
            if i == j:
                matrix[i][j] = 0
            elif matrix[i][j] == 0:
                matrix[i][j] = 999999999
    
    # print_matrix(matrix)

    d_hacked = hacked
    for i in range(count_com):
        min_cost = 999999999
        min_line = -1
        
        for i in range(count_com):
            if matrix[i][d_hacked] != 0 and not visited[i]:
                if min_cost > matrix[i][d_hacked]:
                    min_cost = matrix[i][d_hacked]
                    min_line = i
        if min_line != -1:
            visited[min_line] = True

        for i in range(count_com):
            if matrix[i][min_line] + min_cost < matrix[i][d_hacked]:
                matrix[i][d_hacked] = matrix[i][min_line] + min_cost

    # print_matrix(matrix)
    total_hacked = 0
    total_time = 0
    for i in range(count_com):
        if visited[i]:
            total_hacked += 1
    
    for i in range(count_com):
        # print(i, matrix[i][hacked])
        if matrix[i][hacked] != 999999999:
            total_time = max(total_time, matrix[i][hacked])
            # print(total_time)
    print(total_hacked + 1, total_time)


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
