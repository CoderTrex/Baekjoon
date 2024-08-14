height, width = map(int, input().split())
board = [list(map(str ,input())) for _ in range(height)]
dp = [[0] * width for _ in range(height)]
max_size = 0

for i in range(height):
    for j in range(width):
        if board[i][j] == '1':
            dp[i][j] = 1
            if i > 0 and j > 0:
                dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            max_size = max(max_size, dp[i][j])

print(max_size ** 2)


# 4 4
# 0100
# 0111
# 1110
# 0010

# 4 5
# 01000
# 01111
# 11111
# 00100

# 5 5
# 01000
# 01111
# 11110
# 11111
# 00100