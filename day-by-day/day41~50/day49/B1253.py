# 시간 초과 코드
# number_count = int(input())

# numbers = list(map(int, input().split()))
# good_numbers = []

# for i in range(number_count):
#     for j in range(number_count):
#         if i == j:
#             continue
#         good_number_cp = numbers.copy()
#         good_number_cp.remove(numbers[i])
#         good_number_cp.remove(numbers[j])
#         if numbers[i] + numbers[j] in good_number_cp:
#             good_numbers.append(numbers[i] + numbers[j])

# print(len(good_numbers) // 2)


# 투 포인터 
number_count = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for i in range(number_count):
    start = 0
    end = number_count - 1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        if numbers[start] + numbers[end] == numbers[i]:
            count += 1
            break
        elif numbers[start] + numbers[end] > numbers[i]:
            end -= 1
        else:
            start += 1

print(count)
