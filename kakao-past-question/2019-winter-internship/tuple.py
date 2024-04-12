def solution(s):
    answer = []
    i = 1
    tuple = []
    while i < len(s):
        if s[i] == '{':
            little_tuple = []
            start = i + 1
            while True:
                if s[i] == ',':
                    little_tuple.append(int(s[start:i]))
                    start = i + 1
                elif s[i] == '}':
                    little_tuple.append(int(s[start:i]))
                    break
                i += 1
            tuple.append(little_tuple)
        i += 1
    
    tuple.sort(key=lambda x: len(x))
    for tu in tuple:
        for t in tu:
            if t not in answer:
                answer.append(t)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2},{1}}")) # [1, 2, 3]
print(solution("{{20,111},{111}}")) # [111, 20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]



        # if s[i] != '{':
        #     print(s[i])
        #     little_tuple = []
        #     start = i
        #     end = i
        #     while s[i] != '}':
        #         if s[i + 1] == '}':
        #             little_tuple.append(int(s[start:i + 1]))
        #             answer.append(little_tuple)
        #             while s[i] != ',': i += 1
        #             break
        #         elif s[i] == ',':
        #             print(s[start:end], "start: ", start, "end: ", end, "i: ", i)
        #             little_tuple.append(int(s[start:end]))
        #             i += 1
        #             start = i
        #             end = i
        #         else:
        #             i += 1
        #             end = i