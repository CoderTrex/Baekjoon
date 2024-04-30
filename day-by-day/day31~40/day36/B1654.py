N, K = map(int, input().split())


A = []
max_value = 0
min_value = 999999999999
for i in range(N):
    A.append(int(input()))
    if max_value < A[i]:
        max_value = A[i]
    if min_value > A[i]:
        min_value = A[i]


def check_answer(num1, num2):
    count1 = 0
    count2 = 0
    for i in range(N):
        count1 += A[i] // num1
        count2 += A[i] // num2
    if count1 == K and count2 < K:
        return 1
    elif count1 < K: # 너무 큰 값이 들어와 결과가 작음
        return 2
    else:
        return 3


if (N == K):
    print(min_value)
else:
    binary_min = 1
    binary_max = max_value
    answer = 0
    while True:
        count = 0
        mid = (binary_min + binary_max) // 2
        for i in range(N):
            count += A[i] // mid
        if count > K:
            binary_min = mid + 1
        elif count < K:
            binary_max = mid - 1
        else:
            answer = mid
            break
    
    # print("answer: ", answer, " binary_max: ", binary_max)
    while True:
        new_count = 0
        new_mid = (answer + binary_max) // 2
        # print("new_mid: ", new_mid, " binary_max: ", binary_max)
        if (check_answer(new_mid, new_mid + 1) == 1):
            answer = new_mid
            break
        elif (check_answer(new_mid, new_mid + 1) == 2):
            binary_max = new_mid - 1
        else:
            answer = new_mid + 1
    print(answer)