# 입력 예시
input_data = \
"""6 8 2
3 2 6 3 1 2 9 7
9 7 8 2 1 4 5 3
5 9 2 1 9 6 1 8
2 1 3 8 6 3 9 2
1 3 2 8 7 9 2 1
4 5 1 9 8 2 1 3
2 3
"""



file2_path = "C:/Users/admin/project/algorithm/day by day/day31~40/day31/B17470.py"
import subprocess

def execute_other_file():
    # 실행할 파일의 경로와 명령어를 리스트로 정의합니다.
    command = ['C:/Users/admin/anaconda3/python.exe', "C:/Users/admin/project/algorithm/day-by-day/day31~40/day32/a.py"]
    command2 = ['C:/Users/admin/anaconda3/python.exe', "C:/Users/admin/project/algorithm/day-by-day/day31~40/day32/B17470.py"]

    # subprocess 모듈을 사용하여 다른 파일 실행 및 입력 전달
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)

    process2 = subprocess.Popen(command2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout2, stderr2 = process2.communicate(input=input_data)
    flag = True
    # 실행 결과가 같은지 비교합니다.
    if stdout and stdout2:
        for line1, line2 in zip(stdout.splitlines(), stdout2.splitlines()):
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    flag = False
                    print("결과가 다릅니다.")
                    print("===========")
                    print(stdout)
                    print("===========")
                    print(stdout2)
                    break
            if not flag:
                break
    
    if flag:
        print("결과가 같습니다.")
    else:
        print("결과가 다릅니다.")
    if stderr:
        print("표준 에러:")
        print(stderr)
if __name__ == "__main__":
    # 입력을 다른 파일(b.py)로 전달하고 실행합니다.
    execute_other_file()
