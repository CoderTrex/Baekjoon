# 16x16 숫자 배열 생성
array_16x16 = [[i + j * 16 + 1 for i in range(16)] for j in range(16)]

# 배열 출력
for row in range(16):
    for col in range(16):
        print(array_16x16[row][col], end=' ')
    print()
