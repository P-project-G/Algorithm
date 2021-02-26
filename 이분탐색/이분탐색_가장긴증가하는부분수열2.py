import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 최장증가부분수열 LIS
LIS = [arr[0]]

for i in arr:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        # lower bound 사용 이분탐색
        low, high = 0, len(LIS)-1
        while low < high :
            mid = (low+high)//2
            if LIS[mid] < i:
                low = mid+1
            elif LIS[mid] > i:
                high = mid
            else:
                low = high = mid
                break
        LIS[high] = i
print(len(LIS))


"""
dp풀이 하지만 시간초과
n = int(input())
dp = [1]*n

arr = list(map(int,input().split()))

for i in range (n):
    for j in range (i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
"""

"""
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	12955	5681	3898	45.220%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
"""