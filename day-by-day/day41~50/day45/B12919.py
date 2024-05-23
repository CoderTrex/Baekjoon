import sys
from collections import deque

S = input()
T = input()

# 1. A를 뒤에 추가
# 2. B를 뒤에 추가하고 뒤집기

# 방법: 
#   1. 1번과 2번을 둘 다 진행해서 문자열을 만든다. 
#   2. 해당 문자열이 T가 될 수 있는 문장인지 확인한다.
#   3. O: 더 진행 / X : 더 뻗어나가지 않는다.

dq = deque([S])

def check(st):
    flag = False
    if st in T:
        flag = True
    st2 = st[::-1]
    if st2 in T:
        flag = True
    return flag

# A
# BAABAAAAAB

cnt = 0
while True:
    temp = deque()
    if len(dq) == 0:
        print(0)
        exit()
    # print("=====================================")
    while dq:
        st = dq.popleft()
        # print("cnt: ", cnt , " st: ", st)
        if st == T:
            print(1)
            exit()
        if len(st) >= len(T):
            continue
        st1 = st + 'A'
        st2 = st + 'B'
        st2 = st2[::-1]
        # print("cnt: ", cnt , " st1: ", st1, " st2: ", st2)
        if check(st1):
            # print("append: ", st1)
            temp.append(st1)
        if check(st2):
            # print("append: ", st2)
            temp.append(st2)
    #     print("\n\n")
    # print("=====================================")
    cnt += 1
    dq = temp

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

answer = 0
def reverse_dfs(str1, target):
  global answer
  if len(str1) == len(target):
    if target == str1:
      answer = 1
    return
  if target[-1] == 'A':
    reverse_dfs(str1, target[:-1])
  if target[0] == 'B':
    #target = target
    reverse_dfs(str1, target[:0:-1])

reverse_dfs(s, t)
print(answer)