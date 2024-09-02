import sys
input = sys.stdin.readline

build_cnt, left_see, right_see = map(int, input().split())
building_max_height = 0
building_list = []

is_left_big_side = True
if left_see >= right_see:
    building_max_height = left_see
else:
    building_max_height = right_see
    is_left_big_side = False

def check_build_cnt(build_cnt):
    if (build_cnt < 0):
        print("-1")
        exit(0)

if is_left_big_side:
    build_cnt -= left_see
    check_build_cnt(build_cnt)
    for L_idx in range(1, left_see + 1):
        building_list.append(L_idx)
    build_cnt -= (right_see - 1)
    check_build_cnt(build_cnt)
    for R_idx in range(right_see - 1, 0, -1):
        building_list.append(R_idx)
    for i in range(build_cnt):
        building_list.insert(1, 1)
else:
    build_cnt -= (right_see)
    check_build_cnt(build_cnt)
    for R_idx in range(right_see, 0, -1):
        building_list.append(R_idx)
    build_cnt -= (left_see - 1)
    check_build_cnt(build_cnt)
    for L_idx in range(1, left_see):
        building_list.insert(L_idx - 1, L_idx)
    for i in range(build_cnt):
        building_list.insert(1, 1)


for building_idx in range(len(building_list)):
    if building_idx == len(building_list) - 1:
        print(building_list[building_idx])
    else:
        print(building_list[building_idx], end=" ")
