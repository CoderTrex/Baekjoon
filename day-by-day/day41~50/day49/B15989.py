test_case = int(input())

target_nums = []
for _ in range(test_case):
    target_nums.append(int(input()))
max_num = max(target_nums)

test_cast_sum = [0] * (max_num+1)
test_cast_sum[1] = 1
test_cast_sum[2] = 2
test_cast_sum[3] = 3
test_cast_sum[4] = 4
test_cast_sum[5] = 5
test_cast_sum[6] = 7
test_cast_sum[7] = 8


for i in range(8, max_num+1):
    test_cast_sum[i] = 1 + i//2 + test_cast_sum[i-3]

for target_num in target_nums:
    print(test_cast_sum[target_num])