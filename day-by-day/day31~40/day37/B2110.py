import sys
# N 집의 개수, C 공유기의 개수
N, C = map(int, input().split())
house = []

for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
# print("house:", house)
if C == 2:
    print(max(house) - min(house))
else:
    # 1. 처음과 끝을 기준으로 가운데 값을 찾는다. 값을 (start, end, distance)로 넣는다. -> 처음 이후에는 deque에서 distance가 가장 큰 값을 찾는다.
    # 2. 가운데 값을 기준으로 왼쪽과 오른쪽을 나누어 가장 가까운 집을 찾고, 해당 집이 binary_mid 값이 된다. 또한 나중에 탐색을 위해 deque에 (start, end, distance)를 넣는다.
    # 3. binary_mid 값을 기준으로 왼쪽과 오른쪽 중에 더 거리가 많은 곳을 기준으로 처음과 끝을 찾는다.
    # 4. 1~3을 반복한다.

    list_distance = []
    list_distance.append((0, N-1, house[N-1] - house[0]))
    count = 2
    min_dist = 999999999
    while count < C:
        index = 0
        max_distance = list_distance[0][2]
        for i in range(1, len(list_distance)):
            if list_distance[i][2] > max_distance:
                max_distance = list_distance[i][2]
                index = i
        
        start, end, distance = list_distance.pop(index)
        binary_mid = (house[start] + house[end]) // 2

        if binary_mid in house:
            list_distance.append((start, binary_mid, binary_mid - house[start]))
            list_distance.append((binary_mid, end, house[end] - binary_mid))
        else:
            left = start
            right = end
            mid = (left + right) // 2
            recur = -1
            while True:
                if recur == mid:
                    break
                else:
                    recur = mid
                if abs(house[mid] - binary_mid) > abs(house[mid+1] - binary_mid):
                    left = mid + 1
                elif abs(house[mid] - binary_mid) > abs(house[mid-1] - binary_mid):
                    right = mid - 1
                else:
                    break
                mid = (left + right) // 2
            
            distance = house[mid] - house[start]
            if distance == 1:
                min_dist = 1
                break
            if distance < min_dist:
                min_dist = distance
            list_distance.append((start, mid, distance))
            
            distance = house[end] - house[mid]
            if distance == 1:
                min_dist = 1
                break
            if distance < min_dist:
                min_dist = distance
            list_distance.append((mid, end, distance))
        count += 1
    print(min_dist)
