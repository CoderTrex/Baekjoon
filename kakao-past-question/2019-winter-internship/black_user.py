def solution(user_id, banned_id):
    answer = 0
    ban_list = {}
    num = 0
    for ban in banned_id:
        ban_list[num] = []
        for user in user_id:
            ban_word_len = len(ban)
            if len(user) != ban_word_len:
                continue
            for i in range(len(ban) + 1):
                if i == ban_word_len:
                    ban_list[num].append(user)
                    break
                if ban[i] == '*':
                    continue
                if ban[i] != user[i]:
                    break
        num += 1

    # print(ban_list)
    stacks = []
    for ban in ban_list[0]:
        lstack = []
        lstack.append(ban)
        stacks.append(lstack)
    
    for i in range(1, len(ban_list)):
        for s in stacks: 
            lstacks = []
        
            for ban in ban_list[i]:
                lstack = s.copy()
                if ban not in lstack:
                    lstack.append(ban)
                    lstacks.append(lstack)

            for lstack in lstacks:
                stacks.append(lstack)     

        for s in stacks[:]:
            if len(s) != i + 1:
                stacks.remove(s)
                continue
            # print("stacks: ", stacks)

    sort_stacks = []
    for s in stacks:
        s.sort()
        if s not in sort_stacks:
            sort_stacks.append(s)
    answer = len(sort_stacks)
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3