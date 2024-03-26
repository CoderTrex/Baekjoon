
# 과제를 처음 순서대로 정렬
# 현재 과제 수행시간과 다음 과제의 시작 시간을 비교
# case1. 과제를 다 마칠 수 있다. 과제를 다 진행하고 남는 시간이 있는지 확인
        # 남는 시간이 있다면 stack에 있는 과제를 진행한다.
# case2. 과제를 다 마칠 수 없다. 과제를 진행하다가 시간이 부족하면 다음 과제로 넘어간다.
        #  남은 과제는 [과목명, 남은 시간] 형태로 stack에 저장한다.

import datetime as dt

def solution(plans):
    answer = []
    plans = sorted(plans, key=lambda x: x[1])
    stack = []

    for i in range(len(plans)):
        start_time = dt.datetime.strptime(plans[i][1], "%H:%M")  
        num = int(plans[i][2])
        endtime = start_time + dt.timedelta(minutes=num)  
        print(endtime.time())  
        if i == len(plans) - 1:
            answer.append(plans[i][0])
            break
        
        next_start_time = dt.datetime.strptime(plans[i+1][1], "%H:%M")  
        
        if endtime <= next_start_time:
            answer.append(plans[i][0])
            sparetime = next_start_time - endtime
            while stack:
                if (sparetime <= 0):
                    sparetime = 0
                    break
                leftplan = stack.pop()
                if (sparetime >= leftplan[1]):
                    answer.append(leftplan[0])
                else:
                    stack.append([leftplan[0], leftplan[1] - sparetime])
                    sparetime -= leftplan[1]
            if stack:
                stack[-1][1] -= sparetime
        else:
            stack.append([plans[i][0], endtime - next_start_time])
    
    for leftplan in stack:
        answer.append(leftplan[0])
    
    return answer
