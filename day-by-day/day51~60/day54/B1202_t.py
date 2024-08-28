import sys
import heapq

input = sys.stdin.readline

jewelry_cnt, bag_cnt = map(int, input().split())
jewelry_list = []
for _ in range(jewelry_cnt):
    heapq.heappush(jewelry_list, list(map(int, input().split())))

bags_max_weight = []
for _ in range(bag_cnt):
    bags_max_weight.append(int(input()))

bags_max_weight.sort()
temp_bag = []
max_value = 0

for bag_max_weight in bags_max_weight:
    while jewelry_list and jewelry_list[0][0] <= bag_max_weight:
        heapq.heappush(temp_bag, -heapq.heappop(jewelry_list)[1])
    if temp_bag:
        print(temp_bag)
        max_value -= heapq.heappop(temp_bag)
        print(max_value)
    elif not jewelry_list:
        break

# print(max_value)