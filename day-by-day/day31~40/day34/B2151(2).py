from collections import deque

size = int(input())
matrix = [list(input()) for _ in range(size)]

# 맵의 기본적인 정보 저장
start, end = (0, 0), (0, 0)
list_mirror = []
find = False
for i in range(size):
    for j in range(size):
        if matrix[i][j] == '#':
            if find == False:
                start = (i, j)
                matrix[i][j] = '*'
                find = True
            else:
                end = (i, j)
        if matrix[i][j] == '!':
            list_mirror.append((i, j))

# (top과 bottom), (left와 right)만의 조합은 필요한 거울의 개수는 짝수
# 이외의 2개의 조합은 홀수
top, bottom, left, right = 1, 1, 0, 0
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

def check_mirror():
    dq = deque()
    step = 0
    dq.append((start, start_loc, step))
    while dq:
        temp = deque()
        # print(dq)
        
        while dq:
            current, current_loc, step = dq.popleft()
            if (step == 0):
                y, x = current
                up_flag, down_flag = False, False
                for i in range(1, size + 1):
                    if y - i >= 0 and up_flag == False:
                        if matrix[y-i][x] == '*':
                            up_flag = True
                        elif matrix[y-i][x] == '!':
                            temp.append(((y-i, x), 0, step+1))
                        elif matrix[y-i][x] == '#':
                            return step
                    else:
                        up_flag = True
                    if y + i < size and down_flag == False:
                        if matrix[y+i][x] == '*':
                            down_flag = True
                        elif matrix[y+i][x] == '!':
                            temp.append(((y+i, x), 0, step+1))
                        elif matrix[y+i][x] == '#':
                            return step
                    else:
                        down_flag = True
                y, x = current
                left_flag, right_flag = False, False
                for i in range(1, size + 1):
                    if x - i >= 0 and left_flag == False:
                        if matrix[y][x-i] == '*':
                            left_flag = True
                        elif matrix[y][x-i] == '!':
                            temp.append(((y, x-i), 1, step+1))
                        elif matrix[y][x-i] == '#':
                            return step
                    else:
                        left_flag = True
                    if x + i < size and right_flag == False:
                        if matrix[y][x+i] == '*':
                            right_flag = True
                        elif matrix[y][x+i] == '!':
                            temp.append(((y, x+i), 1, step+1))
                        elif matrix[y][x+i] == '#':
                            return step
                    else:
                        right_flag = True
            elif (current_loc == 0):
                y, x = current
                left_flag, right_flag = False, False
                for i in range(1, size + 1):
                    if x - i >= 0 and left_flag == False:
                        if matrix[y][x-i] == '*':
                            left_flag = True
                        elif matrix[y][x-i] == '!':
                            temp.append(((y, x-i), 1, step+1))
                        elif matrix[y][x-i] == '#':
                            return step
                    else:
                        left_flag = True
                    if x + i < size and right_flag == False:
                        if matrix[y][x+i] == '*':
                            right_flag = True
                        elif matrix[y][x+i] == '!':
                            temp.append(((y, x+i), 1, step+1))
                        elif matrix[y][x+i] == '#':
                            return step
                    else:
                        right_flag = True
            elif (current_loc == 1):
                y, x = current
                up_flag, down_flag = False, False
                for i in range(1, size + 1):
                    if y - i >= 0 and up_flag == False:
                        if matrix[y-i][x] == '*':
                            up_flag = True
                        elif matrix[y-i][x] == '!':
                            temp.append(((y-i, x), 0, step+1))
                        elif matrix[y-i][x] == '#':
                            return step
                    else:
                        up_flag = True
                    if y + i < size and down_flag == False:
                        if matrix[y+i][x] == '*':
                            down_flag = True
                        elif matrix[y+i][x] == '!':
                            temp.append(((y+i, x), 0, step+1))
                        elif matrix[y+i][x] == '#':
                            return step
                    else:
                        down_flag = True
        
        dq = temp

print(check_mirror())







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