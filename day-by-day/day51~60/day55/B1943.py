import sys
input = sys.stdin.readline
TK_cnt = 3


for _ in range(TK_cnt):
    coin_category_cnt = int(input())
    # 코인을 가지고 있는 주머니
    coin_bucket = {}
    # 코인 총합
    coin_sum = 0

    for _ in range(coin_category_cnt):
        coin_value, coin_cnt = map(int, input().split())
        coin_sum += coin_value * coin_cnt
        coin_bucket[coin_value] = coin_cnt

    if coin_sum % 2 != 0:
        print(0)
        continue

    # 목표의 절반 값만 찾으면됨
    coin_sum = int(coin_sum//2)
    dp_coin_values = [1] + [0] * coin_sum
    
    for coin in coin_bucket:
        for money in range(coin_sum, coin-1, -1): # 뒤에서 부터 값을 찾음
            if dp_coin_values[money - coin]: # TRUE인 곳에서만 값을 갱신해줌
                for coin_cnt in range(coin_bucket[coin]): # 코인의 값에 대한 개수만큼 for문을 돌아줌
                    if money + coin * coin_cnt <= coin_sum: # coin_sum보다 작은 값에 대해서만 처리
                        dp_coin_values[money + coin * coin_cnt] = 1

    print(dp_coin_values[coin_sum])