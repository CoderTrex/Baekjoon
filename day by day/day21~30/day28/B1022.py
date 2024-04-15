from cmath import sqrt

# r1: 세로 시작, c1: 가로 시작, r2: 세로 끝, c2: 가로 끝
r1, c1, r2, c2 = map(int, input().split())
max = 0

list = [r1**2, c1**2, r2**2, c2**2]
for li in list:
    if max < li:
        max = li

width, height = sqrt(max) * 2 + 1, sqrt(max) * 2 + 1
width, height = int(width.real), int(height.real)

m_width, m_height = c2 - c1 + 1, r2 - r1 + 1
matrix = [[0 for _ in range(m_width)] for _ in range(m_height)]

location = [width//2, height//2]

# 오른쪽 -> 위로 -> 왼쪽 -> 아래로
# 1(오) -> 1(위) -> 2(왼) -> 2(아) 
# -> 3(오) -> 3(위) -> 4(왼) -> 4(아) 
# -> 5(오) -> 5(위) -> 6(왼) -> 6(아) 와 같은 방식으로 반복 

repeat = int(sqrt(max).real + 1)
m_left = repeat + c1 - 1
m_top = repeat + r1 - 1
m_right = repeat + c2 - 1
m_bottom = repeat + r2 - 1
number = 1

def check_location(location):
    if  location[0] >= m_left and \
        location[0] <= m_right and \
        location[1] >= m_top and \
        location[1] <= m_bottom :
        return True
    return False

if 0 >= r1 and 0 <= r2 and 0 >= c1 and 0 <= c2:
    matrix[0 - r1][0 - c1] = number

for i in range(1, repeat+1):
    # 오른쪽
    move = i * 2 - 1
    if location[1] >= m_top and location[1] <= m_bottom: 
        for _ in range(move):
            number += 1
            location[0] += 1
            if  check_location(location):
                matrix[location[1] - repeat - r1 + 1][location[0] - repeat - c1 + 1] = number
    else:
        number += move
        location[0] += move
    
    # 위로
    if location[0] >= m_left and location[0] <= m_right:
        for _ in range(move):
            number += 1
            location[1] -= 1
            if  check_location(location):
                matrix[location[1] - repeat - r1 + 1][location[0] - repeat - c1 + 1] = number
    else:
        number += move
        location[1] -= move
    
    move = i * 2
    # 왼쪽
    if location[1] >= m_top and location[1] <= m_bottom:
        for _ in range(move):
            number += 1
            location[0] -= 1
            if  check_location(location):
                matrix[location[1] - repeat - r1 + 1][location[0] - repeat - c1 + 1] = number
    else:
        number += move 
        location[0] -= move

    # 아래로
    if location[0] >= m_left and location[0] <= m_right:
        for _ in range(move):
            number += 1
            location[1] += 1
            if  check_location(location):
                matrix[location[1] - repeat - r1 + 1][location[0] - repeat - c1 + 1] = number
    else:
        number += move 
        location[1] += move
max_len = len(str(number))

def print_matrix(matrix):
    for i in range(m_height):
        for j in range(m_width):
            sub = len(str(number)) - len(str(matrix[i][j]))
            if sub > 0:
                print(' ' * sub, end='')
            print(matrix[i][j], end=' ')
        print()

print_matrix(matrix)