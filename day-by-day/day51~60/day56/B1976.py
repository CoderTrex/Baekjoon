# from collections import deque

city_cnt = int(input())
tour_cnt = int(input())

parent = [i for i in range(city_cnt)]

def union(i, j):
    i = find(i)
    j = find(j)
    if i < j:
        parent[j] = i
    else:
        parent[i] = j

def find(num):
    if parent[num] == num:
        return num
    parent[num] = find(parent[num])
    return parent[num]

connection_map = [[] for _ in range(city_cnt)]
for i in range(city_cnt):
    connection_map[i] = list(map(int, input().split()))
tour_list = list(map(int, input().split()))


for i in range(len(connection_map)):
    for j in range(len(connection_map[i])):
        if connection_map[i][j] == 1:
            union(parent[i], parent[j])

for i in range(len(tour_list)):
    tour_list[i] -= 1

temp = find(tour_list[0])

def answer(que, temp):
    for i in range(len(que)):
        if find(que[i]) != temp:
            return "NO"
    return "YES"

print(answer(tour_list, temp))

