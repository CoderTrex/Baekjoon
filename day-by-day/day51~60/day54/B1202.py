import heapq
import sys
input = sys.stdin.readline
jewelry_cnt, bag_cnt = map(int, input().split())

jewelrys = []
for _ in range(jewelry_cnt):
    heapq.heappush(jewelrys, list(map(int, input().split())))

bag_max_weights = []
for _ in range(bag_cnt):
    bag_max_weights.append(int(input()))

bag_max_weights.sort()
max_value = 0
temp = []

for bag_max_weight in bag_max_weights:
    while jewelrys and jewelrys[0][0] <= bag_max_weight:
        # -로 넣는 이유는 값중에 최대값을 빼야함
        heapq.heappush(temp, -heapq.heappop(jewelrys)[1])
    if temp:
        max_value -= heapq.heappop(temp)
    elif not jewelrys:
        break

print(max_value)