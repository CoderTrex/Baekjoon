# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

# 1*1 1*2 1*3 1*4 1*5
# 2*1 2*2 2*3 2*4 2*5
# 3*1 3*2 3*3 3*4 3*5
# 4*1 4*2 4*3 4*4 4*5
# 5*1 5*2 5*3 5*4 5*5

# 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 8, 8, 9, 10, 10, 12, 12, 15, 16, 20, 20, 25

# 1*1 1*2 1*3
# 2*1 2*2 2*3
# 3*1 3*2 3*3


# using namespace std;

# int N, k;

# int main(void)
# {
# 	cin.tie(NULL);
# 	ios::sync_with_stdio(false);
# 	cin >> N >> k;
# 	int f = 1, l = k, m;
# 	int res = 0;
# 	for (;;)
# 	{
# 		if (f > l) break;
# 		m = (f + l) / 2;
# 		int cnt = 0;
# 		for (int i = 1; i <= N; i++)
# 		{
# 			cnt += min(N, m / i);
# 		}
# 		if (cnt >= k)
# 		{
# 			res = m;
# 			l = m - 1;
# 		}
# 		else
# 		{
# 			f = m + 1;
# 		}
# 	}
# 	cout << res << '\n';
# 	return 0;
# }

import sys
input = sys.stdin.readline
N = int(input())
K = int(input())

first = 1
last = K
mid = 0

while first <= last:
    mid = (first + last) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, mid // i)
    if cnt >= K:
        res = mid
        last = mid - 1
    else:
        first = mid + 1

print(res)