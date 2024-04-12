def solution(board, moves):
    answer = 0

    stack = []
    for i in range(len(moves)):
        
        for depth in range(len(board)):
            if board[depth][moves[i]-1] != 0:
                stack.append(board[depth][moves[i]-1])
                board[depth][moves[i]-1] = 0
                break
        
        while True:
            flag = False
            if len(stack) < 2:
                break
            for j in range(len(stack)-1):
                print(stack)
                if stack[j] == stack[j+1]:
                    stack.pop(j)
                    stack.pop(j)
                    answer += 2
                    flag = True
                    break
            if not flag:
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4