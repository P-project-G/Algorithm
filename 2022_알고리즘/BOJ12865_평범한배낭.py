import sys
input = sys.stdin.readline

# 물건 수 n
# 들 수 있는 무게 k
n, k =map(int,input().split())

# 인덱스 맞추기 위해 0,0 추가
backpag = [[0,0]]

for _ in range (n):
    # w = 무게
    # v = 가치
    w,v = map(int,input().split())
    backpag.append([w,v])

# n개, 0 ~ 들 수 있는 가치 의 2차원 dp용 배열 생성
dp = [ [0]*(k+1) for _ in range (n+1) ]

for i in range (1, n+1):
    for j in range (1, k+1):
        weight = backpag[i][0]
        value = backpag[i][1]

        # 가치가 현재 꺼낸 무게보다 작으면, 이전 값 복사
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else: # 가치가 현재 꺼낸 무게보다 크거나 같으면 이전 무게와, 이전 무게에서 꺼낸 무게 weight만큼 뺀 무게에 현재 꺼낸 가치 value를 더한 값과 비교
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

# for i in dp:
#     print(i)

print(dp[-1][-1])