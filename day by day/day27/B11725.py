width = int(input())
height = int(input())
Ap = (input())

matrix = [[0 for i in range(width-1)] for j in range(height)]
for i in range(height):
    matrix[i] = list(map(str, input()))

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet1 = alphabet[:width]
alphabet2 = list(Ap)


for i in range(height):
    if matrix[i][0] != "?":
        for j in range(width - 1):
            if matrix[i][j] == "-":
                tmp = alphabet1[j]
                alphabet1[j] = alphabet1[j + 1]
                alphabet1[j + 1] = tmp
    else:
        break

for i in range(height-1, -1, -1):
    if matrix[i][0] != "?":
        for j in range(width - 1):
            if matrix[i][j] == "-":
                tmp = alphabet2[j]
                alphabet2[j] = alphabet2[j + 1]
                alphabet2[j + 1] = tmp
    else:
        break

flag = True
passport = False
question_line = []

i = 0
flag_change = False
while i < width - 1:
    if flag_change:
        question_line.append("*")
        flag_change = False
        i = i + 1
        continue
    if alphabet1[i] != alphabet2[i]:
        if alphabet1[i + 1] == alphabet2[i]:
            question_line.append("-")
            flag_change = True
            i = i + 1
        else:
            flag = False
            break
    else:
        question_line.append("*")
        i = i + 1

if flag == False:
    for i in range(width - 1):
        print("x", end="")
else:
    print("".join(question_line))