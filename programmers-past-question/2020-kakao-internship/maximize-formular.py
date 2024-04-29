def solution(expression):
    numbers = []
    operators = []

    num = 0
    for i in expression:
        if i.isdigit():
            num = num * 10 + int(i)
        else:
            operators.append(i)
            numbers.append(num)
            num = 0
    numbers.append(num)
    
    operators_order = [["*", "+", "-"], ["*", "-", "+"], ["+", "*", "-"], ["+", "-", "*"], ["-", "*", "+"], ["-", "+", "*"]]
    max_value = -1

    for order in operators_order:
        temp_numbers = numbers.copy()
        temp_operators = operators.copy()
        for order_operator in order:
            i = 0
            while i < len(temp_operators):
                if temp_operators[i] == order_operator:
                    if order_operator == "*":
                        temp_numbers[i] = temp_numbers[i] * temp_numbers[i+1]
                    elif order_operator == "+":
                        temp_numbers[i] = temp_numbers[i] + temp_numbers[i+1]
                    else:
                        temp_numbers[i] = temp_numbers[i] - temp_numbers[i+1]
                    temp_numbers.pop(i+1)
                    temp_operators.pop(i)
                else:
                    i += 1
        if abs(temp_numbers[0]) > max_value:
            max_value = abs(temp_numbers[0])    
    return max_value

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300