from collections import deque

size = int(input())
matrix = [list(input()) for _ in range(size)]

# 맵의 기본적인 정보 저장
start, end = (0, 0), (0, 0)
list_mirror = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] == '#':
            if start == (0, 0):
                start = (i, j)
            else:
                end = (i, j)
        if matrix[i][j] == '!':
            list_mirror.append((i, j))

# (top과 bottom), (left와 right)만의 조합은 필요한 거울의 개수는 짝수
# 이외의 2개의 조합은 홀수
top, left, bottom, right = 1, 2, 3, 4
def check_loc(loc):
    if (loc[0] == 0):
        return top
    if (loc[0] == size-1):
        return bottom
    if (loc[1] == 0):
        return left
    if (loc[1] == size-1):
        return right
start_loc = check_loc(start)
end_loc = check_loc(end)
isodd = (start_loc + end_loc) % 2 != 0

# 거울이 만나는지 확인하는 함수
def is_meet(start, end):
    s_x, s_y = start
    e_x, e_y = end
    if (s_x == e_x):
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        for i in range(s_y+1, e_y):
            if matrix[s_x][i] == '*':
                return False
        return True
    elif (s_y == e_y):
        if s_x > e_x:
            s_x, e_x = e_x, s_x
        for i in range(s_x+1, e_x):
            if matrix[i][s_y] == '*':
                return False
        return True
    return False


# 1. 짝수인 경우
# 자신의 위치에서 
















































# count = 0 # 총 거울의 개수

# # 거울의 개수가 짝수인 경우
# if (isodd != 0):
#     # 시작이 상하인지 좌우인지 확인
#     if (start_loc == top or start_loc == bottom):
#         isup = True
#     else:
#         isup = False
    
#     dq = deque()
#     dq.append((start[0], start[1], isup), (end[0], end[1], isup))
#     while dq:
#         if (is_meet(dq[0], dq[1])):
#             break
#         else:
#             count += 2
#             start_list, end_list = [], []
#             start_flag, end_flag = False, False
#             start_x, start_y, start_isup = dq[0]
#             end_x  , end_y  , end_isup   = dq[1]
#             if (isup):
#                 for i in range(1, size - 1):
#                     if matrix[dp[0] + i][dp[1]] == '*':
#                         break
    

    # 2. 시작점과 끝점이 좌우인 경우




# 5
# ***#*
# *.!.*
# *!.!*
# *.!.*
# *#***

# 5
# *#***
# *.!.*
# *!.!*
# *.!.*
# *#***

# 5
# *#***
# *!!.*
# **.!*
# *!!.*
# *#***