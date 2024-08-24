# height, width = map(int, input().split())
# dig_matrix = []

# for i in range(height):
#     dig_matrix.append(list(map(int, input().split())))


# dig_value_matrix = [[0 for _ in range(width)] for _ in range(height)]
# dig_value_matrix[0][0] = dig_matrix[0][0]

# def print_matrix(matrix):   
#     for i in range(height):
#         print(' '.join(map(str, matrix[i])))
#     print()

# print()
# for hei in range(height):
#     if hei == 0:
#         for wid in range(width):
#             dig_value_matrix[hei][wid] = dig_matrix[hei][wid] + dig_value_matrix[hei][wid-1]
#     elif hei == height-1:
#         for wid in range(width):
#             dig_value_matrix[hei][wid] = max(dig_value_matrix[hei][wid], dig_matrix[hei][wid] + dig_value_matrix[hei-1][wid])
#     else:
#         dig_right_dp = [0 for _ in range(width)]
#         dig_left_dp = [0 for _ in range(width)]
#         for wid in range(width):
#             dig_value_matrix[hei][wid] = dig_matrix[hei][wid] + dig_value_matrix[hei-1][wid]
#             dig_left_dp[wid] = dig_value_matrix[hei][wid]
#             dig_right_dp[wid] = dig_value_matrix[hei][wid]
        
#         for wid in range(width):
#             dig_right_dp[wid] = max(dig_right_dp[wid], dig_right_dp[wid-1] + dig_matrix[hei][wid]) 
#         for wid in range(width-2, -1, -1):
#             dig_left_dp[wid] = max(dig_left_dp[wid], dig_left_dp[wid+1] + dig_matrix[hei][wid])
#         for wid in range(width):
#             dig_value_matrix[hei][wid] = max(dig_right_dp[wid], dig_left_dp[wid])
#     print_matrix(dig_value_matrix)
# print(dig_value_matrix[height-1][width-1])

import sys
input = sys.stdin.readline
MAX = float('inf')
height, width = map(int, input().split())
dig_matrix = [list(map(int, input().split())) for _ in range(height)]
dig_value_dp = [[-MAX]*width for _ in range(height)]

for i in range(width):
    if i == 0:
        dig_value_dp[0][i] = dig_matrix[0][i]
    else:
        dig_value_dp[0][i] = dig_value_dp[0][i-1] + dig_matrix[0][i]

for i in range(1, height):
    dig_left_dp, dig_right_dp = [-MAX]*width, [-MAX]*width
    dig_left_dp[0] = dig_value_dp[i-1][0] + dig_matrix[i][0]
    dig_right_dp[-1] = dig_value_dp[i-1][-1] + dig_matrix[i][-1]
    for j in range(1, width):
        dig_left_dp[j] = max(dig_left_dp[j-1], dig_value_dp[i-1][j]) + dig_matrix[i][j]
        dig_right_dp[-1-j] = max(dig_right_dp[-j], dig_value_dp[i-1][-1-j]) + dig_matrix[i][-1-j]
    for j in range(width):
        dig_value_dp[i][j] = max(dig_left_dp[j], dig_right_dp[j])
print(dig_value_dp[-1][-1])
