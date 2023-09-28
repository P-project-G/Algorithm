"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	68499	23536	17270	36.341%

그림포함 문제
링크
https://www.acmicpc.net/problem/2579
"""

stair = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(stair):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0]+s[1]
dp[2] = max(s[1]+s[2], s[0]+s[2])

for i in range(3,stair):
    dp[i] = max(dp[i-3] + s[i-1]+s[i], dp[i-2] + s[i])
print(dp[stair-1])