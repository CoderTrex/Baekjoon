# 단순 점화식으로 구하기 -> 메모리 초과
# A, B = map(int, input().split())
# arr = {}
# arr[0] = 0

# binary_1_sum = 0
# step = 1
# for i in range(1, B + 1):
#     if i == 2 ** step:
#         step += 1
#     arr[i] = arr[i - 2 ** (step - 1)] + 1

# for i in range(A, B + 1):
#     binary_1_sum += arr[i]

# print(binary_1_sum)

# 비트연산자로 구하기 -> 시간 초과
# A, B = map(int, input().split())

# binary_1_sum = 0

# for i in range(A, B + 1):
#     count = 0
#     while i > 0:
#         i &= (i - 1) 
#         count += 1
#     binary_1_sum += count

# print(binary_1_sum)


# 누적합으로 구하기
A, B = map(int, input().split())
arr = [0 for _ in range(60)]
arr[1] = 1

for i in range(2, 60):
    arr[i] = arr[i - 1] * 2 + 2 ** (i - 1)

def binary_sum(n):
    if n == 0:
        return 0
    binary = bin(n)[2:]
    length = len(binary)
    count = 0
    for i in range(length):
        if binary[i] == '1':
            count += arr[length - i - 1]
            count += (n - 2 ** (length - i - 1) + 1)
            n -= 2 ** (length - i - 1)
    return count

print(binary_sum(B) - binary_sum(A - 1))
