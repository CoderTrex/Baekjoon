import math
def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        x, y = ball
        up, down, left, right = 0, 0, 0, 0
        
        # 4방향으로만 확인하면 됨

        # 위로 확인
        if startX == x:
            continue
        else:
            y1 = (n - startY) + (n - y)
            y2 = startY + y
            if y1 < y2:
                up = (x - startX) ** 2 + y1 ** 2
            else:
                up = (x - startX) ** 2 + y2 ** 2
        
        # 아래로 확인
        if startX == x:
            continue
        else:
            y1 = startY + y
            y2 = (n - startY) + (n - y)
            if y1 < y2:
                down = (x - startX) ** 2 + y1 ** 2
            else:
                down = (x - startX) ** 2 + y2 ** 2

                


    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])) #, [52, 37, 116])) # [52, 37, 116]