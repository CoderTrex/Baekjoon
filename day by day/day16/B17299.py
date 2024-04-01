import sys

N = int(sys.stdin.readline())
X = list(map(int, input().split()))

temp = [0] * 1000001
stack = []
result = [-1] * N

for k in X:
    temp[k] += 1

for i in range(N):
    while stack and temp[x[stack[-1]]] < temp[X[i]]:
        result[stack.pop()] = X[i]
    stack.append(i)

print(" ".join(map(str, result)))