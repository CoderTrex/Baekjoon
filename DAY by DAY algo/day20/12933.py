from collections import deque

str = input()
generated = []
okay_flag = True

def check_used_duck(duck_list, index):
    for i in range(len(duck_list)-1,  -1, -1):
        if (len(duck_list[i]) == index):
            return i
    return -1

for i in range(len(str)):
    if (str[i] == 'q'):
        if (len(generated) == 0):
            d = deque()
            d.append('q')
            generated.append(d)
        else:
            i = check_used_duck(generated, 0)
            if (i == -1):
                d = deque()
                d.append('q')
                generated.append(d)
            else:
                generated[i].append('q')
    elif (str[i] == 'u'):
        if (len(generated) == 0):
            okay_flag = False
            break
        else:
            i = check_used_duck(generated, 1)
            if (i == -1):
                okay_flag = False
                break
            else:
                generated[i].append('u')
    elif (str[i] == 'a'):
        if (len(generated) == 0):
            okay_flag = False
            break
        else:
            i = check_used_duck(generated, 2)
            if (i == -1):
                okay_flag = False
                break
            else:
                generated[i].append('a')
    elif (str[i] == 'c'):
        if (len(generated) == 0):
            okay_flag = False
            break
        else:
            i = check_used_duck(generated, 3)
            if (i == -1):
                okay_flag = False
                break
            else:
                generated[i].append('c')
    elif (str[i] == 'k'):
        if (len(generated) == 0):
            okay_flag = False
            break
        else:
            i = check_used_duck(generated, 4)
            if (i == -1):
                okay_flag = False
                break
            else:
                generated[i].clear()

if okay_flag == False:
    print(-1)
else:
    cnt = 0
    for i in range(len(generated)):
        if (len(generated[i]) == 0):
            cnt += 1
        else:
            cnt = -1
            break
    print(cnt if cnt > 0 else -1)