N = int(input())
caleneder = [0] * 366

for _ in range(N):
    s_start, s_end = map(int, input().split(' '))

    for i in range(s_start, s_end + 1):
        caleneder[i] += 1

row = 0
col = 0
ans = 0
for i in range(366):
    if caleneder[i] != 0:
        row = max(row, caleneder[i])
        col += 1
    else:
        ans += row * col
        row = 0
        col = 0
ans += row * col
print(ans)