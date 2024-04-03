schedule_count = int(input())
schedule = []
schedule_day = []
calaendar = [[0 for i in range(365)] for j in range(1000)]

def check_line(line, start, end):
    for i in range(start, end):
        if line[i] != 0:
            return False
    return True

for i in range(schedule_count):
    schedule.append(list(map(int, input().split())))

for i in range(schedule_count):
    s_start = schedule[i][0]
    s_end = schedule[i][1]

    for i in range(s_start, s_end):
        if schedule_day[i] == 0:
            schedule_day[i] = 1
    for i in range(1000):
        flag = check_line(calaendar[i], s_start, s_end)
        if flag:
            for j in range(s_start, s_end):
                calaendar[i][j] = 1
            break
