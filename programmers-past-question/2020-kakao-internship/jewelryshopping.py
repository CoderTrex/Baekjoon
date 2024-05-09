# def solution(gems):
#     answer = []
#     gem_list = [[] for _ in range(len(gems))] # 보석의 종류를 저장하는 리스트
#     gem_count = [0 for _ in range(len(gems))] # 보석이 중복 없이 몇 개가 있는지 저장하는 리스트
#     gem_last = [0 for _ in range(len(gems))]  # 보석이 마지막으로 나온 위치를 저장하는 리스트
#     gem_dist = [0 for _ in range(len(gems))]  # 보석의 거리를 저장하는 리스트
    
#     max_jewelry = 0
#     answer = [0, len(gems) - 1]
#     for i in range(len(gems)):
#         for j in range(i + 1):
#             if gems[i] not in gem_list[j]:
#                 gem_list[j].append(gems[i])
#                 gem_count[j] = len(gem_list[j])
#                 gem_last[j] = i
#                 if max_jewelry <= gem_count[j]:
#                     max_jewelry = gem_count[j]
#                     gem_dist[j] = i - j
#     dist = gem_dist[0]
#     start = 0
#     for d in range(len(gem_dist)):
#         if gem_dist[d] < dist and gem_dist[d] != 0:
#             dist = gem_dist[d]
#             start = d
    
#     answer = [start + 1, start + dist + 1]

#     return answer


from collections import defaultdict, deque

def solution(gems):
    min_gems  = int(1e9)
    len_gems = len(gems) 
    n_gems = len(set(gems))
    end = 0
    temp = defaultdict(lambda : 0)
    for start, gem in enumerate(gems):
        
        # 어디까지 가야지 모든 보석을 포함하는지 확인하는 반복문 
        while len(temp) < n_gems and end < len_gems: 
            temp[gems[end]] += 1
            end += 1
        
        # 보석을 모두 포함하고, 최소 길이를 갱신하는 조건문
        if len(temp) == n_gems:
            if min_gems > end-start:
                min_gems = end-start
                result = [start+1, end]  

        # start 보석을 제거하는 조건문    
        temp[gem] -= 1
        if temp[gem] == 0:
            del(temp[gem])
    return result

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(["AA", "AB", "AC", "AA", "AC"])
# solution(["XYZ", "XYZ", "XYZ"])
# solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]) == [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5])