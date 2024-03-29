N, R = map(int, input().split())
arr = [[0 for i in range(2**N)] for j in range(2**N)]

for i in range(2**N):
    st = input().split()
    for j in range(2**N):
        arr[i][j] = int(st[j])

# 1번: 상하반전 -> 배열 안에서 진행
# 2번: 좌우반전 -> 배열 안에서 진행
# 3번: 오른쪽 90도 회전 -> 배열 안에서 진행
# 4번: 왼쪽 90도 회전 -> 배열 안에서 진행
# 5번: 상하 반전 -> 배열 안에서 진행
# 6번: 좌우 반전 -> 배열 안에서 진행
# 7번: 오른쪽 90도 회전 -> 배열 안에서 진행
# 8번: 왼쪽 90도 회전 -> 배열 안에서 진행

for _ in range(R):
    cal, l = map(int, input().split()) # l은 배열의 크기로 2^l

    rl = pow(2, N)
    ll = pow(2, l)
    ll_half = pow(2, l - 1)

    if cal == 1:
        for j in range(0, rl, ll): # 세로값
            for i in range(ll_half): # 작은 범위내의 세로값
                for k in range(0, rl, 1): # 가로값
                    arr[j+i][k], arr[j + ll - i - 1][k] = arr[j + ll - i - 1][k], arr[j + i][k]
    elif cal == 2:
        for i in range(0, rl): # 세로값
            for j in range(0, rl, ll_half): # 가로가 적용되는 범위
                for k in range(0, ll_half, 1):
                    arr[i][k], arr[i][j + ll - k - 1] = arr[i][j + ll - k - 1], arr[i][k]



for i in range(2**N):
    for j in range(2**N):
        print(arr[i][j], end=' ')
    print()