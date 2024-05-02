# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

# 1*1 1*2 1*3 1*4 1*5
# 2*1 2*2 2*3 2*4 2*5
# 3*1 3*2 3*3 3*4 3*5
# 4*1 4*2 4*3 4*4 4*5
# 5*1 5*2 5*3 5*4 5*5

# 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 8, 8, 9, 10, 10, 12, 12, 15, 16, 20, 20, 25

# 1*1 1*2 1*3
# 2*1 2*2 2*3
# 3*1 3*2 3*3


import sys
input = sys.stdin.readline
size = int(input())
target = int(input())
count = 0

mid = size

if target < mid:
    for i in range(1, size*2):
        if i < mid:
            range_num = i + 1
            start = 1
            end = range_num - 1
            while end > 0:
                count += 1
                if count == target:
                    print(start * end)
                    break
                end -= 1
                start += 1

if target >= mid:
    range_num = size
    start = 1
    end = range_num
    while end > 0:
        count += 1
        if count == target:
            print(start * end)
            break
        start += 1
        end -= 1

    else:
        range_num = size - (i - mid)
        start = 1 + i - mid
        end = size
        while start <= size:
            count += 1
            if count == target:
                print(start * end)
                break
            start += 1
            end -= 1