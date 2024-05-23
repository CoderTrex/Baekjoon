from itertools import permutations
n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))

def dfs(st):
    if len(st) == m:
        print(" ".join(map(str, st)))
        return
    for i in range(1, n+1):
        if i not in st:
            st.append(i)
            dfs(st)
            st.pop()

dfs([])
