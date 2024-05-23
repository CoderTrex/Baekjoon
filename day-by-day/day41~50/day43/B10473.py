# 25.0 100.0
# 190.0 57.5
# 4
# 125.0 67.5
# 75.0 125.0
# 45.0 72.5
# 185.0 102.5

import heapq

X, Y = map(float, input().split())
TX, TY = map(float, input().split())
cannon = int(input())
cannons = [list(map(float, input().split())) for _ in range(cannon)]
dist_matrix = [[0.0] * (cannon+2) for _ in range(cannon+2)]
time_matrix = [[0.0] * (cannon+2) for _ in range(cannon+2)]

my_speed = 5
cannon_speed = 25

def cal_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            num = round(matrix[i][j], 2)
            print({"{:.2f}".format(num)}, end=" ")
        print()

def make_matrix():
    for i in range(cannon+2):
        for j in range(cannon+2):
            if i == j:
                continue
            elif (i == 0) and (j == cannon+1):
                dist_matrix[i][j] = cal_distance(TX, TY, X, Y)
            elif (i == cannon+1) and (j == 0):
                dist_matrix[i][j] = cal_distance(X, Y, TX, TY)
            elif (j == 0):
                dist_matrix[i][j] = cal_distance(X, Y, cannons[i-1][0], cannons[i-1][1])
            elif (i == 0):
                dist_matrix[i][j] = cal_distance(X, Y, cannons[j-1][0], cannons[j-1][1])
            elif (j == cannon+1):
                dist_matrix[i][j] = cal_distance(cannons[i-1][0], cannons[i-1][1], TX, TY)
            elif (i == cannon+1):
                dist_matrix[i][j] = cal_distance(cannons[j-1][0], cannons[j-1][1], TX, TY)
            elif (i != 0) and (j != cannon+1):
                dist_matrix[i][j] = cal_distance(cannons[i-1][0], cannons[i-1][1], cannons[j-1][0], cannons[j-1][1])

make_matrix()
# print("dist_matrix")
# print_matrix(dist_matrix)

for i in range(cannon+2):
    for j in range(cannon+2):
        if i == j:
            continue
        if i == 0 or i == cannon+1 or j == 0 or j == cannon+1:
            time_matrix[i][j] = dist_matrix[i][j] / my_speed
        else:
            left = abs(dist_matrix[i][j] - 50)
            time_matrix[i][j] = 2 + left / my_speed


# print("time_matrix")
# print_matrix(time_matrix)

visited = [False] * (cannon+2)
visited[0] = True


