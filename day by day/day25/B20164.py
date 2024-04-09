number = int(input())

number_list = []
dict = {}

def check_odd(number):
    if number % 2 == 1:
        return 1
    else:
        return 0

def check_dict(number, dict, dict_number):
    if dict_number not in dict:
        dict[dict_number] = number
    else:
        dict[dict_number] += number

def dfs(number, dict, dict_number, rtime):
    if len(str(number)) == 1:
        num = check_odd(number)
        check_dict(num, dict, dict_number)
    
    elif len(str(number)) == 2:
        number_one = int(str(number)[0])
        number_two = int(str(number)[1])

        temp_number = 0
        temp_number += check_odd(number_one)
        temp_number += check_odd(number_two)

        check_dict(temp_number, dict, dict_number)
        temp_number = number_one + number_two
        dfs(temp_number, dict, dict_number, 1)

    else:
        for i in range(1, len(str(number)) - 1):  
            for j in range(i+1, len(str(number))):
                if rtime != 0:
                    temp_number = dict[dict_number]
                else:
                    temp_number = 0
                dict_number = int(i * (100000) + (rtime * i) + j)

                number_one = int(str(number)[:i])
                number_two = int(str(number)[i:j])
                number_three = int(str(number)[j:])
                
                temp_number += check_odd(number_one)
                temp_number += check_odd(number_two)
                temp_number += check_odd(number_three)
                
                check_dict(temp_number, dict, dict_number)
                temp_number = number_one + number_two + number_three
                
                print("{0}: {1} / {2}".format(dict_number, temp_number, dict))
                dfs(temp_number, dict, dict_number, 1)

dfs(number, dict, 0, 0)
print(dict)