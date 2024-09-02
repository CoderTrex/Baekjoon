RB_cnt = int(input())
RB_str = str(input())
answer = 0

# 앞에 B값을 몰아넣는 경우
BFront_cnt = 0
Flag = False
for i in range(RB_cnt):
    if (i == 0 or Flag):
        if (RB_str[i] == 'B'):
            Flag = True
        else:
            Flag = False
    else:
        if (RB_str[i] == 'B'):
            BFront_cnt += 1

answer = BFront_cnt

# 앞에 R값을 몰아넣는 경우
RFront_cnt = 0
Flag = False
for i in range(RB_cnt):
    if (i == 0 or Flag):
        if (RB_str[i] == 'R'):
            Flag = True
        else:
            Flag = False
    else:
        if (RB_str[i] == 'R'):
            RFront_cnt += 1

if (RFront_cnt < answer):
    answer = RFront_cnt

# 뒤에 B값을 몰아넣는 경우
BBack_cnt = 0
Flag = False
for i in range(RB_cnt-1, -1, -1):
    if (i == RB_cnt - 1 or Flag):
        if (RB_str[i] == 'B'):
            Flag = True
        else:
            Flag = False
    else:
        if (RB_str[i] == 'B'):
            BBack_cnt += 1

if (BBack_cnt < answer):
    answer = BBack_cnt

# 뒤에 R값을 몰아넣는 경우
RBack_cnt = 0
Flag = False
for i in range(RB_cnt-1, -1, -1):
    if (i == RB_cnt - 1 or Flag):
        if (RB_str[i] == 'R'):
            Flag = True
        else:
            Flag = False
    else:
        if (RB_str[i] == 'R'):
            RBack_cnt += 1

if (RBack_cnt < answer):
    answer = RBack_cnt

print(answer)