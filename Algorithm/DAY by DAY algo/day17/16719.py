# import sys

# st = sys.stdin.readline().strip()
# length = len(st)
# visited = [False] * length

# def small_loc1(loc):
#     small = 'Z'
#     loca = loc
#     for i in range(loc, length):
#         if (st[i] < small and visited[i] == False):
#             small = st[i]
#             loca = i
#     return loca

# def small_loc2(loc):
#     small = 'Z'
#     loca = loc
#     for i in range(loc, length):
#         if (st[i] <= small and visited[i] == False):
#             small = st[i]
#             loca = i
#     return loca

# def visited_clear(loc):
#     for i in range(loc, length):
#         if (visited[i] == False):
#             return False
#     return True

# dict = {}
# loc = small_loc1(0)
# start = loc
# list = []

# while(visited_clear(0) != True):
#     # print(dict)
#     if (visited_clear(loc) == False and loc != -1):
#         dict[loc] = st[loc]
#         if (visited[loc] == False):
#             for key in sorted(dict):
#                 print(dict[key], end="")
#             print()
#         visited[loc] = True
#         loc = small_loc1(loc + 1)
#     elif (visited_clear(start) == False):
#         loc = small_loc2(start)
#     else:
#         start = small_loc1(0)
#         loc = start



import sys
input =sys.stdin.readline  

arr = list(input().rstrip()) 
result = [""]*len(arr)

def solution(start,arr):
    if not arr:
        return
    min_val = min(arr)
    temp = arr.index(min_val)
    
    result[start + temp] = min_val
    print("".join(result))
    solution(start+temp+1,arr[temp+1:]) 
    solution(start,arr[:temp])

solution(0,arr)