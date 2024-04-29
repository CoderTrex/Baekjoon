def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]

    left_hand = [3, 0]
    right_hand = [3, 2]
    dict_phone = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}

    for number in numbers:
        if number in left:
            answer += 'L'
            left_hand = dict_phone[number]
        elif number in right:
            answer += 'R'
            right_hand = dict_phone[number]
        else:
            loc_y, loc_x = dict_phone[number]
            left_y, left_x = left_hand
            right_y, right_x = right_hand
            left_distance = abs(loc_y - left_y) + abs(loc_x - left_x)
            right_distance = abs(loc_y - right_y) + abs(loc_x - right_x)
            if left_distance < right_distance:
                answer += 'L'
                left_hand = dict_phone[number]
            elif left_distance > right_distance:
                answer += 'R'
                right_hand = dict_phone[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = dict_phone[number]
                else:
                    answer += 'R'
                    right_hand = dict_phone[number]
    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")


# 1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5
# L  R  L  L  L  R  L  L  R  R  L
# L  R  L  L  R  L  L  L  R  R  L