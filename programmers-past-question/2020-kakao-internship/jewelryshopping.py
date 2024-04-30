def solution(gems):
    answer = []
    gem_list = []
    for gem in gems:
        if gem not in gem_list:
            gem_list.append(gem)
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]) == [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5])