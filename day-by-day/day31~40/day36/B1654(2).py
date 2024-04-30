K, N = map(int, input().split())
A = []
for i in range(K):
    A.append(int(input()))
start, end = 1, max(A) 

while start <= end: 
    mid = (start + end) // 2 
    count = 0 
    for i in A:
        count += i // mid 
        
    if count >= N: 
        start = mid + 1
    else:
        end = mid - 1
print(end)