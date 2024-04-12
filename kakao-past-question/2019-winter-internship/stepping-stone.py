# def solution(stones, k):
#     answer = 0
#     success = True

#     while True:
#         i = 0
#         while i < len(stones):
#             steps = 0
#             if stones[i] > 0:
#                 stones[i] -= 1
#             else:
#                 # print("i: ", i, "stones: ", stones)
#                 for j in range(i + 1, len(stones)):
#                     if stones[j] == 0:
#                         steps += 1
#                     else:
#                         break
#                 if steps >= k - 1:
#                     success = False
#                     break
#                 i += steps
#             i += 1
        
#         if success == True:
#             answer += 1
#         if success == False:
#             break
#     return answer


# def solution(stones, k):
#     success_count = 0
#     while True:
#         print("stones: ", stones)
#         min_val = 1000000000
#         for i in range(len(stones)):
#             if stones[i] < min_val and stones[i] != 0:
#                 min_val = stones[i]
#         for i in range(len(stones)):
#             if stones[i] != 0:
#                 stones[i] -= min_val
        
#         success_count += min_val
#         max_step, i = 0, 0
#         while i < len(stones):
#             if stones[i] == 0:
#                 step = 1
#                 for j in range(i + 1, len(stones)):
#                     if stones[j] == 0:
#                         step += 1
#                     else:
#                         break
#                 if step > max_step:
#                     max_step = step
#                 i += step
#             else:
#                 i += 1
        
#         if max_step >= k:
#             break
#     return success_count

def check_cross(list, k):
    count = 0
    for i in range(len(list)):
        if list[i] == 0:
            count += 1
        else:
            count = 0
        if count >= k:
            return False
    return True

def solution(stone, k):
    try_count = 0
    list = [0 for i in range(len(stone))]
    while True:
        max_stone = max(stone)
        print("max_stone: ", max_stone, "stone: ", stone, "list: ", list)
        for i in range(k):
            if stone[i] == max_stone:
                list[i] = 1
                stone[i] = 0

        if check_cross(list, k) == True:
            break
        else:
            try_count += 1
    print(stone)
    print(try_count)




print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3