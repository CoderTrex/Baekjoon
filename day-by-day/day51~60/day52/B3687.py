test_count = int(input())
test_case = [int(input()) for _ in range(test_count)]

# large number는 
# 홀수라면 7과 1로만 구성하면 된다.
# 짝수라면 1로만 구성하면 된다.
def get_large_number(number):
    if number % 2 == 0:
        return "1" * (number // 2)
    else:
        return "7" + "1" * ((number - 3) // 2)

# small number는 1, 7, 4, 6, 8로만 구성하면 된다.
# 하지만 첫번째 자리가 아닌 경우에는 6 대신에 0을 사용해야 한다.
number_dp = [float("inf")] * 101
number_dp[2] = 1
number_dp[3] = 7
number_dp[4] = 4
number_dp[5] = 2
number_dp[6] = 6
number_dp[7] = 8

for i in range(8, 101):
    for j in range(2, i - 1):
        number_dp[i] = min(number_dp[i], int(str(number_dp[j]) + str(number_dp[i - j])))
        if j == 6:
            number_dp[i] = min(number_dp[i], int(str(number_dp[i - j]) + "0"))
            

for number in test_case:
    print(number_dp[number], get_large_number(number))